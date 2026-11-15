---
id: learning.zephyr-docs.api-protocol-topic-reference.page-6
title: 蓝牙 Mesh 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_蓝牙 Mesh 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_od_5Fpriv_5Fproxy_5Fcli_2Eh"></a>

```c
file od_priv_proxy_cli.h
```

相关声明：[od_priv_proxy_cli.h](../api_file_service_reference/P033_zephyr__bluetooth__mesh__od_priv_proxy_cli.h_文件参考.md)。

蓝牙Mesh按需私有GATT代理客户端（On-Demand Private GATT Proxy Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fod_5Fpriv_5Fproxy_5Fcli"></a>

```c
struct bt_mesh_od_priv_proxy_cli
```

相关声明：[bt_mesh_od_priv_proxy_cli](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md)。

按需私有代理客户端（On-Demand Private Proxy Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga037391820efab2b953805f6373431ca9"></a>

```c
#define BT_MESH_MODEL_OD_PRIV_PROXY_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_OD_PRIV_PROXY_CLI](#ga037391820efab2b953805f6373431ca9)。

按需私有代理客户端模型（On-Demand Private Proxy Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_ga11357595b2d837f6172a2ec98d1e9973"></a>

```c
int bt_mesh_od_priv_proxy_cli_get (uint16_t net_idx, uint16_t addr, uint8_t *val_rsp)
```

相关声明：[bt_mesh_od_priv_proxy_cli_get](#ga11357595b2d837f6172a2ec98d1e9973)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

<a id="r_ga9b239c221f8c74108e2a7e5276122e1f"></a>

```c
int bt_mesh_od_priv_proxy_cli_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *val_rsp)
```

相关声明：[bt_mesh_od_priv_proxy_cli_set](#ga9b239c221f8c74108e2a7e5276122e1f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

<a id="r_gad613c78e708f0df5aabda9e16fae6a2c"></a>

```c
void bt_mesh_od_priv_proxy_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_od_priv_proxy_cli_timeout_set](#gad613c78e708f0df5aabda9e16fae6a2c)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga037391820efab2b953805f6373431ca9"></a>

### `BT_MESH_MODEL_OD_PRIV_PROXY_CLI`

```c
#define BT_MESH_MODEL_OD_PRIV_PROXY_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI,                     \
                 _bt_mesh_od_priv_proxy_cli_op, NULL, cli_data,            \
                 &_bt_mesh_od_priv_proxy_cli_cb)
```

按需私有代理客户端模型（On-Demand Private Proxy Client Model）的组成数据条目（Composition Data Entry）。

<a id="ga11357595b2d837f6172a2ec98d1e9973"></a>

### `bt_mesh_od_priv_proxy_cli_get()`

```c
int bt_mesh_od_priv_proxy_cli_get ( uint16_t net_idx, uint16_t addr, uint8_t * val_rsp )
```

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
```

获取目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

将 `val_rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

若要处理异步方法的响应参数，请在 `bt_mesh_od_priv_proxy_cli` 结构体中注册 `od_status` 回调（callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val_rsp` | 用于按需私有 GATT 代理（On-Demand Private GATT Proxy）值的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga9b239c221f8c74108e2a7e5276122e1f"></a>

### `bt_mesh_od_priv_proxy_cli_set()`

```c
int bt_mesh_od_priv_proxy_cli_set ( uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t * val_rsp )
```

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
```

设置目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

将 `val_rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

若要处理异步方法的响应参数，请在 `bt_mesh_od_priv_proxy_cli` 结构体中注册 `od_status` 回调（callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `val` | 要设置的按需私有 GATT 代理状态（On-Demand Private GATT Proxy state）。 |
| `val_rsp` | 用于按需私有 GATT 代理（On-Demand Private GATT Proxy）值的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gad613c78e708f0df5aabda9e16fae6a2c"></a>

### `bt_mesh_od_priv_proxy_cli_timeout_set()`

```c
void bt_mesh_od_priv_proxy_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时（transmission timeout），单位为毫秒。 |


## 6.6\_原页交叉引用（Cross References）

- [od_priv_proxy_cli.h](../api_file_service_reference/P033_zephyr__bluetooth__mesh__od_priv_proxy_cli.h_文件参考.md)
- [bt_mesh_od_priv_proxy_cli](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gadd36546fb2cb6d1c731f7ae7674af6a7)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gadd36546fb2cb6d1c731f7ae7674af6a7"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_BD8LB600FS API主题.md) · [返回大纲](大纲.md) · [下一章](P007_远程配网模型（Remote Provisioning models）.md)
