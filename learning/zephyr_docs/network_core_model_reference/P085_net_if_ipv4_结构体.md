---
id: learning.zephyr-docs.network-core-model-reference.page-85
title: net_if_ipv4_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_net\_if\_ipv4\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv4.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4配置（Configuration）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

IPv4配置（Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_a806cf92123452ed3aa93540803b0a8d3"></a>

```c
struct net_if_addr_ipv4 unicast [NET_IF_MAX_IPV4_ADDR]
```

相关声明：[net_if_addr_ipv4](P081_net_if_addr_ipv4_结构体.md)、[unicast](#a806cf92123452ed3aa93540803b0a8d3)。

单播 IP 地址（Unicast IP addresses）。

<a id="r_adfaf5b50255bd35297195a7218729ae7"></a>

```c
struct net_if_mcast_addr mcast [NET_IF_MAX_IPV4_MADDR]
```

相关声明：[net_if_mcast_addr](P089_net_if_mcast_addr_结构体.md)、[mcast](#adfaf5b50255bd35297195a7218729ae7)。

多播 IP 地址（Multicast IP addresses）。

<a id="r_a87e23014c88bc5f2987174ca79011a1d"></a>

```c
struct net_in_addr gw
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[gw](#a87e23014c88bc5f2987174ca79011a1d)。

网关（Gateway）。

<a id="r_acdc6d5d6eb5362f4f6d2c027cc40e684"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#acdc6d5d6eb5362f4f6d2c027cc40e684)。

IPv4 生存时间（Time-to-live，TTL）。

<a id="r_a7e9bf16d51989cfcfe564f4f0a43b480"></a>

```c
uint8_t mcast_ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcast_ttl](#a7e9bf16d51989cfcfe564f4f0a43b480)。

多播数据包的 IPv4 生存时间（Time-to-live，TTL）。

## 85.2\_详细说明（Detailed Documentation）

<a id="a87e23014c88bc5f2987174ca79011a1d"></a>

### `gw`

```c
struct net_in_addr net_if_ipv4::gw
```

网关（Gateway）。

<a id="adfaf5b50255bd35297195a7218729ae7"></a>

### `mcast`

```c
struct net_if_mcast_addr net_if_ipv4::mcast[NET_IF_MAX_IPV4_MADDR]
```

多播 IP 地址（Multicast IP addresses）。

<a id="a7e9bf16d51989cfcfe564f4f0a43b480"></a>

### `mcast_ttl`

```c
uint8_t net_if_ipv4::mcast_ttl
```

多播数据包的 IPv4 生存时间（Time-to-live，TTL）。

<a id="acdc6d5d6eb5362f4f6d2c027cc40e684"></a>

### `ttl`

```c
uint8_t net_if_ipv4::ttl
```

IPv4 生存时间（Time-to-live，TTL）。

<a id="a806cf92123452ed3aa93540803b0a8d3"></a>

### `unicast`

```c
struct net_if_addr_ipv4 net_if_ipv4::unicast[NET_IF_MAX_IPV4_ADDR]
```

单播 IP 地址（Unicast IP addresses）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [net_if_addr_ipv4](P081_net_if_addr_ipv4_结构体.md)
- [net_if_mcast_addr](P089_net_if_mcast_addr_结构体.md)
- [net_in_addr](P096_net_in_addr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_net_if_ip_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_net_if_ipv6_结构体.md)
