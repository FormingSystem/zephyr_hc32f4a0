---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-5
title: 运行时配置（Runtime Configuration）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_运行时配置（Runtime Configuration）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

运行时配置（Runtime Configuration）

<a id="details"></a>

运行时配置（Runtime Configuration）

<a id="header-groups"></a>
<a id="groups"></a>

## 5.1\_主题（Topics）

<a id="r_bt_5Fmesh_5Fcfg_5Fapp"></a>

相关声明：[应用配置（Application Configuration）](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md)。

应用配置（Application Configuration）

<a id="r_bt_5Fmesh_5Fcfg_5Fsubnet"></a>

相关声明：[子网配置（Subnet Configuration）](../api_scoped_clock_topic_reference/P005_子网配置（Subnet Configuration）.md)。

子网配置（Subnet Configuration）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga5b3af48dfe15948654b7791d7a684ba8"></a>

```c
#define BT_MESH_KR_NORMAL 0x00
```

相关声明：[BT_MESH_KR_NORMAL](#ga5b3af48dfe15948654b7791d7a684ba8)。

<a id="r_ga139d621ce45ea87b4d8a15fc2b29dbe3"></a>

```c
#define BT_MESH_KR_PHASE_1 0x01
```

相关声明：[BT_MESH_KR_PHASE_1](#ga139d621ce45ea87b4d8a15fc2b29dbe3)。

<a id="r_gaff6e8f59719f341ab681268e421b1612"></a>

```c
#define BT_MESH_KR_PHASE_2 0x02
```

相关声明：[BT_MESH_KR_PHASE_2](#gaff6e8f59719f341ab681268e421b1612)。

<a id="r_gab0e65cdc2b152d3b84615223fdaebb2e"></a>

```c
#define BT_MESH_KR_PHASE_3 0x03
```

相关声明：[BT_MESH_KR_PHASE_3](#gab0e65cdc2b152d3b84615223fdaebb2e)。

<a id="r_gaafd10319da7d2f938207b8fd6de02dbc"></a>

```c
#define BT_MESH_RELAY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_RELAY_DISABLED](#gaafd10319da7d2f938207b8fd6de02dbc)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gae5d235a7c182a8add961d7ce344f87aa"></a>

```c
#define BT_MESH_RELAY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_RELAY_ENABLED](#gae5d235a7c182a8add961d7ce344f87aa)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_gabbbbddd31c2a92256fe2f7a7520e76f7"></a>

```c
#define BT_MESH_RELAY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_RELAY_NOT_SUPPORTED](#gabbbbddd31c2a92256fe2f7a7520e76f7)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga8fa3d0ac3cb9f69464c4068ca61689b9"></a>

```c
#define BT_MESH_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_BEACON_DISABLED](#ga8fa3d0ac3cb9f69464c4068ca61689b9)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga01235217559423b93d7e6cf2236278f0"></a>

```c
#define BT_MESH_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_BEACON_ENABLED](#ga01235217559423b93d7e6cf2236278f0)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga2645fd9e2aed6de7806e7ac5afd1af10"></a>

```c
#define BT_MESH_PRIV_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_PRIV_BEACON_DISABLED](#ga2645fd9e2aed6de7806e7ac5afd1af10)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga1f72ffadff83f30943df88cd1ddcbee8"></a>

```c
#define BT_MESH_PRIV_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_PRIV_BEACON_ENABLED](#ga1f72ffadff83f30943df88cd1ddcbee8)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga3fe3e68efd25a3a03a041b978435fd7b"></a>

```c
#define BT_MESH_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_GATT_PROXY_DISABLED](#ga3fe3e68efd25a3a03a041b978435fd7b)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga77f4438624aae49ea2bb66437c9623f7"></a>

```c
#define BT_MESH_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_GATT_PROXY_ENABLED](#ga77f4438624aae49ea2bb66437c9623f7)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_gaecec3747198a29dd10185e3755e660f8"></a>

```c
#define BT_MESH_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_GATT_PROXY_NOT_SUPPORTED](#gaecec3747198a29dd10185e3755e660f8)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga475302ad8ba5589c7ea95da36f18948e"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_DISABLED](#ga475302ad8ba5589c7ea95da36f18948e)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gac73cdadfd9c9417a051739bce59960a7"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_ENABLED](#gac73cdadfd9c9417a051739bce59960a7)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga66b4ed203ecbc9a70620b5adff04110f"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED](#ga66b4ed203ecbc9a70620b5adff04110f)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga29fe48989e760438f2c5241110134c8c"></a>

```c
#define BT_MESH_FRIEND_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_FRIEND_DISABLED](#ga29fe48989e760438f2c5241110134c8c)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gaa23bba212dc1b322651723ca20f497a3"></a>

```c
#define BT_MESH_FRIEND_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_FRIEND_ENABLED](#gaa23bba212dc1b322651723ca20f497a3)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga35f85e6a9c085cdad4f70b8e60d0b027"></a>

```c
#define BT_MESH_FRIEND_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_FRIEND_NOT_SUPPORTED](#ga35f85e6a9c085cdad4f70b8e60d0b027)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga9a83214cdbd34ac1d4bc644136523bd9"></a>

```c
#define BT_MESH_NODE_IDENTITY_STOPPED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_NODE_IDENTITY_STOPPED](#ga9a83214cdbd34ac1d4bc644136523bd9)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga86e88acc6fdcc26a9cea4415daad016c"></a>

```c
#define BT_MESH_NODE_IDENTITY_RUNNING BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_NODE_IDENTITY_RUNNING](#ga86e88acc6fdcc26a9cea4415daad016c)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga7ffe6722b12a8663518b4e17349e4da5"></a>

```c
#define BT_MESH_NODE_IDENTITY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_NODE_IDENTITY_NOT_SUPPORTED](#ga7ffe6722b12a8663518b4e17349e4da5)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_ga0a3557a71597885a31cf209c6b83cedb"></a>

```c
enum bt_mesh_feat_state { BT_MESH_FEATURE_DISABLED , BT_MESH_FEATURE_ENABLED , BT_MESH_FEATURE_NOT_SUPPORTED }
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[BT_MESH_FEATURE_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)、[BT_MESH_FEATURE_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)、[BT_MESH_FEATURE_NOT_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

蓝牙 Mesh 特性状态（Feature States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga15de1cdc964628b6f001ef893021ce6e"></a>

```c
void bt_mesh_beacon_set (bool beacon)
```

相关声明：[bt_mesh_beacon_set](#ga15de1cdc964628b6f001ef893021ce6e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用安全网络信标（Secure Network Beacon）的发送。

<a id="r_ga479c14f6b0d4a08ddf5b160fa9267844"></a>

```c
bool bt_mesh_beacon_enabled (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_beacon_enabled](#ga479c14f6b0d4a08ddf5b160fa9267844)。

获取当前安全网络信标（Secure Network Beacon）状态。

<a id="r_ga1afc5ec210bbc6090ada922ddf75e284"></a>

```c
int bt_mesh_priv_beacon_set (enum bt_mesh_feat_state priv_beacon)
```

相关声明：[bt_mesh_priv_beacon_set](#ga1afc5ec210bbc6090ada922ddf75e284)、[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用 Mesh 私有信标（Private Beacon）的发送。

<a id="r_ga2c8dc9ee5c3862790efd2a74a1ef6873"></a>

```c
enum bt_mesh_feat_state bt_mesh_priv_beacon_get (void)
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_priv_beacon_get](#ga2c8dc9ee5c3862790efd2a74a1ef6873)。

获取当前 Mesh 私有信标（Private Beacon）状态。

<a id="r_ga01abb07d27edef40ffff4da968065c1d"></a>

```c
void bt_mesh_priv_beacon_update_interval_set (uint8_t interval)
```

相关声明：[bt_mesh_priv_beacon_update_interval_set](#ga01abb07d27edef40ffff4da968065c1d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

<a id="r_gafe3d54c1546b03cebbecaf762ae87781"></a>

```c
uint8_t bt_mesh_priv_beacon_update_interval_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_priv_beacon_update_interval_get](#gafe3d54c1546b03cebbecaf762ae87781)。

获取当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

<a id="r_gaafea57625c9fdba535431cc92dadd162"></a>

```c
int bt_mesh_default_ttl_set (uint8_t default_ttl)
```

相关声明：[bt_mesh_default_ttl_set](#gaafea57625c9fdba535431cc92dadd162)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置默认生存时间（TTL）值。

<a id="r_gaa97f63f5b3167c672fa1a0d8c8fe9ab7"></a>

```c
uint8_t bt_mesh_default_ttl_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_default_ttl_get](#gaa97f63f5b3167c672fa1a0d8c8fe9ab7)。

获取当前默认生存时间（TTL）值。

<a id="r_ga256d00139ca40eb99303fef766a3add7"></a>

```c
int bt_mesh_od_priv_proxy_get (void)
```

相关声明：[bt_mesh_od_priv_proxy_get](#ga256d00139ca40eb99303fef766a3add7)。

获取当前 Mesh 按需私有代理（On-Demand Private Proxy）状态。

<a id="r_ga26023b727e1b180263b22d0ade145f81"></a>

```c
int bt_mesh_od_priv_proxy_set (uint8_t on_demand_proxy)
```

相关声明：[bt_mesh_od_priv_proxy_set](#ga26023b727e1b180263b22d0ade145f81)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 Mesh 按需私有代理（On-Demand Private Proxy）状态。

<a id="r_gaa652e4f1460f62252065ac21854ab3f6"></a>

```c
void bt_mesh_net_transmit_set (uint8_t xmit)
```

相关声明：[bt_mesh_net_transmit_set](#gaa652e4f1460f62252065ac21854ab3f6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置网络发送参数（Network Transmit Parameters）。

<a id="r_ga08b336fa1a4a721ac9b10fbb75e4af6b"></a>

```c
uint8_t bt_mesh_net_transmit_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_net_transmit_get](#ga08b336fa1a4a721ac9b10fbb75e4af6b)。

获取当前网络发送参数（Network Transmit Parameters）。

<a id="r_gad8d6773753b80540b2aaa982c1ec8c03"></a>

```c
int bt_mesh_relay_set (enum bt_mesh_feat_state relay, uint8_t xmit)
```

相关声明：[bt_mesh_relay_set](#gad8d6773753b80540b2aaa982c1ec8c03)、[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置中继特性（Relay Feature）。

<a id="r_gadb41d2f78a490aa81b5640bb7ff5a5ce"></a>

```c
enum bt_mesh_feat_state bt_mesh_relay_get (void)
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_relay_get](#gadb41d2f78a490aa81b5640bb7ff5a5ce)。

获取当前中继特性（Relay Feature）状态。

<a id="r_gaf9abf4bcba55d273a7e6e8ee42c521a9"></a>

```c
uint8_t bt_mesh_relay_retransmit_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_relay_retransmit_get](#gaf9abf4bcba55d273a7e6e8ee42c521a9)。

获取当前中继重传参数（Relay Retransmit Parameters）。

<a id="r_gaac543b57580f9ac8dff36c0ce1196144"></a>

```c
int bt_mesh_gatt_proxy_set (enum bt_mesh_feat_state gatt_proxy)
```

相关声明：[bt_mesh_gatt_proxy_set](#gaac543b57580f9ac8dff36c0ce1196144)、[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用 GATT 代理特性（GATT Proxy Feature）。

<a id="r_ga8457f222211bc812106b2dccc87b1abe"></a>

```c
enum bt_mesh_feat_state bt_mesh_gatt_proxy_get (void)
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_gatt_proxy_get](#ga8457f222211bc812106b2dccc87b1abe)。

获取当前 GATT 代理（GATT Proxy）状态。

<a id="r_ga346244dcc70afe3a85e85c28c56b4f49"></a>

```c
int bt_mesh_priv_gatt_proxy_set (enum bt_mesh_feat_state priv_gatt_proxy)
```

相关声明：[bt_mesh_priv_gatt_proxy_set](#ga346244dcc70afe3a85e85c28c56b4f49)、[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用私有 GATT 代理特性（Private GATT Proxy Feature）。

<a id="r_ga037375c99abb492d30378deca183071d"></a>

```c
enum bt_mesh_feat_state bt_mesh_priv_gatt_proxy_get (void)
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_priv_gatt_proxy_get](#ga037375c99abb492d30378deca183071d)。

获取当前私有 GATT 代理（Private GATT Proxy）状态。

<a id="r_ga74b79bc6a15c35ef399e7d5f7c4d26e6"></a>

```c
int bt_mesh_friend_set (enum bt_mesh_feat_state friendship)
```

相关声明：[bt_mesh_friend_set](#ga74b79bc6a15c35ef399e7d5f7c4d26e6)、[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用朋友特性（Friend Feature）。

<a id="r_gac7b1f1208659c80956e6dab6ac0ebc47"></a>

```c
enum bt_mesh_feat_state bt_mesh_friend_get (void)
```

相关声明：[bt_mesh_feat_state](#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_friend_get](#gac7b1f1208659c80956e6dab6ac0ebc47)。

获取当前朋友（Friend）状态。

## 5.5\_详细说明（Detailed Documentation）

<a id="ga8fa3d0ac3cb9f69464c4068ca61689b9"></a>

### `BT_MESH_BEACON_DISABLED`

```c
#define BT_MESH_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga01235217559423b93d7e6cf2236278f0"></a>

### `BT_MESH_BEACON_ENABLED`

```c
#define BT_MESH_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga29fe48989e760438f2c5241110134c8c"></a>

### `BT_MESH_FRIEND_DISABLED`

```c
#define BT_MESH_FRIEND_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gaa23bba212dc1b322651723ca20f497a3"></a>

### `BT_MESH_FRIEND_ENABLED`

```c
#define BT_MESH_FRIEND_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga35f85e6a9c085cdad4f70b8e60d0b027"></a>

### `BT_MESH_FRIEND_NOT_SUPPORTED`

```c
#define BT_MESH_FRIEND_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga3fe3e68efd25a3a03a041b978435fd7b"></a>

### `BT_MESH_GATT_PROXY_DISABLED`

```c
#define BT_MESH_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga77f4438624aae49ea2bb66437c9623f7"></a>

### `BT_MESH_GATT_PROXY_ENABLED`

```c
#define BT_MESH_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gaecec3747198a29dd10185e3755e660f8"></a>

### `BT_MESH_GATT_PROXY_NOT_SUPPORTED`

```c
#define BT_MESH_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga5b3af48dfe15948654b7791d7a684ba8"></a>

### `BT_MESH_KR_NORMAL`

```c
#define BT_MESH_KR_NORMAL 0x00
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga139d621ce45ea87b4d8a15fc2b29dbe3"></a>

### `BT_MESH_KR_PHASE_1`

```c
#define BT_MESH_KR_PHASE_1 0x01
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gaff6e8f59719f341ab681268e421b1612"></a>

### `BT_MESH_KR_PHASE_2`

```c
#define BT_MESH_KR_PHASE_2 0x02
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gab0e65cdc2b152d3b84615223fdaebb2e"></a>

### `BT_MESH_KR_PHASE_3`

```c
#define BT_MESH_KR_PHASE_3 0x03
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga7ffe6722b12a8663518b4e17349e4da5"></a>

### `BT_MESH_NODE_IDENTITY_NOT_SUPPORTED`

```c
#define BT_MESH_NODE_IDENTITY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga86e88acc6fdcc26a9cea4415daad016c"></a>

### `BT_MESH_NODE_IDENTITY_RUNNING`

```c
#define BT_MESH_NODE_IDENTITY_RUNNING BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga9a83214cdbd34ac1d4bc644136523bd9"></a>

### `BT_MESH_NODE_IDENTITY_STOPPED`

```c
#define BT_MESH_NODE_IDENTITY_STOPPED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga2645fd9e2aed6de7806e7ac5afd1af10"></a>

### `BT_MESH_PRIV_BEACON_DISABLED`

```c
#define BT_MESH_PRIV_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga1f72ffadff83f30943df88cd1ddcbee8"></a>

### `BT_MESH_PRIV_BEACON_ENABLED`

```c
#define BT_MESH_PRIV_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga475302ad8ba5589c7ea95da36f18948e"></a>

### `BT_MESH_PRIV_GATT_PROXY_DISABLED`

```c
#define BT_MESH_PRIV_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gac73cdadfd9c9417a051739bce59960a7"></a>

### `BT_MESH_PRIV_GATT_PROXY_ENABLED`

```c
#define BT_MESH_PRIV_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga66b4ed203ecbc9a70620b5adff04110f"></a>

### `BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED`

```c
#define BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gaafd10319da7d2f938207b8fd6de02dbc"></a>

### `BT_MESH_RELAY_DISABLED`

```c
#define BT_MESH_RELAY_DISABLED BT_MESH_FEATURE_DISABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gae5d235a7c182a8add961d7ce344f87aa"></a>

### `BT_MESH_RELAY_ENABLED`

```c
#define BT_MESH_RELAY_ENABLED BT_MESH_FEATURE_ENABLED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="gabbbbddd31c2a92256fe2f7a7520e76f7"></a>

### `BT_MESH_RELAY_NOT_SUPPORTED`

```c
#define BT_MESH_RELAY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

<a id="ga0a3557a71597885a31cf209c6b83cedb"></a>

### `bt_mesh_feat_state`

```c
enum bt_mesh_feat_state
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

蓝牙 Mesh 特性状态（Feature States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_FEATURE_DISABLED` | 支持该功能（Feature），但已禁用。 |
| `BT_MESH_FEATURE_ENABLED` | 支持该功能（Feature），且已启用。 |
| `BT_MESH_FEATURE_NOT_SUPPORTED` | 不支持该功能（Feature），无法启用。 |

<a id="ga479c14f6b0d4a08ddf5b160fa9267844"></a>

### `bt_mesh_beacon_enabled()`

```c
bool bt_mesh_beacon_enabled ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前安全网络信标（Secure Network Beacon）状态。

**返回（Returns）**：返回值（Returns）：安全网络信标功能（Secure Network Beacon Feature）是否已启用。

<a id="ga15de1cdc964628b6f001ef893021ce6e"></a>

### `bt_mesh_beacon_set()`

```c
void bt_mesh_beacon_set ( bool beacon)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

启用或禁用安全网络信标（Secure Network Beacon）的发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `beacon` | 新的安全网络信标状态（Secure Network Beacon State）。 |

<a id="gaa97f63f5b3167c672fa1a0d8c8fe9ab7"></a>

### `bt_mesh_default_ttl_get()`

```c
uint8_t bt_mesh_default_ttl_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前默认生存时间（TTL）值。

**返回（Returns）**：返回值（Returns）：当前默认生存时间值（Default TTL Value）。

<a id="gaafea57625c9fdba535431cc92dadd162"></a>

### `bt_mesh_default_ttl_set()`

```c
int bt_mesh_default_ttl_set ( uint8_t default_ttl)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置默认生存时间（TTL）值。

未显式设置生存时间（TTL）时使用默认值。当 `bt_mesh_msg_ctx::send_ttl` 为 `BT_MESH_TTL_DEFAULT` 时，模型（Model）将使用默认 TTL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `default_ttl` | 新的默认生存时间值（Default TTL Value）。有效值为 `0x00`，或 `0x02` 至 `BT_MESH_TTL_MAX`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功设置默认生存时间值（Default TTL Value）。 |
| `-EINVAL` | 生存时间值（TTL Value）无效。 |

<a id="gac7b1f1208659c80956e6dab6ac0ebc47"></a>

### `bt_mesh_friend_get()`

```c
enum bt_mesh_feat_state bt_mesh_friend_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前朋友（Friend）状态。

**返回（Returns）**：返回值（Returns）：朋友功能状态（Friend Feature State）。

<a id="ga74b79bc6a15c35ef399e7d5f7c4d26e6"></a>

### `bt_mesh_friend_set()`

```c
int bt_mesh_friend_set ( enum bt_mesh_feat_state friendship)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

启用或禁用朋友特性（Friend Feature）。

禁用朋友功能（Friend Feature）会立即终止所有活动的朋友关系（Friendship）。

必须通过配置选项 `CONFIG_BT_MESH_FRIEND` 启用朋友功能（Friend Feature）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `friendship` | 新的朋友功能状态（Friend Feature State），必须为 `BT_MESH_FEATURE_ENABLED` 或 `BT_MESH_FEATURE_DISABLED`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改朋友功能状态（Friend Feature State）。 |
| `-ENOTSUP` | 不支持朋友功能（Friend Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已处于给定状态（State）。 |

<a id="ga8457f222211bc812106b2dccc87b1abe"></a>

### `bt_mesh_gatt_proxy_get()`

```c
enum bt_mesh_feat_state bt_mesh_gatt_proxy_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前 GATT 代理（GATT Proxy）状态。

**返回（Returns）**：返回值（Returns）：GATT 代理功能状态（GATT Proxy Feature State）。

<a id="gaac543b57580f9ac8dff36c0ce1196144"></a>

### `bt_mesh_gatt_proxy_set()`

```c
int bt_mesh_gatt_proxy_set ( enum bt_mesh_feat_state gatt_proxy)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

启用或禁用 GATT 代理特性（GATT Proxy Feature）。

必须通过配置选项 `CONFIG_BT_MESH_GATT_PROXY` 启用 GATT 代理功能（GATT Proxy Feature）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gatt_proxy` | 新的 GATT 代理状态（GATT Proxy State），必须为 `BT_MESH_FEATURE_ENABLED` 或 `BT_MESH_FEATURE_DISABLED`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改 GATT 代理功能状态（GATT Proxy Feature State）。 |
| `-ENOTSUP` | 不支持 GATT 代理功能（GATT Proxy Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已处于给定状态（State）。 |

**说明（Note）**：注意（Note）：GATT 代理功能（GATT Proxy Feature）仅控制代理节点向 Mesh 网络中继消息的能力。支持 GATT 代理的节点即使禁用该功能，仍会广播可连接代理信标（Connectable Proxy Beacon）。只有通过编译时配置（Compile-time Configuration）才能完全禁用代理功能。

<a id="ga08b336fa1a4a721ac9b10fbb75e4af6b"></a>

### `bt_mesh_net_transmit_get()`

```c
uint8_t bt_mesh_net_transmit_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前网络发送参数（Network Transmit Parameters）。

可以使用 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 宏解码网络发送参数（Network Transmit Parameters）。

**返回（Returns）**：返回值（Returns）：当前网络发送参数（Network Transmit Parameters）。

<a id="gaa652e4f1460f62252065ac21854ab3f6"></a>

### `bt_mesh_net_transmit_set()`

```c
void bt_mesh_net_transmit_set ( uint8_t xmit)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置网络发送参数（Network Transmit Parameters）。

网络发送参数（Network Transmit Parameters）决定发送本地消息时使用的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `xmit` | 新的网络发送参数（Network Transmit Parameters），使用 `BT_MESH_TRANSMIT` 编码。 |

**参阅（See Also）**：另见（See also）：`BT_MESH_TRANSMIT`。

<a id="ga256d00139ca40eb99303fef766a3add7"></a>

### `bt_mesh_od_priv_proxy_get()`

```c
int bt_mesh_od_priv_proxy_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前 Mesh 按需私有代理（On-Demand Private Proxy）状态。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 或以正值表示按需私有代理功能状态（On-Demand Private Proxy Feature State）。 |
| `-ENOTSUP` | 不支持按需私有代理功能（On-Demand Private Proxy Feature）。 |

<a id="ga26023b727e1b180263b22d0ade145f81"></a>

### `bt_mesh_od_priv_proxy_set()`

```c
int bt_mesh_od_priv_proxy_set ( uint8_t on_demand_proxy)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置 Mesh 按需私有代理（On-Demand Private Proxy）状态。

必须使用 `BT_MESH_OD_PRIV_PROXY_SRV` 启用按需私有代理状态（On-Demand Private Proxy State）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `on_demand_proxy` | 新的 Mesh 按需私有代理状态（On-Demand Private Proxy State）。`0x00` 表示不能按需启用使用私有网络身份（Private Network Identity）的广播。`0x01`–`0xFF` 设置收到有效请求 PDU（Solicitation PDU）或客户端断开连接后，这类广播的时间间隔。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改 Mesh 按需私有代理功能状态（On-Demand Private Proxy Feature State）。 |
| `-ENOTSUP` | 不支持按需私有代理功能（On-Demand Private Proxy Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已处于给定状态（State）。 |

<a id="ga2c8dc9ee5c3862790efd2a74a1ef6873"></a>

### `bt_mesh_priv_beacon_get()`

```c
enum bt_mesh_feat_state bt_mesh_priv_beacon_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前 Mesh 私有信标（Private Beacon）状态。

**返回（Returns）**：返回值（Returns）：Mesh 私有信标功能状态（Private Beacon Feature State）。

<a id="ga1afc5ec210bbc6090ada922ddf75e284"></a>

### `bt_mesh_priv_beacon_set()`

```c
int bt_mesh_priv_beacon_set ( enum bt_mesh_feat_state priv_beacon)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

启用或禁用 Mesh 私有信标（Private Beacon）的发送。

必须使用 `CONFIG_BT_MESH_PRIV_BEACONS` 启用私有信标状态（Private Beacon State）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priv_beacon` | 新的 Mesh 私有信标状态（Private Beacon State），必须为 `BT_MESH_FEATURE_ENABLED` 或 `BT_MESH_FEATURE_DISABLED`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改 Mesh 私有信标功能状态（Private Beacon Feature State）。 |
| `-ENOTSUP` | 不支持 Mesh 私有信标功能（Private Beacon Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已处于给定状态（State）。 |

<a id="gafe3d54c1546b03cebbecaf762ae87781"></a>

### `bt_mesh_priv_beacon_update_interval_get()`

```c
uint8_t bt_mesh_priv_beacon_update_interval_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

Mesh 私有信标（Private Beacon）的随机化值（Randomization Value）会定期更新，以维持节点隐私。更新间隔（Update Interval）控制信标更新频率，以 10 秒为步长。

**返回（Returns）**：返回值（Returns）：私有信标更新间隔（Private Beacon Update Interval），以 10 秒为步长；为 0 时，每次发送信标都会更新。

<a id="ga01abb07d27edef40ffff4da968065c1d"></a>

### `bt_mesh_priv_beacon_update_interval_set()`

```c
void bt_mesh_priv_beacon_update_interval_set ( uint8_t interval)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

Mesh 私有信标（Private Beacon）的随机化值（Randomization Value）会定期更新，以维持节点隐私。更新间隔（Update Interval）控制信标更新频率，以 10 秒为步长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `interval` | 私有信标更新间隔（Private Beacon Update Interval），以 10 秒为步长；为 0 时，每次发送信标都更新。 |

<a id="ga037375c99abb492d30378deca183071d"></a>

### `bt_mesh_priv_gatt_proxy_get()`

```c
enum bt_mesh_feat_state bt_mesh_priv_gatt_proxy_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前私有 GATT 代理（Private GATT Proxy）状态。

**返回（Returns）**：返回值（Returns）：私有 GATT 代理功能状态（Private GATT Proxy Feature State）。

<a id="ga346244dcc70afe3a85e85c28c56b4f49"></a>

### `bt_mesh_priv_gatt_proxy_set()`

```c
int bt_mesh_priv_gatt_proxy_set ( enum bt_mesh_feat_state priv_gatt_proxy)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

启用或禁用私有 GATT 代理特性（Private GATT Proxy Feature）。

必须通过配置选项 `CONFIG_BT_MESH_PRIV_BEACONS` 和 `CONFIG_BT_MESH_GATT_PROXY` 启用私有 GATT 代理功能（Private GATT Proxy Feature）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priv_gatt_proxy` | 新的私有 GATT 代理状态（Private GATT Proxy State），必须为 `BT_MESH_FEATURE_ENABLED` 或 `BT_MESH_FEATURE_DISABLED`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改私有 GATT 代理功能状态（Private GATT Proxy Feature State）。 |
| `-ENOTSUP` | 不支持私有 GATT 代理功能（Private GATT Proxy Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已处于给定状态（State）。 |

<a id="gadb41d2f78a490aa81b5640bb7ff5a5ce"></a>

### `bt_mesh_relay_get()`

```c
enum bt_mesh_feat_state bt_mesh_relay_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前中继特性（Relay Feature）状态。

**返回（Returns）**：返回值（Returns）：中继功能状态（Relay Feature State）。

<a id="gaf9abf4bcba55d273a7e6e8ee42c521a9"></a>

### `bt_mesh_relay_retransmit_get()`

```c
uint8_t bt_mesh_relay_retransmit_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取当前中继重传参数（Relay Retransmit Parameters）。

可以使用 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 宏解码中继重传参数（Relay Retransmit Parameters）。

**返回（Returns）**：返回值（Returns）：当前中继重传参数（Relay Retransmit Parameters）；不支持中继时为 0。

<a id="gad8d6773753b80540b2aaa982c1ec8c03"></a>

### `bt_mesh_relay_set()`

```c
int bt_mesh_relay_set ( enum bt_mesh_feat_state relay, uint8_t xmit )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

配置中继特性（Relay Feature）。

启用或禁用中继功能（Relay Feature），并配置用于发送中继消息的参数。

必须通过配置选项 `CONFIG_BT_MESH_RELAY` 启用中继功能（Relay Feature）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `relay` | 新的中继功能状态（Relay Feature State），必须为 `BT_MESH_FEATURE_ENABLED` 或 `BT_MESH_FEATURE_DISABLED`。 |
| `xmit` | 新的中继重传参数（Relay Retransmit Parameters），使用 `BT_MESH_TRANSMIT` 编码。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功更改中继配置（Relay Configuration）。 |
| `-ENOTSUP` | 不支持中继功能（Relay Feature）。 |
| `-EINVAL` | 参数无效（Invalid Parameter）。 |
| `-EALREADY` | 已经在使用给定参数（Parameters）。 |

**参阅（See Also）**：另见（See also）：`BT_MESH_TRANSMIT`。


## 5.6\_原页交叉引用（Cross References）

- [应用配置（Application Configuration）](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md)
- [子网配置（Subnet Configuration）](../api_scoped_clock_topic_reference/P005_子网配置（Subnet Configuration）.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/mesh/cfg.h](../api_file_display_chat_reference/P003_zephyr__bluetooth__mesh__cfg.h_文件参考.md)
- [bt_mesh_msg_ctx::send_ttl](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a43b0ebfdc3c8018a02886d93dfe2f21b)
- [BT_MESH_TTL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga16516272b42420263b1c47c3ea16c0c8)
- [BT_MESH_TTL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga071e85e929589d31bf876e2e09cf2f19)
- [BT_MESH_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga62fda0d731241efbaa4827e4eb9d1795)
- [BT_MESH_TRANSMIT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga2aa21171c5677d23ad0c472291639417)
- [BT_MESH_TRANSMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaff82bf652232fbce71c31f38a10577a9)
- [CONFIG_BT_MESH_PRIV_BEACONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACONS)
- [CONFIG_BT_MESH_GATT_PROXY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_PROXY)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729"></a>
<a id="gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275"></a>
<a id="gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md) · [返回大纲](大纲.md) · [下一章](P006_健康故障（Health Faults）。.md)
