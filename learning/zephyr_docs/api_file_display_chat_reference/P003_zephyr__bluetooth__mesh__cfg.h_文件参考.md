---
id: learning.zephyr-docs.api-file-display-chat-reference.page-3
title: zephyr__bluetooth__mesh__cfg.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_bluetooth\_\_mesh\_\_cfg.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

运行时配置（Runtime Configuration）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <sys/types.h>
```

查看此文件的源码。

运行时配置（Runtime Configuration）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga5b3af48dfe15948654b7791d7a684ba8"></a>

```c
#define BT_MESH_KR_NORMAL 0x00
```

相关声明：[BT_MESH_KR_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga5b3af48dfe15948654b7791d7a684ba8)。

<a id="r_ga139d621ce45ea87b4d8a15fc2b29dbe3"></a>

```c
#define BT_MESH_KR_PHASE_1 0x01
```

相关声明：[BT_MESH_KR_PHASE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga139d621ce45ea87b4d8a15fc2b29dbe3)。

<a id="r_gaff6e8f59719f341ab681268e421b1612"></a>

```c
#define BT_MESH_KR_PHASE_2 0x02
```

相关声明：[BT_MESH_KR_PHASE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaff6e8f59719f341ab681268e421b1612)。

<a id="r_gab0e65cdc2b152d3b84615223fdaebb2e"></a>

```c
#define BT_MESH_KR_PHASE_3 0x03
```

相关声明：[BT_MESH_KR_PHASE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gab0e65cdc2b152d3b84615223fdaebb2e)。

<a id="r_gaafd10319da7d2f938207b8fd6de02dbc"></a>

```c
#define BT_MESH_RELAY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_RELAY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaafd10319da7d2f938207b8fd6de02dbc)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gae5d235a7c182a8add961d7ce344f87aa"></a>

```c
#define BT_MESH_RELAY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_RELAY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gae5d235a7c182a8add961d7ce344f87aa)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_gabbbbddd31c2a92256fe2f7a7520e76f7"></a>

```c
#define BT_MESH_RELAY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_RELAY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gabbbbddd31c2a92256fe2f7a7520e76f7)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga8fa3d0ac3cb9f69464c4068ca61689b9"></a>

```c
#define BT_MESH_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_BEACON_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga8fa3d0ac3cb9f69464c4068ca61689b9)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga01235217559423b93d7e6cf2236278f0"></a>

```c
#define BT_MESH_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_BEACON_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga01235217559423b93d7e6cf2236278f0)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga2645fd9e2aed6de7806e7ac5afd1af10"></a>

```c
#define BT_MESH_PRIV_BEACON_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_PRIV_BEACON_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga2645fd9e2aed6de7806e7ac5afd1af10)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga1f72ffadff83f30943df88cd1ddcbee8"></a>

```c
#define BT_MESH_PRIV_BEACON_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_PRIV_BEACON_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga1f72ffadff83f30943df88cd1ddcbee8)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga3fe3e68efd25a3a03a041b978435fd7b"></a>

```c
#define BT_MESH_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_GATT_PROXY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga3fe3e68efd25a3a03a041b978435fd7b)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga77f4438624aae49ea2bb66437c9623f7"></a>

```c
#define BT_MESH_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_GATT_PROXY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga77f4438624aae49ea2bb66437c9623f7)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_gaecec3747198a29dd10185e3755e660f8"></a>

```c
#define BT_MESH_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_GATT_PROXY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaecec3747198a29dd10185e3755e660f8)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga475302ad8ba5589c7ea95da36f18948e"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga475302ad8ba5589c7ea95da36f18948e)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gac73cdadfd9c9417a051739bce59960a7"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gac73cdadfd9c9417a051739bce59960a7)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga66b4ed203ecbc9a70620b5adff04110f"></a>

```c
#define BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga66b4ed203ecbc9a70620b5adff04110f)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga29fe48989e760438f2c5241110134c8c"></a>

