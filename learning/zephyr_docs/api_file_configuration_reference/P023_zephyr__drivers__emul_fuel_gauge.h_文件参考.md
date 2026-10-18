---
id: learning.zephyr-docs.api-file-configuration-reference.page-23
title: zephyr__drivers__emul_fuel_gauge.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_emul\_fuel\_gauge.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电量计仿真器（Fuel Gauge Emulators）的后端API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/fuel_gauge.h>
#include <zephyr/syscalls/emul_fuel_gauge.h>
```

查看此文件的源码。

电量计仿真器（Fuel Gauge Emulators）的后端API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_gab6493138c35191a58e6f28c24b97715e"></a>

```c
int emul_fuel_gauge_set_battery_charging (const struct emul *target, uint32_t uV, int uA)
```

相关声明：[emul_fuel_gauge_set_battery_charging](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gab6493138c35191a58e6f28c24b97715e)、[emul](../hardware/P477_仿真器实例结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置电量计（Fuel Gauge）关联电池的充电状态（Charging）。

<a id="r_gaf8326331c7470b41aa542f828b20a828"></a>

```c
int emul_fuel_gauge_is_battery_cutoff (const struct emul *target, bool *cutoff)
```

相关声明：[emul_fuel_gauge_is_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gaf8326331c7470b41aa542f828b20a828)、[emul](../hardware/P477_仿真器实例结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查电池是否已切断（Cut Off）。


## 23.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P225_emul_fuel_gauge.h_源码浏览.md)
- [emul_fuel_gauge_set_battery_charging](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gab6493138c35191a58e6f28c24b97715e)
- [emul](../hardware/P477_仿真器实例结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [emul_fuel_gauge_is_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gaf8326331c7470b41aa542f828b20a828)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__usb__emul_bc12.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__drivers__emul_stub_device.h_文件参考.md)
