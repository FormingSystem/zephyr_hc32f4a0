---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-43
title: sensor_occurrence_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__occurrence__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_sensor\_occurrence\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__occurrence__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

仅关心事件是否发生的传感器所提供的数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

仅关心某个事件是否发生的传感器所提供的数据，用于报告触发（trigger）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 43.1\_数据结构（Data Structures）

<a id="r_sensor_5Foccurrence_5Fsample_5Fdata"></a>

```c
struct sensor_occurrence_sample_data
```

相关声明：[sensor_occurrence_sample_data](P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.2\_数据成员（Data Fields）

<a id="r_a06e7c6b24166e1c85d05286d44f60768"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#a06e7c6b24166e1c85d05286d44f60768)。

<a id="r_a181279d03759db87e3855d46d30c5aaf"></a>

```c
struct sensor_occurrence_data::sensor_occurrence_sample_data readings [1]
```

相关声明：[sensor_occurrence_data::sensor_occurrence_sample_data](P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)、[readings](#a181279d03759db87e3855d46d30c5aaf)。

## 43.3\_详细说明（Detailed Documentation）

<a id="a06e7c6b24166e1c85d05286d44f60768"></a>

### `header`

```c
struct sensor_data_header sensor_occurrence_data::header
```

<a id="a181279d03759db87e3855d46d30c5aaf"></a>

### `readings`

```c
struct sensor_occurrence_data::sensor_occurrence_sample_data sensor_occurrence_data::readings[1]
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 43.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_occurrence_sample_data](P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)
