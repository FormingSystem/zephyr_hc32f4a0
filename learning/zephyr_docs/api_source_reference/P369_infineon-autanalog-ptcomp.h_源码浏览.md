---
id: learning.zephyr-docs.api-source-reference.page-369
title: infineon-autanalog-ptcomp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第369章\_infineon-autanalog-ptcomp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h.html)。

## 369.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
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
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
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
<a id="l00117"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_H_

#define IFX_AUTANALOG_PTCOMP_PWR_OFF    0
#define IFX_AUTANALOG_PTCOMP_PWR_ULP    1
#define IFX_AUTANALOG_PTCOMP_PWR_LP     2
#define IFX_AUTANALOG_PTCOMP_PWR_NORMAL 3

#define IFX_AUTANALOG_PTCOMP_INT_DISABLED     0
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING  1
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING 2
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH    3

#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN1    0
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN4    1
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN6    2
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN7    3
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN1    4
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN4    5
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN6    6
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN7    7
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA0_OUT 8
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA1_OUT 9
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA0_OUT 10
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA1_OUT 11
#define IFX_AUTANALOG_PTCOMP_MUX_DAC0         12
#define IFX_AUTANALOG_PTCOMP_MUX_DAC1         13
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0     14
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT1     15
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO0        16
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO1        17
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO2        18
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO3        19
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO4        20
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO5        21
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO6        22
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO7        23

#define IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED 0
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0    1
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1    2

#define IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL        0
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING  1
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING 2
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH    3

#define IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT 0
#define IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME  1
#define IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW 2

#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A           0
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_AND_B 1
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B           2
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B     3
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B_BAR 4
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XOR_B     5
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B      6
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NOR_B     7
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XNOR_B    8
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B_BAR       9
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B_BAR  10
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR       11
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_OR_B  12
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NAND_B    13

#define IFX_AUTANALOG_PTCOMP_PP_WIN_2   0
#define IFX_AUTANALOG_PTCOMP_PP_WIN_4   1
#define IFX_AUTANALOG_PTCOMP_PP_WIN_8   2
#define IFX_AUTANALOG_PTCOMP_PP_WIN_16  3
#define IFX_AUTANALOG_PTCOMP_PP_WIN_32  4
#define IFX_AUTANALOG_PTCOMP_PP_WIN_64  5
#define IFX_AUTANALOG_PTCOMP_PP_WIN_128 6

#define IFX_AUTANALOG_PTCOMP_PP_COND_BELOW   0
#define IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE  1
#define IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE   2
#define IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE 3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_H_ */
```

## 369.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 141 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_H_`。

## 369.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h.html)

---

[上一章](P368_infineon-autanalog-prb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P370_infineon-autanalog.h_源码浏览.md)
