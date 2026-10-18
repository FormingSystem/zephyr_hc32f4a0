---
id: learning.zephyr-docs.network-core-model-reference.page-64
title: net_event_ipv4_pmtu_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv4__pmtu__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_net\_event\_ipv4\_pmtu\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__ipv4__pmtu__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_PMTU_CHANGED网络事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_PMTU_CHANGED网络事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_aea25f385ece879bfc624f2d54f42d219"></a>

```c
struct net_in_addr dst
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[dst](#aea25f385ece879bfc624f2d54f42d219)。

IPv4地址（Address）。

<a id="r_ae4f6951aed4253428a7ac4273b8b43fe"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#ae4f6951aed4253428a7ac4273b8b43fe)。

新的最大传输单元（MTU）。

## 64.2\_详细说明（Detailed Documentation）

<a id="aea25f385ece879bfc624f2d54f42d219"></a>

### `dst`

```c
struct net_in_addr net_event_ipv4_pmtu_info::dst
```

IPv4地址（Address）。

<a id="ae4f6951aed4253428a7ac4273b8b43fe"></a>

### `mtu`

```c
uint16_t net_event_ipv4_pmtu_info::mtu
```

新的最大传输单元（MTU）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [net_in_addr](P096_net_in_addr_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_net_event_coap_service_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_net_event_ipv4_route_结构体.md)
