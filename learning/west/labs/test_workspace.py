# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""在指定实验工作区只读验收；不替读者执行 init、update 或修复。"""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import unittest


class WorkspaceTest(unittest.TestCase):
    workspace = None
    revision = None
    docs = False

    def run_command(self, *args):
        # 参数列表直接启动进程，cwd 固定为验收目标；合并输出便于断言失败诊断。
        result = subprocess.run(args, cwd=self.workspace, text=True,
                                encoding="utf-8", errors="replace",
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertEqual(result.returncode, 0, result.stdout)
        return result.stdout.strip()

    def west(self, *args):
        # 复用运行测试的解释器，避免 PATH 上另一套 west 干扰验收。
        return self.run_command(sys.executable, "-m", "west", *args)

    def test_workspace_identity(self):
        # 先比物理 .west 文件，再核对 west 自己发现的位置。
        self.assertTrue((self.workspace / ".west" / "config").is_file(),
                        "此目录尚未初始化；先检查当前位置，再执行手册的 init 步骤")
        self.assertEqual(Path(self.west("topdir")).resolve(), self.workspace)
        self.assertEqual(self.west("config", "manifest.path"), "manifest")

    def test_active_projects_are_cloned(self):
        # inventory 是教材扩展；通过其 JSON 输出验证选择规则和克隆状态。
        rows = json.loads(self.west("inventory", "--format", "json", "--require-cloned"))
        names = {row["name"] for row in rows}
        self.assertTrue({"app", "arithmetic"}.issubset(names), rows)
        self.assertEqual("guide" in names, self.docs, rows)
        self.assertTrue(all(row["cloned"] for row in rows), rows)

    def test_arithmetic_revision(self):
        # 声明、实际 HEAD、同步引用分别查询，不能仅凭 YAML 声明判定成功。
        wanted = self.west("list", "arithmetic", "-f", "{revision}")
        expected = self.run_command("git", "-C", "libs/arithmetic", "rev-parse",
                                    self.revision + "^{commit}")
        declared = self.run_command("git", "-C", "libs/arithmetic", "rev-parse",
                                    wanted + "^{commit}")
        actual = self.run_command("git", "-C", "libs/arithmetic", "rev-parse", "HEAD")
        tracked = self.run_command("git", "-C", "libs/arithmetic", "rev-parse", "manifest-rev")
        self.assertEqual(actual, expected, "清单已改但实际源码未同步，或仍在本地开发提交")
        self.assertEqual(declared, expected, "清单与验收版本不符；确认 arithmetic 条目")
        self.assertEqual(tracked, expected)

    def test_application_behavior(self):
        # -B 不生成字节码缓存；执行应用与 v2 新接口验证代码实际可用。
        self.assertEqual(self.run_command(sys.executable, "-B", "app/main.py"), "2 + 3 = 5")
        if self.revision == "v2.0":
            self.assertEqual(self.run_command(
                sys.executable, "-B", "-c",
                "import sys; sys.path.insert(0, 'libs/arithmetic'); "
                "from arithmetic import multiply; print(multiply(2, 3))"), "6")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--revision", required=True, choices=("v1.0", "v2.0"))
    parser.add_argument("--docs", action="store_true", help="预期 docs 组已启用并同步")
    args = parser.parse_args()
    WorkspaceTest.workspace = args.workspace.resolve()
    WorkspaceTest.revision = args.revision
    WorkspaceTest.docs = args.docs
    if not WorkspaceTest.workspace.is_dir():
        parser.error("工作区目录不存在；先完成种子生成与初始化")
    # 收集 test_ 方法依次运行；成功返回 False/0，失败返回 True/1 给 shell。
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(WorkspaceTest)
    return not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


if __name__ == "__main__":
    sys.exit(main())
