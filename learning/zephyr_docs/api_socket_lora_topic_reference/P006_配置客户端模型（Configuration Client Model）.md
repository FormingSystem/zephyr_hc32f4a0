---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-6
title: 配置客户端模型（Configuration Client Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_配置客户端模型（Configuration Client Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置客户端模型（Configuration Client Model）

<a id="details"></a>

配置客户端模型（Configuration Client Model）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fcfg_5Fcli_5Fcb"></a>

```c
struct bt_mesh_cfg_cli_cb
```

相关声明：[bt_mesh_cfg_cli_cb](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md)。

Mesh配置客户端（Configuration Client）状态消息的回调。

<a id="r_bt_5Fmesh_5Fcfg_5Fcli"></a>

```c
struct bt_mesh_cfg_cli
```

相关声明：[bt_mesh_cfg_cli](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md)。

Mesh配置客户端（Configuration Client）的模型上下文。

<a id="r_bt_5Fmesh_5Fcfg_5Fcli_5Fmod_5Fpub"></a>

```c
struct bt_mesh_cfg_cli_mod_pub
```

相关声明：[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)。

模型发布（Model Publication）的配置参数。

<a id="r_bt_5Fmesh_5Fcfg_5Fcli_5Fhb_5Fsub"></a>

```c
struct bt_mesh_cfg_cli_hb_sub
```

相关声明：[bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)。

心跳订阅（Heartbeat Subscription）的配置参数。

<a id="r_bt_5Fmesh_5Fcfg_5Fcli_5Fhb_5Fpub"></a>

```c
struct bt_mesh_cfg_cli_hb_pub
```

相关声明：[bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)。

心跳发布（Heartbeat Publication）的配置参数。

<a id="r_bt_5Fmesh_5Fcomp_5Fp0"></a>

```c
struct bt_mesh_comp_p0
```

相关声明：[bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)。

解析后的组成数据（Composition Data）第0页表示。

<a id="r_bt_5Fmesh_5Fcomp_5Fp0_5Felem"></a>

```c
struct bt_mesh_comp_p0_elem
```

