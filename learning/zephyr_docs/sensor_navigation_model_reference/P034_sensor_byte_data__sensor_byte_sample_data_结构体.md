---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-34
title: sensor_byte_data__sensor_byte_sample_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__byte__data_1_1sensor__byte__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_sensor\_byte\_data\_\_sensor\_byte\_sample\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__byte__data_1_1sensor__byte__sample__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_ab29a911990794b35bde3114e813d2c9a"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#ab29a911990794b35bde3114e813d2c9a)。

```c
union {
```

<a id="r_ac7b8f95b9ee523f9b13d1eaffad20dcb"></a>

```c
uint8_t value
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value](#a3ad640ff448fe87d2eda7c5118404b7a)。

```c
struct {
```

<a id="r_a643eefe3e86c9184bd6f4303733189ea"></a>

```c
uint8_t is_near: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_near](#acd42cfa0dc446378cebf998c1b795963)。

<a id="r_a87944ebc87d11d31616c63259127ee77"></a>

```c
uint8_t padding: 7
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[padding](#ab07c2a7ce6e47c61249606a88aeda2bd)。

<a id="r_a4aad36258c01eea3202d28a02aa9f1ff"></a>

```c
}
```

<a id="r_a50af39162773fe8e4a725acbba8d90d4"></a>

```c
};
```

## 34.2\_详细说明（Detailed Documentation）

<a id="a50af39162773fe8e4a725acbba8d90d4"></a>

### `[union]`

```c
union { ... } sensor_byte_data::sensor_byte_sample_data
```

<a id="acd42cfa0dc446378cebf998c1b795963"></a>

### `is_near`

```c
uint8_t sensor_byte_data::sensor_byte_sample_data::is_near
```

<a id="ab07c2a7ce6e47c61249606a88aeda2bd"></a>

### `padding`

```c
uint8_t sensor_byte_data::sensor_byte_sample_data::padding
```

<a id="ab29a911990794b35bde3114e813d2c9a"></a>

### `timestamp_delta`

```c
uint32_t sensor_byte_data::sensor_byte_sample_data::timestamp_delta
```

<a id="a3ad640ff448fe87d2eda7c5118404b7a"></a>

### `value`

```c
uint8_t sensor_byte_data::sensor_byte_sample_data::value
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensor_byte_data::sensor_byte_sample_data](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_sensor_byte_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_sensor_chan_spec_结构体.md)
