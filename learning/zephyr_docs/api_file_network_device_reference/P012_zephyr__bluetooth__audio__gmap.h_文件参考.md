---
id: learning.zephyr-docs.api-file-network-device-reference.page-12
title: zephyr__bluetooth__audio__gmap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_bluetooth\_\_audio\_\_gmap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙游戏音频配置文件（Gaming Audio Profile，GMAP）的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙游戏音频配置文件（Gaming Audio Profile，GMAP）的头文件。版权（Copyright）：© 2023–2024 Nordic Semiconductor ASA。SPDX 许可证标识（License Identifier）：`Apache-2.0`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_bt_5Fgmap_5Ffeat"></a>

```c
struct bt_gmap_feat
```

相关声明：[bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)。

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

<a id="r_bt_5Fgmap_5Fcb"></a>

```c
struct bt_gmap_cb
```

相关声明：[bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)。

游戏音频配置文件（Gaming Audio Profile，GMAP）的回调结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.2\_枚举（Enumerations）

<a id="r_ga55ecab78bcd6de6c294abdc20ad10e56"></a>

```c
enum bt_gmap_role { BT_GMAP_ROLE_UGG = (1UL << (0U)) , BT_GMAP_ROLE_UGT = (1UL << (1U)) , BT_GMAP_ROLE_BGS = (1UL << (2U)) , BT_GMAP_ROLE_BGR = (1UL << (3U)) }
```

相关声明：[bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)、[BT_GMAP_ROLE_UGG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251)、[BT_GMAP_ROLE_UGT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b)、[BT_GMAP_ROLE_BGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6)、[BT_GMAP_ROLE_BGR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091)。

游戏角色位域（Gaming Role Bitfield）。

<a id="r_ga3ef43378bad84bbcd726e318cf0bc145"></a>

```c
enum bt_gmap_ugg_feat { BT_GMAP_UGG_FEAT_MULTIPLEX = (1UL << (0U)) , BT_GMAP_UGG_FEAT_96KBPS_SOURCE = (1UL << (1U)) , BT_GMAP_UGG_FEAT_MULTISINK = (1UL << (2U)) }
```

相关声明：[bt_gmap_ugg_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3ef43378bad84bbcd726e318cf0bc145)、[BT_GMAP_UGG_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e)、[BT_GMAP_UGG_FEAT_96KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331)、[BT_GMAP_UGG_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1)。

单播游戏网关特性位域（Unicast Game Gateway Feature Bitfield）。

<a id="r_ga0fe87d6d1412c15564ba7de29e3d7a48"></a>

```c
enum bt_gmap_ugt_feat { BT_GMAP_UGT_FEAT_SOURCE = (1UL << (0U)) , BT_GMAP_UGT_FEAT_80KBPS_SOURCE = (1UL << (1U)) , BT_GMAP_UGT_FEAT_SINK = (1UL << (2U)) , BT_GMAP_UGT_FEAT_64KBPS_SINK = (1UL << (3U)) , BT_GMAP_UGT_FEAT_MULTIPLEX = (1UL << (4U)) , BT_GMAP_UGT_FEAT_MULTISINK = (1UL << (5U)) , BT_GMAP_UGT_FEAT_MULTISOURCE = (1UL << (6U)) }
```

相关声明：[bt_gmap_ugt_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga0fe87d6d1412c15564ba7de29e3d7a48)、[BT_GMAP_UGT_FEAT_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231)、[BT_GMAP_UGT_FEAT_80KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88)、[BT_GMAP_UGT_FEAT_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c)、[BT_GMAP_UGT_FEAT_64KBPS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604)、[BT_GMAP_UGT_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e)、[BT_GMAP_UGT_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08)、[BT_GMAP_UGT_FEAT_MULTISOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045)。

单播游戏终端特性位域（Unicast Game Terminal Feature Bitfield）。

<a id="r_ga3a79c408b283864616a522b1f04cacaf"></a>

```c
enum bt_gmap_bgs_feat { BT_GMAP_BGS_FEAT_96KBPS = (1UL << (0U)) }
```

