---
id: learning.zephyr-docs.network-application-model-reference.page-75
title: mqtt_topic_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__topic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_mqtt\_topic\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__topic.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可订阅或发布的UTF-8编码MQTT主题（Topic）的抽象。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

可订阅或发布的UTF-8编码MQTT主题（Topic）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_ab859d08baf88e6a1ac5135e1e55158d5"></a>

```c
struct mqtt_utf8 topic
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[topic](#ab859d08baf88e6a1ac5135e1e55158d5)。

要发布到或订阅的主题（Topic）。

<a id="r_a780e90d62c094557bd3918de3b3921e6"></a>

```c
uint8_t qos
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[qos](#a780e90d62c094557bd3918de3b3921e6)。

订阅请求的服务质量（Quality of Service）。

<a id="r_adce01c71f9b31f4ac0916ed1b8628fd4"></a>

```c
uint8_t no_local
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[no_local](#adce01c71f9b31f4ac0916ed1b8628fd4)。

MQTT 5.0第3.8.3.1节：不接收本客户端消息的订阅选项（No Local subscription option）。

<a id="r_afb71b709d04a1a2caf5acb2200f3bfaa"></a>

```c
uint8_t retain_as_published
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retain_as_published](#afb71b709d04a1a2caf5acb2200f3bfaa)。

MQTT 5.0第3.8.3.1节：按发布时保留标志转发的订阅选项（Retain As Published subscription option）。

<a id="r_a52fbe1b4b5c793be0cad004829d57faa"></a>

```c
uint8_t retain_handling
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retain_handling](#a52fbe1b4b5c793be0cad004829d57faa)。

MQTT 5.0第3.8.3.1节：保留消息处理的订阅选项（Retain Handling subscription option）。

## 75.2\_详细说明（Detailed Documentation）

<a id="adce01c71f9b31f4ac0916ed1b8628fd4"></a>

### `no_local`

```c
uint8_t mqtt_topic::no_local
```

MQTT 5.0第3.8.3.1节：不接收本客户端消息的订阅选项（No Local subscription option）。

<a id="a780e90d62c094557bd3918de3b3921e6"></a>

### `qos`

```c
uint8_t mqtt_topic::qos
```

订阅请求的服务质量（Quality of Service）。

详情见mqtt_qos。

<a id="afb71b709d04a1a2caf5acb2200f3bfaa"></a>

### `retain_as_published`

```c
uint8_t mqtt_topic::retain_as_published
```

MQTT 5.0第3.8.3.1节：按发布时保留标志转发的订阅选项（Retain As Published subscription option）。

<a id="a52fbe1b4b5c793be0cad004829d57faa"></a>

### `retain_handling`

```c
uint8_t mqtt_topic::retain_handling
```

MQTT 5.0第3.8.3.1节：保留消息处理的订阅选项（Retain Handling subscription option）。

<a id="ab859d08baf88e6a1ac5135e1e55158d5"></a>

### `topic`

```c
struct mqtt_utf8 mqtt_topic::topic
```

要发布到或订阅的主题（Topic）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga396015e492b0fee8da37c7168d9cdb33)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_mqtt_subscription_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_mqtt_topic_alias_结构体.md)
