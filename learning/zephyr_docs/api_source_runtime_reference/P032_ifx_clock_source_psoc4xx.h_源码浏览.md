---
id: learning.zephyr-docs.api-source-runtime-reference.page-32
title: ifx_clock_source_psoc4xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_ifx\_clock\_source\_psoc4xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h.html)。

## 32.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSOC4XX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSOC4XX_H_

/*
 * Note : use IFX_PATH_PSOC4_IMO for internal main oscillator as src
 * use IFX_PATH_PSOC4_EXT for External clock as src
 *
 * Usage : input src for clk_hf
 */
#define IFX_PATH_PSOC4_IMO 0
#define IFX_PATH_PSOC4_EXT 1

/*
 * Note : use IFX_PATH_PSOC4_PUMP_GND for No clock, connect to gnd
 * use IFX_PATH_PSOC4_PUMP_IMO for main IMO pump output
 * use IFX_PATH_PSOC4_PUMP_HFCLK for clk_hf pump
 *
 * Usage : input src for clk_pump
 */
#define IFX_PATH_PSOC4_PUMP_GND   0
#define IFX_PATH_PSOC4_PUMP_IMO   1
#define IFX_PATH_PSOC4_PUMP_HFCLK 2

/*
 * @brief Device Tree compatible clock source to Infineon PDL clock source
 *
 * This macro converts Device Tree clock source identifiers (defined in
 * ifx_clock_source_common.h) to the corresponding Infineon PDL API values.
 *
 * Usage : in clock_control_infineon_fixed_factor_clock.c, use this macro
 * when passing clock source values from Device Tree to Infineon PDL APIs.
 * This allows users to use the generic ifx_clock_source_common.h macros
 * directly in Device Tree files while ensuring compatibility with the
 * underlying PDL implementation.
 */
#define IFX_PSOC4_HFCLK_DIV(div)                                                                   \
        ((div) == 0   ? CY_SYSCLK_NO_DIV                                                           \
         : (div) == 1 ? CY_SYSCLK_DIV_2                                                            \
         : (div) == 3 ? CY_SYSCLK_DIV_4                                                            \
         : (div) == 7 ? CY_SYSCLK_DIV_8                                                            \
                      : CY_SYSCLK_NO_DIV)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSOC4XX_H_ */
```

## 32.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

注意：使用 `IFX_PATH_PSOC4_IMO` 将内部主振荡器（Internal main oscillator）选为源；使用 `IFX_PATH_PSOC4_EXT` 将外部时钟选为源。

用途：作为 `clk_hf` 的输入源。

### 注释 3：原第 20 行

注意：使用 `IFX_PATH_PSOC4_PUMP_GND` 表示无时钟、连接到地；使用 `IFX_PATH_PSOC4_PUMP_IMO` 选择主 IMO 的泵输出；使用 `IFX_PATH_PSOC4_PUMP_HFCLK` 选择 `clk_hf` 泵。

用途：作为 `clk_pump` 的输入源。

### 注释 4：原第 31 行

功能（Brief）：将设备树兼容的时钟源转换为 Infineon PDL 时钟源。

此宏将设备树时钟源标识符（定义在 `ifx_clock_source_common.h` 中）转换为对应的 Infineon PDL API 值。

用法：在 `clock_control_infineon_fixed_factor_clock.c` 中，将设备树时钟源值传给 Infineon PDL API 时使用此宏。这样，用户可直接在设备树文件中使用通用的 `ifx_clock_source_common.h` 宏，同时保持与底层 PDL 实现兼容。

### 注释 5：原第 50 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSOC4XX_H_`。

## 32.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h.html)

---

[上一章](P031_ifx_cat1-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P033_input-event-codes.h_源码浏览.md)
