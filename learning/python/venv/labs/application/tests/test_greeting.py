# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""应用要求 v1 的输出协议；更换环境后运行同一套测试。"""

import unittest

from lab_greeting import greet


class GreetingContractTest(unittest.TestCase):
    def test_default_reader(self):
        self.assertEqual(greet(), "hello reader from v1")

    def test_board_name(self):
        self.assertEqual(greet("board"), "hello board from v1")


if __name__ == "__main__":
    unittest.main()
