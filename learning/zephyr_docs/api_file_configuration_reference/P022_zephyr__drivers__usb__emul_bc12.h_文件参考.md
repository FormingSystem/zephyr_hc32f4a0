---
id: learning.zephyr-docs.api-file-configuration-reference.page-22
title: zephyr__drivers__usb__emul_bc12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_usb\_\_emul\_bc12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB电池充电规范1.2（BC1.2）仿真器的后端API。

<a id="details"></a>

```c
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/usb/usb_bc12.h>
```

查看此文件的源码。

USB电池充电规范1.2（BC1.2）仿真器的后端API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_gaca0e62f2f8a5ec3135523fa3a1308034"></a>

```c
static int bc12_emul_set_charging_partner (const struct emul *target, enum bc12_type partner_type)
```

相关声明：[bc12_emul_set_charging_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaca0e62f2f8a5ec3135523fa3a1308034)、[emul](../hardware/P477_仿真器实例结构.md)、[bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)。

设置连接到 BC1.2 设备的充电伙伴类型（Charging Partner Type）。

<a id="r_gaa71771a3199aef043fe313f09f3bb4f2"></a>

```c
static int bc12_emul_set_pd_partner (const struct emul *target, bool connected)
```

相关声明：[bc12_emul_set_pd_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaa71771a3199aef043fe313f09f3bb4f2)、[emul](../hardware/P477_仿真器实例结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置便携设备伙伴状态（Portable Device Partner State）。


## 22.2\_原页交叉引用（Cross References）

- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/usb/usb_bc12.h](../api_source_supplement_reference/P235_usb_bc12.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P224_emul_bc12.h_源码浏览.md)
- [bc12_emul_set_charging_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaca0e62f2f8a5ec3135523fa3a1308034)
- [emul](../hardware/P477_仿真器实例结构.md)
- [bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)
- [bc12_emul_set_pd_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaa71771a3199aef043fe313f09f3bb4f2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P021_zephyr__drivers__emul_bbram.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__emul_fuel_gauge.h_文件参考.md)
