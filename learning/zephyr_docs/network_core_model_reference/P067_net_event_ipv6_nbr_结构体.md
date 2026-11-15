---
id: learning.zephyr-docs.network-core-model-reference.page-67
title: net_event_ipv6_nbr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__nbr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_net\_event\_ipv6\_nbr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__nbr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_NBR_ADD、NET_EVENT_IPV6_NBR_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_NBR_ADD、NET_EVENT_IPV6_NBR_DEL等网络事件的信息。注意：对于NET_EVENT_IPV6_NBR_DEL事件，idx为-1。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_ae18f586f643f893d71ab25921eb3ccb3"></a>

```c
struct net_in6_addr addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[addr](#ae18f586f643f893d71ab25921eb3ccb3)。

邻居IPv6地址（Neighbor IPv6 Address）。

<a id="r_adeb139ad70e794d1a805315ffd1fcbee"></a>

```c
int idx
```

相关声明：[idx](#adeb139ad70e794d1a805315ffd1fcbee)。

邻居在缓存中的索引（Neighbor Index）。

## 67.2\_详细说明（Detailed Documentation）

<a id="ae18f586f643f893d71ab25921eb3ccb3"></a>

### `addr`

```c
struct net_in6_addr net_event_ipv6_nbr::addr
```

邻居IPv6地址（Neighbor IPv6 Address）。

<a id="adeb139ad70e794d1a805315ffd1fcbee"></a>

### `idx`

```c
int net_event_ipv6_nbr::idx
```

邻居在缓存中的索引（Neighbor Index）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_net_event_ipv6_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_net_event_ipv6_pe_filter_结构体.md)
