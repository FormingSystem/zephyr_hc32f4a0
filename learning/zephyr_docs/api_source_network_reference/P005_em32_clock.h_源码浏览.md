---
id: learning.zephyr-docs.api-source-network-reference.page-5
title: em32_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/em32__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_em32\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/em32__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/em32__clock_8h.html)。

## 5.1\_原始可见代码（Source Code）

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
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>

```c
/*
 * SPDX-FileCopyrightText: 2025 ELAN Microelectronics Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_EM32_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_EM32_CLOCK_H_

/* Clock Source */
#define EM32_CLK_SRC_IRCLOW    0x00
#define EM32_CLK_SRC_IRCHIGH   0x01
#define EM32_CLK_SRC_EXTERNAL1 0x20

/* Clock Frequency Source */
#define EM32_CLK_FREQ_IRCLOW12   0x00
#define EM32_CLK_FREQ_IRCLOW16   0x01
#define EM32_CLK_FREQ_IRCLOW20   0x02
#define EM32_CLK_FREQ_IRCLOW24   0x03
#define EM32_CLK_FREQ_IRCLOW28   0x04
#define EM32_CLK_FREQ_IRCLOW32   0x05
#define EM32_CLK_FREQ_IRCHIGH64  0x11
#define EM32_CLK_FREQ_IRCHIGH80  0x12
#define EM32_CLK_FREQ_IRCHIGH96  0x13
#define EM32_CLK_FREQ_IRCHIGH112 0x14
#define EM32_CLK_FREQ_IRCHIGH128 0x15
#define EM32_CLK_FREQ_IRCHIGH96Q 0x16

/* AHB PreScaler */
#define EM32_AHB_CLK_DIV1   0x00
#define EM32_AHB_CLK_DIV2   0x01
#define EM32_AHB_CLK_DIV4   0x02
#define EM32_AHB_CLK_DIV8   0x03
#define EM32_AHB_CLK_DIV16  0x04
#define EM32_AHB_CLK_DIV32  0x05
#define EM32_AHB_CLK_DIV64  0x06
#define EM32_AHB_CLK_DIV128 0x07


/* HCLK Gating IDs */

#define EM32_GATE_HCLKG_DMA 0x00

#define EM32_GATE_HCLKG_GPIOA 0x01

#define EM32_GATE_HCLKG_GPIOB 0x02

#define EM32_GATE_HCLKG_7816_1 0x04

#define EM32_GATE_HCLKG_7816_2 0x05

#define EM32_GATE_HCLKG_ENCRYPT 0x06

#define EM32_GATE_HCLKG_ESPI1 0x0F

#define EM32_GATE_HCLKG_EXTSPI 0x1F

#define EM32_GATE_HCLKG_GHM_ACC1 0x20

#define EM32_GATE_HCLKG_GHM_ACC2 0x21

#define EM32_GATE_HCLKG_GHM_ACC3 0x22

/* HCLKF Gating IDs */

#define EM32_GATE_HCLKF_GHM_IP 0x23

#define EM32_GATE_HCLKF_FLASH_BIST 0x24

#define EM32_GATE_HCLKF_GHM_RANSAC 0x25

#define EM32_GATE_HCLKF_SWSPI 0x26

#define EM32_GATE_HCLKF_GHM_DOUBLE 0x27

#define EM32_GATE_HCLKF_GHM_DISTINGUISH 0x28

#define EM32_GATE_HCLKF_GHM_LSE 0x29

#define EM32_GATE_HCLKF_GHM_SAD 0x2A

#define EM32_GATE_HCLKF_GHM_M2D 0x2B

/* PCLK Gating IDs */

#define EM32_GATE_PCLKG_LPC 0x03

#define EM32_GATE_PCLKG_USART 0x07

#define EM32_GATE_PCLKG_TMR1 0x08

#define EM32_GATE_PCLKG_TMR2 0x09

#define EM32_GATE_PCLKG_TMR3 0x0A

#define EM32_GATE_PCLKG_TMR4 0x0B

#define EM32_GATE_PCLKG_UART1 0x0C

#define EM32_GATE_PCLKG_UART2 0x0D

#define EM32_GATE_PCLKG_RVD1 0x0E

#define EM32_GATE_PCLKG_SSP2 0x10

#define EM32_GATE_PCLKG_I2C1 0x11

#define EM32_GATE_PCLKG_I2C2 0x12

#define EM32_GATE_PCLKG_PWM 0x13

#define EM32_GATE_PCLKG_RVD2 0x14

#define EM32_GATE_PCLKG_UDC 0x15

#define EM32_GATE_PCLKG_ATRIM 0x16

#define EM32_GATE_PCLKG_RTC 0x17

#define EM32_GATE_PCLKG_BKP 0x18

#define EM32_GATE_PCLKG_DWG 0x19

#define EM32_GATE_PCLKG_PWR 0x1A

#define EM32_GATE_PCLKG_CACHE 0x1B

#define EM32_GATE_PCLKG_AIP 0x1C

#define EM32_GATE_PCLKG_ECC 0x1D

#define EM32_GATE_PCLKG_TRNG 0x1E

#define EM32_GATE_PCLKG_SSP1 0x30

/* Special IDs */

#define EM32_GATE_NONE 0xFFFE

#define EM32_GATE_PCLKG_ALL 0xFFFF


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_EM32_CLOCK_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2025 ELAN Microelectronics Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

时钟源（Clock Source）。

### 注释 3：原第 15 行

时钟频率源（Clock Frequency Source）。

### 注释 4：原第 29 行

高级高性能总线预分频器（AHB Prescaler）。

### 注释 5：原第 49 行

HCLK 门控标识（Gating IDs）。

### 注释 6：原第 84 行

HCLKF 门控标识（Gating IDs）。

### 注释 7：原第 113 行

PCLK 门控标识（Gating IDs）。

### 注释 8：原第 190 行

特殊标识（Special IDs）。

### 注释 9：原第 200 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_EM32_CLOCK_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/em32__clock_8h.html)

---

[上一章](P004_edac.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_ethernet_bridge.h_源码浏览.md)
