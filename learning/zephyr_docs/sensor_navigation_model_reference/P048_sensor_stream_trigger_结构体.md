---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-48
title: sensor_stream_trigger_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__stream__trigger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_sensor\_stream\_trigger\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__stream__trigger.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a9a367e746764e68140ec9120f2a016e6"></a>

```c
enum sensor_trigger_type trigger
```

相关声明：[sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)、[trigger](#a9a367e746764e68140ec9120f2a016e6)。

<a id="r_a62ccdecf7253b1bfdff4f1d659563d76"></a>

```c
enum sensor_stream_data_opt opt
```

相关声明：[sensor_stream_data_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8613a20521a37d40fd7371dc63ba2dac)、[opt](#a62ccdecf7253b1bfdff4f1d659563d76)。

## 48.2\_详细说明（Detailed Documentation）

<a id="a62ccdecf7253b1bfdff4f1d659563d76"></a>

### `opt`

```c
enum sensor_stream_data_opt sensor_stream_trigger::opt
```

<a id="a9a367e746764e68140ec9120f2a016e6"></a>

### `trigger`

```c
enum sensor_trigger_type sensor_stream_trigger::trigger
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)
- [sensor_stream_data_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8613a20521a37d40fd7371dc63ba2dac)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_sensor_read_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_sensor_three_axis_attribute_结构体.md)
