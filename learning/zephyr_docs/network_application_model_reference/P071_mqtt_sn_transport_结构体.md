---
id: learning.zephyr-docs.network-application-model-reference.page-71
title: mqtt_sn_transport_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_mqtt\_sn\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述MQTT-SN传输（Transport）的结构。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

描述MQTT-SN传输（Transport）的结构。MQTT-SN不要求传输可靠，也不要求维持连接，只要求按帧传输。因此，只要采用某种成帧协议（Framing Protocol），就可以使用UDP、ZigBee，甚至简单的UART。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a3486cb5d56fb42db4c1f62ef9a6bb75b"></a>

```c
int(* init )(struct mqtt_sn_transport *transport)
```

相关声明：[init](#a3486cb5d56fb42db4c1f62ef9a6bb75b)、[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)。

在客户端初始化（Client Init）时调用一次，用于初始化传输。

<a id="r_af51e433970bed12b5217c63416d0ec4c"></a>

```c
void(* deinit )(struct mqtt_sn_transport *transport)
```

相关声明：[deinit](#af51e433970bed12b5217c63416d0ec4c)、[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)。

在客户端反初始化（Client Deinit）时调用。

<a id="r_a700e8b1f1d541b90da76f050d492fb7a"></a>

```c
int(* sendto )(struct mqtt_sn_transport *transport, void *buf, size_t sz, const void *dest_addr, size_t addrlen)
```

相关声明：[sendto](#a700e8b1f1d541b90da76f050d492fb7a)、[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)。

库需要发送消息（Message）时调用。

<a id="r_a1a94f8c7facf9997d1bff237ef2f2503"></a>

```c
ssize_t(* recvfrom )(struct mqtt_sn_transport *transport, void *rx_buf, size_t rx_len, void *src_addr, size_t *addrlen)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[recvfrom](#a1a94f8c7facf9997d1bff237ef2f2503)、[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)。

库需要接收消息（Message）时调用。

<a id="r_af6f8c4904857664d14a578a9ead178e4"></a>

```c
int(* poll )(struct mqtt_sn_transport *transport)
```

相关声明：[poll](#af6f8c4904857664d14a578a9ead178e4)、[mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)。

检查是否有可用的传入数据（Incoming Data）。

## 71.2\_详细说明（Detailed Documentation）

<a id="af51e433970bed12b5217c63416d0ec4c"></a>

### `deinit`

```c
void(* mqtt_sn_transport::deinit) (struct mqtt_sn_transport *transport)
```

在客户端反初始化（Client Deinit）时调用。

用于关闭套接字等资源。可为NULL。

<a id="a3486cb5d56fb42db4c1f62ef9a6bb75b"></a>

### `init`

```c
int(* mqtt_sn_transport::init) (struct mqtt_sn_transport *transport)
```

在客户端初始化（Client Init）时调用一次，用于初始化传输。

用于打开套接字等资源。可为NULL。

<a id="af6f8c4904857664d14a578a9ead178e4"></a>

### `poll`

```c
int(* mqtt_sn_transport::poll) (struct mqtt_sn_transport *transport)
```

检查是否有可用的传入数据（Incoming Data）。

poll()返回正数时，recv不得阻塞（Block）。

可为NULL，但此时recv也不应阻塞（Block）。

返回（Returns）：有数据时返回正数，没有数据时返回0；负值表示错误。

<a id="a1a94f8c7facf9997d1bff237ef2f2503"></a>

### `recvfrom`

```c
ssize_t(* mqtt_sn_transport::recvfrom) (struct mqtt_sn_transport *transport, void *rx_buf, size_t rx_len, void *src_addr, size_t *addrlen)
```

库需要接收消息（Message）时调用。

实现应遵循recvfrom的约定（Conventions）。

<a id="a700e8b1f1d541b90da76f050d492fb7a"></a>

### `sendto`

```c
int(* mqtt_sn_transport::sendto) (struct mqtt_sn_transport *transport, void *buf, size_t sz, const void *dest_addr, size_t addrlen)
```

库需要发送消息（Message）时调用。

实现应遵循sendto的约定（Conventions），但有以下例外：dest_addr == NULL时应广播消息，此时addrlen表示广播半径。地址变化时，也应根据需要建立或销毁连接。

返回（Returns）：连接和传输成功时返回ENOERR；负值表示错误。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [mqtt_sn_transport](P071_mqtt_sn_transport_结构体.md)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_mqtt_sn_evt_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_mqtt_sn_will_update_结构体.md)
