---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-4
title: zephyr__bluetooth__mesh__cfg_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_mesh\_\_cfg\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置客户端模型（Configuration Client Model）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
```

查看此文件的源码。

配置客户端模型（Configuration Client Model）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_ga2f0df6906a27ebbd86dcd11951114001"></a>

```c
#define BT_MESH_MODEL_CFG_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2f0df6906a27ebbd86dcd11951114001)。

通用配置客户端模型（Generic Configuration Client Model）的组成数据条目（Composition Data Entry）。

<a id="r_gab542c707fb5bad0a15088fefda775a42"></a>

```c
#define BT_MESH_PUB_PERIOD_100MS(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_100MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab542c707fb5bad0a15088fefda775a42)。

以 100 ms 为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga29435e527a73ff6e19339b773c8eb79e"></a>

```c
#define BT_MESH_PUB_PERIOD_SEC(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga29435e527a73ff6e19339b773c8eb79e)。

以 1 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga654204077adaa08259d1afbfe92e070e"></a>

```c
#define BT_MESH_PUB_PERIOD_10SEC(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_10SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga654204077adaa08259d1afbfe92e070e)。

以 10 秒为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="r_ga36c37f644ee39ad91b6167f68c806b7e"></a>

```c
#define BT_MESH_PUB_PERIOD_10MIN(steps)
```

相关声明：[BT_MESH_PUB_PERIOD_10MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36c37f644ee39ad91b6167f68c806b7e)。

以 10 分钟为单位编码模型发布周期（Model Publication Period）的辅助宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_gac6675d227749a69cedc5455c70626b76"></a>

```c
int bt_mesh_cfg_cli_node_reset (uint16_t net_idx, uint16_t addr, bool *status)
```

相关声明：[bt_mesh_cfg_cli_node_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac6675d227749a69cedc5455c70626b76)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

复位目标节点，并将其从网络中移除。

<a id="r_ga36259e9c811a8f1a21d642739cf297df"></a>

```c
int bt_mesh_cfg_cli_comp_data_get (uint16_t net_idx, uint16_t addr, uint8_t page, uint8_t *rsp, struct net_buf_simple *comp)
```

相关声明：[bt_mesh_cfg_cli_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36259e9c811a8f1a21d642739cf297df)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取目标节点的组成数据（Composition Data）。

<a id="r_ga2c8a79d1b70e91e0a09c848737bb4a22"></a>

```c
int bt_mesh_cfg_cli_beacon_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2c8a79d1b70e91e0a09c848737bb4a22)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的网络信标状态（Network Beacon State）。

<a id="r_ga660df68049110332ff21610fe4e520c6"></a>

```c
int bt_mesh_cfg_cli_krp_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint8_t *phase)
```

相关声明：[bt_mesh_cfg_cli_krp_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga660df68049110332ff21610fe4e520c6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的网络密钥刷新阶段状态（Network Key Refresh Phase State）。

<a id="r_gae51eee59090cfebed4561ed3bb4df005"></a>

```c
int bt_mesh_cfg_cli_krp_set (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t transition, uint8_t *status, uint8_t *phase)
```

相关声明：[bt_mesh_cfg_cli_krp_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae51eee59090cfebed4561ed3bb4df005)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络密钥刷新阶段参数（Network Key Refresh Phase Parameters）。

<a id="r_gab513c82ebe434907a958cc6da990bd0b"></a>

```c
int bt_mesh_cfg_cli_beacon_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab513c82ebe434907a958cc6da990bd0b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络信标状态（Network Beacon State）。

<a id="r_gaa141d4aabbed6c7780ac7f3955c8b580"></a>

```c
int bt_mesh_cfg_cli_ttl_get (uint16_t net_idx, uint16_t addr, uint8_t *ttl)
```

相关声明：[bt_mesh_cfg_cli_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa141d4aabbed6c7780ac7f3955c8b580)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的生存时间（Time To Live，TTL）值。

<a id="r_ga2671234d739c802fd080a19d01235352"></a>

```c
int bt_mesh_cfg_cli_ttl_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *ttl)
```

相关声明：[bt_mesh_cfg_cli_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2671234d739c802fd080a19d01235352)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的生存时间（Time To Live，TTL）值。

<a id="r_ga4dd1534e9d5b04fc99231ba5dde23e05"></a>

```c
int bt_mesh_cfg_cli_friend_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4dd1534e9d5b04fc99231ba5dde23e05)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的友元功能状态（Friend Feature Status）。

