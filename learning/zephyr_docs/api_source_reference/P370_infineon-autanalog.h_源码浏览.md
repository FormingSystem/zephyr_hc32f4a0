---
id: learning.zephyr-docs.api-source-reference.page-370
title: infineon-autanalog.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第370章\_infineon-autanalog.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h.html)。

## 370.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
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
<a id="l00095"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
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
<a id="l00123"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_AUTANALOG_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_AUTANALOG_H_

#define IFX_AUTANALOG_AC_ACTION_STOP                0
#define IFX_AUTANALOG_AC_ACTION_NEXT                1
#define IFX_AUTANALOG_AC_ACTION_WAIT_FOR            2
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE      3
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE     4
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE_CLR  5
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE_CLR 6

#define IFX_AUTANALOG_AC_COND_FALSE              0
#define IFX_AUTANALOG_AC_COND_TRUE               1
#define IFX_AUTANALOG_AC_COND_BLOCK_READY        2
#define IFX_AUTANALOG_AC_COND_CNT_DONE           3
#define IFX_AUTANALOG_AC_COND_SAR_DONE           4
#define IFX_AUTANALOG_AC_COND_SAR_EOS            5
#define IFX_AUTANALOG_AC_COND_SAR_RANGE0         6
#define IFX_AUTANALOG_AC_COND_SAR_RANGE1         7
#define IFX_AUTANALOG_AC_COND_SAR_RANGE2         8
#define IFX_AUTANALOG_AC_COND_SAR_RANGE3         9
#define IFX_AUTANALOG_AC_COND_SAR_BUSY           10
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_DONE      11
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_DONE      12
#define IFX_AUTANALOG_AC_COND_SAR_FIFO_DONE      13
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_FIFO_DONE 14
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_FIFO_DONE 15
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE0     16
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE1     17
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0        18
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1        19
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE0      20
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE1      21
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0          22
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1          23
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0          24
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1          25
#define IFX_AUTANALOG_AC_COND_CHIP_ACTIVE        32
#define IFX_AUTANALOG_AC_COND_CHIP_DEEPSLEEP     33
#define IFX_AUTANALOG_AC_COND_TR_IN0             34
#define IFX_AUTANALOG_AC_COND_TR_IN1             35
#define IFX_AUTANALOG_AC_COND_TR_IN2             36
#define IFX_AUTANALOG_AC_COND_TR_IN3             37
#define IFX_AUTANALOG_AC_COND_TR_IN_WAKE         38
#define IFX_AUTANALOG_AC_COND_TIMER_DONE_WAKE    39
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0_WAKE     40
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1_WAKE     41
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0_WAKE     42
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1_WAKE     43
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0_WAKE   44
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1_WAKE   45
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL0        46
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL1        47
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL2        48
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL3        49
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL4        50
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL5        51
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL6        52
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL7        53
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE0        54
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE1        55
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE2        56
#define IFX_AUTANALOG_AC_COND_DAC0_EPOCH         57
#define IFX_AUTANALOG_AC_COND_DAC0_STROBE        58
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE0        59
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE1        60
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE2        61
#define IFX_AUTANALOG_AC_COND_DAC1_EPOCH         62
#define IFX_AUTANALOG_AC_COND_DAC1_STROBE        63

#define IFX_AUTANALOG_AC_GPIO_OUT_DISABLED 0x0
#define IFX_AUTANALOG_AC_GPIO_OUT0         0x1
#define IFX_AUTANALOG_AC_GPIO_OUT1         0x2
#define IFX_AUTANALOG_AC_GPIO_OUT2         0x4
#define IFX_AUTANALOG_AC_GPIO_OUT3         0x8

#define IFX_AUTANALOG_CTB_OA_GAIN_1_00  0
#define IFX_AUTANALOG_CTB_OA_GAIN_1_42  1
#define IFX_AUTANALOG_CTB_OA_GAIN_2_00  2
#define IFX_AUTANALOG_CTB_OA_GAIN_2_78  3
#define IFX_AUTANALOG_CTB_OA_GAIN_4_00  4
#define IFX_AUTANALOG_CTB_OA_GAIN_5_82  5
#define IFX_AUTANALOG_CTB_OA_GAIN_8_00  6
#define IFX_AUTANALOG_CTB_OA_GAIN_10_67 7
#define IFX_AUTANALOG_CTB_OA_GAIN_16_00 8
#define IFX_AUTANALOG_CTB_OA_GAIN_21_33 9
#define IFX_AUTANALOG_CTB_OA_GAIN_32_00 10

#define IFX_AUTANALOG_DAC_DIR_DISABLED 0
#define IFX_AUTANALOG_DAC_DIR_FORWARD  1
#define IFX_AUTANALOG_DAC_DIR_REVERSE  2

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_AUTANALOG_H_ */
```

## 370.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 133 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_AUTANALOG_H_`。

## 370.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h.html)

---

[上一章](P369_infineon-autanalog-ptcomp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P371_infineon-hppass.h_源码浏览.md)
