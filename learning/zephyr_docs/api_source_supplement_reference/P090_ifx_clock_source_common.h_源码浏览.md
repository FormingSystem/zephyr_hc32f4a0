---
id: learning.zephyr-docs.api-source-supplement-reference.page-90
title: ifx_clock_source_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_ifx\_clock\_source\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h.html)。

## 90.1\_原始可见代码（Source Code）

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

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_COMMON_H_

#define CLK_SOURCE_IHO
#define CLK_SOURCE_PILO

#define IFX_IHO           1
#define IFX_IMO           2
#define IFX_ECO           3
#define IFX_EXT           4
#define IFX_ALTHF         5
#define IFX_ALTLF         6
#define IFX_ILO           7
#define IFX_PILO          8
#define IFX_WCO           9
#define IFX_MFO           10
#define IFX_PATHMUX       11
#define IFX_FLL           12
#define IFX_PLL200        13
#define IFX_PLL400        14
#define IFX_ECO_PRESCALER 15
#define IFX_LF            16
#define IFX_MF            17
#define IFX_HF            18
#define IFX_PUMP          19
#define IFX_BAK           20
#define IFX_ALT_SYS_TICK  21
#define IFX_PERI          22
#define IFX_DPLL250_0     23
#define IFX_DPLL250_1     24
#define IFX_DPLL500       25

#define IFX_CLK_HF_NO_DIVIDE    0
#define IFX_CLK_HF_DIVIDE_BY_2  1
#define IFX_CLK_HF_DIVIDE_BY_3  2
#define IFX_CLK_HF_DIVIDE_BY_4  3
#define IFX_CLK_HF_DIVIDE_BY_5  4
#define IFX_CLK_HF_DIVIDE_BY_6  5
#define IFX_CLK_HF_DIVIDE_BY_7  6
#define IFX_CLK_HF_DIVIDE_BY_8  7
#define IFX_CLK_HF_DIVIDE_BY_9  8
#define IFX_CLK_HF_DIVIDE_BY_10 9
#define IFX_CLK_HF_DIVIDE_BY_11 10
#define IFX_CLK_HF_DIVIDE_BY_12 11
#define IFX_CLK_HF_DIVIDE_BY_13 12
#define IFX_CLK_HF_DIVIDE_BY_14 13
#define IFX_CLK_HF_DIVIDE_BY_15 14
#define IFX_CLK_HF_DIVIDE_BY_16 15
#define IFX_CLK_HF_MAX_DIVIDER

#define IFX_CLK_HF_IN_CLKPATH0  0
#define IFX_CLK_HF_IN_CLKPATH1  1
#define IFX_CLK_HF_IN_CLKPATH2  2
#define IFX_CLK_HF_IN_CLKPATH3  3
#define IFX_CLK_HF_IN_CLKPATH4  4
#define IFX_CLK_HF_IN_CLKPATH5  5
#define IFX_CLK_HF_IN_CLKPATH6  6
#define IFX_CLK_HF_IN_CLKPATH7  7
#define IFX_CLK_HF_IN_CLKPATH8  8
#define IFX_CLK_HF_IN_CLKPATH9  9
#define IFX_CLK_HF_IN_CLKPATH10 10
#define IFX_CLK_HF_IN_CLKPATH11 11
#define IFX_CLK_HF_IN_CLKPATH12 12
#define IFX_CLK_HF_IN_CLKPATH13 13
#define IFX_CLK_HF_IN_CLKPATH14 14
#define IFX_CLK_HF_IN_CLKPATH15 15

/* Target resource types for peripheral dividers */
#define IFX_RSC_ADC     0
#define IFX_RSC_ADCMIC  1
#define IFX_RSC_BLESS   2
#define IFX_RSC_CAN     3
#define IFX_RSC_CLKPATH 4
#define IFX_RSC_CLOCK   5
#define IFX_RSC_CRYPTO  6
#define IFX_RSC_DAC     7
#define IFX_RSC_DMA     8
#define IFX_RSC_DW      9
#define IFX_RSC_ETH     10
#define IFX_RSC_GPIO    11
#define IFX_RSC_I2S     12
#define IFX_RSC_I3C     13
#define IFX_RSC_KEYSCAN 14
#define IFX_RSC_LCD     15
#define IFX_RSC_LIN     16
#define IFX_RSC_LPCOMP  17
#define IFX_RSC_LPTIMER 18
#define IFX_RSC_OPAMP   19
#define IFX_RSC_PDM     20
#define IFX_RSC_PTC     21
#define IFX_RSC_SMIF    22
#define IFX_RSC_RTC     23
#define IFX_RSC_SCB     24
#define IFX_RSC_SDHC    25
#define IFX_RSC_SDIODEV 26
#define IFX_RSC_TCPWM   27
#define IFX_RSC_TDM     28
#define IFX_RSC_UDB     29
#define IFX_RSC_USB     30
#define IFX_RSC_INVALID 31

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_COMMON_H_ */
```

## 90.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

外设分频器（Peripheral dividers）的目标资源类型。

### 注释 3：原第 109 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_COMMON_H_`。

## 90.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__common_8h.html)

---

[上一章](P089_i2s.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P091_img_mgmt_callbacks.h_源码浏览.md)
