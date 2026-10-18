---
id: learning.zephyr-docs.api-source-reference.page-724
title: rpi-pico-dma-rp2350.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2350_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第724章\_rpi-pico-dma-rp2350.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2350_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2350_8h.html)。

## 724.1\_原始可见代码（Source Code）

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
<a id="arpi-pico-dma-common_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Manuel Aebischer <manuel.aebischer@belden.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_RP2350_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_RP2350_H_

#include "rpi-pico-dma-common.h"

#define RPI_PICO_DMA_SLOT_PIO2_TX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x10)
#define RPI_PICO_DMA_SLOT_PIO2_TX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x11)
#define RPI_PICO_DMA_SLOT_PIO2_TX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x12)
#define RPI_PICO_DMA_SLOT_PIO2_TX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x13)
#define RPI_PICO_DMA_SLOT_PIO2_RX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x14)
#define RPI_PICO_DMA_SLOT_PIO2_RX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x15)
#define RPI_PICO_DMA_SLOT_PIO2_RX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x16)
#define RPI_PICO_DMA_SLOT_PIO2_RX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x17)
#define RPI_PICO_DMA_SLOT_SPI0_TX    RPI_PICO_DMA_DREQ_TO_SLOT(0x18)
#define RPI_PICO_DMA_SLOT_SPI0_RX    RPI_PICO_DMA_DREQ_TO_SLOT(0x19)
#define RPI_PICO_DMA_SLOT_SPI1_TX    RPI_PICO_DMA_DREQ_TO_SLOT(0x1A)
#define RPI_PICO_DMA_SLOT_SPI1_RX    RPI_PICO_DMA_DREQ_TO_SLOT(0x1B)
#define RPI_PICO_DMA_SLOT_UART0_TX   RPI_PICO_DMA_DREQ_TO_SLOT(0x1C)
#define RPI_PICO_DMA_SLOT_UART0_RX   RPI_PICO_DMA_DREQ_TO_SLOT(0x1D)
#define RPI_PICO_DMA_SLOT_UART1_TX   RPI_PICO_DMA_DREQ_TO_SLOT(0x1E)
#define RPI_PICO_DMA_SLOT_UART1_RX   RPI_PICO_DMA_DREQ_TO_SLOT(0x1F)
#define RPI_PICO_DMA_SLOT_PWM_WRAP0  RPI_PICO_DMA_DREQ_TO_SLOT(0x20)
#define RPI_PICO_DMA_SLOT_PWM_WRAP1  RPI_PICO_DMA_DREQ_TO_SLOT(0x21)
#define RPI_PICO_DMA_SLOT_PWM_WRAP2  RPI_PICO_DMA_DREQ_TO_SLOT(0x22)
#define RPI_PICO_DMA_SLOT_PWM_WRAP3  RPI_PICO_DMA_DREQ_TO_SLOT(0x23)
#define RPI_PICO_DMA_SLOT_PWM_WRAP4  RPI_PICO_DMA_DREQ_TO_SLOT(0x24)
#define RPI_PICO_DMA_SLOT_PWM_WRAP5  RPI_PICO_DMA_DREQ_TO_SLOT(0x25)
#define RPI_PICO_DMA_SLOT_PWM_WRAP6  RPI_PICO_DMA_DREQ_TO_SLOT(0x26)
#define RPI_PICO_DMA_SLOT_PWM_WRAP7  RPI_PICO_DMA_DREQ_TO_SLOT(0x27)
#define RPI_PICO_DMA_SLOT_PWM_WRAP8  RPI_PICO_DMA_DREQ_TO_SLOT(0x28)
#define RPI_PICO_DMA_SLOT_PWM_WRAP9  RPI_PICO_DMA_DREQ_TO_SLOT(0x29)
#define RPI_PICO_DMA_SLOT_PWM_WRAP10 RPI_PICO_DMA_DREQ_TO_SLOT(0x2A)
#define RPI_PICO_DMA_SLOT_PWM_WRAP11 RPI_PICO_DMA_DREQ_TO_SLOT(0x2B)
#define RPI_PICO_DMA_SLOT_I2C0_TX    RPI_PICO_DMA_DREQ_TO_SLOT(0x2C)
#define RPI_PICO_DMA_SLOT_I2C0_RX    RPI_PICO_DMA_DREQ_TO_SLOT(0x2D)
#define RPI_PICO_DMA_SLOT_I2C1_TX    RPI_PICO_DMA_DREQ_TO_SLOT(0x2E)
#define RPI_PICO_DMA_SLOT_I2C1_RX    RPI_PICO_DMA_DREQ_TO_SLOT(0x2F)
#define RPI_PICO_DMA_SLOT_ADC        RPI_PICO_DMA_DREQ_TO_SLOT(0x30)
#define RPI_PICO_DMA_SLOT_XIP_STREAM RPI_PICO_DMA_DREQ_TO_SLOT(0x31)
#define RPI_PICO_DMA_SLOT_XIP_QMITX  RPI_PICO_DMA_DREQ_TO_SLOT(0x32)
#define RPI_PICO_DMA_SLOT_XIP_QMIRX  RPI_PICO_DMA_DREQ_TO_SLOT(0x33)
#define RPI_PICO_DMA_SLOT_HSTX       RPI_PICO_DMA_DREQ_TO_SLOT(0x34)
#define RPI_PICO_DMA_SLOT_CORESIGHT  RPI_PICO_DMA_DREQ_TO_SLOT(0x35)
#define RPI_PICO_DMA_SLOT_SHA256     RPI_PICO_DMA_DREQ_TO_SLOT(0x36)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_RP2350_H_ */
```

## 724.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Manuel Aebischer <manuel.aebischer@belden.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_RP2350_H_`。

## 724.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2350_8h.html)
- [rpi-pico-dma-common.h](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h.html)

---

[上一章](P723_rpi-pico-dma-rp2040.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P725_rpi-pico-rp2040-pinctrl.h_源码浏览.md)
