---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-17
title: 简单网络时间协议（SNTP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_简单网络时间协议（SNTP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络时间协议（Simple Network Time Protocol）API

<a id="details"></a>

简单网络时间协议（Simple Network Time Protocol，SNTP）API。**引入版本（Since）：**1.10。**版本（Version）：**0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 17.1\_主题（Topics）

<a id="r_sntp_5Fserver"></a>

相关声明：[SNTP 服务器](../api_protocol_topic_reference/P058_SNTP 服务器.md)。

简单网络时间协议服务器 API

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.2\_数据结构（Data Structures）

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

## 17.3\_函数（Functions）

<a id="r_gab3395460258400a9b36d97418c706988"></a>

```c
int sntp_init (struct sntp_ctx *ctx, const struct net_sockaddr *addr, net_socklen_t addr_len)
```

相关声明：[sntp_init](#gab3395460258400a9b36d97418c706988)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

初始化简单网络时间协议（SNTP）上下文。

<a id="r_ga25ef46cc74be71bbe2f76de7c30cbe45"></a>

```c
int sntp_query (struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_query](#ga25ef46cc74be71bbe2f76de7c30cbe45)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

执行简单网络时间协议（SNTP）查询。

<a id="r_ga8771cdc6e64ab1489b333cc0c1731e9f"></a>

```c
int sntp_recv_response (struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_recv_response](#ga8771cdc6e64ab1489b333cc0c1731e9f)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

发出查询后尝试接收 SNTP 响应（Response）。

<a id="r_ga0cff25edb11ae944dd24a234450a2f3d"></a>

```c
void sntp_close (struct sntp_ctx *ctx)
```

相关声明：[sntp_close](#ga0cff25edb11ae944dd24a234450a2f3d)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)。

释放简单网络时间协议（SNTP）上下文。

<a id="r_gacd621da6168cf064d0bf6c370f6ca597"></a>

```c
int sntp_init_async (struct sntp_ctx *ctx, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct net_socket_service_desc *service)
```

相关声明：[sntp_init_async](#gacd621da6168cf064d0bf6c370f6ca597)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

为异步操作（Asynchronous Operation）初始化 SNTP 上下文。

<a id="r_gab6adcd7259bdfa841b57e535c380508d"></a>

```c
int sntp_send_async (struct sntp_ctx *ctx)
```

相关声明：[sntp_send_async](#gab6adcd7259bdfa841b57e535c380508d)、[sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)。

发送 SNTP 查询（Query）。

<a id="r_gac73db957041a6814abb286fd9143ddb5"></a>

```c
int sntp_read_async (struct net_socket_service_event *event, struct sntp_time *ts)
```

相关声明：[sntp_read_async](#gac73db957041a6814abb286fd9143ddb5)、[net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

读取 SNTP 查询结果（Query Result）。

<a id="r_gaeb595e89c56fbb619010e3c8d7b2b5b1"></a>

```c
void sntp_close_async (const struct net_socket_service_desc *service)
```

相关声明：[sntp_close_async](#gaeb595e89c56fbb619010e3c8d7b2b5b1)、[net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)。

释放简单网络时间协议（SNTP）上下文。

<a id="r_ga25c894db6d24a5e729b4edcb8917ce9c"></a>

```c
int sntp_simple (const char *server, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_simple](#ga25c894db6d24a5e729b4edcb8917ce9c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

以单次方式（One-shot）查询 SNTP 的便捷函数。

<a id="r_gadb5603eeaea68e0823f8a3f6a1b8a6c1"></a>

```c
int sntp_simple_addr (struct net_sockaddr *addr, net_socklen_t addr_len, uint32_t timeout, struct sntp_time *ts)
```

相关声明：[sntp_simple_addr](#gadb5603eeaea68e0823f8a3f6a1b8a6c1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)。

使用预初始化地址结构体，以单次方式（One-shot）查询 SNTP 的便捷函数。

## 17.4\_详细说明（Detailed Documentation）

<a id="ga0cff25edb11ae944dd24a234450a2f3d"></a>

### `sntp_close()`

```c
void sntp_close ( struct sntp_ctx * ctx)
```

```c
#include <zephyr/net/sntp.h>
```

释放简单网络时间协议（SNTP）上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |

<a id="gaeb595e89c56fbb619010e3c8d7b2b5b1"></a>

### `sntp_close_async()`

```c
void sntp_close_async ( const struct net_socket_service_desc * service)
```

```c
#include <zephyr/net/sntp.h>
```

释放简单网络时间协议（SNTP）上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 由 `NET_SOCKET_SERVICE_SYNC_DEFINE` 定义的套接字服务（Socket Service）。 |

<a id="gab3395460258400a9b36d97418c706988"></a>

### `sntp_init()`

```c
int sntp_init ( struct sntp_ctx * ctx, const struct net_sockaddr * addr, net_socklen_t addr_len )
```

```c
#include <zephyr/net/sntp.h>
```

初始化简单网络时间协议（SNTP）上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |
| `addr` | NTP/SNTP 服务器的 IP 地址。 |
| `addr_len` | NTP/SNTP 服务器 IP 地址的长度。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gacd621da6168cf064d0bf6c370f6ca597"></a>

### `sntp_init_async()`

```c
int sntp_init_async ( struct sntp_ctx * ctx, const struct net_sockaddr * addr, net_socklen_t addr_len, const struct net_socket_service_desc * service )
```

```c
#include <zephyr/net/sntp.h>
```

为异步操作（Asynchronous Operation）初始化 SNTP 上下文。

异步操作（Asynchronous Operation）由 `CONFIG_NET_SOCKETS_SERVICE` 提供支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |
| `addr` | NTP/SNTP 服务器的 IP 地址。 |
| `addr_len` | NTP/SNTP 服务器 IP 地址的长度。 |
| `service` | 由 `NET_SOCKET_SERVICE_SYNC_DEFINE` 定义的套接字服务（Socket Service）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga25ef46cc74be71bbe2f76de7c30cbe45"></a>

### `sntp_query()`

```c
int sntp_query ( struct sntp_ctx * ctx, uint32_t timeout, struct sntp_time * ts )
```

```c
#include <zephyr/net/sntp.h>
```

执行简单网络时间协议（SNTP）查询。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |
| `timeout` | 等待 SNTP 响应的超时时间（Timeout），单位为毫秒。 |
| `ts` | 自 1970 年 1 月 1 日以来的时间戳（Timestamp），包含整数秒和小数秒（输出，Output）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回小于 `0` 的值；超时返回 `-ETIMEDOUT`。

<a id="gac73db957041a6814abb286fd9143ddb5"></a>

### `sntp_read_async()`

```c
int sntp_read_async ( struct net_socket_service_event * event, struct sntp_time * ts )
```

```c
#include <zephyr/net/sntp.h>
```

读取 SNTP 查询结果（Query Result）。

必须从附加到 `net_socket_service_desc` 上下文（Context）的回调中调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | 从服务工作回调（Service Work Callback）中提取的事件指针（Event Pointer）。 |
| `ts` | 自 1970 年 1 月 1 日以来的时间戳（Timestamp），包含整数秒和小数秒（输出，Output）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga8771cdc6e64ab1489b333cc0c1731e9f"></a>

### `sntp_recv_response()`

```c
int sntp_recv_response ( struct sntp_ctx * ctx, uint32_t timeout, struct sntp_time * ts )
```

```c
#include <zephyr/net/sntp.h>
```

发出查询后尝试接收 SNTP 响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |
| `timeout` | 等待 SNTP 响应的超时时间（Timeout），单位为毫秒。 |
| `ts` | 自 1970 年 1 月 1 日以来的时间戳（Timestamp），包含整数秒和小数秒（输出，Output）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回小于 `0` 的值；超时返回 `-ETIMEDOUT`。

<a id="gab6adcd7259bdfa841b57e535c380508d"></a>

### `sntp_send_async()`

```c
int sntp_send_async ( struct sntp_ctx * ctx)
```

```c
#include <zephyr/net/sntp.h>
```

发送 SNTP 查询（Query）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | SNTP 上下文（Context）的地址。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga25c894db6d24a5e729b4edcb8917ce9c"></a>

### `sntp_simple()`

```c
int sntp_simple ( const char * server, uint32_t timeout, struct sntp_time * ts )
```

```c
#include <zephyr/net/sntp.h>
```

以单次方式（One-shot）查询 SNTP 的便捷函数。

依次调用 `getaddrinfo()`、`sntp_init()`、`sntp_query()` 和 `sntp_close()` 的便捷包装函数（Convenience Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 格式为 `addr[:port]` 的服务器地址（Server Address）。 |
| `timeout` | 查询超时时间（Query Timeout）。 |
| `ts` | 自 1970 年 1 月 1 日以来的时间戳（Timestamp），包含整数秒和小数秒（输出，Output）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回小于 `0` 的值；超时返回 `-ETIMEDOUT`。

<a id="gadb5603eeaea68e0823f8a3f6a1b8a6c1"></a>

### `sntp_simple_addr()`

```c
int sntp_simple_addr ( struct net_sockaddr * addr, net_socklen_t addr_len, uint32_t timeout, struct sntp_time * ts )
```

```c
#include <zephyr/net/sntp.h>
```

使用预初始化地址结构体，以单次方式（One-shot）查询 SNTP 的便捷函数。

依次调用 `sntp_init()`、`sntp_query()` 和 `sntp_close()` 的便捷包装函数（Convenience Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | NTP/SNTP 服务器的 IP 地址。 |
| `addr_len` | NTP/SNTP 服务器 IP 地址的长度。 |
| `timeout` | 查询超时时间（Query Timeout）。 |
| `ts` | 自 1970 年 1 月 1 日以来的时间戳（Timestamp），包含整数秒和小数秒（输出，Output）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回小于 `0` 的值；超时返回 `-ETIMEDOUT`。


## 17.5\_原页交叉引用（Cross References）

- [SNTP 服务器](../api_protocol_topic_reference/P058_SNTP 服务器.md)
- [sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)
- [sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [zephyr/net/sntp.h](../api_file_network_device_reference/P033_zephyr__net__sntp.h_文件参考.md)
- [NET_SOCKET_SERVICE_SYNC_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga424f319f9ccc675f8eeca23cb2c91bc4)
- [CONFIG_NET_SOCKETS_SERVICE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)
- [getaddrinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#adc9ea491d9008de7cd9e0a5b9147ca70)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_单边沿半字节传输（SENT）.md) · [返回大纲](大纲.md) · [下一章](P018_全球导航卫星系统（GNSS）配置.md)
