---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-35
title: sensor_chan_spec_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__chan__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_sensor\_chan\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__chan__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器通道规格（Sensor Channel Specification）。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

传感器通道规格（Sensor Channel Specification）。它是每个传感器设备中描述某个测量通道的唯一标识符。注意：由于 `sensor_chan_spec` 的大小只有一个机器字，通常按值传递。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a1b2f0ecdc23e0d235536eb5fcdeeb63c"></a>

```c
uint16_t chan_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chan_type](#a1b2f0ecdc23e0d235536eb5fcdeeb63c)。

传感器通道类型。

<a id="r_a00d4a927cfeae33b2beea8cdc415dda1"></a>

```c
uint16_t chan_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chan_idx](#a00d4a927cfeae33b2beea8cdc415dda1)。

传感器通道索引。

## 35.2\_详细说明（Detailed Documentation）

<a id="a00d4a927cfeae33b2beea8cdc415dda1"></a>

### `chan_idx`

```c
uint16_t sensor_chan_spec::chan_idx
```

传感器通道索引。

<a id="a1b2f0ecdc23e0d235536eb5fcdeeb63c"></a>

### `chan_type`

```c
uint16_t sensor_chan_spec::chan_type
```

传感器通道类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sensor_chan_spec](P035_sensor_chan_spec_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_sensor_byte_data__sensor_byte_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_sensor_data_generic_header_结构体.md)
