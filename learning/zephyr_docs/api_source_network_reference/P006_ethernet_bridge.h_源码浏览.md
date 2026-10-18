---
id: learning.zephyr-docs.api-source-network-reference.page-6
title: ethernet_bridge.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_ethernet\_bridge.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h.html)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__eth__bridge_html_ga0f1b170bea388cce27253e757bd74cb0"></a>
<a id="agroup__eth__bridge_html_ga19756a715b210181001b04987a5e23a5"></a>
<a id="agroup__eth__bridge_html_ga5bb8dba7fbde9f2095e19f1912855d31"></a>
<a id="agroup__eth__bridge_html_ga671496bc299581b8d4d3ec9fd2ff1991"></a>
<a id="agroup__eth__bridge_html_ga6b88a47138b199e65da602e0e63f13d1"></a>
<a id="agroup__eth__bridge_html_gab48e819446f5a3753f3395dd30374bd3"></a>
<a id="agroup__eth__bridge_html_gac7d0b995294279cc35408c69ee437778"></a>
<a id="agroup__eth__bridge_html_gad5ab9610d5c9401899a8c8fb257f7389"></a>
<a id="agroup__eth__bridge_html_gafd194ba73599d0e37c8302e25d8208e4"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__if_html_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>
<a id="aslist_8h_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2021 BayLibre SAS
 * Copyright (c) 2024 Nordic Semiconductor
 * SPDX-FileCopyrightText: Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_H_
#define ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_H_

#include <zephyr/sys/slist.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/ethernet.h>

#ifdef __cplusplus
extern "C" {
#endif



#if defined(CONFIG_NET_ETHERNET_BRIDGE)
#define NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT CONFIG_NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT
#else
#define NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT 1
#endif

struct eth_bridge_iface_context {
        /* Lock to protect access to interface array below */
        struct k_mutex lock;

        /* The actual bridge virtual interface  */
        struct net_if *iface;

        /* What Ethernet interfaces are bridged together */
        struct net_if *eth_iface[NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT];

        /* How many interfaces are bridged atm */
        size_t count;

        /* Bridge instance id */
        int id;

        /* Has user configured the bridge */
        bool is_setup : 1;

        /* Is the interface enabled or not */
        bool status : 1;
};


int eth_bridge_iface_add(struct net_if *br, struct net_if *iface);

int eth_bridge_iface_remove(struct net_if *br, struct net_if *iface);

int eth_bridge_get_index(struct net_if *br);

struct net_if *eth_bridge_get_by_index(int index);

typedef void (*eth_bridge_cb_t)(struct eth_bridge_iface_context *br, void *user_data);

void net_eth_bridge_foreach(eth_bridge_cb_t cb, void *user_data);

static inline bool net_eth_iface_is_bridged(struct ethernet_context *ctx)
{
#if defined(CONFIG_NET_ETHERNET_BRIDGE)
        struct eth_bridge_iface_context *br_ctx;

        NET_ASSERT(ctx != NULL);

        if (ctx->bridge == NULL) {
                return false;
        }

        br_ctx = net_if_get_device(ctx->bridge)->data;
        if (br_ctx->is_setup) {
                return true;
        }
#endif
        return false;
}

static inline struct net_if *net_eth_get_bridge(struct ethernet_context *ctx)
{
#if defined(CONFIG_NET_ETHERNET_BRIDGE)
        NET_ASSERT(ctx != NULL);

        return ctx->bridge;
#else
        return NULL;
#endif
}

enum net_verdict eth_bridge_input_process(struct net_if *iface, struct net_pkt *pkt,
                                          struct net_if **dst_iface);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 9 行

版权（Copyright）：© 2021 BayLibre SAS。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 文件版权声明（FileCopyrightText）：Copyright 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

用于保护下方接口数组（Interface Array）访问的锁（Lock）。

### 注释 3：原第 49 行

实际的网桥虚拟接口（Bridge Virtual Interface）。

### 注释 4：原第 52 行

桥接在一起的以太网接口（Ethernet Interfaces）。

### 注释 5：原第 55 行

当前已桥接的接口数量（Number of Bridged Interfaces）。

### 注释 6：原第 58 行

网桥实例标识（Bridge Instance ID）。

### 注释 7：原第 61 行

用户是否已配置网桥（Bridge）。

### 注释 8：原第 64 行

接口（Interface）是否已启用。

### 注释 9：原第 202 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ETHERNET_BRIDGE_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__bridge_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [eth_bridge_iface_add](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga19756a715b210181001b04987a5e23a5)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [eth_bridge_iface_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga671496bc299581b8d4d3ec9fd2ff1991)
- [eth_bridge_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gafd194ba73599d0e37c8302e25d8208e4)
- [eth_bridge_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga6b88a47138b199e65da602e0e63f13d1)
- [eth_bridge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gac7d0b995294279cc35408c69ee437778)
- [net_eth_bridge_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga5bb8dba7fbde9f2095e19f1912855d31)
- [net_eth_iface_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#ga0f1b170bea388cce27253e757bd74cb0)
- [net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [net_eth_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gad5ab9610d5c9401899a8c8fb257f7389)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [eth_bridge_input_process](https://docs.zephyrproject.org/latest/doxygen/html/group__eth__bridge.html#gab48e819446f5a3753f3395dd30374bd3)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P005_em32_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_gpio_intc_stm32.h_源码浏览.md)
