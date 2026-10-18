---
id: learning.zephyr-docs.network-service-model-reference.page-6
title: eth_bridge_fdb_entry_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structeth__bridge__fdb__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_eth\_bridge\_fdb\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structeth__bridge__fdb__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

转发数据库（FDB）的条目结构。

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

<a id="details"></a>

转发数据库（FDB）的条目结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_aa2c608aab6d594308bb4015876e56412"></a>

```c
struct net_eth_addr mac
```

相关声明：[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[mac](#aa2c608aab6d594308bb4015876e56412)。

介质访问控制地址（MAC address）。

<a id="r_af6de371aa68f69e79903168f1e848641"></a>

```c
struct net_if * iface
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface](#af6de371aa68f69e79903168f1e848641)。

接口（Interface）。

<a id="r_a75786def4d1d2c44e7b979e736632aa0"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a75786def4d1d2c44e7b979e736632aa0)。

条目标志。

<a id="r_adc7c4c90b2ffd3de4603e6d0a57261c1"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#adc7c4c90b2ffd3de4603e6d0a57261c1)。

链表节点（Linked list node）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a75786def4d1d2c44e7b979e736632aa0"></a>

### `flags`

```c
uint8_t eth_bridge_fdb_entry::flags
```

条目标志。

<a id="af6de371aa68f69e79903168f1e848641"></a>

### `iface`

```c
struct net_if* eth_bridge_fdb_entry::iface
```

接口（Interface）。

<a id="aa2c608aab6d594308bb4015876e56412"></a>

### `mac`

```c
struct net_eth_addr eth_bridge_fdb_entry::mac
```

介质访问控制地址（MAC address）。

<a id="adc7c4c90b2ffd3de4603e6d0a57261c1"></a>

### `node`

```c
sys_snode_t eth_bridge_fdb_entry::node
```

链表节点（Linked list node）。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet_bridge_fdb.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet_bridge_fdb.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h_source.html)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_dsa_tag_register_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_ethernet_api_结构体.md)
