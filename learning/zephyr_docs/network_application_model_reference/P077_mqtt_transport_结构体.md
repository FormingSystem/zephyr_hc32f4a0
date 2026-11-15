---
id: learning.zephyr-docs.network-application-model-reference.page-77
title: mqtt_transport_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_mqtt\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MQTT传输专用数据（Transport Specific Data）。

```c
#include <zephyr/net/mqtt.h>
```

<a id="details"></a>

MQTT传输专用数据（Transport Specific Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a47b49927c79e67b202112c68b53d83f4"></a>

```c
enum mqtt_transport_type type
```

相关声明：[mqtt_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaffc2c3078004cf8d24935be086ad63b4)、[type](#a47b49927c79e67b202112c68b53d83f4)。

客户端实例的传输类型选择（Transport Type Selection）。

<a id="r_a7cfdf50105a275612dbda28e7c02808e"></a>

```c
const char * if_name
```

相关声明：[if_name](#a7cfdf50105a275612dbda28e7c02808e)。

MQTT客户端实例应绑定到的接口名称（Interface Name）。

```c
union {
```

```c
struct {
```

<a id="r_adba557c3aa9c3513203905677363e7d6"></a>

```c
int sock
```

相关声明：[sock](#a3b4589dd05394589e7af460761b800bf)。

套接字描述符（Socket Descriptor）。

<a id="r_a07b1258f5add90e67d35a4ee48743fe9"></a>

```c
} tcp
```

相关声明：[tcp](#af65e3f0284ba9d881c5b916749f097b2)。

MQTT使用的TCP套接字传输（TCP Socket Transport）。

<a id="r_a5e496cc21ba5d6088183efd57a9db959"></a>

```c
};
```

使用未加密的TCP或安全的TLS传输（Transport）。

## 77.2\_详细说明（Detailed Documentation）

<a id="a5e496cc21ba5d6088183efd57a9db959"></a>

### `[union]`

```c
union { ... } mqtt_transport
```

使用未加密的TCP或安全的TLS传输（Transport）。

<a id="a7cfdf50105a275612dbda28e7c02808e"></a>

### `if_name`

```c
const char* mqtt_transport::if_name
```

MQTT客户端实例应绑定到的接口名称（Interface Name）。

未指定时保留为NULL。

<a id="a3b4589dd05394589e7af460761b800bf"></a>

### `sock`

```c
int mqtt_transport::sock
```

套接字描述符（Socket Descriptor）。

<a id="af65e3f0284ba9d881c5b916749f097b2"></a>

### `[struct]`

```c
struct { ... } mqtt_transport::tcp
```

MQTT使用的TCP套接字传输（TCP Socket Transport）。

<a id="a47b49927c79e67b202112c68b53d83f4"></a>

### `type`

```c
enum mqtt_transport_type mqtt_transport::type
```

客户端实例的传输类型选择（Transport Type Selection）。

可选值见mqtt_transport_type；MQTT_TRANSPORT_MAX不是有效类型。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [mqtt_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaffc2c3078004cf8d24935be086ad63b4)
- [mqtt_transport](P077_mqtt_transport_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_mqtt_topic_alias_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_mqtt_unsuback_param_结构体.md)
