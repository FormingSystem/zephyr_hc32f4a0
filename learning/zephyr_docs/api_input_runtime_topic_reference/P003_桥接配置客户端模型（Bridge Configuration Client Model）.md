---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-3
title: 桥接配置客户端模型（Bridge Configuration Client Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_桥接配置客户端模型（Bridge Configuration Client Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh 桥接配置客户端模型的 API。

<a id="details"></a>

蓝牙 Mesh 桥接配置客户端模型的 API。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_brg_5Fcfg_5Fcli_2Eh"></a>

```c
file brg_cfg_cli.h
```

相关声明：[brg_cfg_cli.h](../api_file_service_interface_reference/P009_zephyr__bluetooth__mesh__brg_cfg_cli.h_文件参考.md)。

蓝牙Mesh桥接配置客户端（Bridge Configuration Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Fcli_5Fcb"></a>

```c
struct bt_mesh_brg_cfg_cli_cb
```

相关声明：[bt_mesh_brg_cfg_cli_cb](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md)。

Mesh桥接配置客户端（Bridge Configuration Client）状态消息的回调。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Fcli"></a>

```c
struct bt_mesh_brg_cfg_cli
```

相关声明：[bt_mesh_brg_cfg_cli](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md)。

桥接配置客户端（Bridge Configuration Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.3\_宏定义（Macros）

<a id="r_ga4cf994be4732bd99b2c8a4642f670efe"></a>

```c
#define BT_MESH_MODEL_BRG_CFG_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_BRG_CFG_CLI](#ga4cf994be4732bd99b2c8a4642f670efe)。

桥接配置客户端模型（Bridge Configuration Client Model）的组合数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_ga6a4507190e425013a9d21ea0a1be1b5c"></a>

```c
int bt_mesh_brg_cfg_cli_get (uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state *status)
```

相关声明：[bt_mesh_brg_cfg_cli_get](#ga6a4507190e425013a9d21ea0a1be1b5c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)。

向指定目标地址发送子网桥接获取（Subnet Bridge Get）消息。

<a id="r_ga6643d4d043af4b0cb30470a5c9a46f38"></a>

```c
int bt_mesh_brg_cfg_cli_set (uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state val, enum bt_mesh_brg_cfg_state *status)
```

相关声明：[bt_mesh_brg_cfg_cli_set](#ga6643d4d043af4b0cb30470a5c9a46f38)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)。

使用指定参数向指定目标地址发送子网桥接设置（Subnet Bridge Set）消息。

<a id="r_ga99951987bd6787e3e1348d8e51e64fe5"></a>

```c
int bt_mesh_brg_cfg_cli_table_size_get (uint16_t net_idx, uint16_t addr, uint16_t *size)
```

相关声明：[bt_mesh_brg_cfg_cli_table_size_get](#ga99951987bd6787e3e1348d8e51e64fe5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用指定参数向指定目标地址发送桥接表大小获取（Bridging Table Size Get）消息。

<a id="r_ga8f055e8ee384e8ea4887a56720959b26"></a>

```c
int bt_mesh_brg_cfg_cli_table_add (uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_table_entry *entry, struct bt_mesh_brg_cfg_table_status *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_add](#ga8f055e8ee384e8ea4887a56720959b26)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)、[bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)。

使用指定参数向指定目标地址发送桥接表添加（Bridging Table Add）消息。

<a id="r_gabdb919dcf177b8d5c8a28b057469bf18"></a>

```c
int bt_mesh_brg_cfg_cli_table_remove (uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t addr1, uint16_t addr2, struct bt_mesh_brg_cfg_table_status *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_remove](#gabdb919dcf177b8d5c8a28b057469bf18)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)。

使用指定参数向指定目标地址发送桥接表移除（Bridging Table Remove）消息。

<a id="r_ga04bb227d14d4f478e4f32a8ca87d2c38"></a>

```c
int bt_mesh_brg_cfg_cli_subnets_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_filter_netkey filter_net_idx, uint8_t start_idx, struct bt_mesh_brg_cfg_subnets_list *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_subnets_get](#ga04bb227d14d4f478e4f32a8ca87d2c38)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)。

使用指定参数向指定目标地址发送已桥接子网获取（Bridged Subnets Get）消息。

<a id="r_gacd3811be7b87d2d9187aed6c50945b85"></a>

```c
int bt_mesh_brg_cfg_cli_table_get (uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t start_idx, struct bt_mesh_brg_cfg_table_list *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_get](#gacd3811be7b87d2d9187aed6c50945b85)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)。

使用指定参数向指定目标地址发送桥接表获取（Bridging Table Get）消息。

<a id="r_ga252994dd3119387703af45c0932ef253"></a>

```c
int32_t bt_mesh_brg_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_brg_cfg_cli_timeout_get](#ga252994dd3119387703af45c0932ef253)。

获取当前传输超时值（transmission timeout）。

<a id="r_gad30102a29983545ec79f178b1390ce74"></a>

```c
void bt_mesh_brg_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_brg_cfg_cli_timeout_set](#gad30102a29983545ec79f178b1390ce74)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 3.5\_详细说明（Detailed Documentation）

<a id="ga4cf994be4732bd99b2c8a4642f670efe"></a>

### `BT_MESH_MODEL_BRG_CFG_CLI`

```c
#define BT_MESH_MODEL_BRG_CFG_CLI ( _cli)
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BRG_CFG_CLI, _bt_mesh_brg_cfg_cli_op, NULL, _cli,        \
                 &_bt_mesh_brg_cfg_cli_cb)
