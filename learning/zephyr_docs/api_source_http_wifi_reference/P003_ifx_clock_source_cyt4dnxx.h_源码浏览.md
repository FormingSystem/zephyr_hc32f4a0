---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-3
title: ifx_clock_source_cyt4dnxx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__cyt4dnxx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_ifx\_clock\_source\_cyt4dnxx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__cyt4dnxx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P144_zephyr__dt-bindings__clock__ifx_clock_source_cyt4dnxx.h_文件参考.md)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * Peripheral clock (PCLK) root clock ids for CYT4DN (TRAVEO(TM) T2G) devices.
 *
 * Each value is the peripheral's output index within its PERI_PCLK group.
 * Refer to the device datasheet, section 20 "Peripheral clocks", for details.
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_CYT4DNXX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_CYT4DNXX_H_

/* CPUSS root clocks (PERI group 0, use under clk_peri0) */
#define IFX_PCLK_CPUSS_TRACE_IN    0    /* Trace clock */
#define IFX_PCLK_SMARTIO7          1    /* Smart I/O #7 */

/* TCPWM0 counters (output = datasheet Table 20-1) */
#define IFX_PCLK_TCPWM0_GRP0_CNT0  2
#define IFX_PCLK_TCPWM0_GRP0_CNT1  3
#define IFX_PCLK_TCPWM0_GRP0_CNT2  4
#define IFX_PCLK_TCPWM0_GRP0_CNT3  5
#define IFX_PCLK_TCPWM0_GRP0_CNT4  6
#define IFX_PCLK_TCPWM0_GRP0_CNT5  7
#define IFX_PCLK_TCPWM0_GRP0_CNT6  8
#define IFX_PCLK_TCPWM0_GRP0_CNT7  9
#define IFX_PCLK_TCPWM0_GRP0_CNT8  10
#define IFX_PCLK_TCPWM0_GRP0_CNT9  11
#define IFX_PCLK_TCPWM0_GRP0_CNT10 12
#define IFX_PCLK_TCPWM0_GRP0_CNT11 13
#define IFX_PCLK_TCPWM0_GRP0_CNT12 14
#define IFX_PCLK_TCPWM0_GRP0_CNT13 15
#define IFX_PCLK_TCPWM0_GRP0_CNT14 16
#define IFX_PCLK_TCPWM0_GRP0_CNT15 17
#define IFX_PCLK_TCPWM0_GRP0_CNT16 18
#define IFX_PCLK_TCPWM0_GRP0_CNT17 19
#define IFX_PCLK_TCPWM0_GRP0_CNT18 20
#define IFX_PCLK_TCPWM0_GRP0_CNT19 21
#define IFX_PCLK_TCPWM0_GRP0_CNT20 22
#define IFX_PCLK_TCPWM0_GRP0_CNT21 23
#define IFX_PCLK_TCPWM0_GRP0_CNT22 24
#define IFX_PCLK_TCPWM0_GRP0_CNT23 25
#define IFX_PCLK_TCPWM0_GRP0_CNT24 26
#define IFX_PCLK_TCPWM0_GRP0_CNT25 27
#define IFX_PCLK_TCPWM0_GRP0_CNT26 28
#define IFX_PCLK_TCPWM0_GRP0_CNT27 29
#define IFX_PCLK_TCPWM0_GRP0_CNT28 30
#define IFX_PCLK_TCPWM0_GRP0_CNT29 31
#define IFX_PCLK_TCPWM0_GRP0_CNT30 32
#define IFX_PCLK_TCPWM0_GRP0_CNT31 33
#define IFX_PCLK_TCPWM0_GRP0_CNT32 34
#define IFX_PCLK_TCPWM0_GRP0_CNT33 35
#define IFX_PCLK_TCPWM0_GRP0_CNT34 36
#define IFX_PCLK_TCPWM0_GRP0_CNT35 37
#define IFX_PCLK_TCPWM0_GRP0_CNT36 38
#define IFX_PCLK_TCPWM0_GRP0_CNT37 39

