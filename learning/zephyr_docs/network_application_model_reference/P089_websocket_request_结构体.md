---
id: learning.zephyr-docs.network-application-model-reference.page-89
title: websocket_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwebsocket__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_websocket\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwebsocket__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WebSocket客户端连接请求（Client Connection Request）。

```c
#include <zephyr/net/websocket.h>
```

<a id="details"></a>

WebSocket客户端连接请求（Client Connection Request），包含发起WebSocket连接请求所需的全部数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_a8769d50f1a6168dc6518f2dd0c74b62a"></a>

```c
const char * host
```

相关声明：[host](#a8769d50f1a6168dc6518f2dd0c74b62a)。

执行HTTP握手（Handshake）时使用的WebSocket服务器主机名。

<a id="r_a49ef6c2f4201beeb3af8992ded2bd4a3"></a>

```c
const char * url
```

相关声明：[url](#a49ef6c2f4201beeb3af8992ded2bd4a3)。

WebSocket的URL。

<a id="r_ab7a281fff2a27a52f7ec346643f55b71"></a>

```c
http_header_cb_t optional_headers_cb
```

相关声明：[http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)、[optional_headers_cb](#ab7a281fff2a27a52f7ec346643f55b71)。

用户提供的回调函数（Callback Function），在需要发送可选头部时调用。

<a id="r_a4cea74d6094325b218b6bbed4005b912"></a>

```c
const char ** optional_headers
```

相关声明：[optional_headers](#a4cea74d6094325b218b6bbed4005b912)。

以NULL终止的列表，包含应添加到HTTP请求的可选头部（Optional Headers）。

<a id="r_a96936b68fec07f077d9e9569ef1411d1"></a>

```c
websocket_connect_cb_t cb
```

相关声明：[websocket_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaabfd7aa30ce659214b990eabb0b6d591)、[cb](#a96936b68fec07f077d9e9569ef1411d1)。

用户提供的回调函数（Callback Function），在连接建立时调用。

<a id="r_a38315d0c37bdc8cfe22cdbc6d2c8af4a"></a>

```c
const struct http_parser_settings * http_cb
```

相关声明：[http_parser_settings](P033_http_parser_settings_结构体.md)、[http_cb](#a38315d0c37bdc8cfe22cdbc6d2c8af4a)。

用户提供的回调函数列表；调用方应用可借此了解握手期间的解析状态或HTTP字段。

<a id="r_a939ed8e980af4bc98f30d1bad835a2d2"></a>

```c
uint8_t * tmp_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tmp_buf](#a939ed8e980af4bc98f30d1bad835a2d2)。

用户提供的缓冲区（Buffer），用于存储HTTP连接数据。

<a id="r_a09bb3c708b51d8f86de244b3fc4a9f57"></a>

```c
size_t tmp_buf_len
```

相关声明：[tmp_buf_len](#a09bb3c708b51d8f86de244b3fc4a9f57)。

用户提供的临时缓冲区（Temporary Buffer）的长度。

## 89.2\_详细说明（Detailed Documentation）

<a id="a96936b68fec07f077d9e9569ef1411d1"></a>

### `cb`

```c
websocket_connect_cb_t websocket_request::cb
```

用户提供的回调函数（Callback Function），在连接建立时调用。

<a id="a8769d50f1a6168dc6518f2dd0c74b62a"></a>

### `host`

```c
const char* websocket_request::host
```

执行HTTP握手（Handshake）时使用的WebSocket服务器主机名。

<a id="a38315d0c37bdc8cfe22cdbc6d2c8af4a"></a>

### `http_cb`

```c
const struct http_parser_settings* websocket_request::http_cb
```

用户提供的回调函数列表；调用方应用可借此了解握手期间的解析状态或HTTP字段。

此参数可选，通常不需要；但调用方希望了解服务器发送的字段时很有用。

<a id="a4cea74d6094325b218b6bbed4005b912"></a>

### `optional_headers`

```c
const char** websocket_request::optional_headers
```

以NULL终止的列表，包含应添加到HTTP请求的可选头部（Optional Headers）。

可为NULL。指定optional_headers_cb后会忽略此字段。

<a id="ab7a281fff2a27a52f7ec346643f55b71"></a>

### `optional_headers_cb`

```c
http_header_cb_t websocket_request::optional_headers_cb
```

用户提供的回调函数（Callback Function），在需要发送可选头部时调用。

可为NULL，此时使用http_request中的optional_headers字段。optional_headers回调（Callback）使用户能够发送比实际可分配内存容量更多的HTTP头部数据。

<a id="a939ed8e980af4bc98f30d1bad835a2d2"></a>

### `tmp_buf`

```c
uint8_t* websocket_request::tmp_buf
```

用户提供的缓冲区（Buffer），用于存储HTTP连接数据。

<a id="a09bb3c708b51d8f86de244b3fc4a9f57"></a>

### `tmp_buf_len`

```c
size_t websocket_request::tmp_buf_len
```

用户提供的临时缓冲区（Temporary Buffer）的长度。

<a id="a49ef6c2f4201beeb3af8992ded2bd4a3"></a>

### `url`

```c
const char* websocket_request::url
```

WebSocket的URL。

本数据类型文档由以下文件生成：

- `zephyr/net/websocket.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/net/websocket.h](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h_source.html)
- [http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)
- [websocket_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaabfd7aa30ce659214b990eabb0b6d591)
- [http_parser_settings](P033_http_parser_settings_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [http_request](P035_http_request_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_sntp_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_coap_client_tcp_event_data_联合体.md)
