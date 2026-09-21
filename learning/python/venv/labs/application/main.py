# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""示例应用：由当前解释器选择已安装的问候包。"""

from lab_greeting import greet

print(greet("board"))
