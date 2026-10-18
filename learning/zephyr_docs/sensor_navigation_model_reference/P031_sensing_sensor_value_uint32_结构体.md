---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-31
title: sensing_sensor_value_uint32_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__uint32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_sensing\_sensor\_value\_uint32\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__uint32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示单个单轴值（Single 1-Axis Value）的传感器值数据结构。

```c
#include <zephyr/sensing/sensing_datatypes.h>
```

<a id="details"></a>

单轴数值的传感器值数据结构。`sensing_sensor_value_uint32` 是 `uint32_t` 版本，可用于 `SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT` 传感器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_adfb3431b5b5e90d29931b9861c9dcd21"></a>

```c
struct sensing_sensor_value_header header
```

相关声明：[sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)、[header](#adfb3431b5b5e90d29931b9861c9dcd21)。

传感器值数据结构的头部（header）。

```c
struct {
```

<a id="r_ac6e0ab91af9a57bd834d539a26c06c77"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#a1fd1c1d018a3793e56e4d0bfded03812)。

读数的时间戳增量（timestamp delta）。

<a id="r_ac85417b1d7f51a43a3cc3f4f95881ac9"></a>

```c
uint32_t v
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[v](#a10d8f7d8f36c4969552b297ed34bf592)。

读数值。

<a id="r_af30e831ebd860b0dec15733220bdb9df"></a>

```c
} readings [1]
```

相关声明：[readings](#af30e831ebd860b0dec15733220bdb9df)。

读数数组。

## 31.2\_详细说明（Detailed Documentation）

<a id="adfb3431b5b5e90d29931b9861c9dcd21"></a>

### `header`

```c
struct sensing_sensor_value_header sensing_sensor_value_uint32::header
```

传感器值数据结构的头部（header）。

<a id="af30e831ebd860b0dec15733220bdb9df"></a>

### `[struct]`

```c
struct { ... } sensing_sensor_value_uint32::readings[1]
```

读数数组。

<a id="a1fd1c1d018a3793e56e4d0bfded03812"></a>

### `timestamp_delta`

```c
uint32_t sensing_sensor_value_uint32::timestamp_delta
```

读数的时间戳增量（timestamp delta）。

单位为微秒。

<a id="a10d8f7d8f36c4969552b297ed34bf592"></a>

### `v`

```c
uint32_t sensing_sensor_value_uint32::v
```

读数值。

对于 `SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT`，单位为勒克斯（lux）。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing_datatypes.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html)
- [sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sensing_sensor_value_uint32](P031_sensing_sensor_value_uint32_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_sensing_sensor_value_q31_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_sensing_sensor_version_结构体.md)
