---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-50
title: sensor_three_axis_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_sensor\_three\_axis\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

报告三轴（Three Axes）信息的传感器通道数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

报告三轴测量值的传感器通道所使用的数据。供以下通道使用：`SENSOR_CHAN_ACCEL_XYZ`、`SENSOR_CHAN_GYRO_XYZ`、`SENSOR_CHAN_MAGN_XYZ`、`SENSOR_CHAN_POS_DXYZ`、`SENSOR_CHAN_GRAVITY_VECTOR` 和 `SENSOR_CHAN_GBIAS_XYZ`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 50.1\_数据结构（Data Structures）

<a id="r_sensor_5Fthree_5Faxis_5Fsample_5Fdata"></a>

```c
struct sensor_three_axis_sample_data
```

相关声明：[sensor_three_axis_sample_data](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.2\_数据成员（Data Fields）

<a id="r_a6017fc7964204235e2222c4950f3650a"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#a6017fc7964204235e2222c4950f3650a)。

<a id="r_ade10fa0bd60d4b31eebed92e564539c5"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#ade10fa0bd60d4b31eebed92e564539c5)。

<a id="r_ad1a498b1cc31b18b17e69300749bbbc0"></a>

```c
struct sensor_three_axis_data::sensor_three_axis_sample_data readings [1]
```

相关声明：[sensor_three_axis_data::sensor_three_axis_sample_data](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)、[readings](#ad1a498b1cc31b18b17e69300749bbbc0)。

## 50.3\_详细说明（Detailed Documentation）

<a id="a6017fc7964204235e2222c4950f3650a"></a>

### `header`

```c
struct sensor_data_header sensor_three_axis_data::header
```

<a id="ad1a498b1cc31b18b17e69300749bbbc0"></a>

### `readings`

```c
struct sensor_three_axis_data::sensor_three_axis_sample_data sensor_three_axis_data::readings[1]
```

<a id="ade10fa0bd60d4b31eebed92e564539c5"></a>

### `shift`

```c
int8_t sensor_three_axis_data::shift
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 50.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_three_axis_sample_data](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [SENSOR_CHAN_ACCEL_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)
- [SENSOR_CHAN_GYRO_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)
- [SENSOR_CHAN_MAGN_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)
- [SENSOR_CHAN_POS_DXYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)
- [SENSOR_CHAN_GRAVITY_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)
- [SENSOR_CHAN_GBIAS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_sensor_three_axis_attribute_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)
