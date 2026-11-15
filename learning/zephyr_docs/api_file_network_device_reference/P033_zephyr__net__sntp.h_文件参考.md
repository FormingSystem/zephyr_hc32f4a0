---
id: learning.zephyr-docs.api-file-network-device-reference.page-33
title: zephyr__net__sntp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_net\_\_sntp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络时间协议（Simple Network Time Protocol，SNTP）。

<a id="details"></a>

```c
#include <zephyr/net/socket.h>
#include <zephyr/net/socket_service.h>
```

查看此文件的源码。

简单网络时间协议（Simple Network Time Protocol，SNTP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_sntp_5Ftime"></a>

```c
struct sntp_time
```

相关声明：[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

SNTP API返回的时间，以自1970年1月1日起经过的秒数表示，包含小数秒部分。

<a id="r_sntp_5Fctx"></a>

```c
struct sntp_ctx
```

相关声明：[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)。

简单网络时间协议（SNTP）的上下文。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.2\_函数（Functions）

<a id="r_gab3395460258400a9b36d97418c706988"></a>

```c
int sntp_init (struct sntp_ctx *ctx, const struct net_sockaddr *addr, net_socklen_t addr_len)
```

相关声明：[sntp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab3395460258400a9b36d97418c706988)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

初始化简单网络时间协议（SNTP）上下文。

<a id="r_ga25ef46cc74be71bbe2f76de7c30cbe45"></a>

```c
int sntp_query (struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_query](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25ef46cc74be71bbe2f76de7c30cbe45)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

执行简单网络时间协议（SNTP）查询。

<a id="r_ga8771cdc6e64ab1489b333cc0c1731e9f"></a>

```c
int sntp_recv_response (struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_recv_response](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga8771cdc6e64ab1489b333cc0c1731e9f)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

发出查询后尝试接收 SNTP 响应（Response）。

<a id="r_ga0cff25edb11ae944dd24a234450a2f3d"></a>

```c
void sntp_close (struct sntp_ctx *ctx)
```

相关声明：[sntp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga0cff25edb11ae944dd24a234450a2f3d)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)。

释放简单网络时间协议（SNTP）上下文。

<a id="r_gacd621da6168cf064d0bf6c370f6ca597"></a>

```c
int sntp_init_async (struct sntp_ctx *ctx, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct net_socket_service_desc *service)
```

相关声明：[sntp_init_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gacd621da6168cf064d0bf6c370f6ca597)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

为异步操作（Asynchronous Operation）初始化 SNTP 上下文。

<a id="r_gab6adcd7259bdfa841b57e535c380508d"></a>

```c
int sntp_send_async (struct sntp_ctx *ctx)
```

相关声明：[sntp_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab6adcd7259bdfa841b57e535c380508d)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)。

发送 SNTP 查询（Query）。

<a id="r_gac73db957041a6814abb286fd9143ddb5"></a>

```c
int sntp_read_async (struct net_socket_service_event *event, struct sntp_time *ts)
```

相关声明：[sntp_read_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gac73db957041a6814abb286fd9143ddb5)、[net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

读取 SNTP 查询结果（Query Result）。

<a id="r_gaeb595e89c56fbb619010e3c8d7b2b5b1"></a>

```c
void sntp_close_async (const struct net_socket_service_desc *service)
```

相关声明：[sntp_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gaeb595e89c56fbb619010e3c8d7b2b5b1)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

释放简单网络时间协议（SNTP）上下文。

<a id="r_ga25c894db6d24a5e729b4edcb8917ce9c"></a>

```c
int sntp_simple (const char *server, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25c894db6d24a5e729b4edcb8917ce9c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

以单次方式（One-shot）查询 SNTP 的便捷函数。

<a id="r_gadb5603eeaea68e0823f8a3f6a1b8a6c1"></a>

```c
int sntp_simple_addr (struct net_sockaddr *addr, net_socklen_t addr_len, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_simple_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gadb5603eeaea68e0823f8a3f6a1b8a6c1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

使用预初始化地址结构体，以单次方式（One-shot）查询 SNTP 的便捷函数。


## 33.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zephyr/net/socket_service.h](../api_source_configuration_reference/P104_socket_service.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P800_sntp.h_源码浏览.md)
- [sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)
- [sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)
- [sntp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab3395460258400a9b36d97418c706988)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [sntp_query](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25ef46cc74be71bbe2f76de7c30cbe45)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sntp_recv_response](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga8771cdc6e64ab1489b333cc0c1731e9f)
- [sntp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga0cff25edb11ae944dd24a234450a2f3d)
- [sntp_init_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gacd621da6168cf064d0bf6c370f6ca597)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [sntp_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab6adcd7259bdfa841b57e535c380508d)
- [sntp_read_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gac73db957041a6814abb286fd9143ddb5)
- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [sntp_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gaeb595e89c56fbb619010e3c8d7b2b5b1)
- [sntp_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25c894db6d24a5e729b4edcb8917ce9c)
- [sntp_simple_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gadb5603eeaea68e0823f8a3f6a1b8a6c1)

<a id="header-details"></a>

---

[上一章](P032_zephyr__dt-bindings__interrupt-controller__rts5817_intc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__net__socket_offload.h_文件参考.md)
