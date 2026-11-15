---
id: learning.zephyr-docs.network-core-model-reference.page-66
title: net_event_ipv6_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_net\_event\_ipv6\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv6__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ADDR_ADD、NET_EVENT_IPV6_ADDR_DEL、NET_EVENT_IPV6_MADDR_ADD、NET_EVENT_IPV6_MADDR_DEL等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ADDR_ADD、NET_EVENT_IPV6_ADDR_DEL、NET_EVENT_IPV6_MADDR_ADD、NET_EVENT_IPV6_MADDR_DEL等网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a2a4cbf602f98c30fd7cd5d024c569115"></a>

```c
struct net_in6_addr addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[addr](#a2a4cbf602f98c30fd7cd5d024c569115)。

与此事件相关的IPv6地址。

## 66.2\_详细说明（Detailed Documentation）

<a id="a2a4cbf602f98c30fd7cd5d024c569115"></a>

### `addr`

```c
struct net_in6_addr net_event_ipv6_addr::addr
```

与此事件相关的IPv6地址。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_net_event_ipv4_route_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_net_event_ipv6_nbr_结构体.md)
