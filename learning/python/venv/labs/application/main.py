# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""示例应用：由当前解释器选择已安装的问候包。"""

# 从当前解释器找到的 lab_greeting 包中取得 greet 函数。
from lab_greeting import greet

# 先调用 greet 得到字符串，再交给 print 显示到终端。
print(greet("board"))
