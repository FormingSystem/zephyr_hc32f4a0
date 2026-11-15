---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-33
title: sensor_byte_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__byte__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_sensor\_byte\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__byte__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

产生单字节数据的传感器所提供的数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

来自每次产生一个字节数据的传感器的数据。供以下通道使用：`SENSOR_CHAN_PROX`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_sensor_5Fbyte_5Fsample_5Fdata"></a>

```c
struct sensor_byte_sample_data
```

相关声明：[sensor_byte_sample_data](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.2\_数据成员（Data Fields）

<a id="r_ab18ad72251bae040fc4752bc125be3ba"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#ab18ad72251bae040fc4752bc125be3ba)。

<a id="r_ad4ac07ed10938265e89a43133c41af24"></a>

```c
struct sensor_byte_data::sensor_byte_sample_data readings [1]
```

相关声明：[sensor_byte_data::sensor_byte_sample_data](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)、[readings](#ad4ac07ed10938265e89a43133c41af24)。

## 33.3\_详细说明（Detailed Documentation）

<a id="ab18ad72251bae040fc4752bc125be3ba"></a>

### `header`

```c
struct sensor_data_header sensor_byte_data::header
```

<a id="ad4ac07ed10938265e89a43133c41af24"></a>

### `readings`

```c
struct sensor_byte_data::sensor_byte_sample_data sensor_byte_data::readings[1]
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 33.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_byte_sample_data](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)
- [SENSOR_CHAN_PROX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_sensing_sensor_version_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)
