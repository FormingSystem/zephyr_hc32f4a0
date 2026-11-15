---
id: learning.zephyr-docs.network-application-model-reference.page-65
title: mqtt_pubrel_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubrel__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_mqtt\_pubrel\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__pubrel__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT发布释放（PUBREL）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT发布释放（PUBREL）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a4333fba7ac37d5a68fe921453b56b572"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#a4333fba7ac37d5a68fe921453b56b572)。

正在确认的PUBREC消息的消息标识（Message ID）。

<a id="r_a8fe8b7921add0b5fa2926a9eec68d102"></a>

```c
uint8_t reason_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason_code](#a8fe8b7921add0b5fa2926a9eec68d102)。

MQTT 5.0原因码（Reason Code）。

<a id="r_a4e2c97c37bc4c43fd4a63391372dfed3"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#a4e2c97c37bc4c43fd4a63391372dfed3)。

MQTT 5.0属性（Properties）。

## 65.2\_详细说明（Detailed Documentation）

<a id="a4333fba7ac37d5a68fe921453b56b572"></a>

### `message_id`

```c
uint16_t mqtt_pubrel_param::message_id
```

正在确认的PUBREC消息的消息标识（Message ID）。

<a id="a4e2c97c37bc4c43fd4a63391372dfed3"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_pubrel_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a8fe8b7921add0b5fa2926a9eec68d102"></a>

### `reason_code`

```c
uint8_t mqtt_pubrel_param::reason_code
```

MQTT 5.0原因码（Reason Code）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_mqtt_pubrec_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_mqtt_sec_config_结构体.md)
