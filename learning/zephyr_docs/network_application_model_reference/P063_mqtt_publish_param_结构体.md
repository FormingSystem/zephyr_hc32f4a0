---
id: learning.zephyr-docs.network-application-model-reference.page-63
title: mqtt_publish_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__publish__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_mqtt\_publish\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__publish__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发布消息（PUBLISH）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

发布消息（PUBLISH）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_a9841a4fbb30b597a9710863ce6034688"></a>

```c
struct mqtt_publish_message message
```

相关声明：[mqtt_publish_message](P062_mqtt_publish_message_结构体.md)、[message](#a9841a4fbb30b597a9710863ce6034688)。

要发布的消息，包括主题（Topic）、服务质量（QoS）及其载荷（如有）。

<a id="r_aac4c6ba605506c183d2d5bdd7e550b3e"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#aac4c6ba605506c183d2d5bdd7e550b3e)。

发布消息所用的消息标识（Message ID）。

<a id="r_a2c2062c2b3ad027d5dfea56cb81c48e7"></a>

```c
uint8_t dup_flag: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dup_flag](#a2c2062c2b3ad027d5dfea56cb81c48e7)。

重复标志（Duplicate Flag）。

<a id="r_a9b2c6fad5bf830276d8d3f6b5ab04210"></a>

```c
uint8_t retain_flag: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retain_flag](#a9b2c6fad5bf830276d8d3f6b5ab04210)。

保留标志（Retain Flag）。

```c
struct {
```

<a id="r_a190f15b69ff030f7220afd2dcde10a9f"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a813b18b4c859fb5e703d90fc8eb9bd2e)。

MQTT 5.0第3.3.2.3.7节：用户属性（User Property）。

<a id="r_a078804239546cf3fdbdb1a298ba0ea2b"></a>

