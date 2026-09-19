# SPDX-License-Identifier: Apache-2.0
"""Verify per-checkout environment selection and safe west configuration."""
import configparser
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


envtool = load("project_env")
westtool = load("configure_west")


class ProjectEnvironmentTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="project-env-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve() / "checkout"
        self.root.mkdir()
        self.sdk = self.root / "sdk"
        self.sdk.mkdir()
        (self.sdk / "sdk_version").write_text("1.0.1")
        (self.root / ".local").mkdir()
        (self.root / ".local/environment.json").write_text(json.dumps({"sdk_root": str(self.sdk)}))
        (self.root / "dependencies.lock.json").write_text(json.dumps({
            "sdk": {"version": "1.0.1"},
            "cmsis_6": {"source_path": "modules/hal/cmsis_6"},
            "hal_xhsc": {"source_path": "modules/hal/xhsc"},
        }))
        python = envtool.python_path(self.root)
        python.parent.mkdir(parents=True)
        python.touch()

    def test_foreign_venv_and_module_variables_do_not_redirect_checkout(self):
        with patch.object(envtool, "windows_paths", return_value=[]):
            env = envtool.environment(self.root, {"VIRTUAL_ENV": "foreign",
                "PYTHONPATH": "foreign", "EXTRA_ZEPHYR_MODULES": "foreign", "PATH": ""})
        self.assertEqual(env["VIRTUAL_ENV"], str(self.root / ".venv"))
        self.assertEqual(env["ZEPHYR_BASE"], str(self.root))
        self.assertNotIn("PYTHONPATH", env)
        self.assertNotIn("EXTRA_ZEPHYR_MODULES", env)
        self.assertTrue(env["PATH"].startswith(str(envtool.python_path(self.root).parent)))

    def test_no_shared_environment_fallback(self):
        envtool.python_path(self.root).unlink()
        with self.assertRaisesRegex(RuntimeError, ".venv"):
            envtool.environment(self.root, {"VIRTUAL_ENV": "shared"})

    def test_wrong_sdk_version_fails(self):
        (self.sdk / "sdk_version").write_text("wrong")
        with self.assertRaisesRegex(RuntimeError, "SDK"):
            envtool.environment(self.root, {})

    def test_west_configuration_is_relative_and_idempotent(self):
        (self.root / "project-west.yml").write_text("manifest: {}")
        westtool.configure(self.root)
        config = self.root.parent / ".west/config"
        original = config.read_bytes()
        westtool.configure(self.root)
        self.assertEqual(config.read_bytes(), original)
        parsed = configparser.ConfigParser()
        parsed.read(config)
        self.assertEqual(parsed["manifest"]["path"], self.root.name)
        self.assertEqual(parsed["manifest"]["file"], "project-west.yml")

    def test_foreign_west_configuration_is_not_overwritten(self):
        (self.root / "project-west.yml").write_text("manifest: {}")
        (self.root.parent / ".west").mkdir()
        config = self.root.parent / ".west/config"
        config.write_text("[manifest]\npath=other\nfile=west.yml\n")
        before = config.read_bytes()
        with self.assertRaisesRegex(RuntimeError, "another layout"):
            westtool.configure(self.root)
        self.assertEqual(config.read_bytes(), before)

    def test_workspace_cannot_be_git_root(self):
        (self.root.parent / ".git").mkdir()
        with self.assertRaisesRegex(RuntimeError, "must not itself"):
            westtool.configure(self.root)

    def test_nested_workspace_is_not_overwritten(self):
        (self.root / ".west").mkdir()
        with self.assertRaisesRegex(RuntimeError, "not a supported layout"):
            westtool.configure(self.root)
        self.assertFalse((self.root.parent / ".west").exists())
