---
id: learning.zephyr-docs.api-source-supplement-reference.page-105
title: mchp-xec-dmac.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-dmac_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_mchp-xec-dmac.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-dmac_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-dmac_8h.html)。

## 105.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_MCHP_XEC_DMAC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_MCHP_XEC_DMAC_H_

#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB0_TARG 0x0
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB0_CTRL 0x1
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB1_TARG 0x2
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB1_CTRL 0x3
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB2_TARG 0x4
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB2_CTRL 0x5
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB3_TARG 0x6
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB3_CTRL 0x7
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB4_TARG 0x8
#define DMA_MCHP_XEC_TRIG_SRC_I2C_SMB4_CTRL 0x9
#define DMA_MCHP_XEC_TRIG_SRC_QMSPI0_TX     0xA
#define DMA_MCHP_XEC_TRIG_SRC_QMSPI0_RX     0xB
#define DMA_MCHP_XEC_TRIG_SRC_GPSPI0_TX     0xC
#define DMA_MCHP_XEC_TRIG_SRC_GPSPI0_RX     0xD
#define DMA_MCHP_XEC_TRIG_SRC_GPSPI1_TX     0xE
#define DMA_MCHP_XEC_TRIG_SRC_GPSPI1_RX     0xF
/* Additional channels for MEC175x */
#define DMA_MCHP_XEC_TRIG_SRC_I3C_HC0_TX    0x10
#define DMA_MCHP_XEC_TRIG_SRC_I3C_HC0_RX    0x11
#define DMA_MCHP_XEC_TRIG_SRC_I3C_SC0_TX    0x12
#define DMA_MCHP_XEC_TRIG_SRC_I3C_SC0_RX    0x13

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_MCHP_XEC_DMAC_H_ */
```

## 105.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

MEC175x 的附加通道。

### 注释 3：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_MCHP_XEC_DMAC_H_`。

## 105.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-dmac_8h.html)

---

[上一章](P104_mb_display.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P106_mchp_clock_control.h_源码浏览.md)
