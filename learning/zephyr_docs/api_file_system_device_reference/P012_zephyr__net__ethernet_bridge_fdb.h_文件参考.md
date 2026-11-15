---
id: learning.zephyr-docs.api-file-system-device-reference.page-12
title: zephyr__net__ethernet_bridge_fdb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_net\_\_ethernet\_bridge\_fdb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge__fdb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网桥转发数据库（FDB）的定义。

<a id="details"></a>

```c
#include <zephyr/net/net_if.h>
#include <zephyr/net/ethernet.h>
```

查看此文件的源码。

以太网桥转发数据库（FDB）的定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_eth_5Fbridge_5Ffdb_5Fentry"></a>

```c
struct eth_bridge_fdb_entry
```

相关声明：[eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)。

转发数据库（FDB）的条目结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_ga674966c222582d7ab9b1eaec9e1317b8"></a>

```c
#define ETHERNET_BRIDGE_FDB_FLAG_STATIC BIT(0)
```

相关声明：[ETHERNET_BRIDGE_FDB_FLAG_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga674966c222582d7ab9b1eaec9e1317b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

转发数据库（FDB）条目标志（entry flags）。

<a id="r_ga29bbd35f32e5de29f057a309c3ab1fd9"></a>

```c
#define ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC BIT(1)
```

相关声明：[ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga29bbd35f32e5de29f057a309c3ab1fd9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

动态条目（dynamic entry），通过学习得到。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga07fd9a5eb63ad632b0c8f50a4fff4c7f"></a>

```c
typedef void(* eth_bridge_fdb_entry_cb_t) (struct eth_bridge_fdb_entry *entry, void *user_data)
```

相关声明：[eth_bridge_fdb_entry_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)、[eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)。

用于遍历 FDB 条目的回调函数类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_gac0e8713bff16d35285e1889881d63260"></a>

```c
int eth_bridge_fdb_add (struct net_eth_addr *mac, struct net_if *iface)
```

相关声明：[eth_bridge_fdb_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gac0e8713bff16d35285e1889881d63260)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

添加静态 FDB 条目。

<a id="r_ga578cfd4c5902513e90f4d79f69c5168b"></a>

```c
int eth_bridge_fdb_del (struct net_eth_addr *mac, struct net_if *iface)
```

相关声明：[eth_bridge_fdb_del](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga578cfd4c5902513e90f4d79f69c5168b)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

删除 FDB 条目。

<a id="r_gaa0ba43a9be49261a790c9a66472b983e"></a>

```c
int eth_bridge_fdb_del_iface (struct net_if *iface)
```

相关声明：[eth_bridge_fdb_del_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gaa0ba43a9be49261a790c9a66472b983e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

删除某接口上的 FDB 条目。

<a id="r_gab865519cb3f906438d0e2e206841fba2"></a>

```c
void eth_bridge_fdb_foreach (eth_bridge_fdb_entry_cb_t cb, void *user_data)
```

相关声明：[eth_bridge_fdb_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gab865519cb3f906438d0e2e206841fba2)、[eth_bridge_fdb_entry_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)。

遍历 FDB 表中的所有条目。


## 12.5\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P245_ethernet_bridge_fdb.h_源码浏览.md)
- [eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)
- [ETHERNET_BRIDGE_FDB_FLAG_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga674966c222582d7ab9b1eaec9e1317b8)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga29bbd35f32e5de29f057a309c3ab1fd9)
- [eth_bridge_fdb_entry_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)
- [eth_bridge_fdb_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gac0e8713bff16d35285e1889881d63260)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [eth_bridge_fdb_del](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#ga578cfd4c5902513e90f4d79f69c5168b)
- [eth_bridge_fdb_del_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gaa0ba43a9be49261a790c9a66472b983e)
- [eth_bridge_fdb_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html#gab865519cb3f906438d0e2e206841fba2)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__display__ed2208-gca.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__i3c__ibi.h_文件参考.md)
