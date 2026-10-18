---
id: learning.zephyr-docs.api-topic-reference.page-60
title: 数据类型（Data Types）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__datatypes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_数据类型（Data Types）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__datatypes.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统使用的传感器数据结构。

<a id="details"></a>

感知子系统使用的传感器数据结构。

<a id="header-files"></a>
<a id="files"></a>

## 60.1\_文件（Files）

<a id="r_sensing_5Fdatatypes_2Eh"></a>

```c
file sensing_datatypes.h
```

相关声明：[sensing_datatypes.h](../api_file_reference/P382_zephyr__sensing__sensing_datatypes.h_文件参考.md)。

感知子系统（Sensing Subsystem）数据类型定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 60.2\_数据结构（Data Structures）

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


## 60.3\_原页交叉引用（Cross References）

- [sensing_datatypes.h](../api_file_reference/P382_zephyr__sensing__sensing_datatypes.h_文件参考.md)
- [sensing_sensor_value_header](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md)
- [sensing_sensor_value_3d_q31](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md)
- [sensing_sensor_value_uint32](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md)
- [sensing_sensor_value_q31](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md)

<a id="header-details"></a>

---

[上一章](P059_协议（Protocols）.md) · [返回大纲](大纲.md) · [下一章](P061_设备专用传感器 API 扩展和设备树常量。.md)
