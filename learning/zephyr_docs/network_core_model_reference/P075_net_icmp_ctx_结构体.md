---
id: learning.zephyr-docs.network-core-model-reference.page-75
title: net_icmp_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_net\_icmp\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网控制消息协议（ICMP）的上下文结构。

```c
#include <zephyr/net/icmp.h>
```

<a id="details"></a>

互联网控制消息协议（ICMP）的上下文结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_a792d11b7dc74b0c064e5471f385028e5"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a792d11b7dc74b0c064e5471f385028e5)。

列表节点（List Node）。

<a id="r_a9da78845a12a69a359087607e11f7e72"></a>

```c
net_icmp_handler_t handler
```

相关声明：[net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)、[handler](#a9da78845a12a69a359087607e11f7e72)。

互联网控制消息协议（ICMP）的响应处理程序。

<a id="r_a88e1f3dc6118366f37ff5a110fff4b08"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#a88e1f3dc6118366f37ff5a110fff4b08)。

发送ICMP请求所用的网络接口（Network Interface）。

<a id="r_a2a718521d0b8c6de45c39fc8b45e47cf"></a>

```c
void * user_data
```

相关声明：[user_data](#a2a718521d0b8c6de45c39fc8b45e47cf)。

用户提供的不透明数据（Opaque Data）。

<a id="r_a2701c104e363538adfffdf1c15fd21d7"></a>

```c
uint8_t family
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[family](#a2701c104e363538adfffdf1c15fd21d7)。

为处理程序注册的地址族（Address Family）。

<a id="r_ae7ccf9c7bbcc89d656d20e9486cf7df5"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#ae7ccf9c7bbcc89d656d20e9486cf7df5)。

正在等待的响应的ICMP类型（Type）。

<a id="r_a8eaa061d7ade479523cfdbcb465f76b2"></a>

```c
uint8_t code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[code](#a8eaa061d7ade479523cfdbcb465f76b2)。

正在等待的响应类型对应的ICMP代码（Code）。

## 75.2\_详细说明（Detailed Documentation）

<a id="a8eaa061d7ade479523cfdbcb465f76b2"></a>

### `code`

```c
uint8_t net_icmp_ctx::code
```

正在等待的响应类型对应的ICMP代码（Code）。

<a id="a2701c104e363538adfffdf1c15fd21d7"></a>

### `family`

```c
uint8_t net_icmp_ctx::family
```

为处理程序注册的地址族（Address Family）。

<a id="a9da78845a12a69a359087607e11f7e72"></a>

### `handler`

```c
net_icmp_handler_t net_icmp_ctx::handler
```

互联网控制消息协议（ICMP）的响应处理程序。

<a id="a88e1f3dc6118366f37ff5a110fff4b08"></a>

### `iface`

```c
struct net_if* net_icmp_ctx::iface
```

发送ICMP请求所用的网络接口（Network Interface）。

<a id="a792d11b7dc74b0c064e5471f385028e5"></a>

### `node`

```c
sys_snode_t net_icmp_ctx::node
```

列表节点（List Node）。

<a id="ae7ccf9c7bbcc89d656d20e9486cf7df5"></a>

### `type`

```c
uint8_t net_icmp_ctx::type
```

正在等待的响应的ICMP类型（Type）。

<a id="a2a718521d0b8c6de45c39fc8b45e47cf"></a>

### `user_data`

```c
void* net_icmp_ctx::user_data
```

用户提供的不透明数据（Opaque Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/icmp.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/net/icmp.h](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)
- [net_if](P079_net_if_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_net_event_vpn_peer_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_net_icmp_ip_hdr_结构体.md)