#define IFX_PCLK_TCPWM0_GRP1_CNT0  40
#define IFX_PCLK_TCPWM0_GRP1_CNT1  41
#define IFX_PCLK_TCPWM0_GRP1_CNT2  42
#define IFX_PCLK_TCPWM0_GRP1_CNT3  43
#define IFX_PCLK_TCPWM0_GRP1_CNT4  44
#define IFX_PCLK_TCPWM0_GRP1_CNT5  45
#define IFX_PCLK_TCPWM0_GRP1_CNT6  46
#define IFX_PCLK_TCPWM0_GRP1_CNT7  47
#define IFX_PCLK_TCPWM0_GRP1_CNT8  48
#define IFX_PCLK_TCPWM0_GRP1_CNT9  49
#define IFX_PCLK_TCPWM0_GRP1_CNT10 50
#define IFX_PCLK_TCPWM0_GRP1_CNT11 51

#define IFX_PCLK_TCPWM0_GRP2_CNT0  52
#define IFX_PCLK_TCPWM0_GRP2_CNT1  53
#define IFX_PCLK_TCPWM0_GRP2_CNT2  54
#define IFX_PCLK_TCPWM0_GRP2_CNT3  55
#define IFX_PCLK_TCPWM0_GRP2_CNT4  56
#define IFX_PCLK_TCPWM0_GRP2_CNT5  57
#define IFX_PCLK_TCPWM0_GRP2_CNT6  58
#define IFX_PCLK_TCPWM0_GRP2_CNT7  59
#define IFX_PCLK_TCPWM0_GRP2_CNT8  60
#define IFX_PCLK_TCPWM0_GRP2_CNT9  61
#define IFX_PCLK_TCPWM0_GRP2_CNT10 62
#define IFX_PCLK_TCPWM0_GRP2_CNT11 63
#define IFX_PCLK_TCPWM0_GRP2_CNT12 64
#define IFX_PCLK_TCPWM0_GRP2_CNT13 65
#define IFX_PCLK_TCPWM0_GRP2_CNT14 66
#define IFX_PCLK_TCPWM0_GRP2_CNT15 67
#define IFX_PCLK_TCPWM0_GRP2_CNT16 68
#define IFX_PCLK_TCPWM0_GRP2_CNT17 69
#define IFX_PCLK_TCPWM0_GRP2_CNT18 70
#define IFX_PCLK_TCPWM0_GRP2_CNT19 71
#define IFX_PCLK_TCPWM0_GRP2_CNT20 72
#define IFX_PCLK_TCPWM0_GRP2_CNT21 73
#define IFX_PCLK_TCPWM0_GRP2_CNT22 74
#define IFX_PCLK_TCPWM0_GRP2_CNT23 75
#define IFX_PCLK_TCPWM0_GRP2_CNT24 76
#define IFX_PCLK_TCPWM0_GRP2_CNT25 77
#define IFX_PCLK_TCPWM0_GRP2_CNT26 78
#define IFX_PCLK_TCPWM0_GRP2_CNT27 79
#define IFX_PCLK_TCPWM0_GRP2_CNT28 80
#define IFX_PCLK_TCPWM0_GRP2_CNT29 81
#define IFX_PCLK_TCPWM0_GRP2_CNT30 82
#define IFX_PCLK_TCPWM0_GRP2_CNT31 83

