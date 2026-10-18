---
id: learning.zephyr-docs.network-core-model-reference.page-70
title: net_event_ipv6_prefix_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__prefix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_net\_event\_ipv6\_prefix\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__prefix.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PREFIX_ADD、NET_EVENT_IPV6_PREFIX_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PREFIX_ADD、NET_EVENT_IPV6_PREFIX_DEL等网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_ada864bb20887133a472363a5f66208ee"></a>

```c
struct net_in6_addr addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[addr](#ada864bb20887133a472363a5f66208ee)。

IPv6前缀（Prefix）。

<a id="r_a3d70216e13fc0f78e08eb27f34fe8ace"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a3d70216e13fc0f78e08eb27f34fe8ace)。

IPv6前缀长度（Prefix Length）。

<a id="r_a6d7b0323896e43a04931ece4daaa09c4"></a>

```c
uint32_t lifetime
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[lifetime](#a6d7b0323896e43a04931ece4daaa09c4)。

IPv6前缀生存期（Prefix Lifetime），单位为秒。

## 70.2\_详细说明（Detailed Documentation）

<a id="ada864bb20887133a472363a5f66208ee"></a>

### `addr`

```c
struct net_in6_addr net_event_ipv6_prefix::addr
```

IPv6前缀（Prefix）。

<a id="a3d70216e13fc0f78e08eb27f34fe8ace"></a>

### `len`

```c
uint8_t net_event_ipv6_prefix::len
```

IPv6前缀长度（Prefix Length）。

<a id="a6d7b0323896e43a04931ece4daaa09c4"></a>

### `lifetime`

```c
uint32_t net_event_ipv6_prefix::lifetime
```

IPv6前缀生存期（Prefix Lifetime），单位为秒。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_net_event_ipv6_pmtu_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_net_event_ipv6_route_结构体.md)
