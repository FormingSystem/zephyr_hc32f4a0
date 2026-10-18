---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-9
title: 互联网控制消息协议（ICMP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_互联网控制消息协议（ICMP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送和接收 IPv4 或 IPv6 的互联网控制消息协议（Internet Control Message Protocol，ICMP）回显请求消息（Echo Request）。

<a id="details"></a>

发送和接收 IPv4 或 IPv6 的网际控制消息协议回送请求（Internet Control Message Protocol Echo Request，ICMP Echo Request）消息。引入版本（Since）：3.5；API 版本（Version）：0.8.0。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_icmp_2Eh"></a>

```c
file icmp.h
```

相关声明：[icmp.h](../api_file_protocol_service_reference/P020_zephyr__net__icmp.h_文件参考.md)。

互联网控制消息协议（ICMP）支持功能的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_net_5Ficmp_5Fctx"></a>

```c
struct net_icmp_ctx
```

相关声明：[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)。

互联网控制消息协议（ICMP）的上下文结构。

<a id="r_net_5Ficmp_5Fip_5Fhdr"></a>

```c
struct net_icmp_ip_hdr
```

相关声明：[net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)。

表示ICMP响应消息中IPv4或IPv6头部（Header）的结构。

<a id="r_net_5Ficmp_5Fping_5Fparams"></a>

```c
struct net_icmp_ping_params
```

