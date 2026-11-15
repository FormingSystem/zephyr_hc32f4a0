# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""教学包第一版：返回旧版问候语。"""


# name 默认使用 reader，调用者也可以传入自己的名字。
def greet(name="reader"):
    """名字参数影响输出，不依赖第三方包。"""
    # 把文字交还调用者；由应用决定是否打印到终端。
    return f"hello {name} from v1"
