---
id: learning.zephyr-docs.network-application-model-reference.page-92
title: mqtt_sn_evt_param_联合体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmqtt__sn__evt__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_mqtt\_sn\_evt\_param\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionmqtt__sn__evt__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

事件元数据（Event Metadata）。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

事件元数据（Event Metadata）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_aeed83942de752c891c93ac1d350ab69f"></a>

```c
struct mqtt_sn_data data
```

相关声明：[mqtt_sn_data](P069_mqtt_sn_data_结构体.md)、[data](#a2440375957dae427bb61526331052567)。

与事件关联的载荷数据（Payload Data）。

<a id="r_afe7d7586a4ef47ca0e71fac0de0f9d2f"></a>

```c
enum mqtt_sn_topic_type topic_type
```

相关声明：[mqtt_sn_topic_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabca9262da31b09086b0f802d15eea3fd)、[topic_type](#ab7930bb48e91a24a79593e375f17cdf1)。

事件的主题类型（Topic Type）。

<a id="r_ab66e88898d378de80a57d5dd3f152a4e"></a>

```c
uint16_t topic_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[topic_id](#ae79e9793f8fc70cc781c4527d8f8496d)。

事件主题的标识符（Topic Identifier）。

<a id="r_afa0ea7d03a7ffdc95c68848af4c9f3ae"></a>

```c
} publish
```

相关声明：[publish](#afa0ea7d03a7ffdc95c68848af4c9f3ae)。

保存发布事件详情（Publish Event Details）的结构。

## 92.2\_详细说明（Detailed Documentation）

<a id="a2440375957dae427bb61526331052567"></a>

### `data`

```c
struct mqtt_sn_data mqtt_sn_evt_param::data
```

与事件关联的载荷数据（Payload Data）。

<a id="afa0ea7d03a7ffdc95c68848af4c9f3ae"></a>

### `[struct]`

```c
struct { ... } mqtt_sn_evt_param::publish
```

保存发布事件详情（Publish Event Details）的结构。

<a id="ae79e9793f8fc70cc781c4527d8f8496d"></a>

### `topic_id`

```c
uint16_t mqtt_sn_evt_param::topic_id
```

事件主题的标识符（Topic Identifier）。

<a id="ab7930bb48e91a24a79593e375f17cdf1"></a>

### `topic_type`

```c
enum mqtt_sn_topic_type mqtt_sn_evt_param::topic_type
```

事件的主题类型（Topic Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [mqtt_sn_data](P069_mqtt_sn_data_结构体.md)
- [mqtt_sn_topic_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabca9262da31b09086b0f802d15eea3fd)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_mqtt_evt_param_联合体.md) · [返回大纲](大纲.md)
