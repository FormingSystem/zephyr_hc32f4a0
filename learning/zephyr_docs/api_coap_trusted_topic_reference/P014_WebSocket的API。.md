---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-14
title: WebSocket的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_WebSocket的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WebSocket的API。

<a id="details"></a>

WebSocket API。自 1.12 起提供（Since 1.12），版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_websocket_5Frequest"></a>

```c
struct websocket_request
```

相关声明：[websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)。

WebSocket客户端连接请求（Client Connection Request）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga002ade0e3787b6d9da82ab84af1cd354"></a>

```c
#define WEBSOCKET_FLAG_FINAL 0x00000001
```

相关声明：[WEBSOCKET_FLAG_FINAL](#ga002ade0e3787b6d9da82ab84af1cd354)。

消息类型值（Message Type Values）。

<a id="r_ga9405e69474b48472dfe0b10017dfcd75"></a>

```c
#define WEBSOCKET_FLAG_TEXT 0x00000002
```

相关声明：[WEBSOCKET_FLAG_TEXT](#ga9405e69474b48472dfe0b10017dfcd75)。

文本数据（Textual Data）。

<a id="r_ga8616f88cb194d82da9367f2f48832842"></a>

```c
#define WEBSOCKET_FLAG_BINARY 0x00000004
```

相关声明：[WEBSOCKET_FLAG_BINARY](#ga8616f88cb194d82da9367f2f48832842)。

二进制数据（Binary Data）。

<a id="r_gaab5fa480351106751f6482f5056b4238"></a>

```c
#define WEBSOCKET_FLAG_CLOSE 0x00000008
```

相关声明：[WEBSOCKET_FLAG_CLOSE](#gaab5fa480351106751f6482f5056b4238)。

关闭连接（Closing Connection）。

<a id="r_ga2f2ea01b18c13f38fe834f855ae0da93"></a>

```c
#define WEBSOCKET_FLAG_PING 0x00000010
```

相关声明：[WEBSOCKET_FLAG_PING](#ga2f2ea01b18c13f38fe834f855ae0da93)。

Ping 消息（Message）。

<a id="r_ga68cdf577c5401440095dacf224541047"></a>

```c
#define WEBSOCKET_FLAG_PONG 0x00000020
```

相关声明：[WEBSOCKET_FLAG_PONG](#ga68cdf577c5401440095dacf224541047)。

Pong 消息（Message）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.3\_类型定义（Typedefs）

<a id="r_gaabfd7aa30ce659214b990eabb0b6d591"></a>

```c
typedef int(* websocket_connect_cb_t) (int ws_sock, struct http_request *req, void *user_data)
```

相关声明：[websocket_connect_cb_t](#gaabfd7aa30ce659214b990eabb0b6d591)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

WebSocket 连接建立后调用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.4\_枚举（Enumerations）

<a id="r_ga207402575311103c75906143724e8c35"></a>

```c
enum websocket_opcode { WEBSOCKET_OPCODE_CONTINUE = 0x00 , WEBSOCKET_OPCODE_DATA_TEXT = 0x01 , WEBSOCKET_OPCODE_DATA_BINARY = 0x02 , WEBSOCKET_OPCODE_CLOSE = 0x08 , WEBSOCKET_OPCODE_PING = 0x09 , WEBSOCKET_OPCODE_PONG = 0x0A }
```

相关声明：[websocket_opcode](#ga207402575311103c75906143724e8c35)、[WEBSOCKET_OPCODE_CONTINUE](#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35)、[WEBSOCKET_OPCODE_DATA_TEXT](#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c)、[WEBSOCKET_OPCODE_DATA_BINARY](#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69)、[WEBSOCKET_OPCODE_CLOSE](#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191)、[WEBSOCKET_OPCODE_PING](#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709)、[WEBSOCKET_OPCODE_PONG](#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90)。

WebSocket 选项代码（Option Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.5\_函数（Functions）

<a id="r_ga71a43ec629929d2eb1baba4e3f13a615"></a>

```c
int websocket_connect (int http_sock, struct websocket_request *req, int32_t timeout, void *user_data)
```

相关声明：[websocket_connect](#ga71a43ec629929d2eb1baba4e3f13a615)、[websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

连接到提供 WebSocket 服务（Service）的服务器。

<a id="r_gac23c351e5020d0fc9e936933d399b187"></a>

```c
int websocket_send_msg (int ws_sock, const uint8_t *payload, size_t payload_len, enum websocket_opcode opcode, bool mask, bool final, int32_t timeout)
```

相关声明：[websocket_send_msg](#gac23c351e5020d0fc9e936933d399b187)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[websocket_opcode](#ga207402575311103c75906143724e8c35)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

向对端（Peer）发送 WebSocket 消息。

<a id="r_ga0fb118f84b7631d12c1b742b75593ba6"></a>

```c
int websocket_recv_msg (int ws_sock, uint8_t *buf, size_t buf_len, uint32_t *message_type, uint64_t *remaining, int32_t timeout)
```

相关声明：[websocket_recv_msg](#ga0fb118f84b7631d12c1b742b75593ba6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

从对端（Peer）接收 WebSocket 消息。

<a id="r_gacc2f06e2c361317ff48f171abc3d1209"></a>

```c
int websocket_disconnect (int ws_sock)
```

相关声明：[websocket_disconnect](#gacc2f06e2c361317ff48f171abc3d1209)。

关闭 WebSocket。

<a id="r_gabc2556e62f001f8109bf6ae9f50f3952"></a>

```c
int websocket_register (int http_sock, uint8_t *recv_buf, size_t recv_buf_len)
```

相关声明：[websocket_register](#gabc2556e62f001f8109bf6ae9f50f3952)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将套接字（Socket）注册为 WebSocket。

<a id="r_gaa3131d2599c8c69ab95c55c2e38e28e0"></a>

```c
int websocket_unregister (int ws_sock)
```

相关声明：[websocket_unregister](#gaa3131d2599c8c69ab95c55c2e38e28e0)。

注销 WebSocket。

## 14.6\_详细说明（Detailed Documentation）

<a id="ga8616f88cb194d82da9367f2f48832842"></a>

### `WEBSOCKET_FLAG_BINARY`

```c
#define WEBSOCKET_FLAG_BINARY 0x00000004
```

```c
#include <zephyr/net/websocket.h>
```

二进制数据（Binary Data）。

<a id="gaab5fa480351106751f6482f5056b4238"></a>

### `WEBSOCKET_FLAG_CLOSE`

```c
#define WEBSOCKET_FLAG_CLOSE 0x00000008
```

```c
#include <zephyr/net/websocket.h>
```

关闭连接（Closing Connection）。

<a id="ga002ade0e3787b6d9da82ab84af1cd354"></a>

### `WEBSOCKET_FLAG_FINAL`

```c
#define WEBSOCKET_FLAG_FINAL 0x00000001
```

```c
#include <zephyr/net/websocket.h>
```

消息类型值（Message Type Values）。

在 websocket_recv_msg() 中返回：最终帧（Final Frame）。

<a id="ga2f2ea01b18c13f38fe834f855ae0da93"></a>

### `WEBSOCKET_FLAG_PING`

```c
#define WEBSOCKET_FLAG_PING 0x00000010
```

```c
#include <zephyr/net/websocket.h>
```

Ping 消息（Message）。

<a id="ga68cdf577c5401440095dacf224541047"></a>

### `WEBSOCKET_FLAG_PONG`

```c
#define WEBSOCKET_FLAG_PONG 0x00000020
```

```c
#include <zephyr/net/websocket.h>
```

Pong 消息（Message）。

<a id="ga9405e69474b48472dfe0b10017dfcd75"></a>

### `WEBSOCKET_FLAG_TEXT`

```c
#define WEBSOCKET_FLAG_TEXT 0x00000002
```

```c
#include <zephyr/net/websocket.h>
```

文本数据（Textual Data）。

<a id="gaabfd7aa30ce659214b990eabb0b6d591"></a>

### `websocket_connect_cb_t`

```c
typedef int(* websocket_connect_cb_t) (int ws_sock, struct http_request *req, void *user_data)
```

```c
#include <zephyr/net/websocket.h>
```

WebSocket 连接建立后调用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_sock` | WebSocket 标识符（ID）。 |
| `req` | HTTP 握手请求（Handshake Request）。 |
| `user_data` | 指向某些用户数据（User Data）的有效指针，或 NULL。 |

返回（Returns）：正常时为 0；出错且应中止连接时小于 0。

<a id="ga207402575311103c75906143724e8c35"></a>

### `websocket_opcode`

```c
enum websocket_opcode
```

```c
#include <zephyr/net/websocket.h>
```

WebSocket 选项代码（Option Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WEBSOCKET_OPCODE_CONTINUE` | 消息继续（Message Continues）。 |
| `WEBSOCKET_OPCODE_DATA_TEXT` | 文本数据（Textual Data）。 |
| `WEBSOCKET_OPCODE_DATA_BINARY` | 二进制数据（Binary Data）。 |
| `WEBSOCKET_OPCODE_CLOSE` | 关闭连接（Closing Connection）。 |
| `WEBSOCKET_OPCODE_PING` | Ping 消息（Message）。 |
| `WEBSOCKET_OPCODE_PONG` | Pong 消息（Message）。 |

<a id="ga71a43ec629929d2eb1baba4e3f13a615"></a>

### `websocket_connect()`

```c
int websocket_connect ( int http_sock, struct websocket_request * req, int32_t timeout, void * user_data )
```

```c
#include <zephyr/net/websocket.h>
```

连接到提供 WebSocket 服务（Service）的服务器。

连接建立后调用回调。返回值为新的套接字描述符（Socket Descriptor），可通过 BSD 套接字 API 使用它发送／接收数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `http_sock` | 连接服务器的套接字标识符（Socket ID）。此套接字用于 HTTP 握手等操作，实际 WebSocket 通信使用返回的 WebSocket 标识符。此函数返回后不得关闭 http_sock，因为它用于向 WebSocket 服务器传送 WebSocket 数据包。 |
| `req` | WebSocket 请求（Request）。用户应分配并填写请求数据。 |
| `timeout` | 等待连接的最大超时（Timeout），单位为毫秒；SYS_FOREVER_MS 表示无限等待。 |
| `user_data` | 传递给回调（Callback）的用户指定数据（User-specified Data）。 |

返回（Returns）：发送／接收 WebSocket 数据时使用的 WebSocket 标识符（ID）。

<a id="gacc2f06e2c361317ff48f171abc3d1209"></a>

### `websocket_disconnect()`

```c
int websocket_disconnect ( int ws_sock)
```

```c
#include <zephyr/net/websocket.h>
```

关闭 WebSocket。

调用此函数后，必须调用 websocket_connect() 才能重新建立连接（Re-establish Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_sock` | websocket_connect() 返回的 WebSocket 标识符（ID）。 |

返回（Returns）：出错时小于 0；连接成功关闭时为 0。

<a id="ga0fb118f84b7631d12c1b742b75593ba6"></a>

### `websocket_recv_msg()`

```c
int websocket_recv_msg ( int ws_sock, uint8_t * buf, size_t buf_len, uint32_t * message_type, uint64_t * remaining, int32_t timeout )
```

```c
#include <zephyr/net/websocket.h>
```

从对端（Peer）接收 WebSocket 消息。

此函数会自动从消息中移除 WebSocket 头部（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_sock` | websocket_connect() 返回的 WebSocket 标识符（ID）。 |
| `buf` | 用于读入 WebSocket 数据的缓冲区（Buffer）。 |
| `buf_len` | 数据缓冲区长度（Data Buffer Length）。 |
| `message_type` | 消息类型。 |
| `remaining` | 此次读取后消息中还剩多少数据。 |
| `timeout` | 尝试接收消息的时长，单位为毫秒；SYS_FOREVER_MS 表示无限等待。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `>=0` | 收到的字节数量（Bytes Received）。 |
| `-EAGAIN` | 超时（Timeout）时。 |
| `-ENOTCONN` | 套接字关闭（Socket Close）时。 |
| `-errno` | 失败时为其他负 errno 值。 |

<a id="gabc2556e62f001f8109bf6ae9f50f3952"></a>

### `websocket_register()`

```c
int websocket_register ( int http_sock, uint8_t * recv_buf, size_t recv_buf_len )
```

```c
#include <zephyr/net/websocket.h>
```

将套接字（Socket）注册为 WebSocket。

连接升级（Upgrade）为 WebSocket 连接时，由 HTTP 服务器调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `http_sock` | 底层套接字连接（Underlying Socket Connection）的套接字。 |
| `recv_buf` | 用于 WebSocket 解析（Parsing）的临时接收缓冲区。它必须指向一块在整个 WebSocket 会话（Session）期间均有效的内存区域。 |
| `recv_buf_len` | 临时接收缓冲区长度（Temporary Receive Buffer Length）。 |

返回（Returns）：出错时小于 0；大于或等于 0 时，为应用应使用的实际 WebSocket 标识符。

<a id="gac23c351e5020d0fc9e936933d399b187"></a>

### `websocket_send_msg()`

```c
int websocket_send_msg ( int ws_sock, const uint8_t * payload, size_t payload_len, enum websocket_opcode opcode, bool mask, bool final, int32_t timeout )
```

```c
#include <zephyr/net/websocket.h>
```

向对端（Peer）发送 WebSocket 消息。

此函数会自动向消息添加 WebSocket 头部（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_sock` | websocket_connect() 返回的 WebSocket 标识符（ID）。 |
| `payload` | 要发送的 WebSocket 数据。 |
| `payload_len` | 待发送数据的长度（Data Length）。 |
| `opcode` | 操作码（Operation Code）：text、binary、ping、pong 或 close。 |
| `mask` | 对数据应用掩码（Mask）；详情参见 RFC 6455。 |
| `final` | 是否为此次消息发送中的最后一部分。final == false 时，第一部分必须具有有效操作码（Opcode），后续部分必须使用 WEBSOCKET_OPCODE_CONTINUE。final == true 且这是唯一一部分时，opcode 应设置为适当的操作码，即 text 或 binary。 |
| `timeout` | 尝试发送消息的时长，单位为毫秒；SYS_FOREVER_MS 表示无限等待。 |

返回（Returns）：出错时小于 0；大于或等于 0 时，为已发送的字节数。

<a id="gaa3131d2599c8c69ab95c55c2e38e28e0"></a>

### `websocket_unregister()`

```c
int websocket_unregister ( int ws_sock)
```

```c
#include <zephyr/net/websocket.h>
```

注销 WebSocket。

不再需要底层“真实”套接字（Underlying "Real" Socket）时调用。它先关闭 WebSocket，再关闭原始套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws_sock` | WebSocket 连接套接字（Connection Socket）。 |

返回（Returns）：出错时小于 0；为 0 时，WebSocket 连接已完全关闭。


## 14.7\_原页交叉引用（Cross References）

- [websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [zephyr/net/websocket.h](../api_file_storage_event_reference/P024_zephyr__net__websocket.h_文件参考.md)
- [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35"></a>
<a id="gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c"></a>
<a id="gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69"></a>
<a id="gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191"></a>
<a id="gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709"></a>
<a id="gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_视频驱动（Video Drivers）.md) · [返回大纲](大纲.md) · [下一章](P015_Xen Dom0 域控制（Domain control）.md)
