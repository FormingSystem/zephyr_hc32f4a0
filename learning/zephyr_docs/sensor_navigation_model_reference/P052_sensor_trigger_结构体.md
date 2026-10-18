---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-52
title: sensor_trigger_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__trigger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_sensor\_trigger\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__trigger.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器触发器规格（Sensor Trigger Spec）。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

传感器触发器规格（Sensor Trigger Spec）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_ac2cce1ec6ff82f95cb06d0dccafd7af0"></a>

```c
enum sensor_trigger_type type
```

相关声明：[sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)、[type](#ac2cce1ec6ff82f95cb06d0dccafd7af0)。

触发类型（Trigger type）。

<a id="r_ae01f99b124aa99c59b9967818022e112"></a>

```c
enum sensor_channel chan
```

相关声明：[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[chan](#ae01f99b124aa99c59b9967818022e112)。

触发器所设置的通道。

## 52.2\_详细说明（Detailed Documentation）

<a id="ae01f99b124aa99c59b9967818022e112"></a>

### `chan`

```c
enum sensor_channel sensor_trigger::chan
```

触发器所设置的通道。

<a id="ac2cce1ec6ff82f95cb06d0dccafd7af0"></a>

### `type`

```c
enum sensor_trigger_type sensor_trigger::type
```

触发类型（Trigger type）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_sensor_uint64_data_结构体.md)
