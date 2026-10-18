---
id: learning.zephyr-docs.network-application-model-reference.page-73
title: mqtt_suback_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__suback__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_mqtt\_suback\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__suback__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT订阅确认（SUBACK）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT订阅确认（SUBACK）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a985b53444e7b2c10ab68844fcee34ee4"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#a985b53444e7b2c10ab68844fcee34ee4)。

正在确认的SUBSCRIBE消息的消息标识（Message ID）。

<a id="r_a94ef5183aa3438db0521f445650c5868"></a>

```c
struct mqtt_binstr return_codes
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[return_codes](#a94ef5183aa3438db0521f445650c5868)。

MQTT 3.1：返回码表示订阅列表中各主题获准的最高服务质量（QoS）等级。

<a id="r_a5f0eff81eef7d9dc0767addea0782bf5"></a>

```c
struct mqtt_common_ack_properties prop
```

相关声明：[mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)、[prop](#a5f0eff81eef7d9dc0767addea0782bf5)。

MQTT 5.0属性（Properties）。

## 73.2\_详细说明（Detailed Documentation）

<a id="a985b53444e7b2c10ab68844fcee34ee4"></a>

### `message_id`

```c
uint16_t mqtt_suback_param::message_id
```

正在确认的SUBSCRIBE消息的消息标识（Message ID）。

<a id="a5f0eff81eef7d9dc0767addea0782bf5"></a>

### `prop`

```c
struct mqtt_common_ack_properties mqtt_suback_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a94ef5183aa3438db0521f445650c5868"></a>

### `return_codes`

```c
struct mqtt_binstr mqtt_suback_param::return_codes
```

MQTT 3.1：返回码表示订阅列表中各主题获准的最高服务质量（QoS）等级。

MQTT 5.0：与订阅列表中各主题对应的原因码（Reason Codes）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [mqtt_common_ack_properties](P055_mqtt_common_ack_properties_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_mqtt_sn_will_update_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_mqtt_subscription_list_结构体.md)
