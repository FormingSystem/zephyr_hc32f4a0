# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""应用要求 v1 的输出协议；更换环境后运行同一套测试。"""

# 标准库测试框架，负责找测试、运行测试并汇总结果。
import unittest

# 这是被检查的函数，由本次运行测试的环境提供。
from lab_greeting import greet


# 把同一组应用要求放在一个测试类里。
class GreetingContractTest(unittest.TestCase):
    def test_default_reader(self):
        # 不传名字，比较“实际返回值”与“应用要求的值”。
        self.assertEqual(greet(), "hello reader from v1")

    def test_board_name(self):
        # 传入 board，检查参数是否进入问候语且仍使用 v1 协议。
        self.assertEqual(greet("board"), "hello board from v1")


# 直接运行本文件时启动测试；被 discover 导入时由 discover 调度。
if __name__ == "__main__":
    unittest.main()
