---
id: learning.zephyr-docs.network-application-model-reference.page-74
title: mqtt_subscription_list_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__subscription__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_mqtt\_subscription\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__subscription__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

订阅/取消订阅消息（Subscribe / Unsubscribe Message）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

订阅/取消订阅消息（Subscribe / Unsubscribe Message）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_a677b9c49972b6d6ade2dd934c8518cc9"></a>

```c
const struct mqtt_topic * list
```

相关声明：[mqtt_topic](P075_mqtt_topic_结构体.md)、[list](#a677b9c49972b6d6ade2dd934c8518cc9)。

包含各主题（Topics）及其服务质量（QoS）的数组。

<a id="r_aa44e0af3526ee0424627bb24a90ea6b1"></a>

```c
uint16_t list_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[list_count](#aa44e0af3526ee0424627bb24a90ea6b1)。

订阅列表（Subscription List）中的主题数量。

<a id="r_a0667dcd4bd5eb5fe1b13b4df1bf2c26f"></a>

```c
uint16_t message_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_id](#a0667dcd4bd5eb5fe1b13b4df1bf2c26f)。

用于标识订阅请求的消息标识（Message ID）。

```c
struct {
```

<a id="r_a57bbc1bbd30931eee635e3032996a0ff"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a9736f9d14db3097c2081e81e765a60ec)。

MQTT 5.0第3.8.2.1.3 / 3.10.2.1.2节：用户属性（User Property）。

<a id="r_a945f57f85204d28669b37bdfa81dcc98"></a>

```c
uint32_t subscription_identifier
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subscription_identifier](#a314f91139b4a837b173a6a930c3bdc6b)。

MQTT 5.0第3.8.2.1.2节：订阅标识符（Subscription Identifier）。

<a id="r_a97fefa83de8657d85b0f76013ca1f222"></a>

```c
} prop
```

相关声明：[prop](#a97fefa83de8657d85b0f76013ca1f222)。

MQTT 5.0属性（Properties）。

## 74.2\_详细说明（Detailed Documentation）

<a id="a677b9c49972b6d6ade2dd934c8518cc9"></a>

### `list`

```c
const struct mqtt_topic* mqtt_subscription_list::list
```

包含各主题（Topics）及其服务质量（QoS）的数组。

<a id="aa44e0af3526ee0424627bb24a90ea6b1"></a>

### `list_count`

```c
uint16_t mqtt_subscription_list::list_count
```

订阅列表（Subscription List）中的主题数量。

<a id="a0667dcd4bd5eb5fe1b13b4df1bf2c26f"></a>

### `message_id`

```c
uint16_t mqtt_subscription_list::message_id
```

用于标识订阅请求的消息标识（Message ID）。

<a id="a97fefa83de8657d85b0f76013ca1f222"></a>

### `[struct]`

```c
struct { ... } mqtt_subscription_list::prop
```

MQTT 5.0属性（Properties）。

<a id="a314f91139b4a837b173a6a930c3bdc6b"></a>

### `subscription_identifier`

```c
uint32_t mqtt_subscription_list::subscription_identifier
```

MQTT 5.0第3.8.2.1.2节：订阅标识符（Subscription Identifier）。

对于UNSUBSCRIBE请求忽略此项。

<a id="a9736f9d14db3097c2081e81e765a60ec"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_subscription_list::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.8.2.1.3 / 3.10.2.1.2节：用户属性（User Property）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_topic](P075_mqtt_topic_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_mqtt_suback_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_mqtt_topic_结构体.md)
