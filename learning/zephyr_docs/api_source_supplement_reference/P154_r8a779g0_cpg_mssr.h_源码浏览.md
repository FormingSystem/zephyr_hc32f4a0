---
id: learning.zephyr-docs.api-source-supplement-reference.page-154
title: r8a779g0_cpg_mssr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/r8a779g0__cpg__mssr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第154章\_r8a779g0\_cpg\_mssr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/r8a779g0__cpg__mssr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/r8a779g0__cpg__mssr_8h.html)。

## 154.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
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
<a id="l00126"></a>
<a id="l00127"></a>
<a id="adt-bindings_2clock_2renesas__cpg__mssr_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779G0_CPG_MSSR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779G0_CPG_MSSR_H_

#include "renesas_cpg_mssr.h"

/* r8a779g0 CPG Core Clocks */
#define R8A779G0_CLK_Z0  0
#define R8A779G0_CLK_Z1  1
#define R8A779G0_CLK_Z2  2
#define R8A779G0_CLK_ZG  3
#define R8A779G0_CLK_ZR  4
#define R8A779G0_CLK_ZX  5
#define R8A779G0_CLK_ZS  6
#define R8A779G0_CLK_ZT  7
#define R8A779G0_CLK_ZTR 8

#define R8A779G0_CLK_S0   9
#define R8A779G0_CLK_S0D2 10
#define R8A779G0_CLK_S0D3 11
#define R8A779G0_CLK_S0D4 12

#define R8A779G0_CLK_S0VIO    13
#define R8A779G0_CLK_S0D1_VIO 14
#define R8A779G0_CLK_S0D2_VIO 15
#define R8A779G0_CLK_S0D4_VIO 16
#define R8A779G0_CLK_S0D8_VIO 17

#define R8A779G0_CLK_S0VC    18
#define R8A779G0_CLK_S0D1_VC 19
#define R8A779G0_CLK_S0D2_VC 20
#define R8A779G0_CLK_S0D4_VC 21

#define R8A779G0_CLK_S0D2_MM 22
#define R8A779G0_CLK_S0D4_MM 23

#define R8A779G0_CLK_S0D2_U3DG 24
#define R8A779G0_CLK_S0D4_U3DG 25

#define R8A779G0_CLK_S0D2_RT  26
#define R8A779G0_CLK_S0D3_RT  27
#define R8A779G0_CLK_S0D4_RT  28
#define R8A779G0_CLK_S0D6_RT  29
#define R8A779G0_CLK_S0D24_RT 30

#define R8A779G0_CLK_S0D2_PER  31
#define R8A779G0_CLK_S0D3_PER  32
#define R8A779G0_CLK_S0D4_PER  33
#define R8A779G0_CLK_S0D6_PER  34
#define R8A779G0_CLK_S0D12_PER 35
#define R8A779G0_CLK_S0D24_PER 36

#define R8A779G0_CLK_S0_HSC   37
#define R8A779G0_CLK_S0D1_HSC 38
#define R8A779G0_CLK_S0D2_HSC 39
#define R8A779G0_CLK_S0D4_HSC 40
#define R8A779G0_CLK_S0D8_HSC 41

#define R8A779G0_CLK_S0D2_CC  42
#define R8A779G0_CLK_SV_IR    43
#define R8A779G0_CLK_SVD1_IR  44
#define R8A779G0_CLK_SVD2_IR  45
#define R8A779G0_CLK_IMPA0    46
#define R8A779G0_CLK_SV_VIP   47
#define R8A779G0_CLK_SVD1_VIP 48
#define R8A779G0_CLK_SVD2_VIP 49

#define R8A779G0_CLK_CL        50
#define R8A779G0_CLK_CL16M     51
#define R8A779G0_CLK_CL16M_MM  52
#define R8A779G0_CLK_CL16M_RT  53
#define R8A779G0_CLK_CL16M_PER 54
#define R8A779G0_CLK_CL16M_HSC 55

#define R8A779G0_CLK_ZB3   56
#define R8A779G0_CLK_ZB3D2 57
#define R8A779G0_CLK_ZB3D4 58

#define R8A779G0_CLK_SDSRC 59
#define R8A779G0_CLK_SD0H  60
#define R8A779G0_CLK_SD0   61
#define R8A779G0_CLK_RPC   62
#define R8A779G0_CLK_RPCD2 63
#define R8A779G0_CLK_MSO   64
#define R8A779G0_CLK_CANFD 65
#define R8A779G0_CLK_CSI   66
#define R8A779G0_CLK_FRAY  67
#define R8A779G0_CLK_IPC   68
#define R8A779G0_CLK_POST2 69
#define R8A779G0_CLK_POST3 70
#define R8A779G0_CLK_POST4 71
#define R8A779G0_CLK_POST  72

#define R8A779G0_CLK_SASYNCRT    73
#define R8A779G0_CLK_SASYNCPERD1 74
#define R8A779G0_CLK_SASYNCPERD2 75
#define R8A779G0_CLK_SASYNCPERD4 76

#define R8A779G0_CLK_VIOBUS   77
#define R8A779G0_CLK_VIOBUSD2 78
#define R8A779G0_CLK_VCBUS    79
#define R8A779G0_CLK_VCBUSD2  80
#define R8A779G0_CLK_IMPA1    81
#define R8A779G0_CLK_DSIREF   82
#define R8A779G0_CLK_ADGH     83

#define R8A779G0_CLK_OSCCLK 84
#define R8A779G0_CLK_IMPA   85
#define R8A779G0_CLK_IMPAD4 86
#define R8A779G0_CLK_CPEX   87
#define R8A779G0_CLK_CP     88
#define R8A779G0_CLK_CBFUSA 89
#define R8A779G0_CLK_RCLK   90

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779G0_CPG_MSSR_H_ */
```

## 154.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 18 行

r8a779g0 时钟脉冲发生器（CPG）核心时钟。

### 注释 3：原第 127 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A779G0_CPG_MSSR_H_`。

## 154.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/r8a779g0__cpg__mssr_8h.html)
- [renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2renesas__cpg__mssr_8h.html)

---

[上一章](P153_r8a779f0_cpg_mssr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P155_r8a78000_cpg_mssr.h_源码浏览.md)
