---
id: learning.zephyr-docs.network-core-model-reference.page-61
title: net_eth_mcast_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mcast__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_net\_eth\_mcast\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mcast__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口的第二层组播地址（L2 Multicast Address）。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

网络接口的第二层组播地址（L2 Multicast Address）。保存接口监听的链路层组播地址，以及已加入该地址的用户数量。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a5c7f1a2351a493681525a5c610389e15"></a>

```c
struct net_eth_addr addr
```

相关声明：[net_eth_addr](P059_net_eth_addr_结构体.md)、[addr](#a5c7f1a2351a493681525a5c610389e15)。

组播MAC地址（Multicast MAC Address）。

<a id="r_af8dec139bae61ede5a2233ab0f3c66a4"></a>

```c
atomic_t atomic_ref
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[atomic_ref](#af8dec139bae61ede5a2233ab0f3c66a4)。

引用计数器。

<a id="r_ab8a4a73276b5236befb1ac34a379f689"></a>

```c
uint8_t is_used: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_used](#ab8a4a73276b5236befb1ac34a379f689)。

此地址是否正在使用。

## 61.2\_详细说明（Detailed Documentation）

<a id="a5c7f1a2351a493681525a5c610389e15"></a>

### `addr`

```c
struct net_eth_addr net_eth_mcast_addr::addr
```

组播MAC地址（Multicast MAC Address）。

<a id="af8dec139bae61ede5a2233ab0f3c66a4"></a>

### `atomic_ref`

```c
atomic_t net_eth_mcast_addr::atomic_ref
```

引用计数器。

用于跟踪IP层和数据包套接字（Packet Sockets）的组播组加入与离开。

<a id="ab8a4a73276b5236befb1ac34a379f689"></a>

### `is_used`

```c
uint8_t net_eth_mcast_addr::is_used
```

此地址是否正在使用。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [net_eth_addr](P059_net_eth_addr_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_net_eth_mac_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_net_event_coap_observer_结构体.md)
