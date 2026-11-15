---
id: learning.zephyr-docs.network-core-model-reference.page-103
title: net_l2_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__l2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_net\_l2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__l2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络第二层（Network L2）结构。

```c
#include <zephyr/net/net_l2.h>
```

<a id="details"></a>

网络二层结构（Network L2 structure）。用于提供通往下层网络栈（Lower network stack）的接口。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 103.1\_数据成员（Data Fields）

<a id="r_a1faa6e5b0c9228dd52c64fc7f2fd8036"></a>

```c
enum net_verdict(* recv )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[recv](#a1faa6e5b0c9228dd52c64fc7f2fd8036)、[net_if](P079_net_if_结构体.md)、[net_pkt](P114_net_pkt_结构体.md)。

网络核心（Net core）使用此函数，让接口的二层（L2）解析与自身相关的内容。

<a id="r_a17d649732c3bb6bf9cc77a4939eb8801"></a>

```c
int(* send )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[send](#a17d649732c3bb6bf9cc77a4939eb8801)、[net_if](P079_net_if_结构体.md)、[net_pkt](P114_net_pkt_结构体.md)。

网络核心（Net core）使用此函数将数据包交给下层，即接口的二层（L2）；后者可以对数据包执行相关处理。

<a id="r_a5d42c51eb8dc4d6a990aa9ff88a66b94"></a>

```c
int(* enable )(struct net_if *iface, bool state)
```

相关声明：[enable](#a5d42c51eb8dc4d6a990aa9ff88a66b94)、[net_if](P079_net_if_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

此函数用于启用或禁用网络接口上的流量（Traffic）。

<a id="r_a492c5c75801b9c8784c9322805869334"></a>

```c
enum net_l2_flags(* get_flags )(struct net_if *iface)
```

相关声明：[net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)、[get_flags](#a492c5c75801b9c8784c9322805869334)、[net_if](P079_net_if_结构体.md)。

返回网络接口的二层标志（L2 flags）。

<a id="r_a9aed44777aa01efcd45874679c6ea1c2"></a>

```c
int(* alloc )(struct net_if *iface, struct net_pkt *pkt, size_t size, enum net_ip_protocol proto, k_timeout_t timeout)
```

相关声明：[alloc](#a9aed44777aa01efcd45874679c6ea1c2)、[net_if](P079_net_if_结构体.md)、[net_pkt](P114_net_pkt_结构体.md)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

可选函数，用于为此技术预留二层报头空间（L2 header space）。

## 103.2\_详细说明（Detailed Documentation）

<a id="a9aed44777aa01efcd45874679c6ea1c2"></a>

### `alloc`

```c
int(* net_l2::alloc) (struct net_if *iface, struct net_pkt *pkt, size_t size, enum net_ip_protocol proto, k_timeout_t timeout)
```

可选函数，用于为此技术预留二层报头空间（L2 header space）。

<a id="a5d42c51eb8dc4d6a990aa9ff88a66b94"></a>

### `enable`

```c
int(* net_l2::enable) (struct net_if *iface, bool state)
```

此函数用于启用或禁用网络接口上的流量（Traffic）。

发生错误时，此函数返回小于 `0` 的值；未发生错误时返回大于或等于 `0` 的值。

<a id="a492c5c75801b9c8784c9322805869334"></a>

### `get_flags`

```c
enum net_l2_flags(* net_l2::get_flags) (struct net_if *iface)
```

返回网络接口的二层标志（L2 flags）。

<a id="a1faa6e5b0c9228dd52c64fc7f2fd8036"></a>

### `recv`

```c
enum net_verdict(* net_l2::recv) (struct net_if *iface, struct net_pkt *pkt)
```

网络核心（Net core）使用此函数，让接口的二层（L2）解析与自身相关的内容。

<a id="a17d649732c3bb6bf9cc77a4939eb8801"></a>

### `send`

```c
int(* net_l2::send) (struct net_if *iface, struct net_pkt *pkt)
```

网络核心（Net core）使用此函数将数据包交给下层，即接口的二层（L2）；后者可以对数据包执行相关处理。

例如添加适当的报头（Header）等。返回负错误码；数据包已被接受时返回 `0`。

本数据类型文档由以下文件生成：

- `zephyr/net/net_l2.h`

## 103.3\_原页交叉引用（Cross References）

- [zephyr/net/net_l2.h](https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h_source.html)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [net_if](P079_net_if_结构体.md)
- [net_pkt](P114_net_pkt_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P102_net_ipv6_mreq_结构体.md) · [返回大纲](大纲.md) · [下一章](P104_net_linger_结构体.md)
