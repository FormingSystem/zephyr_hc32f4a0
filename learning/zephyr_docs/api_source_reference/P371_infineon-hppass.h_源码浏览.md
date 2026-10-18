---
id: learning.zephyr-docs.api-source-reference.page-371
title: infineon-hppass.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第371章\_infineon-hppass.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h.html)。

## 371.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
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
<a id="l00084"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_HPPASS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_HPPASS_H_

#define IFX_HPPASS_AC_ACTION_STOP            0
#define IFX_HPPASS_AC_ACTION_NEXT            1
#define IFX_HPPASS_AC_ACTION_WAIT_FOR        2
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_TRUE  3
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_FALSE 4

#define IFX_HPPASS_AC_COND_FALSE              0
#define IFX_HPPASS_AC_COND_TRUE               1
#define IFX_HPPASS_AC_COND_BLOCK_READY        2
#define IFX_HPPASS_AC_COND_CNT_DONE           3
#define IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE   4
#define IFX_HPPASS_AC_COND_SAR_GROUP_1_DONE   5
#define IFX_HPPASS_AC_COND_SAR_GROUP_2_DONE   6
#define IFX_HPPASS_AC_COND_SAR_GROUP_3_DONE   7
#define IFX_HPPASS_AC_COND_SAR_GROUP_4_DONE   8
#define IFX_HPPASS_AC_COND_SAR_GROUP_5_DONE   9
#define IFX_HPPASS_AC_COND_SAR_GROUP_6_DONE   10
#define IFX_HPPASS_AC_COND_SAR_GROUP_7_DONE   11
#define IFX_HPPASS_AC_COND_SAR_LIMIT_0        12
#define IFX_HPPASS_AC_COND_SAR_LIMIT_1        13
#define IFX_HPPASS_AC_COND_SAR_LIMIT_2        14
#define IFX_HPPASS_AC_COND_SAR_LIMIT_3        15
#define IFX_HPPASS_AC_COND_SAR_LIMIT_4        16
#define IFX_HPPASS_AC_COND_SAR_LIMIT_5        17
#define IFX_HPPASS_AC_COND_SAR_LIMIT_6        18
#define IFX_HPPASS_AC_COND_SAR_LIMIT_7        19
#define IFX_HPPASS_AC_COND_SAR_BUSY           20
#define IFX_HPPASS_AC_COND_SAR_FIR_0_DONE     21
#define IFX_HPPASS_AC_COND_SAR_FIR_1_DONE     22
#define IFX_HPPASS_AC_COND_SAR_QUEUE_HI_EMPTY 23
#define IFX_HPPASS_AC_COND_SAR_QUEUE_LO_EMPTY 24
#define IFX_HPPASS_AC_COND_SAR_QUEUES_EMPTY   25
#define IFX_HPPASS_AC_COND_TRIG_0             32
#define IFX_HPPASS_AC_COND_TRIG_1             33
#define IFX_HPPASS_AC_COND_TRIG_2             34
#define IFX_HPPASS_AC_COND_TRIG_3             35
#define IFX_HPPASS_AC_COND_TRIG_4             36
#define IFX_HPPASS_AC_COND_TRIG_5             37
#define IFX_HPPASS_AC_COND_TRIG_6             38
#define IFX_HPPASS_AC_COND_TRIG_7             39
#define IFX_HPPASS_AC_COND_FIFO_0_LEVEL       42
#define IFX_HPPASS_AC_COND_FIFO_1_LEVEL       43
#define IFX_HPPASS_AC_COND_FIFO_2_LEVEL       44
#define IFX_HPPASS_AC_COND_FIFO_3_LEVEL       45
#define IFX_HPPASS_AC_COND_CSG_0_DAC_DONE     48
#define IFX_HPPASS_AC_COND_CSG_1_DAC_DONE     49
#define IFX_HPPASS_AC_COND_CSG_2_DAC_DONE     50
#define IFX_HPPASS_AC_COND_CSG_3_DAC_DONE     51
#define IFX_HPPASS_AC_COND_CSG_4_DAC_DONE     52
#define IFX_HPPASS_AC_COND_CSG_0_COMP         56
#define IFX_HPPASS_AC_COND_CSG_1_COMP         57
#define IFX_HPPASS_AC_COND_CSG_2_COMP         58
#define IFX_HPPASS_AC_COND_CSG_3_COMP         59
#define IFX_HPPASS_AC_COND_CSG_4_COMP         60

#define IFX_HPPASS_GPIO_OUT_0 0x01
#define IFX_HPPASS_GPIO_OUT_1 0x02
#define IFX_HPPASS_GPIO_OUT_2 0x04
#define IFX_HPPASS_GPIO_OUT_3 0x08
#define IFX_HPPASS_GPIO_OUT_4 0x10

#define IFX_HPPASS_SAR_GRP_0 0x01
#define IFX_HPPASS_SAR_GRP_1 0x02
#define IFX_HPPASS_SAR_GRP_2 0x04
#define IFX_HPPASS_SAR_GRP_3 0x08
#define IFX_HPPASS_SAR_GRP_4 0x10
#define IFX_HPPASS_SAR_GRP_5 0x20
#define IFX_HPPASS_SAR_GRP_6 0x40
#define IFX_HPPASS_SAR_GRP_7 0x80

#define IFX_HPPASS_TR_DISABLED 0
#define IFX_HPPASS_TR_HW_A     1
#define IFX_HPPASS_TR_HW_B     2
#define IFX_HPPASS_TR_FW_PULSE 3
#define IFX_HPPASS_TR_FW_LEVEL 4

#define IFX_HPPASS_TR_HW_PULSE_POS_DSYNC  0
#define IFX_HPPASS_TR_HW_PULSE_NEG_DSYNC  1
#define IFX_HPPASS_TR_HW_PULSE_BOTH_DSYNC 2
#define IFX_HPPASS_TR_HW_LEVEL_DSYNC      3
#define IFX_HPPASS_TR_HW_PULSE_POS_SSYNC  4
#define IFX_HPPASS_TR_HW_PULSE_NEG_SSYNC  5
#define IFX_HPPASS_TR_HW_PULSE_BOTH_SSYNC 6
#define IFX_HPPASS_TR_HW_LEVEL_SSYNC      7

#define IFX_HPPASS_TR_OUT_DISABLED    0
#define IFX_HPPASS_TR_OUT_SAR_GROUP_0 1
#define IFX_HPPASS_TR_OUT_SAR_GROUP_1 2
#define IFX_HPPASS_TR_OUT_SAR_GROUP_2 3
#define IFX_HPPASS_TR_OUT_SAR_GROUP_3 4
#define IFX_HPPASS_TR_OUT_SAR_GROUP_4 5
#define IFX_HPPASS_TR_OUT_SAR_GROUP_5 6
#define IFX_HPPASS_TR_OUT_SAR_GROUP_6 7
#define IFX_HPPASS_TR_OUT_SAR_GROUP_7 8
#define IFX_HPPASS_TR_OUT_FIR_0       9
#define IFX_HPPASS_TR_OUT_FIR_1       10
#define IFX_HPPASS_TR_OUT_AC          11

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_HPPASS_H_ */
```

## 371.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MFD_INFINEON_HPPASS_H_`。

## 371.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h.html)

---

[上一章](P370_infineon-autanalog.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P372_infineon-xmc4xxx-dma.h_源码浏览.md)
