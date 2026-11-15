---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-36
title: sensor_data_generic_header_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__data__generic__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_sensor\_data\_generic\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__data__generic__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a429e22b3191df271ccfe321b796e1ac9"></a>

```c
uint64_t timestamp_ns
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[timestamp_ns](#a429e22b3191df271ccfe321b796e1ac9)。

从传感器采集数据时的时间戳。

<a id="r_a7edbe674f28c95f3aa40b1df84ca61fe"></a>

```c
uint32_t num_channels
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_channels](#a7edbe674f28c95f3aa40b1df84ca61fe)。

<a id="r_a68067521c1058b6802176e1d48fed788"></a>

```c
int8_t shift
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[shift](#a68067521c1058b6802176e1d48fed788)。

帧内所有样本的移位值（shift value）。

<a id="r_ac09f23959c66ff75b0854a95e8d4504b"></a>

```c
struct sensor_chan_spec channels [0]
```

相关声明：[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)、[channels](#ac09f23959c66ff75b0854a95e8d4504b)。

帧中包含的通道。

## 36.2\_详细说明（Detailed Documentation）

<a id="ac09f23959c66ff75b0854a95e8d4504b"></a>

### `channels`

```c
struct sensor_chan_spec sensor_data_generic_header::channels[0]
```

帧中包含的通道。

<a id="a7edbe674f28c95f3aa40b1df84ca61fe"></a>

### `num_channels`

```c
uint32_t sensor_data_generic_header::num_channels
```

<a id="a68067521c1058b6802176e1d48fed788"></a>

### `shift`

```c
int8_t sensor_data_generic_header::shift
```

帧内所有样本的移位值（shift value）。

<a id="a429e22b3191df271ccfe321b796e1ac9"></a>

### `timestamp_ns`

```c
uint64_t sensor_data_generic_header::timestamp_ns
```

从传感器采集数据时的时间戳。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [sensor_chan_spec](P035_sensor_chan_spec_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_sensor_chan_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_sensor_data_header_结构体.md)
