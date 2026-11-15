---
id: learning.zephyr-docs.network-application-model-reference.page-21
title: dns_resolve_context__dns_server_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context_1_1dns__server__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_dns\_resolve\_context\_\_dns\_server\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context_1_1dns__server__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

一个已配置DNS服务器的信息。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

一个已配置DNS服务器的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a6cab2a1ca50fe70577a3047395e762c1"></a>

```c
struct net_sockaddr_storage dns_server_addr
```

相关声明：[dns_server_addr](#a376e382dcee794c822b17d5d9eeb2c0d)。

DNS服务器信息。

<a id="r_ac2cc4ce90cf087be0e809d4c5cf17a45"></a>

```c
};
```

DNS服务器的地址存储（Address Storage）。

<a id="r_ab0aa7615cba374226bee823302d5b94a"></a>

```c
int sock
```

相关声明：[sock](#ab0aa7615cba374226bee823302d5b94a)。

与DNS服务器的连接（Connection）。

<a id="r_a9d5e279f80a571fdca057ed552db3b92"></a>

```c
int if_index
```

相关声明：[if_index](#a9d5e279f80a571fdca057ed552db3b92)。

如果应通过此网络接口解析DNS，则为该接口的索引（Interface Index）。

<a id="r_a65114f0c580f06ca2a5262c5336e682e"></a>

```c
enum dns_server_source source
```

相关声明：[dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)、[source](#a65114f0c580f06ca2a5262c5336e682e)。

DNS服务器的来源（Source），例如手动配置、DHCPv4/6等。

<a id="r_a211583df0f70ea94b6fb38785bd6b08c"></a>

```c
uint8_t is_mdns: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_mdns](#a211583df0f70ea94b6fb38785bd6b08c)。

此服务器是否为组播DNS（mDNS）服务器。

<a id="r_a7f15ba79ca39d6403ebd41d8fef017c3"></a>

```c
uint8_t is_llmnr: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_llmnr](#a7f15ba79ca39d6403ebd41d8fef017c3)。

此服务器是否为链路本地组播名称解析（LLMNR）服务器。

## 21.2\_详细说明（Detailed Documentation）

<a id="ac2cc4ce90cf087be0e809d4c5cf17a45"></a>

### `[union]`

```c
union { ... } dns_resolve_context::dns_server_info
```

DNS服务器的地址存储（Address Storage）。

<a id="a376e382dcee794c822b17d5d9eeb2c0d"></a>

### `dns_server_addr`

```c
struct net_sockaddr_storage dns_resolve_context::dns_server_info::dns_server_addr
```

DNS服务器信息。

<a id="a9d5e279f80a571fdca057ed552db3b92"></a>

### `if_index`

```c
int dns_resolve_context::dns_server_info::if_index
```

如果应通过此网络接口解析DNS，则为该接口的索引（Interface Index）。

0表示可使用任意接口（Interface）。

<a id="a7f15ba79ca39d6403ebd41d8fef017c3"></a>

### `is_llmnr`

```c
uint8_t dns_resolve_context::dns_server_info::is_llmnr
```

此服务器是否为链路本地组播名称解析（LLMNR）服务器。

<a id="a211583df0f70ea94b6fb38785bd6b08c"></a>

### `is_mdns`

```c
uint8_t dns_resolve_context::dns_server_info::is_mdns
```

此服务器是否为组播DNS（mDNS）服务器。

<a id="ab0aa7615cba374226bee823302d5b94a"></a>

### `sock`

```c
int dns_resolve_context::dns_server_info::sock
```

与DNS服务器的连接（Connection）。

<a id="a65114f0c580f06ca2a5262c5336e682e"></a>

### `source`

```c
enum dns_server_source dns_resolve_context::dns_server_info::source
```

DNS服务器的来源（Source），例如手动配置、DHCPv4/6等。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [dns_resolve_context::dns_server_info](P021_dns_resolve_context__dns_server_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_dns_resolve_context__dns_pending_query_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_dns_resolve_private_结构体.md)
