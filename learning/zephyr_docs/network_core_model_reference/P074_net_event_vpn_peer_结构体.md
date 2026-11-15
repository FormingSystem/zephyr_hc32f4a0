---
id: learning.zephyr-docs.network-core-model-reference.page-74
title: net_event_vpn_peer_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__vpn__peer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_net\_event\_vpn\_peer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__vpn__peer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_VPN_PEER_ADD网络事件的信息。

```c
#include <zephyr/net/wireguard.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_VPN_PEER_ADD事件的信息。NET_EVENT_VPN_PEER_DEL事件只通过事件信息中的指针传递对端标识（Peer ID）。注意，指向对端信息的指针仅在事件处理期间有效，处理完成后不应继续使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_ab7b7c00b17c106a2f696401c1381de39"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#ab7b7c00b17c106a2f696401c1381de39)。

虚拟专用网络（VPN）的对端标识符。

<a id="r_a48c12bdfa2f09998fe24d586f70ed35a"></a>

```c
const char * public_key
```

相关声明：[public_key](#a48c12bdfa2f09998fe24d586f70ed35a)。

虚拟专用网络（VPN）的对端公钥。

<a id="r_a668c569513326c8d1a9e235afab0ce7e"></a>

```c
struct net_sockaddr * endpoint
```

相关声明：[net_sockaddr](P117_net_sockaddr_结构体.md)、[endpoint](#a668c569513326c8d1a9e235afab0ce7e)。

虚拟专用网络（VPN）的对端端点。

<a id="r_a94c46c495acd29cb29a0645da1dcd137"></a>

```c
struct wireguard_allowed_ip * allowed_ip [WIREGUARD_MAX_SRC_IPS+1]
```

相关声明：[wireguard_allowed_ip](https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__allowed__ip.html)、[allowed_ip](#a94c46c495acd29cb29a0645da1dcd137)。

虚拟专用网络（VPN）对端允许的IP地址，以空值终止的列表表示。

<a id="r_affc68879eae926cfcf6b5aaba745b62d"></a>

```c
int keepalive_interval
```

相关声明：[keepalive_interval](#affc68879eae926cfcf6b5aaba745b62d)。

虚拟专用网络（VPN）对端的保活间隔。

## 74.2\_详细说明（Detailed Documentation）

<a id="a94c46c495acd29cb29a0645da1dcd137"></a>

### `allowed_ip`

```c
struct wireguard_allowed_ip* net_event_vpn_peer::allowed_ip[WIREGUARD_MAX_SRC_IPS+1]
```

虚拟专用网络（VPN）对端允许的IP地址，以空值终止的列表表示。

<a id="a668c569513326c8d1a9e235afab0ce7e"></a>

### `endpoint`

```c
struct net_sockaddr* net_event_vpn_peer::endpoint
```

虚拟专用网络（VPN）的对端端点。

<a id="ab7b7c00b17c106a2f696401c1381de39"></a>

### `id`

```c
uint32_t net_event_vpn_peer::id
```

虚拟专用网络（VPN）的对端标识符。

<a id="affc68879eae926cfcf6b5aaba745b62d"></a>

### `keepalive_interval`

```c
int net_event_vpn_peer::keepalive_interval
```

虚拟专用网络（VPN）对端的保活间隔。

<a id="a48c12bdfa2f09998fe24d586f70ed35a"></a>

### `public_key`

```c
const char* net_event_vpn_peer::public_key
```

虚拟专用网络（VPN）的对端公钥。

本数据类型文档由以下文件生成：

- `zephyr/net/wireguard.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/net/wireguard.h](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [net_sockaddr](P117_net_sockaddr_结构体.md)
- [wireguard_allowed_ip](https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__allowed__ip.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_net_event_packet_mcast_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_net_icmp_ctx_结构体.md)
