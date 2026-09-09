# SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
# SPDX-License-Identifier: Apache-2.0
"""Exercise the actual Git hook and reject accidental configuration of a parent."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


project_root = Path(__file__).resolve().parents[2]
framework_files = (
    ".githooks/commit-msg",
    "scripts/check_commit_message.py",
    "scripts/git_setup.py",
    "governance/templates/git_commit_message.txt",
)


class git_workflow_test(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(prefix="hc32_git_")
        self.addCleanup(self.temporary_directory.cleanup)
        self.repo_root = Path(self.temporary_directory.name) / "test repo"
        self.repo_root.mkdir()
        self.environment = {
            name: value for name, value in os.environ.items() if not name.startswith("GIT_")
        }
        self.environment.update(
            GIT_CONFIG_NOSYSTEM="1",
            GIT_CONFIG_GLOBAL=os.devnull,
            GIT_TERMINAL_PROMPT="0",
            PYTHONUTF8="1",
            VIRTUAL_ENV="",
        )
        self.environment["PATH"] = str(Path(sys.executable).parent) + os.pathsep + os.environ["PATH"]
        self.run_command("git", "init", "-b", "master", str(self.repo_root))
        for relative_path in framework_files:
            destination = self.repo_root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(project_root / relative_path, destination)
        (self.repo_root / ".githooks/commit-msg").chmod(0o755)
        self.run_git("config", "user.name", "Hook Test")
        self.run_git("config", "user.email", "hook@example.invalid")
        self.run_setup()

    def run_command(self, *arguments, expected=0, cwd=None):
        result = subprocess.run(
            arguments,
            cwd=cwd,
            env=self.environment,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def run_git(self, *arguments, expected=0):
        return self.run_command("git", "-C", str(self.repo_root), *arguments, expected=expected)

    def run_setup(self, *arguments, expected=0):
        return self.run_command(
            sys.executable,
            str(self.repo_root / "scripts/git_setup.py"),
            *arguments,
            expected=expected,
        )

    def commit_message(self, message, accepted):
        message_file = self.repo_root / ".git/test_commit_message.txt"
        message_file.write_text(message, encoding="utf-8", newline="\n")
        return self.run_git(
            "commit", "--allow-empty", "--file", str(message_file), expected=0 if accepted else 1
        )

    def test_hook_accepts_supported_subjects_and_trailers(self):
        messages = (
            "docs: 补充使用说明\n",
            "feat(board/uyup): 增加启动配置\n",
            "fix(时钟/配置)!: 修正频率\n\n- 采用12MHz外部晶振\n",
            "build(toolchain): 增加工具链检查\n\nSigned-off-by: Human Author <author@example.invalid>\n",
            "test(git): 验证提交钩子\n\n- 实际执行提交校验\n\nAssisted-by: TestAgent:test-model\n",
            "docs: 补充检查步骤\n\nAssisted-by: TestAgent:test-model checker\nSigned-off-by: Human Author <author@example.invalid>\n",
        )
        for message in messages:
            with self.subTest(subject=message.splitlines()[0]):
                self.commit_message(message, accepted=True)

    def test_hook_rejects_invalid_messages_without_committing(self):
        messages = (
            "update: 增加配置\n",
            "feat(board/uyup/uart): 增加串口\n",
            "feat(board uyup): 增加配置\n",
            "feat: add configuration\n",
            "feat: café\n",
            "feat: ✅\n",
            "feat: 增加配置\n正文没有使用列表\n",
            "feat: 增加配置\n\nAssisted-by: Agent:first\nAssisted-by: Agent:second\n",
            "feat: 增加配置\n\nAssisted-by: missing-model\n",
            "feat: 增加配置\n\nSigned-off-by: invalid\n",
            "feat: 增加配置\nAssisted-by: Agent:model\n",
            "feat: 增加配置\n\nAssisted-by: Agent:model\n\nSigned-off-by: Human <human@example.invalid>\n",
            "feat: 增加配置\n\nAssisted-by: Agent:model\n- 尾注后追加正文\n",
            "feat: 增加配置\n\nCo-authored-by: Agent <agent@example.invalid>\n",
        )
        for message in messages:
            with self.subTest(message=message):
                self.commit_message(message, accepted=False)
        result = self.run_git("rev-parse", "--verify", "HEAD", expected=128)
        self.assertNotEqual(result.returncode, 0)

    def test_setup_is_idempotent_and_preserves_identity_and_remote(self):
        self.run_git("remote", "add", "origin", "https://example.invalid/unchanged.git")
        self.run_setup()
        first_config = (self.repo_root / ".git/config").read_bytes()
        self.run_setup()
        self.assertEqual(first_config, (self.repo_root / ".git/config").read_bytes())
        self.run_setup("--check")
        self.assertEqual(self.run_git("config", "user.name").stdout.strip(), "Hook Test")
        self.assertEqual(self.run_git("remote", "get-url", "origin").stdout.strip(), "https://example.invalid/unchanged.git")

    def test_check_reports_missing_setting_without_writing(self):
        self.run_git("config", "--unset", "pull.ff")
        before = (self.repo_root / ".git/config").read_bytes()
        result = self.run_setup("--check", expected=1)
        self.assertIn("pull.ff", result.stdout)
        self.assertEqual(before, (self.repo_root / ".git/config").read_bytes())

    def test_setup_does_not_configure_enclosing_repository(self):
        child_root = self.repo_root / "child"
        (child_root / "scripts").mkdir(parents=True)
        shutil.copyfile(project_root / "scripts/git_setup.py", child_root / "scripts/git_setup.py")
        before = (self.repo_root / ".git/config").read_bytes()
        result = self.run_command(
            sys.executable, str(child_root / "scripts/git_setup.py"), expected=1
        )
        self.assertIn(".git", result.stderr)
        self.assertEqual(before, (self.repo_root / ".git/config").read_bytes())


if __name__ == "__main__":
    unittest.main()