```

桥接配置客户端模型（Bridge Configuration Client Model）的组合数据（Composition Data）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_cli` | 指向网桥配置客户端模型（Bridge Configuration Client Model）实例的指针。 |

<a id="ga6a4507190e425013a9d21ea0a1be1b5c"></a>

### `bt_mesh_brg_cfg_cli_get()`

```c
int bt_mesh_brg_cfg_cli_get ( uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state * status )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

向指定目标地址发送子网桥接获取（Subnet Bridge Get）消息。

本函数向给定目的地址发送子网桥接获取（Subnet Bridge Get）消息，查询子网的子网桥接状态（Subnet Bridge State）。该状态表示子网桥接功能是否启用。预期目的节点返回子网桥接状态（Subnet Bridge Status）消息。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `status` | 状态响应参数（Status Response Parameter），成功时返回 `BT_MESH_BRG_CFG_DISABLED` 或 `BT_MESH_BRG_CFG_ENABLED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga6643d4d043af4b0cb30470a5c9a46f38"></a>

### `bt_mesh_brg_cfg_cli_set()`

```c
int bt_mesh_brg_cfg_cli_set ( uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state val, enum bt_mesh_brg_cfg_state * status )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送子网桥接设置（Subnet Bridge Set）消息。

本函数使用给定参数向目的地址发送子网桥接设置（Subnet Bridge Set）消息，设置子网的子网桥接状态（Subnet Bridge State）。该状态表示子网桥接功能是否启用。预期目的节点返回子网桥接状态（Subnet Bridge Status）消息。

将 `status` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 要设置的子网桥接状态（Subnet Bridge State），必须为 `BT_MESH_BRG_CFG_DISABLED` 或 `BT_MESH_BRG_CFG_ENABLED`。 |
| `status` | 状态响应参数（Status Response Parameter），成功时返回 `BT_MESH_BRG_CFG_DISABLED` 或 `BT_MESH_BRG_CFG_ENABLED`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga04bb227d14d4f478e4f32a8ca87d2c38"></a>

### `bt_mesh_brg_cfg_cli_subnets_get()`

```c
int bt_mesh_brg_cfg_cli_subnets_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_filter_netkey filter_net_idx, uint8_t start_idx, struct bt_mesh_brg_cfg_subnets_list * rsp )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送已桥接子网获取（Bridged Subnets Get）消息。

本函数使用给定参数向目的地址发送已桥接子网获取（Bridged Subnets Get）消息，获取该节点所桥接的子网列表。预期目的节点返回已桥接子网列表（Bridged Subnets List）消息。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

设置了 `rsp` 时，用户负责在 `bt_mesh_brg_cfg_subnets_list::list` 中提供缓冲区，用于存放经过筛选的 N 对网络密钥索引（NetKey Indexes）。若未提供缓冲区，不复制已桥接子网。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `filter_net_idx` | 用于筛选的过滤器（Filter）及网络密钥索引（NetKey Index）。 |
| `start_idx` | 读取的起始偏移量（Start Offset），以桥接表状态条目（Bridging Table State Entries）为单位。 |
| `rsp` | 指向保存服务器响应的结构体的指针；设为 `NULL` 则不等待响应。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga8f055e8ee384e8ea4887a56720959b26"></a>

### `bt_mesh_brg_cfg_cli_table_add()`

```c
int bt_mesh_brg_cfg_cli_table_add ( uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_table_entry * entry, struct bt_mesh_brg_cfg_table_status * rsp )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送桥接表添加（Bridging Table Add）消息。

本函数使用给定参数向目的地址发送桥接表添加（Bridging Table Add）消息，向桥接表加入条目。桥接表（Bridging Table）包含允许由该节点桥接的网络密钥和地址。预期目的节点返回桥接表状态（Bridging Table Status）消息。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `entry` | 指向要添加的桥接表条目（Bridging Table Entry）的指针。 |
| `rsp` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gacd3811be7b87d2d9187aed6c50945b85"></a>

### `bt_mesh_brg_cfg_cli_table_get()`

```c
int bt_mesh_brg_cfg_cli_table_get ( uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t start_idx, struct bt_mesh_brg_cfg_table_list * rsp )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送桥接表获取（Bridging Table Get）消息。

