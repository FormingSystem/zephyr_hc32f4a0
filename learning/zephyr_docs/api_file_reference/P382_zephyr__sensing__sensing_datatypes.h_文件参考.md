---
id: learning.zephyr-docs.api-file-reference.page-382
title: zephyr__sensing__sensing_datatypes.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第382章\_zephyr\_\_sensing\_\_sensing\_datatypes.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统（Sensing Subsystem）数据类型定义的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/dsp/types.h>
```

查看此文件的源码。

感知子系统（Sensing Subsystem）数据类型定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 382.1\_数据结构（Data Structures）

<a id="r_sensing_5Fsensor_5Fvalue_5Fheader"></a>

```c
struct sensing_sensor_value_header
```

相关声明：[sensing_sensor_value_header](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md)。

全部传感器值载荷（Sensor Value Payloads）的通用头部。

<a id="r_sensing_5Fsensor_5Fvalue_5F3d_5Fq31"></a>

```c
struct sensing_sensor_value_3d_q31
```

相关声明：[sensing_sensor_value_3d_q31](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md)。

基于通用数据类型的传感器值（Sensor Value）数据结构类型。

<a id="r_sensing_5Fsensor_5Fvalue_5Fuint32"></a>

```c
struct sensing_sensor_value_uint32
```

相关声明：[sensing_sensor_value_uint32](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md)。

表示单个单轴值（Single 1-Axis Value）的传感器值数据结构。

<a id="r_sensing_5Fsensor_5Fvalue_5Fq31"></a>

```c
struct sensing_sensor_value_q31
```

相关声明：[sensing_sensor_value_q31](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md)。

表示单个单轴值（Single 1-Axis Value）的传感器值数据结构。


## 382.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P758_sensing_datatypes.h_源码浏览.md)
- [sensing_sensor_value_header](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md)
- [sensing_sensor_value_3d_q31](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md)
- [sensing_sensor_value_uint32](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md)
- [sensing_sensor_value_q31](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md)

<a id="header-details"></a>

---

[上一章](P381_zephyr__posix__semaphore.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P383_zephyr__drivers__sensor_attribute_types.h_文件参考.md)
