---
id: learning.zephyr-docs.network-application-model-reference.page-26
title: http_client_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__client__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_http\_client\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__client__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接到服务器的HTTP客户端（Client）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

连接到服务器的HTTP客户端（Client）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_aca2c3fae568ad984d90646e6b543b959"></a>

```c
size_t content_len
```

相关声明：[content_len](#aca2c3fae568ad984d90646e6b543b959)。

请求内容长度（Request Content Length）。

<a id="r_ab0695811450793361bc88ca0bb582c15"></a>

```c
enum http_method method
```

相关声明：[http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)、[method](#ab0695811450793361bc88ca0bb582c15)。

请求方法（Request Method）。

<a id="r_aaaa95f16bde409fab692fc193a692169"></a>

```c
bool is_h3: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_h3](#aaaa95f16bde409fab692fc193a692169)。

表示此客户端是HTTP/3客户端（QUIC流）的标志。

<a id="r_aab71d232273c8bb6374b44d15614a7e1"></a>

```c
bool preface_sent: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[preface_sent](#aab71d232273c8bb6374b44d15614a7e1)。

表示HTTP/2连接前言（Preface）已发送的标志。

<a id="r_ac805cda657ee679d5ccbf80fcc6007b2"></a>

```c
bool http1_headers_sent: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[http1_headers_sent](#ac805cda657ee679d5ccbf80fcc6007b2)。

表示HTTP/1头部（Headers）已发送的标志。

<a id="r_ae8fe0bf1dd0e5015b077a01f01fa40e9"></a>

```c
bool has_upgrade_header: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_upgrade_header](#ae8fe0bf1dd0e5015b077a01f01fa40e9)。

表示请求中包含升级头部（Upgrade Header）的标志。

<a id="r_afcc28f111655bab47516d2e71468bc55"></a>

```c
bool http2_upgrade: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[http2_upgrade](#afcc28f111655bab47516d2e71468bc55)。

表示正在进行HTTP/2升级（Upgrade）的标志。

<a id="r_ae20c4d4038a643bef49dbb77b497e7b1"></a>

```c
bool websocket_upgrade: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[websocket_upgrade](#ae20c4d4038a643bef49dbb77b497e7b1)。

表示正在进行WebSocket升级（Upgrade）的标志。

## 26.2\_详细说明（Detailed Documentation）

<a id="aca2c3fae568ad984d90646e6b543b959"></a>

### `content_len`

```c
size_t http_client_ctx::content_len
```

请求内容长度（Request Content Length）。

<a id="ae8fe0bf1dd0e5015b077a01f01fa40e9"></a>

### `has_upgrade_header`

```c
bool http_client_ctx::has_upgrade_header
```

表示请求中包含升级头部（Upgrade Header）的标志。

<a id="ac805cda657ee679d5ccbf80fcc6007b2"></a>

### `http1_headers_sent`

```c
bool http_client_ctx::http1_headers_sent
```

表示HTTP/1头部（Headers）已发送的标志。

<a id="afcc28f111655bab47516d2e71468bc55"></a>

### `http2_upgrade`

```c
bool http_client_ctx::http2_upgrade
```

表示正在进行HTTP/2升级（Upgrade）的标志。

<a id="aaaa95f16bde409fab692fc193a692169"></a>

### `is_h3`

```c
bool http_client_ctx::is_h3
```

表示此客户端是HTTP/3客户端（QUIC流）的标志。

<a id="ab0695811450793361bc88ca0bb582c15"></a>

### `method`

```c
enum http_method http_client_ctx::method
```

请求方法（Request Method）。

<a id="aab71d232273c8bb6374b44d15614a7e1"></a>

### `preface_sent`

```c
bool http_client_ctx::preface_sent
```

表示HTTP/2连接前言（Preface）已发送的标志。

<a id="ae20c4d4038a643bef49dbb77b497e7b1"></a>

### `websocket_upgrade`

```c
bool http_client_ctx::websocket_upgrade
```

表示正在进行WebSocket升级（Upgrade）的标志。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_dns_sd_rec_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_http_client_internal_data_结构体.md)