相关声明：[bt_gmap_bgs_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3a79c408b283864616a522b1f04cacaf)、[BT_GMAP_BGS_FEAT_96KBPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8)。

广播游戏发送端特性位域（Broadcast Game Sender Feature Bitfield）。

<a id="r_ga9c1145ad5334e14d4978b6d7d3c84b6c"></a>

```c
enum bt_gmap_bgr_feat { BT_GMAP_BGR_FEAT_MULTISINK = (1UL << (0U)) , BT_GMAP_BGR_FEAT_MULTIPLEX = (1UL << (1U)) }
```

相关声明：[bt_gmap_bgr_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga9c1145ad5334e14d4978b6d7d3c84b6c)、[BT_GMAP_BGR_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630)、[BT_GMAP_BGR_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6)。

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_gacc4853bf69d0a13353fc941aa7e4e190"></a>

```c
int bt_gmap_cb_register (const struct bt_gmap_cb *cb)
```

相关声明：[bt_gmap_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gacc4853bf69d0a13353fc941aa7e4e190)、[bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)。

注册游戏音频配置文件（Gaming Audio Profile）使用的回调。

<a id="r_gab54963e226753d44085a7d1f5dccdef6"></a>

```c
int bt_gmap_discover (struct bt_conn *conn)
```

相关声明：[bt_gmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gab54963e226753d44085a7d1f5dccdef6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

在远端设备上发现游戏服务（Gaming Service）。

<a id="r_ga75211707bbdceff35235c353dc8c7609"></a>

```c
int bt_gmap_register (enum bt_gmap_role role, struct bt_gmap_feat features)
```

相关声明：[bt_gmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga75211707bbdceff35235c353dc8c7609)、[bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)、[bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)。

将游戏音频服务（GMAS）实例加入数据库，并设置收到的游戏音频配置文件（Gaming Audio Profile）角色。

<a id="r_ga956efe257f06b627615a0a82d44db919"></a>

```c
int bt_gmap_set_role (enum bt_gmap_role role, struct bt_gmap_feat features)
```

相关声明：[bt_gmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga956efe257f06b627615a0a82d44db919)、[bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)、[bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)。

动态设置一个或多个游戏音频配置文件（Gaming Audio Profile）角色和特性。


## 12.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P079_gmap.h_源码浏览.md)
- [bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)
- [bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)
- [bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)
- [BT_GMAP_ROLE_UGG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251)
- [BT_GMAP_ROLE_UGT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b)
- [BT_GMAP_ROLE_BGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6)
- [BT_GMAP_ROLE_BGR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091)
- [bt_gmap_ugg_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3ef43378bad84bbcd726e318cf0bc145)
- [BT_GMAP_UGG_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e)
- [BT_GMAP_UGG_FEAT_96KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331)
- [BT_GMAP_UGG_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1)
- [bt_gmap_ugt_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga0fe87d6d1412c15564ba7de29e3d7a48)
- [BT_GMAP_UGT_FEAT_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231)
- [BT_GMAP_UGT_FEAT_80KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88)
- [BT_GMAP_UGT_FEAT_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c)
- [BT_GMAP_UGT_FEAT_64KBPS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604)
- [BT_GMAP_UGT_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e)
- [BT_GMAP_UGT_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08)
- [BT_GMAP_UGT_FEAT_MULTISOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045)
- [bt_gmap_bgs_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3a79c408b283864616a522b1f04cacaf)
- [BT_GMAP_BGS_FEAT_96KBPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8)
- [bt_gmap_bgr_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga9c1145ad5334e14d4978b6d7d3c84b6c)
- [BT_GMAP_BGR_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630)
- [BT_GMAP_BGR_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6)
- [bt_gmap_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gacc4853bf69d0a13353fc941aa7e4e190)
- [bt_gmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gab54963e226753d44085a7d1f5dccdef6)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga75211707bbdceff35235c353dc8c7609)
- [bt_gmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga956efe257f06b627615a0a82d44db919)

<a id="header-details"></a>

---

[上一章](P011_zephyr__net__ethernet_vlan.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__xen__gnttab.h_文件参考.md)
