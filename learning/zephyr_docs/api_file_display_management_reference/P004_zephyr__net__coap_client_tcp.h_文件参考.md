---
id: learning.zephyr-docs.api-file-display-management-reference.page-4
title: zephyr__net__coap_client_tcp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_coap\_client\_tcp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP TCP客户端（Client）的API。

<a id="details"></a>

```c
#include <zephyr/net/coap.h>
#include <zephyr/net/coap_client.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

受限应用协议（CoAP）TCP 客户端 API。供应用按照 RFC 8323，通过可靠传输（Reliable Transports）TCP／TLS 发送 CoAP 请求。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_gacb66929e0d233cf9623845ca9803f34b"></a>

```c
#define MAX_COAP_TCP_MSG_LEN
```

相关声明：[MAX_COAP_TCP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gacb66929e0d233cf9623845ca9803f34b)。

CoAP TCP 消息的最大大小（Maximum Message Size）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_gaabd183897d2d59a23fca6848e463a400"></a>

```c
typedef void(* coap_client_tcp_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

相关声明：[coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)、[coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)。

CoAP TCP 请求回调（Request Callback）。

<a id="r_gad97f2afc8f4fec4b8b13eb73707ef953"></a>

```c
typedef int(* coap_client_tcp_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

相关声明：[coap_client_tcp_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad97f2afc8f4fec4b8b13eb73707ef953)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

用于提供 CoAP TCP 请求有效载荷（Payload）的回调。

<a id="r_ga8a4ec2cb48137f477ae5e3adc352dec7"></a>

```c
typedef int(* coap_client_tcp_socket_config_cb_t) (int fd, void *user_data)
```

相关声明：[coap_client_tcp_socket_config_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga8a4ec2cb48137f477ae5e3adc352dec7)。

在连接之前配置套接字（Socket）的回调。

<a id="r_ga04927f52d6f7495c635d0ced1515c3ca"></a>

```c
typedef void(* coap_client_tcp_event_cb_t) (struct coap_client_tcp *client, enum coap_client_tcp_event event, const union coap_client_tcp_event_data *data, void *user_data)
```

相关声明：[coap_client_tcp_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga04927f52d6f7495c635d0ced1515c3ca)、[coap_client_tcp_event](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gab8b714180fd3bfa728e25abe09a9a8a1)、[coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)。

CoAP TCP 信令事件（Signaling Events）回调，涵盖 Release／Abort。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_gab8b714180fd3bfa728e25abe09a9a8a1"></a>

```c
enum coap_client_tcp_event { COAP_CLIENT_TCP_EVENT_CSM_UPDATED , COAP_CLIENT_TCP_EVENT_PONG_RECEIVED , COAP_CLIENT_TCP_EVENT_RELEASE , COAP_CLIENT_TCP_EVENT_ABORT }
```

相关声明：[coap_client_tcp_event](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gab8b714180fd3bfa728e25abe09a9a8a1)、[COAP_CLIENT_TCP_EVENT_CSM_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5)、[COAP_CLIENT_TCP_EVENT_PONG_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f)、[COAP_CLIENT_TCP_EVENT_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a)、[COAP_CLIENT_TCP_EVENT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590)。

CoAP TCP 客户端信令事件类型（Event Types for Signaling）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_gaeb9a69c7b6b91cfa26d63eeb561451c8"></a>

```c
int coap_client_tcp_init (struct coap_client_tcp *client, const char *info)
```

相关声明：[coap_client_tcp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaeb9a69c7b6b91cfa26d63eeb561451c8)。

初始化 TCP CoAP 客户端（Client）。

<a id="r_gabc8c1782e586f61a4ba196576279baad"></a>

```c
int coap_client_tcp_connect (struct coap_client_tcp *client, const struct net_sockaddr *addr, net_socklen_t addrlen, int proto)
```

相关声明：[coap_client_tcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gabc8c1782e586f61a4ba196576279baad)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将 CoAP TCP 客户端连接到服务器（Server）。

<a id="r_ga84b766361341c2494aa127cc0ee1578c"></a>

```c
int coap_client_tcp_close (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga84b766361341c2494aa127cc0ee1578c)。

关闭 CoAP TCP 客户端连接（Connection）。

<a id="r_gaaac96d77cd1ee8abeb137717bd076b3e"></a>

```c
int coap_client_tcp_req (struct coap_client_tcp *client, struct coap_client_tcp_request *req)
```

相关声明：[coap_client_tcp_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaaac96d77cd1ee8abeb137717bd076b3e)、[coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)。

通过 TCP 发送 CoAP 请求（Request）。

<a id="r_ga856f370559bb93b84b66238ce3a031eb"></a>

```c
int coap_client_tcp_csm_req (struct coap_client_tcp *client, uint32_t max_block_size, coap_client_tcp_response_cb_t cb, void *user_data)
```

相关声明：[coap_client_tcp_csm_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga856f370559bb93b84b66238ce3a031eb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)。

通过 TCP 发送能力与设置消息（Capabilities and Settings Message，CSM）。

<a id="r_ga5a2cdabf25ccd37aa3e2db8aa60d5058"></a>

```c
void coap_client_tcp_cancel_requests (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga5a2cdabf25ccd37aa3e2db8aa60d5058)。

取消当前所有 TCP 请求（Requests）。

<a id="r_ga0008f54568fe1ea489f052aa98c7cd2c"></a>

```c
void coap_client_tcp_cancel_and_reset_all (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_cancel_and_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0008f54568fe1ea489f052aa98c7cd2c)。

更换套接字（Socket）时取消并完全重置所有请求。

<a id="r_ga0857b3d8ccb249e46e636765b0570c8c"></a>

```c
struct coap_client_tcp_option coap_client_tcp_option_initial_block2 (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)、[coap_client_tcp_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0857b3d8ccb249e46e636765b0570c8c)。

获取 TCP 的初始 Block2 选项，并考虑 BERT 机制（BERT-aware）。

<a id="r_ga3e35576e92b53b22faf458c859339d41"></a>

```c
bool coap_client_tcp_has_ongoing_exchange (struct coap_client_tcp *client)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_client_tcp_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga3e35576e92b53b22faf458c859339d41)。

