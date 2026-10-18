---
id: learning.zephyr-docs.network-core-model-reference.page-90
title: net_if_mcast_monitor_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__mcast__monitor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_net\_if\_mcast\_monitor\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__mcast__monitor.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组播监测处理程序（Multicast Monitor Handler）的结构。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

多播监视器处理结构（Multicast monitor handler struct）。保存多播回调信息。调用者必须确保所指向的变量在整个注册有效期（Lifetime of registration）内均有效；通常意味着该变量不能在栈（Stack）上分配。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_a570b7d8a8a5fabca83982a5f7d1d896a"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a570b7d8a8a5fabca83982a5f7d1d896a)。

单向链表（Slist）的节点信息（Node information）。

<a id="r_af4d0e937b2b9161918a13a0d6723c60a"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#af4d0e937b2b9161918a13a0d6723c60a)。

网络接口（Network Interface）

<a id="r_aec441b858a5f6792ac9cdbc625f6babe"></a>

```c
net_if_mcast_callback_t cb
```

相关声明：[net_if_mcast_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0d64291573740a67eae7ff3fcc0910c5)、[cb](#aec441b858a5f6792ac9cdbc625f6babe)。

多播回调（Multicast callback）。

## 90.2\_详细说明（Detailed Documentation）

<a id="aec441b858a5f6792ac9cdbc625f6babe"></a>

### `cb`

```c
net_if_mcast_callback_t net_if_mcast_monitor::cb
```

多播回调（Multicast callback）。

<a id="af4d0e937b2b9161918a13a0d6723c60a"></a>

### `iface`

```c
struct net_if* net_if_mcast_monitor::iface
```

网络接口（Network Interface）

<a id="a570b7d8a8a5fabca83982a5f7d1d896a"></a>

### `node`

```c
sys_snode_t net_if_mcast_monitor::node
```

单向链表（Slist）的节点信息（Node information）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_if](P079_net_if_结构体.md)
- [net_if_mcast_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0d64291573740a67eae7ff3fcc0910c5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_net_if_mcast_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_net_if_router_结构体.md)
