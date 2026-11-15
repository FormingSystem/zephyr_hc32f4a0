---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-38
title: sensor_decode_context_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__decode__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_sensor\_decode\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__decode__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于通过sensor_decoder_api遍历数据帧（Data Frames）。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

用于通过 `sensor_decoder_api` 遍历数据帧。用法示例：

```c
(.c)
   struct sensor_decode_context ctx = SENSOR_DECODE_CONTEXT_INIT(
       decoder, buffer, SENSOR_CHAN_ACCEL_XYZ, 0);

   while (true) {
     struct sensor_three_axis_data accel_out_data;

     num_decoded_channels = sensor_decode(ctx, &accel_out_data, 1);

     if (num_decoded_channels <= 0) {
       printk("Done decoding buffer\n");
       break;
     }

     printk("Decoded (%" PRId32 ", %" PRId32 ", %" PRId32 ")\n", accel_out_data.readings[0].x,
         accel_out_data.readings[0].y, accel_out_data.readings[0].z);
   }
```

译注：示例代码按官方原样保留，包括开头的 `(.c)` 标记。

原页符号提示：`sensor_decode` 的声明为 `static int sensor_decode(struct sensor_decode_context *ctx, void *out, uint16_t max_count)`，使用 `sensor_decode_context` 解码 N 帧，定义于 `sensor.h:725`。`SENSOR_DECODE_CONTEXT_INIT` 的声明为 `#define SENSOR_DECODE_CONTEXT_INIT(decoder_, buffer_, channel_type_, channel_index_)`，用于初始化 `sensor_decode_context`，定义于 `sensor.h:709`。`SENSOR_CHAN_ACCEL_XYZ`（`@ SENSOR_CHAN_ACCEL_XYZ`）表示 X、Y、Z 轴的加速度，定义于 `sensor.h:74`。`PRId32`（`#define PRId32`）定义于 `inttypes.h:15`。`printk` 的声明为 `void printk(const char *fmt,...)`，用于打印内核调试消息。`sensor_decode_context` 用于通过 `sensor_decoder_api` 遍历数据帧，定义于 `sensor.h:699`；其 `decoder` 成员声明为 `const struct sensor_decoder_api * decoder`，定义于 `sensor.h:700`；其 `buffer` 成员声明为 `const uint8_t * buffer`，定义于 `sensor.h:701`。`sensor_three_axis_data` 保存报告三轴测量值的传感器通道数据，定义于 `sensor_data_types.h:42`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a1ac0773e83a086455371d108264ef4f6"></a>

```c
const struct sensor_decoder_api * decoder
```

相关声明：[sensor_decoder_api](P039_sensor_decoder_api_结构体.md)、[decoder](#a1ac0773e83a086455371d108264ef4f6)。

<a id="r_a23e27eb0687d722be78e1b89278613d1"></a>

```c
const uint8_t * buffer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buffer](#a23e27eb0687d722be78e1b89278613d1)。

<a id="r_a1c051bd8d0030f81cc561e32b2897d74"></a>

```c
struct sensor_chan_spec channel
```

相关声明：[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)、[channel](#a1c051bd8d0030f81cc561e32b2897d74)。

<a id="r_ada9e40625829093087886c41f2fb7350"></a>

```c
uint32_t fit
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fit](#ada9e40625829093087886c41f2fb7350)。

## 38.2\_详细说明（Detailed Documentation）

<a id="a23e27eb0687d722be78e1b89278613d1"></a>

### `buffer`

```c
const uint8_t* sensor_decode_context::buffer
```

<a id="a1c051bd8d0030f81cc561e32b2897d74"></a>

### `channel`

```c
struct sensor_chan_spec sensor_decode_context::channel
```

<a id="a1ac0773e83a086455371d108264ef4f6"></a>

### `decoder`

```c
const struct sensor_decoder_api* sensor_decode_context::decoder
```

<a id="ada9e40625829093087886c41f2fb7350"></a>

### `fit`

```c
uint32_t sensor_decode_context::fit
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 38.3\_原页交叉引用（Cross References）

- [sensor_decoder_api](P039_sensor_decoder_api_结构体.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensor_chan_spec](P035_sensor_chan_spec_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sensor_decode_context](P038_sensor_decode_context_结构体.md)
- [SENSOR_DECODE_CONTEXT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae69ec503df53d2d5ee417e481f9ac9ea)
- [SENSOR_CHAN_ACCEL_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)
- [sensor_three_axis_data](P050_sensor_three_axis_data_结构体.md)
- [sensor_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga018bca56056ae2558f9e45aeb2fa5f53)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [PRId32](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html#a6d94d1417e1b35c53aee6306590de72b)

<a id="header-details"></a>
<a id="agroup__sensor__interface_html_ga018bca56056ae2558f9e45aeb2fa5f53"></a>
<a id="agroup__sensor__interface_html_gae69ec503df53d2d5ee417e481f9ac9ea"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9"></a>
<a id="ainttypes_8h_html_a6d94d1417e1b35c53aee6306590de72b"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="astructsensor__decode__context_html"></a>
<a id="astructsensor__decode__context_html_a1ac0773e83a086455371d108264ef4f6"></a>
<a id="astructsensor__decode__context_html_a23e27eb0687d722be78e1b89278613d1"></a>
<a id="astructsensor__three__axis__data_html"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_sensor_data_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_sensor_decoder_api_结构体.md)
