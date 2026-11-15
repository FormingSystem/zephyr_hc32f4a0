---
id: learning.zephyr-docs.api-source-reference.page-777
title: sf32lb52x-dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第777章\_sf32lb52x-dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-dma_8h.html)。

## 777.1\_原始可见代码（Source Code）

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
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="asf32lb-dma-config_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Core Devices LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SF32LB52X_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SF32LB52X_DMA_H_

#include "sf32lb-dma-config.h"

#define SF32LB52X_DMA_REQ_MPI1              0U
#define SF32LB52X_DMA_REQ_MPI2              1U
#define SF32LB52X_DMA_REQ_I2C4              3U
#define SF32LB52X_DMA_REQ_USART1_TX         4U
#define SF32LB52X_DMA_REQ_USART1_RX         5U
#define SF32LB52X_DMA_REQ_USART2_TX         6U
#define SF32LB52X_DMA_REQ_USART2_RX         7U
#define SF32LB52X_DMA_REQ_GPTIM1_UPDATE     8U
#define SF32LB52X_DMA_REQ_GPTIM1_TRIGGER    9U
#define SF32LB52X_DMA_REQ_GPTIM1_CC1        10U
#define SF32LB52X_DMA_REQ_GPTIM1_CC2        11U
#define SF32LB52X_DMA_REQ_GPTIM1_CC3        12U
#define SF32LB52X_DMA_REQ_GPTIM1_CC4        13U
#define SF32LB52X_DMA_REQ_BTIM1             14U
#define SF32LB52X_DMA_REQ_BTIM2             15U
#define SF32LB52X_DMA_REQ_ATIM1_UPDATE      16U
#define SF32LB52X_DMA_REQ_ATIM1_TRIGGER     17U
#define SF32LB52X_DMA_REQ_ATIM1_CC1         18U
#define SF32LB52X_DMA_REQ_ATIM1_CC2         19U
#define SF32LB52X_DMA_REQ_ATIM1_CC3         20U
#define SF32LB52X_DMA_REQ_ATIM1_CC4         21U
#define SF32LB52X_DMA_REQ_I2C1              22U
#define SF32LB52X_DMA_REQ_I2C2              23U
#define SF32LB52X_DMA_REQ_I2C3              24U
#define SF32LB52X_DMA_REQ_ATIM1_COM         25U
#define SF32LB52X_DMA_REQ_USART3_TX         26U
#define SF32LB52X_DMA_REQ_USART3_RX         27U
#define SF32LB52X_DMA_REQ_SPI1_TX           28U
#define SF32LB52X_DMA_REQ_SPI1_RX           29U
#define SF32LB52X_DMA_REQ_SPI2_TX           30U
#define SF32LB52X_DMA_REQ_SPI2_RX           31U
#define SF32LB52X_DMA_REQ_I2S1_TX           32U
#define SF32LB52X_DMA_REQ_I2S1_RX           33U
#define SF32LB52X_DMA_REQ_PDM1_L            36U
#define SF32LB52X_DMA_REQ_PDM1_R            37U
#define SF32LB52X_DMA_REQ_GPADC             38U
#define SF32LB52X_DMA_REQ_AUDADC_CH0        39U
#define SF32LB52X_DMA_REQ_AUDADC_CH1        40U
#define SF32LB52X_DMA_REQ_AUDAC_CH0         41U
#define SF32LB52X_DMA_REQ_AUDAC_CH1         42U
#define SF32LB52X_DMA_REQ_GPTIM2_UPDATE     43U
#define SF32LB52X_DMA_REQ_GPTIM2_TRIGGER    44U
#define SF32LB52X_DMA_REQ_GPTIM2_CC1        45U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_OUT_CH1 46U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_OUT_CH0 47U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_CH3     48U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_CH2     49U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_CH1     50U
#define SF32LB52X_DMA_REQ_AUDPRC_TX_CH0     51U
#define SF32LB52X_DMA_REQ_AUDPRC_RX_CH1     52U
#define SF32LB52X_DMA_REQ_AUDPRC_RX_CH0     53U
#define SF32LB52X_DMA_REQ_GPTIM2_CC2        54U
#define SF32LB52X_DMA_REQ_GPTIM2_CC3        55U
#define SF32LB52X_DMA_REQ_GPTIM2_CC4        56U
#define SF32LB52X_DMA_REQ_SDMMC1            57U

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SF32LB52X_DMA_H_ */
```

## 777.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Core Devices LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SF32LB52X_DMA_H_`。

## 777.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-dma_8h.html)
- [sf32lb-dma-config.h](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-dma-config_8h.html)

---

[上一章](P776_sf32lb52x-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P778_sf32lb_reset.h_源码浏览.md)
