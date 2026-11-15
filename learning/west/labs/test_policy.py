# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""维护者回归：新建隔离实验，验证 P02～P05 的解析、Git 与策略边界。"""

import copy
import os
from pathlib import Path
import subprocess
import sys
import unittest
import uuid

import yaml


LABS = Path(__file__).resolve().parent
REPO = LABS.parents[2]


class PolicyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 每轮新建名称，不覆盖读者 textbook-01，也不复用先前测试的 Git 状态。
        name = "policy-" + uuid.uuid4().hex[:10]
        cls.workspace = REPO / "build/learning-tools/west" / name / "workspace"
        cls.env = os.environ.copy()
        for key in list(cls.env):
            if key.startswith("WEST_CONFIG_") or key in ("ZEPHYR_BASE", "PYTHONPATH", "PYTHONHOME"):
                cls.env.pop(key)
        cls.env["PYTHONUTF8"] = "1"
        cls.env["MSYS"] = cls.env.get("MSYS", "") + " noglob"
        cls.command(sys.executable, LABS / "seed_workspace.py", "--name", name, cwd=REPO)
        cls.command(sys.executable, LABS / "init_workspace.py", "-l", "manifest")
        # 只把本测试 west 子进程的配置路径指向新实验，隔离用户个人配置。
        cls.env["WEST_CONFIG_SYSTEM"] = str(cls.workspace.parent / "empty-system.ini")
        cls.env["WEST_CONFIG_GLOBAL"] = str(cls.workspace.parent / "empty-global.ini")
        cls.env["WEST_CONFIG_LOCAL"] = str(cls.workspace / ".west/config")
        cls.manifest_file = cls.workspace / "manifest/west.yml"
        cls.original = yaml.safe_load(cls.manifest_file.read_text(encoding="utf-8"))
        cls.original["manifest"]["projects"][1]["revision"] = "v2.0"
        cls.manifest_file.write_text(yaml.safe_dump(cls.original, sort_keys=False), encoding="utf-8")
        cls.command(sys.executable, "-m", "west", "update")
        cls.registry = cls.workspace / "manifest/west-commands.yml"
        cls.old_registry = cls.registry.read_text(encoding="utf-8")
        cls.new_registry = cls.old_registry + (
            "  - file: commands/repo_audit.py\n    commands:\n"
            "      - name: repo-audit\n        class: RepoAudit\n"
            "        help: Check team repository policy.\n")
        cls.source = cls.workspace / "libs/arithmetic/arithmetic.py"
        cls.source_bytes = cls.source.read_bytes()
        cls.log = cls.workspace.parent / "policy-evidence.log"
        print(f"Policy evidence: {cls.workspace}", flush=True)

    @classmethod
    def command(cls, *args, cwd=None, expected=0):
        # 不经 shell，固定目录和环境；预期失败同时核对退出码和各测试中的错误内容。
        result = subprocess.run([str(arg) for arg in args], cwd=cwd or cls.workspace,
                                env=cls.env, text=True, encoding="utf-8", errors="replace",
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if hasattr(cls, "log"):
            with cls.log.open("a", encoding="utf-8") as stream:
                stream.write(f"{args}\nexit={result.returncode}\n{result.stdout}\n")
        if (result.returncode == 0) != (expected == 0):
            raise AssertionError(f"Unexpected exit {result.returncode}: {args}\n{result.stdout}")
        return result.stdout.strip()

    def west(self, *args, expected=0):
        return self.command(sys.executable, "-m", "west", *args, expected=expected)

    def setUp(self):
        # 每个用例从同一份有效声明开始；业务 policy 是测试自己新增的数据。
        self.document = copy.deepcopy(self.original)
        self.project = self.document["manifest"]["projects"][1]
        self.policy = {"required-files": ["arithmetic.py"], "require-clean-tracked": True}
        self.project["userdata"] = {"team-policy": self.policy}
        self.registry.write_text(self.new_registry, encoding="utf-8")
        self.save()

    def save(self):
        self.manifest_file.write_text(yaml.safe_dump(self.document, sort_keys=False), encoding="utf-8")

    def tearDown(self):
        # 只恢复本次新建副本中已知的两个文件，保留全部证据供排查。
        self.source.write_bytes(self.source_bytes)
        self.command("git", "-C", self.workspace / "libs/arithmetic", "reset", "--", "arithmetic.py")
        self.west("config", "--local", "commands.allow_extensions", "true")

    def test_01_trace_update_and_git(self):
        output = self.west("-vv", "update", "--fetch=always", "arithmetic")
        for token in ("fetch", "update-ref", "checkout --detach", "libs", "arithmetic"):
            self.assertIn(token, output)
        self.assertIn("PASS arithmetic", self.west("-vv", "repo-audit", "arithmetic"))

    def test_02_effective_defaults(self):
        self.document["manifest"]["remotes"] = [{"name": "lab", "url-base": "../../../remotes"}]
        self.document["manifest"]["defaults"] = {"remote": "lab", "revision": "v1.0"}
        self.project.pop("url")
        self.save()
        # 同时证明原始字典没有 url，而 West Manifest API 对象已有有效 URL。
        self.assertIsNone(self.project.get("url"))
        output = self.command(sys.executable, "-c",
                              "from pathlib import Path; from west.manifest import Manifest; "
                              "p=Manifest.from_topdir(topdir=Path.cwd()).get_projects(['arithmetic'])[0]; "
                              "print(p.url, p.revision, p.path)")
        self.assertEqual(output, "../../../remotes/arithmetic v2.0 libs/arithmetic")

    def test_03_unknown_standard_field(self):
        before = self.command("git", "-C", "libs/arithmetic", "rev-parse", "HEAD")
        self.project["build-command"] = "echo hello"
        self.save()
        self.assertIsInstance(yaml.safe_load(self.manifest_file.read_text(encoding="utf-8")), dict)
        self.west("-vv", "manifest", "--validate", expected=1)
        # 1.5.0 的 CLI 此时可能只显示 manifest unavailable；直接调用解析器取原因。
        detail = self.command(sys.executable, "-c",
                              "from pathlib import Path; from west.manifest import Manifest; "
                              "Manifest.from_topdir(topdir=Path.cwd())", expected=1)
        self.assertIn("build-command", detail)
        self.assertEqual(before, self.command("git", "-C", "libs/arithmetic", "rev-parse", "HEAD"))

    def test_04_missing_file_is_not_update_policy(self):
        self.policy["required-files"] = ["missing.txt"]
        self.save()
        self.west("manifest", "--validate")
        self.west("update", "arithmetic")
        self.assertIn("cat-file", self.west("repo-audit", expected=1))

    def test_05_policy_types_and_spelling(self):
        cases = [(42, "team-policy must be a mapping"),
                 ({"required-files": 42}, "nonempty list"),
                 ({"required-files": []}, "nonempty list"),
                 ({"required-files": [42]}, "relative Git paths"),
                 ({"required-fiels": ["arithmetic.py"]}, "unknown team-policy key"),
                 ({"required-files": ["arithmetic.py"], "require-clean-tracked": "false"}, "boolean")]
        for policy, message in cases:
            with self.subTest(policy=policy):
                self.project["userdata"]["team-policy"] = policy
                self.save()
                self.west("manifest", "--validate")
                self.assertIn(message, self.west("repo-audit", expected=1))

    def test_06_path_boundaries(self):
        for name in ("../app/main.py", "/tmp/file", "C:/file", "dir\\file"):
            with self.subTest(name=name):
                self.policy["required-files"] = [name]
                self.save()
                self.assertIn("relative Git paths", self.west("repo-audit", expected=1))
        self.policy["required-files"] = ["."]
        self.save()
        self.assertIn("cat-file", self.west("repo-audit", expected=1))

    def test_07_dirty_worktree_and_staging(self):
        self.source.write_bytes(self.source_bytes + b"\n# test tracked change\n")
        self.assertIn("tracked changes", self.west("repo-audit", expected=1))
        self.command("git", "-C", "libs/arithmetic", "add", "arithmetic.py")
        self.assertIn("tracked changes", self.west("repo-audit", expected=1))
        self.assertIn("test tracked change", self.west("diff", "--cached", "arithmetic"))
        self.policy["require-clean-tracked"] = False
        self.save()
        self.assertIn("PASS arithmetic", self.west("repo-audit"))

    def test_08_select_projects_and_inactive(self):
        self.document["manifest"]["projects"][0]["userdata"] = {
            "team-policy": {"required-files": ["main.py"]}}
        self.save()
        self.assertIn("Audited 2", self.west("repo-audit"))
        self.assertIn("Audited 1", self.west("repo-audit", "app"))
        self.assertIn("active dependency", self.west("repo-audit", "guide", expected=1))
        self.assertIn("Unknown project", self.west("repo-audit", "absent", expected=1))

    def test_09_active_but_missing(self):
        guide = self.document["manifest"]["projects"][2]
        guide["userdata"] = {"team-policy": {"required-files": ["README.md"]}}
        self.document["manifest"]["group-filter"] = ["+docs"]
        self.save()
        self.assertIn("missing repository", self.west("repo-audit", "guide", expected=1))

    def test_10_empty_policy_does_not_pass(self):
        self.project.pop("userdata")
        self.save()
        self.assertIn("No active project", self.west("repo-audit", expected=1))

    def test_11_registration_and_enable_switch(self):
        self.assertIn("repo-audit", self.west("help", "repo-audit"))
        self.registry.write_text(self.old_registry, encoding="utf-8")
        self.west("repo-audit", expected=1)
        self.registry.write_text(self.new_registry, encoding="utf-8")
        self.west("config", "--local", "commands.allow_extensions", "false")
        self.west("repo-audit", expected=1)
        self.west("config", "--local", "commands.allow_extensions", "true")
        self.assertIn("PASS arithmetic", self.west("repo-audit"))

    def test_12_inert_config_and_builtin_queries(self):
        before = self.west("list", "-f", "{name}")
        self.west("config", "--local", "tutorial.message", "hello")
        self.assertEqual(self.west("config", "tutorial.message"), "hello")
        self.assertEqual(before, self.west("list", "-f", "{name}"))
        self.west("config", "--local", "-d", "tutorial.message")
        self.west("status", "arithmetic")
        self.west("diff", "arithmetic")
        self.west("compare", "arithmetic")
        output = self.west("forall", "arithmetic", "-c", "git rev-parse --show-toplevel")
        self.assertIn((self.workspace / "libs/arithmetic").as_posix(), output)
        self.assertIn("def add", self.west("grep", "--", "def add"))
        # west grep 消化底层的未匹配退出码 1；整体成功不代表有匹配。
        self.assertEqual(self.west("grep", "--", "no-such-token-781a6c"), "")


if __name__ == "__main__":
    # unittest 汇总每项结果并设置进程退出码；它不是 west 的加载入口。
    unittest.main(verbosity=2)
