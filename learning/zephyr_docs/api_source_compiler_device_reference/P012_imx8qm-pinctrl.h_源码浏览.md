---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-12
title: imx8qm-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx8qm-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_imx8qm-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx8qm-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P148_zephyr__dt-bindings__pinctrl__imx8qm-pinctrl.h_文件参考.md)。

## 12.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright 2023, 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IMX8QM_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IMX8QM_PINCTRL_H_

/* values for pad field */
#define SC_P_UART0_RTS_B 23
#define SC_P_UART0_CTS_B 24
#define SC_P_ESAI0_FSR 104
#define SC_P_ESAI0_FST 105
#define SC_P_ESAI0_SCKR 106
#define SC_P_ESAI0_SCKT 107
#define SC_P_ESAI0_TX0 108
#define SC_P_ESAI0_TX1 109
#define SC_P_ESAI0_TX2_RX3 110
#define SC_P_ESAI0_TX3_RX2 111
#define SC_P_ESAI0_TX4_RX1 112
#define SC_P_ESAI0_TX5_RX0 113
#define SC_P_SAI1_RXD 128
#define SC_P_SAI1_TXC 130
#define SC_P_SAI1_TXD 131
#define SC_P_SAI1_TXFS 132

/* mux values */
#define IMX8QM_DMA_LPUART2_RX_UART0_RTS_B 2 /* UART0_RTS_B ---> DMA_LPUART2_RX */
#define IMX8QM_DMA_LPUART2_TX_UART0_CTS_B 2 /* DMA_LPUART2_TX ---> UART0_CTS_B */
#define IMX8QM_AUD_SAI1_RXD_SAI1_RXD 0 /* AUD_SAI1_RXD <--- SAI1_RXD */
#define IMX8QM_AUD_SAI1_TXC_SAI1_TXC 0 /* AUD_SAI1_TXC <---> SAI1_TXC */
#define IMX8QM_AUD_SAI1_TXD_SAI1_TXD 0 /* AUD_SAI1_TXD ---> SAI1_TXD */
#define IMX8QM_AUD_SAI1_TXFS_SAI1_TXFS 0 /* AUD_SAI1_TXFS <---> SAI1_TXFS */
#define IMX8QM_AUD_ESAI0_FSR_ESAI0_FSR 0
#define IMX8QM_AUD_ESAI0_FST_ESAI0_FST 0
#define IMX8QM_AUD_ESAI0_SCKR_ESAI0_SCKR 0
#define IMX8QM_AUD_ESAI0_SCKT_ESAI0_SCKT 0
#define IMX8QM_AUD_ESAI0_TX0_ESAI_TX0 0
#define IMX8QM_AUD_ESAI0_TX1_ESAI_TX1 0
#define IMX8QM_AUD_ESAI0_TX2_RX3_ESAI0_TX2_RX3 0
#define IMX8QM_AUD_ESAI0_TX3_RX2_ESAI0_TX3_RX2 0
#define IMX8QM_AUD_ESAI0_TX4_RX1_ESAI0_TX4_RX1 0
#define IMX8QM_AUD_ESAI0_TX5_RX0_ESAI0_TX5_RX0 0

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IMX8QM_PINCTRL_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023, 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

焊盘字段（pad field）的取值。

### 注释 3：原第 28 行

复用（mux）取值。

### 注释 4：原第 29 行

信号连接方向：`UART0_RTS_B ---> DMA_LPUART2_RX`。

### 注释 5：原第 30 行

信号连接方向：`DMA_LPUART2_TX ---> UART0_CTS_B`。

### 注释 6：原第 31 行

信号连接方向：`AUD_SAI1_RXD <--- SAI1_RXD`。

### 注释 7：原第 32 行

信号连接方向：`AUD_SAI1_TXC <---> SAI1_TXC`。

### 注释 8：原第 33 行

信号连接方向：`AUD_SAI1_TXD ---> SAI1_TXD`。

### 注释 9：原第 34 行

信号连接方向：`AUD_SAI1_TXFS <---> SAI1_TXFS`。

### 注释 10：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IMX8QM_PINCTRL_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P148_zephyr__dt-bindings__pinctrl__imx8qm-pinctrl.h_文件参考.md)

---

[上一章](P011_gd32_dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_imx8qxp-pinctrl.h_源码浏览.md)
