---
id: learning.zephyr-docs.network-service-model-reference.page-55
title: socket_dns_offload_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsocket__dns__offload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_socket\_dns\_offload\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsocket__dns__offload.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

卸载式套接字DNS（Offloaded Socket DNS）的API接口。

```c
#include <zephyr/net/socket_offload.h>
```

<a id="details"></a>

卸载型套接字 DNS API（offloaded Socket DNS API）接口。假定这些卸载函数在参数、返回值及 `errno` 设置方面遵守 POSIX 套接字 API 标准。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a5241208180bcc8f553d0db6e74e5c115"></a>

```c
int(* getaddrinfo )(const char *node, const char *service, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

相关声明：[getaddrinfo](#a5241208180bcc8f553d0db6e74e5c115)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

DNS `getaddrinfo` 的卸载实现 API。

<a id="r_a73640bb24b4838c337ef1a61ffd4949f"></a>

```c
void(* freeaddrinfo )(struct zsock_addrinfo *res)
```

相关声明：[freeaddrinfo](#a73640bb24b4838c337ef1a61ffd4949f)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

DNS `freeaddrinfo` 的卸载实现 API。

## 55.2\_详细说明（Detailed Documentation）

<a id="a73640bb24b4838c337ef1a61ffd4949f"></a>

### `freeaddrinfo`

```c
void(* socket_dns_offload::freeaddrinfo) (struct zsock_addrinfo *res)
```

DNS `freeaddrinfo` 的卸载实现 API。

<a id="a5241208180bcc8f553d0db6e74e5c115"></a>

### `getaddrinfo`

```c
int(* socket_dns_offload::getaddrinfo) (const char *node, const char *service, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

DNS `getaddrinfo` 的卸载实现 API。

本数据类型文档由以下文件生成：

- `zephyr/net/socket_offload.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/net/socket_offload.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h_source.html)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_ptp_clock_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_socketcan_filter_结构体.md)
