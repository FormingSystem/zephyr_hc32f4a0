---
id: learning.zephyr-docs.api-source-supplement-reference.page-168
title: rpi_pico_clock_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_rpi\_pico\_clock\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h.html)。

## 168.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2022 Andrei-Edward Popa
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RPI_PICO_CLOCK_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RPI_PICO_CLOCK_COMMON_H_

#define RPI_PICO_PLL_SYS   0
#define RPI_PICO_PLL_USB   1
#define RPI_PICO_PLL_COUNT 2

#define RPI_PICO_GPIN_0     0
#define RPI_PICO_GPIN_1     1
#define RPI_PICO_GPIN_COUNT 2

#define RPI_PICO_CLKID_CLK_GPOUT0 0
#define RPI_PICO_CLKID_CLK_GPOUT1 1
#define RPI_PICO_CLKID_CLK_GPOUT2 2
#define RPI_PICO_CLKID_CLK_GPOUT3 3
#define RPI_PICO_CLKID_CLK_REF    4
#define RPI_PICO_CLKID_CLK_SYS    5
#define RPI_PICO_CLKID_CLK_PERI   6
/* N.b. clock ids 7-9 are defined in SoC-specific files. */

#define RPI_PICO_CLKID_PLL_SYS 10
#define RPI_PICO_CLKID_PLL_USB 11
#define RPI_PICO_CLKID_XOSC    12
#define RPI_PICO_CLKID_ROSC    13
#define RPI_PICO_CLKID_ROSC_PH 14
#define RPI_PICO_CLKID_GPIN0   15
#define RPI_PICO_CLKID_GPIN1   16

#define RPI_PICO_ROSC_RANGE_RESET   0xAA0
#define RPI_PICO_ROSC_RANGE_LOW     0xFA4
#define RPI_PICO_ROSC_RANGE_MEDIUM  0xFA5
#define RPI_PICO_ROSC_RANGE_HIGH    0xFA7
#define RPI_PICO_ROSC_RANGE_TOOHIGH 0xFA6

#define RPI_PICO_CLOCK_COUNT 10

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RPI_PICO_CLOCK_COMMON_H_ */
```

## 168.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Andrei-Edward Popa。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

注意：时钟标识符 7–9 在 SoC 专用文件中定义。

### 注释 3：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RPI_PICO_CLOCK_COMMON_H_`。

## 168.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi__pico__clock__common_8h.html)

---

[上一章](P167_rpi-pico-rp2350a-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P169_rpr_cli.h_源码浏览.md)
