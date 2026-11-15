# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Keep object-experiment failures current and terminate timed-out tool trees."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[2] / "scripts/learning/inspect_objects.py"
SPEC = importlib.util.spec_from_file_location("learning_objects", SOURCE)
objects = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(objects)


class LearningObjectsTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.output = self.root / "build/learning/compilation"
        self.output.mkdir(parents=True)
        for name, value in (("ROOT", self.root), ("OUTPUT", self.output)):
            patcher = patch.object(objects, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def previous_success(self):
        (self.output / "report.json").write_text('{"status": "PASS"}')
        (self.output / "commands.json").write_text('[{"exit_code": 0}]')
        (self.output / "previous-artifact.txt").write_text("retain prior output")

    def assert_setup_failed(self, message):
        report = json.loads((self.output / "report.json").read_text())
        self.assertEqual(report["status"], "FAIL")
        self.assertIn(message, report["error"])
        self.assertEqual(json.loads((self.output / "commands.json").read_text()), [])
        self.assertTrue((self.output / "previous-artifact.txt").is_file())

    def test_missing_sdk_replaces_previous_success(self):
        self.previous_success()
        with patch.dict(os.environ, {"ZEPHYR_SDK_INSTALL_DIR": ""}):
            self.assertEqual(objects.main([]), 1)
        self.assert_setup_failed("provide --sdk")

    def test_missing_sdk_tool_replaces_previous_success(self):
        self.previous_success()
        self.assertEqual(objects.main(["--sdk", str(self.root / "missing-sdk")]), 1)
        self.assert_setup_failed("Missing ARM SDK tool")

    def test_missing_executable_is_recorded_as_failure(self):
        commands = []
        with self.assertRaises(OSError):
            objects.run_command([self.root / "missing-tool"], self.output / "missing.log", commands)
        recorded = json.loads((self.output / "commands.json").read_text())
        self.assertIsNone(recorded[0]["exit_code"])
        self.assertIn("error", recorded[0])

    def test_expected_link_failure_requires_its_specific_error(self):
        for code, message, accepted in ((1, "undefined reference to `g_bias'", True),
                                        (1, "different compiler failure", False),
                                        (0, "undefined reference to `g_bias'", False)):
            with self.subTest(code=code, message=message):
                command = [sys.executable, "-c", "import sys; print(sys.argv[1]); "
                           "sys.exit(int(sys.argv[2]))", message, str(code)]
                if accepted:
                    self.assertIn("g_bias", objects.run_command(
                        command, self.output / "link.log", [], expected_failure=True))
                else:
                    with self.assertRaisesRegex(RuntimeError, "Expected unresolved"):
                        objects.run_command(command, self.output / "link.log", [], expected_failure=True)

    def test_failure_during_experiment_publishes_failure(self):
        self.previous_success()
        with patch.object(objects, "inspect", side_effect=RuntimeError("compile failed")):
            self.assertEqual(objects.main(["--sdk", str(self.root)]), 1)
        self.assert_setup_failed("compile failed")

    def test_unconfirmed_cleanup_is_recorded(self):
        commands = []
        with patch.object(objects.subprocess, "Popen") as popen, \
                patch.object(objects, "stop_process_tree", side_effect=RuntimeError("cleanup failed")):
            popen.return_value.pid = 1234
            popen.return_value.wait.side_effect = subprocess.TimeoutExpired("tool", 1)
            with self.assertRaisesRegex(RuntimeError, "exceeded"):
                objects.run_command(["tool"], self.output / "timeout.log", commands, timeout=1)
        self.assertIn("cleanup failed", commands[0]["cleanup_error"])
        self.assertNotIn("process_tree_stopped", commands[0])

    def test_timeout_stops_tool_and_descendant_even_for_expected_failure(self):
        # Reuse the platform-neutral liveness check, not the runner's tests.
        from test_learning_runner import LearningRunnerTest

        commands = []
        marker = self.output / "child.pid"
        child = ("import os,sys,time; from pathlib import Path; "
                 "Path(sys.argv[1]).write_text(str(os.getpid())); "
                 "print('undefined reference to g_bias', flush=True); time.sleep(60)")
        parent = ("import subprocess,sys,time; "
                  "subprocess.Popen([sys.executable, '-c', sys.argv[1], sys.argv[2]]); "
                  "time.sleep(60)")
        try:
            with self.assertRaisesRegex(RuntimeError, "exceeded"):
                objects.run_command([sys.executable, "-c", parent, child, marker],
                                    self.output / "timeout.log", commands,
                                    expected_failure=True, timeout=2)
            self.assertTrue(marker.is_file(), "The descendant must start before the timeout")
            child_pid = int(marker.read_text())
            deadline = time.monotonic() + 3
            while LearningRunnerTest.process_running(child_pid) and time.monotonic() < deadline:
                time.sleep(0.05)
            self.assertFalse(LearningRunnerTest.process_running(child_pid))
            self.assertFalse(LearningRunnerTest.process_running(commands[0]["pid"]))
        finally:
            if marker.is_file():
                child_pid = int(marker.read_text())
                if LearningRunnerTest.process_running(child_pid):
                    if os.name == "nt":
                        subprocess.run(["taskkill", "/PID", str(child_pid), "/T", "/F"],
                                       capture_output=True, timeout=10, check=False)
                    else:
                        os.kill(child_pid, 9)
        self.assertEqual(commands[0]["exit_code"], 124)
        self.assertTrue(commands[0]["timed_out"])
        self.assertTrue(commands[0]["process_tree_stopped"])


if __name__ == "__main__":
    unittest.main()
