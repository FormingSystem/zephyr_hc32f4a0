---
id: learning.zephyr-docs.api-file-configuration-reference.page-32
title: zephyr__drivers__sensor__generic_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_drivers\_\_sensor\_\_generic\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

控制通用仿真传感器测试设备（Emulated Sensor Test Device）的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
```

查看此文件的源码。

控制通用仿真传感器测试设备（Emulated Sensor Test Device）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 32.1\_函数（Functions）

<a id="r_gaa46e3a3f212fabb397347cacece3325c"></a>

```c
void generic_emul_reset (const struct emul *target, bool reset_rc)
```

相关声明：[generic_emul_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gaa46e3a3f212fabb397347cacece3325c)、[emul](../hardware/P477_仿真器实例结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有通道（Channels）重置为未配置状态（Unconfigured）。

<a id="r_gadaae3d98d7e56858b882319b26990803"></a>

```c
void generic_emul_func_rc (const struct emul *target, int resume_rc, int suspend_rc, int fetch_rc)
```

相关声明：[generic_emul_func_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gadaae3d98d7e56858b882319b26990803)、[emul](../hardware/P477_仿真器实例结构.md)。

配置通用传感器设备（Generic Sensor Device）的返回值（Return Value）。


## 32.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P289_generic_emul.h_源码浏览.md)
- [generic_emul_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gaa46e3a3f212fabb397347cacece3325c)
- [emul](../hardware/P477_仿真器实例结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [generic_emul_func_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gadaae3d98d7e56858b882319b26990803)

<a id="header-details"></a>

---

[上一章](P031_zephyr__net__prometheus__gauge.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__drivers__gnss__gnss_publish.h_文件参考.md)
