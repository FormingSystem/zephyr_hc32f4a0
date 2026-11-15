---
id: learning.zephyr-docs.api-source-supplement-reference.page-153
title: r8a779f0_cpg_mssr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/r8a779f0__cpg__mssr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_r8a779f0\_cpg\_mssr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/r8a779f0__cpg__mssr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/r8a779f0__cpg__mssr_8h.html)。

## 153.1\_原始可见代码（Source Code）

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
<a id="adt-bindings_2clock_2renesas__cpg__mssr_8h_html"></a>

```c
/*
 * Copyright (c) 2023 IoT.bzh
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779F0_CPG_MSSR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779F0_CPG_MSSR_H_

#include "renesas_cpg_mssr.h"

/* r8a779f0 CPG Core Clocks */
#define R8A779F0_CLK_Z0                 0
#define R8A779F0_CLK_Z1                 1
#define R8A779F0_CLK_ZR                 2
#define R8A779F0_CLK_ZX                 3
#define R8A779F0_CLK_ZS                 4
#define R8A779F0_CLK_ZT                 5
#define R8A779F0_CLK_ZTR                6
#define R8A779F0_CLK_S0D2               7
#define R8A779F0_CLK_S0D3               8
#define R8A779F0_CLK_S0D4               9
#define R8A779F0_CLK_S0D2_MM            10
#define R8A779F0_CLK_S0D3_MM            11
#define R8A779F0_CLK_S0D4_MM            12
#define R8A779F0_CLK_S0D2_RT            13
#define R8A779F0_CLK_S0D3_RT            14
#define R8A779F0_CLK_S0D4_RT            15
#define R8A779F0_CLK_S0D6_RT            16
#define R8A779F0_CLK_S0D3_PER           17
#define R8A779F0_CLK_S0D6_PER           18
#define R8A779F0_CLK_S0D12_PER          19
#define R8A779F0_CLK_S0D24_PER          20
#define R8A779F0_CLK_S0D2_HSC           21
#define R8A779F0_CLK_S0D3_HSC           22
#define R8A779F0_CLK_S0D4_HSC           23
#define R8A779F0_CLK_S0D6_HSC           24
#define R8A779F0_CLK_S0D12_HSC          25
#define R8A779F0_CLK_S0D2_CC            26
#define R8A779F0_CLK_CL                 27
#define R8A779F0_CLK_CL16M              28
#define R8A779F0_CLK_CL16M_MM           29
#define R8A779F0_CLK_CL16M_RT           30
#define R8A779F0_CLK_CL16M_PER          31
#define R8A779F0_CLK_CL16M_HSC          32
#define R8A779F0_CLK_ZB3                33
#define R8A779F0_CLK_ZB3D2              34
#define R8A779F0_CLK_ZB3D4              35
#define R8A779F0_CLK_SD0H               36
#define R8A779F0_CLK_SD0                37
#define R8A779F0_CLK_RPC                38
#define R8A779F0_CLK_RPCD2              39
#define R8A779F0_CLK_MSO                40
#define R8A779F0_CLK_POST               41
#define R8A779F0_CLK_POST2              42
#define R8A779F0_CLK_SASYNCRT           43
#define R8A779F0_CLK_SASYNCPERD1        44
#define R8A779F0_CLK_SASYNCPERD2        45
#define R8A779F0_CLK_SASYNCPERD4        46
#define R8A779F0_CLK_DBGSOC_HSC         47
#define R8A779F0_CLK_RSW2               48
#define R8A779F0_CLK_CPEX               49
#define R8A779F0_CLK_CBFUSA             50
#define R8A779F0_CLK_R                  51
#define R8A779F0_CLK_OSC                52

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779F0_CPG_MSSR_H_ */
```

## 153.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 IoT.bzh。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

r8a779f0 时钟脉冲发生器（CPG）核心时钟。

### 注释 3：原第 67 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779F0_CPG_MSSR_H_`。

## 153.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/r8a779f0__cpg__mssr_8h.html)
- [renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2renesas__cpg__mssr_8h.html)

---

[上一章](P152_qdec_nxp_tpm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P154_r8a779g0_cpg_mssr.h_源码浏览.md)