相关声明：[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

组成数据（Composition Data）第0页的元素表示。

<a id="r_bt_5Fmesh_5Fcomp_5Fp1_5Felem"></a>

```c
struct bt_mesh_comp_p1_elem
```

相关声明：[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)。

组成数据（Composition Data）第1页的元素表示。

<a id="r_bt_5Fmesh_5Fcomp_5Fp1_5Fmodel_5Fitem"></a>

```c
struct bt_mesh_comp_p1_model_item
```

相关声明：[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)。

组成数据（Composition Data）第1页的模型项表示。

<a id="r_bt_5Fmesh_5Fcomp_5Fp1_5Fitem_5Fshort"></a>

```c
struct bt_mesh_comp_p1_item_short
```

相关声明：[bt_mesh_comp_p1_item_short](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md)。

短格式表示的扩展模型项（Extended Model Item）。

<a id="r_bt_5Fmesh_5Fcomp_5Fp1_5Fitem_5Flong"></a>

```c
struct bt_mesh_comp_p1_item_long
```

相关声明：[bt_mesh_comp_p1_item_long](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md)。

长格式表示的扩展模型项（Extended Model Item）。

<a id="r_bt_5Fmesh_5Fcomp_5Fp1_5Fext_5Fitem"></a>

```c
struct bt_mesh_comp_p1_ext_item
```

相关声明：[bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)。

扩展模型项（Extended Model Item）。

<a id="r_bt_5Fmesh_5Fcomp_5Fp2_5Frecord"></a>

```c
struct bt_mesh_comp_p2_record
```

相关声明：[bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)。

组成数据（Composition Data）第2页记录的解析结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga2f0df6906a27ebbd86dcd11951114001"></a>

```c
#define BT_MESH_MODEL_CFG_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_CFG_CLI](#ga2f0df6906a27ebbd86dcd11951114001)。

通用配置客户端模型（Generic Configuration Client Model）的组成数据条目（Composition Data Entry）。

<a id="r_gab542c707fb5bad0a15088fefda775a42"></a>

```c
#define BT_MESH_PUB_PERIOD_100MS(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_100MS](#gab542c707fb5bad0a15088fefda775a42)。

以 100 ms 为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga29435e527a73ff6e19339b773c8eb79e"></a>

```c
#define BT_MESH_PUB_PERIOD_SEC(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_SEC](#ga29435e527a73ff6e19339b773c8eb79e)。

以 1 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga654204077adaa08259d1afbfe92e070e"></a>

```c
#define BT_MESH_PUB_PERIOD_10SEC(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_10SEC](#ga654204077adaa08259d1afbfe92e070e)。

以 10 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga36c37f644ee39ad91b6167f68c806b7e"></a>

```c
#define BT_MESH_PUB_PERIOD_10MIN(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_10MIN](#ga36c37f644ee39ad91b6167f68c806b7e)。

以 10 分钟为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_gac6675d227749a69cedc5455c70626b76"></a>

```c
int bt_mesh_cfg_cli_node_reset (uint16_t net_idx, uint16_t addr, bool *status)
```

相关声明：[bt_mesh_cfg_cli_node_reset](#gac6675d227749a69cedc5455c70626b76)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

复位目标节点，并将其从网络中移除。

<a id="r_ga36259e9c811a8f1a21d642739cf297df"></a>

```c
int bt_mesh_cfg_cli_comp_data_get (uint16_t net_idx, uint16_t addr, uint8_t page, uint8_t *rsp, struct net_buf_simple *comp)
```

相关声明：[bt_mesh_cfg_cli_comp_data_get](#ga36259e9c811a8f1a21d642739cf297df)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取目标节点的组成数据（Composition Data）。

<a id="r_ga2c8a79d1b70e91e0a09c848737bb4a22"></a>

```c
int bt_mesh_cfg_cli_beacon_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_beacon_get](#ga2c8a79d1b70e91e0a09c848737bb4a22)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的网络信标状态（Network Beacon State）。

<a id="r_ga660df68049110332ff21610fe4e520c6"></a>

```c
int bt_mesh_cfg_cli_krp_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint8_t *phase)
```

相关声明：[bt_mesh_cfg_cli_krp_get](#ga660df68049110332ff21610fe4e520c6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的网络密钥刷新阶段状态（Network Key Refresh Phase State）。

<a id="r_gae51eee59090cfebed4561ed3bb4df005"></a>

```c
int bt_mesh_cfg_cli_krp_set (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t transition, uint8_t *status, uint8_t *phase)
```

相关声明：[bt_mesh_cfg_cli_krp_set](#gae51eee59090cfebed4561ed3bb4df005)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络密钥刷新阶段参数（Network Key Refresh Phase Parameters）。

<a id="r_gab513c82ebe434907a958cc6da990bd0b"></a>

```c
int bt_mesh_cfg_cli_beacon_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_beacon_set](#gab513c82ebe434907a958cc6da990bd0b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络信标状态（Network Beacon State）。

<a id="r_gaa141d4aabbed6c7780ac7f3955c8b580"></a>

```c
int bt_mesh_cfg_cli_ttl_get (uint16_t net_idx, uint16_t addr, uint8_t *ttl)
```

相关声明：[bt_mesh_cfg_cli_ttl_get](#gaa141d4aabbed6c7780ac7f3955c8b580)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的生存时间（Time To Live，TTL）值。

<a id="r_ga2671234d739c802fd080a19d01235352"></a>

```c
int bt_mesh_cfg_cli_ttl_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *ttl)
```

相关声明：[bt_mesh_cfg_cli_ttl_set](#ga2671234d739c802fd080a19d01235352)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的生存时间（Time To Live，TTL）值。

<a id="r_ga4dd1534e9d5b04fc99231ba5dde23e05"></a>

```c
int bt_mesh_cfg_cli_friend_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_friend_get](#ga4dd1534e9d5b04fc99231ba5dde23e05)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的友元功能状态（Friend Feature Status）。

<a id="r_gacf8ad783910449c7cdc304c1b9b3fe0b"></a>

```c
int bt_mesh_cfg_cli_friend_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_friend_set](#gacf8ad783910449c7cdc304c1b9b3fe0b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的友元功能状态（Friend Feature State）。

<a id="r_gaaf945377cf6a3d2b3e7c7cdb5a8df016"></a>

```c
int bt_mesh_cfg_cli_gatt_proxy_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_gatt_proxy_get](#gaaf945377cf6a3d2b3e7c7cdb5a8df016)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的代理功能状态（Proxy Feature State）。

<a id="r_ga5a717835a416ba2930f65a975265649f"></a>

```c
int bt_mesh_cfg_cli_gatt_proxy_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_gatt_proxy_set](#ga5a717835a416ba2930f65a975265649f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的代理功能状态（Proxy Feature State）。

<a id="r_ga92ee7984b14590ed11a470c0dfea0bc9"></a>

```c
int bt_mesh_cfg_cli_net_transmit_get (uint16_t net_idx, uint16_t addr, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_net_transmit_get](#ga92ee7984b14590ed11a470c0dfea0bc9)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的 `network_transmit` 状态（Network Transmit State）。

<a id="r_ga87f7c1e06b5c721c89031c527960bf40"></a>

```c
int bt_mesh_cfg_cli_net_transmit_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_net_transmit_set](#ga87f7c1e06b5c721c89031c527960bf40)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络发送参数（Network Transmit Parameters）。

<a id="r_ga4a50a6a5dcfdc42b7476f0b9e463ea45"></a>

```c
int bt_mesh_cfg_cli_relay_get (uint16_t net_idx, uint16_t addr, uint8_t *status, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_relay_get](#ga4a50a6a5dcfdc42b7476f0b9e463ea45)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的中继功能状态（Relay Feature State）。

<a id="r_ga7fe8418130568bdf2a5e56ed2ad027b0"></a>

```c
int bt_mesh_cfg_cli_relay_set (uint16_t net_idx, uint16_t addr, uint8_t new_relay, uint8_t new_transmit, uint8_t *status, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_relay_set](#ga7fe8418130568bdf2a5e56ed2ad027b0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的中继参数（Relay Parameters）。

<a id="r_ga283fb06ddb6427852ff0ac556d3c1852"></a>

```c
int bt_mesh_cfg_cli_net_key_add (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_add](#ga283fb06ddb6427852ff0ac556d3c1852)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向目标节点添加网络密钥（Network Key）。

<a id="r_gab42c5bdff36bea35e967946462b12457"></a>

```c
int bt_mesh_cfg_cli_net_key_get (uint16_t net_idx, uint16_t addr, uint16_t *keys, size_t *key_cnt)
```

相关声明：[bt_mesh_cfg_cli_net_key_get](#gab42c5bdff36bea35e967946462b12457)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点的网络密钥索引列表（Network Key Indexes）。

<a id="r_gab2963ec5536cb4b941578bb490fdc013"></a>

```c
int bt_mesh_cfg_cli_net_key_del (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_del](#gab2963ec5536cb4b941578bb490fdc013)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从目标节点删除网络密钥（Network Key）。

<a id="r_gafabf4c0fa707eba1fd40cc9a403daa07"></a>

```c
int bt_mesh_cfg_cli_app_key_add (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_add](#gafabf4c0fa707eba1fd40cc9a403daa07)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向目标节点添加应用密钥（Application Key）。

<a id="r_ga6391ce297ca0be73ccd51044a9e0a76f"></a>

```c
int bt_mesh_cfg_cli_app_key_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint16_t *keys, size_t *key_cnt)
```

相关声明：[bt_mesh_cfg_cli_app_key_get](#ga6391ce297ca0be73ccd51044a9e0a76f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上与指定网络密钥关联的应用密钥索引列表（Application Key Indexes）。

<a id="r_ga5140472c687584babf885bc08349c865"></a>

```c
int bt_mesh_cfg_cli_app_key_del (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_del](#ga5140472c687584babf885bc08349c865)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从目标节点删除应用密钥（Application Key）。

<a id="r_gaa4a02dd0c1f67621ee71d011fe4a29c1"></a>

```c
int bt_mesh_cfg_cli_mod_app_bind (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_bind](#gaa4a02dd0c1f67621ee71d011fe4a29c1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将应用（Application）绑定到目标节点上的 SIG 模型。

<a id="r_gaf82b54a4b2d3176b10daf728272a0977"></a>

```c
int bt_mesh_cfg_cli_mod_app_unbind (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_unbind](#gaf82b54a4b2d3176b10daf728272a0977)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解除应用（Application）与目标节点上 SIG 模型的绑定。

<a id="r_gada33602562721c9f413eb06b34a823a8"></a>

```c
int bt_mesh_cfg_cli_mod_app_bind_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_bind_vnd](#gada33602562721c9f413eb06b34a823a8)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将应用（Application）绑定到目标节点上的厂商模型（Vendor Model）。

<a id="r_ga1fb53b9a49be25e633cac9d668c5b209"></a>

```c
int bt_mesh_cfg_cli_mod_app_unbind_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_unbind_vnd](#ga1fb53b9a49be25e633cac9d668c5b209)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解除应用（Application）与目标节点上厂商模型（Vendor Model）的绑定。

<a id="r_ga67cf5ff993f2444cc66b2ae5353865d2"></a>

```c
int bt_mesh_cfg_cli_mod_app_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status, uint16_t *apps, size_t *app_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_app_get](#ga67cf5ff993f2444cc66b2ae5353865d2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取绑定到目标节点上 SIG 模型的所有应用（Applications）的列表。

<a id="r_gaf7e0f85bbbbfc382bfe4aea8298227d1"></a>

```c
int bt_mesh_cfg_cli_mod_app_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *apps, size_t *app_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_app_get_vnd](#gaf7e0f85bbbbfc382bfe4aea8298227d1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取绑定到目标节点上厂商模型（Vendor Model）的所有应用（Applications）的列表。

<a id="r_ga1b36596a20ca8751006b0f7f2221067d"></a>

```c
int bt_mesh_cfg_cli_mod_pub_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_get](#ga1b36596a20ca8751006b0f7f2221067d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点上 SIG 模型的发布参数（Publish Parameters）。

<a id="r_ga0bc2c24403e0cd79a061ba1244b1a1db"></a>

```c
int bt_mesh_cfg_cli_mod_pub_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_get_vnd](#ga0bc2c24403e0cd79a061ba1244b1a1db)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

<a id="r_ga7fc2acda16f3f03a929c38796c67028e"></a>

```c
int bt_mesh_cfg_cli_mod_pub_set (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_set](#ga7fc2acda16f3f03a929c38796c67028e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点上 SIG 模型的发布参数（Publish Parameters）。

<a id="r_gad2c602a2685ff38c0e78c1990b244e54"></a>

```c
int bt_mesh_cfg_cli_mod_pub_set_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_set_vnd](#gad2c602a2685ff38c0e78c1990b244e54)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

<a id="r_gaf4ee720ce27eea9602b59a380278bb57"></a>

```c
int bt_mesh_cfg_cli_mod_sub_add (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_add](#gaf4ee720ce27eea9602b59a380278bb57)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SIG 模型的订阅列表（Subscription List）添加组地址（Group Address）。

<a id="r_ga3ba34f8be138bc62a7eb7859b18dc441"></a>

```c
int bt_mesh_cfg_cli_mod_sub_add_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_add_vnd](#ga3ba34f8be138bc62a7eb7859b18dc441)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加组地址（Group Address）。

<a id="r_ga8d8595f077267b7d784fde30cbc4b207"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del](#ga8d8595f077267b7d784fde30cbc4b207)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SIG 模型的订阅列表（Subscription List）删除组地址（Group Address）。

<a id="r_ga74bad73184af2d6ce71134831f70680d"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_vnd](#ga74bad73184af2d6ce71134831f70680d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除组地址（Group Address）。

<a id="r_gadac1cc360c30d290a861bbd534fca58d"></a>

```c
int bt_mesh_cfg_cli_mod_sub_overwrite (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_overwrite](#gadac1cc360c30d290a861bbd534fca58d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个组地址（Group Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

<a id="r_ga69b2dfacc27ed94b9e1331ff4ac4b582"></a>

```c
int bt_mesh_cfg_cli_mod_sub_overwrite_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_overwrite_vnd](#ga69b2dfacc27ed94b9e1331ff4ac4b582)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个组地址（Group Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

<a id="r_ga2d22612cf9dc5030699bf7c6c58bf6d5"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_add (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_add](#ga2d22612cf9dc5030699bf7c6c58bf6d5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SIG 模型的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

<a id="r_gaa3a10a54a18a99d0b4b0aa85330b1640"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_add_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_add_vnd](#gaa3a10a54a18a99d0b4b0aa85330b1640)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

<a id="r_gaf7107373fc0c70d091e9a521d8b641ad"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_del (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_del](#gaf7107373fc0c70d091e9a521d8b641ad)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SIG 模型的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

<a id="r_ga8884786e3ec349bcb8b89b60aa11f198"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_del_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_del_vnd](#ga8884786e3ec349bcb8b89b60aa11f198)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

<a id="r_ga69809ad3f2cff8e1f394f6da6ed63264"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_overwrite](#ga69809ad3f2cff8e1f394f6da6ed63264)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个虚拟地址（Virtual Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

<a id="r_ga70d3bb7fb914fa3685f4ad9b561a48b6"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd](#ga70d3bb7fb914fa3685f4ad9b561a48b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个虚拟地址（Virtual Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

<a id="r_gaf739e5e3a4b225e10bf2aedf143d7793"></a>

```c
int bt_mesh_cfg_cli_mod_sub_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status, uint16_t *subs, size_t *sub_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_get](#gaf739e5e3a4b225e10bf2aedf143d7793)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上 SIG 模型的订阅列表（Subscription List）。

<a id="r_ga09e751a9071402ae978c0355edfbdf03"></a>

```c
int bt_mesh_cfg_cli_mod_sub_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *subs, size_t *sub_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_get_vnd](#ga09e751a9071402ae978c0355edfbdf03)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上厂商模型（Vendor Model）的订阅列表（Subscription List）。

<a id="r_ga1adae658bf8f4512a7d80d0194dcb362"></a>

```c
int bt_mesh_cfg_cli_hb_sub_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_sub_set](#ga1adae658bf8f4512a7d80d0194dcb362)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

<a id="r_ga86e5de1b216d62b7c77bf43b7af062fc"></a>

```c
int bt_mesh_cfg_cli_hb_sub_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_sub_get](#ga86e5de1b216d62b7c77bf43b7af062fc)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

<a id="r_ga352eb00b78ff978a1a1e81ec5a0575b8"></a>

```c
int bt_mesh_cfg_cli_hb_pub_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_cfg_cli_hb_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_pub_set](#ga352eb00b78ff978a1a1e81ec5a0575b8)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_ga07c443476adef9c7bb573ffbb8d1b1ce"></a>

```c
int bt_mesh_cfg_cli_hb_pub_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_pub_get](#ga07c443476adef9c7bb573ffbb8d1b1ce)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_gacd647905484fa8319a5377aa5777c254"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_all (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_all](#gacd647905484fa8319a5377aa5777c254)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除 SIG 模型订阅列表（Subscription List）中的所有组地址（Group Addresses）。

<a id="r_ga2059ccbc689af9c2127e4e399ea5bd43"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_all_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_all_vnd](#ga2059ccbc689af9c2127e4e399ea5bd43)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除厂商模型（Vendor Model）订阅列表中的所有组地址（Group Addresses）。

<a id="r_gafdaff279685b821a7b205e45feed9a05"></a>

```c
int bt_mesh_cfg_cli_net_key_update (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_update](#gafdaff279685b821a7b205e45feed9a05)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新目标节点上的网络密钥（Network Key）。

<a id="r_gacf1bd7a771a45981a82eeea0dcce01b7"></a>

```c
int bt_mesh_cfg_cli_app_key_update (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_update](#gacf1bd7a771a45981a82eeea0dcce01b7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新目标节点上的应用密钥（Application Key）。

<a id="r_ga12a8618d2b73f30742f8e8d2bdddc138"></a>

```c
int bt_mesh_cfg_cli_node_identity_set (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t new_identity, uint8_t *status, uint8_t *identity)
```

相关声明：[bt_mesh_cfg_cli_node_identity_set](#ga12a8618d2b73f30742f8e8d2bdddc138)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置节点身份参数（Node Identity Parameters）。

<a id="r_gac02c170e260980d5b749b581910672d2"></a>

```c
int bt_mesh_cfg_cli_node_identity_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint8_t *identity)
```

相关声明：[bt_mesh_cfg_cli_node_identity_get](#gac02c170e260980d5b749b581910672d2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取节点身份参数（Node Identity Parameters）。

<a id="r_ga0ee1d0849d632b5d806ee31c87bbc888"></a>

```c
int bt_mesh_cfg_cli_lpn_timeout_get (uint16_t net_idx, uint16_t addr, uint16_t unicast_addr, int32_t *polltimeout)
```

相关声明：[bt_mesh_cfg_cli_lpn_timeout_get](#ga0ee1d0849d632b5d806ee31c87bbc888)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取低功耗节点轮询超时参数（Low Power Node Polltimeout Parameters）。

<a id="r_gaf5262c0a27e4b9249ecf908c259cc7d7"></a>

```c
int32_t bt_mesh_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_cfg_cli_timeout_get](#gaf5262c0a27e4b9249ecf908c259cc7d7)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga7e3521ae973dc825422c6dd5f07ef547"></a>

```c
void bt_mesh_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_cfg_cli_timeout_set](#ga7e3521ae973dc825422c6dd5f07ef547)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

<a id="r_ga1f79d98273a984f1c49b4d5dd5bf8d30"></a>

```c
int bt_mesh_comp_p0_get (struct bt_mesh_comp_p0 *comp, struct net_buf_simple *buf)
```

相关声明：[bt_mesh_comp_p0_get](#ga1f79d98273a984f1c49b4d5dd5bf8d30)、[bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区创建组成数据第 0 页（Composition Data Page 0）的表示。

<a id="r_gaa6d60ebad6dc4a4f5b022937dbae3120"></a>

```c
struct bt_mesh_comp_p0_elem * bt_mesh_comp_p0_elem_pull (const struct bt_mesh_comp_p0 *comp, struct bt_mesh_comp_p0_elem *elem)
```

相关声明：[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)、[bt_mesh_comp_p0_elem_pull](#gaa6d60ebad6dc4a4f5b022937dbae3120)、[bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从组成数据第 0 页（Composition Data Page 0）的实例中取出一个第 0 页元素（Element）。

<a id="r_gac005f52e191c3e5628f063dbc1a19645"></a>

```c
uint16_t bt_mesh_comp_p0_elem_mod (struct bt_mesh_comp_p0_elem *elem, int idx)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_comp_p0_elem_mod](#gac005f52e191c3e5628f063dbc1a19645)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取 SIG 模型。

<a id="r_ga4f656102982961b7bf2e3d3896a2240e"></a>

```c
struct bt_mesh_mod_id_vnd bt_mesh_comp_p0_elem_mod_vnd (struct bt_mesh_comp_p0_elem *elem, int idx)
```

相关声明：[bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)、[bt_mesh_comp_p0_elem_mod_vnd](#ga4f656102982961b7bf2e3d3896a2240e)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取厂商模型（Vendor Model）。

<a id="r_gae9a19b089d898af914ea5c287aca8fba"></a>

```c
struct bt_mesh_comp_p1_elem * bt_mesh_comp_p1_elem_pull (struct net_buf_simple *buf, struct bt_mesh_comp_p1_elem *elem)
```

相关声明：[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)、[bt_mesh_comp_p1_elem_pull](#gae9a19b089d898af914ea5c287aca8fba)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)。

从组成数据第 1 页（Composition Data Page 1）的实例中取出一个第 1 页元素（Element）。

<a id="r_gac8b4b670c82b80a51834f7ef32206985"></a>

```c
struct bt_mesh_comp_p1_model_item * bt_mesh_comp_p1_item_pull (struct bt_mesh_comp_p1_elem *elem, struct bt_mesh_comp_p1_model_item *item)
```

相关声明：[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)、[bt_mesh_comp_p1_item_pull](#gac8b4b670c82b80a51834f7ef32206985)、[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)、[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)。

从组成数据第 1 页元素（Composition Data Page 1 Element）中取出一个第 1 页模型项（Model Item）。

<a id="r_gac527fe27308c8a61ac1831af9605e429"></a>

```c
struct bt_mesh_comp_p1_ext_item * bt_mesh_comp_p1_pull_ext_item (struct bt_mesh_comp_p1_model_item *item, struct bt_mesh_comp_p1_ext_item *ext_item)
```

相关声明：[bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)、[bt_mesh_comp_p1_pull_ext_item](#gac527fe27308c8a61ac1831af9605e429)、[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)、[bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)。

取出模型项（Model Item）中包含的扩展模型项（Extended Model Item）。

<a id="r_ga0854a494707a40b84beb8582f45e0470"></a>

```c
struct bt_mesh_comp_p2_record * bt_mesh_comp_p2_record_pull (struct net_buf_simple *buf, struct bt_mesh_comp_p2_record *record)
```

相关声明：[bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)、[bt_mesh_comp_p2_record_pull](#ga0854a494707a40b84beb8582f45e0470)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)。

从组成数据第 2 页（Composition Data Page 2）的实例中取出一个第 2 页记录（Record）。

<a id="r_gaa411ab7db2e71a114a8108eaec9ca12c"></a>

```c
int bt_mesh_key_idx_unpack_list (struct net_buf_simple *buf, uint16_t *dst_arr, size_t *dst_cnt)
```

相关声明：[bt_mesh_key_idx_unpack_list](#gaa411ab7db2e71a114a8108eaec9ca12c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从缓冲区解包密钥索引条目列表（Key Index Entries）。

## 6.4\_详细说明（Detailed Documentation）

<a id="ga2f0df6906a27ebbd86dcd11951114001"></a>

### `BT_MESH_MODEL_CFG_CLI`

```c
#define BT_MESH_MODEL_CFG_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CNT_CB(BT_MESH_MODEL_ID_CFG_CLI,  \
                     bt_mesh_cfg_cli_op, NULL,  \
                     cli_data, 1, 0, &bt_mesh_cfg_cli_cb)
```

通用配置客户端模型（Generic Configuration Client Model）的组成数据条目（Composition Data Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli_data` | 指向配置客户端模型（Configuration Client Model）实例的指针。 |

<a id="gab542c707fb5bad0a15088fefda775a42"></a>

### `BT_MESH_PUB_PERIOD_100MS`

```c
#define BT_MESH_PUB_PERIOD_100MS ( steps)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

展开值（Value）：

```c
((steps) & BIT_MASK(6))
```

以 100 ms 为单位编码模型发布周期（Model Publication Period）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `steps` | 以 100 ms 为步长（Step）的步数。 |

**返回（Returns）**：返回值（Returns）：可赋给 `bt_mesh_cfg_cli_mod_pub.period` 的编码值（Encoded Value）。

<a id="ga36c37f644ee39ad91b6167f68c806b7e"></a>

### `BT_MESH_PUB_PERIOD_10MIN`

```c
#define BT_MESH_PUB_PERIOD_10MIN ( steps)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

展开值（Value）：

```c
(((steps) & BIT_MASK(6)) | (3 << 6))
```

以 10 分钟为单位编码模型发布周期（Model Publication Period）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `steps` | 以 10 分钟为步长（Step）的步数。 |

**返回（Returns）**：返回值（Returns）：可赋给 `bt_mesh_cfg_cli_mod_pub.period` 的编码值（Encoded Value）。

<a id="ga654204077adaa08259d1afbfe92e070e"></a>

### `BT_MESH_PUB_PERIOD_10SEC`

```c
#define BT_MESH_PUB_PERIOD_10SEC ( steps)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

展开值（Value）：

```c
(((steps) & BIT_MASK(6)) | (2 << 6))
```

以 10 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `steps` | 以 10 秒为步长（Step）的步数。 |

**返回（Returns）**：返回值（Returns）：可赋给 `bt_mesh_cfg_cli_mod_pub.period` 的编码值（Encoded Value）。

<a id="ga29435e527a73ff6e19339b773c8eb79e"></a>

### `BT_MESH_PUB_PERIOD_SEC`

```c
#define BT_MESH_PUB_PERIOD_SEC ( steps)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

展开值（Value）：

```c
(((steps) & BIT_MASK(6)) | (1 << 6))
```

以 1 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `steps` | 以 1 秒为步长（Step）的步数。 |

**返回（Returns）**：返回值（Returns）：可赋给 `bt_mesh_cfg_cli_mod_pub.period` 的编码值（Encoded Value）。

<a id="gafabf4c0fa707eba1fd40cc9a403daa07"></a>

### `bt_mesh_cfg_cli_app_key_add()`

```c
int bt_mesh_cfg_cli_app_key_add ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向目标节点添加应用密钥（Application Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 应用密钥（Application Key）所属的网络密钥索引（Network Key Index）。 |
| `key_app_idx` | 应用密钥索引（Application key index）。 |
| `app_key` | 应用密钥（Application Key）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga5140472c687584babf885bc08349c865"></a>

### `bt_mesh_cfg_cli_app_key_del()`

```c
int bt_mesh_cfg_cli_app_key_del ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从目标节点删除应用密钥（Application Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 应用密钥（Application Key）所属的网络密钥索引（Network Key Index）。 |
| `key_app_idx` | 应用密钥索引（Application key index）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga6391ce297ca0be73ccd51044a9e0a76f"></a>

### `bt_mesh_cfg_cli_app_key_get()`

```c
int bt_mesh_cfg_cli_app_key_get ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t * status, uint16_t * keys, size_t * key_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点上与指定网络密钥关联的应用密钥索引列表（Application Key Indexes）。

将 `status` 以及 `keys` 或 `key_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 要查询其应用密钥索引（App Key Indexes）的网络密钥索引（Network Key Index）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `keys` | 应用密钥索引列表（App Key Index List）的响应参数，将填入所有能够容纳的返回应用密钥索引。 |
| `key_cnt` | 应用密钥索引列表（App Key Index List）的长度。调用时应设为 `keys` 列表的容量；成功时返回实际返回的应用密钥索引数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gacf1bd7a771a45981a82eeea0dcce01b7"></a>

### `bt_mesh_cfg_cli_app_key_update()`

```c
int bt_mesh_cfg_cli_app_key_update ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

更新目标节点上的应用密钥（Application Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 应用密钥（Application Key）所属的网络密钥索引（Network Key Index）。 |
| `key_app_idx` | 应用密钥索引（Application key index）。 |
| `app_key` | 应用密钥（Application Key）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2c8a79d1b70e91e0a09c848737bb4a22"></a>

### `bt_mesh_cfg_cli_beacon_get()`

```c
int bt_mesh_cfg_cli_beacon_get ( uint16_t net_idx, uint16_t addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的网络信标状态（Network Beacon State）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（Status Response Parameter）；成功时返回 `BT_MESH_BEACON_DISABLED` 或 `BT_MESH_BEACON_ENABLED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gab513c82ebe434907a958cc6da990bd0b"></a>

### `bt_mesh_cfg_cli_beacon_set()`

```c
int bt_mesh_cfg_cli_beacon_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的网络信标状态（Network Beacon State）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的网络信标状态（Network Beacon State），应为 `BT_MESH_BEACON_DISABLED` 或 `BT_MESH_BEACON_ENABLED`。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_BEACON_DISABLED` 或 `BT_MESH_BEACON_ENABLED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga36259e9c811a8f1a21d642739cf297df"></a>

### `bt_mesh_cfg_cli_comp_data_get()`

```c
int bt_mesh_cfg_cli_comp_data_get ( uint16_t net_idx, uint16_t addr, uint8_t page, uint8_t * rsp, struct net_buf_simple * comp )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的组成数据（Composition Data）。

如果对端设备没有指定的组成数据页（Composition Data Page），将返回它所支持且小于请求页索引的最大页码。设备实际响应的页码通过 `rsp` 返回。

将 `rsp` 和 `comp` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `page` | 组成数据页（Composition Data Page）；使用 `0xff` 可请求第一个可用页。 |
| `rsp` | 用于接收返回页码（Page Number）的返回参数，或者 `NULL`。 |
| `comp` | 待填充的组成数据缓冲区（Composition Data Buffer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga4dd1534e9d5b04fc99231ba5dde23e05"></a>

### `bt_mesh_cfg_cli_friend_get()`

```c
int bt_mesh_cfg_cli_friend_get ( uint16_t net_idx, uint16_t addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的友元功能状态（Friend Feature Status）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_FRIEND_DISABLED`、`BT_MESH_FRIEND_ENABLED` 或 `BT_MESH_FRIEND_NOT_SUPPORTED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gacf8ad783910449c7cdc304c1b9b3fe0b"></a>

### `bt_mesh_cfg_cli_friend_set()`

```c
int bt_mesh_cfg_cli_friend_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的友元功能状态（Friend Feature State）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的友谊功能状态（Friend Feature State），应为 `BT_MESH_FRIEND_DISABLED` 或 `BT_MESH_FRIEND_ENABLED`。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_FRIEND_DISABLED`、`BT_MESH_FRIEND_ENABLED` 或 `BT_MESH_FRIEND_NOT_SUPPORTED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaaf945377cf6a3d2b3e7c7cdb5a8df016"></a>

### `bt_mesh_cfg_cli_gatt_proxy_get()`

```c
int bt_mesh_cfg_cli_gatt_proxy_get ( uint16_t net_idx, uint16_t addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的代理功能状态（Proxy Feature State）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_GATT_PROXY_DISABLED`、`BT_MESH_GATT_PROXY_ENABLED` 或 `BT_MESH_GATT_PROXY_NOT_SUPPORTED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga5a717835a416ba2930f65a975265649f"></a>

### `bt_mesh_cfg_cli_gatt_proxy_set()`

```c
int bt_mesh_cfg_cli_gatt_proxy_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的代理功能状态（Proxy Feature State）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的代理功能状态（Proxy Feature State），必须为 `BT_MESH_GATT_PROXY_DISABLED` 或 `BT_MESH_GATT_PROXY_ENABLED`。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_GATT_PROXY_DISABLED`、`BT_MESH_GATT_PROXY_ENABLED` 或 `BT_MESH_GATT_PROXY_NOT_SUPPORTED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga07c443476adef9c7bb573ffbb8d1b1ce"></a>

### `bt_mesh_cfg_cli_hb_pub_get()`

```c
int bt_mesh_cfg_cli_hb_pub_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的心跳发布参数（Heartbeat Publication Parameters）。

将 `status` 和 `pub` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `pub` | 用于返回心跳发布参数（Heartbeat Publication Parameters）的缓冲区。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga352eb00b78ff978a1a1e81ec5a0575b8"></a>

### `bt_mesh_cfg_cli_hb_pub_set()`

```c
int bt_mesh_cfg_cli_hb_pub_set ( uint16_t net_idx, uint16_t addr, const struct bt_mesh_cfg_cli_hb_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的心跳发布参数（Heartbeat Publication Parameters）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

`pub` 不得为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `pub` | 新的心跳发布参数（Heartbeat Publication Parameters）。 |
| `status` | 状态响应参数（status response parameter）。 |

**说明（Note）**：注意（Note）：目标节点（Target Node）必须已经收到指定的网络密钥（Network Key）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga86e5de1b216d62b7c77bf43b7af062fc"></a>

### `bt_mesh_cfg_cli_hb_sub_get()`

```c
int bt_mesh_cfg_cli_hb_sub_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub * sub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

将 `status` 和 `sub` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `sub` | 用于返回心跳订阅参数（Heartbeat Subscription Parameters）的缓冲区。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga1adae658bf8f4512a7d80d0194dcb362"></a>

### `bt_mesh_cfg_cli_hb_sub_set()`

```c
int bt_mesh_cfg_cli_hb_sub_set ( uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub * sub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

`sub` 不得为空（Null）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `sub` | 新的心跳订阅参数（Heartbeat Subscription Parameters）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga660df68049110332ff21610fe4e520c6"></a>

### `bt_mesh_cfg_cli_krp_get()`

```c
int bt_mesh_cfg_cli_krp_get ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t * status, uint8_t * phase )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的网络密钥刷新阶段状态（Network Key Refresh Phase State）。

将 `status` 和 `phase` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 网络密钥索引（Network key index）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `phase` | 指向待填充的密钥刷新变量（Key Refresh Variable）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gae51eee59090cfebed4561ed3bb4df005"></a>

### `bt_mesh_cfg_cli_krp_set()`

```c
int bt_mesh_cfg_cli_krp_set ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t transition, uint8_t * status, uint8_t * phase )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的网络密钥刷新阶段参数（Network Key Refresh Phase Parameters）。

将 `status` 和 `phase` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 网络密钥索引（Network key index）。 |
| `transition` | 转换参数（Transition Parameter）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `phase` | 指向新密钥刷新阶段（Key Refresh Phase）的指针；更新后返回实际的密钥刷新阶段。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga0ee1d0849d632b5d806ee31c87bbc888"></a>

### `bt_mesh_cfg_cli_lpn_timeout_get()`

```c
int bt_mesh_cfg_cli_lpn_timeout_get ( uint16_t net_idx, uint16_t addr, uint16_t unicast_addr, int32_t * polltimeout )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取低功耗节点轮询超时参数（Low Power Node Polltimeout Parameters）。

将 `polltimeout` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `unicast_addr` | 低功耗节点（LPN）的单播地址（Unicast Address）。 |
| `polltimeout` | 轮询超时（Poll Timeout）响应参数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaa4a02dd0c1f67621ee71d011fe4a29c1"></a>

### `bt_mesh_cfg_cli_mod_app_bind()`

```c
int bt_mesh_cfg_cli_mod_app_bind ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

将应用（Application）绑定到目标节点上的 SIG 模型。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_app_idx` | 待绑定的应用索引（Application Index）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gada33602562721c9f413eb06b34a823a8"></a>

### `bt_mesh_cfg_cli_mod_app_bind_vnd()`

```c
int bt_mesh_cfg_cli_mod_app_bind_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

将应用（Application）绑定到目标节点上的厂商模型（Vendor Model）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_app_idx` | 待绑定的应用索引（Application Index）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga67cf5ff993f2444cc66b2ae5353865d2"></a>

### `bt_mesh_cfg_cli_mod_app_get()`

```c
int bt_mesh_cfg_cli_mod_app_get ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t * status, uint16_t * apps, size_t * app_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取绑定到目标节点上 SIG 模型的所有应用（Applications）的列表。

将 `status` 以及 `apps` 或 `app_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `apps` | 应用索引列表（App Index List）的响应参数，将填入所有能够容纳的返回应用密钥索引（Application Key Indexes）。 |
| `app_cnt` | 应用索引列表（App Index List）的长度。调用时应设为 `apps` 列表的容量；成功时返回实际返回的应用密钥索引（Application Key Indexes）数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf7e0f85bbbbfc382bfe4aea8298227d1"></a>

### `bt_mesh_cfg_cli_mod_app_get_vnd()`

```c
int bt_mesh_cfg_cli_mod_app_get_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t * status, uint16_t * apps, size_t * app_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取绑定到目标节点上厂商模型（Vendor Model）的所有应用（Applications）的列表。

将 `status` 以及 `apps` 或 `app_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `apps` | 应用索引列表（App Index List）的响应参数，将填入所有能够容纳的返回应用密钥索引（Application Key Indexes）。 |
| `app_cnt` | 应用索引列表（App Index List）的长度。调用时应设为 `apps` 列表的容量；成功时返回实际返回的应用密钥索引（Application Key Indexes）数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf82b54a4b2d3176b10daf728272a0977"></a>

### `bt_mesh_cfg_cli_mod_app_unbind()`

```c
int bt_mesh_cfg_cli_mod_app_unbind ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

解除应用（Application）与目标节点上 SIG 模型的绑定。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_app_idx` | 待解除绑定的应用索引（Application Index）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga1fb53b9a49be25e633cac9d668c5b209"></a>

### `bt_mesh_cfg_cli_mod_app_unbind_vnd()`

```c
int bt_mesh_cfg_cli_mod_app_unbind_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

解除应用（Application）与目标节点上厂商模型（Vendor Model）的绑定。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_app_idx` | 待解除绑定的应用索引（Application Index）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga1b36596a20ca8751006b0f7f2221067d"></a>

### `bt_mesh_cfg_cli_mod_pub_get()`

```c
int bt_mesh_cfg_cli_mod_pub_get ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点上 SIG 模型的发布参数（Publish Parameters）。

将 `status` 和 `pub` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `pub` | 用于返回发布参数（Publication Parameters）的缓冲区。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga0bc2c24403e0cd79a061ba1244b1a1db"></a>

### `bt_mesh_cfg_cli_mod_pub_get_vnd()`

```c
int bt_mesh_cfg_cli_mod_pub_get_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

将 `status` 和 `pub` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `pub` | 用于返回发布参数（Publication Parameters）的缓冲区。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga7fc2acda16f3f03a929c38796c67028e"></a>

### `bt_mesh_cfg_cli_mod_pub_set()`

```c
int bt_mesh_cfg_cli_mod_pub_set ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点上 SIG 模型的发布参数（Publish Parameters）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

`pub` 不得为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `pub` | 发布参数（Publication Parameters）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gad2c602a2685ff38c0e78c1990b244e54"></a>

### `bt_mesh_cfg_cli_mod_pub_set_vnd()`

```c
int bt_mesh_cfg_cli_mod_pub_set_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub * pub, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

`pub` 不得为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `pub` | 发布参数（Publication Parameters）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf4ee720ce27eea9602b59a380278bb57"></a>

### `bt_mesh_cfg_cli_mod_sub_add()`

```c
int bt_mesh_cfg_cli_mod_sub_add ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向 SIG 模型的订阅列表（Subscription List）添加组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga3ba34f8be138bc62a7eb7859b18dc441"></a>

### `bt_mesh_cfg_cli_mod_sub_add_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_add_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga8d8595f077267b7d784fde30cbc4b207"></a>

### `bt_mesh_cfg_cli_mod_sub_del()`

```c
int bt_mesh_cfg_cli_mod_sub_del ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从 SIG 模型的订阅列表（Subscription List）删除组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gacd647905484fa8319a5377aa5777c254"></a>

### `bt_mesh_cfg_cli_mod_sub_del_all()`

```c
int bt_mesh_cfg_cli_mod_sub_del_all ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

删除 SIG 模型订阅列表（Subscription List）中的所有组地址（Group Addresses）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2059ccbc689af9c2127e4e399ea5bd43"></a>

### `bt_mesh_cfg_cli_mod_sub_del_all_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_del_all_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

删除厂商模型（Vendor Model）订阅列表中的所有组地址（Group Addresses）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga74bad73184af2d6ce71134831f70680d"></a>

### `bt_mesh_cfg_cli_mod_sub_del_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_del_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf739e5e3a4b225e10bf2aedf143d7793"></a>

### `bt_mesh_cfg_cli_mod_sub_get()`

```c
int bt_mesh_cfg_cli_mod_sub_get ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t * status, uint16_t * subs, size_t * sub_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点上 SIG 模型的订阅列表（Subscription List）。

将 `status` 以及 `subs` 或 `sub_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `subs` | 订阅列表（Subscription List）的响应参数，将填入所有能够容纳的返回订阅。 |
| `sub_cnt` | 订阅列表元素数（Subscription List Element Count）。调用时应设为 `subs` 列表的容量；成功时返回实际返回的订阅数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga09e751a9071402ae978c0355edfbdf03"></a>

### `bt_mesh_cfg_cli_mod_sub_get_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_get_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t * status, uint16_t * subs, size_t * sub_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点上厂商模型（Vendor Model）的订阅列表（Subscription List）。

将 `status` 以及 `subs` 或 `sub_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `subs` | 订阅列表（Subscription List）的响应参数，将填入所有能够容纳的返回订阅。 |
| `sub_cnt` | 订阅列表元素数（Subscription List Element Count）。调用时应设为 `subs` 列表的容量；成功时返回实际返回的订阅数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gadac1cc360c30d290a861bbd534fca58d"></a>

### `bt_mesh_cfg_cli_mod_sub_overwrite()`

```c
int bt_mesh_cfg_cli_mod_sub_overwrite ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

用一个组地址（Group Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

删除模型订阅列表（Model Subscription List）中的全部订阅，改为添加单个组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga69b2dfacc27ed94b9e1331ff4ac4b582"></a>

### `bt_mesh_cfg_cli_mod_sub_overwrite_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_overwrite_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

用一个组地址（Group Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

删除模型订阅列表（Model Subscription List）中的全部订阅，改为添加单个组地址（Group Address）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `sub_addr` | 要添加到订阅列表（Subscription List）的组地址（Group Address）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2d22612cf9dc5030699bf7c6c58bf6d5"></a>

### `bt_mesh_cfg_cli_mod_sub_va_add()`

```c
int bt_mesh_cfg_cli_mod_sub_va_add ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向 SIG 模型的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址标签（Virtual Address Label）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaa3a10a54a18a99d0b4b0aa85330b1640"></a>

### `bt_mesh_cfg_cli_mod_sub_va_add_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_va_add_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址标签（Virtual Address Label）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf7107373fc0c70d091e9a521d8b641ad"></a>

### `bt_mesh_cfg_cli_mod_sub_va_del()`

```c
int bt_mesh_cfg_cli_mod_sub_va_del ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从 SIG 模型的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址参数（Virtual Address Parameter）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga8884786e3ec349bcb8b89b60aa11f198"></a>

### `bt_mesh_cfg_cli_mod_sub_va_del_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_va_del_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址标签（Virtual Address Label）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga69809ad3f2cff8e1f394f6da6ed63264"></a>

### `bt_mesh_cfg_cli_mod_sub_va_overwrite()`

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

用一个虚拟地址（Virtual Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

删除模型订阅列表（Model Subscription List）中的全部订阅，改为添加单个组地址（Group Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址标签（Virtual Address Label）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga70d3bb7fb914fa3685f4ad9b561a48b6"></a>

### `bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd()`

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd ( uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t * virt_addr, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

用一个虚拟地址（Virtual Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

删除模型订阅列表（Model Subscription List）中的全部订阅，改为添加单个组地址（Group Address）。

将 `status` 和 `virt_addr` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `elem_addr` | 模型（Model）所在的元素地址（Element Address）。 |
| `label` | 要添加到订阅列表（Subscription List）的虚拟地址标签（Virtual Address Label）。 |
| `mod_id` | 模型标识符（Model ID）。 |
| `cid` | 模型的公司 ID（Company ID）。 |
| `virt_addr` | 虚拟地址（Virtual Address）响应参数。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga283fb06ddb6427852ff0ac556d3c1852"></a>

### `bt_mesh_cfg_cli_net_key_add()`

```c
int bt_mesh_cfg_cli_net_key_add ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

向目标节点添加网络密钥（Network Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 网络密钥索引（Network key index）。 |
| `net_key` | 网络密钥（Network Key）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gab2963ec5536cb4b941578bb490fdc013"></a>

### `bt_mesh_cfg_cli_net_key_del()`

```c
int bt_mesh_cfg_cli_net_key_del ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从目标节点删除网络密钥（Network Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 网络密钥索引（Network key index）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gab42c5bdff36bea35e967946462b12457"></a>

### `bt_mesh_cfg_cli_net_key_get()`

```c
int bt_mesh_cfg_cli_net_key_get ( uint16_t net_idx, uint16_t addr, uint16_t * keys, size_t * key_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的网络密钥索引列表（Network Key Indexes）。

将 `keys` 或 `key_cnt` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `keys` | 网络密钥索引列表（Net Key Index List）的响应参数，将填入所有能够容纳的返回网络密钥索引。 |
| `key_cnt` | 网络密钥索引列表（Net Key Index List）的长度。调用时应设为 `keys` 列表的容量；成功时返回实际返回的网络密钥索引数量。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gafdaff279685b821a7b205e45feed9a05"></a>

### `bt_mesh_cfg_cli_net_key_update()`

```c
int bt_mesh_cfg_cli_net_key_update ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

更新目标节点上的网络密钥（Network Key）。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 网络密钥索引（Network key index）。 |
| `net_key` | 网络密钥（Network Key）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga92ee7984b14590ed11a470c0dfea0bc9"></a>

### `bt_mesh_cfg_cli_net_transmit_get()`

```c
int bt_mesh_cfg_cli_net_transmit_get ( uint16_t net_idx, uint16_t addr, uint8_t * transmit )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的 `network_transmit` 状态（Network Transmit State）。

将 `transmit` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `transmit` | 网络发送（Network Transmit）响应参数。成功时返回编码后的网络传输参数，可通过 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 解码。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga87f7c1e06b5c721c89031c527960bf40"></a>

### `bt_mesh_cfg_cli_net_transmit_set()`

```c
int bt_mesh_cfg_cli_net_transmit_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * transmit )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的网络发送参数（Network Transmit Parameters）。

将 `transmit` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的编码后网络发送参数（Encoded Network Transmit Parameters）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transmit` | 网络发送（Network Transmit）响应参数。成功时返回编码后的网络传输参数，可通过 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 解码。 |

**参阅（See Also）**：另见（See also）：`BT_MESH_TRANSMIT`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gac02c170e260980d5b749b581910672d2"></a>

### `bt_mesh_cfg_cli_node_identity_get()`

```c
int bt_mesh_cfg_cli_node_identity_get ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t * status, uint8_t * identity )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取节点身份参数（Node Identity Parameters）。

将 `status` 和 `identity` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 应用密钥（Application Key）所属的网络密钥索引（Network Key Index）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `identity` | 身份（Identity）响应参数，必须为 `BT_MESH_NODE_IDENTITY_STOPPED` 或 `BT_MESH_NODE_IDENTITY_RUNNING`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga12a8618d2b73f30742f8e8d2bdddc138"></a>

### `bt_mesh_cfg_cli_node_identity_set()`

```c
int bt_mesh_cfg_cli_node_identity_set ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t new_identity, uint8_t * status, uint8_t * identity )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置节点身份参数（Node Identity Parameters）。

将 `status` 和 `identity` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `new_identity` | 新的身份状态（Identity State），必须为 `BT_MESH_NODE_IDENTITY_STOPPED` 或 `BT_MESH_NODE_IDENTITY_RUNNING`。 |
| `key_net_idx` | 应用密钥（Application Key）所属的网络密钥索引（Network Key Index）。 |
| `status` | 状态响应参数（status response parameter）。 |
| `identity` | 身份（Identity）响应参数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gac6675d227749a69cedc5455c70626b76"></a>

### `bt_mesh_cfg_cli_node_reset()`

```c
int bt_mesh_cfg_cli_node_reset ( uint16_t net_idx, uint16_t addr, bool * status )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

复位目标节点，并将其从网络中移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga4a50a6a5dcfdc42b7476f0b9e463ea45"></a>

### `bt_mesh_cfg_cli_relay_get()`

```c
int bt_mesh_cfg_cli_relay_get ( uint16_t net_idx, uint16_t addr, uint8_t * status, uint8_t * transmit )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的中继功能状态（Relay Feature State）。

将 `status` 和 `transmit` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_RELAY_DISABLED`、`BT_MESH_RELAY_ENABLED` 或 `BT_MESH_RELAY_NOT_SUPPORTED`。 |
| `transmit` | 发送（Transmit）响应参数。成功时返回编码后的中继传输参数（Relay Transmission Parameters），可通过 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 解码。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga7fe8418130568bdf2a5e56ed2ad027b0"></a>

### `bt_mesh_cfg_cli_relay_set()`

```c
int bt_mesh_cfg_cli_relay_set ( uint16_t net_idx, uint16_t addr, uint8_t new_relay, uint8_t new_transmit, uint8_t * status, uint8_t * transmit )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的中继参数（Relay Parameters）。

将 `status` 和 `transmit` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `new_relay` | 新的中继状态（Relay State），必须为 `BT_MESH_RELAY_DISABLED` 或 `BT_MESH_RELAY_ENABLED`。 |
| `new_transmit` | 新的编码后中继发送参数（Encoded Relay Transmit Parameters）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 状态响应参数（Status Response Parameter）。成功时返回 `BT_MESH_RELAY_DISABLED`、`BT_MESH_RELAY_ENABLED` 或 `BT_MESH_RELAY_NOT_SUPPORTED`。 |
| `transmit` | 发送（Transmit）响应参数。成功时返回编码后的中继传输参数（Relay Transmission Parameters），可通过 `BT_MESH_TRANSMIT_COUNT` 和 `BT_MESH_TRANSMIT_INT` 解码。 |

**参阅（See Also）**：另见（See also）：`BT_MESH_TRANSMIT`。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaf5262c0a27e4b9249ecf908c259cc7d7"></a>

### `bt_mesh_cfg_cli_timeout_get()`

```c
int32_t bt_mesh_cfg_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="ga7e3521ae973dc825422c6dd5f07ef547"></a>

### `bt_mesh_cfg_cli_timeout_set()`

```c
void bt_mesh_cfg_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |

<a id="gaa141d4aabbed6c7780ac7f3955c8b580"></a>

### `bt_mesh_cfg_cli_ttl_get()`

```c
int bt_mesh_cfg_cli_ttl_get ( uint16_t net_idx, uint16_t addr, uint8_t * ttl )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

获取目标节点的生存时间（Time To Live，TTL）值。

将 `ttl` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `ttl` | 生存时间（TTL）响应缓冲区。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2671234d739c802fd080a19d01235352"></a>

### `bt_mesh_cfg_cli_ttl_set()`

```c
int bt_mesh_cfg_cli_ttl_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * ttl )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

设置目标节点的生存时间（Time To Live，TTL）值。

将 `ttl` 设为 `NULL`，即可异步（Asynchronously）使用此方法。此时方法不等待响应，而是在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的生存时间值（Time To Live Value）。 |
| `ttl` | 生存时间（TTL）响应缓冲区。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gac005f52e191c3e5628f063dbc1a19645"></a>

### `bt_mesh_comp_p0_elem_mod()`

```c
uint16_t bt_mesh_comp_p0_elem_mod ( struct bt_mesh_comp_p0_elem * elem, int idx )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取 SIG 模型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 要从中读取模型（Model）的元素（Element）。 |
| `idx` | 要读取的 SIG 模型（SIG Model）的索引。 |

**返回（Returns）**：返回值（Returns）：给定索引处 SIG 模型的模型标识符（Model ID）；索引越界时返回 `0xffff`。

<a id="ga4f656102982961b7bf2e3d3896a2240e"></a>

### `bt_mesh_comp_p0_elem_mod_vnd()`

```c
struct bt_mesh_mod_id_vnd bt_mesh_comp_p0_elem_mod_vnd ( struct bt_mesh_comp_p0_elem * elem, int idx )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取厂商模型（Vendor Model）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 要从中读取模型（Model）的元素（Element）。 |
| `idx` | 要读取的厂商模型（Vendor Model）的索引。 |

**返回（Returns）**：返回值（Returns）：给定索引处厂商模型（Vendor Model）的模型标识符（Model ID）；索引越界时返回 `{0xffff, 0xffff}`。

<a id="gaa6d60ebad6dc4a4f5b022937dbae3120"></a>

### `bt_mesh_comp_p0_elem_pull()`

```c
struct bt_mesh_comp_p0_elem * bt_mesh_comp_p0_elem_pull ( const struct bt_mesh_comp_p0 * comp, struct bt_mesh_comp_p0_elem * elem )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从组成数据第 0 页（Composition Data Page 0）的实例中取出一个第 0 页元素（Element）。

每次调用此函数，都从组成数据页（Composition Data Page）中取出一个新元素（Element），直到所有元素均已取出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `comp` | 组成数据页（Composition data page）。 |
| `elem` | 待填充的元素（Element）。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `elem` 的指针；无法再取出元素（Element）时返回 `NULL`。

<a id="ga1f79d98273a984f1c49b4d5dd5bf8d30"></a>

### `bt_mesh_comp_p0_get()`

```c
int bt_mesh_comp_p0_get ( struct bt_mesh_comp_p0 * comp, struct net_buf_simple * buf )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从缓冲区创建组成数据第 0 页（Composition Data Page 0）的表示。

组成数据页对象（Composition Data Page Object）将取得缓冲区（Buffer）的所有权；调用此函数后，不应再直接操作该缓冲区。

此函数可与 `bt_mesh_cfg_cli_comp_data_get` 结合使用，从其他设备读取组成数据页 0（Composition Data Page 0）：

原始示例（Example）：

```c
NET_BUF_SIMPLE_DEFINE(buf, BT_MESH_RX_SDU_MAX);
struct bt_mesh_comp_p0 comp;

err = bt_mesh_cfg_cli_comp_data_get(net_idx, addr, 0, &page, &buf);
if (!err) {
        bt_mesh_comp_p0_get(&comp, &buf);
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含组成数据（Composition Data）的网络缓冲区（Network Buffer）。 |
| `comp` | 待填充的组成数据结构体（Composition Data Structure）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gae9a19b089d898af914ea5c287aca8fba"></a>

### `bt_mesh_comp_p1_elem_pull()`

```c
struct bt_mesh_comp_p1_elem * bt_mesh_comp_p1_elem_pull ( struct net_buf_simple * buf, struct bt_mesh_comp_p1_elem * elem )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从组成数据第 1 页（Composition Data Page 1）的实例中取出一个第 1 页元素（Element）。

每次调用此函数，都从组成数据页（Composition Data Page）中取出一个新元素（Element），直到所有元素均已取出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 组成数据页 1（Composition Data Page 1）的缓冲区。 |
| `elem` | 待填充的元素（Element）。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `elem` 的指针；无法再取出元素（Element）时返回 `NULL`。

<a id="gac8b4b670c82b80a51834f7ef32206985"></a>

### `bt_mesh_comp_p1_item_pull()`

```c
struct bt_mesh_comp_p1_model_item * bt_mesh_comp_p1_item_pull ( struct bt_mesh_comp_p1_elem * elem, struct bt_mesh_comp_p1_model_item * item )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从组成数据第 1 页元素（Composition Data Page 1 Element）中取出一个第 1 页模型项（Model Item）。

每次调用此函数，都从组成数据页 1 元素（Composition Data Page 1 Element）中取出一个新条目（Item），直到所有条目均已取出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 组成数据页 1 元素（Composition Data Page 1 Element）。 |
| `item` | 待填充的模型条目（Model Item）。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `item` 的指针；无法再取出元素（Element）时返回 `NULL`。

<a id="gac527fe27308c8a61ac1831af9605e429"></a>

### `bt_mesh_comp_p1_pull_ext_item()`

```c
struct bt_mesh_comp_p1_ext_item * bt_mesh_comp_p1_pull_ext_item ( struct bt_mesh_comp_p1_model_item * item, struct bt_mesh_comp_p1_ext_item * ext_item )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

取出模型项（Model Item）中包含的扩展模型项（Extended Model Item）。

每次调用此函数，都从扩展模型条目（Extended Model Item）中取出一个新元素（Element），直到所有元素均已取出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `item` | 要从中取出扩展模型条目（Extended Model Items）的模型条目（Model Item）。 |
| `ext_item` | 待填充的扩展模型条目（Extended Model Item）。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `ext_item` 的指针；无法取出条目（Item）时返回 `NULL`。

<a id="ga0854a494707a40b84beb8582f45e0470"></a>

### `bt_mesh_comp_p2_record_pull()`

```c
struct bt_mesh_comp_p2_record * bt_mesh_comp_p2_record_pull ( struct net_buf_simple * buf, struct bt_mesh_comp_p2_record * record )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从组成数据第 2 页（Composition Data Page 2）的实例中取出一个第 2 页记录（Record）。

每次调用此函数，都从组成数据页（Composition Data Page）中取出一个新元素（Element），直到所有元素均已取出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 组成数据页 2（Composition Data Page 2）的缓冲区。 |
| `record` | 待填充的记录（Record）。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `record` 的指针；无法再取出元素（Element）时返回 `NULL`。

<a id="gaa411ab7db2e71a114a8108eaec9ca12c"></a>

### `bt_mesh_key_idx_unpack_list()`

```c
int bt_mesh_key_idx_unpack_list ( struct net_buf_simple * buf, uint16_t * dst_arr, size_t * dst_cnt )
```

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

从缓冲区解包密钥索引条目列表（Key Index Entries）。

成功时，`dst_cnt` 被设为已解包的密钥索引条目数（Unpacked Key Index Entries）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含已编码应用密钥索引（AppKey Indexes）或网络密钥索引（NetKey Indexes）的消息缓冲区（Message Buffer）。 |
| `dst_arr` | 用于存放已解包列表（Unpacked List）的目标数组（Destination Array）。 |
| `dst_cnt` | 目标数组（Destination Array）的大小。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；`dst_arr` 大小不足以解析完整消息时为 `-EMSGSIZE`。


## 6.5\_原页交叉引用（Cross References）

- [bt_mesh_cfg_cli_cb](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md)
- [bt_mesh_cfg_cli](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md)
- [bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)
- [bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)
- [bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)
- [bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)
- [bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)
- [bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)
- [bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)
- [bt_mesh_comp_p1_item_short](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md)
- [bt_mesh_comp_p1_item_long](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md)
- [bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)
- [bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [zephyr/bluetooth/mesh/cfg_cli.h](../api_file_mesh_acpi_reference/P004_zephyr__bluetooth__mesh__cfg_cli.h_文件参考.md)
- [BT_MESH_MODEL_CNT_CB](../api_biometric_mesh_topic_reference/P002_访问层（Access layer）.md#ga925da443eb15a4c1980d48a69388dc2c)
- [BT_MESH_MODEL_ID_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3f8442dcd1a110ea0d0023f50057139f)
- [配置客户端模型（Configuration Client Model）](P006_配置客户端模型（Configuration Client Model）.md)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [bt_mesh_cfg_cli_mod_pub.period](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a104afe2b8d9766e037293b09c0c1b91c)
- [BT_MESH_BEACON_DISABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga8fa3d0ac3cb9f69464c4068ca61689b9)
- [BT_MESH_BEACON_ENABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga01235217559423b93d7e6cf2236278f0)
- [BT_MESH_FRIEND_DISABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga29fe48989e760438f2c5241110134c8c)
- [BT_MESH_FRIEND_ENABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#gaa23bba212dc1b322651723ca20f497a3)
- [BT_MESH_FRIEND_NOT_SUPPORTED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga35f85e6a9c085cdad4f70b8e60d0b027)
- [BT_MESH_GATT_PROXY_DISABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga3fe3e68efd25a3a03a041b978435fd7b)
- [BT_MESH_GATT_PROXY_ENABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga77f4438624aae49ea2bb66437c9623f7)
- [BT_MESH_GATT_PROXY_NOT_SUPPORTED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#gaecec3747198a29dd10185e3755e660f8)
- [BT_MESH_TRANSMIT_COUNT](../api_biometric_mesh_topic_reference/P002_访问层（Access layer）.md#ga62fda0d731241efbaa4827e4eb9d1795)
- [BT_MESH_TRANSMIT_INT](../api_biometric_mesh_topic_reference/P002_访问层（Access layer）.md#ga2aa21171c5677d23ad0c472291639417)
- [BT_MESH_TRANSMIT](../api_biometric_mesh_topic_reference/P002_访问层（Access layer）.md#gaff82bf652232fbce71c31f38a10577a9)
- [BT_MESH_NODE_IDENTITY_STOPPED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga9a83214cdbd34ac1d4bc644136523bd9)
- [BT_MESH_NODE_IDENTITY_RUNNING](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#ga86e88acc6fdcc26a9cea4415daad016c)
- [BT_MESH_RELAY_DISABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#gaafd10319da7d2f938207b8fd6de02dbc)
- [BT_MESH_RELAY_ENABLED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#gae5d235a7c182a8add961d7ce344f87aa)
- [BT_MESH_RELAY_NOT_SUPPORTED](../api_usb_gnss_topic_reference/P005_运行时配置（Runtime Configuration）.md#gabbbbddd31c2a92256fe2f7a7520e76f7)
- [NET_BUF_SIMPLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf85aa0b705bb4fbe2630191fde802501)
- [BT_MESH_RX_SDU_MAX](../api_biometric_mesh_topic_reference/P002_访问层（Access layer）.md#ga36f299f2fc13892b5a7d871dad1ec9ce)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga3f8442dcd1a110ea0d0023f50057139f"></a>
<a id="agroup__bt__mesh__access_html_ga925da443eb15a4c1980d48a69388dc2c"></a>
<a id="astructbt__mesh__cfg__cli__cb_html"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__bt__mesh__access_html_ga36f299f2fc13892b5a7d871dad1ec9ce"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga1f79d98273a984f1c49b4d5dd5bf8d30"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga36259e9c811a8f1a21d642739cf297df"></a>
<a id="agroup__net__buf_html_gaf85aa0b705bb4fbe2630191fde802501"></a>
<a id="astructbt__mesh__comp__p0_html"></a>

---

[上一章](P005_GATT 客户端 API.md) · [返回大纲](大纲.md) · [下一章](P007_以太网支持函数（Ethernet Support Functions）.md)