<a id="r_gacf8ad783910449c7cdc304c1b9b3fe0b"></a>

```c
int bt_mesh_cfg_cli_friend_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf8ad783910449c7cdc304c1b9b3fe0b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的友元功能状态（Friend Feature State）。

<a id="r_gaaf945377cf6a3d2b3e7c7cdb5a8df016"></a>

```c
int bt_mesh_cfg_cli_gatt_proxy_get (uint16_t net_idx, uint16_t addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaaf945377cf6a3d2b3e7c7cdb5a8df016)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的代理功能状态（Proxy Feature State）。

<a id="r_ga5a717835a416ba2930f65a975265649f"></a>

```c
int bt_mesh_cfg_cli_gatt_proxy_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5a717835a416ba2930f65a975265649f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的代理功能状态（Proxy Feature State）。

<a id="r_ga92ee7984b14590ed11a470c0dfea0bc9"></a>

```c
int bt_mesh_cfg_cli_net_transmit_get (uint16_t net_idx, uint16_t addr, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga92ee7984b14590ed11a470c0dfea0bc9)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的 `network_transmit` 状态（Network Transmit State）。

<a id="r_ga87f7c1e06b5c721c89031c527960bf40"></a>

```c
int bt_mesh_cfg_cli_net_transmit_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga87f7c1e06b5c721c89031c527960bf40)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的网络发送参数（Network Transmit Parameters）。

<a id="r_ga4a50a6a5dcfdc42b7476f0b9e463ea45"></a>

```c
int bt_mesh_cfg_cli_relay_get (uint16_t net_idx, uint16_t addr, uint8_t *status, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4a50a6a5dcfdc42b7476f0b9e463ea45)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的中继功能状态（Relay Feature State）。

<a id="r_ga7fe8418130568bdf2a5e56ed2ad027b0"></a>

```c
int bt_mesh_cfg_cli_relay_set (uint16_t net_idx, uint16_t addr, uint8_t new_relay, uint8_t new_transmit, uint8_t *status, uint8_t *transmit)
```

相关声明：[bt_mesh_cfg_cli_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fe8418130568bdf2a5e56ed2ad027b0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的中继参数（Relay Parameters）。

<a id="r_ga283fb06ddb6427852ff0ac556d3c1852"></a>

```c
int bt_mesh_cfg_cli_net_key_add (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga283fb06ddb6427852ff0ac556d3c1852)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向目标节点添加网络密钥（Network Key）。

<a id="r_gab42c5bdff36bea35e967946462b12457"></a>

```c
int bt_mesh_cfg_cli_net_key_get (uint16_t net_idx, uint16_t addr, uint16_t *keys, size_t *key_cnt)
```

相关声明：[bt_mesh_cfg_cli_net_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab42c5bdff36bea35e967946462b12457)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点的网络密钥索引列表（Network Key Indexes）。

<a id="r_gab2963ec5536cb4b941578bb490fdc013"></a>

```c
int bt_mesh_cfg_cli_net_key_del (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab2963ec5536cb4b941578bb490fdc013)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从目标节点删除网络密钥（Network Key）。

<a id="r_gafabf4c0fa707eba1fd40cc9a403daa07"></a>

```c
int bt_mesh_cfg_cli_app_key_add (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafabf4c0fa707eba1fd40cc9a403daa07)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向目标节点添加应用密钥（Application Key）。

<a id="r_ga6391ce297ca0be73ccd51044a9e0a76f"></a>

```c
int bt_mesh_cfg_cli_app_key_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint16_t *keys, size_t *key_cnt)
```

相关声明：[bt_mesh_cfg_cli_app_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga6391ce297ca0be73ccd51044a9e0a76f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上与指定网络密钥关联的应用密钥索引列表（Application Key Indexes）。

<a id="r_ga5140472c687584babf885bc08349c865"></a>

```c
int bt_mesh_cfg_cli_app_key_del (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5140472c687584babf885bc08349c865)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从目标节点删除应用密钥（Application Key）。