```c
#define BT_MESH_FRIEND_DISABLED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_FRIEND_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga29fe48989e760438f2c5241110134c8c)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_gaa23bba212dc1b322651723ca20f497a3"></a>

```c
#define BT_MESH_FRIEND_ENABLED BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_FRIEND_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa23bba212dc1b322651723ca20f497a3)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga35f85e6a9c085cdad4f70b8e60d0b027"></a>

```c
#define BT_MESH_FRIEND_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_FRIEND_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga35f85e6a9c085cdad4f70b8e60d0b027)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="r_ga9a83214cdbd34ac1d4bc644136523bd9"></a>

```c
#define BT_MESH_NODE_IDENTITY_STOPPED BT_MESH_FEATURE_DISABLED
```

相关声明：[BT_MESH_NODE_IDENTITY_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga9a83214cdbd34ac1d4bc644136523bd9)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)。

<a id="r_ga86e88acc6fdcc26a9cea4415daad016c"></a>

```c
#define BT_MESH_NODE_IDENTITY_RUNNING BT_MESH_FEATURE_ENABLED
```

相关声明：[BT_MESH_NODE_IDENTITY_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga86e88acc6fdcc26a9cea4415daad016c)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)。

<a id="r_ga7ffe6722b12a8663518b4e17349e4da5"></a>

```c
#define BT_MESH_NODE_IDENTITY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED
```

相关声明：[BT_MESH_NODE_IDENTITY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga7ffe6722b12a8663518b4e17349e4da5)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_ga0a3557a71597885a31cf209c6b83cedb"></a>

```c
enum bt_mesh_feat_state { BT_MESH_FEATURE_DISABLED , BT_MESH_FEATURE_ENABLED , BT_MESH_FEATURE_NOT_SUPPORTED }
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)、[BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)、[BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)。

蓝牙 Mesh 特性状态（Feature States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga15de1cdc964628b6f001ef893021ce6e"></a>

```c
void bt_mesh_beacon_set (bool beacon)
```

相关声明：[bt_mesh_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga15de1cdc964628b6f001ef893021ce6e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用安全网络信标（Secure Network Beacon）的发送。

<a id="r_ga479c14f6b0d4a08ddf5b160fa9267844"></a>

```c
bool bt_mesh_beacon_enabled (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_beacon_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga479c14f6b0d4a08ddf5b160fa9267844)。

获取当前安全网络信标（Secure Network Beacon）状态。

<a id="r_ga1afc5ec210bbc6090ada922ddf75e284"></a>

```c
int bt_mesh_priv_beacon_set (enum bt_mesh_feat_state priv_beacon)
```

相关声明：[bt_mesh_priv_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga1afc5ec210bbc6090ada922ddf75e284)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用 Mesh 私有信标（Private Beacon）的发送。

<a id="r_ga2c8dc9ee5c3862790efd2a74a1ef6873"></a>

```c
enum bt_mesh_feat_state bt_mesh_priv_beacon_get (void)
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_priv_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga2c8dc9ee5c3862790efd2a74a1ef6873)。

获取当前 Mesh 私有信标（Private Beacon）状态。

<a id="r_ga01abb07d27edef40ffff4da968065c1d"></a>

```c
void bt_mesh_priv_beacon_update_interval_set (uint8_t interval)
```

相关声明：[bt_mesh_priv_beacon_update_interval_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga01abb07d27edef40ffff4da968065c1d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

<a id="r_gafe3d54c1546b03cebbecaf762ae87781"></a>

```c
uint8_t bt_mesh_priv_beacon_update_interval_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_priv_beacon_update_interval_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gafe3d54c1546b03cebbecaf762ae87781)。

获取当前 Mesh 私有信标更新间隔（Private Beacon Update Interval）。

<a id="r_gaafea57625c9fdba535431cc92dadd162"></a>

```c
int bt_mesh_default_ttl_set (uint8_t default_ttl)
```

相关声明：[bt_mesh_default_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaafea57625c9fdba535431cc92dadd162)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置默认生存时间（TTL）值。

<a id="r_gaa97f63f5b3167c672fa1a0d8c8fe9ab7"></a>

```c
uint8_t bt_mesh_default_ttl_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_default_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa97f63f5b3167c672fa1a0d8c8fe9ab7)。

