---
id: learning.zephyr-docs.network-application-model-reference.page-42
title: http_resource_detail_websocket_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__websocket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_http\_resource\_detail\_websocket\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__websocket.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WebSocket服务器资源（Server Resource）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

WebSocket服务器资源（Server Resource）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_acd10efe8ca1f82fb6e0557512f18d9ee"></a>

```c
struct http_resource_detail common
```

相关声明：[http_resource_detail](P038_http_resource_detail_结构体.md)、[common](#acd10efe8ca1f82fb6e0557512f18d9ee)。

通用资源详情（Common Resource Details）。

<a id="r_adbfb331ad424fac889f5e53bb1240ed8"></a>

```c
int ws_sock
```

相关声明：[ws_sock](#adbfb331ad424fac889f5e53bb1240ed8)。

WebSocket套接字值。

<a id="r_ad3a18df78d4ab4443bba2fbf00a0cbc0"></a>

```c
http_resource_websocket_cb_t cb
```

相关声明：[http_resource_websocket_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaa51ec52c8960a37566d2ac77d624be93)、[cb](#ad3a18df78d4ab4443bba2fbf00a0cbc0)。

服务器与应用交互所用的资源回调（Resource Callback）。

<a id="r_af9c3292e2d450b70831812cb9d084e3c"></a>

```c
uint8_t * data_buffer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_buffer](#af9c3292e2d450b70831812cb9d084e3c)。

在服务器与应用之间交换数据的数据缓冲区（Data Buffer）。

<a id="r_a512b5da3bdc20eca57c060160c823117"></a>

```c
size_t data_buffer_len
```

相关声明：[data_buffer_len](#a512b5da3bdc20eca57c060160c823117)。

数据缓冲区（Data Buffer）中的数据长度。

<a id="r_a8f6ceaee3ccae18974fbc2c6498737c8"></a>

```c
void * user_data
```

相关声明：[user_data](#a8f6ceaee3ccae18974fbc2c6498737c8)。

指向应用注册的用户数据（User Data）的指针。

## 42.2\_详细说明（Detailed Documentation）

<a id="ad3a18df78d4ab4443bba2fbf00a0cbc0"></a>

### `cb`

```c
http_resource_websocket_cb_t http_resource_detail_websocket::cb
```

服务器与应用交互所用的资源回调（Resource Callback）。

<a id="acd10efe8ca1f82fb6e0557512f18d9ee"></a>

### `common`

```c
struct http_resource_detail http_resource_detail_websocket::common
```

通用资源详情（Common Resource Details）。

<a id="af9c3292e2d450b70831812cb9d084e3c"></a>

### `data_buffer`

```c
uint8_t* http_resource_detail_websocket::data_buffer
```

在服务器与应用之间交换数据的数据缓冲区（Data Buffer）。

<a id="a512b5da3bdc20eca57c060160c823117"></a>

### `data_buffer_len`

```c
size_t http_resource_detail_websocket::data_buffer_len
```

数据缓冲区（Data Buffer）中的数据长度。

<a id="a8f6ceaee3ccae18974fbc2c6498737c8"></a>

### `user_data`

```c
void* http_resource_detail_websocket::user_data
```

指向应用注册的用户数据（User Data）的指针。

<a id="adbfb331ad424fac889f5e53bb1240ed8"></a>

### `ws_sock`

```c
int http_resource_detail_websocket::ws_sock
```

WebSocket套接字值。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_resource_detail](P038_http_resource_detail_结构体.md)
- [http_resource_websocket_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaa51ec52c8960a37566d2ac77d624be93)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_http_resource_detail_static_fs_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_http_response_结构体.md)