<a id="r_gaa4a02dd0c1f67621ee71d011fe4a29c1"></a>

```c
int bt_mesh_cfg_cli_mod_app_bind (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa4a02dd0c1f67621ee71d011fe4a29c1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将应用（Application）绑定到目标节点上的 SIG 模型。

<a id="r_gaf82b54a4b2d3176b10daf728272a0977"></a>

```c
int bt_mesh_cfg_cli_mod_app_unbind (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf82b54a4b2d3176b10daf728272a0977)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解除应用（Application）与目标节点上 SIG 模型的绑定。

<a id="r_gada33602562721c9f413eb06b34a823a8"></a>

```c
int bt_mesh_cfg_cli_mod_app_bind_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_bind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gada33602562721c9f413eb06b34a823a8)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将应用（Application）绑定到目标节点上的厂商模型（Vendor Model）。

<a id="r_ga1fb53b9a49be25e633cac9d668c5b209"></a>

```c
int bt_mesh_cfg_cli_mod_app_unbind_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_app_unbind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1fb53b9a49be25e633cac9d668c5b209)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解除应用（Application）与目标节点上厂商模型（Vendor Model）的绑定。

<a id="r_ga67cf5ff993f2444cc66b2ae5353865d2"></a>

```c
int bt_mesh_cfg_cli_mod_app_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status, uint16_t *apps, size_t *app_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_app_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga67cf5ff993f2444cc66b2ae5353865d2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取绑定到目标节点上 SIG 模型的所有应用（Applications）的列表。

<a id="r_gaf7e0f85bbbbfc382bfe4aea8298227d1"></a>

```c
int bt_mesh_cfg_cli_mod_app_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *apps, size_t *app_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_app_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7e0f85bbbbfc382bfe4aea8298227d1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取绑定到目标节点上厂商模型（Vendor Model）的所有应用（Applications）的列表。

<a id="r_ga1b36596a20ca8751006b0f7f2221067d"></a>

```c
int bt_mesh_cfg_cli_mod_pub_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1b36596a20ca8751006b0f7f2221067d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点上 SIG 模型的发布参数（Publish Parameters）。

<a id="r_ga0bc2c24403e0cd79a061ba1244b1a1db"></a>

```c
int bt_mesh_cfg_cli_mod_pub_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0bc2c24403e0cd79a061ba1244b1a1db)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

<a id="r_ga7fc2acda16f3f03a929c38796c67028e"></a>

```c
int bt_mesh_cfg_cli_mod_pub_set (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fc2acda16f3f03a929c38796c67028e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点上 SIG 模型的发布参数（Publish Parameters）。

<a id="r_gad2c602a2685ff38c0e78c1990b244e54"></a>

```c
int bt_mesh_cfg_cli_mod_pub_set_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_pub_set_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gad2c602a2685ff38c0e78c1990b244e54)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点上厂商模型（Vendor Model）的发布参数（Publish Parameters）。

<a id="r_gaf4ee720ce27eea9602b59a380278bb57"></a>

```c
int bt_mesh_cfg_cli_mod_sub_add (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf4ee720ce27eea9602b59a380278bb57)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SIG 模型的订阅列表（Subscription List）添加组地址（Group Address）。

<a id="r_ga3ba34f8be138bc62a7eb7859b18dc441"></a>

```c
int bt_mesh_cfg_cli_mod_sub_add_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga3ba34f8be138bc62a7eb7859b18dc441)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加组地址（Group Address）。

