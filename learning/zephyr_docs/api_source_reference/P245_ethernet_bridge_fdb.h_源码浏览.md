---
id: learning.zephyr-docs.api-source-reference.page-245
title: ethernet_bridge_fdb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第245章\_ethernet\_bridge\_fdb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h.html)。

## 245.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__eth__bridge__fdb_html_ga07fd9a5eb63ad632b0c8f50a4fff4c7f"></a>
<a id="agroup__eth__bridge__fdb_html_ga578cfd4c5902513e90f4d79f69c5168b"></a>
<a id="agroup__eth__bridge__fdb_html_gaa0ba43a9be49261a790c9a66472b983e"></a>
<a id="agroup__eth__bridge__fdb_html_gab865519cb3f906438d0e2e206841fba2"></a>
<a id="agroup__eth__bridge__fdb_html_gac0e8713bff16d35285e1889881d63260"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="anet__if_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructeth__bridge__fdb__entry_html"></a>
<a id="astructeth__bridge__fdb__entry_html_a75786def4d1d2c44e7b979e736632aa0"></a>
<a id="astructeth__bridge__fdb__entry_html_aa2c608aab6d594308bb4015876e56412"></a>
<a id="astructeth__bridge__fdb__entry_html_adc7c4c90b2ffd3de4603e6d0a57261c1"></a>
<a id="astructeth__bridge__fdb__entry_html_af6de371aa68f69e79903168f1e848641"></a>
<a id="astructnet__eth__addr_html"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_FDB_H_
#define ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_FDB_H_


#include <zephyr/net/net_if.h>
#include <zephyr/net/ethernet.h>

#ifdef __cplusplus
extern "C" {
#endif

#define ETHERNET_BRIDGE_FDB_FLAG_STATIC  BIT(0)
#define ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC BIT(1)

struct eth_bridge_fdb_entry {
        struct net_eth_addr mac;
        struct net_if *iface;
        uint8_t flags;
        sys_snode_t node;
};

int eth_bridge_fdb_add(struct net_eth_addr *mac, struct net_if *iface);

int eth_bridge_fdb_del(struct net_eth_addr *mac, struct net_if *iface);

int eth_bridge_fdb_del_iface(struct net_if *iface);

typedef void (*eth_bridge_fdb_entry_cb_t)(struct eth_bridge_fdb_entry *entry, void *user_data);

void eth_bridge_fdb_foreach(eth_bridge_fdb_entry_cb_t cb, void *user_data);


#endif /* ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_FDB_H_ */
```

## 245.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_FDB_H_`。

## 245.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [mac](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#aa2c608aab6d594308bb4015876e56412)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#af6de371aa68f69e79903168f1e848641)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#a75786def4d1d2c44e7b979e736632aa0)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#adc7c4c90b2ffd3de4603e6d0a57261c1)
- [eth_bridge_fdb_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gac0e8713bff16d35285e1889881d63260)
- [eth_bridge_fdb_del](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga578cfd4c5902513e90f4d79f69c5168b)
- [eth_bridge_fdb_del_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gaa0ba43a9be49261a790c9a66472b983e)
- [eth_bridge_fdb_entry_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)
- [eth_bridge_fdb_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gab865519cb3f906438d0e2e206841fba2)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [eth_bridge_fdb_entry::flags](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#a75786def4d1d2c44e7b979e736632aa0)
- [eth_bridge_fdb_entry::mac](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#aa2c608aab6d594308bb4015876e56412)
- [eth_bridge_fdb_entry::node](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#adc7c4c90b2ffd3de4603e6d0a57261c1)
- [eth_bridge_fdb_entry::iface](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md#af6de371aa68f69e79903168f1e848641)

---

[上一章](P244_eth_adin2111.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P246_ethernet_mgmt.h_源码浏览.md)
