---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-30
title: sensing_sensor_value_q31_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__q31.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_sensing\_sensor\_value\_q31\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__q31.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示单个单轴值（Single 1-Axis Value）的传感器值数据结构。

```c
#include <zephyr/sensing/sensing_datatypes.h>
```

<a id="details"></a>

单轴数值的传感器值数据结构。`sensing_sensor_value_q31` 是 Q31 版本，可用于 `SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE` 传感器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_af3dbde41e764de34d1b2b38800909da9"></a>

```c
struct sensing_sensor_value_header header
```

相关声明：[sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)、[header](#af3dbde41e764de34d1b2b38800909da9)。

传感器值数据结构的头部（header）。

<a id="r_a555e1bec3fe6f781fd12c13a097d4f16"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#a555e1bec3fe6f781fd12c13a097d4f16)。

`q31_t v` 读数的移位值（shift value）。

```c
struct {
```

<a id="r_a9e2f34a9eb8f5d6e0d1e173af6d7b023"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#aff3865d5645e7cb53718b4f09b20b162)。

读数的时间戳增量（timestamp delta）。

<a id="r_aed4f2bffc18613573df90603450306d8"></a>

```c
q31_t v
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[v](#ad3ed83faec34ebce96e57e23aab36101)。

读数值。

<a id="r_a94e301bf8a27dfdb0e5e6c2d6540b83b"></a>

```c
} readings [1]
```

相关声明：[readings](#a94e301bf8a27dfdb0e5e6c2d6540b83b)。

读数数组。

## 30.2\_详细说明（Detailed Documentation）

<a id="af3dbde41e764de34d1b2b38800909da9"></a>

### `header`

```c
struct sensing_sensor_value_header sensing_sensor_value_q31::header
```

传感器值数据结构的头部（header）。

<a id="a94e301bf8a27dfdb0e5e6c2d6540b83b"></a>

### `[struct]`

```c
struct { ... } sensing_sensor_value_q31::readings[1]
```

读数数组。

<a id="a555e1bec3fe6f781fd12c13a097d4f16"></a>

### `shift`

```c
int8_t sensing_sensor_value_q31::shift
```

`q31_t v` 读数的移位值（shift value）。

<a id="aff3865d5645e7cb53718b4f09b20b162"></a>

### `timestamp_delta`

```c
uint32_t sensing_sensor_value_q31::timestamp_delta
```

读数的时间戳增量（timestamp delta）。

单位为微秒。

<a id="ad3ed83faec34ebce96e57e23aab36101"></a>

### `v`

```c
q31_t sensing_sensor_value_q31::v
```

读数值。

对于 `SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE`，单位为度（degrees）。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing_datatypes.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html)
- [sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sensing_sensor_value_q31](P030_sensing_sensor_value_q31_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_sensing_sensor_value_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_sensing_sensor_value_uint32_结构体.md)
