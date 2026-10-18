---
id: learning.zephyr-docs.network-core-model-reference.page-68
title: net_event_ipv6_pe_filter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__pe__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_net\_event\_ipv6\_pe\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__pe__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PE_FILTER_ADD、NET_EVENT_IPV6_PE_FILTER_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PE_FILTER_ADD、NET_EVENT_IPV6_PE_FILTER_DEL等网络事件的信息。仅当CONFIG_NET_IPV6_PE_FILTER_PREFIX_COUNT大于0时可用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a20e3beb1a70c1ff4c4aabe95456df1e0"></a>

```c
struct net_in6_addr prefix
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[prefix](#a20e3beb1a70c1ff4c4aabe95456df1e0)。

隐私扩展过滤器（Privacy Extension Filter）的IPv6地址。

<a id="r_a07961a42f5ff8ca98615164192b8ca5a"></a>

```c
bool is_deny_list
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_deny_list](#a07961a42f5ff8ca98615164192b8ca5a)。

IPv6过滤器的拒绝或允许列表（Deny / Allow List）。

## 68.2\_详细说明（Detailed Documentation）

<a id="a07961a42f5ff8ca98615164192b8ca5a"></a>

### `is_deny_list`

```c
bool net_event_ipv6_pe_filter::is_deny_list
```

IPv6过滤器的拒绝或允许列表（Deny / Allow List）。

<a id="a20e3beb1a70c1ff4c4aabe95456df1e0"></a>

### `prefix`

```c
struct net_in6_addr net_event_ipv6_pe_filter::prefix
```

隐私扩展过滤器（Privacy Extension Filter）的IPv6地址。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_net_event_ipv6_nbr_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_net_event_ipv6_pmtu_info_结构体.md)
