---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-53
title: sensor_uint64_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__uint64__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_sensor\_uint64\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__uint64__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

产生类似计数值（Count-Like Value）的传感器所提供的数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

产生计数类数值的传感器所提供的数据。供以下通道使用：`SENSOR_CHAN_GAUGE_CYCLE_COUNT`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 53.1\_数据结构（Data Structures）

<a id="r_sensor_5Fuint64_5Fsample_5Fdata"></a>

```c
struct sensor_uint64_sample_data
```

相关声明：[sensor_uint64_sample_data](P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.2\_数据成员（Data Fields）

<a id="r_a61e2d0796ba3c0e95a0455e03ce01d76"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#a61e2d0796ba3c0e95a0455e03ce01d76)。

<a id="r_a86a1b96bd7a3aeb6b615e6ab0c3a96a6"></a>

```c
struct sensor_uint64_data::sensor_uint64_sample_data readings [1]
```

相关声明：[sensor_uint64_data::sensor_uint64_sample_data](P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)、[readings](#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)。

## 53.3\_详细说明（Detailed Documentation）

<a id="a61e2d0796ba3c0e95a0455e03ce01d76"></a>

### `header`

```c
struct sensor_data_header sensor_uint64_data::header
```

<a id="a86a1b96bd7a3aeb6b615e6ab0c3a96a6"></a>

### `readings`

```c
struct sensor_uint64_data::sensor_uint64_sample_data sensor_uint64_data::readings[1]
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 53.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_uint64_sample_data](P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)
- [SENSOR_CHAN_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_sensor_trigger_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)