本函数使用给定参数向目的地址发送桥接表获取（Bridging Table Get）消息，获取桥接表内容。桥接表（Bridging Table）包含允许由该节点桥接的地址。预期目的节点返回桥接表列表（Bridging Table List）消息。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

设置了 `rsp` 时，用户负责在 `bt_mesh_brg_cfg_table_list::list` 中提供缓冲区，用于存放经过筛选的 N 对网络密钥索引（NetKey Indexes）。若未提供缓冲区，不复制已桥接地址；若缓冲区比收到的列表短，只复制能容纳的条目，其余丢弃。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `net_idx1` | 第一个子网的网络密钥索引（NetKey Index）。 |
| `net_idx2` | 第二个子网的网络密钥索引（NetKey Index）。 |
| `start_idx` | 读取的起始偏移量（Start Offset），以桥接表状态条目（Bridging Table State Entries）为单位。 |
| `rsp` | 指向保存服务器响应的结构体的指针；设为 `NULL` 则不等待响应。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gabdb919dcf177b8d5c8a28b057469bf18"></a>

### `bt_mesh_brg_cfg_cli_table_remove()`

```c
int bt_mesh_brg_cfg_cli_table_remove ( uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t addr1, uint16_t addr2, struct bt_mesh_brg_cfg_table_status * rsp )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送桥接表移除（Bridging Table Remove）消息。

本函数使用给定参数向目的地址发送桥接表移除（Bridging Table Remove）消息，从桥接表移除条目。桥接表（Bridging Table）包含允许由该节点桥接的网络密钥和地址。预期目的节点返回桥接表状态（Bridging Table Status）消息。

将 `rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `net_idx1` | 第一个子网的网络密钥索引（NetKey Index）。 |
| `net_idx2` | 第二个子网的网络密钥索引（NetKey Index）。 |
| `addr1` | 第一个子网中的节点地址（Node address）。 |
| `addr2` | 第二个子网中的节点地址（Node address）。 |
| `rsp` | 指向保存服务器响应的结构体的指针；设为 `NULL` 则不等待响应。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga99951987bd6787e3e1348d8e51e64fe5"></a>

### `bt_mesh_brg_cfg_cli_table_size_get()`

```c
int bt_mesh_brg_cfg_cli_table_size_get ( uint16_t net_idx, uint16_t addr, uint16_t * size )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

使用指定参数向指定目标地址发送桥接表大小获取（Bridging Table Size Get）消息。

本函数使用给定参数向目的地址发送桥接表大小获取（Bridging Table Size Get）消息，获取节点的桥接表大小，即最多可存储的条目数。预期目的节点返回桥接表大小状态（Bridging Table Size Status）消息。

将 `size` 设为 `NULL` 可异步（Asynchronously）使用此方法；它不等待响应，发送命令后立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密消息的网络索引（Network Index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `size` | 桥接表大小响应参数（Bridging Table Size Response Parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga252994dd3119387703af45c0932ef253"></a>

### `bt_mesh_brg_cfg_cli_timeout_get()`

```c
int32_t bt_mesh_brg_cfg_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="gad30102a29983545ec79f178b1390ce74"></a>

### `bt_mesh_brg_cfg_cli_timeout_set()`

```c
void bt_mesh_brg_cfg_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |


## 3.6\_原页交叉引用（Cross References）

- [brg_cfg_cli.h](../api_file_service_interface_reference/P009_zephyr__bluetooth__mesh__brg_cfg_cli.h_文件参考.md)
- [bt_mesh_brg_cfg_cli_cb](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md)
- [bt_mesh_brg_cfg_cli](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_BRG_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga9c776b4befd21c15f4867d906f631257)
- [桥接配置客户端模型（Bridge Configuration Client Model）](P003_桥接配置客户端模型（Bridge Configuration Client Model）.md)
- [BT_MESH_BRG_CFG_DISABLED](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)
- [BT_MESH_BRG_CFG_ENABLED](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)
- [bt_mesh_brg_cfg_subnets_list::list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md#a00ebe6255aabcd1cab49f08e4dc7e21b)
- [bt_mesh_brg_cfg_table_list::list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md#a44ce11d9a2cbda69b605fab6ed68cc56)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga9c776b4befd21c15f4867d906f631257"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_当前时间服务（Current Time Service，CTS）.md) · [返回大纲](大纲.md) · [下一章](P004_连接管理器连接性实现 API（Connectivity Implementation API）.md)
