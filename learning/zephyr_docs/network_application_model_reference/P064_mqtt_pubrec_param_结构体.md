---
id: learning.zephyr-docs.network-application-model-reference.page-64
title: mqtt_pubrec_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubrec__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_mqtt\_pubrec\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubrec__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT发布已接收（PUBREC）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT发布已接收（PUBREC）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_ab0f92884dbd6e63894210ff7f57fe62c"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#ab0f92884dbd6e63894210ff7f57fe62c)。

正在确认的PUBLISH消息的消息标识（Message ID）。

<a id="r_a4d52112e88d954a88e4c65c9be5b0b93"></a>

```c
uint8_t reason_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason_code](#a4d52112e88d954a88e4c65c9be5b0b93)。

MQTT 5.0原因码（Reason Code）。

<a id="r_acf7d23d86fa5a7d935711459e52b092d"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#acf7d23d86fa5a7d935711459e52b092d)。

MQTT 5.0属性（Properties）。

## 64.2\_详细说明（Detailed Documentation）

<a id="ab0f92884dbd6e63894210ff7f57fe62c"></a>

### `message_id`

```c
uint16_t mqtt_pubrec_param::message_id
```

正在确认的PUBLISH消息的消息标识（Message ID）。

<a id="acf7d23d86fa5a7d935711459e52b092d"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_pubrec_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a4d52112e88d954a88e4c65c9be5b0b93"></a>

### `reason_code`

```c
uint8_t mqtt_pubrec_param::reason_code
```

MQTT 5.0原因码（Reason Code）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_mqtt_publish_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_mqtt_pubrel_param_结构体.md)
