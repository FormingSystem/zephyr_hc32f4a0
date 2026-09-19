# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""教学包第一版：返回旧版问候语。"""


def greet(name="reader"):
    """名字参数影响输出，不依赖第三方包。"""
    return f"hello {name} from v1"
