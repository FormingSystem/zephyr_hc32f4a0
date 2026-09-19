# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""显示运行此文件的解释器身份，不修改环境。"""

import json
import os
import site
import sys


print(json.dumps({
    "executable": sys.executable,
    "prefix": sys.prefix,
    "base_prefix": sys.base_prefix,
    "is_venv": sys.prefix != sys.base_prefix,
    "VIRTUAL_ENV": os.environ.get("VIRTUAL_ENV"),
    "site_packages": site.getsitepackages(),
    "user_site_enabled": site.ENABLE_USER_SITE,
}, indent=2, ensure_ascii=False))