获取当前默认生存时间（TTL）值。

<a id="r_ga256d00139ca40eb99303fef766a3add7"></a>

```c
int bt_mesh_od_priv_proxy_get (void)
```

相关声明：[bt_mesh_od_priv_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga256d00139ca40eb99303fef766a3add7)。

获取当前 Mesh 按需私有代理（On-Demand Private Proxy）状态。

<a id="r_ga26023b727e1b180263b22d0ade145f81"></a>

```c
int bt_mesh_od_priv_proxy_set (uint8_t on_demand_proxy)
```

相关声明：[bt_mesh_od_priv_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga26023b727e1b180263b22d0ade145f81)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 Mesh 按需私有代理（On-Demand Private Proxy）状态。

<a id="r_gaa652e4f1460f62252065ac21854ab3f6"></a>

```c
void bt_mesh_net_transmit_set (uint8_t xmit)
```

相关声明：[bt_mesh_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa652e4f1460f62252065ac21854ab3f6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置网络发送参数（Network Transmit Parameters）。

<a id="r_ga08b336fa1a4a721ac9b10fbb75e4af6b"></a>

```c
uint8_t bt_mesh_net_transmit_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga08b336fa1a4a721ac9b10fbb75e4af6b)。

获取当前网络发送参数（Network Transmit Parameters）。

<a id="r_gad8d6773753b80540b2aaa982c1ec8c03"></a>

```c
int bt_mesh_relay_set (enum bt_mesh_feat_state relay, uint8_t xmit)
```

相关声明：[bt_mesh_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gad8d6773753b80540b2aaa982c1ec8c03)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置中继特性（Relay Feature）。

<a id="r_gadb41d2f78a490aa81b5640bb7ff5a5ce"></a>

```c
enum bt_mesh_feat_state bt_mesh_relay_get (void)
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gadb41d2f78a490aa81b5640bb7ff5a5ce)。

获取当前中继特性（Relay Feature）状态。

<a id="r_gaf9abf4bcba55d273a7e6e8ee42c521a9"></a>

```c
uint8_t bt_mesh_relay_retransmit_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_relay_retransmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaf9abf4bcba55d273a7e6e8ee42c521a9)。

获取当前中继重传参数（Relay Retransmit Parameters）。

<a id="r_gaac543b57580f9ac8dff36c0ce1196144"></a>

```c
int bt_mesh_gatt_proxy_set (enum bt_mesh_feat_state gatt_proxy)
```

相关声明：[bt_mesh_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaac543b57580f9ac8dff36c0ce1196144)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用 GATT 代理特性（GATT Proxy Feature）。

<a id="r_ga8457f222211bc812106b2dccc87b1abe"></a>

```c
enum bt_mesh_feat_state bt_mesh_gatt_proxy_get (void)
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga8457f222211bc812106b2dccc87b1abe)。

获取当前 GATT 代理（GATT Proxy）状态。

<a id="r_ga346244dcc70afe3a85e85c28c56b4f49"></a>

```c
int bt_mesh_priv_gatt_proxy_set (enum bt_mesh_feat_state priv_gatt_proxy)
```

相关声明：[bt_mesh_priv_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga346244dcc70afe3a85e85c28c56b4f49)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用私有 GATT 代理特性（Private GATT Proxy Feature）。

<a id="r_ga037375c99abb492d30378deca183071d"></a>