<a id="r_ga8d8595f077267b7d784fde30cbc4b207"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8d8595f077267b7d784fde30cbc4b207)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SIG 模型的订阅列表（Subscription List）删除组地址（Group Address）。

<a id="r_ga74bad73184af2d6ce71134831f70680d"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga74bad73184af2d6ce71134831f70680d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除组地址（Group Address）。

<a id="r_gadac1cc360c30d290a861bbd534fca58d"></a>

```c
int bt_mesh_cfg_cli_mod_sub_overwrite (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gadac1cc360c30d290a861bbd534fca58d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个组地址（Group Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

<a id="r_ga69b2dfacc27ed94b9e1331ff4ac4b582"></a>

```c
int bt_mesh_cfg_cli_mod_sub_overwrite_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t sub_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69b2dfacc27ed94b9e1331ff4ac4b582)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个组地址（Group Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

<a id="r_ga2d22612cf9dc5030699bf7c6c58bf6d5"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_add (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2d22612cf9dc5030699bf7c6c58bf6d5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SIG 模型的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

<a id="r_gaa3a10a54a18a99d0b4b0aa85330b1640"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_add_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa3a10a54a18a99d0b4b0aa85330b1640)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向厂商模型（Vendor Model）的订阅列表（Subscription List）添加虚拟地址（Virtual Address）。

<a id="r_gaf7107373fc0c70d091e9a521d8b641ad"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_del (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7107373fc0c70d091e9a521d8b641ad)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SIG 模型的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

<a id="r_ga8884786e3ec349bcb8b89b60aa11f198"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_del_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8884786e3ec349bcb8b89b60aa11f198)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从厂商模型（Vendor Model）的订阅列表（Subscription List）删除虚拟地址（Virtual Address）。

<a id="r_ga69809ad3f2cff8e1f394f6da6ed63264"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69809ad3f2cff8e1f394f6da6ed63264)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个虚拟地址（Virtual Address）覆盖 SIG 模型订阅列表（Subscription List）中的所有地址。

<a id="r_ga70d3bb7fb914fa3685f4ad9b561a48b6"></a>

```c
int bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, const uint8_t label[16], uint16_t mod_id, uint16_t cid, uint16_t *virt_addr, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga70d3bb7fb914fa3685f4ad9b561a48b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用一个虚拟地址（Virtual Address）覆盖厂商模型（Vendor Model）订阅列表中的所有地址。

<a id="r_gaf739e5e3a4b225e10bf2aedf143d7793"></a>

```c
int bt_mesh_cfg_cli_mod_sub_get (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status, uint16_t *subs, size_t *sub_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf739e5e3a4b225e10bf2aedf143d7793)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上 SIG 模型的订阅列表（Subscription List）。

<a id="r_ga09e751a9071402ae978c0355edfbdf03"></a>

```c
int bt_mesh_cfg_cli_mod_sub_get_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *subs, size_t *sub_cnt)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga09e751a9071402ae978c0355edfbdf03)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取目标节点上厂商模型（Vendor Model）的订阅列表（Subscription List）。

<a id="r_ga1adae658bf8f4512a7d80d0194dcb362"></a>

```c
int bt_mesh_cfg_cli_hb_sub_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_sub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1adae658bf8f4512a7d80d0194dcb362)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

<a id="r_ga86e5de1b216d62b7c77bf43b7af062fc"></a>

```c
int bt_mesh_cfg_cli_hb_sub_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga86e5de1b216d62b7c77bf43b7af062fc)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的心跳订阅参数（Heartbeat Subscription Parameters）。

<a id="r_ga352eb00b78ff978a1a1e81ec5a0575b8"></a>

```c
int bt_mesh_cfg_cli_hb_pub_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_cfg_cli_hb_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga352eb00b78ff978a1a1e81ec5a0575b8)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_ga07c443476adef9c7bb573ffbb8d1b1ce"></a>

