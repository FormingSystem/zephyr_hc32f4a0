---
id: learning.zephyr-docs.api-file-runtime-reference.page-74
title: zephyr__drivers__sensor__veml60xx-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_zephyr\_\_drivers\_\_sensor\_\_veml60xx-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

VEML60xx传感器系列的扩展API头文件（Extended Sensor API Header）。

查看此文件的源码。

<a id="details"></a>

VEML60xx传感器系列的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 74.1\_数据结构（Data Structures）

<a id="r_veml60xx_5Fit_5Fdata"></a>

```c
struct veml60xx_it_data
```

相关声明：[veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 74.2\_枚举（Enumerations）

<a id="r_ga8945da51940f67ee875a729d6de4d287"></a>

```c
enum veml60xx_it { VEML60XX_IT_3_125 , VEML60XX_IT_6_25 , VEML60XX_IT_12_5 , VEML60XX_IT_25 , VEML60XX_IT_50 , VEML60XX_IT_100 , VEML60XX_IT_200 , VEML60XX_IT_400 }
```

相关声明：[veml60xx_it](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga8945da51940f67ee875a729d6de4d287)、[VEML60XX_IT_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965)、[VEML60XX_IT_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888)、[VEML60XX_IT_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa)、[VEML60XX_IT_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144)、[VEML60XX_IT_50](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77)、[VEML60XX_IT_100](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636)、[VEML60XX_IT_200](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b)、[VEML60XX_IT_400](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93)。

VEML60xx 环境光测量（Ambient Light Measurements）的积分时间选项（Integration Time Options）。

<a id="r_gacf7907b21bea0f35196db039a709aae2"></a>

```c
enum veml60xx_gain { VEML60XX_GAIN_1 = 0x00 , VEML60XX_GAIN_2 = 0x01 , VEML60XX_GAIN_0_66 = 0x02 , VEML60XX_GAIN_0_5 = 0x03 }
```

相关声明：[veml60xx_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacf7907b21bea0f35196db039a709aae2)、[VEML60XX_GAIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b)、[VEML60XX_GAIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5)、[VEML60XX_GAIN_0_66](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f)、[VEML60XX_GAIN_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4)。

VEML60xx 环境光测量（Ambient Light Measurements）的增益选项（Gain Options）。

<a id="r_gacb2554bb01df63048cdcc1894903dd73"></a>

```c
enum veml60xx_pers { VEML60XX_PERS_1 = 0x00 , VEML60XX_PERS_2 = 0x01 , VEML60XX_PERS_4 = 0x02 , VEML60XX_PERS_8 = 0x03 }
```

相关声明：[veml60xx_pers](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacb2554bb01df63048cdcc1894903dd73)、[VEML60XX_PERS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1)、[VEML60XX_PERS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da)、[VEML60XX_PERS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393)、[VEML60XX_PERS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4)。

VEML60xx 环境光传感器（ALS）中断持续性保护次数选项（Interrupt Persistence Protect Number Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 74.3\_函数（Functions）

<a id="r_gaba51cd71795a34af85d21da10cba5b44"></a>

```c
static bool veml60xx_gain_in_range (int32_t gain)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_gain_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gaba51cd71795a34af85d21da10cba5b44)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="r_ga2635095ab9ddf8ffd8e25cbaf08b824a"></a>

```c
static bool veml60xx_it_in_range (int32_t it)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_it_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga2635095ab9ddf8ffd8e25cbaf08b824a)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="r_ga030b4553bb1982a3f470dcfe70a74636"></a>

```c
static bool veml60xx_pers_in_range (int32_t pers)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_pers_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga030b4553bb1982a3f470dcfe70a74636)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 74.4\_变量（Variables）

<a id="r_ga95d24f44c42ba4d71df013ace6c6d613"></a>

```c
static const struct veml60xx_it_data veml60xx_it_values [VEML60XX_IT_COUNT]
```

相关声明：[veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)、[veml60xx_it_values](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga95d24f44c42ba4d71df013ace6c6d613)。


## 74.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h_source.html)
- [veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)
- [veml60xx_it](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga8945da51940f67ee875a729d6de4d287)
- [VEML60XX_IT_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965)
- [VEML60XX_IT_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888)
- [VEML60XX_IT_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa)
- [VEML60XX_IT_25](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144)
- [VEML60XX_IT_50](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77)
- [VEML60XX_IT_100](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636)
- [VEML60XX_IT_200](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b)
- [VEML60XX_IT_400](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93)
- [veml60xx_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacf7907b21bea0f35196db039a709aae2)
- [VEML60XX_GAIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b)
- [VEML60XX_GAIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5)
- [VEML60XX_GAIN_0_66](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f)
- [VEML60XX_GAIN_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4)
- [veml60xx_pers](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gacb2554bb01df63048cdcc1894903dd73)
- [VEML60XX_PERS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1)
- [VEML60XX_PERS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da)
- [VEML60XX_PERS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393)
- [VEML60XX_PERS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [veml60xx_gain_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#gaba51cd71795a34af85d21da10cba5b44)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [veml60xx_it_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga2635095ab9ddf8ffd8e25cbaf08b824a)
- [veml60xx_pers_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga030b4553bb1982a3f470dcfe70a74636)
- [veml60xx_it_values](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html#ga95d24f44c42ba4d71df013ace6c6d613)

<a id="header-details"></a>

---

[上一章](P073_zephyr__drivers__sensor__veml6046.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P075_zephyr__sys__word_granular_access.h_文件参考.md)
