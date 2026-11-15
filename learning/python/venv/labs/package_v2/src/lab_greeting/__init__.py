# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""教学包第二版：同样的接口，新的输出。"""


# 第二版仍接受相同的名字参数，省略时使用 reader。
def greet(name="reader"):
    """用于观察同名包在不同环境中的独立安装。"""
    # 只改变返回文字中的版本，用来观察环境隔离与行为测试。
    return f"hello {name} from v2"