```c
struct mqtt_utf8 response_topic
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[response_topic](#a63e9311cf0acf33386ceb8328b040d2a)。

MQTT 5.0第3.3.2.3.5节：响应主题（Response Topic）。

<a id="r_a497cfcc432610c1258bdcc684d23c0ff"></a>

```c
struct mqtt_binstr correlation_data
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[correlation_data](#ab98e52ae704c6e988d554cf388b2ec0c)。

MQTT 5.0第3.3.2.3.6节：关联数据（Correlation Data）。

<a id="r_ad2f9161b3a217845ccfa2340dc5ba6c9"></a>

```c
struct mqtt_utf8 content_type
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[content_type](#a8f76494a04d91150aee2ed7e9a271243)。

MQTT 5.0第3.3.2.3.9节：内容类型（Content Type）。

<a id="r_a045a5c8606aa3b8e4b04593a89fd86b0"></a>

```c
uint32_t subscription_identifier [CONFIG_MQTT_SUBSCRIPTION_ID_PROPERTIES_MAX]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subscription_identifier](#a5edb680fe44b795b02e35fcb73b98efa)。

MQTT 5.0第3.3.2.3.8节：订阅标识符（Subscription Identifier）。

<a id="r_aa17d2bb4da3127751dd386df0a64a929"></a>

```c
uint32_t message_expiry_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[message_expiry_interval](#a4a486b254bd8e0f081251f8ca087e9d2)。

MQTT 5.0第3.3.2.3.3节：消息过期间隔（Message Expiry Interval）。

<a id="r_a42a49c7961ec7a04444ecc1b1bf14cfb"></a>

```c
uint16_t topic_alias
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[topic_alias](#a13bf77403471f79687fe63a93cd1627d)。

MQTT 5.0第3.3.2.3.4节：主题别名（Topic Alias）。

<a id="r_a03a4021b0fea3606b9b9bf80b8bc9ece"></a>

```c
uint8_t payload_format_indicator
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_format_indicator](#a8d9905f31bfc9072516f00082eda9c50)。

MQTT 5.0第3.3.2.3.2节：载荷格式指示符（Payload Format Indicator）。

```c
struct {
```

<a id="r_a69b65c14e02b086441bb920b04d3d01b"></a>

```c
bool has_payload_format_indicator
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_payload_format_indicator](#a4190ccdfbf97a4ef63121e6a841d5f79)。

包含载荷格式指示符（Payload Format Indicator）属性。

<a id="r_a8a96dc5da9162b0c2a875ba5daa2f947"></a>

```c
bool has_message_expiry_interval
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_message_expiry_interval](#a85e5a3a9c7347c506780627515dc84ea)。

包含消息过期间隔（Message Expiry Interval）属性。

<a id="r_a79a4ce9982a3b52fa5ed9283d15ec218"></a>

```c
bool has_topic_alias
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_topic_alias](#a36a4d07ed13c5d4befc51a6285606090)。

包含主题别名（Topic Alias）属性。

<a id="r_aa9199f065b09a1fbe9a1b9faea95aaf7"></a>

```c
bool has_response_topic
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_response_topic](#aafc5473b88a64df887751903314f0fac)。

包含响应主题（Response Topic）属性。

<a id="r_a59765565f5797dbcff32d5ea72cd8c3b"></a>

```c
bool has_correlation_data
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_correlation_data](#a599f8830ef4b42a68955ad58411ef0f1)。

包含关联数据（Correlation Data）属性。

<a id="r_a68c58ddaf328106819aeac5b2511f9ec"></a>

```c
bool has_user_prop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_user_prop](#a5e4b146a69c82fa36fd43adb8658ef5f)。

包含用户属性（User Property）属性。

<a id="r_abd5e3b6aa4018ac88b934217eb1e86a2"></a>

```c
bool has_subscription_identifier
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_subscription_identifier](#aab2664e89f086b62b9af5cd481fccde3)。

包含订阅标识符（Subscription Identifier）属性。

<a id="r_a95fbaee13ec9b54a911d4bfb4d2769e5"></a>

```c
bool has_content_type
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_content_type](#a00413022cecf2a624506ab5da630aefa)。

包含内容类型（Content Type）属性。

<a id="r_aa6b8c0bc4cfd8e6488ab6842b5775809"></a>

```c
} rx
```

相关声明：[rx](#a9cf950636bfa82b88bd4c3fc562c8f71)。

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="r_a5e87084f72285ebdf5d26aca0eed6f00"></a>

```c
} prop
```

相关声明：[prop](#a5e87084f72285ebdf5d26aca0eed6f00)。

MQTT 5.0属性（Properties）。

## 63.2\_详细说明（Detailed Documentation）

<a id="a8f76494a04d91150aee2ed7e9a271243"></a>

### `content_type`

```c
struct mqtt_utf8 mqtt_publish_param::content_type
```

MQTT 5.0第3.3.2.3.9节：内容类型（Content Type）。

<a id="ab98e52ae704c6e988d554cf388b2ec0c"></a>

### `correlation_data`

```c
struct mqtt_binstr mqtt_publish_param::correlation_data
```

MQTT 5.0第3.3.2.3.6节：关联数据（Correlation Data）。

<a id="a2c2062c2b3ad027d5dfea56cb81c48e7"></a>

### `dup_flag`

```c
uint8_t mqtt_publish_param::dup_flag
```

重复标志（Duplicate Flag）。

1表示正在重传该消息。对于QoS 0没有意义。

<a id="a00413022cecf2a624506ab5da630aefa"></a>

### `has_content_type`

```c
bool mqtt_publish_param::has_content_type
```

包含内容类型（Content Type）属性。

<a id="a599f8830ef4b42a68955ad58411ef0f1"></a>

### `has_correlation_data`

```c
bool mqtt_publish_param::has_correlation_data
```

包含关联数据（Correlation Data）属性。

<a id="a85e5a3a9c7347c506780627515dc84ea"></a>

### `has_message_expiry_interval`

```c
bool mqtt_publish_param::has_message_expiry_interval
```

包含消息过期间隔（Message Expiry Interval）属性。

<a id="a4190ccdfbf97a4ef63121e6a841d5f79"></a>

### `has_payload_format_indicator`

```c
bool mqtt_publish_param::has_payload_format_indicator
```

包含载荷格式指示符（Payload Format Indicator）属性。

<a id="aafc5473b88a64df887751903314f0fac"></a>

### `has_response_topic`

```c
bool mqtt_publish_param::has_response_topic
```

包含响应主题（Response Topic）属性。

<a id="aab2664e89f086b62b9af5cd481fccde3"></a>

### `has_subscription_identifier`

```c
bool mqtt_publish_param::has_subscription_identifier
```

包含订阅标识符（Subscription Identifier）属性。

<a id="a36a4d07ed13c5d4befc51a6285606090"></a>

### `has_topic_alias`

```c
bool mqtt_publish_param::has_topic_alias
```

包含主题别名（Topic Alias）属性。

<a id="a5e4b146a69c82fa36fd43adb8658ef5f"></a>

### `has_user_prop`

```c
bool mqtt_publish_param::has_user_prop
```

包含用户属性（User Property）属性。

<a id="a9841a4fbb30b597a9710863ce6034688"></a>

### `message`

```c
struct mqtt_publish_message mqtt_publish_param::message
```

要发布的消息，包括主题（Topic）、服务质量（QoS）及其载荷（如有）。

<a id="a4a486b254bd8e0f081251f8ca087e9d2"></a>

### `message_expiry_interval`

```c
uint32_t mqtt_publish_param::message_expiry_interval
```

MQTT 5.0第3.3.2.3.3节：消息过期间隔（Message Expiry Interval）。

<a id="aac4c6ba605506c183d2d5bdd7e550b3e"></a>

### `message_id`

```c
uint16_t mqtt_publish_param::message_id
```

发布消息所用的消息标识（Message ID）。

对于QoS 0，此项多余。

<a id="a8d9905f31bfc9072516f00082eda9c50"></a>

### `payload_format_indicator`

```c
uint8_t mqtt_publish_param::payload_format_indicator
```

MQTT 5.0第3.3.2.3.2节：载荷格式指示符（Payload Format Indicator）。

<a id="a5e87084f72285ebdf5d26aca0eed6f00"></a>

### `[struct]`

```c
struct { ... } mqtt_publish_param::prop
```

MQTT 5.0属性（Properties）。

<a id="a63e9311cf0acf33386ceb8328b040d2a"></a>

### `response_topic`

```c
struct mqtt_utf8 mqtt_publish_param::response_topic
```

MQTT 5.0第3.3.2.3.5节：响应主题（Response Topic）。

<a id="a9b2c6fad5bf830276d8d3f6b5ab04210"></a>

### `retain_flag`

```c
uint8_t mqtt_publish_param::retain_flag
```

保留标志（Retain Flag）。

1表示消息应由消息代理（Broker）持久保存。

<a id="a9cf950636bfa82b88bd4c3fc562c8f71"></a>

### `[struct]`

```c
struct { ... } mqtt_publish_param::rx
```

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="a5edb680fe44b795b02e35fcb73b98efa"></a>

### `subscription_identifier`

```c
uint32_t mqtt_publish_param::subscription_identifier[CONFIG_MQTT_SUBSCRIPTION_ID_PROPERTIES_MAX]
```

MQTT 5.0第3.3.2.3.8节：订阅标识符（Subscription Identifier）。

<a id="a13bf77403471f79687fe63a93cd1627d"></a>

### `topic_alias`

```c
uint16_t mqtt_publish_param::topic_alias
```

MQTT 5.0第3.3.2.3.4节：主题别名（Topic Alias）。

<a id="a813b18b4c859fb5e703d90fc8eb9bd2e"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_publish_param::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.3.2.3.7节：用户属性（User Property）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_publish_message](P062_mqtt_publish_message_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_mqtt_publish_message_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_mqtt_pubrec_param_结构体.md)
