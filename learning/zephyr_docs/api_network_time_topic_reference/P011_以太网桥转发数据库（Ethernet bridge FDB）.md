---
id: learning.zephyr-docs.api-network-time-topic-reference.page-11
title: 以太网桥转发数据库（Ethernet bridge FDB）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_以太网桥转发数据库（Ethernet bridge FDB）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge__fdb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网桥转发数据库（FDB）的定义。

<a id="details"></a>

以太网桥转发数据库（Ethernet bridge FDB）的定义。自 Zephyr 4.4 起提供；API 版本为 0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_eth_5Fbridge_5Ffdb_5Fentry"></a>

```c
struct eth_bridge_fdb_entry
```

相关声明：[eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)。

转发数据库（FDB）的条目结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ga674966c222582d7ab9b1eaec9e1317b8"></a>

```c
#define ETHERNET_BRIDGE_FDB_FLAG_STATIC BIT(0)
```

相关声明：[ETHERNET_BRIDGE_FDB_FLAG_STATIC](#ga674966c222582d7ab9b1eaec9e1317b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

转发数据库（FDB）条目标志（entry flags）。

<a id="r_ga29bbd35f32e5de29f057a309c3ab1fd9"></a>

```c
#define ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC BIT(1)
```

相关声明：[ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC](#ga29bbd35f32e5de29f057a309c3ab1fd9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

动态条目（dynamic entry），通过学习得到。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.3\_类型定义（Typedefs）

<a id="r_ga07fd9a5eb63ad632b0c8f50a4fff4c7f"></a>

```c
typedef void(* eth_bridge_fdb_entry_cb_t) (struct eth_bridge_fdb_entry *entry, void *user_data)
```

相关声明：[eth_bridge_fdb_entry_cb_t](#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)、[eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)。

用于遍历 FDB 条目的回调函数类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_gac0e8713bff16d35285e1889881d63260"></a>

```c
int eth_bridge_fdb_add (struct net_eth_addr *mac, struct net_if *iface)
```

相关声明：[eth_bridge_fdb_add](#gac0e8713bff16d35285e1889881d63260)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

添加静态 FDB 条目。

<a id="r_ga578cfd4c5902513e90f4d79f69c5168b"></a>

```c
int eth_bridge_fdb_del (struct net_eth_addr *mac, struct net_if *iface)
```

相关声明：[eth_bridge_fdb_del](#ga578cfd4c5902513e90f4d79f69c5168b)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

删除 FDB 条目。

<a id="r_gaa0ba43a9be49261a790c9a66472b983e"></a>

```c
int eth_bridge_fdb_del_iface (struct net_if *iface)
```

相关声明：[eth_bridge_fdb_del_iface](#gaa0ba43a9be49261a790c9a66472b983e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

删除某接口上的 FDB 条目。

<a id="r_gab865519cb3f906438d0e2e206841fba2"></a>

```c
void eth_bridge_fdb_foreach (eth_bridge_fdb_entry_cb_t cb, void *user_data)
```

相关声明：[eth_bridge_fdb_foreach](#gab865519cb3f906438d0e2e206841fba2)、[eth_bridge_fdb_entry_cb_t](#ga07fd9a5eb63ad632b0c8f50a4fff4c7f)。

遍历 FDB 表中的所有条目。

## 11.5\_详细说明（Detailed Documentation）

<a id="ga29bbd35f32e5de29f057a309c3ab1fd9"></a>

### `ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC`

```c
#define ETHERNET_BRIDGE_FDB_FLAG_DYNAMIC BIT(1)
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

动态条目（dynamic entry），通过学习得到。

<a id="ga674966c222582d7ab9b1eaec9e1317b8"></a>

### `ETHERNET_BRIDGE_FDB_FLAG_STATIC`

```c
#define ETHERNET_BRIDGE_FDB_FLAG_STATIC BIT(0)
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

转发数据库（FDB）条目标志（entry flags）。

静态条目（static entry），由人工添加。

<a id="ga07fd9a5eb63ad632b0c8f50a4fff4c7f"></a>

### `eth_bridge_fdb_entry_cb_t`

```c
typedef void(* eth_bridge_fdb_entry_cb_t) (struct eth_bridge_fdb_entry *entry, void *user_data)
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

用于遍历 FDB 条目的回调函数类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `entry` | 指向当前正在处理的 FDB 条目的指针。 |
| `user_data` | 由 foreach 遍历函数传入的用户自定义数据。 |

<a id="gac0e8713bff16d35285e1889881d63260"></a>

### `eth_bridge_fdb_add()`

```c
int eth_bridge_fdb_add ( struct net_eth_addr * mac, struct net_if * iface )
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

添加静态 FDB 条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mac` | 介质访问控制地址（MAC address）。 |
| `iface` | 接口（Interface）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga578cfd4c5902513e90f4d79f69c5168b"></a>

### `eth_bridge_fdb_del()`

```c
int eth_bridge_fdb_del ( struct net_eth_addr * mac, struct net_if * iface )
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

删除 FDB 条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mac` | 介质访问控制地址（MAC address）。 |
| `iface` | 接口；为 `NULL` 时从任意接口删除。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaa0ba43a9be49261a790c9a66472b983e"></a>

### `eth_bridge_fdb_del_iface()`

```c
int eth_bridge_fdb_del_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

删除某接口上的 FDB 条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接口；为 `NULL` 时从任意接口删除。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gab865519cb3f906438d0e2e206841fba2"></a>

### `eth_bridge_fdb_foreach()`

```c
void eth_bridge_fdb_foreach ( eth_bridge_fdb_entry_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/ethernet_bridge_fdb.h>
```

遍历 FDB 表中的所有条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 对每个 FDB 条目调用的回调函数。 |
| `user_data` | 每次调用回调时传入的用户自定义数据指针。 |


## 11.6\_原页交叉引用（Cross References）

- [eth_bridge_fdb_entry](../network_service_model_reference/P006_eth_bridge_fdb_entry_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/ethernet_bridge_fdb.h](../api_file_system_device_reference/P012_zephyr__net__ethernet_bridge_fdb.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_eSPI SAF 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P012_EPORTRSTR 复位控制（Reset Control）.md)
