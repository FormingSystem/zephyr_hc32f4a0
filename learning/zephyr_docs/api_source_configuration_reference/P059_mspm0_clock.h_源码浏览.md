---
id: learning.zephyr-docs.api-source-configuration-reference.page-59
title: mspm0_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_mspm0\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)。

## 59.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>

```c
/*
 * Copyright 2025 Texas Instruments Inc.
 * Copyright 2025 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MSPM0_CLOCK_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MSPM0_CLOCK_H

#define MSPM0_CLOCK(clk, bit) ((clk << 8) | bit)

/* Peripheral clock source selection register mask */
#define MSPM0_CLOCK_PERIPH_REG_MASK(X)  (X & 0xFF)

/* Clock references */
#define MSPM0_CLOCK_SYSOSC              MSPM0_CLOCK(0x0, 0x0)
#define MSPM0_CLOCK_LFCLK               MSPM0_CLOCK(0x1, 0x2)
#define MSPM0_CLOCK_MFCLK               MSPM0_CLOCK(0x2, 0x4)
#define MSPM0_CLOCK_BUSCLK              MSPM0_CLOCK(0x3, 0x8)
#define MSPM0_CLOCK_ULPCLK              MSPM0_CLOCK(0x4, 0x8)
#define MSPM0_CLOCK_MCLK                MSPM0_CLOCK(0x5, 0x8)
#define MSPM0_CLOCK_MFPCLK              MSPM0_CLOCK(0x6, 0x0)
#define MSPM0_CLOCK_CANCLK              MSPM0_CLOCK(0x7, 0x0)
#define MSPM0_CLOCK_CLK_OUT             MSPM0_CLOCK(0x8, 0x0)
#define MSPM0_CLOCK_HFCLK               MSPM0_CLOCK(0x9, 0x2)

#endif
```

## 59.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Texas Instruments Inc.。

版权（Copyright）：2025 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

外设时钟源选择寄存器的掩码。

### 注释 3：原第 16 行

时钟引用（Clock references）。

## 59.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)

---

[上一章](P058_mpipe_bin.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P060_npm13xx_charger.h_源码浏览.md)
