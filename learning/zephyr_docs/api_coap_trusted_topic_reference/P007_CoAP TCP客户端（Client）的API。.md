---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-7
title: CoAP TCP客户端（Client）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_CoAP TCP客户端（Client）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP TCP客户端（Client）的API。

<a id="details"></a>

CoAP TCP客户端（Client）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_coap_5Fclient_5Ftcp_5Fevent_5Fdata"></a>

```c
union coap_client_tcp_event_data
```

相关声明：[coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)。

CoAP TCP信令事件（Signaling Events）的事件数据。

<a id="r_coap_5Fclient_5Ftcp_5Foption"></a>

```c
struct coap_client_tcp_option
```

相关声明：[coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)。

CoAP TCP客户端请求的附加选项（Extra Options）的表示。

<a id="r_coap_5Fclient_5Ftcp_5Frequest"></a>

```c
struct coap_client_tcp_request
```

相关声明：[coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)。

CoAP TCP客户端请求（Client Request）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gacb66929e0d233cf9623845ca9803f34b"></a>

```c
#define MAX_COAP_TCP_MSG_LEN
```

相关声明：[MAX_COAP_TCP_MSG_LEN](#gacb66929e0d233cf9623845ca9803f34b)。

CoAP TCP 消息的最大大小（Maximum Message Size）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_gaabd183897d2d59a23fca6848e463a400"></a>

```c
typedef void(* coap_client_tcp_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

相关声明：[coap_client_tcp_response_cb_t](#gaabd183897d2d59a23fca6848e463a400)、[coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)。

CoAP TCP 请求回调（Request Callback）。

<a id="r_gad97f2afc8f4fec4b8b13eb73707ef953"></a>

```c
typedef int(* coap_client_tcp_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

相关声明：[coap_client_tcp_payload_cb_t](#gad97f2afc8f4fec4b8b13eb73707ef953)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于提供 CoAP TCP 请求有效载荷（Payload）的回调。

<a id="r_ga8a4ec2cb48137f477ae5e3adc352dec7"></a>

```c
typedef int(* coap_client_tcp_socket_config_cb_t) (int fd, void *user_data)
```

相关声明：[coap_client_tcp_socket_config_cb_t](#ga8a4ec2cb48137f477ae5e3adc352dec7)。

在连接之前配置套接字（Socket）的回调。

<a id="r_ga04927f52d6f7495c635d0ced1515c3ca"></a>

```c
typedef void(* coap_client_tcp_event_cb_t) (struct coap_client_tcp *client, enum coap_client_tcp_event event, const union coap_client_tcp_event_data *data, void *user_data)
```

相关声明：[coap_client_tcp_event_cb_t](#ga04927f52d6f7495c635d0ced1515c3ca)、[coap_client_tcp_event](#gab8b714180fd3bfa728e25abe09a9a8a1)、[coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)。

CoAP TCP 信令事件（Signaling Events）回调，涵盖 Release／Abort。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_gab8b714180fd3bfa728e25abe09a9a8a1"></a>

```c
enum coap_client_tcp_event { COAP_CLIENT_TCP_EVENT_CSM_UPDATED , COAP_CLIENT_TCP_EVENT_PONG_RECEIVED , COAP_CLIENT_TCP_EVENT_RELEASE , COAP_CLIENT_TCP_EVENT_ABORT }
```

相关声明：[coap_client_tcp_event](#gab8b714180fd3bfa728e25abe09a9a8a1)、[COAP_CLIENT_TCP_EVENT_CSM_UPDATED](#ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5)、[COAP_CLIENT_TCP_EVENT_PONG_RECEIVED](#ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f)、[COAP_CLIENT_TCP_EVENT_RELEASE](#ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a)、[COAP_CLIENT_TCP_EVENT_ABORT](#ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590)。

CoAP TCP 客户端信令事件类型（Event Types for Signaling）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gaeb9a69c7b6b91cfa26d63eeb561451c8"></a>

```c
int coap_client_tcp_init (struct coap_client_tcp *client, const char *info)
```

相关声明：[coap_client_tcp_init](#gaeb9a69c7b6b91cfa26d63eeb561451c8)。

初始化 TCP CoAP 客户端（Client）。

<a id="r_gabc8c1782e586f61a4ba196576279baad"></a>

```c
int coap_client_tcp_connect (struct coap_client_tcp *client, const struct net_sockaddr *addr, net_socklen_t addrlen, int proto)
```

相关声明：[coap_client_tcp_connect](#gabc8c1782e586f61a4ba196576279baad)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将 CoAP TCP 客户端连接到服务器（Server）。

<a id="r_ga84b766361341c2494aa127cc0ee1578c"></a>

```c
int coap_client_tcp_close (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_close](#ga84b766361341c2494aa127cc0ee1578c)。

关闭 CoAP TCP 客户端连接（Connection）。

<a id="r_gaaac96d77cd1ee8abeb137717bd076b3e"></a>

```c
int coap_client_tcp_req (struct coap_client_tcp *client, struct coap_client_tcp_request *req)
```

相关声明：[coap_client_tcp_req](#gaaac96d77cd1ee8abeb137717bd076b3e)、[coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)。

通过 TCP 发送 CoAP 请求（Request）。

<a id="r_ga856f370559bb93b84b66238ce3a031eb"></a>

```c
int coap_client_tcp_csm_req (struct coap_client_tcp *client, uint32_t max_block_size, coap_client_tcp_response_cb_t cb, void *user_data)
```

相关声明：[coap_client_tcp_csm_req](#ga856f370559bb93b84b66238ce3a031eb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[coap_client_tcp_response_cb_t](#gaabd183897d2d59a23fca6848e463a400)。

通过 TCP 发送能力与设置消息（Capabilities and Settings Message，CSM）。

<a id="r_ga5a2cdabf25ccd37aa3e2db8aa60d5058"></a>

```c
void coap_client_tcp_cancel_requests (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_cancel_requests](#ga5a2cdabf25ccd37aa3e2db8aa60d5058)。

取消当前所有 TCP 请求（Requests）。

<a id="r_ga0008f54568fe1ea489f052aa98c7cd2c"></a>

```c
void coap_client_tcp_cancel_and_reset_all (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_cancel_and_reset_all](#ga0008f54568fe1ea489f052aa98c7cd2c)。

更换套接字（Socket）时取消并完全重置所有请求。

<a id="r_ga0857b3d8ccb249e46e636765b0570c8c"></a>

```c
struct coap_client_tcp_option coap_client_tcp_option_initial_block2 (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)、[coap_client_tcp_option_initial_block2](#ga0857b3d8ccb249e46e636765b0570c8c)。

获取 TCP 的初始 Block2 选项，并考虑 BERT 机制（BERT-aware）。

<a id="r_ga3e35576e92b53b22faf458c859339d41"></a>

```c
bool coap_client_tcp_has_ongoing_exchange (struct coap_client_tcp *client)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_client_tcp_has_ongoing_exchange](#ga3e35576e92b53b22faf458c859339d41)。

检查 TCP 客户端是否存在正在进行的交换（Exchange）。

<a id="r_gad10b972ab7a50a05afae900551f870d0"></a>

```c
int coap_client_tcp_ping (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_ping](#gad10b972ab7a50a05afae900551f870d0)。

向服务器发送 Ping 信令（Signal），遵循 RFC 8323。

<a id="r_ga37c2721b11b48b887ab3d6d6374a635a"></a>

```c
int coap_client_tcp_release (struct coap_client_tcp *client, const char *alt_addr, uint32_t hold_off_sec)
```

相关声明：[coap_client_tcp_release](#ga37c2721b11b48b887ab3d6d6374a635a)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向服务器发送 Release 信令（Signal），遵循 RFC 8323。

<a id="r_gad7246717e5e1ae1f8664f7fb3c6d1a26"></a>

```c
void coap_client_tcp_set_event_cb (struct coap_client_tcp *client, coap_client_tcp_event_cb_t cb, void *user_data)
```

相关声明：[coap_client_tcp_set_event_cb](#gad7246717e5e1ae1f8664f7fb3c6d1a26)、[coap_client_tcp_event_cb_t](#ga04927f52d6f7495c635d0ced1515c3ca)。

设置信令事件（Signaling Events）Release／Abort 的回调。

## 7.6\_详细说明（Detailed Documentation）

<a id="gacb66929e0d233cf9623845ca9803f34b"></a>

### `MAX_COAP_TCP_MSG_LEN`

```c
#define MAX_COAP_TCP_MSG_LEN
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

展开值（Value）：

```c
(CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE + \
CONFIG_COAP_CLIENT_MESSAGE_SIZE)
```

CoAP TCP 消息的最大大小（Maximum Message Size）。

<a id="ga04927f52d6f7495c635d0ced1515c3ca"></a>

### `coap_client_tcp_event_cb_t`

```c
typedef void(* coap_client_tcp_event_cb_t) (struct coap_client_tcp *client, enum coap_client_tcp_event event, const union coap_client_tcp_event_data *data, void *user_data)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

CoAP TCP 信令事件（Signaling Events）回调，涵盖 Release／Abort。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 收到事件的客户端实例（Client Instance）。 |
| `event` | 信令事件类型（Signaling Event Type）。 |
| `data` | 事件特定数据（Event-specific Data），某些事件可以为 NULL。 |
| `user_data` | 用户提供的上下文（Context）。 |

<a id="gad97f2afc8f4fec4b8b13eb73707ef953"></a>

### `coap_client_tcp_payload_cb_t`

```c
typedef int(* coap_client_tcp_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

用于提供 CoAP TCP 请求有效载荷（Payload）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `offset` | 载荷相对于分块传输（Blockwise Transfer）起点的偏移量。 |
| `payload` | 指向包含负载块（Payload Block）的缓冲区的指针。 |
| `len` | 输入时为请求的最大块大小（Block Size）；输出时为实际负载长度（Payload Length）。 |
| `last_block` | 指向标志的指针，该标志表示是否预期还有更多负载块（Payload Blocks）。 |
| `user_data` | 用户提供的上下文（Context）。 |

返回（Returns）：成功时为 0；返回负错误码可中止上传（Abort Upload）。

<a id="gaabd183897d2d59a23fca6848e463a400"></a>

### `coap_client_tcp_response_cb_t`

```c
typedef void(* coap_client_tcp_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

CoAP TCP 请求回调（Request Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | CoAP 响应数据（Response Data）。 |
| `user_data` | 用户提供的上下文（Context）。 |

<a id="ga8a4ec2cb48137f477ae5e3adc352dec7"></a>

### `coap_client_tcp_socket_config_cb_t`

```c
typedef int(* coap_client_tcp_socket_config_cb_t) (int fd, void *user_data)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

在连接之前配置套接字（Socket）的回调。

在创建套接字（Socket）之后、连接（Connect）之前调用，使应用可以设置套接字选项，例如 TLS 凭据（Credentials）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 套接字文件描述符（Socket File Descriptor）。 |
| `user_data` | 用户提供的上下文（Context）。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="gab8b714180fd3bfa728e25abe09a9a8a1"></a>

### `coap_client_tcp_event`

```c
enum coap_client_tcp_event
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

CoAP TCP 客户端信令事件类型（Event Types for Signaling）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COAP_CLIENT_TCP_EVENT_CSM_UPDATED` | 已根据服务器更新能力与设置消息（CSM）中的能力信息。 |
| `COAP_CLIENT_TCP_EVENT_PONG_RECEIVED` | 收到响应 Ping 的 Pong。 |
| `COAP_CLIENT_TCP_EVENT_RELEASE` | 服务器发起连接释放（Connection Release），参见 RFC 8323。 |
| `COAP_CLIENT_TCP_EVENT_ABORT` | 服务器中止连接（Abort Connection），参见 RFC 8323。 |

<a id="ga0008f54568fe1ea489f052aa98c7cd2c"></a>

### `coap_client_tcp_cancel_and_reset_all()`

```c
void coap_client_tcp_cancel_and_reset_all ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

更换套接字（Socket）时取消并完全重置所有请求。

在拆除传输连接（Transport）时使用，确保新套接字具有干净的初始状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |

<a id="ga5a2cdabf25ccd37aa3e2db8aa60d5058"></a>

### `coap_client_tcp_cancel_requests()`

```c
void coap_client_tcp_cancel_requests ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

取消当前所有 TCP 请求（Requests）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |

<a id="ga84b766361341c2494aa127cc0ee1578c"></a>

### `coap_client_tcp_close()`

```c
int coap_client_tcp_close ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

关闭 CoAP TCP 客户端连接（Connection）。

取消所有正在进行的请求并关闭底层套接字（Underlying Socket）。如需优雅关闭（Graceful Shutdown），应先通过 coap_client_tcp_release 发送 Release 信号，再调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="gabc8c1782e586f61a4ba196576279baad"></a>

### `coap_client_tcp_connect()`

```c
int coap_client_tcp_connect ( struct coap_client_tcp * client, const struct net_sockaddr * addr, net_socklen_t addrlen, int proto )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

将 CoAP TCP 客户端连接到服务器（Server）。

与 UDP 客户端不同，TCP 客户端在内部管理套接字（Socket）。此函数创建 TCP 套接字、连接到服务器，并自动发送能力与设置消息（Capabilities and Settings Message，CSM），按照 RFC 8323 协商能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |
| `addr` | 服务器的目标地址（Destination Address）。 |
| `addrlen` | 地址结构体的长度（Address Structure Length）。 |
| `proto` | 要使用的协议（Protocol），为 IPPROTO_TCP 或 IPPROTO_TLS_1_2。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="ga856f370559bb93b84b66238ce3a031eb"></a>

### `coap_client_tcp_csm_req()`

```c
int coap_client_tcp_csm_req ( struct coap_client_tcp * client, uint32_t max_block_size, coap_client_tcp_response_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

通过 TCP 发送能力与设置消息（Capabilities and Settings Message，CSM）。

按照 RFC 8323，建立 TCP 上的 CoAP 连接（CoAP-over-TCP）时应交换能力与设置消息（CSM），以协商最大消息大小和 BERT 等能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance），必须已通过 coap_client_tcp_connect 连接。 |
| `max_block_size` | 要通告的最大块大小（Maximum Block Size）。 |
| `cb` | 响应回调（Response Callback），由于服务器可能不响应，因此可以为 NULL。 |
| `user_data` | 传给回调的用户数据（User Data）。 |

返回（Returns）：成功时为 0；未连接时为 -ENOTCONN；其他情况为负错误码。

<a id="ga3e35576e92b53b22faf458c859339d41"></a>

### `coap_client_tcp_has_ongoing_exchange()`

```c
bool coap_client_tcp_has_ongoing_exchange ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

检查 TCP 客户端是否存在正在进行的交换（Exchange）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向 CoAP TCP 客户端实例（Client Instance）的指针。 |

返回（Returns）：存在正在进行的交换（Exchange）时为 true，否则为 false。

<a id="gaeb9a69c7b6b91cfa26d63eeb561451c8"></a>

### `coap_client_tcp_init()`

```c
int coap_client_tcp_init ( struct coap_client_tcp * client, const char * info )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

初始化 TCP CoAP 客户端（Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 客户端实例（Client Instance）。 |
| `[in] info` | 接收线程（Receiving Thread）名称，使用默认名称时传入 NULL。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="ga0857b3d8ccb249e46e636765b0570c8c"></a>

### `coap_client_tcp_option_initial_block2()`

```c
struct coap_client_tcp_option coap_client_tcp_option_initial_block2 ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

获取 TCP 的初始 Block2 选项，并考虑 BERT 机制（BERT-aware）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |

返回（Returns）：CoAP 客户端的初始 Block2 选项结构体（Option Structure）。

<a id="gad10b972ab7a50a05afae900551f870d0"></a>

### `coap_client_tcp_ping()`

```c
int coap_client_tcp_ping ( struct coap_client_tcp * client)
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

向服务器发送 Ping 信令（Signal），遵循 RFC 8323。

发送 Ping 信号并等待 Pong 响应，可用于连接保活（Keep-alive）或往返时间（RTT）测量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance），必须已连接。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="ga37c2721b11b48b887ab3d6d6374a635a"></a>

### `coap_client_tcp_release()`

```c
int coap_client_tcp_release ( struct coap_client_tcp * client, const char * alt_addr, uint32_t hold_off_sec )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

向服务器发送 Release 信令（Signal），遵循 RFC 8323。

发出优雅终止连接（Graceful Connection Termination）的信号。服务器应在关闭之前完成待处理请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance），必须已连接。 |
| `alt_addr` | 建议的替代地址（Alternative Address），没有时为 NULL。 |
| `hold_off_sec` | 等待时间（Hold-off Time），单位为秒，没有时为 0。 |

返回（Returns）：成功时为 0，否则为负错误码。

<a id="gaaac96d77cd1ee8abeb137717bd076b3e"></a>

### `coap_client_tcp_req()`

```c
int coap_client_tcp_req ( struct coap_client_tcp * client, struct coap_client_tcp_request * req )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

通过 TCP 发送 CoAP 请求（Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance），必须已通过 coap_client_tcp_connect 连接。 |
| `req` | CoAP 请求结构体（Request Structure）。 |

返回（Returns）：成功时为 0；未连接时为 -ENOTCONN；其他情况为负错误码。

<a id="gad7246717e5e1ae1f8664f7fb3c6d1a26"></a>

### `coap_client_tcp_set_event_cb()`

```c
void coap_client_tcp_set_event_cb ( struct coap_client_tcp * client, coap_client_tcp_event_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/coap_client_tcp.h>
```

设置信令事件（Signaling Events）Release／Abort 的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |
| `cb` | 发生事件时调用的回调函数（Callback Function）。 |
| `user_data` | 传给回调的用户数据。 |


## 7.7\_原页交叉引用（Cross References）

- [coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)
- [coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)
- [coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)
- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [RFC 8323](https://datatracker.ietf.org/doc/html/rfc8323)
- [zephyr/net/coap_client_tcp.h](../api_file_display_management_reference/P004_zephyr__net__coap_client_tcp.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5"></a>
<a id="ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f"></a>
<a id="ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a"></a>
<a id="ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_CoAP客户端（Client）的API。.md) · [返回大纲](大纲.md) · [下一章](P008_CoAP 服务 API.md)
