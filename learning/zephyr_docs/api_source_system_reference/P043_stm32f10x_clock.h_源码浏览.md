---
id: learning.zephyr-docs.api-source-system-reference.page-43
title: stm32f10x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f10x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_stm32f10x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f10x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P422_zephyr__dt-bindings__clock__stm32f10x_clock.h_文件参考.md)。

## 43.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="astm32f1__clock_8h_html"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (C) 2024, Joakim Andersson
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F10X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F10X_CLOCK_H_

/* Ensure correct order by including generic F1 definitions first. */
#include <zephyr/dt-bindings/clock/stm32f1_clock.h>


/* Low speed clocks defined in stm32_common_clocks.h */
/* Common clocks with stm32f1x defined in stm32f1_clock.h */
#define STM32_SRC_PLL2CLK           (STM32_SRC_TIMPCLK2 + 1)
#define STM32_SRC_PLL3CLK           (STM32_SRC_PLL2CLK + 1)

#undef MCO1_SEL /* Need to redefine generic F1 MCO_SEL for connectivity line devices. */
#define MCO1_SEL(val)           STM32_DT_CLOCK_SELECT((val), 27, 24, CFGR1_REG)
/* No MCO prescaler support on STM32F1 series. */


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F10X_CLOCK_H_ */
```

## 43.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX-License-Identifier: Apache-2.0。

版权所有（Copyright）2024 Joakim Andersson。

### 注释 2：原第 10 行

先包含通用 F1 定义（Generic F1 Definitions），以确保顺序正确。

### 注释 3：原第 16 行

低速时钟定义在 `stm32_common_clocks.h` 中。

### 注释 4：原第 17 行

与 stm32f1x 共用的时钟（Common Clocks）定义在 `stm32f1_clock.h` 中。

### 注释 5：原第 22 行

对于互联型器件（Connectivity Line Devices），需要重新定义通用 F1 的 `MCO_SEL`。

### 注释 6：原第 24 行

STM32F1 系列不支持微控制器时钟输出预分频器（MCO Prescaler）。

### 注释 7：原第 28 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F10X_CLOCK_H_`。

## 43.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P422_zephyr__dt-bindings__clock__stm32f10x_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32f1_clock.h](../api_file_reference/P423_zephyr__dt-bindings__clock__stm32f1_clock.h_文件参考.md)
- [stm32f1_clock.h](../api_file_reference/P423_zephyr__dt-bindings__clock__stm32f1_clock.h_文件参考.md)

---

[上一章](P042_stdio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P044_stm32f4_clock.h_源码浏览.md)
