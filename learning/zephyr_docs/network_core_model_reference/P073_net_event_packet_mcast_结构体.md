---
id: learning.zephyr-docs.network-core-model-reference.page-73
title: net_event_packet_mcast_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__packet__mcast.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_net\_event\_packet\_mcast\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__packet__mcast.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD、NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP等网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD、NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP等网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a381a3493e2ca457eb5dda2516193e280"></a>

```c
struct net_linkaddr addr
```

相关声明：[net_linkaddr](P105_net_linkaddr_结构体.md)、[addr](#a381a3493e2ca457eb5dda2516193e280)。

该组的第二层组播地址（L2 Multicast Address）。

<a id="r_ade122db0aa2fb8b72064da6dc3e4afe7"></a>

```c
uint16_t type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[type](#ade122db0aa2fb8b72064da6dc3e4afe7)。

组播过滤类型（Multicast Filtering Type），取NET_PACKET_MR_*中的一个值。

## 73.2\_详细说明（Detailed Documentation）

<a id="a381a3493e2ca457eb5dda2516193e280"></a>

### `addr`

```c
struct net_linkaddr net_event_packet_mcast::addr
```

该组的第二层组播地址（L2 Multicast Address）。

<a id="ade122db0aa2fb8b72064da6dc3e4afe7"></a>

### `type`

```c
uint16_t net_event_packet_mcast::type
```

组播过滤类型（Multicast Filtering Type），取NET_PACKET_MR_*中的一个值。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_linkaddr](P105_net_linkaddr_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_net_event_l4_hostname_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_net_event_vpn_peer_结构体.md)
