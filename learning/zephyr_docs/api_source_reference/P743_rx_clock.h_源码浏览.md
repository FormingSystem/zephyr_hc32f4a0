---
id: learning.zephyr-docs.api-source-reference.page-743
title: rx_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第743章\_rx\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html)。

## 743.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
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
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>

```c
/*
 * Copyright (c) 2024 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RX_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RX_CLOCK_H_


#define RX_CLOCKS_SOURCE_CLOCK_LOCO     0
#define RX_CLOCKS_SOURCE_CLOCK_HOCO     1
#define RX_CLOCKS_SOURCE_CLOCK_MAIN_OSC 2
#define RX_CLOCKS_SOURCE_CLOCK_SUBCLOCK 3
#define RX_CLOCKS_SOURCE_PLL            4
#define RX_CLOCKS_SOURCE_CLOCK_DISABLE  0xff


#define RX_IF_CLOCKS_SOURCE_CLOCK_HOCO 0
#define RX_IF_CLOCKS_SOURCE_CLOCK_LOCO 2
#define RX_IF_CLOCKS_SOURCE_PLL        5
#define RX_IF_CLOCKS_SOURCE_PLL2       6


#define RX_LPT_CLOCKS_SOURCE_CLOCK_SUBCLOCK       0
#define RX_LPT_CLOCKS_SOURCE_CLOCK_IWDT_LOW_SPEED 1
#define RX_LPT_CLOCKS_NON_USE                     2
#define RX_LPT_CLOCKS_SOURCE_CLOCK_LOCO           3


#ifdef CONFIG_SOC_SERIES_RX26T
#define RX_PLL_CLOCKS_SOURCE_CLOCK_MAIN_OSC 0
#define RX_PLL_CLOCKS_SOURCE_CLOCK_HOCO     1
#endif /* CONFIG_SOC_SERIES_RX26T */


#define RX_PLL_MUL_4   7
#define RX_PLL_MUL_4_5 8
#define RX_PLL_MUL_5   9
#define RX_PLL_MUL_5_5 10
#define RX_PLL_MUL_6   11
#define RX_PLL_MUL_6_5 12
#define RX_PLL_MUL_7   13
#define RX_PLL_MUL_7_5 14
#define RX_PLL_MUL_8   15
#define RX_PLL_MUL_10   19
#define RX_PLL_MUL_10_5 20
#define RX_PLL_MUL_11   21
#define RX_PLL_MUL_11_5 22
#define RX_PLL_MUL_12   23
#define RX_PLL_MUL_12_5 24
#define RX_PLL_MUL_13   25
#define RX_PLL_MUL_13_5 26
#define RX_PLL_MUL_14   27
#define RX_PLL_MUL_14_5 28
#define RX_PLL_MUL_15   29
#define RX_PLL_MUL_15_5 30
#define RX_PLL_MUL_16   31
#define RX_PLL_MUL_16_5 32
#define RX_PLL_MUL_17   33
#define RX_PLL_MUL_17_5 34
#define RX_PLL_MUL_18   35
#define RX_PLL_MUL_18_5 36
#define RX_PLL_MUL_19   37
#define RX_PLL_MUL_19_5 38
#define RX_PLL_MUL_20   39
#define RX_PLL_MUL_20_5 40
#define RX_PLL_MUL_21   41
#define RX_PLL_MUL_21_5 42
#define RX_PLL_MUL_22   43
#define RX_PLL_MUL_22_5 44
#define RX_PLL_MUL_23   45
#define RX_PLL_MUL_23_5 46
#define RX_PLL_MUL_24   47
#define RX_PLL_MUL_24_5 48
#define RX_PLL_MUL_25   49
#define RX_PLL_MUL_25_5 50
#define RX_PLL_MUL_26   51
#define RX_PLL_MUL_26_5 52
#define RX_PLL_MUL_27   53
#define RX_PLL_MUL_27_5 54
#define RX_PLL_MUL_28   55
#define RX_PLL_MUL_28_5 56
#define RX_PLL_MUL_29   57
#define RX_PLL_MUL_29_5 58
#define RX_PLL_MUL_30   59


#define MSTPA 0
#define MSTPB 1
#define MSTPC 2
#define MSTPD 3
#define MSTPE 4
#define MSTPF 5


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RX_CLOCK_H_ */
```

## 743.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

条件编译配置（Configuration）标记：`CONFIG_SOC_SERIES_RX26T`。

### 注释 3：原第 136 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RX_CLOCK_H_`。

## 743.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html)

---

[上一章](P742_rv32m1-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P744_s3km1110.h_源码浏览.md)
