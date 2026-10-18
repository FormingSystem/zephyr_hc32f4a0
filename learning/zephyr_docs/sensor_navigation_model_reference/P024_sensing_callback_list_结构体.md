---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-24
title: sensing_callback_list_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__callback__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_sensing\_callback\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__callback__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器实例（Sensor Instance）的回调注册。

```c
#include <zephyr/sensing/sensing.h>
```

<a id="details"></a>

传感器实例的回调注册信息，即感知子系统（Sensing subsystem）的事件回调列表。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a7d0d7c878e338f19fd48c66cda9d04fc"></a>

```c
sensing_data_event_t on_data_event
```

相关声明：[sensing_data_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga5440a8914b664209d62388183b3c89ea)、[on_data_event](#a7d0d7c878e338f19fd48c66cda9d04fc)。

传感器数据事件的回调函数。

<a id="r_a43504dbe7d484f0d0e7d33b8bb6318d4"></a>

```c
void * context
```

相关声明：[context](#a43504dbe7d484f0d0e7d33b8bb6318d4)。

将传给回调的上下文（context）。

## 24.2\_详细说明（Detailed Documentation）

<a id="a43504dbe7d484f0d0e7d33b8bb6318d4"></a>

### `context`

```c
void* sensing_callback_list::context
```

将传给回调的上下文（context）。

<a id="a7d0d7c878e338f19fd48c66cda9d04fc"></a>

### `on_data_event`

```c
sensing_data_event_t sensing_callback_list::on_data_event
```

传感器数据事件的回调函数。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html)
- [sensing_data_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga5440a8914b664209d62388183b3c89ea)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_r502a_template_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_sensing_sensor_config_结构体.md)
