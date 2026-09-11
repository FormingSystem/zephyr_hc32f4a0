# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Guard learning input boundaries and distinguish running from building."""

import importlib.util
import json
import os
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[2] / "scripts/learning/run.py"
SPEC = importlib.util.spec_from_file_location("learning_runner", SOURCE)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class LearningRunnerTest(unittest.TestCase):
    def test_external_and_parent_applications_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            app = root / "tests/learning/probe"
            app.mkdir(parents=True)
            (app / "CMakeLists.txt").write_text("# fixture\n")
            with patch.object(runner.project, "ROOT", root):
                self.assertEqual(runner.application_path("tests/learning/probe"), app)
                for value in ("../zephyr", "tests/learning", "samples/bringup", "tests/learning/../.."):
                    with self.subTest(value=value), self.assertRaises(RuntimeError):
                        runner.application_path(value)

    def test_extra_configuration_cannot_escape_application(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            app = root / "app"
            app.mkdir()
            (root / "foreign.conf").write_text("CONFIG_TEST=y\n")
            (app / "fail.conf").write_text("CONFIG_TEST=y\n")
            self.assertEqual(runner.extra_config(app.resolve(), "fail.conf"), app.resolve() / "fail.conf")
            with self.assertRaises(RuntimeError):
                runner.extra_config(app.resolve(), "../foreign.conf")

    def test_zero_filtered_skipped_and_built_only_do_not_pass(self):
        reports = [
            {}, {"testsuites": []},
            {"testsuites": [{"runnable": False, "status": "passed", "testcases": [
                {"status": "passed"}]}]},
            {"testsuites": [{"runnable": True, "status": "filtered", "testcases": []}]},
            {"testsuites": [{"runnable": True, "status": "passed", "testcases": [
                {"status": "skipped"}]}]},
            {"testsuites": [{"runnable": True, "status": "passed", "testcases": []}]},
        ]
        for report in reports:
            with self.subTest(report=report):
                self.assertFalse(runner.report_summary(report)["all_executed_and_passed"])

    def test_all_executed_cases_required(self):
        report = {"testsuites": [{"runnable": True, "status": "passed", "testcases": [
            {"status": "passed"}, {"status": "passed"}]}]}
        self.assertEqual(runner.report_summary(report), {
            "suites": 1, "cases": 2, "passed": 2, "all_executed_and_passed": True,
        })
        report["testsuites"][0]["testcases"][1]["status"] = "failed"
        self.assertFalse(runner.report_summary(report)["all_executed_and_passed"])

    @staticmethod
    def process_running(pid):
        if os.name == "nt":
            import ctypes
            from ctypes import wintypes
            kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            kernel.OpenProcess.restype = wintypes.HANDLE
            kernel.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
            kernel.CloseHandle.argtypes = [wintypes.HANDLE]
            handle = kernel.OpenProcess(0x00100000, False, pid)
            if not handle:
                return False
            try:
                return kernel.WaitForSingleObject(handle, 0) == 0x102
            finally:
                kernel.CloseHandle(handle)
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        # A terminated orphan may remain as a zombie until the system reaps it.
        status = Path(f"/proc/{pid}/stat")
        if status.exists():
            return status.read_text().rsplit(")", 1)[1].split()[0] != "Z"
        return True

    def test_timeout_stops_real_parent_and_child_processes(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory).resolve()
            evidence = {"commands": []}
            marker = destination / "child.pid"
            child = ("import os,sys,time; from pathlib import Path; "
                     "Path(sys.argv[1]).write_text(str(os.getpid())); time.sleep(60)")
            parent = ("import subprocess,sys,time; "
                      "subprocess.Popen([sys.executable, '-c', sys.argv[1], sys.argv[2]]); "
                      "time.sleep(60)")
            try:
                with patch.object(runner.project, "ROOT", destination):
                    with self.assertRaisesRegex(RuntimeError, "exceeded"):
                        runner.execute([sys.executable, "-c", parent, child, str(marker)],
                                       os.environ.copy(), destination, evidence, 2)
                self.assertTrue(marker.is_file(), "Child must actually start before timeout")
                child_pid = int(marker.read_text())
                deadline = time.monotonic() + 3
                while self.process_running(child_pid) and time.monotonic() < deadline:
                    time.sleep(0.05)
                self.assertFalse(self.process_running(child_pid))
                self.assertFalse(self.process_running(evidence["commands"][0]["pid"]))
            finally:
                # Only test-created PIDs may be cleaned up if an assertion fails.
                if marker.is_file():
                    child_pid = int(marker.read_text())
                    if self.process_running(child_pid):
                        if os.name == "nt":
                            subprocess.run(["taskkill", "/PID", str(child_pid), "/T", "/F"],
                                           capture_output=True, timeout=10, check=False)
                        else:
                            os.kill(child_pid, 9)
            self.assertEqual(evidence["commands"][0]["exit_code"], 124)
            self.assertTrue(evidence["commands"][0]["timed_out"])
            self.assertTrue(evidence["commands"][0]["process_tree_stopped"])

    @staticmethod
    def application_fixture(root):
        app = root / "tests/learning/probe"
        app.mkdir(parents=True)
        (app / "CMakeLists.txt").write_text("# fixture\n")
        return app

    def test_setup_failure_replaces_previous_success_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            self.application_fixture(root)
            index = root / "build/learning/tests/probe/mps2_an386/normal/latest.json"
            index.parent.mkdir(parents=True)
            index.write_text('{"success": true, "evidence": "old"}')
            with patch.object(runner.project, "ROOT", root), \
                    patch.object(runner.project, "environment", side_effect=RuntimeError("SDK missing")):
                self.assertEqual(runner.main(["build", "--app", "tests/learning/probe"]), 1)
            latest = json.loads(index.read_text())
            self.assertFalse(latest["success"])
            evidence = json.loads((root / latest["evidence"]).read_text())
            self.assertEqual(evidence["state"], "failed")
            self.assertIn("SDK missing", evidence["error"])

    def test_successful_commands_without_elf_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            self.application_fixture(root)
            environment = {"ZEPHYR_BASE": root.as_posix(), "ZEPHYR_MODULES": ""}
            with patch.object(runner.project, "ROOT", root), \
                    patch.object(runner.project, "environment", return_value=environment), \
                    patch.object(runner, "source_identity", return_value={}), \
                    patch.object(runner, "toolchain_identity", return_value=root / "gcc"), \
                    patch.object(runner, "execute", return_value=None) as execute:
                self.assertEqual(runner.main(["build", "--app", "tests/learning/probe"]), 1)
                self.assertEqual(execute.call_count, 2)
            latest = json.loads((root / "build/learning/tests/probe/mps2_an386/normal/latest.json").read_text())
            evidence = json.loads((root / latest["evidence"]).read_text())
            self.assertFalse(latest["success"])
            self.assertIn("artifact is missing", evidence["error"])

    def test_image_identity_checks_application_board_and_compiler(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            app = self.application_fixture(root)
            build = root / "build/firmware"
            (build / "zephyr").mkdir(parents=True)
            header = bytearray(52)
            header[:6] = b"\x7fELF\x01\x01"
            struct.pack_into("<HH", header, 16, 2, 40)
            (build / "zephyr/zephyr.elf").write_bytes(header)
            (build / "zephyr/.config").write_text('CONFIG_BOARD_TARGET="mps2/an386"\n')
            compiler = root / "sdk/gcc"
            cache = {"CMAKE_HOME_DIRECTORY": app.as_posix(), "ZEPHYR_BASE": root.as_posix(),
                     "CMAKE_C_COMPILER": compiler.as_posix(), "BOARD": "mps2/an386"}

            def write_cache(values):
                (build / "CMakeCache.txt").write_text(
                    "".join(f"{key}:STRING={value}\n" for key, value in values.items()))

            write_cache(cache)
            with patch.object(runner.project, "ROOT", root):
                self.assertEqual(runner.audit_build(build, app, "mps2/an386", compiler)["board"], "mps2/an386")
                for key in cache:
                    with self.subTest(key=key):
                        write_cache({**cache, key: (root.parent / "foreign").as_posix()})
                        with self.assertRaises(RuntimeError):
                            runner.audit_build(build, app, "mps2/an386", compiler)

    def test_sdk_version_is_observed_before_it_is_compared(self):
        with tempfile.TemporaryDirectory() as directory:
            sdk = Path(directory)
            (sdk / "sdk_version").write_text("unexpected-version\n")
            evidence = {"commands": []}
            with self.assertRaisesRegex(RuntimeError, "differs"):
                runner.toolchain_identity({"ZEPHYR_SDK_INSTALL_DIR": str(sdk)}, sdk, evidence, 1)
            self.assertEqual(evidence["sdk"], "unexpected-version")
            self.assertEqual(evidence["commands"], [])

    def test_untracked_shared_input_has_a_content_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            app = self.application_fixture(root)
            script = root / "scripts/learning/run.py"
            script.parent.mkdir(parents=True)
            script.write_text("# script fixture\n")
            (root / "scripts/project.py").write_text("# project fixture\n")
            (root / "dependencies.lock.json").write_text("{}\n")
            shared = root / "new_shared.h"
            shared.write_text("#define SHARED_VALUE 1\n")

            def git_output(command, **kwargs):
                if command[1] == "rev-parse":
                    return "test-head\n"
                if command[1] == "diff":
                    return b""
                if command[1] == "status":
                    return "?? new_shared.h\n"
                if command[1] == "ls-files":
                    self.assertIn("--exclude-standard", command)
                    return b"new_shared.h\0"
                self.fail(f"Unexpected Git call: {command}")

            with patch.object(runner.project, "ROOT", root), \
                    patch.object(runner, "__file__", str(script)), \
                    patch.object(runner.subprocess, "check_output", side_effect=git_output):
                before = runner.source_identity(app)
                shared.write_text("#define SHARED_VALUE 2\n")
                after = runner.source_identity(app)
            self.assertEqual(before["tracked_diff_sha256"], after["tracked_diff_sha256"])
            self.assertNotEqual(before["input_sha256"]["new_shared.h"],
                                after["input_sha256"]["new_shared.h"])


if __name__ == "__main__":
    unittest.main()
