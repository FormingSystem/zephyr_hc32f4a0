---
id: learning.zephyr-docs.api-source-reference.page-45
title: atmel_samx7x_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_atmel\_samx7x\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h.html)。

## 45.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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

```c
/*
 * Copyright (c) 2020 Linaro Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_ATMEL_SAMX7X_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_ATMEL_SAMX7X_DMA_H_

#define DMA_PERID_HSMCI_TX_RX 0
#define DMA_PERID_SPI0_TX     1
#define DMA_PERID_SPI0_RX     2
#define DMA_PERID_SPI1_TX     3
#define DMA_PERID_SPI1_RX     4
#define DMA_PERID_QSPI_TX     5
#define DMA_PERID_QSPI_RX     6
#define DMA_PERID_USART0_TX   7
#define DMA_PERID_USART0_RX   8
#define DMA_PERID_USART1_TX   9
#define DMA_PERID_USART1_RX   10
#define DMA_PERID_USART2_TX   11
#define DMA_PERID_USART2_RX   12
#define DMA_PERID_PWM0_TX     13
#define DMA_PERID_TWIHS0_TX   14
#define DMA_PERID_TWIHS0_RX   15
#define DMA_PERID_TWIHS1_TX   16
#define DMA_PERID_TWIHS1_RX   17
#define DMA_PERID_TWIHS2_TX   18
#define DMA_PERID_TWIHS2_RX   19
#define DMA_PERID_UART0_TX    20
#define DMA_PERID_UART0_RX    21
#define DMA_PERID_UART1_TX    22
#define DMA_PERID_UART1_RX    23
#define DMA_PERID_UART2_TX    24
#define DMA_PERID_UART2_RX    25
#define DMA_PERID_UART3_TX    26
#define DMA_PERID_UART3_RX    27
#define DMA_PERID_UART4_TX    28
#define DMA_PERID_UART4_RX    29
#define DMA_PERID_DACC0_TX    30
#define DMA_PERID_DACC1_TX    31
#define DMA_PERID_SSC_TX      32
#define DMA_PERID_SSC_RX      33
#define DMA_PERID_PIOA_RX     34
#define DMA_PERID_AFEC0_RX    35
#define DMA_PERID_AFEC1_RX    36
#define DMA_PERID_AES_TX      37
#define DMA_PERID_AES_RX      38
#define DMA_PERID_PWM1_TX     39
#define DMA_PERID_TC0_RX      40
#define DMA_PERID_TC1_RX      41
#define DMA_PERID_TC2_RX      42
#define DMA_PERID_TC3_RX      43
#define DMA_PERID_I2SC0_TX_L  44
#define DMA_PERID_I2SC0_RX_L  45
#define DMA_PERID_I2SC1_TX_L  46
#define DMA_PERID_I2SC1_RX_L  47
#define DMA_PERID_I2SC0_TX_R  48
#define DMA_PERID_I2SC0_RX_R  49
#define DMA_PERID_I2SC1_TX_R  50
#define DMA_PERID_I2SC1_RX_R  51

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_ATMEL_SAMX7X_DMA_H_ */
```

## 45.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_ATMEL_SAMX7X_DMA_H_`。

## 45.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/atmel__samx7x__dma_8h.html)

---

[上一章](P044_atmel-sam0-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P046_autohandler.h_源码浏览.md)
