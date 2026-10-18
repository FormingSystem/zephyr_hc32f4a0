---
id: learning.zephyr-docs.api-file-runtime-reference.page-1
title: zephyr__drivers__sensor__adltc2990.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adltc2990_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_sensor\_\_adltc2990.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adltc2990_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ADLTC2990传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/device.h>
```

查看此文件的源码。

ADLTC2990传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.1\_枚举（Enumerations）

<a id="r_ga2bb0bc14920f8645b371c194148e8d21"></a>

```c
enum adltc2990_acquisition_format { ADLTC2990_REPEATED_ACQUISITION , ADLTC2990_SINGLE_SHOT_ACQUISITION }
```

相关声明：[adltc2990_acquisition_format](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#ga2bb0bc14920f8645b371c194148e8d21)、[ADLTC2990_REPEATED_ACQUISITION](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gga2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415)、[ADLTC2990_SINGLE_SHOT_ACQUISITION](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gga2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870)。

采集格式（Acquisition Format）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_gae6b634f7ff028d3c4a954c111bcbc4d2"></a>

```c
int adltc2990_is_busy (const struct device *dev, bool *is_busy)
```

相关声明：[adltc2990_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gae6b634f7ff028d3c4a954c111bcbc4d2)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查 adtlc2990 是否正在执行转换（Conversion）。

<a id="r_ga1952f17894be82e3b09065f79168edde"></a>

```c
int adltc2990_trigger_measurement (const struct device *dev, enum adltc2990_acquisition_format format)
```

相关声明：[adltc2990_trigger_measurement](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#ga1952f17894be82e3b09065f79168edde)、[device](../device_reference/P002_设备对象结构.md)、[adltc2990_acquisition_format](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#ga2bb0bc14920f8645b371c194148e8d21)。

触发 adltc2990 开始测量（Measurement）。


## 1.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P009_adltc2990.h_源码浏览.md)
- [adltc2990_acquisition_format](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#ga2bb0bc14920f8645b371c194148e8d21)
- [ADLTC2990_REPEATED_ACQUISITION](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gga2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415)
- [ADLTC2990_SINGLE_SHOT_ACQUISITION](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gga2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870)
- [adltc2990_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#gae6b634f7ff028d3c4a954c111bcbc4d2)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [adltc2990_trigger_measurement](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html#ga1952f17894be82e3b09065f79168edde)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__video__arducam_mega.h_文件参考.md)
