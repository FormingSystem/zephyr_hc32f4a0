---
id: learning.zephyr-docs.network-core-model-reference.page-89
title: net_if_mcast_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__mcast__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_net\_if\_mcast\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__mcast__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口的组播IP地址（Multicast IP Addresses）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络接口多播 IP 地址（Network Interface multicast IP addresses）。保存分配给此网络接口的多播 IP 地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_a3e470fc2eb02ac9e5d3d7d0bea0aaa69"></a>

```c
struct net_addr address
```

相关声明：[address](#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)。

IP 地址（IP address）。

<a id="r_a89e15d11cf1d5ff07b86cfd44e45d7e3"></a>

```c
atomic_t atomic_ref
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[atomic_ref](#a89e15d11cf1d5ff07b86cfd44e45d7e3)。

引用计数器。

<a id="r_a74db1527b3a2b614509cc43fdf7d09ef"></a>

```c
sys_snode_t rejoin_node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[rejoin_node](#a74db1527b3a2b614509cc43fdf7d09ef)。

重新加入多播组的链表节点（Rejoining multicast groups list node）。

<a id="r_abab3e6dba72e24ef522c033d277369ca"></a>

```c
uint8_t is_used: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_used](#abab3e6dba72e24ef522c033d277369ca)。

此多播 IP 地址是否正在使用（In use）。

<a id="r_a4af9009b2f9ccc0589a9ba6dac10927b"></a>

```c
uint8_t is_joined: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_joined](#a4af9009b2f9ccc0589a9ba6dac10927b)。

是否已加入此多播组（Multicast group）。

## 89.2\_详细说明（Detailed Documentation）

<a id="a3e470fc2eb02ac9e5d3d7d0bea0aaa69"></a>

### `address`

```c
struct net_addr net_if_mcast_addr::address
```

IP 地址（IP address）。

<a id="a89e15d11cf1d5ff07b86cfd44e45d7e3"></a>

### `atomic_ref`

```c
atomic_t net_if_mcast_addr::atomic_ref
```

引用计数器。

用于跟踪各子系统（Subsystems）加入和退出多播组的情况。

<a id="a4af9009b2f9ccc0589a9ba6dac10927b"></a>

### `is_joined`

```c
uint8_t net_if_mcast_addr::is_joined
```

是否已加入此多播组（Multicast group）。

<a id="abab3e6dba72e24ef522c033d277369ca"></a>

### `is_used`

```c
uint8_t net_if_mcast_addr::is_used
```

此多播 IP 地址是否正在使用（In use）。

<a id="a74db1527b3a2b614509cc43fdf7d09ef"></a>

### `rejoin_node`

```c
sys_snode_t net_if_mcast_addr::rejoin_node
```

重新加入多播组的链表节点（Rejoining multicast groups list node）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_net_if_link_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_net_if_mcast_monitor_结构体.md)
