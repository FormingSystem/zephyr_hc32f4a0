---
id: learning.zephyr-docs.network-application-model-reference.page-55
title: mqtt_common_ack_properties_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__common__ack__properties.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_mqtt\_common\_ack\_properties\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__common__ack__properties.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

所有确认类型消息（ACK-Type Messages）共享的通用MQTT 5.0属性。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

所有确认类型消息（ACK-Type Messages）共享的通用MQTT 5.0属性。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_aa827f37cfc537e00e8ff4e774ec9b835"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#aa827f37cfc537e00e8ff4e774ec9b835)。

MQTT 5.0第3.4.2.2.3节：用户属性（User Property）。

<a id="r_a282e39c4e3bdcebf331969fdf0a60570"></a>

```c
struct mqtt_utf8 reason_string
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[reason_string](#a282e39c4e3bdcebf331969fdf0a60570)。

MQTT 5.0第3.4.2.2.2节：原因字符串（Reason String）。

```c
struct {
```

<a id="r_a40e69c669b35345c15d7ae96a381e040"></a>

```c
bool has_reason_string
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_reason_string](#abf672bc44df434fe2dd4f519343d6480)。

包含原因字符串（Reason String）属性。

<a id="r_a84c835bcf8cdfb50e669b4bba02e0e94"></a>

```c
bool has_user_prop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_user_prop](#a69d6a6795e309cb64bff1dd3eeb698c6)。

包含用户属性（User Property）属性。

<a id="r_a87c543e4eb14b9e1e1fbd9fe7d4b047b"></a>

```c
} rx
```

相关声明：[rx](#a87c543e4eb14b9e1e1fbd9fe7d4b047b)。

指示收到的数据包是否包含给定属性（Property）的标志。

## 55.2\_详细说明（Detailed Documentation）

<a id="abf672bc44df434fe2dd4f519343d6480"></a>

### `has_reason_string`

```c
bool mqtt_common_ack_properties::has_reason_string
```

包含原因字符串（Reason String）属性。

<a id="a69d6a6795e309cb64bff1dd3eeb698c6"></a>

### `has_user_prop`

```c
bool mqtt_common_ack_properties::has_user_prop
```

包含用户属性（User Property）属性。

<a id="a282e39c4e3bdcebf331969fdf0a60570"></a>

### `reason_string`

```c
struct mqtt_utf8 mqtt_common_ack_properties::reason_string
```

MQTT 5.0第3.4.2.2.2节：原因字符串（Reason String）。

<a id="a87c543e4eb14b9e1e1fbd9fe7d4b047b"></a>

### `[struct]`

```c
struct { ... } mqtt_common_ack_properties::rx
```

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="aa827f37cfc537e00e8ff4e774ec9b835"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_common_ack_properties::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.4.2.2.3节：用户属性（User Property）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_mqtt_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_mqtt_connack_param_结构体.md)
