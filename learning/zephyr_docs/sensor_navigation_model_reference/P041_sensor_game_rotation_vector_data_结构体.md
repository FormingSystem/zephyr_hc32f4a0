---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-41
title: sensor_game_rotation_vector_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__game__rotation__vector__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_sensor\_game\_rotation\_vector\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__game__rotation__vector__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

报告游戏旋转向量（Game Rotation Vector）数据的传感器通道数据。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="details"></a>

报告游戏旋转向量（game rotation vector）数据的传感器通道所使用的数据。供以下通道使用：`SENSOR_CHAN_GAME_ROTATION_VECTOR`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 41.1\_数据结构（Data Structures）

<a id="r_sensor_5Fgame_5Frotation_5Fvector_5Fsample_5Fdata"></a>

```c
struct sensor_game_rotation_vector_sample_data
```

相关声明：[sensor_game_rotation_vector_sample_data](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.2\_数据成员（Data Fields）

<a id="r_abb709edf89ac7dc720a5f307cd1a48bb"></a>

```c
struct sensor_data_header header
```

相关声明：[sensor_data_header](P037_sensor_data_header_结构体.md)、[header](#abb709edf89ac7dc720a5f307cd1a48bb)。

<a id="r_a22817d2c2b6b9e04ab574eb816df5442"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#a22817d2c2b6b9e04ab574eb816df5442)。

<a id="r_acc17463dbd99f1ce4fc6a0c42a6bf0c2"></a>

```c
struct sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data readings [1]
```

相关声明：[sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)、[readings](#acc17463dbd99f1ce4fc6a0c42a6bf0c2)。

## 41.3\_详细说明（Detailed Documentation）

<a id="abb709edf89ac7dc720a5f307cd1a48bb"></a>

### `header`

```c
struct sensor_data_header sensor_game_rotation_vector_data::header
```

<a id="acc17463dbd99f1ce4fc6a0c42a6bf0c2"></a>

### `readings`

```c
struct sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data sensor_game_rotation_vector_data::readings[1]
```

<a id="a22817d2c2b6b9e04ab574eb816df5442"></a>

### `shift`

```c
int8_t sensor_game_rotation_vector_data::shift
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 41.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [sensor_game_rotation_vector_sample_data](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)
- [sensor_data_header](P037_sensor_data_header_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [SENSOR_CHAN_GAME_ROTATION_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_sensor_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)
