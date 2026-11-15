---
id: learning.zephyr-docs.api-source-reference.page-689
title: qdec_nxp_s32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__s32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第689章\_qdec\_nxp\_s32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__s32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__s32_8h.html)。

## 689.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
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
<a id="l00067"></a>
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
<a id="l00096"></a>
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
<a id="l00131"></a>
<a id="l00138"></a>
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
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_QDEC_NXP_S32_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_QDEC_NXP_S32_H_


#define TRGMUX_LOGIC_GROUP_0_TRIGGER_0 (0)
#define TRGMUX_LOGIC_GROUP_0_TRIGGER_1 (1)
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_0 (2)
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_1 (3)

#define TRGMUX_IP_INPUT_SIUL2_IN0  (60)
#define TRGMUX_IP_INPUT_SIUL2_IN1  (61)
#define TRGMUX_IP_INPUT_SIUL2_IN2  (62)
#define TRGMUX_IP_INPUT_SIUL2_IN3  (63)
#define TRGMUX_IP_INPUT_SIUL2_IN4  (64)
#define TRGMUX_IP_INPUT_SIUL2_IN5  (65)
#define TRGMUX_IP_INPUT_SIUL2_IN6  (66)
#define TRGMUX_IP_INPUT_SIUL2_IN7  (67)
#define TRGMUX_IP_INPUT_SIUL2_IN8  (68)
#define TRGMUX_IP_INPUT_SIUL2_IN9  (69)
#define TRGMUX_IP_INPUT_SIUL2_IN10 (70)
#define TRGMUX_IP_INPUT_SIUL2_IN11 (71)
#define TRGMUX_IP_INPUT_SIUL2_IN12 (72)
#define TRGMUX_IP_INPUT_SIUL2_IN13 (73)
#define TRGMUX_IP_INPUT_SIUL2_IN14 (74)
#define TRGMUX_IP_INPUT_SIUL2_IN15 (75)

#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I0 (105)
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I1 (106)
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2 (107)
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3 (108)

#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I0 (144)
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I1 (145)
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I2 (146)
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I3 (147)

#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH1    (32)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH2    (33)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH3    (34)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH4    (35)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH5    (36)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6    (37)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7    (38)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH9    (39)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH10 (40)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH11 (41)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH12 (42)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH13 (43)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH14 (44)
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH15 (45)

#define LCU_IP_MUX_SEL_LOGIC_0                   (0)
#define LCU_IP_MUX_SEL_LU_IN_0                   (1)
#define LCU_IP_MUX_SEL_LU_IN_1                   (2)
#define LCU_IP_MUX_SEL_LU_IN_2                   (3)
#define LCU_IP_MUX_SEL_LU_IN_3                   (4)
#define LCU_IP_MUX_SEL_LU_IN_4                   (5)
#define LCU_IP_MUX_SEL_LU_IN_5                   (6)
#define LCU_IP_MUX_SEL_LU_IN_6                   (7)
#define LCU_IP_MUX_SEL_LU_IN_7                   (8)
#define LCU_IP_MUX_SEL_LU_IN_8                   (9)
#define LCU_IP_MUX_SEL_LU_IN_9                   (10)
#define LCU_IP_MUX_SEL_LU_IN_10                  (11)
#define LCU_IP_MUX_SEL_LU_IN_11                  (12)
#define LCU_IP_MUX_SEL_LU_OUT_0                  (13)
#define LCU_IP_MUX_SEL_LU_OUT_1                  (14)
#define LCU_IP_MUX_SEL_LU_OUT_2                  (15)
#define LCU_IP_MUX_SEL_LU_OUT_3                  (16)
#define LCU_IP_MUX_SEL_LU_OUT_4                  (17)
#define LCU_IP_MUX_SEL_LU_OUT_5                  (18)
#define LCU_IP_MUX_SEL_LU_OUT_6                  (19)
#define LCU_IP_MUX_SEL_LU_OUT_7                  (20)
#define LCU_IP_MUX_SEL_LU_OUT_8                  (21)
#define LCU_IP_MUX_SEL_LU_OUT_9                  (22)
#define LCU_IP_MUX_SEL_LU_OUT_10                 (23)
#define LCU_IP_MUX_SEL_LU_OUT_11                 (24)

#define LCU_IP_IN_0                              (0)
#define LCU_IP_IN_1                              (1)
#define LCU_IP_IN_2                              (2)
#define LCU_IP_IN_3                              (3)
#define LCU_IP_IN_4                              (4)
#define LCU_IP_IN_5                              (5)
#define LCU_IP_IN_6                              (6)
#define LCU_IP_IN_7                              (7)
#define LCU_IP_IN_8                              (8)
#define LCU_IP_IN_9                              (9)
#define LCU_IP_IN_10                             (10)
#define LCU_IP_IN_11                             (11)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_QDEC_NXP_S32_H_ */
```

## 689.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 154 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_QDEC_NXP_S32_H_`。

## 689.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nxp__s32_8h.html)

---

[上一章](P688_qdec_nrf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P690_qdec_stm32.h_源码浏览.md)
