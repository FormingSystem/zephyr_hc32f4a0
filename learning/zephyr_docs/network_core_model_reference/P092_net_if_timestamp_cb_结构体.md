---
id: learning.zephyr-docs.network-core-model-reference.page-92
title: net_if_timestamp_cb_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__timestamp__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_net\_if\_timestamp\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__timestamp__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

时间戳回调处理程序（Timestamp Callback Handler）的结构。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

时间戳回调处理结构（Timestamp callback handler struct）。保存时间戳回调信息。调用者必须确保所指向的变量在整个注册有效期（Lifetime of registration）内均有效；通常意味着该变量不能在栈（Stack）上分配。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_a0becd1b9eba3db5fd76280dc2e773773"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a0becd1b9eba3db5fd76280dc2e773773)。

单向链表（Slist）的节点信息（Node information）。

<a id="r_ad10186fe9652756a2f7d20d2f63777a9"></a>

```c
struct net_pkt * pkt
```

相关声明：[net_pkt](P114_net_pkt_结构体.md)、[pkt](#ad10186fe9652756a2f7d20d2f63777a9)。

需要此回调的数据包（Packet）。

<a id="r_aaf799f4b899d0e61430ccb549fd54c52"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#aaf799f4b899d0e61430ccb549fd54c52)。

需要此回调的网络接口（Network interface）。

<a id="r_ad2ee7e6572d59b849a758ead443bc0ac"></a>

```c
net_if_timestamp_callback_t cb
```

相关声明：[net_if_timestamp_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga656c2ba47d280aa1c47bc2d062debbfa)、[cb](#ad2ee7e6572d59b849a758ead443bc0ac)。

时间戳回调（Timestamp callback）。

## 92.2\_详细说明（Detailed Documentation）

<a id="ad2ee7e6572d59b849a758ead443bc0ac"></a>

### `cb`

```c
net_if_timestamp_callback_t net_if_timestamp_cb::cb
```

时间戳回调（Timestamp callback）。

<a id="aaf799f4b899d0e61430ccb549fd54c52"></a>

### `iface`

```c
struct net_if* net_if_timestamp_cb::iface
```

需要此回调的网络接口（Network interface）。

值为 `NULL` 时表示所有接口（All interfaces）。

<a id="a0becd1b9eba3db5fd76280dc2e773773"></a>

### `node`

```c
sys_snode_t net_if_timestamp_cb::node
```

单向链表（Slist）的节点信息（Node information）。

<a id="ad10186fe9652756a2f7d20d2f63777a9"></a>

### `pkt`

```c
struct net_pkt* net_if_timestamp_cb::pkt
```

需要此回调的数据包（Packet）。

值为 `NULL` 时表示所有数据包（All packets）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_pkt](P114_net_pkt_结构体.md)
- [net_if](P079_net_if_结构体.md)
- [net_if_timestamp_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga656c2ba47d280aa1c47bc2d062debbfa)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_net_if_router_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_net_ifreq_结构体.md)
