---
id: learning.zephyr-docs.api-source-reference.page-367
title: infineon-autanalog-ctb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第367章\_infineon-autanalog-ctb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h.html)。

## 367.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
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
<a id="l00077"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_OPAMP_INFINEON_AUTANALOG_CTB_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_OPAMP_INFINEON_AUTANALOG_CTB_H_

#define IFX_AUTANALOG_CTB_OA_PWR_OFF             0
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW       1
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL  2
#define IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL        4
#define IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL     6
#define IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL       8
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL 10

#define IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR      0
#define IFX_AUTANALOG_CTB_OA_TOPO_PGA             1
#define IFX_AUTANALOG_CTB_OA_TOPO_TIA             2
#define IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP 3
#define IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER  4
#define IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR 5
#define IFX_AUTANALOG_CTB_OA_TOPO_BUFFER          6

#define IFX_AUTANALOG_CTB_COMP_INT_DISABLED     0
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_RISING  1
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_FALLING 2
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_BOTH    3

#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_pF    0
#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_7_pF  1
#define IFX_AUTANALOG_CTB_OA_FB_CAP_1_4_pF  2
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_1_pF  3
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_8_pF  4
#define IFX_AUTANALOG_CTB_OA_FB_CAP_3_5_pF  5
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_2_pF  6
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_9_pF  7
#define IFX_AUTANALOG_CTB_OA_FB_CAP_5_6_pF  8
#define IFX_AUTANALOG_CTB_OA_FB_CAP_6_3_pF  9
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_0_pF  10
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_7_pF  11
#define IFX_AUTANALOG_CTB_OA_FB_CAP_8_4_pF  12
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_1_pF  13
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_8_pF  14
#define IFX_AUTANALOG_CTB_OA_FB_CAP_10_5_pF 15

#define IFX_AUTANALOG_CTB_OA_CC_CAP_0_1_pF   0
#define IFX_AUTANALOG_CTB_OA_CC_CAP_1_1_pF   1
#define IFX_AUTANALOG_CTB_OA_CC_CAP_2_1_pF   2
#define IFX_AUTANALOG_CTB_OA_CC_CAP_3_1_pF   3
#define IFX_AUTANALOG_CTB_OA_CC_CAP_4_1_pF   4
#define IFX_AUTANALOG_CTB_OA_CC_CAP_5_1_pF   5
#define IFX_AUTANALOG_CTB_OA_CC_CAP_6_1_pF   6
#define IFX_AUTANALOG_CTB_OA_CC_CAP_7_1_pF   7
#define IFX_AUTANALOG_CTB_OA_CC_CAP_DISABLED 8

#define IFX_AUTANALOG_CTB_OA_NINV_PIN_DISCONNECT    0
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5 1
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4 2

#define IFX_AUTANALOG_CTB_OA_NINV_REF_DISCONNECT  0
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC0        1
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC1        2
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT0    3
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT1    4
#define IFX_AUTANALOG_CTB_OA_NINV_REF_VBGR        5
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA0_OUT 6
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA1_OUT 7

#define IFX_AUTANALOG_CTB_OA_INV_PIN_DISCONNECT    0
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P0_OA1_P5 1
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P1_OA1_P4 2

#define IFX_AUTANALOG_CTB_OA_RES_PIN_DISCONNECT    0
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P0_OA1_P5 1
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P1_OA1_P4 2

#define IFX_AUTANALOG_CTB_OA_RES_REF_DISCONNECT  0
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC0        1
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC1        2
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA0_OUT 3
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA1_OUT 4
#define IFX_AUTANALOG_CTB_OA_RES_REF_VSSA        5

#define IFX_AUTANALOG_CTB_OA_MUX_IN_DISCONNECT 0
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P0         1
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P1         2
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P2         3
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P3         4
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P4         5
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P5         6
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P6         7
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P7         8

#define IFX_AUTANALOG_CTB_OA_MUX_OUT_DISCONNECT 0
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_NINV       1
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_INV        2
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_RES        3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_OPAMP_INFINEON_AUTANALOG_CTB_H_ */
```

## 367.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 171 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_OPAMP_INFINEON_AUTANALOG_CTB_H_`。

## 367.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h.html)

---

[上一章](P366_inet.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P368_infineon-autanalog-prb.h_源码浏览.md)