```c
int bt_mesh_cfg_cli_hb_pub_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_pub *pub, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga07c443476adef9c7bb573ffbb8d1b1ce)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_gacd647905484fa8319a5377aa5777c254"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_all (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacd647905484fa8319a5377aa5777c254)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除 SIG 模型订阅列表（Subscription List）中的所有组地址（Group Addresses）。

<a id="r_ga2059ccbc689af9c2127e4e399ea5bd43"></a>

```c
int bt_mesh_cfg_cli_mod_sub_del_all_vnd (uint16_t net_idx, uint16_t addr, uint16_t elem_addr, uint16_t mod_id, uint16_t cid, uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_mod_sub_del_all_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2059ccbc689af9c2127e4e399ea5bd43)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除厂商模型（Vendor Model）订阅列表中的所有组地址（Group Addresses）。

<a id="r_gafdaff279685b821a7b205e45feed9a05"></a>

```c
int bt_mesh_cfg_cli_net_key_update (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, const uint8_t net_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_net_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafdaff279685b821a7b205e45feed9a05)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新目标节点上的网络密钥（Network Key）。

<a id="r_gacf1bd7a771a45981a82eeea0dcce01b7"></a>

```c
int bt_mesh_cfg_cli_app_key_update (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint16_t key_app_idx, const uint8_t app_key[16], uint8_t *status)
```

相关声明：[bt_mesh_cfg_cli_app_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf1bd7a771a45981a82eeea0dcce01b7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新目标节点上的应用密钥（Application Key）。

<a id="r_ga12a8618d2b73f30742f8e8d2bdddc138"></a>

```c
int bt_mesh_cfg_cli_node_identity_set (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t new_identity, uint8_t *status, uint8_t *identity)
```

相关声明：[bt_mesh_cfg_cli_node_identity_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga12a8618d2b73f30742f8e8d2bdddc138)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置节点身份参数（Node Identity Parameters）。

<a id="r_gac02c170e260980d5b749b581910672d2"></a>

```c
int bt_mesh_cfg_cli_node_identity_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status, uint8_t *identity)
```

相关声明：[bt_mesh_cfg_cli_node_identity_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac02c170e260980d5b749b581910672d2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取节点身份参数（Node Identity Parameters）。

<a id="r_ga0ee1d0849d632b5d806ee31c87bbc888"></a>

```c
int bt_mesh_cfg_cli_lpn_timeout_get (uint16_t net_idx, uint16_t addr, uint16_t unicast_addr, int32_t *polltimeout)
```

相关声明：[bt_mesh_cfg_cli_lpn_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0ee1d0849d632b5d806ee31c87bbc888)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取低功耗节点轮询超时参数（Low Power Node Polltimeout Parameters）。

<a id="r_gaf5262c0a27e4b9249ecf908c259cc7d7"></a>

```c
int32_t bt_mesh_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf5262c0a27e4b9249ecf908c259cc7d7)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga7e3521ae973dc825422c6dd5f07ef547"></a>

```c
void bt_mesh_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7e3521ae973dc825422c6dd5f07ef547)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

<a id="r_ga1f79d98273a984f1c49b4d5dd5bf8d30"></a>

```c
int bt_mesh_comp_p0_get (struct bt_mesh_comp_p0 *comp, struct net_buf_simple *buf)
```

相关声明：[bt_mesh_comp_p0_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1f79d98273a984f1c49b4d5dd5bf8d30)、[bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区创建组成数据第 0 页（Composition Data Page 0）的表示。

<a id="r_gaa6d60ebad6dc4a4f5b022937dbae3120"></a>

```c
struct bt_mesh_comp_p0_elem * bt_mesh_comp_p0_elem_pull (const struct bt_mesh_comp_p0 *comp, struct bt_mesh_comp_p0_elem *elem)
```

相关声明：[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)、[bt_mesh_comp_p0_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa6d60ebad6dc4a4f5b022937dbae3120)、[bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从组成数据第 0 页（Composition Data Page 0）的实例中取出一个第 0 页元素（Element）。

<a id="r_gac005f52e191c3e5628f063dbc1a19645"></a>

```c
uint16_t bt_mesh_comp_p0_elem_mod (struct bt_mesh_comp_p0_elem *elem, int idx)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_comp_p0_elem_mod](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac005f52e191c3e5628f063dbc1a19645)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取 SIG 模型。

