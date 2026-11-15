---
id: learning.zephyr-docs.network-core-model-reference.page-101
title: net_iptable_rule_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__iptable__rule__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_net\_iptable\_rule\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__iptable__rule__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

定义iptable规则（Rule）的参数。

```c
#include <zephyr/net/ipv4_nat.h>
```

<a id="details"></a>

定义 iptable 规则的参数（Parameters to define an iptable rule）。由表规则管理 API 使用，用于指定匹配条件（Matching criteria）、输入／输出接口、协议和超时值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_ac731d0a60bd96a930deafa1179d14134"></a>

```c
int input_iface_idx
```

相关声明：[input_iface_idx](#ac731d0a60bd96a930deafa1179d14134)。

输入接口索引（Input interface index）。

<a id="r_ac69afcdae871894e60eb33b11d993f78"></a>

```c
int output_iface_idx
```

相关声明：[output_iface_idx](#ac69afcdae871894e60eb33b11d993f78)。

输出接口索引（Output interface index）。

<a id="r_a66c8ccc605a0844014afeab2c5d337e8"></a>

```c
uint8_t src [NET_IPV4_ADDR_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src](#a66c8ccc605a0844014afeab2c5d337e8)、[NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)。

源 IPv4 地址（Source IPv4 address）。

<a id="r_a4a47dc1f59a6a06e81e7919d3c65e2a3"></a>

```c
uint8_t src_mask [NET_IPV4_ADDR_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_mask](#a4a47dc1f59a6a06e81e7919d3c65e2a3)、[NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)。

源 IPv4 掩码（Source IPv4 mask）。

<a id="r_ab7c1391be324c39af5b20d5d74b9af57"></a>

```c
uint8_t dst [NET_IPV4_ADDR_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dst](#ab7c1391be324c39af5b20d5d74b9af57)、[NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)。

目的 IPv4 地址（Destination IPv4 address）。

<a id="r_a026951fdc60b664ac2351db32772ae83"></a>

```c
uint8_t dst_mask [NET_IPV4_ADDR_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dst_mask](#a026951fdc60b664ac2351db32772ae83)、[NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)。

目的 IPv4 掩码（Destination IPv4 mask）。

<a id="r_ad172d5e9ed919528b2198d60d32fa1be"></a>

```c
enum net_ip_protocol proto
```

相关声明：[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[proto](#ad172d5e9ed919528b2198d60d32fa1be)。

协议编号（Protocol number），例如 `IPPROTO_TCP`、`IPPROTO_UDP`。

<a id="r_a39657345b8fefd0343a66739a0375288"></a>

```c
uint8_t priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[priority](#a39657345b8fefd0343a66739a0375288)。

规则的匹配优先级（Match priority），数值越大，优先级越高。

<a id="r_a8ba3da2a023d05bd305ce2d9733fe12e"></a>

```c
int unreply_timeout
```

相关声明：[unreply_timeout](#a8ba3da2a023d05bd305ce2d9733fe12e)。

未收到回复时的超时值（Unreplied timeout），单位为秒；`0` 表示使用默认值，`-1` 表示永不过期。

<a id="r_ab031a8d36a7779cb39b53e9b469233cc"></a>

```c
int reply_timeout
```

相关声明：[reply_timeout](#ab031a8d36a7779cb39b53e9b469233cc)。

收到回复后的超时值（Replied timeout），单位为秒；`0` 表示使用默认值，`-1` 表示永不过期。

## 101.2\_详细说明（Detailed Documentation）

<a id="ab7c1391be324c39af5b20d5d74b9af57"></a>

### `dst`

```c
uint8_t net_iptable_rule_params::dst[NET_IPV4_ADDR_SIZE]
```

目的 IPv4 地址（Destination IPv4 address）。

<a id="a026951fdc60b664ac2351db32772ae83"></a>

### `dst_mask`

```c
uint8_t net_iptable_rule_params::dst_mask[NET_IPV4_ADDR_SIZE]
```

目的 IPv4 掩码（Destination IPv4 mask）。

<a id="ac731d0a60bd96a930deafa1179d14134"></a>

### `input_iface_idx`

```c
int net_iptable_rule_params::input_iface_idx
```

输入接口索引（Input interface index）。

<a id="ac69afcdae871894e60eb33b11d993f78"></a>

### `output_iface_idx`

```c
int net_iptable_rule_params::output_iface_idx
```

输出接口索引（Output interface index）。

<a id="a39657345b8fefd0343a66739a0375288"></a>

### `priority`

```c
uint8_t net_iptable_rule_params::priority
```

规则的匹配优先级（Match priority），数值越大，优先级越高。

<a id="ad172d5e9ed919528b2198d60d32fa1be"></a>

### `proto`

```c
enum net_ip_protocol net_iptable_rule_params::proto
```

协议编号（Protocol number），例如 `IPPROTO_TCP`、`IPPROTO_UDP`。

<a id="ab031a8d36a7779cb39b53e9b469233cc"></a>

### `reply_timeout`

```c
int net_iptable_rule_params::reply_timeout
```

收到回复后的超时值（Replied timeout），单位为秒；`0` 表示使用默认值，`-1` 表示永不过期。

<a id="a66c8ccc605a0844014afeab2c5d337e8"></a>

### `src`

```c
uint8_t net_iptable_rule_params::src[NET_IPV4_ADDR_SIZE]
```

源 IPv4 地址（Source IPv4 address）。

<a id="a4a47dc1f59a6a06e81e7919d3c65e2a3"></a>

### `src_mask`

```c
uint8_t net_iptable_rule_params::src_mask[NET_IPV4_ADDR_SIZE]
```

源 IPv4 掩码（Source IPv4 mask）。

<a id="a8ba3da2a023d05bd305ce2d9733fe12e"></a>

### `unreply_timeout`

```c
int net_iptable_rule_params::unreply_timeout
```

未收到回复时的超时值（Unreplied timeout），单位为秒；`0` 表示使用默认值，`-1` 表示永不过期。

本数据类型文档由以下文件生成：

- `zephyr/net/ipv4_nat.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/net/ipv4_nat.h](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_net_ip_mreqn_结构体.md) · [返回大纲](大纲.md) · [下一章](P102_net_ipv6_mreq_结构体.md)
