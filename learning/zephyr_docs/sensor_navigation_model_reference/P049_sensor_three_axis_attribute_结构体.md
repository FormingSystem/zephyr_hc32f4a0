---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-49
title: sensor_three_axis_attribute_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__attribute.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_sensor\_three\_axis\_attribute\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__three__axis__attribute.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

供以下通道/属性对（Channel / Attribute Pairs）使用：

```c
#include <zephyr/drivers/sensor_attribute_types.h>
```

<a id="details"></a>

供以下通道/属性组合使用：`SENSOR_CHAN_ACCEL_XYZ` 与 `SENSOR_ATTR_OFFSET`；`SENSOR_CHAN_GYRO_XYZ` 与 `SENSOR_ATTR_OFFSET`；`SENSOR_CHAN_MAGN_XYZ` 与 `SENSOR_ATTR_OFFSET`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a230f8021356406c3225868d43e39be18"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#a230f8021356406c3225868d43e39be18)。

```c
union {
```

```c
struct {
```

<a id="r_a5c2e54fa0ee3ec94345ba5bc608b38f1"></a>

```c
q31_t x
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[x](#a82ee018216949a3132fcdf165e63d2be)。

<a id="r_aa9b4a9baf37035a271002996f8de5b96"></a>

```c
q31_t y
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[y](#a5c1bd40fb615aa6515c10ff249bae0c2)。

<a id="r_a86cbe8ac1f48f5501d51d6824bbe1b3d"></a>

```c
q31_t z
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[z](#afee1c9c4fc2b18fb5ae7f6a69af6e2e9)。

<a id="r_a4ddc642131d1bb48e1a4c2385ac01538"></a>

```c
}
```

<a id="r_a8ec8f682cb08d3dd9fe1047a040ed8ce"></a>

```c
q31_t values [3]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[values](#a88cb3f5259b9dde34c5b26daae4ed270)。

<a id="r_abf2ad5c8026b94c5632bdaab099362c6"></a>

```c
};
```

## 49.2\_详细说明（Detailed Documentation）

<a id="abf2ad5c8026b94c5632bdaab099362c6"></a>

### `[union]`

```c
union { ... } sensor_three_axis_attribute
```

<a id="a230f8021356406c3225868d43e39be18"></a>

### `shift`

```c
int8_t sensor_three_axis_attribute::shift
```

<a id="a88cb3f5259b9dde34c5b26daae4ed270"></a>

### `values`

```c
q31_t sensor_three_axis_attribute::values[3]
```

<a id="a82ee018216949a3132fcdf165e63d2be"></a>

### `x`

```c
q31_t sensor_three_axis_attribute::x
```

<a id="a5c1bd40fb615aa6515c10ff249bae0c2"></a>

### `y`

```c
q31_t sensor_three_axis_attribute::y
```

<a id="afee1c9c4fc2b18fb5ae7f6a69af6e2e9"></a>

### `z`

```c
q31_t sensor_three_axis_attribute::z
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_attribute_types.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_attribute_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [sensor_three_axis_attribute](P049_sensor_three_axis_attribute_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_sensor_stream_trigger_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_sensor_three_axis_data_结构体.md)
