---
id: learning.zephyr-docs.network-core-model-reference.page-76
title: net_icmp_ip_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ip__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_net\_icmp\_ip\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ip__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示ICMP响应消息中IPv4或IPv6头部（Header）的结构。

```c
#include <zephyr/net/icmp.h>
```

<a id="details"></a>

表示ICMP响应消息中IPv4或IPv6头部（Header）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a9842b865111a49ee8644a22ea014de07"></a>

```c
struct net_ipv4_hdr * ipv4
```

相关声明：[ipv4](#a3d0d8b7442611c74a71a72ab1d1c7a90)。

响应消息中的IPv4头部（Header）。

<a id="r_a7a956139794da42d8d83a032a97fe839"></a>

```c
struct net_ipv6_hdr * ipv6
```

相关声明：[ipv6](#ac993b71afdd637dba048ba5038d489c8)。

响应消息中的IPv6头部（Header）。

<a id="r_a2db6f9a29bd3cc97b662f00d2d886e85"></a>

```c
};
```

<a id="r_a354d2ab876d9cb13f18d4ef905cf16cb"></a>

```c
net_sa_family_t family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[family](#a354d2ab876d9cb13f18d4ef905cf16cb)。

头部（Header）属于IPv4还是IPv6。

## 76.2\_详细说明（Detailed Documentation）

<a id="a2db6f9a29bd3cc97b662f00d2d886e85"></a>

### `[union]`

```c
union { ... } net_icmp_ip_hdr
```

<a id="a354d2ab876d9cb13f18d4ef905cf16cb"></a>

### `family`

```c
net_sa_family_t net_icmp_ip_hdr::family
```

头部（Header）属于IPv4还是IPv6。

值为NET_AF_INET或NET_AF_INET6。

<a id="a3d0d8b7442611c74a71a72ab1d1c7a90"></a>

### `ipv4`

```c
struct net_ipv4_hdr* net_icmp_ip_hdr::ipv4
```

响应消息中的IPv4头部（Header）。

<a id="ac993b71afdd637dba048ba5038d489c8"></a>

### `ipv6`

```c
struct net_ipv6_hdr* net_icmp_ip_hdr::ipv6
```

响应消息中的IPv6头部（Header）。

本数据类型文档由以下文件生成：

- `zephyr/net/icmp.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/net/icmp.h](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_icmp_ip_hdr](P076_net_icmp_ip_hdr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_net_icmp_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_net_icmp_offload_结构体.md)
