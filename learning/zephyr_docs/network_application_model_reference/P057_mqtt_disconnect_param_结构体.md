---
id: learning.zephyr-docs.network-application-model-reference.page-57
title: mqtt_disconnect_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__disconnect__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_mqtt\_disconnect\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__disconnect__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

断开连接消息（Disconnect Message）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

断开连接消息（Disconnect Message）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_aa1b60dae11e0cad827e2d9942c1137e4"></a>

```c
enum mqtt_disconnect_reason_code reason_code
```

相关声明：[mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)、[reason_code](#aa1b60dae11e0cad827e2d9942c1137e4)。

```c
struct {
```

<a id="r_aef8db15ea81f29f2ac2eaaf57374629c"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a03050c6d4879f0d0eb62093b340bb99c)。

MQTT 5.0第3.14.2.2.4节：用户属性（User Property）。

<a id="r_ad2df27f5da5a42f60e7f609288c2db67"></a>

```c
struct mqtt_utf8 reason_string
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[reason_string](#a7a3b72acdd5a2d239c9e3d78e59bb4c2)。

MQTT 5.0第3.14.2.2.3节：原因字符串（Reason String）。

<a id="r_af0df999a20150918e746a48d168f0b6b"></a>

```c
struct mqtt_utf8 server_reference
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[server_reference](#aa44656e2663a058070a3d30e3bdabee9)。

MQTT 5.0第3.14.2.2.5节：服务器引用（Server Reference）。

<a id="r_afdb4b6e92c6775ca2ebfa14a830492ab"></a>

```c
uint32_t session_expiry_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[session_expiry_interval](#a9a0531c1fb9b95019bb49f1642d54b07)。

MQTT 5.0第3.14.2.2.2节：会话过期间隔（Session Expiry Interval）。

```c
struct {
```

<a id="r_a76929b202f42cb5fc51dc7a43d55a295"></a>

```c
bool has_session_expiry_interval
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_session_expiry_interval](#a2360cc037d244abed416ace079f82257)。

包含会话过期间隔（Session Expiry Interval）属性。

<a id="r_a8c83b18ff8c427ee52510cc5b63f25b6"></a>

```c
bool has_reason_string
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_reason_string](#ae2077e489cf38f4bccfebb78a840b9fe)。

包含原因字符串（Reason String）属性。

<a id="r_a41aba605aaf7915b9a03c869e9a2f69f"></a>

```c
bool has_user_prop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_user_prop](#a02b38f24432c8def5dcda439bc8e9ab7)。

包含用户属性（User Property）属性。

<a id="r_a0a8e335352d984f2d106e62191fe3253"></a>

```c
bool has_server_reference
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_server_reference](#a8891e52deb9c40f4f838f1df67db9794)。

包含服务器引用（Server Reference）属性。

<a id="r_a1e0e657a360a8b1ff48021f40df7e9a2"></a>

```c
} rx
```

相关声明：[rx](#a6fb48a1ddf15d525f13f979758a06132)。

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="r_aa211770e88640378928e3ed3d09c23ac"></a>

```c
} prop
```

相关声明：[prop](#aa211770e88640378928e3ed3d09c23ac)。

MQTT 5.0属性（Properties）。

## 57.2\_详细说明（Detailed Documentation）

<a id="ae2077e489cf38f4bccfebb78a840b9fe"></a>

### `has_reason_string`

```c
bool mqtt_disconnect_param::has_reason_string
```

包含原因字符串（Reason String）属性。

<a id="a8891e52deb9c40f4f838f1df67db9794"></a>

### `has_server_reference`

```c
bool mqtt_disconnect_param::has_server_reference
```

包含服务器引用（Server Reference）属性。

<a id="a2360cc037d244abed416ace079f82257"></a>

### `has_session_expiry_interval`

```c
bool mqtt_disconnect_param::has_session_expiry_interval
```

包含会话过期间隔（Session Expiry Interval）属性。

<a id="a02b38f24432c8def5dcda439bc8e9ab7"></a>

### `has_user_prop`

```c
bool mqtt_disconnect_param::has_user_prop
```

包含用户属性（User Property）属性。

<a id="aa211770e88640378928e3ed3d09c23ac"></a>

### `[struct]`

```c
struct { ... } mqtt_disconnect_param::prop
```

MQTT 5.0属性（Properties）。

<a id="aa1b60dae11e0cad827e2d9942c1137e4"></a>

### `reason_code`

```c
enum mqtt_disconnect_reason_code mqtt_disconnect_param::reason_code
```

<a id="a7a3b72acdd5a2d239c9e3d78e59bb4c2"></a>

### `reason_string`

```c
struct mqtt_utf8 mqtt_disconnect_param::reason_string
```

MQTT 5.0第3.14.2.2.3节：原因字符串（Reason String）。

<a id="a6fb48a1ddf15d525f13f979758a06132"></a>

### `[struct]`

```c
struct { ... } mqtt_disconnect_param::rx
```

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="aa44656e2663a058070a3d30e3bdabee9"></a>

### `server_reference`

```c
struct mqtt_utf8 mqtt_disconnect_param::server_reference
```

MQTT 5.0第3.14.2.2.5节：服务器引用（Server Reference）。

<a id="a9a0531c1fb9b95019bb49f1642d54b07"></a>

### `session_expiry_interval`

```c
uint32_t mqtt_disconnect_param::session_expiry_interval
```

MQTT 5.0第3.14.2.2.2节：会话过期间隔（Session Expiry Interval）。

<a id="a03050c6d4879f0d0eb62093b340bb99c"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_disconnect_param::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.14.2.2.4节：用户属性（User Property）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_mqtt_connack_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_mqtt_evt_结构体.md)
