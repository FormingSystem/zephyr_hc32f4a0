---
id: learning.zephyr-docs.api-file-storage-event-reference.page-24
title: zephyr__net__websocket.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_net\_\_websocket.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WebSocket的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/http/parser.h>
#include <zephyr/net/http/client.h>
```

查看此文件的源码。

WebSocket API，供应用建立 WebSocket 连接（Connections）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

<a id="r_websocket_5Frequest"></a>

```c
struct websocket_request
```

相关声明：[websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)。

WebSocket客户端连接请求（Client Connection Request）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.2\_宏定义（Macros）

<a id="r_ga002ade0e3787b6d9da82ab84af1cd354"></a>

```c
#define WEBSOCKET_FLAG_FINAL 0x00000001
```

相关声明：[WEBSOCKET_FLAG_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga002ade0e3787b6d9da82ab84af1cd354)。

消息类型值（Message Type Values）。

<a id="r_ga9405e69474b48472dfe0b10017dfcd75"></a>

```c
#define WEBSOCKET_FLAG_TEXT 0x00000002
```

相关声明：[WEBSOCKET_FLAG_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga9405e69474b48472dfe0b10017dfcd75)。

文本数据（Textual Data）。

<a id="r_ga8616f88cb194d82da9367f2f48832842"></a>

```c
#define WEBSOCKET_FLAG_BINARY 0x00000004
```

相关声明：[WEBSOCKET_FLAG_BINARY](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga8616f88cb194d82da9367f2f48832842)。

二进制数据（Binary Data）。

<a id="r_gaab5fa480351106751f6482f5056b4238"></a>

```c
#define WEBSOCKET_FLAG_CLOSE 0x00000008
```

相关声明：[WEBSOCKET_FLAG_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaab5fa480351106751f6482f5056b4238)。

关闭连接（Closing Connection）。

<a id="r_ga2f2ea01b18c13f38fe834f855ae0da93"></a>

```c
#define WEBSOCKET_FLAG_PING 0x00000010
```

相关声明：[WEBSOCKET_FLAG_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga2f2ea01b18c13f38fe834f855ae0da93)。

Ping 消息（Message）。

<a id="r_ga68cdf577c5401440095dacf224541047"></a>

```c
#define WEBSOCKET_FLAG_PONG 0x00000020
```

相关声明：[WEBSOCKET_FLAG_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga68cdf577c5401440095dacf224541047)。

Pong 消息（Message）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.3\_类型定义（Typedefs）

<a id="r_gaabfd7aa30ce659214b990eabb0b6d591"></a>

```c
typedef int(* websocket_connect_cb_t) (int ws_sock, struct http_request *req, void *user_data)
```

相关声明：[websocket_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaabfd7aa30ce659214b990eabb0b6d591)、[http_request](../network_application_model_reference/P035_http_request_结构体.md)。

WebSocket 连接建立后调用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.4\_枚举（Enumerations）

<a id="r_ga207402575311103c75906143724e8c35"></a>

```c
enum websocket_opcode { WEBSOCKET_OPCODE_CONTINUE = 0x00 , WEBSOCKET_OPCODE_DATA_TEXT = 0x01 , WEBSOCKET_OPCODE_DATA_BINARY = 0x02 , WEBSOCKET_OPCODE_CLOSE = 0x08 , WEBSOCKET_OPCODE_PING = 0x09 , WEBSOCKET_OPCODE_PONG = 0x0A }
```

相关声明：[websocket_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga207402575311103c75906143724e8c35)、[WEBSOCKET_OPCODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35)、[WEBSOCKET_OPCODE_DATA_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c)、[WEBSOCKET_OPCODE_DATA_BINARY](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69)、[WEBSOCKET_OPCODE_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191)、[WEBSOCKET_OPCODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709)、[WEBSOCKET_OPCODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90)。

WebSocket 选项代码（Option Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.5\_函数（Functions）

<a id="r_ga71a43ec629929d2eb1baba4e3f13a615"></a>

```c
int websocket_connect (int http_sock, struct websocket_request *req, int32_t timeout, void *user_data)
```

相关声明：[websocket_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga71a43ec629929d2eb1baba4e3f13a615)、[websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

连接到提供 WebSocket 服务（Service）的服务器。

<a id="r_gac23c351e5020d0fc9e936933d399b187"></a>

```c
int websocket_send_msg (int ws_sock, const uint8_t *payload, size_t payload_len, enum websocket_opcode opcode, bool mask, bool final, int32_t timeout)
```

相关声明：[websocket_send_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gac23c351e5020d0fc9e936933d399b187)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[websocket_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga207402575311103c75906143724e8c35)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

向对端（Peer）发送 WebSocket 消息。

<a id="r_ga0fb118f84b7631d12c1b742b75593ba6"></a>

```c
int websocket_recv_msg (int ws_sock, uint8_t *buf, size_t buf_len, uint32_t *message_type, uint64_t *remaining, int32_t timeout)
```

相关声明：[websocket_recv_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga0fb118f84b7631d12c1b742b75593ba6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

从对端（Peer）接收 WebSocket 消息。

<a id="r_gacc2f06e2c361317ff48f171abc3d1209"></a>

```c
int websocket_disconnect (int ws_sock)
```

相关声明：[websocket_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gacc2f06e2c361317ff48f171abc3d1209)。

关闭 WebSocket。

<a id="r_gabc2556e62f001f8109bf6ae9f50f3952"></a>

```c
int websocket_register (int http_sock, uint8_t *recv_buf, size_t recv_buf_len)
```

相关声明：[websocket_register](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gabc2556e62f001f8109bf6ae9f50f3952)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将套接字（Socket）注册为 WebSocket。

<a id="r_gaa3131d2599c8c69ab95c55c2e38e28e0"></a>

```c
int websocket_unregister (int ws_sock)
```

相关声明：[websocket_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaa3131d2599c8c69ab95c55c2e38e28e0)。

注销 WebSocket。


## 24.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/http/parser.h](../api_source_http_wifi_reference/P007_parser.h_源码浏览.md)
- [zephyr/net/http/client.h](../api_source_supplement_reference/P088_client.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P916_websocket.h_源码浏览.md)
- [websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)
- [WEBSOCKET_FLAG_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga002ade0e3787b6d9da82ab84af1cd354)
- [WEBSOCKET_FLAG_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga9405e69474b48472dfe0b10017dfcd75)
- [WEBSOCKET_FLAG_BINARY](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga8616f88cb194d82da9367f2f48832842)
- [WEBSOCKET_FLAG_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaab5fa480351106751f6482f5056b4238)
- [WEBSOCKET_FLAG_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga2f2ea01b18c13f38fe834f855ae0da93)
- [WEBSOCKET_FLAG_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga68cdf577c5401440095dacf224541047)
- [websocket_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaabfd7aa30ce659214b990eabb0b6d591)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [websocket_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga207402575311103c75906143724e8c35)
- [WEBSOCKET_OPCODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35)
- [WEBSOCKET_OPCODE_DATA_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c)
- [WEBSOCKET_OPCODE_DATA_BINARY](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69)
- [WEBSOCKET_OPCODE_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191)
- [WEBSOCKET_OPCODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709)
- [WEBSOCKET_OPCODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90)
- [websocket_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga71a43ec629929d2eb1baba4e3f13a615)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [websocket_send_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gac23c351e5020d0fc9e936933d399b187)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [websocket_recv_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga0fb118f84b7631d12c1b742b75593ba6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [websocket_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gacc2f06e2c361317ff48f171abc3d1209)
- [websocket_register](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gabc2556e62f001f8109bf6ae9f50f3952)
- [websocket_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaa3131d2599c8c69ab95c55c2e38e28e0)

<a id="header-details"></a>

---

[上一章](P023_zephyr__drivers__uart_pipe.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__sys__zassert.h_文件参考.md)
