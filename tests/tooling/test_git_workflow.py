# SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
# SPDX-License-Identifier: Apache-2.0
"""Exercise the actual Git hook and reject accidental configuration of a parent."""

import hashlib
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
    ".githooks/upstream/commit-msg",
    "scripts/git_setup.py",
    "governance/templates/git_commit_message.txt",
    "governance/templates/upstream/git_commit_message.txt",
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

    def test_hook_accepts_source_subjects_and_list_bodies(self):
        messages = (
            "docs: 补充使用说明\n\n- 说明初始化命令与输出目录\n",
            "feat(board/uyup): 增加启动配置\n\n- 指定目标芯片与板级默认值\n",
            "fix(时钟/配置)!: 修正频率\n\n- 采用12MHz外部晶振\n",
            "content(knowledge/kernel): 解释线程等待与唤醒\n\n- 对照可运行用例说明阻塞与就绪状态\n",
            "docs(repository/git): 补齐提交粒度规则\n\n- 独立治理政策与知识正文分别提交\n",
            "test(git): 验证提交钩子\n\n# 模板注释不会成为正文\n- 实际执行来源校验\n",
        )
        for message in messages:
            with self.subTest(subject=message.splitlines()[0]):
                self.commit_message(message, accepted=True)

    def test_hook_rejects_invalid_messages_without_committing(self):
        messages = (
            "docs: 只有标题\n",
            "feat(board/uyup): 只有空行\n\n\n",
            "docs: 只有注释\n\n# - 这不是实际正文\n",
            "docs: 只有空白明细\n\n-    \n",
            "update: 增加配置\n",
            "feat(board/uyup/uart): 增加串口\n",
            "feat(board uyup): 增加配置\n",
            "feat: add configuration\n",
            "feat: 增加配置\n正文没有使用列表\n",
            "feat: 增加配置\n\nAssisted-by: Agent:first\nAssisted-by: Agent:second\n",
            "feat: 增加配置\n\nAssisted-by: missing-model\n",
            "feat: 增加配置\n\nSigned-off-by: invalid\n",
            "feat: 增加配置\nAssisted-by: Agent:model\n",
            "feat: 增加配置\n\nAssisted-by: Agent:model\n\nSigned-off-by: Human <human@example.invalid>\n",
            "feat: 增加配置\n\nAssisted-by: Agent:model\n- 尾注后追加正文\n",
            "feat: 增加配置\n\nCo-authored-by: Agent <agent@example.invalid>\n",
            "docs: 补充工程介绍与Zephyr学习实验路线\n\n- 新增四篇工程入门介绍\n\nAssisted-by: Codex:gpt-6\n",
            "build(toolchain): 增加工具链检查\n\nSigned-off-by: Human Author <author@example.invalid>\n",
            "content: \n",
            "docs(repository:git): 更新规范\n",
            "docs(repository/git/extra): 更新规范\n",
            "docs: 更新规范\n\n- \n",
        )
        for message in messages:
            with self.subTest(message=message):
                self.commit_message(message, accepted=False)
        result = self.run_git("rev-parse", "--verify", "HEAD", expected=128)
        self.assertNotEqual(result.returncode, 0)

    def test_inherited_hook_and_template_match_source_baseline(self):
        expected_hashes = {
            ".githooks/upstream/commit-msg": "83b0c6db5d93ca5e3c11c7004094c96d29116f050ecd2c25c2d710b53690c78b",
            "governance/templates/upstream/git_commit_message.txt": "bee96272811082c7312b15322d641c43bc67ee5442c7f7c3231be1ffe90b5193",
        }
        for relative_path, expected_hash in expected_hashes.items():
            with self.subTest(path=relative_path):
                lines = (self.repo_root / relative_path).read_text(encoding="utf-8").splitlines(keepends=True)
                # 只去掉本项目补充的许可和来源注释，行为正文应与来源逐字一致。
                source = "".join(line for line in lines if not line.startswith((
                    "# SPDX-FileCopyrightText:", "# SPDX-License-Identifier:",
                    "# Inherited verbatim from linux-note ",
                )))
                self.assertEqual(hashlib.sha256(source.encode("utf-8")).hexdigest(), expected_hash)

    def test_project_requires_details_while_source_baseline_remains_unchanged(self):
        message = "docs: 补充工程说明\n"
        message_file = self.repo_root / ".git/source_message.txt"
        message_file.write_text(message, encoding="utf-8")
        self.run_command("sh", str(self.repo_root / ".githooks/upstream/commit-msg"),
                         str(message_file), cwd=self.repo_root)
        self.commit_message(message, accepted=False)

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
