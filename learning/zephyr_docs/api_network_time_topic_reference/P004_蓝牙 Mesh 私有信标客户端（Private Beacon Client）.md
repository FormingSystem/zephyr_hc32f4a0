---
id: learning.zephyr-docs.api-network-time-topic-reference.page-4
title: 蓝牙 Mesh 私有信标客户端（Private Beacon Client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙 Mesh 私有信标客户端（Private Beacon Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_priv_5Fbeacon_5Fcli_2Eh"></a>

```c
file priv_beacon_cli.h
```

相关声明：[priv_beacon_cli.h](../api_file_system_device_reference/P039_zephyr__bluetooth__mesh__priv_beacon_cli.h_文件参考.md)。

蓝牙Mesh私有信标客户端（Private Beacon Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

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

## 4.3\_宏定义（Macros）

<a id="r_ga65008412f2fc89aa9f71c067ad3fe264"></a>

```c
#define BT_MESH_MODEL_PRIV_BEACON_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_PRIV_BEACON_CLI](#ga65008412f2fc89aa9f71c067ad3fe264)。

私有信标客户端（Private Beacon Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga8a535d31954d8871fed557808b6abc71"></a>

```c
int bt_mesh_priv_beacon_cli_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon *val, struct bt_mesh_priv_beacon *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_set](#ga8a535d31954d8871fed557808b6abc71)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)。

设置目标的私有信标（Private Beacon）状态。

<a id="r_ga76d797a76d8f8fda31feacce840a6f9e"></a>

```c
int bt_mesh_priv_beacon_cli_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon *val)
```

相关声明：[bt_mesh_priv_beacon_cli_get](#ga76d797a76d8f8fda31feacce840a6f9e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)。

获取目标的私有信标状态。

<a id="r_ga389626a517c1bb9cae31501663725483"></a>

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_gatt_proxy_set](#ga389626a517c1bb9cae31501663725483)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标的私有 GATT 代理（Private GATT Proxy）状态。

<a id="r_ga838880ae8391b33d0481fba069ea921b"></a>

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_get (uint16_t net_idx, uint16_t addr, uint8_t *val)
```

相关声明：[bt_mesh_priv_beacon_cli_gatt_proxy_get](#ga838880ae8391b33d0481fba069ea921b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标的私有 GATT 代理状态。

<a id="r_ga2a581e49b8812bd78604fc829bd1d79a"></a>

```c
int bt_mesh_priv_beacon_cli_node_id_set (uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_node_id *val, struct bt_mesh_priv_node_id *rsp)
```

相关声明：[bt_mesh_priv_beacon_cli_node_id_set](#ga2a581e49b8812bd78604fc829bd1d79a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)。

设置目标的私有节点身份（Private Node Identity）状态。

<a id="r_gadd6fc3321cd536771921566bbc650396"></a>

```c
int bt_mesh_priv_beacon_cli_node_id_get (uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, struct bt_mesh_priv_node_id *val)
```

相关声明：[bt_mesh_priv_beacon_cli_node_id_get](#gadd6fc3321cd536771921566bbc650396)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)。

获取目标的私有节点身份状态。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga65008412f2fc89aa9f71c067ad3fe264"></a>

### `BT_MESH_MODEL_PRIV_BEACON_CLI`

```c
#define BT_MESH_MODEL_PRIV_BEACON_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_PRIV_BEACON_CLI,                     \
                 bt_mesh_priv_beacon_cli_op, NULL, cli_data,           \
                 &bt_mesh_priv_beacon_cli_cb)
```

私有信标客户端（Private Beacon Client）模型的组成数据条目（composition data entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli_data` | 指向蓝牙 Mesh 私有信标客户端（Private Beacon Client）实例的指针。 |

<a id="ga838880ae8391b33d0481fba069ea921b"></a>

### `bt_mesh_priv_beacon_cli_gatt_proxy_get()`

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_get ( uint16_t net_idx, uint16_t addr, uint8_t * val )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

获取目标的私有 GATT 代理状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 私有 GATT 代理（Private GATT Proxy）值的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga389626a517c1bb9cae31501663725483"></a>

### `bt_mesh_priv_beacon_cli_gatt_proxy_set()`

```c
int bt_mesh_priv_beacon_cli_gatt_proxy_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * rsp )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

设置目标的私有 GATT 代理（Private GATT Proxy）状态。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的私有 GATT 代理值。 |
| `rsp` | 设置此项后，成功时返回响应状态（response status）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga76d797a76d8f8fda31feacce840a6f9e"></a>

### `bt_mesh_priv_beacon_cli_get()`

```c
int bt_mesh_priv_beacon_cli_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon * val )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

获取目标的私有信标状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 私有信标（Private Beacon）值的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gadd6fc3321cd536771921566bbc650396"></a>

### `bt_mesh_priv_beacon_cli_node_id_get()`

```c
int bt_mesh_priv_beacon_cli_node_id_get ( uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, struct bt_mesh_priv_node_id * val )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

获取目标的私有节点身份状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `key_net_idx` | 要获取其私有节点身份（Private Node Identity）状态的网络索引。 |
| `val` | 私有节点身份值的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga2a581e49b8812bd78604fc829bd1d79a"></a>

### `bt_mesh_priv_beacon_cli_node_id_set()`

```c
int bt_mesh_priv_beacon_cli_node_id_set ( uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_node_id * val, struct bt_mesh_priv_node_id * rsp )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

设置目标的私有节点身份（Private Node Identity）状态。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的私有节点身份值。 |
| `rsp` | 设置此项后，成功时返回响应状态（response status）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga8a535d31954d8871fed557808b6abc71"></a>

### `bt_mesh_priv_beacon_cli_set()`

```c
int bt_mesh_priv_beacon_cli_set ( uint16_t net_idx, uint16_t addr, struct bt_mesh_priv_beacon * val, struct bt_mesh_priv_beacon * rsp )
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

设置目标的私有信标（Private Beacon）状态。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 新的私有信标值。 |
| `rsp` | 设置此项后，成功时返回响应状态（response status）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。


## 4.6\_原页交叉引用（Cross References）

- [priv_beacon_cli.h](../api_file_system_device_reference/P039_zephyr__bluetooth__mesh__priv_beacon_cli.h_文件参考.md)
- [bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)
- [bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)
- [bt_mesh_priv_beacon_cli_cb](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md)
- [bt_mesh_priv_beacon_cli](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_PRIV_BEACON_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gab3b21cbee4e11319a6e0ba3b02b24a91)
- [蓝牙 Mesh 私有信标客户端（Private Beacon Client）](P004_蓝牙 Mesh 私有信标客户端（Private Beacon Client）.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gab3b21cbee4e11319a6e0ba3b02b24a91"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="astructbt__mesh__priv__beacon__cli__cb_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_操作码聚合器客户端模型（Opcodes Aggregator Client model）.md) · [返回大纲](大纲.md) · [下一章](P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md)
