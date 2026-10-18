---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-20
title: zephyr__net__icmp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_net\_\_icmp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网控制消息协议（ICMP）支持功能的头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
```

查看此文件的源码。

互联网控制消息协议（ICMP）支持功能的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

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

## 20.2\_宏定义（Macros）

<a id="r_gab09cfc243ae8aea120c2da9e77b3154f"></a>

```c
#define NET_ICMPV4_ECHO_REQUEST 8
```

相关声明：[NET_ICMPV4_ECHO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gab09cfc243ae8aea120c2da9e77b3154f)。

ICMPv4 回显请求（Echo-Request）。

<a id="r_ga34b93cc7084276868f2b635021aad53b"></a>

```c
#define NET_ICMPV4_ECHO_REPLY 0
```

相关声明：[NET_ICMPV4_ECHO_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga34b93cc7084276868f2b635021aad53b)。

ICMPv4 回显应答（Echo-Reply）。

<a id="r_ga30ba68bc2372c6253ebce3db452591b3"></a>

```c
#define NET_ICMPV6_ECHO_REQUEST 128
```

相关声明：[NET_ICMPV6_ECHO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga30ba68bc2372c6253ebce3db452591b3)。

ICMPv6 回显请求（Echo-Request）。

<a id="r_ga88187908775c5b84ec183f645454ac76"></a>

```c
#define NET_ICMPV6_ECHO_REPLY 129
```

相关声明：[NET_ICMPV6_ECHO_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga88187908775c5b84ec183f645454ac76)。

ICMPv6 回显应答（Echo-Reply）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 20.3\_类型定义（Typedefs）

<a id="r_ga35da387f482e5da0c944bbfa349c3ea2"></a>

```c
typedef enum net_verdict(* net_icmp_handler_t) (struct net_icmp_ctx *ctx, struct net_pkt *pkt, struct net_icmp_ip_hdr *ip_hdr, struct net_icmp_hdr *icmp_hdr, void *user_data)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)。

收到 ICMP 响应（Response）时调用的处理函数。

<a id="r_gad85b780080117bf3b53c5623f962ea71"></a>

```c
typedef int(* net_icmp_offload_ping_handler_t) (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.4\_函数（Functions）

<a id="r_ga897d79bdeddb0890d4ef66f51d9505a7"></a>

```c
int net_icmp_init_ctx (struct net_icmp_ctx *ctx, uint8_t family, uint8_t type, uint8_t code, net_icmp_handler_t handler)
```

相关声明：[net_icmp_init_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga897d79bdeddb0890d4ef66f51d9505a7)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)。

初始化 ICMP 上下文结构体（Context Structure）。

<a id="r_gab90fe71303498c127f1f093d78d16ffa"></a>

```c
int net_icmp_cleanup_ctx (struct net_icmp_ctx *ctx)
```

相关声明：[net_icmp_cleanup_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gab90fe71303498c127f1f093d78d16ffa)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)。

清理 ICMP 上下文结构体（Context Structure）。

<a id="r_ga588b1eecda05d5c275328fee4711b46b"></a>

```c
int net_icmp_send_echo_request (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_send_echo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga588b1eecda05d5c275328fee4711b46b)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

发送 ICMP 回显请求消息（Echo Request Message）。

<a id="r_ga4a1b59fac1b8934a8d0b8f1b981a65cf"></a>

```c
int net_icmp_send_echo_request_no_wait (struct net_icmp_ctx *ctx, struct net_if *iface, struct net_sockaddr *dst, struct net_icmp_ping_params *params, void *user_data)
```

相关声明：[net_icmp_send_echo_request_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga4a1b59fac1b8934a8d0b8f1b981a65cf)、[net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)。

发送 ICMP 回显请求消息（Echo Request Message），发送过程中不等待。

<a id="r_ga6cec9e51d91483c33deae86f24e582ae"></a>

```c
int net_icmp_register_offload_ping (struct net_icmp_offload *ctx, struct net_if *iface, net_icmp_offload_ping_handler_t ping_handler)
```

相关声明：[net_icmp_register_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga6cec9e51d91483c33deae86f24e582ae)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)。

注册向卸载设备（Offloaded Device）发送回显请求（Echo-Request）时调用的处理函数。

<a id="r_ga75f993c1f04d67c63689b5a6e1046d62"></a>

```c
int net_icmp_unregister_offload_ping (struct net_icmp_offload *ctx)
```

相关声明：[net_icmp_unregister_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga75f993c1f04d67c63689b5a6e1046d62)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)。

注销卸载处理程序（Offload Handler）。

<a id="r_gad18ca68c320d977abaa3b757c4a1e5b0"></a>

```c
int net_icmp_get_offload_rsp_handler (struct net_icmp_offload *ctx, net_icmp_handler_t *resp_handler)
```

相关声明：[net_icmp_get_offload_rsp_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad18ca68c320d977abaa3b757c4a1e5b0)、[net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)、[net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)。

获取卸载设备（Offloaded Device）的 ICMP 响应处理函数（Response Handler）。


## 20.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_pkt.h](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P337_icmp.h_源码浏览.md)
- [net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)
- [net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)
- [net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)
- [net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)
- [NET_ICMPV4_ECHO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gab09cfc243ae8aea120c2da9e77b3154f)
- [NET_ICMPV4_ECHO_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga34b93cc7084276868f2b635021aad53b)
- [NET_ICMPV6_ECHO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga30ba68bc2372c6253ebce3db452591b3)
- [NET_ICMPV6_ECHO_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga88187908775c5b84ec183f645454ac76)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_icmp_init_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga897d79bdeddb0890d4ef66f51d9505a7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_icmp_cleanup_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gab90fe71303498c127f1f093d78d16ffa)
- [net_icmp_send_echo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga588b1eecda05d5c275328fee4711b46b)
- [net_icmp_send_echo_request_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga4a1b59fac1b8934a8d0b8f1b981a65cf)
- [net_icmp_register_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga6cec9e51d91483c33deae86f24e582ae)
- [net_icmp_unregister_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga75f993c1f04d67c63689b5a6e1046d62)
- [net_icmp_get_offload_rsp_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad18ca68c320d977abaa3b757c4a1e5b0)

<a id="header-details"></a>

---

[上一章](P019_zephyr__drivers__sensor__htu31d.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__net__ieee802154_ie.h_文件参考.md)
