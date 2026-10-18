---
id: learning.zephyr-docs.network-core-model-reference.page-56
title: net_dhcpv6_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_net\_dhcpv6\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv6客户端（Client）的配置参数。

```c
#include <zephyr/net/dhcpv6.h>
```

<a id="details"></a>

DHCPv6客户端（Client）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_a4bc3655ee2a830879667cdb554883573"></a>

```c
bool request_addr: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[request_addr](#a4bc3655ee2a830879667cdb554883573)。

请求IPv6地址（Address）。

<a id="r_afd290d92fcc5ae3bac9a9c7030910e6b"></a>

```c
bool request_prefix: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[request_prefix](#afd290d92fcc5ae3bac9a9c7030910e6b)。

请求IPv6前缀（Prefix）。

<a id="r_a2549234454437b4316f863347236ef6c"></a>

```c
uint8_t downstream_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[downstream_count](#a2549234454437b4316f863347236ef6c)。

downstream_ifaces中有效条目的数量。

<a id="r_ad66949eb34540dbe8808dc9aea9e6368"></a>

```c
int downstream_ifaces [NET_DHCPV6_MAX_DOWNSTREAM]
```

相关声明：[downstream_ifaces](#ad66949eb34540dbe8808dc9aea9e6368)。

可选的下游接口索引（Downstream Interface Indices）。

## 56.2\_详细说明（Detailed Documentation）

<a id="a2549234454437b4316f863347236ef6c"></a>

### `downstream_count`

```c
uint8_t net_dhcpv6_params::downstream_count
```

downstream_ifaces中有效条目的数量。

<a id="ad66949eb34540dbe8808dc9aea9e6368"></a>

### `downstream_ifaces`

```c
int net_dhcpv6_params::downstream_ifaces[NET_DHCPV6_MAX_DOWNSTREAM]
```

可选的下游接口索引（Downstream Interface Indices）。

委派前缀（request_prefix）时，列表中的每个接口都会成为请求路由器（Requesting Router）的下游链路，见RFC 8415：从委派前缀中为每个接口划分不同的/64前缀，第N个条目得到第N个/64，并通过路由器通告（Router Advertisements）发布。需要CONFIG_NET_IPV6_ND_RA_TX。downstream_count为0表示仅在iface上安装委派前缀。

注意，委派前缀（Delegated Prefix）的长度必须足够短，以便为列表中的每个接口划分不同的/64。长度为L的委派最多支持2^(64 - L)个下游接口。无法分配不同/64前缀的接口会被跳过。

<a id="a4bc3655ee2a830879667cdb554883573"></a>

### `request_addr`

```c
bool net_dhcpv6_params::request_addr
```

请求IPv6地址（Address）。

<a id="afd290d92fcc5ae3bac9a9c7030910e6b"></a>

### `request_prefix`

```c
bool net_dhcpv6_params::request_prefix
```

请求IPv6前缀（Prefix）。

本数据类型文档由以下文件生成：

- `zephyr/net/dhcpv6.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/net/dhcpv6.h](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [RFC 8415](https://datatracker.ietf.org/doc/html/rfc8415)
- [CONFIG_NET_IPV6_ND_RA_TX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND_RA_TX)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_net_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_net_dhcpv6_server_params_结构体.md)
