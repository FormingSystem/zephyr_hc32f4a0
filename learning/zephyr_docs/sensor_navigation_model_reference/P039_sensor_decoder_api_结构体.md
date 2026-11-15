---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-39
title: sensor_decoder_api_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__decoder__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_sensor\_decoder\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__decoder__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

解码单个原始数据缓冲区。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

解码一个原始数据缓冲区。数据缓冲区通过传给 `sensor_read` 的实时输入/输出（RTIO）上下文提供。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a0693dd5369a21c12ce4539ad2dd8940e"></a>

```c
int(* get_frame_count )(const uint8_t *buffer, struct sensor_chan_spec chan_spec, uint16_t *frame_count)
```

相关声明：[get_frame_count](#a0693dd5369a21c12ce4539ad2dd8940e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

从缓冲区获取指定 `chan_spec` 的帧数 `frame_count`。

<a id="r_a026be8086386e9eea0a1cb25c1cd602e"></a>

```c
int(* get_size_info )(struct sensor_chan_spec channel, size_t *base_size, size_t *frame_size)
```

相关声明：[get_size_info](#a026be8086386e9eea0a1cb25c1cd602e)、[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)。

获取解码给定通道所需的空间大小。

<a id="r_a2d219ff0ea1ce71976a5e81814e3a3ff"></a>

```c
int(* decode )(const uint8_t *buffer, struct sensor_chan_spec chan_spec, uint32_t *fit, uint16_t max_count, void *data_out)
```

相关声明：[decode](#a2d219ff0ea1ce71976a5e81814e3a3ff)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

从缓冲区解码 `chan_spec` 指定的帧，最多解码 `max_count` 帧。

<a id="r_a78706bae0f1314615b5804736ef43493"></a>

```c
bool(* has_trigger )(const uint8_t *buffer, enum sensor_trigger_type trigger)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_trigger](#a78706bae0f1314615b5804736ef43493)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)。

检查是否存在给定的触发类型（trigger type）。

## 39.2\_详细说明（Detailed Documentation）

<a id="a2d219ff0ea1ce71976a5e81814e3a3ff"></a>

### `decode`

```c
int(* sensor_decoder_api::decode) (const uint8_t *buffer, struct sensor_chan_spec chan_spec, uint32_t *fit, uint16_t max_count, void *data_out)
```

从缓冲区解码 `chan_spec` 指定的帧，最多解码 `max_count` 帧。

示例演示为每个距离传感器通道最多解码 `MAX_FRAMES` 帧的过程。切换到新通道时重置帧迭代器，使每个通道的全部历史数据都能够被解码。

原始示例（Example）：

```c
for (int i = 0; i < NUM_DISTANCE_CHANNELS; i++) {
    fit = 0;
    decoder->decode(buffer, {SENSOR_CHAN_DISTANCE, i}, &fit, MAX_FRAMES, out);
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buffer` | 通过 RTIO 上下文提供的缓冲区。 |
| `[in] chan_spec` | 要解码的通道规格（channel specification）。 |
| `[in,out] fit` | 当前帧迭代器（frame iterator）。 |
| `[in] max_count` | 要解码的最大帧数。 |
| `[out] data_out` | 解码后的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效或通道不受支持。 |
| `-ENODATA` | 帧中不存在所请求的数据类型。 |

**返回（Returns）**：返回值：已解码的帧数。

<a id="a0693dd5369a21c12ce4539ad2dd8940e"></a>

### `get_frame_count`

```c
int(* sensor_decoder_api::get_frame_count) (const uint8_t *buffer, struct sensor_chan_spec chan_spec, uint16_t *frame_count)
```

从缓冲区获取指定 `chan_spec` 的帧数 `frame_count`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buffer` | 通过 RTIO 上下文提供的缓冲区。 |
| `[in] chan_spec` | 要统计帧数的通道规格。 |
| `[out] frame_count` | 指定 `chan_spec` 的帧数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 无效的通道规格。 |

<a id="a026be8086386e9eea0a1cb25c1cd602e"></a>

### `get_size_info`

```c
int(* sensor_decoder_api::get_size_info) (struct sensor_chan_spec channel, size_t *base_size, size_t *frame_size)
```

获取解码给定通道所需的空间大小。

解码单帧时使用 `base_size`；每增加一帧，再增加一个 `frame_size`。例如，解码 3 帧时使用 `base_size + 2 * frame_size`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] channel` | 要查询的通道。 |
| `[out] base_size` | 解码第一帧所需的空间大小。 |
| `[out] frame_size` | 每增加一帧所需增加的空间大小。 |

**返回（Returns）**：返回值：成功时返回 0；通道不受支持时返回 `-ENOTSUP`。

<a id="a78706bae0f1314615b5804736ef43493"></a>

### `has_trigger`

```c
bool(* sensor_decoder_api::has_trigger) (const uint8_t *buffer, enum sensor_trigger_type trigger)
```

检查是否存在给定的触发类型（trigger type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buffer` | 通过 RTIO 上下文提供的缓冲区。 |
| `[in] trigger` | 要检查的触发类型。 |

**返回（Returns）**：返回值：缓冲区中是否存在该触发。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensor_chan_spec](P035_sensor_chan_spec_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)
- [RTIO](../rtio_core_reference/P001_RTIO公共接口.md)
- [sensor_read](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gace7f20e29b302e607ba274fe40a2c2bd)
- [SENSOR_CHAN_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08"></a>

---

[上一章](P038_sensor_decode_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_sensor_driver_api_结构体.md)
