---
id: learning.zephyr-docs.network-application-model-reference.page-61
title: mqtt_pubcomp_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubcomp__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_mqtt\_pubcomp\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubcomp__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT发布完成（PUBCOMP）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT发布完成（PUBCOMP）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_ae8484ad4d62f953ecace6c990002e316"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#ae8484ad4d62f953ecace6c990002e316)。

正在确认的PUBREL消息的消息标识（Message ID）。

<a id="r_a4e969aeee8c66a10e23731f8fe74db93"></a>

```c
uint8_t reason_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason_code](#a4e969aeee8c66a10e23731f8fe74db93)。

MQTT 5.0原因码（Reason Code）。

<a id="r_a1e38cde0e4e18b091e893bf207fa6c6d"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#a1e38cde0e4e18b091e893bf207fa6c6d)。

MQTT 5.0属性（Properties）。

## 61.2\_详细说明（Detailed Documentation）

<a id="ae8484ad4d62f953ecace6c990002e316"></a>

### `message_id`

```c
uint16_t mqtt_pubcomp_param::message_id
```

正在确认的PUBREL消息的消息标识（Message ID）。

<a id="a1e38cde0e4e18b091e893bf207fa6c6d"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_pubcomp_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a4e969aeee8c66a10e23731f8fe74db93"></a>

### `reason_code`

```c
uint8_t mqtt_pubcomp_param::reason_code
```

MQTT 5.0原因码（Reason Code）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_mqtt_puback_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_mqtt_publish_message_结构体.md)
