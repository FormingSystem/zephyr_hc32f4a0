---
id: learning.zephyr-docs.network-application-model-reference.page-60
title: mqtt_puback_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__puback__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_mqtt\_puback\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__puback__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT发布确认（PUBACK）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT发布确认（PUBACK）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a727b919b853e77e480fb841e74a2dedf"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#a727b919b853e77e480fb841e74a2dedf)。

正在确认的PUBLISH消息的消息标识（Message ID）。

<a id="r_a44307fc6b172729478f1d097bbaf34bb"></a>

```c
uint8_t reason_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason_code](#a44307fc6b172729478f1d097bbaf34bb)。

MQTT 5.0原因码（Reason Code）。

<a id="r_a5fbbc6613660883a96aa37c8def6baa5"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#a5fbbc6613660883a96aa37c8def6baa5)。

MQTT 5.0属性（Properties）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a727b919b853e77e480fb841e74a2dedf"></a>

### `message_id`

```c
uint16_t mqtt_puback_param::message_id
```

正在确认的PUBLISH消息的消息标识（Message ID）。

<a id="a5fbbc6613660883a96aa37c8def6baa5"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_puback_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a44307fc6b172729478f1d097bbaf34bb"></a>

### `reason_code`

```c
uint8_t mqtt_puback_param::reason_code
```

MQTT 5.0原因码（Reason Code）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_mqtt_internal_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_mqtt_pubcomp_param_结构体.md)
