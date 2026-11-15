---
id: learning.zephyr-docs.network-application-model-reference.page-78
title: mqtt_unsuback_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__unsuback__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_mqtt\_unsuback\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__unsuback__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT取消订阅确认（UNSUBACK）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT取消订阅确认（UNSUBACK）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_aa453177181e07cd0532b8cf591be0f32"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#aa453177181e07cd0532b8cf591be0f32)。

正在确认的UNSUBSCRIBE消息的消息标识（Message ID）。

<a id="r_a992c0c038413377c8edd701d2ef8455e"></a>

```c
struct mqtt_binstr reason_codes
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[reason_codes](#a992c0c038413377c8edd701d2ef8455e)。

与取消订阅列表中各主题对应的原因码（Reason Codes）。

<a id="r_a543fb60386725e9096bb0243beaa1181"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#a543fb60386725e9096bb0243beaa1181)。

MQTT 5.0属性（Properties）。

## 78.2\_详细说明（Detailed Documentation）

<a id="aa453177181e07cd0532b8cf591be0f32"></a>

### `message_id`

```c
uint16_t mqtt_unsuback_param::message_id
```

正在确认的UNSUBSCRIBE消息的消息标识（Message ID）。

<a id="a543fb60386725e9096bb0243beaa1181"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_unsuback_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a992c0c038413377c8edd701d2ef8455e"></a>

### `reason_codes`

```c
struct mqtt_binstr mqtt_unsuback_param::reason_codes
```

与取消订阅列表中各主题对应的原因码（Reason Codes）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_mqtt_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_mqtt_utf8_结构体.md)
