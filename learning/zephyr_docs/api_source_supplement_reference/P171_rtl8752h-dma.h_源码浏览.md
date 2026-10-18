---
id: learning.zephyr-docs.api-source-supplement-reference.page-171
title: rtl8752h-dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_rtl8752h-dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h.html)。

## 171.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="abee-dma_8h_html"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RTL8752H_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RTL8752H_DMA_H_

#include "bee-dma.h"

/* Handshake (slot) IDs, second cell of a "dmas" entry. */
#define BEE_DMA_HANDSHAKE_UART1_TX  0
#define BEE_DMA_HANDSHAKE_UART1_RX  1
#define BEE_DMA_HANDSHAKE_ENH_TIM0  2
#define BEE_DMA_HANDSHAKE_ENH_TIM1  3
#define BEE_DMA_HANDSHAKE_SPI0_TX   4
#define BEE_DMA_HANDSHAKE_SPI0_RX   5
#define BEE_DMA_HANDSHAKE_SPI1_TX   6
#define BEE_DMA_HANDSHAKE_SPI1_RX   7
#define BEE_DMA_HANDSHAKE_I2C0_TX   8
#define BEE_DMA_HANDSHAKE_I2C0_RX   9
#define BEE_DMA_HANDSHAKE_I2C1_TX   10
#define BEE_DMA_HANDSHAKE_I2C1_RX   11
#define BEE_DMA_HANDSHAKE_ADC       12
#define BEE_DMA_HANDSHAKE_AES_TX    13
#define BEE_DMA_HANDSHAKE_AES_RX    14
#define BEE_DMA_HANDSHAKE_UART0_TX  15
#define BEE_DMA_HANDSHAKE_I2S0_TX   16
#define BEE_DMA_HANDSHAKE_I2S0_RX   17
#define BEE_DMA_HANDSHAKE_UART2_TX  18
#define BEE_DMA_HANDSHAKE_UART2_RX  19
#define BEE_DMA_HANDSHAKE_SPIC0_TX  20
#define BEE_DMA_HANDSHAKE_SPIC0_RX  21
#define BEE_DMA_HANDSHAKE_I8080_RX  22
#define BEE_DMA_HANDSHAKE_UART0_RX  23
#define BEE_DMA_HANDSHAKE_TIM0      24
#define BEE_DMA_HANDSHAKE_TIM1      25
#define BEE_DMA_HANDSHAKE_TIM2      26
#define BEE_DMA_HANDSHAKE_IR_TX     27
#define BEE_DMA_HANDSHAKE_IR_RX     28
#define BEE_DMA_HANDSHAKE_TIM3      29
#define BEE_DMA_HANDSHAKE_TIM4      30
#define BEE_DMA_HANDSHAKE_TIM5      31
#define BEE_DMA_HANDSHAKE_SPIC1_TX  32
#define BEE_DMA_HANDSHAKE_SPIC1_RX  33
#define BEE_DMA_HANDSHAKE_SHA256_TX 35

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RTL8752H_DMA_H_ */
```

## 171.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

握手标识符（Handshake IDs，即 slot），作为 `dmas` 条目的第二个单元。

### 注释 3：原第 58 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RTL8752H_DMA_H_`。

## 171.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-dma_8h.html)
- [bee-dma.h](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h.html)

---

[上一章](P170_rtk_publish.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P172_rtl87x2g-dma.h_源码浏览.md)