<a id="r_ga4f656102982961b7bf2e3d3896a2240e"></a>

```c
struct bt_mesh_mod_id_vnd bt_mesh_comp_p0_elem_mod_vnd (struct bt_mesh_comp_p0_elem *elem, int idx)
```

相关声明：[bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)、[bt_mesh_comp_p0_elem_mod_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4f656102982961b7bf2e3d3896a2240e)、[bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)。

从给定的组成数据第 0 页元素（Composition Data Page 0 Element）中获取厂商模型（Vendor Model）。

<a id="r_gae9a19b089d898af914ea5c287aca8fba"></a>

```c
struct bt_mesh_comp_p1_elem * bt_mesh_comp_p1_elem_pull (struct net_buf_simple *buf, struct bt_mesh_comp_p1_elem *elem)
```

相关声明：[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)、[bt_mesh_comp_p1_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae9a19b089d898af914ea5c287aca8fba)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)。

从组成数据第 1 页（Composition Data Page 1）的实例中取出一个第 1 页元素（Element）。

<a id="r_gac8b4b670c82b80a51834f7ef32206985"></a>

```c
struct bt_mesh_comp_p1_model_item * bt_mesh_comp_p1_item_pull (struct bt_mesh_comp_p1_elem *elem, struct bt_mesh_comp_p1_model_item *item)
```

相关声明：[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)、[bt_mesh_comp_p1_item_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac8b4b670c82b80a51834f7ef32206985)、[bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)、[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)。

从组成数据第 1 页元素（Composition Data Page 1 Element）中取出一个第 1 页模型项（Model Item）。

<a id="r_gac527fe27308c8a61ac1831af9605e429"></a>

```c
struct bt_mesh_comp_p1_ext_item * bt_mesh_comp_p1_pull_ext_item (struct bt_mesh_comp_p1_model_item *item, struct bt_mesh_comp_p1_ext_item *ext_item)
```

相关声明：[bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)、[bt_mesh_comp_p1_pull_ext_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac527fe27308c8a61ac1831af9605e429)、[bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)、[bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)。

取出模型项（Model Item）中包含的扩展模型项（Extended Model Item）。

<a id="r_ga0854a494707a40b84beb8582f45e0470"></a>

```c
struct bt_mesh_comp_p2_record * bt_mesh_comp_p2_record_pull (struct net_buf_simple *buf, struct bt_mesh_comp_p2_record *record)
```

相关声明：[bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)、[bt_mesh_comp_p2_record_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0854a494707a40b84beb8582f45e0470)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)。

从组成数据第 2 页（Composition Data Page 2）的实例中取出一个第 2 页记录（Record）。

<a id="r_gaa411ab7db2e71a114a8108eaec9ca12c"></a>

```c
int bt_mesh_key_idx_unpack_list (struct net_buf_simple *buf, uint16_t *dst_arr, size_t *dst_cnt)
```

