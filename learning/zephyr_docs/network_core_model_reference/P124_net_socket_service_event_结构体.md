---
id: learning.zephyr-docs.network-core-model-reference.page-124
title: net_socket_service_event_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__socket__service__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_net\_socket\_service\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__socket__service__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

该结构包含由哪个套接字（Socket）触发回调函数调用的信息。

```c
#include <zephyr/net/socket_service.h>
```

<a id="details"></a>

该结构包含由哪个套接字（Socket）触发回调函数调用的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 124.1\_数据成员（Data Fields）

<a id="r_a82695b0eaa7c563033fce4afde33cab9"></a>

```c
net_socket_service_handler_t callback
```

相关声明：[net_socket_service_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga5d9495470c1ade51791df56c59cfb1f5)、[callback](#a82695b0eaa7c563033fce4afde33cab9)。

发生所关注的套接字活动（Socket activity）时调用的回调。

<a id="r_a8246a87e2171474eb214bb8f909cb9bf"></a>

```c
struct zsock_pollfd event
```

相关声明：[zsock_pollfd](https://docs.zephyrproject.org/latest/doxygen/html/structzsock__pollfd.html)、[event](#a8246a87e2171474eb214bb8f909cb9bf)。

触发此事件的套接字信息（Socket information）。

<a id="r_aa11bb43a2cc48d167bf8995d860fd638"></a>

```c
void * user_data
```

相关声明：[user_data](#aa11bb43a2cc48d167bf8995d860fd638)。

用户数据（User Data）。

<a id="r_a7052fad6a65c5a1b610a69e16fc72785"></a>

```c
struct net_socket_service_desc * svc
```

相关声明：[net_socket_service_desc](P123_net_socket_service_desc_结构体.md)、[svc](#a7052fad6a65c5a1b610a69e16fc72785)。

服务反向指针（Service back pointer）。

## 124.2\_详细说明（Detailed Documentation）

<a id="a82695b0eaa7c563033fce4afde33cab9"></a>

### `callback`

```c
net_socket_service_handler_t net_socket_service_event::callback
```

发生所关注的套接字活动（Socket activity）时调用的回调。

<a id="a8246a87e2171474eb214bb8f909cb9bf"></a>

### `event`

```c
struct zsock_pollfd net_socket_service_event::event
```

触发此事件的套接字信息（Socket information）。

<a id="a7052fad6a65c5a1b610a69e16fc72785"></a>

### `svc`

```c
struct net_socket_service_desc* net_socket_service_event::svc
```

服务反向指针（Service back pointer）。

<a id="aa11bb43a2cc48d167bf8995d860fd638"></a>

### `user_data`

```c
void* net_socket_service_event::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/socket_service.h`

## 124.3\_原页交叉引用（Cross References）

- [zephyr/net/socket_service.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h_source.html)
- [net_socket_service_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga5d9495470c1ade51791df56c59cfb1f5)
- [zsock_pollfd](https://docs.zephyrproject.org/latest/doxygen/html/structzsock__pollfd.html)
- [net_socket_service_desc](P123_net_socket_service_desc_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P123_net_socket_service_desc_结构体.md) · [返回大纲](大纲.md) · [下一章](P125_net_stats_结构体.md)
