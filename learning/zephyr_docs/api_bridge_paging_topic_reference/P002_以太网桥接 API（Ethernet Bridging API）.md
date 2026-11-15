---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-2
title: 以太网桥接 API（Ethernet Bridging API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_以太网桥接 API（Ethernet Bridging API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网桥接 API（Ethernet Bridging API）

<a id="details"></a>

以太网桥接（Ethernet Bridging）API。自 2.7 起提供，版本 0.8.0。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.1\_类型定义（Typedefs）

<a id="r_gac7d0b995294279cc35408c69ee437778"></a>

```c
typedef void(* eth_bridge_cb_t) (struct eth_bridge_iface_context *br, void *user_data)
```

相关声明：[eth_bridge_cb_t](#gac7d0b995294279cc35408c69ee437778)。

遍历网桥实例（Bridge Instances）时使用的回调（Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga19756a715b210181001b04987a5e23a5"></a>

```c
int eth_bridge_iface_add (struct net_if *br, struct net_if *iface)
```

相关声明：[eth_bridge_iface_add](#ga19756a715b210181001b04987a5e23a5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将以太网网络接口（Ethernet Network Interface）加入网桥（Bridge）。

<a id="r_ga671496bc299581b8d4d3ec9fd2ff1991"></a>

```c
int eth_bridge_iface_remove (struct net_if *br, struct net_if *iface)
```

相关声明：[eth_bridge_iface_remove](#ga671496bc299581b8d4d3ec9fd2ff1991)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从网桥（Bridge）移除以太网网络接口（Ethernet Network Interface）。

<a id="r_gafd194ba73599d0e37c8302e25d8208e4"></a>

```c
int eth_bridge_get_index (struct net_if *br)
```

相关声明：[eth_bridge_get_index](#gafd194ba73599d0e37c8302e25d8208e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指针获取网桥索引（Bridge Index）。

<a id="r_ga6b88a47138b199e65da602e0e63f13d1"></a>

```c
struct net_if * eth_bridge_get_by_index (int index)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[eth_bridge_get_by_index](#ga6b88a47138b199e65da602e0e63f13d1)。

根据索引获取网桥实例（Bridge Instance）。

<a id="r_ga5bb8dba7fbde9f2095e19f1912855d31"></a>

```c
void net_eth_bridge_foreach (eth_bridge_cb_t cb, void *user_data)
```

相关声明：[net_eth_bridge_foreach](#ga5bb8dba7fbde9f2095e19f1912855d31)、[eth_bridge_cb_t](#gac7d0b995294279cc35408c69ee437778)。

遍历所有网桥上下文实例（Bridge Context Instances），获取它们的信息。

<a id="r_ga0f1b170bea388cce27253e757bd74cb0"></a>

```c
static bool net_eth_iface_is_bridged (struct ethernet_context *ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_iface_is_bridged](#ga0f1b170bea388cce27253e757bd74cb0)。

检查接口（Interface）是否已加入网桥（Bridged）。

<a id="r_gad5ab9610d5c9401899a8c8fb257f7389"></a>

```c
static struct net_if * net_eth_get_bridge (struct ethernet_context *ctx)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_bridge](#gad5ab9610d5c9401899a8c8fb257f7389)。

获取网桥接口（Bridge Interface）。

<a id="r_gab48e819446f5a3753f3395dd30374bd3"></a>

```c
enum net_verdict eth_bridge_input_process (struct net_if *iface, struct net_pkt *pkt, struct net_if **dst_iface)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[eth_bridge_input_process](#gab48e819446f5a3753f3395dd30374bd3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

处理从网桥成员接口（Bridged Interface）接收到的数据包 `pkt`。

## 2.3\_详细说明（Detailed Documentation）

<a id="gac7d0b995294279cc35408c69ee437778"></a>

### `eth_bridge_cb_t`

```c
typedef void(* eth_bridge_cb_t) (struct eth_bridge_iface_context *br, void *user_data)
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

遍历网桥实例（Bridge Instances）时使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `br` | 指向网桥上下文实例（Bridge Context Instance）的指针。 |
| `user_data` | 用户提供的数据（User Supplied Data）。 |

<a id="ga6b88a47138b199e65da602e0e63f13d1"></a>

### `eth_bridge_get_by_index()`

```c
struct net_if * eth_bridge_get_by_index ( int index)
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

根据索引获取网桥实例（Bridge Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网桥实例索引（Bridge Instance Index）。 |

**返回（Returns）**：返回值：指向网桥接口（Bridge Interface）的指针；若未找到则返回 `NULL`。

<a id="gafd194ba73599d0e37c8302e25d8208e4"></a>

### `eth_bridge_get_index()`

```c
int eth_bridge_get_index ( struct net_if * br)
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

根据指针获取网桥索引（Bridge Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `br` | 指向网桥实例（Bridge Instance）的指针。 |

**返回（Returns）**：返回值：网桥索引（Bridge Index）。

<a id="ga19756a715b210181001b04987a5e23a5"></a>

### `eth_bridge_iface_add()`

```c
int eth_bridge_iface_add ( struct net_if * br, struct net_if * iface )
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

将以太网网络接口（Ethernet Network Interface）加入网桥（Bridge）。

将网络接口（Network Interface）加入网桥（Bridge），随后该接口会进入混杂模式（Promiscuous Mode）。向网桥接口添加两个或更多以太网接口后，网桥接口的设置即完成。设置完成后，可以启用网桥接口，使其开始桥接二层流量（L2 Traffic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `br` | 指向网桥接口（Bridge Interface）的指针。 |
| `iface` | 要添加的接口（Interface）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码（Negative Error Code）。

<a id="ga671496bc299581b8d4d3ec9fd2ff1991"></a>

### `eth_bridge_iface_remove()`

```c
int eth_bridge_iface_remove ( struct net_if * br, struct net_if * iface )
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

从网桥（Bridge）移除以太网网络接口（Ethernet Network Interface）。

若调用后网桥接口中仅剩一个以太网接口，则网桥会被禁用，因为它已无法桥接二层流量（L2 Traffic）。在这种情况下，网桥接口仍保持 `UP` 状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `br` | 指向网桥接口（Bridge Interface）的指针。 |
| `iface` | 要移除的接口（Interface）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码（Negative Error Code）。

<a id="gab48e819446f5a3753f3395dd30374bd3"></a>

### `eth_bridge_input_process()`

```c
enum net_verdict eth_bridge_input_process ( struct net_if * iface, struct net_pkt * pkt, struct net_if ** dst_iface )
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

处理从网桥成员接口（Bridged Interface）接收到的数据包 `pkt`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向已桥接接口（Bridged Interface）的指针。 |
| `pkt` | 指向数据包 `pkt` 的指针。 |
| `dst_iface` | 指向目标接口指针（Destination Interface Pointer）的指针。 |

**返回（Returns）**：返回值：`net_verdict` 网络处理判定。

<a id="ga5bb8dba7fbde9f2095e19f1912855d31"></a>

### `net_eth_bridge_foreach()`

```c
void net_eth_bridge_foreach ( eth_bridge_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/ethernet_bridge.h>
```

遍历所有网桥上下文实例（Bridge Context Instances），获取它们的信息。

这主要用于网络 Shell（net-shell）中，打印当前活动网桥的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 为每个网桥实例调用的回调函数（Callback）。 |
| `user_data` | 用户提供的数据（User Supplied Data）。 |

<a id="gad5ab9610d5c9401899a8c8fb257f7389"></a>

### `net_eth_get_bridge()`

```c
struct net_if * net_eth_get_bridge ( struct ethernet_context * ctx)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_bridge.h>
```

获取网桥接口（Bridge Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向 `ethernet_context` 以太网上下文的指针。 |

**返回（Returns）**：返回值：指向网桥接口（Bridge Interface）的指针，或 `NULL`。

<a id="ga0f1b170bea388cce27253e757bd74cb0"></a>

### `net_eth_iface_is_bridged()`

```c
bool net_eth_iface_is_bridged ( struct ethernet_context * ctx)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_bridge.h>
```

检查接口（Interface）是否已加入网桥（Bridged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向 `ethernet_context` 以太网上下文的指针。 |

**返回（Returns）**：返回值：已桥接时返回 `true`，否则返回 `false`。


## 2.4\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [zephyr/net/ethernet_bridge.h](../api_file_transfer_device_reference/P013_zephyr__net__ethernet_bridge.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_微芯（Microchip）PIC32CM PL.md) · [返回大纲](大纲.md) · [下一章](P003_GNSS 驱动后端 API（Driver Backend API）.md)
