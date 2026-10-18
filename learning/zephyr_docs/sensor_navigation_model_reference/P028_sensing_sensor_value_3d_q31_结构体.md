---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-28
title: sensing_sensor_value_3d_q31_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__3d__q31.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_sensing\_sensor\_value\_3d\_q31\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__3d__q31.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于通用数据类型的传感器值（Sensor Value）数据结构类型。

```c
#include <zephyr/sensing/sensing_datatypes.h>
```

<a id="details"></a>

基于常见数据类型的传感器值数据结构，适用于惯性测量单元（IMU）、光传感器和方向传感器等常见传感器。此处为三轴传感器的数据结构：`sensing_sensor_value_3d_q31` 是 Q31 版本，可供三维 IMU 传感器使用，例如 `SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D`、`SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D` 和 `SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a163e62d50de3b5f61688ff9b00db0dcd"></a>

```c
struct sensing_sensor_value_header header
```

相关声明：[sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)、[header](#a163e62d50de3b5f61688ff9b00db0dcd)。

传感器值数据结构的头部（header）。

<a id="r_af0db9faee6eaabff7f9c2f955873378b"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#af0db9faee6eaabff7f9c2f955873378b)。

`q31_t v[3]` 读数的移位值（shift value）。

```c
struct {
```

<a id="r_a650f3a22cb4bff186805b2acd9b6fcc9"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#a1bf323a7bb69af0801acebfe03e35b7a)。

读数的时间戳增量（timestamp delta）。

```c
union {
```

<a id="r_abcf397e6c82bed400941a69ac1c1a264"></a>

```c
q31_t v [3]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[v](#a68eefb9ba2e8d954e8ea3c4f30893f3f)。

以数组表示的三维读数向量。

```c
struct {
```

<a id="r_a2c9739f85a5a55bf4287cec6bcb239ac"></a>

```c
q31_t x
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[x](#ad1d2f43d1a9a4b5333ac1b8531d6c94c)。

三维向量的 X 值。

<a id="r_ad77f50dde175c7d3ddd80009ac1e4120"></a>

```c
q31_t y
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[y](#a721b9cd33e360691b9fb07a90c3f4df2)。

三维向量的 Y 值。

<a id="r_a92f318f46dde95191ca6be3141e94b61"></a>

```c
q31_t z
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[z](#abbf0f5aaae8978eba1e5f3e2ffad20d0)。

三维向量的 Z 值。

<a id="r_a1a7c569cffd6e7775d2c5beaad68c79a"></a>

```c
}
```

<a id="r_ae30337349840c1a6feaa91fe6860943a"></a>

```c
}
```

<a id="r_aea782e09d486595b5fbd7a94f3bde253"></a>

```c
} readings [1]
```

相关声明：[readings](#aea782e09d486595b5fbd7a94f3bde253)。

读数数组。

## 28.2\_详细说明（Detailed Documentation）

<a id="a163e62d50de3b5f61688ff9b00db0dcd"></a>

### `header`

```c
struct sensing_sensor_value_header sensing_sensor_value_3d_q31::header
```

传感器值数据结构的头部（header）。

<a id="aea782e09d486595b5fbd7a94f3bde253"></a>

### `[struct]`

```c
struct { ... } sensing_sensor_value_3d_q31::readings[1]
```

读数数组。

<a id="af0db9faee6eaabff7f9c2f955873378b"></a>

### `shift`

```c
int8_t sensing_sensor_value_3d_q31::shift
```

`q31_t v[3]` 读数的移位值（shift value）。

<a id="a1bf323a7bb69af0801acebfe03e35b7a"></a>

### `timestamp_delta`

```c
uint32_t sensing_sensor_value_3d_q31::timestamp_delta
```

读数的时间戳增量（timestamp delta）。

单位为微秒。

<a id="a68eefb9ba2e8d954e8ea3c4f30893f3f"></a>

### `v`

```c
q31_t sensing_sensor_value_3d_q31::v[3]
```

以数组表示的三维读数向量。

对于 `SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D` 和 `SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D`，单位为重力加速度倍数（Gs，gravitational force）。对于 `SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D`，单位按原文为度（degrees）。

<a id="ad1d2f43d1a9a4b5333ac1b8531d6c94c"></a>

### `x`

```c
q31_t sensing_sensor_value_3d_q31::x
```

三维向量的 X 值。

<a id="a721b9cd33e360691b9fb07a90c3f4df2"></a>

### `y`

```c
q31_t sensing_sensor_value_3d_q31::y
```

三维向量的 Y 值。

<a id="abbf0f5aaae8978eba1e5f3e2ffad20d0"></a>

### `z`

```c
q31_t sensing_sensor_value_3d_q31::z
```

三维向量的 Z 值。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing_datatypes.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html)
- [sensing_sensor_value_header](P029_sensing_sensor_value_header_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sensing_sensor_value_3d_q31](P028_sensing_sensor_value_3d_q31_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_sensing_sensor_register_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_sensing_sensor_value_header_结构体.md)
