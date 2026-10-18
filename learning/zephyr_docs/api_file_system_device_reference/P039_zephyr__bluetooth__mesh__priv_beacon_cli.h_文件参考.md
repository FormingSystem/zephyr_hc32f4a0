---
id: learning.zephyr-docs.api-file-system-device-reference.page-39
title: zephyr__bluetooth__mesh__priv_beacon_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_bluetooth\_\_mesh\_\_priv\_beacon\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh私有信标客户端（Private Beacon Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh私有信标客户端（Private Beacon Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 39.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fpriv_5Fbeacon"></a>

```c
struct bt_mesh_priv_beacon
```

相关声明：[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)。

私有信标（Private Beacon）。

<a id="r_bt_5Fmesh_5Fpriv_5Fnode_5Fid"></a>

```c
struct bt_mesh_priv_node_id
```

相关声明：[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)。

私有节点标识（Private Node Identity）。

<a id="r_bt_5Fmesh_5Fpriv_5Fbeacon_5Fcli_5Fcb"></a>

```c
struct bt_mesh_priv_beacon_cli_cb
```

相关声明：[bt_mesh_priv_beacon_cli_cb](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md)。

私有信标客户端（Private Beacon Client）状态消息的回调。

<a id="r_bt_5Fmesh_5Fpriv_5Fbeacon_5Fcli"></a>

```c
struct bt_mesh_priv_beacon_cli
```

相关声明：[bt_mesh_priv_beacon_cli](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md)。

Mesh私有信标客户端（Private Beacon Client）模型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 39.2\_宏定义（Macros）

<a id="r_ga65008412f2fc89aa9f71c067ad3fe264"></a>

```c
#define BT_MESH_MODEL_PRIV_BEACON_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_PRIV_BEACON_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga65008412f2fc89aa9f71c067ad3fe264)。

私有信标客户端（Private Beacon Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.3\_函数（Functions）

<a id="r_ga8a535d31954d8871fed557808b6abc71"></a>

```c
int bt_mesh_priv_beacon_cli_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon *val, struct bt_mesh_priv_beacon *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga8a535d31954d8871fed557808b6abc71)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)。

设置目标的私有信标（Private Beacon）状态。

<a id="r_ga76d797a76d8f8fda31feacce840a6f9e"></a>

```c
int bt_mesh_priv_beacon_cli_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon *val)
```

相关声明：[bt_mesh_priv_beacon_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga76d797a76d8f8fda31feacce840a6f9e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)。

获取目标的私有信标状态。

<a id="r_ga389626a517c1bb9cae31501663725483"></a>

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga389626a517c1bb9cae31501663725483)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标的私有 GATT 代理（Private GATT Proxy）状态。

<a id="r_ga838880ae8391b33d0481fba069ea921b"></a>

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_get (uint16_t net_idx, uint16_t addr, uint8_t *val)
```

相关声明：[bt_mesh_priv_beacon_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga838880ae8391b33d0481fba069ea921b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标的私有 GATT 代理状态。

<a id="r_ga2a581e49b8812bd78604fc829bd1d79a"></a>

```c
int bt_mesh_priv_beacon_cli_node_id_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_node_id *val, struct bt_mesh_priv_node_id *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga2a581e49b8812bd78604fc829bd1d79a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)。

设置目标的私有节点身份（Private Node Identity）状态。

<a id="r_gadd6fc3321cd536771921566bbc650396"></a>

```c
int bt_mesh_priv_beacon_cli_node_id_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, struct bt_mesh_priv_node_id *val)
```

相关声明：[bt_mesh_priv_beacon_cli_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#gadd6fc3321cd536771921566bbc650396)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)。

获取目标的私有节点身份状态。


## 39.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P672_priv_beacon_cli.h_源码浏览.md)
- [bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)
- [bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)
- [bt_mesh_priv_beacon_cli_cb](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md)
- [bt_mesh_priv_beacon_cli](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md)
- [BT_MESH_MODEL_PRIV_BEACON_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga65008412f2fc89aa9f71c067ad3fe264)
- [bt_mesh_priv_beacon_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga8a535d31954d8871fed557808b6abc71)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_priv_beacon_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga76d797a76d8f8fda31feacce840a6f9e)
- [bt_mesh_priv_beacon_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga389626a517c1bb9cae31501663725483)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_priv_beacon_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga838880ae8391b33d0481fba069ea921b)
- [bt_mesh_priv_beacon_cli_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga2a581e49b8812bd78604fc829bd1d79a)
- [bt_mesh_priv_beacon_cli_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#gadd6fc3321cd536771921566bbc650396)

<a id="header-details"></a>

---

[上一章](P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__ps.h_文件参考.md)
