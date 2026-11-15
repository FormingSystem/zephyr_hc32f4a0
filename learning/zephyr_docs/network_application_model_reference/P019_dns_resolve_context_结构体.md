---
id: learning.zephyr-docs.network-application-model-reference.page-19
title: dns_resolve_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_dns\_resolve\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS解析上下文（Resolve Context）结构。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

DNS解析上下文（Resolve Context）结构。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.1\_数据结构（Data Structures）

<a id="r_dns_5Fserver_5Finfo"></a>

```c
struct dns_server_info
```

相关声明：[dns_server_info](P021_dns_resolve_context__dns_server_info_结构体.md)。

一个已配置DNS服务器的信息。

<a id="r_dns_5Fpending_5Fquery"></a>

```c
struct dns_pending_query
```

相关声明：[dns_pending_query](P020_dns_resolve_context__dns_pending_query_结构体.md)。

结果回调（Result Callbacks）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.2\_数据成员（Data Fields）

<a id="r_a8613ff54a235c211ba2cc3d232cb10a2"></a>

```c
struct dns_resolve_context::dns_server_info servers [DNS_RESOLVER_MAX_POLL]
```

相关声明：[dns_resolve_context::dns_server_info](P021_dns_resolve_context__dns_server_info_结构体.md)、[servers](#a8613ff54a235c211ba2cc3d232cb10a2)。

已配置DNS服务器的列表。

<a id="r_a9d1ada3ab20399f750acfee94e8e6cd7"></a>

```c
struct k_mutex lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[lock](#a9d1ada3ab20399f750acfee94e8e6cd7)。

防止并发访问（Concurrent Access）。

<a id="r_a402a4a2adfe3859f8dab749b44b7d8e6"></a>

```c
k_timeout_t buf_timeout
```

相关声明：[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[buf_timeout](#a402a4a2adfe3859f8dab749b44b7d8e6)。

需要从缓冲池（Buffer Pools）取得缓冲区时，也使用此超时值。

<a id="r_a596053473b44be4977947632a1abb51e"></a>

```c
struct dns_resolve_context::dns_pending_query queries [DNS_NUM_CONCUR_QUERIES]
```

相关声明：[dns_resolve_context::dns_pending_query](P020_dns_resolve_context__dns_pending_query_结构体.md)、[queries](#a596053473b44be4977947632a1abb51e)。

<a id="r_a88f6600061cdb8e9f34802fe2a0a7d5a"></a>

```c
enum dns_resolve_context_state state
```

相关声明：[state](#a88f6600061cdb8e9f34802fe2a0a7d5a)。

此上下文（Context）是否正在使用。

<a id="r_a250a016056fd44533eeffc30419ec283"></a>

```c
dns_resolve_pkt_fw_cb_t pkt_fw_cb
```

相关声明：[dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)、[pkt_fw_cb](#a250a016056fd44533eeffc30419ec283)。

DNS数据包转发回调（Packet Forwarding Callback）。

## 19.3\_详细说明（Detailed Documentation）

<a id="a402a4a2adfe3859f8dab749b44b7d8e6"></a>

### `buf_timeout`

```c
k_timeout_t dns_resolve_context::buf_timeout
```

需要从缓冲池（Buffer Pools）取得缓冲区时，也使用此超时值。

<a id="a9d1ada3ab20399f750acfee94e8e6cd7"></a>

### `lock`

```c
struct k_mutex dns_resolve_context::lock
```

防止并发访问（Concurrent Access）。

<a id="a250a016056fd44533eeffc30419ec283"></a>

### `pkt_fw_cb`

```c
dns_resolve_pkt_fw_cb_t dns_resolve_context::pkt_fw_cb
```

DNS数据包转发回调（Packet Forwarding Callback）。

<a id="a596053473b44be4977947632a1abb51e"></a>

### `queries`

```c
struct dns_resolve_context::dns_pending_query dns_resolve_context::queries[DNS_NUM_CONCUR_QUERIES]
```

<a id="a8613ff54a235c211ba2cc3d232cb10a2"></a>

### `servers`

```c
struct dns_resolve_context::dns_server_info dns_resolve_context::servers[DNS_RESOLVER_MAX_POLL]
```

已配置DNS服务器的列表。

<a id="a88f6600061cdb8e9f34802fe2a0a7d5a"></a>

### `state`

```c
enum dns_resolve_context_state dns_resolve_context::state
```

此上下文（Context）是否正在使用。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 19.4\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [dns_server_info](P021_dns_resolve_context__dns_server_info_结构体.md)
- [dns_pending_query](P020_dns_resolve_context__dns_pending_query_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_dns_addrinfo_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_dns_resolve_context__dns_pending_query_结构体.md)
