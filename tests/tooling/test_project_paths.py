# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Prevent build commands from silently using a sibling Zephyr checkout."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


source = Path(__file__).resolve().parents[2] / "scripts/project.py"
spec = importlib.util.spec_from_file_location("hc32_project", source)
project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(project)


class ProjectPathTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="hc32-layout-")
        self.addCleanup(self.temporary.cleanup)
        self.storage = Path(self.temporary.name).resolve()
        self.repo = self.storage / "workspace/zephyr_hc32f4a0"
        for relative in ("VERSION", "CMakeLists.txt", "Kconfig", "scripts/twister"):
            path = self.repo / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("fixture\n")
        self.modules = []
        for name in ("cmsis_6", "hal_xhsc"):
            path = self.repo / project.LOCK[name]["source_path"]
            (path / "zephyr").mkdir(parents=True)
            (path / "zephyr/module.yml").write_text(f"name: {name}\n")
            self.modules.append(path)
        self.sdk = self.storage / f"zephyr-sdk-{project.LOCK['sdk']['version']}"
        self.sdk.mkdir()
        (self.sdk / "sdk_version").write_text(project.LOCK["sdk"]["version"])
        self.root_patch = patch.object(project, "ROOT", self.repo)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.env_patch = patch.dict(os.environ, {}, clear=True)
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

    def test_clone_uses_its_own_sources_without_siblings_or_west_workspace(self):
        env = project.environment()
        self.assertEqual(Path(env["ZEPHYR_BASE"]), self.repo)
        self.assertEqual(Path(env["ZEPHYR_SDK_INSTALL_DIR"]), self.sdk)
        self.assertEqual(env["ZEPHYR_MODULES"], ";".join(p.as_posix() for p in self.modules))
        self.assertFalse((self.repo.parent / "zephyr").exists())
        self.assertFalse((self.repo.parent / ".west").exists())

    def test_foreign_activated_environment_cannot_redirect_sources(self):
        os.environ.update({
            "ZEPHYR_BASE": str(self.storage / "foreign-zephyr"),
            "ZEPHYR_MODULES": str(self.storage / "foreign-cmsis"),
            "EXTRA_ZEPHYR_MODULES": str(self.storage / "foreign-extra"),
            "ZEPHYR_EXTRA_MODULES": str(self.storage / "legacy-extra"),
        })
        env = project.environment()
        self.assertEqual(Path(env["ZEPHYR_BASE"]), self.repo)
        self.assertEqual(env["ZEPHYR_MODULES"], ";".join(p.as_posix() for p in self.modules))
        self.assertNotIn("EXTRA_ZEPHYR_MODULES", env)
        self.assertNotIn("ZEPHYR_EXTRA_MODULES", env)

    def test_missing_local_source_does_not_fall_back_to_activated_checkout(self):
        (self.repo / "VERSION").unlink()
        os.environ["ZEPHYR_BASE"] = str(source.parents[1])
        with self.assertRaisesRegex(RuntimeError, "missing Zephyr source"):
            project.environment()

    def test_missing_vendored_dependency_is_an_error(self):
        (self.modules[0] / "zephyr/module.yml").unlink()
        with self.assertRaisesRegex(RuntimeError, "Missing vendored cmsis_6"):
            project.environment()

    def test_explicit_sdk_is_supported(self):
        alternate = self.storage / "custom sdk"
        alternate.mkdir()
        (alternate / "sdk_version").write_text(project.LOCK["sdk"]["version"])
        os.environ["ZEPHYR_SDK_INSTALL_DIR"] = str(alternate)
        self.assertEqual(Path(project.environment()["ZEPHYR_SDK_INSTALL_DIR"]), alternate)

    def test_build_output_cannot_escape_build_directory(self):
        for path in ("../soc", "../..", ".", str(self.storage / "external")):
            with self.subTest(path=path), self.assertRaisesRegex(RuntimeError, "outside"):
                project.build_path(path)

    def test_hardware_and_simulation_builds_use_separate_outputs(self):
        with patch.object(project, "run") as run:
            project.main(["build"])
            hc32_commands = [call.args[0] for call in run.call_args_list]
            run.reset_mock()
            project.main(["build", "--board", project.SIMULATION_BOARD, "--pristine"])
            simulation_commands = [call.args[0] for call in run.call_args_list]
        hc32_configure = hc32_commands[0]
        simulation_configure = simulation_commands[0]
        self.assertIn(f"-DBOARD={project.HC32_BOARD}", hc32_configure)
        self.assertEqual(hc32_configure[hc32_configure.index("-B") + 1],
                         self.repo / "build/bringup")
        self.assertEqual(simulation_configure[simulation_configure.index("-B") + 1],
                         self.repo / "build/mps2")
        self.assertIn("--fresh", simulation_configure)
        self.assertEqual(hc32_commands[1], ["cmake", "--build", self.repo / "build/bringup"])
        self.assertEqual(hc32_commands[2], [
            project.sys.executable, self.repo / "scripts/verify_hc32_image.py",
            "--build-dir", self.repo / "build/bringup",
        ])
        self.assertEqual(len(simulation_commands), 2)
        self.assertEqual(simulation_commands[1], ["cmake", "--build", self.repo / "build/mps2"])
        zephyr_dir = (self.repo / "share/zephyr-package/cmake").as_posix()
        self.assertIn(f"-DZephyr_DIR={zephyr_dir}", hc32_configure)
        python_path = Path(project.sys.executable).as_posix()
        self.assertIn(f"-DPython3_EXECUTABLE={python_path}", hc32_configure)
        for command in (hc32_configure, simulation_configure):
            for argument in command:
                if isinstance(argument, str) and argument.startswith("-D"):
                    # CMake later evaluates these strings for generated targets.
                    self.assertNotIn("\\", argument)

    def test_failed_compilation_does_not_validate_a_stale_image(self):
        error = project.subprocess.CalledProcessError(1, ["cmake", "--build"])
        with patch.object(project, "run", side_effect=[None, error]) as run:
            with self.assertRaises(project.subprocess.CalledProcessError):
                project.main(["build"])
        self.assertEqual(run.call_count, 2)

    def test_image_validation_failure_is_a_build_failure(self):
        error = project.subprocess.CalledProcessError(1, ["verify_hc32_image.py"])
        with patch.object(project, "run", side_effect=[None, None, error]):
            with self.assertRaises(project.subprocess.CalledProcessError):
                project.main(["build"])

    def test_twister_uses_in_repository_entrypoint(self):
        with patch.object(project, "run") as run:
            project.main(["test"])
        command = run.call_args.args[0]
        self.assertEqual(command[1], self.repo / "scripts/twister")
        self.assertNotIn("west", command)
        self.assertIn(self.repo / "build/twister", command)
        self.assertEqual(Path(run.call_args.kwargs["env"]["ZEPHYR_BASE"]), self.repo)


if __name__ == "__main__":
    unittest.main()
