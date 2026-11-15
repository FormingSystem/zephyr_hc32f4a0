---
id: learning.zephyr-docs.network-service-model-reference.page-5
title: dsa_tag_register_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdsa__tag__register.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_dsa\_tag\_register\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__tag__register.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DSA标签协议（Tag Protocol）的注册信息。

```c
#include <zephyr/net/dsa_tag.h>
```

<a id="details"></a>

DSA标签协议（Tag Protocol）的注册信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a96f1ec63a5e0d1f11df75b3c1732fcad"></a>

```c
int proto
```

相关声明：[proto](#a96f1ec63a5e0d1f11df75b3c1732fcad)。

协议 ID（Protocol ID）。

<a id="r_ab20724506cf4311dd76e8aa176a48f63"></a>

```c
struct net_if *(* recv )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[recv](#ab20724506cf4311dd76e8aa176a48f63)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

接收数据包处理函数。

<a id="r_abcb6234153f855969d957fd9c6934e48"></a>

```c
struct net_pkt *(* xmit )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[xmit](#abcb6234153f855969d957fd9c6934e48)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

发送数据包处理函数。

## 5.2\_详细说明（Detailed Documentation）

<a id="a96f1ec63a5e0d1f11df75b3c1732fcad"></a>

### `proto`

```c
int dsa_tag_register::proto
```

协议 ID（Protocol ID）。

<a id="ab20724506cf4311dd76e8aa176a48f63"></a>

### `recv`

```c
struct net_if *(* dsa_tag_register::recv) (struct net_if *iface, struct net_pkt *pkt)
```

接收数据包处理函数。

<a id="abcb6234153f855969d957fd9c6934e48"></a>

### `xmit`

```c
struct net_pkt *(* dsa_tag_register::xmit) (struct net_if *iface, struct net_pkt *pkt)
```

发送数据包处理函数。

本数据类型文档由以下文件生成：

- `zephyr/net/dsa_tag.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/net/dsa_tag.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_dsa_switch_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_eth_bridge_fdb_entry_结构体.md)
