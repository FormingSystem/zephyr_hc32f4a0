---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-47
title: sensor_read_config_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__read__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_sensor\_read\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__read__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ad49d5ab5293017d1ad2cf60adc542090"></a>

```c
const struct device * sensor
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[sensor](#ad49d5ab5293017d1ad2cf60adc542090)。

<a id="r_aca96de2c23fb63f887c4c40dcb272798"></a>

```c
const bool is_streaming
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_streaming](#aca96de2c23fb63f887c4c40dcb272798)。

```c
union {
```

<a id="r_a7d3c24965b9b30d5cfb30e4345b2143b"></a>

```c
struct sensor_chan_spec *const channels
```

相关声明：[sensor_chan_spec](P035_sensor_chan_spec_结构体.md)、[channels](#a2aff44f02b25fd4ad1d4bc217800fad1)。

<a id="r_a943f15f4629c994156da2653f6d59646"></a>

```c
struct sensor_stream_trigger *const triggers
```

相关声明：[sensor_stream_trigger](P048_sensor_stream_trigger_结构体.md)、[triggers](#a6eaa6df7bc9378abe0f5b4b8c9a05909)。

<a id="r_a7ee7e4bbe5132206f84eec1e0cba36ca"></a>

```c
};
```

<a id="r_a5236049e0563ebba754994d70e22383a"></a>

```c
size_t count
```

相关声明：[count](#a5236049e0563ebba754994d70e22383a)。

<a id="r_aecb9c899e292fdb25c3c990bdaf1c76b"></a>

```c
const size_t max
```

相关声明：[max](#aecb9c899e292fdb25c3c990bdaf1c76b)。

## 47.2\_详细说明（Detailed Documentation）

<a id="a7ee7e4bbe5132206f84eec1e0cba36ca"></a>

### `[union]`

```c
union { ... } sensor_read_config
```

<a id="a2aff44f02b25fd4ad1d4bc217800fad1"></a>

### `channels`

```c
struct sensor_chan_spec* const sensor_read_config::channels
```

<a id="a5236049e0563ebba754994d70e22383a"></a>

### `count`

```c
size_t sensor_read_config::count
```

<a id="aca96de2c23fb63f887c4c40dcb272798"></a>

### `is_streaming`

```c
const bool sensor_read_config::is_streaming
```

<a id="aecb9c899e292fdb25c3c990bdaf1c76b"></a>

### `max`

```c
const size_t sensor_read_config::max
```

<a id="ad49d5ab5293017d1ad2cf60adc542090"></a>

### `sensor`

```c
const struct device* sensor_read_config::sensor
```

<a id="a6eaa6df7bc9378abe0f5b4b8c9a05909"></a>

### `triggers`

```c
struct sensor_stream_trigger* const sensor_read_config::triggers
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [sensor_chan_spec](P035_sensor_chan_spec_结构体.md)
- [sensor_stream_trigger](P048_sensor_stream_trigger_结构体.md)
- [sensor_read_config](P047_sensor_read_config_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_sensor_stream_trigger_结构体.md)
