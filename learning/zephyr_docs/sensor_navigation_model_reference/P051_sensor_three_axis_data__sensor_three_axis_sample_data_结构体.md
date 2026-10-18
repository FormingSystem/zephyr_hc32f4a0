---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-51
title: sensor_three_axis_data__sensor_three_axis_sample_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__data_1_1sensor__three__axis__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_sensor\_three\_axis\_data\_\_sensor\_three\_axis\_sample\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__data_1_1sensor__three__axis__sample__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a62dd4febada1d6b0b0fad600747089a2"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#a62dd4febada1d6b0b0fad600747089a2)。

```c
union {
```

<a id="r_a8e13de2926d68ff4f4bef1ba6b7000aa"></a>

```c
q31_t values [3]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[values](#aa8a07324f3139a6a34f695927a1d6486)。

<a id="r_a88a93ab0f7db4bb785f4de7c143e58b7"></a>

```c
q31_t v [3]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[v](#aa0de6e1354c259857b2b5a89717a5f9a)。

```c
struct {
```

<a id="r_ad64bc830d7c0a88379da363fb8e0b755"></a>

```c
q31_t x
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[x](#a60a8b323508fb4ececd4c3bdad770525)。

<a id="r_a4a9b287a5423dda7e61eb75ff16d0c15"></a>

```c
q31_t y
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[y](#ac78d9fa7e085025f1ccc9f53bf30f3bb)。

<a id="r_a0084c08d984643c35b2df32f72cbaa65"></a>

```c
q31_t z
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[z](#a5ef91a336b07c2c3e79ed34afbbf8850)。

<a id="r_aede768d969d3b24df5c5263a377e1401"></a>

```c
}
```

<a id="r_a193b99770e283c803a08db173b457431"></a>

```c
};
```

## 51.2\_详细说明（Detailed Documentation）

<a id="a193b99770e283c803a08db173b457431"></a>

### `[union]`

```c
union { ... } sensor_three_axis_data::sensor_three_axis_sample_data
```

<a id="a62dd4febada1d6b0b0fad600747089a2"></a>

### `timestamp_delta`

```c
uint32_t sensor_three_axis_data::sensor_three_axis_sample_data::timestamp_delta
```

<a id="aa0de6e1354c259857b2b5a89717a5f9a"></a>

### `v`

```c
q31_t sensor_three_axis_data::sensor_three_axis_sample_data::v[3]
```

<a id="aa8a07324f3139a6a34f695927a1d6486"></a>

### `values`

```c
q31_t sensor_three_axis_data::sensor_three_axis_sample_data::values[3]
```

<a id="a60a8b323508fb4ececd4c3bdad770525"></a>

### `x`

```c
q31_t sensor_three_axis_data::sensor_three_axis_sample_data::x
```

<a id="ac78d9fa7e085025f1ccc9f53bf30f3bb"></a>

### `y`

```c
q31_t sensor_three_axis_data::sensor_three_axis_sample_data::y
```

<a id="a5ef91a336b07c2c3e79ed34afbbf8850"></a>

### `z`

```c
q31_t sensor_three_axis_data::sensor_three_axis_sample_data::z
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [sensor_three_axis_data::sensor_three_axis_sample_data](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_sensor_three_axis_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_sensor_trigger_结构体.md)
