---
id: learning.zephyr-docs.network-service-model-reference.page-61
title: ssh_server_event_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_ssh\_server\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__server__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH服务器事件（Server Event）。

```c
#include <zephyr/net/ssh/server.h>
```

<a id="details"></a>

SSH 服务器事件。表示 SSH 服务器中可能发生的不同事件，例如客户端连接和断开。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_aa74854d6e2e6e05a5749ea65adb3eb22"></a>

```c
enum ssh_server_event_type type
```

相关声明：[ssh_server_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga38729e64c5c13a3df058fba5481f56cd)、[type](#aa74854d6e2e6e05a5749ea65adb3eb22)。

事件类型。

```c
union {
```

<a id="r_afd223f9b120152110d2d8f34a0e0c444"></a>

```c
struct ssh_server_event_client_connected client_connected
```

相关声明：[ssh_server_event_client_connected](P062_ssh_server_event_client_connected_结构体.md)、[client_connected](#a12c0b1ecce7fb8d50a771c47907909e3)。

客户端连接事件的专用数据。

<a id="r_ae2541735976acbfa7546d2a74d8c4709"></a>

```c
struct ssh_server_event_client_disconnected client_disconnected
```

相关声明：[ssh_server_event_client_disconnected](P063_ssh_server_event_client_disconnected_结构体.md)、[client_disconnected](#aff11456412dd9833beec1bdc610db868)。

客户端断开事件的专用数据。

<a id="r_a0d792dc4518961a9d31af9f65f202f61"></a>

```c
};
```

事件数据（Event Data）。

## 61.2\_详细说明（Detailed Documentation）

<a id="a0d792dc4518961a9d31af9f65f202f61"></a>

### `[union]`

```c
union { ... } ssh_server_event
```

事件数据（Event Data）。

<a id="a12c0b1ecce7fb8d50a771c47907909e3"></a>

### `client_connected`

```c
struct ssh_server_event_client_connected ssh_server_event::client_connected
```

客户端连接事件的专用数据。

<a id="aff11456412dd9833beec1bdc610db868"></a>

### `client_disconnected`

```c
struct ssh_server_event_client_disconnected ssh_server_event::client_disconnected
```

客户端断开事件的专用数据。

<a id="aa74854d6e2e6e05a5749ea65adb3eb22"></a>

### `type`

```c
enum ssh_server_event_type ssh_server_event::type
```

事件类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/server.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html)
- [ssh_server_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__server.html#ga38729e64c5c13a3df058fba5481f56cd)
- [ssh_server_event_client_connected](P062_ssh_server_event_client_connected_结构体.md)
- [ssh_server_event_client_disconnected](P063_ssh_server_event_client_disconnected_结构体.md)
- [ssh_server_event](P061_ssh_server_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_ssh_channel_event_channel_request_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_ssh_server_event_client_connected_结构体.md)
