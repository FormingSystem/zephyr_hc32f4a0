---
id: learning.zephyr-docs.api-source-reference.page-410
title: ipv4_nat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第410章\_ipv4\_nat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h.html)。

## 410.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="agroup__ip__4__6_html_ga10a82ea9ba9ca19f3b773bdd53c978e0"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__nat_html_ga2732dba0a704fbb4fc2b75ee7e455271"></a>
<a id="agroup__nat_html_ga83c32791968479d187622f931764b201"></a>
<a id="agroup__nat_html_gaddb6f51b57a9bd5522ba82784577cc21"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__iptable__rule__params_html"></a>
<a id="astructnet__iptable__rule__params_html_a026951fdc60b664ac2351db32772ae83"></a>
<a id="astructnet__iptable__rule__params_html_a39657345b8fefd0343a66739a0375288"></a>
<a id="astructnet__iptable__rule__params_html_a4a47dc1f59a6a06e81e7919d3c65e2a3"></a>
<a id="astructnet__iptable__rule__params_html_a66c8ccc605a0844014afeab2c5d337e8"></a>
<a id="astructnet__iptable__rule__params_html_a8ba3da2a023d05bd305ce2d9733fe12e"></a>
<a id="astructnet__iptable__rule__params_html_ab031a8d36a7779cb39b53e9b469233cc"></a>
<a id="astructnet__iptable__rule__params_html_ab7c1391be324c39af5b20d5d74b9af57"></a>
<a id="astructnet__iptable__rule__params_html_ac69afcdae871894e60eb33b11d993f78"></a>
<a id="astructnet__iptable__rule__params_html_ac731d0a60bd96a930deafa1179d14134"></a>
<a id="astructnet__iptable__rule__params_html_ad172d5e9ed919528b2198d60d32fa1be"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IPV4_NAT_H_
#define ZEPHYR_INCLUDE_NET_IPV4_NAT_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>

#include <zephyr/net/net_core.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>

#ifdef __cplusplus
extern "C" {
#endif

struct net_iptable_rule_params {
        int input_iface_idx;
        int output_iface_idx;
        uint8_t src[NET_IPV4_ADDR_SIZE];
        uint8_t src_mask[NET_IPV4_ADDR_SIZE];
        uint8_t dst[NET_IPV4_ADDR_SIZE];
        uint8_t dst_mask[NET_IPV4_ADDR_SIZE];
        enum net_ip_protocol proto;
        uint8_t priority;
        int unreply_timeout;
        int reply_timeout;
};

int net_ipv4_table_rule_add(struct net_iptable_rule_params *param);

void net_ipv4_table_rule_del(int idx);

void net_ipv4_nat_init(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_IPV4_NAT_H_ */
```

## 410.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IPV4_NAT_H_`。

## 410.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)
- [input_iface_idx](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ac731d0a60bd96a930deafa1179d14134)
- [output_iface_idx](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ac69afcdae871894e60eb33b11d993f78)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [src](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a66c8ccc605a0844014afeab2c5d337e8)
- [NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)
- [src_mask](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a4a47dc1f59a6a06e81e7919d3c65e2a3)
- [dst](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ab7c1391be324c39af5b20d5d74b9af57)
- [dst_mask](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a026951fdc60b664ac2351db32772ae83)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [proto](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ad172d5e9ed919528b2198d60d32fa1be)
- [priority](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a39657345b8fefd0343a66739a0375288)
- [unreply_timeout](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a8ba3da2a023d05bd305ce2d9733fe12e)
- [reply_timeout](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ab031a8d36a7779cb39b53e9b469233cc)
- [net_ipv4_table_rule_add](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga83c32791968479d187622f931764b201)
- [net_ipv4_table_rule_del](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga2732dba0a704fbb4fc2b75ee7e455271)
- [net_ipv4_nat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#gaddb6f51b57a9bd5522ba82784577cc21)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_iptable_rule_params::dst_mask](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a026951fdc60b664ac2351db32772ae83)
- [net_iptable_rule_params::priority](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a39657345b8fefd0343a66739a0375288)
- [net_iptable_rule_params::src_mask](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a4a47dc1f59a6a06e81e7919d3c65e2a3)
- [net_iptable_rule_params::src](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a66c8ccc605a0844014afeab2c5d337e8)
- [net_iptable_rule_params::unreply_timeout](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#a8ba3da2a023d05bd305ce2d9733fe12e)
- [net_iptable_rule_params::reply_timeout](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ab031a8d36a7779cb39b53e9b469233cc)
- [net_iptable_rule_params::dst](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ab7c1391be324c39af5b20d5d74b9af57)
- [net_iptable_rule_params::output_iface_idx](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ac69afcdae871894e60eb33b11d993f78)
- [net_iptable_rule_params::input_iface_idx](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ac731d0a60bd96a930deafa1179d14134)
- [net_iptable_rule_params::proto](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md#ad172d5e9ed919528b2198d60d32fa1be)

---

[上一章](P409_ipv4_autoconf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P411_irq_nextlevel.h_源码浏览.md)
