---
id: learning.zephyr-docs.api-source-supplement-reference.page-166
title: rpi-pico-dma-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_rpi-pico-dma-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h.html)。

## 166.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_COMMON_H_

/*
 * Use lower 6-bit of inverted DREQ value for `slot` cell.
 * Need to be able to work for memory-to-memory transfer
 * with zero, which is the default value.
 */
#define RPI_PICO_DMA_SLOT_TO_DREQ(s) (~(s)&0x3F)
#define RPI_PICO_DMA_DREQ_TO_SLOT    RPI_PICO_DMA_SLOT_TO_DREQ

#define RPI_PICO_DMA_SLOT_PIO0_TX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x00)
#define RPI_PICO_DMA_SLOT_PIO0_TX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x01)
#define RPI_PICO_DMA_SLOT_PIO0_TX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x02)
#define RPI_PICO_DMA_SLOT_PIO0_TX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x03)
#define RPI_PICO_DMA_SLOT_PIO0_RX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x04)
#define RPI_PICO_DMA_SLOT_PIO0_RX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x05)
#define RPI_PICO_DMA_SLOT_PIO0_RX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x06)
#define RPI_PICO_DMA_SLOT_PIO0_RX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x07)
#define RPI_PICO_DMA_SLOT_PIO1_TX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x08)
#define RPI_PICO_DMA_SLOT_PIO1_TX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x09)
#define RPI_PICO_DMA_SLOT_PIO1_TX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x0A)
#define RPI_PICO_DMA_SLOT_PIO1_TX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x0B)
#define RPI_PICO_DMA_SLOT_PIO1_RX0   RPI_PICO_DMA_DREQ_TO_SLOT(0x0C)
#define RPI_PICO_DMA_SLOT_PIO1_RX1   RPI_PICO_DMA_DREQ_TO_SLOT(0x0D)
#define RPI_PICO_DMA_SLOT_PIO1_RX2   RPI_PICO_DMA_DREQ_TO_SLOT(0x0E)
#define RPI_PICO_DMA_SLOT_PIO1_RX3   RPI_PICO_DMA_DREQ_TO_SLOT(0x0F)

#define RPI_PICO_DMA_SLOT_DMA_TIMER0 RPI_PICO_DMA_DREQ_TO_SLOT(0x3B)
#define RPI_PICO_DMA_SLOT_DMA_TIMER1 RPI_PICO_DMA_DREQ_TO_SLOT(0x3C)
#define RPI_PICO_DMA_SLOT_DMA_TIMER2 RPI_PICO_DMA_DREQ_TO_SLOT(0x3D)
#define RPI_PICO_DMA_SLOT_DMA_TIMER3 RPI_PICO_DMA_DREQ_TO_SLOT(0x3E)
#define RPI_PICO_DMA_SLOT_FORCE      RPI_PICO_DMA_DREQ_TO_SLOT(0x3F)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_COMMON_H_ */
```

## 166.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

将 DREQ 值按位取反后的低 6 位用于 `slot` 单元。此编码必须能够处理值为零的内存到内存传输（Memory-to-memory transfer）；零也是默认值。

### 注释 3：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RPI_PICO_DMA_COMMON_H_`。

## 166.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-common_8h.html)

---

[上一章](P165_rp1-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P167_rpi-pico-rp2350a-pinctrl.h_源码浏览.md)
