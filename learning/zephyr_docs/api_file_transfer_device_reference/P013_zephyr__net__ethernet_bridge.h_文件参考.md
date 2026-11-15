---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-13
title: zephyr__net__ethernet_bridge.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_net\_\_ethernet\_bridge.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网桥（Ethernet Bridge）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/sys/slist.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/ethernet.h>
```

查看此文件的源码。

以太网桥（Ethernet Bridge）公共头文件。以太网桥连接两个或更多以太网网络，并透明地将数据包从一个网络转发到其他网络，使它们看起来属于同一个网络。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.1\_类型定义（Typedefs）

<a id="r_gac7d0b995294279cc35408c69ee437778"></a>

```c
typedef void(* eth_bridge_cb_t) (struct eth_bridge_iface_context *br, void *user_data)
```

相关声明：[eth_bridge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gac7d0b995294279cc35408c69ee437778)。

遍历网桥实例（Bridge Instances）时使用的回调（Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.2\_函数（Functions）

<a id="r_ga19756a715b210181001b04987a5e23a5"></a>

```c
int eth_bridge_iface_add (struct net_if *br, struct net_if *iface)
```

相关声明：[eth_bridge_iface_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga19756a715b210181001b04987a5e23a5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将以太网网络接口（Ethernet Network Interface）加入网桥（Bridge）。

<a id="r_ga671496bc299581b8d4d3ec9fd2ff1991"></a>

```c
int eth_bridge_iface_remove (struct net_if *br, struct net_if *iface)
```

相关声明：[eth_bridge_iface_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga671496bc299581b8d4d3ec9fd2ff1991)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从网桥（Bridge）移除以太网网络接口（Ethernet Network Interface）。

<a id="r_gafd194ba73599d0e37c8302e25d8208e4"></a>

```c
int eth_bridge_get_index (struct net_if *br)
```

相关声明：[eth_bridge_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gafd194ba73599d0e37c8302e25d8208e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指针获取网桥索引（Bridge Index）。

<a id="r_ga6b88a47138b199e65da602e0e63f13d1"></a>

```c
struct net_if * eth_bridge_get_by_index (int index)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[eth_bridge_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga6b88a47138b199e65da602e0e63f13d1)。

根据索引获取网桥实例（Bridge Instance）。

<a id="r_ga5bb8dba7fbde9f2095e19f1912855d31"></a>

```c
void net_eth_bridge_foreach (eth_bridge_cb_t cb, void *user_data)
```

相关声明：[net_eth_bridge_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga5bb8dba7fbde9f2095e19f1912855d31)、[eth_bridge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gac7d0b995294279cc35408c69ee437778)。

遍历所有网桥上下文实例（Bridge Context Instances），获取它们的信息。

<a id="r_ga0f1b170bea388cce27253e757bd74cb0"></a>

```c
static bool net_eth_iface_is_bridged (struct ethernet_context *ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_iface_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga0f1b170bea388cce27253e757bd74cb0)。

检查接口（Interface）是否已加入网桥（Bridged）。

<a id="r_gad5ab9610d5c9401899a8c8fb257f7389"></a>

```c
static struct net_if * net_eth_get_bridge (struct ethernet_context *ctx)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gad5ab9610d5c9401899a8c8fb257f7389)。

获取网桥接口（Bridge Interface）。

<a id="r_gab48e819446f5a3753f3395dd30374bd3"></a>

```c
enum net_verdict eth_bridge_input_process (struct net_if *iface, struct net_pkt *pkt, struct net_if **dst_iface)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[eth_bridge_input_process](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gab48e819446f5a3753f3395dd30374bd3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

处理从网桥成员接口（Bridged Interface）接收到的数据包 `pkt`。


## 13.3\_原页交叉引用（Cross References）

- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/ethernet.h](../api_source_socket_ethernet_reference/P003_ethernet.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P006_ethernet_bridge.h_源码浏览.md)
- [eth_bridge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gac7d0b995294279cc35408c69ee437778)
- [eth_bridge_iface_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga19756a715b210181001b04987a5e23a5)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [eth_bridge_iface_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga671496bc299581b8d4d3ec9fd2ff1991)
- [eth_bridge_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gafd194ba73599d0e37c8302e25d8208e4)
- [eth_bridge_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga6b88a47138b199e65da602e0e63f13d1)
- [net_eth_bridge_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga5bb8dba7fbde9f2095e19f1912855d31)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_eth_iface_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga0f1b170bea388cce27253e757bd74cb0)
- [net_eth_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gad5ab9610d5c9401899a8c8fb257f7389)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [eth_bridge_input_process](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gab48e819446f5a3753f3395dd30374bd3)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>

---

[上一章](P012_zephyr__dsp__utils.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__dt-bindings__pinctrl__focaltech_ft9001_pinctrl.h_文件参考.md)
