---
id: learning.zephyr-docs.network-core-model-reference.page-69
title: net_event_ipv6_pmtu_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__pmtu__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_net\_event\_ipv6\_pmtu\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__pmtu__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PMTU_CHANGED网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PMTU_CHANGED网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a5614582b5a0c361355c29abaf1045b62"></a>

```c
struct net_in6_addr dst
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[dst](#a5614582b5a0c361355c29abaf1045b62)。

IPv6地址（Address）。

<a id="r_a52e5078e0f39cb5e95d4e5bc42674480"></a>

```c
uint32_t mtu
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mtu](#a52e5078e0f39cb5e95d4e5bc42674480)。

新的最大传输单元（MTU）。

## 69.2\_详细说明（Detailed Documentation）

<a id="a5614582b5a0c361355c29abaf1045b62"></a>

### `dst`

```c
struct net_in6_addr net_event_ipv6_pmtu_info::dst
```

IPv6地址（Address）。

<a id="a52e5078e0f39cb5e95d4e5bc42674480"></a>

### `mtu`

```c
uint32_t net_event_ipv6_pmtu_info::mtu
```

新的最大传输单元（MTU）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_net_event_ipv6_pe_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_net_event_ipv6_prefix_结构体.md)
