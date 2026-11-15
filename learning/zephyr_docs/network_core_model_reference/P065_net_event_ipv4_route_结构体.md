---
id: learning.zephyr-docs.network-core-model-reference.page-65
title: net_event_ipv4_route_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv4__route.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_net\_event\_ipv4\_route\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv4__route.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_ROUTE_ADD、NET_EVENT_IPV4_ROUTE_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_ROUTE_ADD、NET_EVENT_IPV4_ROUTE_DEL等网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a1b4cf425bb860b6a2b210ce49969218b"></a>

```c
struct net_in_addr nexthop
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[nexthop](#a1b4cf425bb860b6a2b210ce49969218b)。

下一跳（Next Hop）的IPv4地址。

<a id="r_afe30f770f0776d0116bb737a7130ce0f"></a>

```c
struct net_in_addr addr
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[addr](#afe30f770f0776d0116bb737a7130ce0f)。

路由（Route）的IPv4地址或前缀。

<a id="r_a6db2fd490100464f4085202cbd30acc2"></a>

```c
uint8_t prefix_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prefix_len](#a6db2fd490100464f4085202cbd30acc2)。

IPv4前缀长度（Prefix Length）。

## 65.2\_详细说明（Detailed Documentation）

<a id="afe30f770f0776d0116bb737a7130ce0f"></a>

### `addr`

```c
struct net_in_addr net_event_ipv4_route::addr
```

路由（Route）的IPv4地址或前缀。

<a id="a1b4cf425bb860b6a2b210ce49969218b"></a>

### `nexthop`

```c
struct net_in_addr net_event_ipv4_route::nexthop
```

下一跳（Next Hop）的IPv4地址。

<a id="a6db2fd490100464f4085202cbd30acc2"></a>

### `prefix_len`

```c
uint8_t net_event_ipv4_route::prefix_len
```

IPv4前缀长度（Prefix Length）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in_addr](P096_net_in_addr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_net_event_ipv4_pmtu_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_net_event_ipv6_addr_结构体.md)
