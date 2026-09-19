# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""教学包第二版：同样的接口，新的输出。"""


def greet(name="reader"):
    """用于观察同名包在不同环境中的独立安装。"""
    return f"hello {name} from v2"
