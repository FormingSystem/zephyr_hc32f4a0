---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-1
title: adi_max32_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_adi\_max32\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P002_zephyr__dt-bindings__clock__adi_max32_clock.h_文件参考.md)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
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

```c
/*
 * Copyright (c) 2023-2024 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ADI_MAX32_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ADI_MAX32_CLOCK_H_

#define ADI_MAX32_CLOCK_BUS0 0
#define ADI_MAX32_CLOCK_BUS1 1
#define ADI_MAX32_CLOCK_BUS2 2

#define ADI_MAX32_PRPH_CLK_SRC_PCLK      0 /* Peripheral clock */
#define ADI_MAX32_PRPH_CLK_SRC_EXTCLK    1 /* External clock */
#define ADI_MAX32_PRPH_CLK_SRC_IBRO      2 /* Internal Baud Rate Oscillator*/
#define ADI_MAX32_PRPH_CLK_SRC_ERFO      3 /* External RF Oscillator */
#define ADI_MAX32_PRPH_CLK_SRC_ERTCO     4 /* External RTC Oscillator */
#define ADI_MAX32_PRPH_CLK_SRC_INRO      5 /* Internal Nano Ring Oscillator */
#define ADI_MAX32_PRPH_CLK_SRC_ISO       6 /* Internal Secondary Oscillator */
#define ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8 7 /* IBRO/8 */
#define ADI_MAX32_PRPH_CLK_SRC_IPLL      8 /* Internal Phase Lock Loop Oscillator */
#define ADI_MAX32_PRPH_CLK_SRC_EBO       9 /* External Base Oscillator */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ADI_MAX32_CLOCK_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023-2024 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

外设时钟（peripheral clock）。

### 注释 3：原第 17 行

外部时钟（external clock）。

### 注释 4：原第 18 行

内部波特率振荡器（Internal Baud Rate Oscillator）。

### 注释 5：原第 19 行

外部射频振荡器（External RF Oscillator）。

### 注释 6：原第 20 行

外部实时时钟振荡器（External RTC Oscillator）。

### 注释 7：原第 21 行

内部纳米环形振荡器（Internal Nano Ring Oscillator）。

### 注释 8：原第 22 行

内部次级振荡器（Internal Secondary Oscillator）。

### 注释 9：原第 23 行

内部波特率振荡器时钟除以 8（IBRO/8）。

### 注释 10：原第 24 行

内部锁相环振荡器（Internal Phase Lock Loop Oscillator）。

### 注释 11：原第 25 行

外部基准振荡器（External Base Oscillator）。

### 注释 12：原第 27 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ADI_MAX32_CLOCK_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P002_zephyr__dt-bindings__clock__adi_max32_clock.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_cmux.h_源码浏览.md)
