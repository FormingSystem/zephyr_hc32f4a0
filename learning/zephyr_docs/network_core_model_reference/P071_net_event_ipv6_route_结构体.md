---
id: learning.zephyr-docs.network-core-model-reference.page-71
title: net_event_ipv6_route_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__route.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_net\_event\_ipv6\_route\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__route.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ROUTE_ADD、NET_EVENT_IPV6_ROUTE_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ROUTE_ADD、NET_EVENT_IPV6_ROUTE_DEL等网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_af9498993cb46796e1d2f150a49bfb067"></a>

```c
struct net_in6_addr nexthop
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[nexthop](#af9498993cb46796e1d2f150a49bfb067)。

下一跳（Next Hop）的IPv6地址。

<a id="r_ae47c91ba21747f56b6e3ee0bd5ec199f"></a>

```c
struct net_in6_addr addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[addr](#ae47c91ba21747f56b6e3ee0bd5ec199f)。

路由（Route）的IPv6地址或前缀。

<a id="r_aa1f21f6963befb3f94183d02c6d2d23f"></a>

```c
uint8_t prefix_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prefix_len](#aa1f21f6963befb3f94183d02c6d2d23f)。

IPv6前缀长度（Prefix Length）。

## 71.2\_详细说明（Detailed Documentation）

<a id="ae47c91ba21747f56b6e3ee0bd5ec199f"></a>

### `addr`

```c
struct net_in6_addr net_event_ipv6_route::addr
```

路由（Route）的IPv6地址或前缀。

<a id="af9498993cb46796e1d2f150a49bfb067"></a>

### `nexthop`

```c
struct net_in6_addr net_event_ipv6_route::nexthop
```

下一跳（Next Hop）的IPv6地址。

<a id="aa1f21f6963befb3f94183d02c6d2d23f"></a>

### `prefix_len`

```c
uint8_t net_event_ipv6_route::prefix_len
```

IPv6前缀长度（Prefix Length）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_net_event_ipv6_prefix_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_net_event_l4_hostname_结构体.md)