```c
enum bt_mesh_feat_state bt_mesh_priv_gatt_proxy_get (void)
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_priv_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga037375c99abb492d30378deca183071d)。

获取当前私有 GATT 代理（Private GATT Proxy）状态。

<a id="r_ga74b79bc6a15c35ef399e7d5f7c4d26e6"></a>

```c
int bt_mesh_friend_set (enum bt_mesh_feat_state friendship)
```

相关声明：[bt_mesh_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga74b79bc6a15c35ef399e7d5f7c4d26e6)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

启用或禁用朋友特性（Friend Feature）。

<a id="r_gac7b1f1208659c80956e6dab6ac0ebc47"></a>

```c
enum bt_mesh_feat_state bt_mesh_friend_get (void)
```

相关声明：[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)、[bt_mesh_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gac7b1f1208659c80956e6dab6ac0ebc47)。

获取当前朋友（Friend）状态。

<a id="r_ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f"></a>

```c
uint8_t bt_mesh_subnet_add (uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加子网（Subnet）。

<a id="r_ga47236f48940303be27fa6af4797424c2"></a>

```c
uint8_t bt_mesh_subnet_update (uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga47236f48940303be27fa6af4797424c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新给定子网（Subnet）。

<a id="r_gaec9d827d5f026b473f3ac88988d3c842"></a>

```c
uint8_t bt_mesh_subnet_del (uint16_t net_idx)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaec9d827d5f026b473f3ac88988d3c842)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除子网（Subnet）。

<a id="r_gad48780acaae085350a8b48d033717bfa"></a>

```c
bool bt_mesh_subnet_exists (uint16_t net_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_subnet_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad48780acaae085350a8b48d033717bfa)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查子网（Subnet）是否已知。

<a id="r_gaef15af43e74e3c71590c63c5f1e3ea55"></a>

```c
uint8_t bt_mesh_subnet_kr_phase_set (uint16_t net_idx, uint8_t *phase)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_kr_phase_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaef15af43e74e3c71590c63c5f1e3ea55)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置子网的密钥刷新阶段（Key Refresh Phase）。

<a id="r_gad251907892150649f3f1ae6b4112cd84"></a>

```c
uint8_t bt_mesh_subnet_kr_phase_get (uint16_t net_idx, uint8_t *phase)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_kr_phase_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad251907892150649f3f1ae6b4112cd84)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子网的密钥刷新阶段（Key Refresh Phase）。

<a id="r_ga59bf9f022665edc0ad03267e4bd16632"></a>

```c
uint8_t bt_mesh_subnet_node_id_set (uint16_t net_idx, enum bt_mesh_feat_state node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga59bf9f022665edc0ad03267e4bd16632)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

设置子网的节点身份（Node Identity）状态。

<a id="r_ga683d1f9abe82649a774b3d53dcaced8e"></a>

```c
uint8_t bt_mesh_subnet_node_id_get (uint16_t net_idx, enum bt_mesh_feat_state *node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga683d1f9abe82649a774b3d53dcaced8e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

获取子网的节点身份（Node Identity）状态。

<a id="r_ga5aa3e7f6b64e1b8b98f9737606d5d1ec"></a>

```c
uint8_t bt_mesh_subnet_priv_node_id_set (uint16_t net_idx, enum bt_mesh_feat_state priv_node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_priv_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga5aa3e7f6b64e1b8b98f9737606d5d1ec)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

设置子网的私有节点身份（Private Node Identity）状态。

<a id="r_ga555b4a7127869355fdf6040b8d14f999"></a>

```c
uint8_t bt_mesh_subnet_priv_node_id_get (uint16_t net_idx, enum bt_mesh_feat_state *priv_node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_priv_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga555b4a7127869355fdf6040b8d14f999)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

获取子网的私有节点身份（Private Node Identity）状态。

<a id="r_ga0fd04bff5423a36b013089a4ba351d67"></a>

```c
ssize_t bt_mesh_subnets_get (uint16_t net_idxs[], size_t max, off_t skip)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_mesh_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga0fd04bff5423a36b013089a4ba351d67)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