相关声明：[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

表示发送回显请求（Echo-Request，ping）消息时所需参数的结构。

<a id="r_net_5Ficmp_5Foffload"></a>

```c
struct net_icmp_offload
```

相关声明：[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)。

互联网控制消息协议（ICMP）的卸载上下文（Offload Context）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.3\_宏定义（Macros）

<a id="r_gab09cfc243ae8aea120c2da9e77b3154f"></a>

```c
#define NET_ICMPV4_ECHO_REQUEST 8
```

相关声明：[NET_ICMPV4_ECHO_REQUEST](#gab09cfc243ae8aea120c2da9e77b3154f)。

ICMPv4 回显请求（Echo-Request）。

<a id="r_ga34b93cc7084276868f2b635021aad53b"></a>

```c
#define NET_ICMPV4_ECHO_REPLY 0
```

相关声明：[NET_ICMPV4_ECHO_REPLY](#ga34b93cc7084276868f2b635021aad53b)。

ICMPv4 回显应答（Echo-Reply）。

<a id="r_ga30ba68bc2372c6253ebce3db452591b3"></a>

```c
#define NET_ICMPV6_ECHO_REQUEST 128
```

相关声明：[NET_ICMPV6_ECHO_REQUEST](#ga30ba68bc2372c6253ebce3db452591b3)。

ICMPv6 回显请求（Echo-Request）。

<a id="r_ga88187908775c5b84ec183f645454ac76"></a>

```c
#define NET_ICMPV6_ECHO_REPLY 129
```

相关声明：[NET_ICMPV6_ECHO_REPLY](#ga88187908775c5b84ec183f645454ac76)。

ICMPv6 回显应答（Echo-Reply）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.4\_类型定义（Typedefs）

<a id="r_ga35da387f482e5da0c944bbfa349c3ea2"></a>

```c
typedef enum net_verdict(* net_icmp_handler_t) (struct net_icmp_ctx *ctx, struct net_pkt *pkt, struct net_icmp_ip_hdr *ip_hdr, struct net_icmp_hdr *icmp_hdr, void *user_data)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_icmp_handler_t](#ga35da387f482e5da0c944bbfa349c3ea2)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)。

收到 ICMP 响应（Response）时调用的处理函数。

<a id="r_gad85b780080117bf3b53c5623f962ea71"></a>

```c
typedef int(* net_icmp_offload_ping_handler_t) (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_offload_ping_handler_t](#gad85b780080117bf3b53c5623f962ea71)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga897d79bdeddb0890d4ef66f51d9505a7"></a>

```c
int net_icmp_init_ctx (struct net_icmp_ctx *ctx, uint8_t family, uint8_t type, uint8_t code, net_icmp_handler_t handler)
```

相关声明：[net_icmp_init_ctx](#ga897d79bdeddb0890d4ef66f51d9505a7)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_icmp_handler_t](#ga35da387f482e5da0c944bbfa349c3ea2)。

初始化 ICMP 上下文结构体（Context Structure）。

<a id="r_gab90fe71303498c127f1f093d78d16ffa"></a>

```c
int net_icmp_cleanup_ctx (struct net_icmp_ctx *ctx)
```

相关声明：[net_icmp_cleanup_ctx](#gab90fe71303498c127f1f093d78d16ffa)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)。

清理 ICMP 上下文结构体（Context Structure）。

<a id="r_ga588b1eecda05d5c275328fee4711b46b"></a>

```c
int net_icmp_send_echo_request (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_send_echo_request](#ga588b1eecda05d5c275328fee4711b46b)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

发送 ICMP 回显请求消息（Echo Request Message）。

<a id="r_ga4a1b59fac1b8934a8d0b8f1b981a65cf"></a>

```c
int net_icmp_send_echo_request_no_wait (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_send_echo_request_no_wait](#ga4a1b59fac1b8934a8d0b8f1b981a65cf)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

发送 ICMP 回显请求消息（Echo Request Message），发送过程中不等待。

<a id="r_ga6cec9e51d91483c33deae86f24e582ae"></a>

```c
int net_icmp_register_offload_ping (struct net_icmp_offload *ctx, struct net_if *iface, net_icmp_offload_ping_handler_t ping_handler)
```

相关声明：[net_icmp_register_offload_ping](#ga6cec9e51d91483c33deae86f24e582ae)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_icmp_offload_ping_handler_t](#gad85b780080117bf3b53c5623f962ea71)。

注册向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

<a id="r_ga75f993c1f04d67c63689b5a6e1046d62"></a>

```c
int net_icmp_unregister_offload_ping (struct net_icmp_offload *ctx)
```

相关声明：[net_icmp_unregister_offload_ping](#ga75f993c1f04d67c63689b5a6e1046d62)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)。

注销卸载处理程序（Offload Handler）。

<a id="r_gad18ca68c320d977abaa3b757c4a1e5b0"></a>

```c
int net_icmp_get_offload_rsp_handler (struct net_icmp_offload *ctx, net_icmp_handler_t *resp_handler)
```

相关声明：[net_icmp_get_offload_rsp_handler](#gad18ca68c320d977abaa3b757c4a1e5b0)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)、[net_icmp_handler_t](#ga35da387f482e5da0c944bbfa349c3ea2)。

获取卸载设备（Offloaded Device）的 ICMP 响应处理函数（Response Handler）。

## 9.6\_详细说明（Detailed Documentation）

<a id="ga34b93cc7084276868f2b635021aad53b"></a>

### `NET_ICMPV4_ECHO_REPLY`

```c
#define NET_ICMPV4_ECHO_REPLY 0
```

```c
#include <zephyr/net/icmp.h>
```

ICMPv4 回显应答（Echo-Reply）。

<a id="gab09cfc243ae8aea120c2da9e77b3154f"></a>

### `NET_ICMPV4_ECHO_REQUEST`

```c
#define NET_ICMPV4_ECHO_REQUEST 8
```

```c
#include <zephyr/net/icmp.h>
```

ICMPv4 回显请求（Echo-Request）。

<a id="ga88187908775c5b84ec183f645454ac76"></a>

### `NET_ICMPV6_ECHO_REPLY`

```c
#define NET_ICMPV6_ECHO_REPLY 129
```

```c
#include <zephyr/net/icmp.h>
```

ICMPv6 回显应答（Echo-Reply）。

<a id="ga30ba68bc2372c6253ebce3db452591b3"></a>

### `NET_ICMPV6_ECHO_REQUEST`

```c
#define NET_ICMPV6_ECHO_REQUEST 128
```

```c
#include <zephyr/net/icmp.h>
```

ICMPv6 回显请求（Echo-Request）。

<a id="ga35da387f482e5da0c944bbfa349c3ea2"></a>

### `net_icmp_handler_t`

```c
typedef enum net_verdict(* net_icmp_handler_t) (struct net_icmp_ctx *ctx, struct net_pkt *pkt, struct net_icmp_ip_hdr *ip_hdr, struct net_icmp_hdr *icmp_hdr, void *user_data)
```

```c
#include <zephyr/net/icmp.h>
```

收到 ICMP 响应（Response）时调用的处理函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 要使用的 ICMP 上下文（Context）。 |
| `pkt` | 收到的 ICMP 响应网络数据包。 |
| `ip_hdr` | 数据包的 IP 头部（IP Header）。 |
| `icmp_hdr` | 数据包的 ICMP 头部（ICMP Header）。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_OK` | 已成功处理数据包，不再调用后续处理函数（Handlers）。 |
| `NET_CONTINUE` | 本处理函数未处理该数据包，应将其传递给下一个处理函数（Handler）。 |
| `NET_DROP` | 应丢弃该数据包，不再调用后续处理函数（Handlers）。 |

<a id="gad85b780080117bf3b53c5623f962ea71"></a>

### `net_icmp_offload_ping_handler_t`

```c
typedef int(* net_icmp_offload_ping_handler_t) (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

```c
#include <zephyr/net/icmp.h>
```

向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

此处理函数通常由设备驱动设置，以便捕获 ping 请求并发送给提供卸载功能的设备（Offloaded Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 上下文（Context）。 |
| `iface` | 网络接口（Network Interface），可设为 NULL，此时根据目标地址选择接口。 |
| `dst` | 目标主机的 IP 地址。 |
| `params` | 回送请求专用参数（Echo-Request Parameters）；可为 NULL，此时使用适当的默认参数。 |
| `user_data` | 传给处理函数的用户不透明数据（Opaque Data），可为 NULL。 |

<a id="gab90fe71303498c127f1f093d78d16ffa"></a>

### `net_icmp_cleanup_ctx()`

```c
int net_icmp_cleanup_ctx ( struct net_icmp_ctx * ctx)
```

```c
#include <zephyr/net/icmp.h>
```

清理 ICMP 上下文结构体（Context Structure）。

从系统中注销 ICMP 处理函数（Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 上下文（Context）。 |

<a id="gad18ca68c320d977abaa3b757c4a1e5b0"></a>

### `net_icmp_get_offload_rsp_handler()`

```c
int net_icmp_get_offload_rsp_handler ( struct net_icmp_offload * ctx, net_icmp_handler_t * resp_handler )
```

```c
#include <zephyr/net/icmp.h>
```

获取卸载设备（Offloaded Device）的 ICMP 响应处理函数（Response Handler）。

驱动收到 ping 响应后，应以适当参数调用处理函数，使网络协议栈接收到 ICMP 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 卸载上下文（Offload Context）。 |
| `resp_handler` | 提供卸载功能的驱动收到卸载 ping 响应时调用的函数。接口返回 ICMP 响应处理函数，调用方应在适当时机调用它。 |

**返回（Returns）**：返回值（Returns）：调用成功返回 0，否则返回小于 0 的值。

<a id="ga897d79bdeddb0890d4ef66f51d9505a7"></a>

### `net_icmp_init_ctx()`

```c
int net_icmp_init_ctx ( struct net_icmp_ctx * ctx, uint8_t family, uint8_t type, uint8_t code, net_icmp_handler_t handler )
```

```c
#include <zephyr/net/icmp.h>
```

初始化 ICMP 上下文结构体（Context Structure）。

必须在发送 ICMP 消息之前调用，以向系统注册处理函数（Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 上下文（Context）。 |
| `family` | 此上下文使用的地址族（Address Family）。 |
| `type` | 所处理 ICMP 消息的类型（Type）。 |
| `code` | 所处理 ICMP 消息的代码（Code）。 |
| `handler` | 收到响应时调用的回调函数（Callback Function）。 |

<a id="ga6cec9e51d91483c33deae86f24e582ae"></a>

### `net_icmp_register_offload_ping()`

```c
int net_icmp_register_offload_ping ( struct net_icmp_offload * ctx, struct net_if * iface, net_icmp_offload_ping_handler_t ping_handler )
```

```c
#include <zephyr/net/icmp.h>
```

注册向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

此函数通常由设备驱动调用，以执行实际的卸载 ping 调用（Offloaded Ping Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 此接口使用的 ICMP 卸载上下文（Offload Context）。 |
| `iface` | 提供卸载功能的设备的网络接口（Network Interface）。 |
| `ping_handler` | 卸载 ping 请求完成时调用的函数。 |

**返回（Returns）**：返回值（Returns）：注册成功返回 0，否则返回小于 0 的值。

<a id="ga588b1eecda05d5c275328fee4711b46b"></a>

### `net_icmp_send_echo_request()`

```c
int net_icmp_send_echo_request ( struct net_icmp_ctx * ctx, struct net_if * iface, struct net_sockaddr * dst, struct net_icmp_ping_params * params, void * user_data )
```

```c
#include <zephyr/net/icmp.h>
```

发送 ICMP 回显请求消息（Echo Request Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 上下文（Context）。 |
| `iface` | 网络接口（Network Interface），可设为 NULL，此时根据目标地址选择接口。 |
| `dst` | 目标主机的 IP 地址。 |
| `params` | 回送请求专用参数（Echo-Request Parameters）；可为 NULL，此时使用适当的默认参数。 |
| `user_data` | 传给处理函数的用户不透明数据（Opaque Data），可为 NULL。 |

**返回（Returns）**：返回值（Returns）：发送成功返回 0，否则返回小于 0 的值。

<a id="ga4a1b59fac1b8934a8d0b8f1b981a65cf"></a>

### `net_icmp_send_echo_request_no_wait()`

```c
int net_icmp_send_echo_request_no_wait ( struct net_icmp_ctx * ctx, struct net_if * iface, struct net_sockaddr * dst, struct net_icmp_ping_params * params, void * user_data )
```

```c
#include <zephyr/net/icmp.h>
```

发送 ICMP 回显请求消息（Echo Request Message），发送过程中不等待。

可使用此函数从系统工作队列处理函数（System Workqueue Handler）发送 ICMP 回送请求（Echo-Request），该处理函数不应休眠或等待。此变体使用 K_NO_WAIT 分配 net_buf，避免日志中出现有关超时的警告。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 本次请求使用的 ICMP 上下文（Context）。 |
| `iface` | 网络接口（Network Interface），可设为 NULL，此时根据目标地址选择接口。 |
| `dst` | 目标主机的 IP 地址。 |
| `params` | 回送请求专用参数（Echo-Request Parameters）；可为 NULL，此时使用适当的默认参数。 |
| `user_data` | 传给处理函数的用户不透明数据（Opaque Data），可为 NULL。 |

**返回（Returns）**：返回值（Returns）：发送成功返回 0，否则返回小于 0 的值。

<a id="ga75f993c1f04d67c63689b5a6e1046d62"></a>

### `net_icmp_unregister_offload_ping()`

```c
int net_icmp_unregister_offload_ping ( struct net_icmp_offload * ctx)
```

```c
#include <zephyr/net/icmp.h>
```

注销卸载处理程序（Offload Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 此接口使用的 ICMP 卸载上下文（Offload Context）。 |

**返回（Returns）**：返回值（Returns）：调用成功返回 0，否则返回小于 0 的值。


## 9.7\_原页交叉引用（Cross References）

- [icmp.h](../api_file_protocol_service_reference/P020_zephyr__net__icmp.h_文件参考.md)
- [net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)
- [net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)
- [net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)
- [net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [NET_OK](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)
- [NET_CONTINUE](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)
- [NET_DROP](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_HTTP服务器（Server）API。.md) · [返回大纲](大纲.md) · [下一章](P010_IPv6 套接字选项（Socket options）.md)
