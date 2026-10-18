---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-16
title: zephyr__drivers__mspi__mspi_cadence.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr__drivers__mspi__mspi_cadence.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspi__cadence_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="agroup__mspi__cadence__interface_html_ga9437f27953847cd2c6e79e5252586d77"></a>
<a id="agroup__mspi__cadence__interface_html_gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmspi__cadence__timing__cfg_html"></a>
<a id="astructmspi__cadence__timing__cfg_html_af0f7347dcd065484df7e9b2f079f61e4"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: 2026 Texas Instruments Incorporated
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MSPI_CADENCE_H_
#define ZEPHYR_INCLUDE_DRIVERS_MSPI_CADENCE_H_


#include <zephyr/sys/util_macro.h>
#include <stdint.h>


struct mspi_cadence_timing_cfg {
        uint8_t rd_delay;
};

enum mspi_cadence_timing_param {
        MSPI_CADENCE_TIMING_PARAM_RD_DELAY = BIT(0)
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_MSPI_CADENCE_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 Texas Instruments Incorporated。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MSPI_CADENCE_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [mspi_cadence_timing_cfg](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rd_delay](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md#af0f7347dcd065484df7e9b2f079f61e4)
- [mspi_cadence_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#ga9437f27953847cd2c6e79e5252586d77)
- [MSPI_CADENCE_TIMING_PARAM_RD_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html#gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [mspi_cadence_timing_cfg::rd_delay](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md#af0f7347dcd065484df7e9b2f079f61e4)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P015_zephyr__sd__sd_spec.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__mspi.h_头文件源码.md)