获取所有已知子网索引（Subnet Indexes）的列表。

<a id="r_ga0110ef750489af49a156a259c5a95c9b"></a>

```c
uint8_t bt_mesh_app_key_add (uint16_t app_idx, uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_add](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga0110ef750489af49a156a259c5a95c9b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加应用密钥（Application Key）。

<a id="r_ga5ae73ef766f0e1c38c0414c0a34e4053"></a>

```c
uint8_t bt_mesh_app_key_update (uint16_t app_idx, uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_update](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga5ae73ef766f0e1c38c0414c0a34e4053)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新应用密钥（Application Key）。

<a id="r_gaa0e80a19c14d47808fc11459bf5ea2eb"></a>

```c
uint8_t bt_mesh_app_key_del (uint16_t app_idx, uint16_t net_idx)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_del](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#gaa0e80a19c14d47808fc11459bf5ea2eb)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除应用密钥（Application Key）。

<a id="r_ga42c46a936e589460225a1fa69598a1ac"></a>

```c
bool bt_mesh_app_key_exists (uint16_t app_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_app_key_exists](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga42c46a936e589460225a1fa69598a1ac)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查是否已知某个应用密钥（Application Key）。

<a id="r_gad7a949a0a814f6c9a26816c076d8b92a"></a>

