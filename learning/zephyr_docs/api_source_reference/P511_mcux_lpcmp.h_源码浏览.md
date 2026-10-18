---
id: learning.zephyr-docs.api-source-reference.page-511
title: mcux_lpcmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第511章\_mcux\_lpcmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html)。

## 511.1\_原始可见代码（Source Code）

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
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00054"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00083"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="amcux__lpcmp_8h_html_a0afc296fa89b7bdd31105574f459fb5a"></a>
<a id="amcux__lpcmp_8h_html_a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03e"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03"></a>
<a id="amcux__lpcmp_8h_html_a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9"></a>
<a id="amcux__lpcmp_8h_html_ad86c67639b0a919fd5ea0b5b6a3d4cd6"></a>
<a id="amcux__lpcmp_8h_html_ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9"></a>
<a id="amcux__lpcmp_8h_html_ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Vestas Wind Systems A/S
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_LPCMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_LPCMP_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

enum sensor_channel_mcux_lpcmp {
        SENSOR_CHAN_MCUX_LPCMP_OUTPUT = SENSOR_CHAN_PRIV_START,
};

enum sensor_trigger_type_mcux_lpcmp {
        SENSOR_TRIG_MCUX_LPCMP_OUTPUT_RISING = SENSOR_TRIG_PRIV_START,
        SENSOR_TRIG_MCUX_LPCMP_OUTPUT_FALLING,
};

enum sensor_attribute_mcux_lpcmp {
        SENSOR_ATTR_MCUX_LPCMP_POSITIVE_MUX_INPUT = SENSOR_ATTR_COMMON_COUNT,
        SENSOR_ATTR_MCUX_LPCMP_NEGATIVE_MUX_INPUT,

        SENSOR_ATTR_MCUX_LPCMP_DAC_ENABLE,
        SENSOR_ATTR_MCUX_LPCMP_DAC_HIGH_POWER_MODE_ENABLE,
        SENSOR_ATTR_MCUX_LPCMP_DAC_REFERENCE_VOLTAGE_SOURCE,
        SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE,

        SENSOR_ATTR_MCUX_LPCMP_SAMPLE_ENABLE,
        SENSOR_ATTR_MCUX_LPCMP_FILTER_COUNT,
        SENSOR_ATTR_MCUX_LPCMP_FILTER_PERIOD,

        SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_ENABLE,
        SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_SIGNAL_INVERT_ENABLE,
        SENSOR_ATTR_MCUX_LPCMP_COUTA_SIGNAL,
        SENSOR_ATTR_MCUX_LPCMP_COUT_EVENT_TO_CLOSE_WINDOW
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_LPCMP_H_ */
```

## 511.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Vestas Wind Systems A/S。

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_MCUX_LPCMP_H_`。

## 511.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_mcux_lpcmp](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a0afc296fa89b7bdd31105574f459fb5a)
- [SENSOR_CHAN_MCUX_LPCMP_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor_trigger_type_mcux_lpcmp](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#ad86c67639b0a919fd5ea0b5b6a3d4cd6)
- [SENSOR_TRIG_MCUX_LPCMP_OUTPUT_RISING](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e)
- [SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)
- [SENSOR_TRIG_MCUX_LPCMP_OUTPUT_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9)
- [sensor_attribute_mcux_lpcmp](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03e)
- [SENSOR_ATTR_MCUX_LPCMP_POSITIVE_MUX_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab)
- [SENSOR_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)
- [SENSOR_ATTR_MCUX_LPCMP_NEGATIVE_MUX_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52)
- [SENSOR_ATTR_MCUX_LPCMP_DAC_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7)
- [SENSOR_ATTR_MCUX_LPCMP_DAC_HIGH_POWER_MODE_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574)
- [SENSOR_ATTR_MCUX_LPCMP_DAC_REFERENCE_VOLTAGE_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01)
- [SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9)
- [SENSOR_ATTR_MCUX_LPCMP_SAMPLE_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66)
- [SENSOR_ATTR_MCUX_LPCMP_FILTER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03)
- [SENSOR_ATTR_MCUX_LPCMP_FILTER_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa)
- [SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e)
- [SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_SIGNAL_INVERT_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf)
- [SENSOR_ATTR_MCUX_LPCMP_COUTA_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a)
- [SENSOR_ATTR_MCUX_LPCMP_COUT_EVENT_TO_CLOSE_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P510_mctp_memory.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P512_memc_stm32.h_源码浏览.md)
