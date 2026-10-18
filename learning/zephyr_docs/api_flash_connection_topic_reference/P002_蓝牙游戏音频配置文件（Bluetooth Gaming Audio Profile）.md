---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-2
title: 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile，GMAP）

<a id="details"></a>

蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile，GMAP）。起始版本（Since）：3.5。接口版本（Version）：0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

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

## 2.2\_枚举（Enumerations）

<a id="r_ga55ecab78bcd6de6c294abdc20ad10e56"></a>

```c
enum bt_gmap_role { BT_GMAP_ROLE_UGG = (1UL << (0U)) , BT_GMAP_ROLE_UGT = (1UL << (1U)) , BT_GMAP_ROLE_BGS = (1UL << (2U)) , BT_GMAP_ROLE_BGR = (1UL << (3U)) }
```

相关声明：[bt_gmap_role](#ga55ecab78bcd6de6c294abdc20ad10e56)、[BT_GMAP_ROLE_UGG](#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251)、[BT_GMAP_ROLE_UGT](#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b)、[BT_GMAP_ROLE_BGS](#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6)、[BT_GMAP_ROLE_BGR](#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091)。

游戏角色位域（Gaming Role Bitfield）。

<a id="r_ga3ef43378bad84bbcd726e318cf0bc145"></a>

```c
enum bt_gmap_ugg_feat { BT_GMAP_UGG_FEAT_MULTIPLEX = (1UL << (0U)) , BT_GMAP_UGG_FEAT_96KBPS_SOURCE = (1UL << (1U)) , BT_GMAP_UGG_FEAT_MULTISINK = (1UL << (2U)) }
```

相关声明：[bt_gmap_ugg_feat](#ga3ef43378bad84bbcd726e318cf0bc145)、[BT_GMAP_UGG_FEAT_MULTIPLEX](#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e)、[BT_GMAP_UGG_FEAT_96KBPS_SOURCE](#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331)、[BT_GMAP_UGG_FEAT_MULTISINK](#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1)。

单播游戏网关特性位域（Unicast Game Gateway Feature Bitfield）。

<a id="r_ga0fe87d6d1412c15564ba7de29e3d7a48"></a>

```c
enum bt_gmap_ugt_feat { BT_GMAP_UGT_FEAT_SOURCE = (1UL << (0U)) , BT_GMAP_UGT_FEAT_80KBPS_SOURCE = (1UL << (1U)) , BT_GMAP_UGT_FEAT_SINK = (1UL << (2U)) , BT_GMAP_UGT_FEAT_64KBPS_SINK = (1UL << (3U)) , BT_GMAP_UGT_FEAT_MULTIPLEX = (1UL << (4U)) , BT_GMAP_UGT_FEAT_MULTISINK = (1UL << (5U)) , BT_GMAP_UGT_FEAT_MULTISOURCE = (1UL << (6U)) }
```

相关声明：[bt_gmap_ugt_feat](#ga0fe87d6d1412c15564ba7de29e3d7a48)、[BT_GMAP_UGT_FEAT_SOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231)、[BT_GMAP_UGT_FEAT_80KBPS_SOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88)、[BT_GMAP_UGT_FEAT_SINK](#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c)、[BT_GMAP_UGT_FEAT_64KBPS_SINK](#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604)、[BT_GMAP_UGT_FEAT_MULTIPLEX](#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e)、[BT_GMAP_UGT_FEAT_MULTISINK](#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08)、[BT_GMAP_UGT_FEAT_MULTISOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045)。

单播游戏终端特性位域（Unicast Game Terminal Feature Bitfield）。

<a id="r_ga3a79c408b283864616a522b1f04cacaf"></a>

```c
enum bt_gmap_bgs_feat { BT_GMAP_BGS_FEAT_96KBPS = (1UL << (0U)) }
```

相关声明：[bt_gmap_bgs_feat](#ga3a79c408b283864616a522b1f04cacaf)、[BT_GMAP_BGS_FEAT_96KBPS](#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8)。

广播游戏发送端特性位域（Broadcast Game Sender Feature Bitfield）。

<a id="r_ga9c1145ad5334e14d4978b6d7d3c84b6c"></a>

```c
enum bt_gmap_bgr_feat { BT_GMAP_BGR_FEAT_MULTISINK = (1UL << (0U)) , BT_GMAP_BGR_FEAT_MULTIPLEX = (1UL << (1U)) }
```

相关声明：[bt_gmap_bgr_feat](#ga9c1145ad5334e14d4978b6d7d3c84b6c)、[BT_GMAP_BGR_FEAT_MULTISINK](#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630)、[BT_GMAP_BGR_FEAT_MULTIPLEX](#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6)。

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gacc4853bf69d0a13353fc941aa7e4e190"></a>

```c
int bt_gmap_cb_register (const struct bt_gmap_cb *cb)
```

相关声明：[bt_gmap_cb_register](#gacc4853bf69d0a13353fc941aa7e4e190)、[bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)。

注册游戏音频配置文件（Gaming Audio Profile）使用的回调。

<a id="r_gab54963e226753d44085a7d1f5dccdef6"></a>

```c
int bt_gmap_discover (struct bt_conn *conn)
```

相关声明：[bt_gmap_discover](#gab54963e226753d44085a7d1f5dccdef6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

在远端设备上发现游戏服务（Gaming Service）。

<a id="r_ga75211707bbdceff35235c353dc8c7609"></a>

```c
int bt_gmap_register (enum bt_gmap_role role, struct bt_gmap_feat features)
```

相关声明：[bt_gmap_register](#ga75211707bbdceff35235c353dc8c7609)、[bt_gmap_role](#ga55ecab78bcd6de6c294abdc20ad10e56)、[bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)。

将游戏音频服务（GMAS）实例加入数据库，并设置收到的游戏音频配置文件（Gaming Audio Profile）角色。

<a id="r_ga956efe257f06b627615a0a82d44db919"></a>

```c
int bt_gmap_set_role (enum bt_gmap_role role, struct bt_gmap_feat features)
```

相关声明：[bt_gmap_set_role](#ga956efe257f06b627615a0a82d44db919)、[bt_gmap_role](#ga55ecab78bcd6de6c294abdc20ad10e56)、[bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)。

动态设置一个或多个游戏音频配置文件（Gaming Audio Profile）角色和特性。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga9c1145ad5334e14d4978b6d7d3c84b6c"></a>

### `bt_gmap_bgr_feat`

```c
enum bt_gmap_bgr_feat
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GMAP_BGR_FEAT_MULTISINK` | 支持接收至少两个音频声道（Audio Channel），每个声道位于独立的广播等时流（BIS）中。要求 `CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT > 1`。 |
| `BT_GMAP_BGR_FEAT_MULTIPLEX` | 支持在一个服务数据单元（SDU）的每个块（Block）中接收多个 LC3 编解码器帧（Codec Frame）。 |

<a id="ga3a79c408b283864616a522b1f04cacaf"></a>

### `bt_gmap_bgs_feat`

```c
enum bt_gmap_bgs_feat
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

广播游戏发送端特性位域（Broadcast Game Sender Feature Bitfield）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GMAP_BGS_FEAT_96KBPS` | 支持 96 kbps。 |

<a id="ga55ecab78bcd6de6c294abdc20ad10e56"></a>

### `bt_gmap_role`

```c
enum bt_gmap_role
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

游戏角色位域（Gaming Role Bitfield）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GMAP_ROLE_UGG` | 游戏角色：单播游戏网关（Unicast Game Gateway）。要求启用 `CONFIG_BT_CAP_INITIATOR`、`CONFIG_BT_BAP_UNICAST_CLIENT` 和 `CONFIG_BT_VCP_VOL_CTLR`。 |
| `BT_GMAP_ROLE_UGT` | 游戏角色：单播游戏终端（Unicast Game Terminal）。要求启用 `CONFIG_BT_CAP_ACCEPTOR` 和 `CONFIG_BT_BAP_UNICAST_SERVER`。 |
| `BT_GMAP_ROLE_BGS` | 游戏角色：广播游戏发送端（Broadcast Game Sender）。要求启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。 |
| `BT_GMAP_ROLE_BGR` | 游戏角色：广播游戏接收端（Broadcast Game Receiver）。要求启用 `CONFIG_BT_CAP_ACCEPTOR`、`CONFIG_BT_BAP_BROADCAST_SINK` 和 `CONFIG_BT_VCP_VOL_REND`。 |

<a id="ga3ef43378bad84bbcd726e318cf0bc145"></a>

### `bt_gmap_ugg_feat`

```c
enum bt_gmap_ugg_feat
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

单播游戏网关特性位域（Unicast Game Gateway Feature Bitfield）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GMAP_UGG_FEAT_MULTIPLEX` | 支持在一个服务数据单元（SDU）的每个块（Block）中发送多个 LC3 编解码器帧（Codec Frame）。要求 `CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT > 0`。 |
| `BT_GMAP_UGG_FEAT_96KBPS_SOURCE` | 源端（Source）支持 96 kbps。要求 `CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT > 0`。 |
| `BT_GMAP_UGG_FEAT_MULTISINK` | 支持接收至少两个音频声道（Audio Channel），每个声道位于独立的连接等时流（CIS）中。要求 `CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT > 1` 且 `CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT > 1`。 |

<a id="ga0fe87d6d1412c15564ba7de29e3d7a48"></a>

### `bt_gmap_ugt_feat`

```c
enum bt_gmap_ugt_feat
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

单播游戏终端特性位域（Unicast Game Terminal Feature Bitfield）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GMAP_UGT_FEAT_SOURCE` | 支持源端（Source）。要求 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT > 0`。 |
| `BT_GMAP_UGT_FEAT_80KBPS_SOURCE` | 源端（Source）支持 80 kbps。还要求设置 `BT_GMAP_UGT_FEAT_SOURCE`。 |
| `BT_GMAP_UGT_FEAT_SINK` | 支持接收端（Sink）。要求 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT > 0`。 |
| `BT_GMAP_UGT_FEAT_64KBPS_SINK` | 接收端（Sink）支持 64 kbps。还要求设置 `BT_GMAP_UGT_FEAT_SINK`。 |
| `BT_GMAP_UGT_FEAT_MULTIPLEX` | 支持在一个服务数据单元（SDU）的每个块（Block）中接收多个 LC3 编解码器帧（Codec Frame）。还要求设置 `BT_GMAP_UGT_FEAT_SINK`。 |
| `BT_GMAP_UGT_FEAT_MULTISINK` | 支持接收至少两个音频声道（Audio Channel），每个声道位于独立的连接等时流（CIS）中。要求 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT > 1` 且 `CONFIG_BT_ASCS_MAX_ACTIVE_ASES > 1`，并且还须设置 `BT_GMAP_UGT_FEAT_SINK`。 |
| `BT_GMAP_UGT_FEAT_MULTISOURCE` | 支持发送至少两个音频声道（Audio Channel），每个声道位于独立的连接等时流（CIS）中。要求 `CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT > 1` 且 `CONFIG_BT_ASCS_MAX_ACTIVE_ASES > 1`，并且还须设置 `BT_GMAP_UGT_FEAT_SOURCE`。 |

<a id="gacc4853bf69d0a13353fc941aa7e4e190"></a>

### `bt_gmap_cb_register()`

```c
int bt_gmap_cb_register ( const struct bt_gmap_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

注册游戏音频配置文件（Gaming Audio Profile）使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | 回调（Callbacks）已经注册时。 |
| `0` | 成功时返回。 |

<a id="gab54963e226753d44085a7d1f5dccdef6"></a>

### `bt_gmap_discover()`

```c
int bt_gmap_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

在远端设备上发现游戏服务（Gaming Service）。

在 `conn` 标识的服务器上查找游戏服务（Gaming Service）的过程。发现过程（Discovery Procedure）完成或失败时，调用 `bt_gmap_cb::discover` 回调。发现成功时，回调包含远端设备的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `conn` 为 `NULL` 时。 |
| `-EBUSY` | `conn` 的发现过程（Discovery）已经在进行时。 |
| `-ENOTCONN` | `conn` 未连接时。 |
| `-ENOEXEC` | 无法发起发现过程（Discovery）时。 |
| `0` | 成功时返回。 |

<a id="ga75211707bbdceff35235c353dc8c7609"></a>

### `bt_gmap_register()`

```c
int bt_gmap_register ( enum bt_gmap_role role, struct bt_gmap_feat features )
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

将游戏音频服务（GMAS）实例加入数据库，并设置收到的游戏音频配置文件（Gaming Audio Profile）角色。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role` | 设备的游戏音频配置文件角色（Gaming Audio Profile Roles），可指定一个或多个。 |
| `features` | 各角色的功能（Features）。如果 `role` 参数中没有某个角色，则忽略该角色的功能值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效（Invalid Arguments）时。 |
| `-ENOEXEC` | 服务注册（Service Registration）失败时。 |
| `0` | 成功时返回。 |

<a id="ga956efe257f06b627615a0a82d44db919"></a>

### `bt_gmap_set_role()`

```c
int bt_gmap_set_role ( enum bt_gmap_role role, struct bt_gmap_feat features )
```

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

动态设置一个或多个游戏音频配置文件（Gaming Audio Profile）角色和特性。

将覆盖先前注册的值。如果角色（Role）发生变化，将触发游戏音频服务（Gaming Audio Service，GMAS）的服务变更（Service Change）；如果仅功能（Feature）变化，则不会发生服务变更。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role` | 游戏音频配置文件角色（Gaming Audio Profile Roles）。 |
| `features` | 各角色的功能（Features）。如果 `role` 参数中没有某个角色，则忽略该角色的功能值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOEXEC` | 服务（Service）尚未注册时。 |
| `-EINVAL` | 参数无效（Invalid Arguments）时。 |
| `-EALREADY` | 角色（Role）和功能（Features）与现有值相同时。 |
| `-ENOENT` | 服务注销（Service Unregistration）失败时。 |
| `-ECANCELED` | 服务重新注册（Service Re-registration）失败时。 |
| `0` | 成功时返回。 |


## 2.5\_原页交叉引用（Cross References）

- [bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)
- [bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/gmap.h](../api_file_network_device_reference/P012_zephyr__bluetooth__audio__gmap.h_文件参考.md)
- [CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT)
- [CONFIG_BT_CAP_INITIATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_INITIATOR)
- [CONFIG_BT_BAP_UNICAST_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT)
- [CONFIG_BT_VCP_VOL_CTLR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VCP_VOL_CTLR)
- [CONFIG_BT_CAP_ACCEPTOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_ACCEPTOR)
- [CONFIG_BT_BAP_UNICAST_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_SERVER)
- [CONFIG_BT_BAP_BROADCAST_SOURCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SOURCE)
- [CONFIG_BT_BAP_BROADCAST_SINK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SINK)
- [CONFIG_BT_VCP_VOL_REND](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VCP_VOL_REND)
- [CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT)
- [CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT)
- [CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT)
- [CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT)
- [CONFIG_BT_ASCS_MAX_ACTIVE_ASES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS_MAX_ACTIVE_ASES)
- [bt_gmap_cb::discover](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md#a72c25ae277e04d419f41733d0b11aefc)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630"></a>
<a id="gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6"></a>
<a id="gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8"></a>
<a id="gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251"></a>
<a id="gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b"></a>
<a id="gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6"></a>
<a id="gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091"></a>
<a id="gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e"></a>
<a id="gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331"></a>
<a id="gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08"></a>
<a id="gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_蓝牙音频（Bluetooth Audio）.md) · [返回大纲](大纲.md) · [下一章](P003_nPM10xx 充电器接口（Charger interface）.md)