/* COMM root clocks (PERI group 1, use under clk_peri1) */
#define IFX_PCLK_CANFD0_CH0        0    /* CAN0, channel 0 */
#define IFX_PCLK_CANFD0_CH1        1    /* CAN0, channel 1 */
#define IFX_PCLK_CANFD1_CH0        2    /* CAN1, channel 0 */
#define IFX_PCLK_CANFD1_CH1        3    /* CAN1, channel 1 */
#define IFX_PCLK_LIN0_CH0          4    /* LIN0, channel 0 */
#define IFX_PCLK_LIN0_CH1          5    /* LIN0, channel 1 */
#define IFX_PCLK_CXPI0_CH0         6    /* CXPI0, channel 0 */
#define IFX_PCLK_CXPI0_CH1         7    /* CXPI0, channel 1 */
#define IFX_PCLK_SCB0              8    /* SCB0 */
#define IFX_PCLK_SCB1              9    /* SCB1 */
#define IFX_PCLK_SCB2              10   /* SCB2 */
#define IFX_PCLK_SCB3              11   /* SCB3 */
#define IFX_PCLK_SCB4              12   /* SCB4 */
#define IFX_PCLK_SCB5              13   /* SCB5 */
#define IFX_PCLK_SCB6              14   /* SCB6 */
#define IFX_PCLK_SCB7              15   /* SCB7 */
#define IFX_PCLK_SCB8              16   /* SCB8 */
#define IFX_PCLK_SCB9              17   /* SCB9 */
#define IFX_PCLK_SCB10             18   /* SCB10 */
#define IFX_PCLK_SCB11             19   /* SCB11 */
#define IFX_PCLK_SAR0              20   /* PASS0 SAR0 */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_CYT4DNXX_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

CYT4DN（TRAVEO(TM) T2G）设备的外设时钟（PCLK）根时钟标识（Root Clock IDs）。每个值均为外设在所属 `PERI_PCLK` 组内的输出索引。详情参见设备数据手册第 20 节“外设时钟”（Peripheral Clocks）。

### 注释 3：原第 17 行

CPU 子系统（CPUSS）根时钟，属于 PERI 组 0，在 `clk_peri0` 下使用。

### 注释 4：原第 18 行

跟踪时钟（Trace Clock）。

### 注释 5：原第 19 行

智能输入输出（Smart I/O）7。

### 注释 6：原第 21 行

TCPWM0 计数器（Counters），输出编号见数据手册表 20-1。

### 注释 7：原第 107 行

通信子系统（COMM）根时钟，属于 PERI 组 1，在 `clk_peri1` 下使用。

### 注释 8：原第 108 行

CAN0，通道 0（Channel 0）。

### 注释 9：原第 109 行

CAN0，通道 1（Channel 1）。

### 注释 10：原第 110 行

CAN1，通道 0（Channel 0）。

### 注释 11：原第 111 行

CAN1，通道 1（Channel 1）。

### 注释 12：原第 112 行

LIN0，通道 0（Channel 0）。

### 注释 13：原第 113 行

LIN0，通道 1（Channel 1）。

### 注释 14：原第 114 行

CXPI0，通道 0（Channel 0）。

### 注释 15：原第 115 行

CXPI0，通道 1（Channel 1）。

### 注释 16：原第 116 行

串行通信模块（Serial Communication Block）：`SCB0`。

### 注释 17：原第 117 行

串行通信模块（Serial Communication Block）：`SCB1`。

### 注释 18：原第 118 行

串行通信模块（Serial Communication Block）：`SCB2`。

### 注释 19：原第 119 行

串行通信模块（Serial Communication Block）：`SCB3`。

### 注释 20：原第 120 行

串行通信模块（Serial Communication Block）：`SCB4`。

### 注释 21：原第 121 行

串行通信模块（Serial Communication Block）：`SCB5`。

### 注释 22：原第 122 行

串行通信模块（Serial Communication Block）：`SCB6`。

### 注释 23：原第 123 行

串行通信模块（Serial Communication Block）：`SCB7`。

### 注释 24：原第 124 行

串行通信模块（Serial Communication Block）：`SCB8`。

### 注释 25：原第 125 行

串行通信模块（Serial Communication Block）：`SCB9`。

### 注释 26：原第 126 行

串行通信模块（Serial Communication Block）：`SCB10`。

### 注释 27：原第 127 行

串行通信模块（Serial Communication Block）：`SCB11`。

### 注释 28：原第 128 行

可编程模拟子系统 PASS0 的逐次逼近转换器 SAR0。

### 注释 29：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_CYT4DNXX_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P144_zephyr__dt-bindings__clock__ifx_clock_source_cyt4dnxx.h_文件参考.md)

---

[上一章](P002_amebadplus_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_intc_esp32.h_源码浏览.md)
