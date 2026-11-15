---
id: learning.zephyr-docs.api-file-service-interface-reference.page-33
title: zephyr__net__lldp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_net\_\_lldp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

链路层发现协议（LLDP）的定义和处理程序。

<a id="details"></a>

```c
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
```

查看此文件的源码。

链路层发现协议（Link Layer Discovery Protocol，LLDP）的定义及处理程序。应用程序不应包含此文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_net_5Flldp_5Fchassis_5Ftlv"></a>

```c
struct net_lldp_chassis_tlv
```

相关声明：[net_lldp_chassis_tlv](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md)。

机箱ID类型-长度-值（Chassis ID TLV），见IEEE 802.1AB第8.5.2节。

<a id="r_net_5Flldp_5Fport_5Ftlv"></a>

```c
struct net_lldp_port_tlv
```

相关声明：[net_lldp_port_tlv](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md)。

端口ID类型-长度-值（Port ID TLV），见IEEE 802.1AB第8.5.3节。

<a id="r_net_5Flldp_5Ftime_5Fto_5Flive_5Ftlv"></a>

```c
struct net_lldp_time_to_live_tlv
```

相关声明：[net_lldp_time_to_live_tlv](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md)。

生存时间类型-长度-值（Time To Live TLV），见IEEE 802.1AB第8.5.4节。

<a id="r_net_5Flldpdu"></a>

```c
struct net_lldpdu
```

相关声明：[net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)。

按IEEE 802.1AB第8.2节“LLDPDU格式”的规定，链路层发现协议数据单元（LLDPDU）应按以下顺序包含类型-长度-值（TLV）项。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.2\_宏定义（Macros）

<a id="r_ga961bc59567ffa2d5a4d21290d1d78407"></a>

```c
#define net_lldp_set_lldpdu(iface)
```

相关声明：[net_lldp_set_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga961bc59567ffa2d5a4d21290d1d78407)。

为网络接口设置 LLDP 协议数据单元（LLDPDU）。

<a id="r_gafdd1b4cea9f560597c31a0e42d5341e0"></a>

```c
#define net_lldp_unset_lldpdu(iface)
```

相关声明：[net_lldp_unset_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gafdd1b4cea9f560597c31a0e42d5341e0)。

取消网络接口的 LLDP 协议数据单元（LLDPDU）设置。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 33.3\_类型定义（Typedefs）

<a id="r_ga1e9fb662d7cdfc3c4c68cfd0312987cf"></a>

```c
typedef enum net_verdict(* net_lldp_recv_cb_t) (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

LLDP 接收数据包回调（Receive Packet Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 33.4\_枚举（Enumerations）

<a id="r_gadd4273e4fe55757729008ce081771899"></a>

```c
enum net_lldp_tlv_type { LLDP_TLV_END_LLDPDU = 0 , LLDP_TLV_CHASSIS_ID = 1 , LLDP_TLV_PORT_ID = 2 , LLDP_TLV_TTL = 3 , LLDP_TLV_PORT_DESC = 4 , LLDP_TLV_SYSTEM_NAME = 5 , LLDP_TLV_SYSTEM_DESC = 6 , LLDP_TLV_SYSTEM_CAPABILITIES = 7 , LLDP_TLV_MANAGEMENT_ADDR = 8 , LLDP_TLV_ORG_SPECIFIC = 127 }
```

相关声明：[net_lldp_tlv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gadd4273e4fe55757729008ce081771899)、[LLDP_TLV_END_LLDPDU](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a)、[LLDP_TLV_CHASSIS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6)、[LLDP_TLV_PORT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45)、[LLDP_TLV_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c)、[LLDP_TLV_PORT_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0)、[LLDP_TLV_SYSTEM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9)、[LLDP_TLV_SYSTEM_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782)、[LLDP_TLV_SYSTEM_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521)、[LLDP_TLV_MANAGEMENT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5)、[LLDP_TLV_ORG_SPECIFIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad)。

类型－长度－值（TLV）类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.5\_函数（Functions）

<a id="r_ga0efa1813c537dcf02e021db60049c284"></a>

```c
int net_lldp_config (struct net_if *iface, const struct net_lldpdu *lldpdu)
```

相关声明：[net_lldp_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga0efa1813c537dcf02e021db60049c284)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)。

为网络接口设置 LLDP 数据单元（Data Unit）。

<a id="r_ga9702175375a71eaab20f450291cb51ad"></a>

```c
int net_lldp_config_optional (struct net_if *iface, const uint8_t *tlv, size_t len)
```

相关声明：[net_lldp_config_optional](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga9702175375a71eaab20f450291cb51ad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为网络接口设置可选 LLDP TLV。

<a id="r_ga61845c96c65d6df83f422a68e31162cf"></a>

```c
int net_lldp_register_callback (struct net_if *iface, net_lldp_recv_cb_t cb)
```

相关声明：[net_lldp_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga61845c96c65d6df83f422a68e31162cf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)。

注册 LLDP 接收（Rx）回调函数。


## 33.6\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [查看此文件的源码。](../api_source_network_reference/P012_lldp.h_源码浏览.md)
- [net_lldp_chassis_tlv](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md)
- [net_lldp_port_tlv](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md)
- [net_lldp_time_to_live_tlv](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md)
- [net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)
- [net_lldp_set_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga961bc59567ffa2d5a4d21290d1d78407)
- [net_lldp_unset_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gafdd1b4cea9f560597c31a0e42d5341e0)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_lldp_tlv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gadd4273e4fe55757729008ce081771899)
- [LLDP_TLV_END_LLDPDU](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a)
- [LLDP_TLV_CHASSIS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6)
- [LLDP_TLV_PORT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45)
- [LLDP_TLV_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c)
- [LLDP_TLV_PORT_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0)
- [LLDP_TLV_SYSTEM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9)
- [LLDP_TLV_SYSTEM_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782)
- [LLDP_TLV_SYSTEM_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521)
- [LLDP_TLV_MANAGEMENT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5)
- [LLDP_TLV_ORG_SPECIFIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad)
- [net_lldp_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga0efa1813c537dcf02e021db60049c284)
- [net_lldp_config_optional](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga9702175375a71eaab20f450291cb51ad)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_lldp_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga61845c96c65d6df83f422a68e31162cf)

<a id="header-details"></a>

---

[上一章](P032_zephyr__dt-bindings__sensor__lis2de12.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__lorawan__emul.h_文件参考.md)
