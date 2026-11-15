---
id: learning.zephyr-docs.network-application-model-reference.page-52
title: mqtt_auth_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__auth__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_mqtt\_auth\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__auth__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

认证消息（Auth Message）的参数。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

认证消息（Auth Message）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_adace77cd3860024ece2252ee41dcd134"></a>

```c
enum mqtt_auth_reason_code reason_code
```

相关声明：[mqtt_auth_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacdbeff0450bbcd438cdf35cd543fc6d6)、[reason_code](#adace77cd3860024ece2252ee41dcd134)。

```c
struct {
```

<a id="r_ac313bc8df41e636a384ef40cc5131456"></a>

```c
struct mqtt_utf8_pair user_prop [CONFIG_MQTT_USER_PROPERTIES_MAX]
```

相关声明：[mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)、[user_prop](#a1ad0e22ec7f3d5d1d304bacad06cb0c6)。

MQTT 5.0第3.15.2.2.5节：用户属性（User Property）。

<a id="r_ad742f5c4dcc01cbd3597775cb199b323"></a>

```c
struct mqtt_utf8 auth_method
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[auth_method](#a5602413c28ceadc87420f8c7a6c53489)。

MQTT 5.0第3.15.2.2.2节：认证方法（Authentication Method）。

<a id="r_a462da9adea001c56a51dbd2e891b055a"></a>

```c
struct mqtt_binstr auth_data
```

相关声明：[mqtt_binstr](P053_mqtt_binstr_结构体.md)、[auth_data](#aaa1aa29efd09cf58aaf79b4e279dc2a9)。

MQTT 5.0第3.15.2.2.3节：认证数据（Authentication Data）。

<a id="r_a45c2f1988e2aada8bd7fe1e4c48c5daf"></a>

```c
struct mqtt_utf8 reason_string
```

相关声明：[mqtt_utf8](P079_mqtt_utf8_结构体.md)、[reason_string](#a500d1b239b9882a1625d5d6035dd3199)。

MQTT 5.0第3.15.2.2.4节：原因字符串（Reason String）。

```c
struct {
```

<a id="r_a8d34624a39ebb9846020fe44f37e6618"></a>

```c
bool has_auth_method
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_auth_method](#a6cf278bec874623fcd97a5c5e7d43940)。

包含认证方法（Authentication Method）属性。

<a id="r_a7f2ec93aa3dc22c60288ed38de52773e"></a>

```c
bool has_auth_data
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_auth_data](#a32bfb124dbaa11a328e7300bc0890cfc)。

包含认证数据（Authentication Data）属性。

<a id="r_afb127d07faf2ed2b77a9f2ef1cfd5f3a"></a>

```c
bool has_reason_string
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_reason_string](#a772343a4f3df425e54c00c43f5fdced4)。

包含原因字符串（Reason String）属性。

<a id="r_a2b60fa5b0b39de406dcb37735f3255d0"></a>

```c
bool has_user_prop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_user_prop](#a50f570175c944f7e0dad4b276c07a6ea)。

包含用户属性（User Property）属性。

<a id="r_a47a215939f96c4741aeabc3ec4206706"></a>

```c
} rx
```

相关声明：[rx](#a9403d927a86f90eb1847840d6f47fe37)。

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="r_a6bd366cb6479370f9db0abaa22e1b803"></a>

```c
} prop
```

相关声明：[prop](#a6bd366cb6479370f9db0abaa22e1b803)。

## 52.2\_详细说明（Detailed Documentation）

<a id="aaa1aa29efd09cf58aaf79b4e279dc2a9"></a>

### `auth_data`

```c
struct mqtt_binstr mqtt_auth_param::auth_data
```

MQTT 5.0第3.15.2.2.3节：认证数据（Authentication Data）。

<a id="a5602413c28ceadc87420f8c7a6c53489"></a>

### `auth_method`

```c
struct mqtt_utf8 mqtt_auth_param::auth_method
```

MQTT 5.0第3.15.2.2.2节：认证方法（Authentication Method）。

<a id="a32bfb124dbaa11a328e7300bc0890cfc"></a>

### `has_auth_data`

```c
bool mqtt_auth_param::has_auth_data
```

包含认证数据（Authentication Data）属性。

<a id="a6cf278bec874623fcd97a5c5e7d43940"></a>

### `has_auth_method`

```c
bool mqtt_auth_param::has_auth_method
```

包含认证方法（Authentication Method）属性。

<a id="a772343a4f3df425e54c00c43f5fdced4"></a>

### `has_reason_string`

```c
bool mqtt_auth_param::has_reason_string
```

包含原因字符串（Reason String）属性。

<a id="a50f570175c944f7e0dad4b276c07a6ea"></a>

### `has_user_prop`

```c
bool mqtt_auth_param::has_user_prop
```

包含用户属性（User Property）属性。

<a id="a6bd366cb6479370f9db0abaa22e1b803"></a>

### `[struct]`

```c
struct { ... } mqtt_auth_param::prop
```

<a id="adace77cd3860024ece2252ee41dcd134"></a>

### `reason_code`

```c
enum mqtt_auth_reason_code mqtt_auth_param::reason_code
```

<a id="a500d1b239b9882a1625d5d6035dd3199"></a>

### `reason_string`

```c
struct mqtt_utf8 mqtt_auth_param::reason_string
```

MQTT 5.0第3.15.2.2.4节：原因字符串（Reason String）。

<a id="a9403d927a86f90eb1847840d6f47fe37"></a>

### `[struct]`

```c
struct { ... } mqtt_auth_param::rx
```

指示收到的数据包是否包含给定属性（Property）的标志。

<a id="a1ad0e22ec7f3d5d1d304bacad06cb0c6"></a>

### `user_prop`

```c
struct mqtt_utf8_pair mqtt_auth_param::user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX]
```

MQTT 5.0第3.15.2.2.5节：用户属性（User Property）。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_auth_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacdbeff0450bbcd438cdf35cd543fc6d6)
- [mqtt_utf8_pair](P080_mqtt_utf8_pair_结构体.md)
- [mqtt_utf8](P079_mqtt_utf8_结构体.md)
- [mqtt_binstr](P053_mqtt_binstr_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_lwm2m_time_series_elem_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_mqtt_binstr_结构体.md)
