---
id: learning.zephyr-docs.api-source-supplement-reference.page-107
title: mchp_mss_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__mss__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_mchp\_mss\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__mss__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__mss__reset_8h.html)。

## 107.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (C) 2025 embedded brains GmbH & Co. KG
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_MCHP_MSS_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_MCHP_MSS_RESET_H_

/*
 * The reset ID encodes the bit index of the SUBBLK_CLOCK_CR and SOFT_RESET_CR
 * registers associated with the device.
 */
#define MSS_RESET_ID_ENVM    0x0
#define MSS_RESET_ID_MAC0    0x1
#define MSS_RESET_ID_MAC1    0x2
#define MSS_RESET_ID_MMC     0x3
#define MSS_RESET_ID_TIMER   0x4
#define MSS_RESET_ID_MMUART0 0x5
#define MSS_RESET_ID_MMUART1 0x6
#define MSS_RESET_ID_MMUART2 0x7
#define MSS_RESET_ID_MMUART3 0x8
#define MSS_RESET_ID_MMUART4 0x9
#define MSS_RESET_ID_SPI0    0xa
#define MSS_RESET_ID_SPI1    0xb
#define MSS_RESET_ID_I2C0    0xc
#define MSS_RESET_ID_I2C1    0xd
#define MSS_RESET_ID_CAN0    0xe
#define MSS_RESET_ID_CAN1    0xf
#define MSS_RESET_ID_USB     0x10
#define MSS_RESET_ID_RSVD    0x11
#define MSS_RESET_ID_RTC     0x12
#define MSS_RESET_ID_QSPI    0x13
#define MSS_RESET_ID_GPIO0   0x14
#define MSS_RESET_ID_GPIO1   0x15
#define MSS_RESET_ID_GPIO2   0x16
#define MSS_RESET_ID_DDRC    0x17
#define MSS_RESET_ID_FIC0    0x18
#define MSS_RESET_ID_FIC1    0x19
#define MSS_RESET_ID_FIC2    0x1a
#define MSS_RESET_ID_FIC3    0x1b
#define MSS_RESET_ID_ATHENA  0x1c
#define MSS_RESET_ID_CFM     0x1d

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_MCHP_MSS_RESET_H_ */
```

## 107.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 embedded brains GmbH & Co. KG。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

复位标识符（Reset ID）编码了与设备关联的 `SUBBLK_CLOCK_CR` 和 `SOFT_RESET_CR` 寄存器中的位索引。

### 注释 3：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_MCHP_MSS_RESET_H_`。

## 107.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__mss__reset_8h.html)

---

[上一章](P106_mchp_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P108_mcs.h_源码浏览.md)