相关声明：[bt_mesh_key_idx_unpack_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa411ab7db2e71a114a8108eaec9ca12c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从缓冲区解包密钥索引条目列表（Key Index Entries）。


## 4.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P088_cfg_cli.h_源码浏览.md)
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
- [BT_MESH_MODEL_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2f0df6906a27ebbd86dcd11951114001)
- [BT_MESH_PUB_PERIOD_100MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab542c707fb5bad0a15088fefda775a42)
- [BT_MESH_PUB_PERIOD_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga29435e527a73ff6e19339b773c8eb79e)
- [BT_MESH_PUB_PERIOD_10SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga654204077adaa08259d1afbfe92e070e)
- [BT_MESH_PUB_PERIOD_10MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36c37f644ee39ad91b6167f68c806b7e)
- [bt_mesh_cfg_cli_node_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac6675d227749a69cedc5455c70626b76)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_cfg_cli_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36259e9c811a8f1a21d642739cf297df)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_cfg_cli_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2c8a79d1b70e91e0a09c848737bb4a22)
- [bt_mesh_cfg_cli_krp_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga660df68049110332ff21610fe4e520c6)
- [bt_mesh_cfg_cli_krp_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae51eee59090cfebed4561ed3bb4df005)
- [bt_mesh_cfg_cli_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab513c82ebe434907a958cc6da990bd0b)
- [bt_mesh_cfg_cli_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa141d4aabbed6c7780ac7f3955c8b580)
- [bt_mesh_cfg_cli_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2671234d739c802fd080a19d01235352)
- [bt_mesh_cfg_cli_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4dd1534e9d5b04fc99231ba5dde23e05)
- [bt_mesh_cfg_cli_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf8ad783910449c7cdc304c1b9b3fe0b)
- [bt_mesh_cfg_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaaf945377cf6a3d2b3e7c7cdb5a8df016)
- [bt_mesh_cfg_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5a717835a416ba2930f65a975265649f)
- [bt_mesh_cfg_cli_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga92ee7984b14590ed11a470c0dfea0bc9)
- [bt_mesh_cfg_cli_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga87f7c1e06b5c721c89031c527960bf40)
- [bt_mesh_cfg_cli_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4a50a6a5dcfdc42b7476f0b9e463ea45)
- [bt_mesh_cfg_cli_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fe8418130568bdf2a5e56ed2ad027b0)
- [bt_mesh_cfg_cli_net_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga283fb06ddb6427852ff0ac556d3c1852)
- [bt_mesh_cfg_cli_net_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab42c5bdff36bea35e967946462b12457)
- [bt_mesh_cfg_cli_net_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab2963ec5536cb4b941578bb490fdc013)
- [bt_mesh_cfg_cli_app_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafabf4c0fa707eba1fd40cc9a403daa07)
- [bt_mesh_cfg_cli_app_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga6391ce297ca0be73ccd51044a9e0a76f)
- [bt_mesh_cfg_cli_app_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5140472c687584babf885bc08349c865)
- [bt_mesh_cfg_cli_mod_app_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa4a02dd0c1f67621ee71d011fe4a29c1)
- [bt_mesh_cfg_cli_mod_app_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf82b54a4b2d3176b10daf728272a0977)
- [bt_mesh_cfg_cli_mod_app_bind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gada33602562721c9f413eb06b34a823a8)
- [bt_mesh_cfg_cli_mod_app_unbind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1fb53b9a49be25e633cac9d668c5b209)
- [bt_mesh_cfg_cli_mod_app_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga67cf5ff993f2444cc66b2ae5353865d2)
- [bt_mesh_cfg_cli_mod_app_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7e0f85bbbbfc382bfe4aea8298227d1)
- [bt_mesh_cfg_cli_mod_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1b36596a20ca8751006b0f7f2221067d)
- [bt_mesh_cfg_cli_mod_pub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0bc2c24403e0cd79a061ba1244b1a1db)
- [bt_mesh_cfg_cli_mod_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fc2acda16f3f03a929c38796c67028e)
- [bt_mesh_cfg_cli_mod_pub_set_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gad2c602a2685ff38c0e78c1990b244e54)
- [bt_mesh_cfg_cli_mod_sub_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf4ee720ce27eea9602b59a380278bb57)
- [bt_mesh_cfg_cli_mod_sub_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga3ba34f8be138bc62a7eb7859b18dc441)
- [bt_mesh_cfg_cli_mod_sub_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8d8595f077267b7d784fde30cbc4b207)
- [bt_mesh_cfg_cli_mod_sub_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga74bad73184af2d6ce71134831f70680d)
- [bt_mesh_cfg_cli_mod_sub_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gadac1cc360c30d290a861bbd534fca58d)
- [bt_mesh_cfg_cli_mod_sub_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69b2dfacc27ed94b9e1331ff4ac4b582)
- [bt_mesh_cfg_cli_mod_sub_va_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2d22612cf9dc5030699bf7c6c58bf6d5)
- [bt_mesh_cfg_cli_mod_sub_va_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa3a10a54a18a99d0b4b0aa85330b1640)
- [bt_mesh_cfg_cli_mod_sub_va_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7107373fc0c70d091e9a521d8b641ad)
- [bt_mesh_cfg_cli_mod_sub_va_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8884786e3ec349bcb8b89b60aa11f198)
- [bt_mesh_cfg_cli_mod_sub_va_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69809ad3f2cff8e1f394f6da6ed63264)
- [bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga70d3bb7fb914fa3685f4ad9b561a48b6)
- [bt_mesh_cfg_cli_mod_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf739e5e3a4b225e10bf2aedf143d7793)
- [bt_mesh_cfg_cli_mod_sub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga09e751a9071402ae978c0355edfbdf03)
- [bt_mesh_cfg_cli_hb_sub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1adae658bf8f4512a7d80d0194dcb362)
- [bt_mesh_cfg_cli_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga86e5de1b216d62b7c77bf43b7af062fc)
- [bt_mesh_cfg_cli_hb_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga352eb00b78ff978a1a1e81ec5a0575b8)
- [bt_mesh_cfg_cli_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga07c443476adef9c7bb573ffbb8d1b1ce)
- [bt_mesh_cfg_cli_mod_sub_del_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacd647905484fa8319a5377aa5777c254)
- [bt_mesh_cfg_cli_mod_sub_del_all_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2059ccbc689af9c2127e4e399ea5bd43)
- [bt_mesh_cfg_cli_net_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafdaff279685b821a7b205e45feed9a05)
- [bt_mesh_cfg_cli_app_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf1bd7a771a45981a82eeea0dcce01b7)
- [bt_mesh_cfg_cli_node_identity_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga12a8618d2b73f30742f8e8d2bdddc138)
- [bt_mesh_cfg_cli_node_identity_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac02c170e260980d5b749b581910672d2)
- [bt_mesh_cfg_cli_lpn_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0ee1d0849d632b5d806ee31c87bbc888)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf5262c0a27e4b9249ecf908c259cc7d7)
- [bt_mesh_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7e3521ae973dc825422c6dd5f07ef547)
- [bt_mesh_comp_p0_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1f79d98273a984f1c49b4d5dd5bf8d30)
- [bt_mesh_comp_p0_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa6d60ebad6dc4a4f5b022937dbae3120)
- [bt_mesh_comp_p0_elem_mod](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac005f52e191c3e5628f063dbc1a19645)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [bt_mesh_comp_p0_elem_mod_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4f656102982961b7bf2e3d3896a2240e)
- [bt_mesh_comp_p1_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae9a19b089d898af914ea5c287aca8fba)
- [bt_mesh_comp_p1_item_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac8b4b670c82b80a51834f7ef32206985)
- [bt_mesh_comp_p1_pull_ext_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac527fe27308c8a61ac1831af9605e429)
- [bt_mesh_comp_p2_record_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0854a494707a40b84beb8582f45e0470)
- [bt_mesh_key_idx_unpack_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa411ab7db2e71a114a8108eaec9ca12c)

<a id="header-details"></a>

---

[上一章](P003_zephyr__bluetooth__audio__audio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__hci_types.h_文件参考.md)
