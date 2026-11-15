---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-45
title: sensor_q31_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__q31__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_sensor\_q31\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__q31__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

报告标量数据（Scalar Data）的传感器通道数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

报告标量数据（Scalar Data）的传感器通道数据。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 45.1\_数据结构（Data Structures）

<a id="r_sensor_5Fq31_5Fsample_5Fdata"></a>

```c
struct sensor_q31_sample_data
```

相关声明：[sensor_q31_sample_data](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.2\_数据成员（Data Fields）

<a id="r_a9dcc5ffe1d31c37eef75b4132c5f94fd"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#a9dcc5ffe1d31c37eef75b4132c5f94fd)。

<a id="r_a41f8315cbe740bdc7aec6bd30ce0e096"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#a41f8315cbe740bdc7aec6bd30ce0e096)。

<a id="r_a23fc75fd1dafe2789a7d0bff116cb681"></a>

```c
struct sensor_q31_data::sensor_q31_sample_data readings [1]
```

相关声明：[sensor_q31_data::sensor_q31_sample_data](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)、[readings](#a23fc75fd1dafe2789a7d0bff116cb681)。

## 45.3\_详细说明（Detailed Documentation）

<a id="a9dcc5ffe1d31c37eef75b4132c5f94fd"></a>

### `header`

```c
struct sensor_data_header sensor_q31_data::header
```

<a id="a23fc75fd1dafe2789a7d0bff116cb681"></a>

### `readings`

```c
struct sensor_q31_data::sensor_q31_sample_data sensor_q31_data::readings[1]
```

<a id="a41f8315cbe740bdc7aec6bd30ce0e096"></a>

### `shift`

```c
int8_t sensor_q31_data::shift
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 45.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_q31_sample_data](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)
