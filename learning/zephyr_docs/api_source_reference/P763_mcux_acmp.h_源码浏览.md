---
id: learning.zephyr-docs.api-source-reference.page-763
title: mcux_acmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第763章\_mcux\_acmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html)。

## 763.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_2mcux__acmp_8h_html_a017d1a028479db7f49a1327814fe72da"></a>
<a id="asensor_2mcux__acmp_8h_html_a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36daf"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361"></a>
<a id="asensor_2mcux__acmp_8h_html_a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c"></a>
<a id="asensor_2mcux__acmp_8h_html_af10919d10852c60efa9fb8d3fa56c829"></a>
<a id="asensor_2mcux__acmp_8h_html_af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d"></a>
<a id="asensor_2mcux__acmp_8h_html_af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Vestas Wind Systems A/S
 * Copyright 2022, 2024-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_ACMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_ACMP_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

#if defined(FSL_FEATURE_ACMP_HAS_C1_INPSEL_BIT) && (FSL_FEATURE_ACMP_HAS_C1_INPSEL_BIT == 1U)
#define MCUX_ACMP_HAS_INPSEL 1
#else
#define MCUX_ACMP_HAS_INPSEL 0
#endif

#if defined(FSL_FEATURE_ACMP_HAS_C1_INNSEL_BIT) && (FSL_FEATURE_ACMP_HAS_C1_INNSEL_BIT == 1U)
#define MCUX_ACMP_HAS_INNSEL 1
#else
#define MCUX_ACMP_HAS_INNSEL 0
#endif

#if defined(FSL_FEATURE_ACMP_HAS_C0_OFFSET_BIT) && (FSL_FEATURE_ACMP_HAS_C0_OFFSET_BIT == 1U)
#define MCUX_ACMP_HAS_OFFSET 1
#else
#define MCUX_ACMP_HAS_OFFSET 0
#endif

#if defined(FSL_FEATURE_ACMP_HAS_C3_REG) && (FSL_FEATURE_ACMP_HAS_C3_REG != 0U) && \
        (FSL_FEATURE_ACMP_HAS_NO_3V_DOMAIN == 0U)
#define MCUX_ACMP_HAS_DISCRETE_MODE 1
#else
#define MCUX_ACMP_HAS_DISCRETE_MODE 0
#endif

#if defined(FSL_FEATURE_ACMP_HAS_C0_HYSTCTR_BIT) && (FSL_FEATURE_ACMP_HAS_C0_HYSTCTR_BIT == 1U)
#define MCUX_ACMP_HAS_HYSTCTR 1
#else
#define MCUX_ACMP_HAS_HYSTCTR 0
#endif

#if defined(FSL_FEATURE_ACMP_HAS_NO_WINDOW_MODE) && (FSL_FEATURE_ACMP_HAS_NO_WINDOW_MODE == 1U)
#define MCUX_ACMP_HAS_WINDOW_MODE 0
#else
#define MCUX_ACMP_HAS_WINDOW_MODE 1
#endif

#if defined(FSL_FEATURE_ACMP_HAS_NO_C0_SE_BIT) && (FSL_FEATURE_ACMP_HAS_NO_C0_SE_BIT == 1U)
#define MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION 0
#else
#define MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION 1
#endif

enum sensor_channel_mcux_acmp {
        SENSOR_CHAN_MCUX_ACMP_OUTPUT = SENSOR_CHAN_PRIV_START,
};

enum sensor_trigger_type_mcux_acmp {
        SENSOR_TRIG_MCUX_ACMP_OUTPUT_RISING = SENSOR_TRIG_PRIV_START,
        SENSOR_TRIG_MCUX_ACMP_OUTPUT_FALLING,
};

enum sensor_attribute_mcux_acmp {
        SENSOR_ATTR_MCUX_ACMP_OFFSET_LEVEL = SENSOR_ATTR_COMMON_COUNT,
        SENSOR_ATTR_MCUX_ACMP_HYSTERESIS_LEVEL,
        SENSOR_ATTR_MCUX_ACMP_DAC_VOLTAGE_REFERENCE,
        SENSOR_ATTR_MCUX_ACMP_DAC_VALUE,
        SENSOR_ATTR_MCUX_ACMP_POSITIVE_PORT_INPUT,
        SENSOR_ATTR_MCUX_ACMP_POSITIVE_MUX_INPUT,
        SENSOR_ATTR_MCUX_ACMP_NEGATIVE_PORT_INPUT,
        SENSOR_ATTR_MCUX_ACMP_NEGATIVE_MUX_INPUT,
#if MCUX_ACMP_HAS_DISCRETE_MODE
        SENSOR_ATTR_MCUX_ACMP_POSITIVE_DISCRETE_MODE,
        SENSOR_ATTR_MCUX_ACMP_NEGATIVE_DISCRETE_MODE,
        SENSOR_ATTR_MCUX_ACMP_DISCRETE_CLOCK,
        SENSOR_ATTR_MCUX_ACMP_DISCRETE_ENABLE_RESISTOR_DIVIDER,
        SENSOR_ATTR_MCUX_ACMP_DISCRETE_SAMPLE_TIME,
        SENSOR_ATTR_MCUX_ACMP_DISCRETE_PHASE1_TIME,
        SENSOR_ATTR_MCUX_ACMP_DISCRETE_PHASE2_TIME,
#endif
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_ACMP_H_ */
```

## 763.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Vestas Wind Systems A/S。

版权（Copyright）：2022, 2024-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 119 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_ACMP_H_`。

## 763.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_mcux_acmp](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a017d1a028479db7f49a1327814fe72da)
- [SENSOR_CHAN_MCUX_ACMP_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor_trigger_type_mcux_acmp](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#af10919d10852c60efa9fb8d3fa56c829)
- [SENSOR_TRIG_MCUX_ACMP_OUTPUT_RISING](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697)
- [SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)
- [SENSOR_TRIG_MCUX_ACMP_OUTPUT_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d)
- [sensor_attribute_mcux_acmp](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36daf)
- [SENSOR_ATTR_MCUX_ACMP_OFFSET_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250)
- [SENSOR_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)
- [SENSOR_ATTR_MCUX_ACMP_HYSTERESIS_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c)
- [SENSOR_ATTR_MCUX_ACMP_DAC_VOLTAGE_REFERENCE](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361)
- [SENSOR_ATTR_MCUX_ACMP_DAC_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d)
- [SENSOR_ATTR_MCUX_ACMP_POSITIVE_PORT_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000)
- [SENSOR_ATTR_MCUX_ACMP_POSITIVE_MUX_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2)
- [SENSOR_ATTR_MCUX_ACMP_NEGATIVE_PORT_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6)
- [SENSOR_ATTR_MCUX_ACMP_NEGATIVE_MUX_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P762_max31790.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P764_tle9104.h_源码浏览.md)