```c
ssize_t bt_mesh_app_keys_get (uint16_t net_idx, uint16_t app_idxs[], size_t max, off_t skip)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_mesh_app_keys_get](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#gad7a949a0a814f6c9a26816c076d8b92a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

获取所有已知应用密钥索引（Application Key Indexes）的列表。


## 3.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P011_cfg.h_源码浏览.md)
- [BT_MESH_KR_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga5b3af48dfe15948654b7791d7a684ba8)
- [BT_MESH_KR_PHASE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga139d621ce45ea87b4d8a15fc2b29dbe3)
- [BT_MESH_KR_PHASE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaff6e8f59719f341ab681268e421b1612)
- [BT_MESH_KR_PHASE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gab0e65cdc2b152d3b84615223fdaebb2e)
- [BT_MESH_RELAY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaafd10319da7d2f938207b8fd6de02dbc)
- [BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)
- [BT_MESH_RELAY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gae5d235a7c182a8add961d7ce344f87aa)
- [BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)
- [BT_MESH_RELAY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gabbbbddd31c2a92256fe2f7a7520e76f7)
- [BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)
- [BT_MESH_BEACON_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga8fa3d0ac3cb9f69464c4068ca61689b9)
- [BT_MESH_BEACON_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga01235217559423b93d7e6cf2236278f0)
- [BT_MESH_PRIV_BEACON_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga2645fd9e2aed6de7806e7ac5afd1af10)
- [BT_MESH_PRIV_BEACON_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga1f72ffadff83f30943df88cd1ddcbee8)
- [BT_MESH_GATT_PROXY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga3fe3e68efd25a3a03a041b978435fd7b)
- [BT_MESH_GATT_PROXY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga77f4438624aae49ea2bb66437c9623f7)
- [BT_MESH_GATT_PROXY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaecec3747198a29dd10185e3755e660f8)
- [BT_MESH_PRIV_GATT_PROXY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga475302ad8ba5589c7ea95da36f18948e)
- [BT_MESH_PRIV_GATT_PROXY_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gac73cdadfd9c9417a051739bce59960a7)
- [BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga66b4ed203ecbc9a70620b5adff04110f)
- [BT_MESH_FRIEND_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga29fe48989e760438f2c5241110134c8c)
- [BT_MESH_FRIEND_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa23bba212dc1b322651723ca20f497a3)
- [BT_MESH_FRIEND_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga35f85e6a9c085cdad4f70b8e60d0b027)
- [BT_MESH_NODE_IDENTITY_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga9a83214cdbd34ac1d4bc644136523bd9)
- [BT_MESH_NODE_IDENTITY_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga86e88acc6fdcc26a9cea4415daad016c)
- [BT_MESH_NODE_IDENTITY_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga7ffe6722b12a8663518b4e17349e4da5)
- [bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)
- [bt_mesh_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga15de1cdc964628b6f001ef893021ce6e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_beacon_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga479c14f6b0d4a08ddf5b160fa9267844)
- [bt_mesh_priv_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga1afc5ec210bbc6090ada922ddf75e284)
- [bt_mesh_priv_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga2c8dc9ee5c3862790efd2a74a1ef6873)
- [bt_mesh_priv_beacon_update_interval_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga01abb07d27edef40ffff4da968065c1d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_priv_beacon_update_interval_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gafe3d54c1546b03cebbecaf762ae87781)
- [bt_mesh_default_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaafea57625c9fdba535431cc92dadd162)
- [bt_mesh_default_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa97f63f5b3167c672fa1a0d8c8fe9ab7)
- [bt_mesh_od_priv_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga256d00139ca40eb99303fef766a3add7)
- [bt_mesh_od_priv_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga26023b727e1b180263b22d0ade145f81)
- [bt_mesh_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa652e4f1460f62252065ac21854ab3f6)
- [bt_mesh_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga08b336fa1a4a721ac9b10fbb75e4af6b)
- [bt_mesh_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gad8d6773753b80540b2aaa982c1ec8c03)
- [bt_mesh_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gadb41d2f78a490aa81b5640bb7ff5a5ce)
- [bt_mesh_relay_retransmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaf9abf4bcba55d273a7e6e8ee42c521a9)
- [bt_mesh_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaac543b57580f9ac8dff36c0ce1196144)
- [bt_mesh_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga8457f222211bc812106b2dccc87b1abe)
- [bt_mesh_priv_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga346244dcc70afe3a85e85c28c56b4f49)
- [bt_mesh_priv_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga037375c99abb492d30378deca183071d)
- [bt_mesh_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga74b79bc6a15c35ef399e7d5f7c4d26e6)
- [bt_mesh_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gac7b1f1208659c80956e6dab6ac0ebc47)
- [bt_mesh_subnet_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_subnet_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga47236f48940303be27fa6af4797424c2)
- [bt_mesh_subnet_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaec9d827d5f026b473f3ac88988d3c842)
- [bt_mesh_subnet_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad48780acaae085350a8b48d033717bfa)
- [bt_mesh_subnet_kr_phase_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaef15af43e74e3c71590c63c5f1e3ea55)
- [bt_mesh_subnet_kr_phase_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad251907892150649f3f1ae6b4112cd84)
- [bt_mesh_subnet_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga59bf9f022665edc0ad03267e4bd16632)
- [bt_mesh_subnet_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga683d1f9abe82649a774b3d53dcaced8e)
- [bt_mesh_subnet_priv_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga5aa3e7f6b64e1b8b98f9737606d5d1ec)
- [bt_mesh_subnet_priv_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga555b4a7127869355fdf6040b8d14f999)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_mesh_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga0fd04bff5423a36b013089a4ba351d67)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [bt_mesh_app_key_add](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga0110ef750489af49a156a259c5a95c9b)
- [bt_mesh_app_key_update](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga5ae73ef766f0e1c38c0414c0a34e4053)
- [bt_mesh_app_key_del](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#gaa0e80a19c14d47808fc11459bf5ea2eb)
- [bt_mesh_app_key_exists](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#ga42c46a936e589460225a1fa69598a1ac)
- [bt_mesh_app_keys_get](../api_radio_permission_topic_reference/P005_应用配置（Application Configuration）.md#gad7a949a0a814f6c9a26816c076d8b92a)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__memory-controller__adi-max32-hpb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__modem__chat.h_文件参考.md)
