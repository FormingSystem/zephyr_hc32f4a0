---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-16
title: zephyr__drivers__mspi__mspi_cadence.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_mspi\_\_mspi\_cadence.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Cadence MSPI控制器的专用定义（Controller Specific Definitions）。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
#include <stdint.h>
```

查看此文件的源码。

Cadence MSPI控制器的专用定义（Controller Specific Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_mspi_5Fcadence_5Ftiming_5Fcfg"></a>

```c
struct mspi_cadence_timing_cfg
```

相关声明：[mspi_cadence_timing_cfg](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md)。

TI K3 MSPI外设的时序配置（Timing Configuration）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.2\_枚举（Enumerations）

<a id="r_ga9437f27953847cd2c6e79e5252586d77"></a>

```c
enum mspi_cadence_timing_param { MSPI_CADENCE_TIMING_PARAM_RD_DELAY = BIT(0) }
```

相关声明：[mspi_cadence_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#ga9437f27953847cd2c6e79e5252586d77)、[MSPI_CADENCE_TIMING_PARAM_RD_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce)。

枚举，指定应修改哪些时序参数（Timing parameters）。


## 16.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h_source.html)
- [mspi_cadence_timing_cfg](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md)
- [mspi_cadence_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#ga9437f27953847cd2c6e79e5252586d77)
- [MSPI_CADENCE_TIMING_PARAM_RD_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce)

<a id="header-details"></a>

---

[上一章](P015_zephyr__sd__sd_spec.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__mspi.h_头文件参考.md)
