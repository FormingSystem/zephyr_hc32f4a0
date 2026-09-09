# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Guard the separate project and Zephyr dependency roots."""

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
        self.workspace = self.storage / "workspace"
        self.repo = self.workspace / "zephyr_hc32f4a0"
        self.repo.mkdir(parents=True)
        self.zephyr = self.workspace / "zephyr"
        self.create_zephyr(self.zephyr)
        self.sdk = self.storage / f"zephyr-sdk-{project.LOCK['sdk']['version']}"
        self.sdk.mkdir()
        (self.sdk / "sdk_version").write_text(project.LOCK["sdk"]["version"])
        self.root_patch = patch.object(project, "ROOT", self.repo)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.env_patch = patch.dict(os.environ, {}, clear=True)
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

    @staticmethod
    def create_zephyr(path):
        path.mkdir(parents=True, exist_ok=True)
        (path / "VERSION").write_text("VERSION_MAJOR = 4\n")
        (path / "west.yml").write_text("manifest: {}\n")

    def test_dependency_is_sibling_even_when_parent_has_markers(self):
        self.create_zephyr(self.workspace)
        env = project.environment()
        self.assertEqual(Path(env["ZEPHYR_BASE"]), self.zephyr)
        self.assertEqual(Path(env["ZEPHYR_SDK_INSTALL_DIR"]), self.sdk)
        self.assertEqual(env["EXTRA_ZEPHYR_MODULES"], str(self.repo))
        self.assertEqual(project.build_path("bringup"), self.repo / "build/bringup")

    def test_missing_sibling_does_not_fall_back_to_parent(self):
        self.create_zephyr(self.workspace)
        (self.zephyr / "west.yml").unlink()
        with self.assertRaisesRegex(RuntimeError, "ZEPHYR_BASE"):
            project.environment()

    def test_explicit_dependencies_and_extra_modules_are_preserved(self):
        external_zephyr = self.storage / "external/zephyr"
        self.create_zephyr(external_zephyr)
        external_module = self.storage / "other-module"
        external_module.mkdir()
        os.environ.update({
            "ZEPHYR_BASE": str(external_zephyr),
            "ZEPHYR_SDK_INSTALL_DIR": str(self.sdk),
            "EXTRA_ZEPHYR_MODULES": f"{self.repo};{external_module};{self.repo}",
        })
        env = project.environment()
        self.assertEqual(Path(env["ZEPHYR_BASE"]), external_zephyr)
        self.assertEqual(env["EXTRA_ZEPHYR_MODULES"], f"{self.repo};{external_module}")

    def test_build_output_cannot_escape_repository(self):
        with self.assertRaisesRegex(RuntimeError, "outside this repository"):
            project.build_path("../..")

    def test_reactivation_removes_only_the_misplaced_checkout(self):
        misplaced = self.zephyr / "_hc32f4a0"
        other_module = self.storage / "other-module"
        other_module.mkdir()
        os.environ["EXTRA_ZEPHYR_MODULES"] = f"{misplaced};{other_module};{self.repo}"
        os.environ["ZEPHYR_EXTRA_MODULES"] = f"{other_module};{misplaced}"
        env = project.environment()
        self.assertEqual(env["EXTRA_ZEPHYR_MODULES"], f"{self.repo};{other_module}")
        self.assertEqual(env["ZEPHYR_EXTRA_MODULES"], str(other_module))


if __name__ == "__main__":
    unittest.main()