检查 TCP 客户端是否存在正在进行的交换（Exchange）。

<a id="r_gad10b972ab7a50a05afae900551f870d0"></a>

```c
int coap_client_tcp_ping (struct coap_client_tcp *client)
```

相关声明：[coap_client_tcp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad10b972ab7a50a05afae900551f870d0)。

向服务器发送 Ping 信令（Signal），遵循 RFC 8323。

<a id="r_ga37c2721b11b48b887ab3d6d6374a635a"></a>

```c
int coap_client_tcp_release (struct coap_client_tcp *client, const char *alt_addr, uint32_t hold_off_sec)
```

相关声明：[coap_client_tcp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga37c2721b11b48b887ab3d6d6374a635a)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向服务器发送 Release 信令（Signal），遵循 RFC 8323。

<a id="r_gad7246717e5e1ae1f8664f7fb3c6d1a26"></a>

```c
void coap_client_tcp_set_event_cb (struct coap_client_tcp *client, coap_client_tcp_event_cb_t cb, void *user_data)
```

相关声明：[coap_client_tcp_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad7246717e5e1ae1f8664f7fb3c6d1a26)、[coap_client_tcp_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga04927f52d6f7495c635d0ced1515c3ca)。

设置信令事件（Signaling Events）Release／Abort 的回调。


## 4.6\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](../api_source_transport_clock_reference/P006_coap.h_源码浏览.md)
- [zephyr/net/coap_client.h](../api_source_system_reference/P006_coap_client.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P004_coap_client_tcp.h_源码浏览.md)
- [coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)
- [coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)
- [coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)
- [MAX_COAP_TCP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gacb66929e0d233cf9623845ca9803f34b)
- [coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)
- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [coap_client_tcp_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad97f2afc8f4fec4b8b13eb73707ef953)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [coap_client_tcp_socket_config_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga8a4ec2cb48137f477ae5e3adc352dec7)
- [coap_client_tcp_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga04927f52d6f7495c635d0ced1515c3ca)
- [coap_client_tcp_event](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gab8b714180fd3bfa728e25abe09a9a8a1)
- [COAP_CLIENT_TCP_EVENT_CSM_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5)
- [COAP_CLIENT_TCP_EVENT_PONG_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f)
- [COAP_CLIENT_TCP_EVENT_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a)
- [COAP_CLIENT_TCP_EVENT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590)
- [coap_client_tcp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaeb9a69c7b6b91cfa26d63eeb561451c8)
- [coap_client_tcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gabc8c1782e586f61a4ba196576279baad)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_client_tcp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga84b766361341c2494aa127cc0ee1578c)
- [coap_client_tcp_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaaac96d77cd1ee8abeb137717bd076b3e)
- [coap_client_tcp_csm_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga856f370559bb93b84b66238ce3a031eb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [coap_client_tcp_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga5a2cdabf25ccd37aa3e2db8aa60d5058)
- [coap_client_tcp_cancel_and_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0008f54568fe1ea489f052aa98c7cd2c)
- [coap_client_tcp_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0857b3d8ccb249e46e636765b0570c8c)
- [coap_client_tcp_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga3e35576e92b53b22faf458c859339d41)
- [coap_client_tcp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad10b972ab7a50a05afae900551f870d0)
- [RFC 8323](https://datatracker.ietf.org/doc/html/rfc8323)
- [coap_client_tcp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga37c2721b11b48b887ab3d6d6374a635a)
- [coap_client_tcp_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad7246717e5e1ae1f8664f7fb3c6d1a26)

<a id="header-details"></a>

---

[上一章](P003_zephyr__bluetooth__buf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__data.h_文件参考.md)
