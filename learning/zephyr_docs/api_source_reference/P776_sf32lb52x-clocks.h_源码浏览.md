---
id: learning.zephyr-docs.api-source-reference.page-776
title: sf32lb52x-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第776章\_sf32lb52x-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h.html)。

## 776.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
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
<a id="l00067"></a>
<a id="l00068"></a>
<a id="asf32lb-clocks-common_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Core Devices LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SF32LB52X_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SF32LB52X_CLOCKS_H_

#include "sf32lb-clocks-common.h"


#define SF32LB52X_RCC_ENR1 0x08U
#define SF32LB52X_RCC_ENR2 0x0CU



#define SF32LB52X_CLOCK_DMAC1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 0U)
#define SF32LB52X_CLOCK_MAILBOX1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 1U)
#define SF32LB52X_CLOCK_PINMUX1  SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 2U)
#define SF32LB52X_CLOCK_USART2   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 4U)
#define SF32LB52X_CLOCK_EZIP1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 5U)
#define SF32LB52X_CLOCK_EPIC     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 6U)
#define SF32LB52X_CLOCK_LCDC1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 7U)
#define SF32LB52X_CLOCK_I2S1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 8U)
#define SF32LB52X_CLOCK_SYSCFG1  SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 10U)
#define SF32LB52X_CLOCK_EFUSEC   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 11U)
#define SF32LB52X_CLOCK_AES      SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 12U)
#define SF32LB52X_CLOCK_CRC1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 13U)
#define SF32LB52X_CLOCK_TRNG     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 14U)
#define SF32LB52X_CLOCK_GPTIM1   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 15U)
#define SF32LB52X_CLOCK_GPTIM2   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 16U)
#define SF32LB52X_CLOCK_BTIM1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 17U)
#define SF32LB52X_CLOCK_BTIM2    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 18U)
#define SF32LB52X_CLOCK_SPI1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 20U)
#define SF32LB52X_CLOCK_SPI2     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 21U)
#define SF32LB52X_CLOCK_EXTDMA   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 22U)
#define SF32LB52X_CLOCK_SECU1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 23U)
#define SF32LB52X_CLOCK_PDM1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 25U)
#define SF32LB52X_CLOCK_I2C1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 27U)
#define SF32LB52X_CLOCK_I2C2     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 28U)
#define SF32LB52X_CLOCK_PTC1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 31U)

#define SF32LB52X_CLOCK_GPIO1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 0U)
#define SF32LB52X_CLOCK_MPI1     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 1U)
#define SF32LB52X_CLOCK_MPI2     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 2U)
#define SF32LB52X_CLOCK_SDMMC1   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 4U)
#define SF32LB52X_CLOCK_USBC     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 6U)
#define SF32LB52X_CLOCK_I2C3     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 8U)
#define SF32LB52X_CLOCK_ATIM1    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 9U)
#define SF32LB52X_CLOCK_USART3   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 12U)
#define SF32LB52X_CLOCK_AUDCODEC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 19U)
#define SF32LB52X_CLOCK_AUDPRC   SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 20U)
#define SF32LB52X_CLOCK_GPADC    SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 22U)
#define SF32LB52X_CLOCK_TSEN     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 23U)
#define SF32LB52X_CLOCK_I2C4     SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 25U)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SF32LB52X_CLOCKS_H_ */
```

## 776.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Core Devices LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SF32LB52X_CLOCKS_H_`。

## 776.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h.html)
- [sf32lb-clocks-common.h](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html)

---

[上一章](P775_sf32lb-dma-config.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P777_sf32lb52x-dma.h_源码浏览.md)
