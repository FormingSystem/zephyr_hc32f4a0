---
id: learning.zephyr-docs.api-video-event-topic-reference.page-3
title: 蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_blob_5Fcli_2Eh"></a>

```c
file blob_cli.h
```

相关声明：[blob_cli.h](../api_file_transfer_device_reference/P001_zephyr__bluetooth__mesh__blob_cli.h_文件参考.md)。

蓝牙Mesh BLOB传输客户端（Transfer Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Ftarget_5Fpull"></a>

```c
struct bt_mesh_blob_target_pull
```

相关声明：[bt_mesh_blob_target_pull](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md)。

向目标节点发送分片时使用的目标节点拉取模式（Pull BLOB Transfer Mode）上下文。

<a id="r_bt_5Fmesh_5Fblob_5Ftarget"></a>

```c
struct bt_mesh_blob_target
```

相关声明：[bt_mesh_blob_target](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md)。

BLOB传输客户端（BLOB Transfer Client）的目标节点。

<a id="r_bt_5Fmesh_5Fblob_5Fxfer_5Finfo"></a>

```c
struct bt_mesh_blob_xfer_info
```

相关声明：[bt_mesh_blob_xfer_info](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md)。

二进制大对象传输（BLOB Transfer）的信息。

<a id="r_bt_5Fmesh_5Fblob_5Fcli_5Finputs"></a>

```c
struct bt_mesh_blob_cli_inputs
```

相关声明：[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)。

BLOB传输客户端（BLOB Transfer Client）的传输输入。

<a id="r_bt_5Fmesh_5Fblob_5Fcli_5Fcaps"></a>

```c
struct bt_mesh_blob_cli_caps
```

相关声明：[bt_mesh_blob_cli_caps](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md)。

目标节点（Target Node）的传输能力。

<a id="r_bt_5Fmesh_5Fblob_5Fcli_5Fcb"></a>

```c
struct bt_mesh_blob_cli_cb
```

相关声明：[bt_mesh_blob_cli_cb](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md)。

BLOB传输客户端（BLOB Transfer Client）模型的事件处理回调。

<a id="r_bt_5Fmesh_5Fblob_5Fcli"></a>

```c
struct bt_mesh_blob_cli
```

相关声明：[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

BLOB传输客户端（BLOB Transfer Client）的模型实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.3\_宏定义（Macros）

<a id="r_ga882e9cec348625c7990de4ee5eb7ed5a"></a>

```c
#define BT_MESH_MODEL_BLOB_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_BLOB_CLI](#ga882e9cec348625c7990de4ee5eb7ed5a)。

BLOB 传输客户端（BLOB Transfer Client）模型的组成数据（Composition Data）条目。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_gac86db11f09e53adb2e012bf9e446d073"></a>

```c
enum bt_mesh_blob_cli_state { BT_MESH_BLOB_CLI_STATE_NONE , BT_MESH_BLOB_CLI_STATE_CAPS_GET , BT_MESH_BLOB_CLI_STATE_START , BT_MESH_BLOB_CLI_STATE_BLOCK_START , BT_MESH_BLOB_CLI_STATE_BLOCK_SEND , BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK , BT_MESH_BLOB_CLI_STATE_XFER_CHECK , BT_MESH_BLOB_CLI_STATE_CANCEL , BT_MESH_BLOB_CLI_STATE_SUSPENDED , BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET }
```

相关声明：[bt_mesh_blob_cli_state](#gac86db11f09e53adb2e012bf9e446d073)、[BT_MESH_BLOB_CLI_STATE_NONE](#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67)、[BT_MESH_BLOB_CLI_STATE_CAPS_GET](#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de)、[BT_MESH_BLOB_CLI_STATE_START](#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2)、[BT_MESH_BLOB_CLI_STATE_BLOCK_START](#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2)、[BT_MESH_BLOB_CLI_STATE_BLOCK_SEND](#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9)、[BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK](#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c)、[BT_MESH_BLOB_CLI_STATE_XFER_CHECK](#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96)、[BT_MESH_BLOB_CLI_STATE_CANCEL](#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646)、[BT_MESH_BLOB_CLI_STATE_SUSPENDED](#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9)、[BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET](#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)。

BLOB 传输客户端（BLOB Transfer Client）状态。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_gac401336775dc6274450d5e27ea1cd720"></a>

```c
int bt_mesh_blob_cli_caps_get (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs)
```

相关声明：[bt_mesh_blob_cli_caps_get](#gac401336775dc6274450d5e27ea1cd720)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)。

获取目标节点（Target Node）列表的传输能力（Transfer Capabilities）。

<a id="r_ga708e4afb3d9e1d6a8fb02d8fd5ab78c2"></a>

```c
int bt_mesh_blob_cli_send (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_io *io)
```

相关声明：[bt_mesh_blob_cli_send](#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)、[bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)。

执行 BLOB 传输（BLOB Transfer）。

<a id="r_ga78487f10fae6c87edaaf4e6ec8f7362c"></a>

```c
int bt_mesh_blob_cli_suspend (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_suspend](#ga78487f10fae6c87edaaf4e6ec8f7362c)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

挂起（Suspend）正在进行的传输。

<a id="r_ga5aed01e812215d153fdfafd6375cc453"></a>

```c
int bt_mesh_blob_cli_resume (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_resume](#ga5aed01e812215d153fdfafd6375cc453)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

恢复（Resume）已挂起的传输。

<a id="r_ga222c650657e9a7958b119d4dddd55783"></a>

```c
void bt_mesh_blob_cli_cancel (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_cancel](#ga222c650657e9a7958b119d4dddd55783)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

取消（Cancel）正在进行的传输。

<a id="r_ga17a73cb313dbfc6652b4bcf638b9a30f"></a>

```c
int bt_mesh_blob_cli_xfer_progress_get (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs)
```

相关声明：[bt_mesh_blob_cli_xfer_progress_get](#ga17a73cb313dbfc6652b4bcf638b9a30f)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)。

获取 BLOB 传输（BLOB Transfer）进度。

<a id="r_ga065196837cbf9d2626b5589ce2671441"></a>

```c
uint8_t bt_mesh_blob_cli_xfer_progress_active_get (struct bt_mesh_blob_cli *cli)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_blob_cli_xfer_progress_active_get](#ga065196837cbf9d2626b5589ce2671441)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

获取当前活动传输的进度，以百分比表示。

<a id="r_ga37bbc559b48ea8cfe7cb3ddf8cad24da"></a>

```c
bool bt_mesh_blob_cli_is_busy (struct bt_mesh_blob_cli *cli)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_blob_cli_is_busy](#ga37bbc559b48ea8cfe7cb3ddf8cad24da)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

获取 BLOB 传输客户端（BLOB Transfer Client）的当前状态。

<a id="r_ga047e0cd9817b2ff0a241b2ccfad2acf6"></a>

```c
void bt_mesh_blob_cli_set_chunk_interval_ms (struct bt_mesh_blob_cli *cli, uint32_t interval_ms)
```

相关声明：[bt_mesh_blob_cli_set_chunk_interval_ms](#ga047e0cd9817b2ff0a241b2ccfad2acf6)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置块发送间隔（Chunk Sending Interval），单位为毫秒。

## 3.6\_详细说明（Detailed Documentation）

<a id="ga882e9cec348625c7990de4ee5eb7ed5a"></a>

### `BT_MESH_MODEL_BLOB_CLI`

```c
#define BT_MESH_MODEL_BLOB_CLI ( _cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BLOB_CLI, _bt_mesh_blob_cli_op,      \
                 NULL, _cli, &_bt_mesh_blob_cli_cb)
```

BLOB 传输客户端（BLOB Transfer Client）模型的组成数据（Composition Data）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_cli` | 指向蓝牙 Mesh 二进制大对象传输客户端模型（BLOB Transfer Client Model）API 实例的指针。 |

<a id="gac86db11f09e53adb2e012bf9e446d073"></a>

### `bt_mesh_blob_cli_state`

```c
enum bt_mesh_blob_cli_state
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

BLOB 传输客户端（BLOB Transfer Client）状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BLOB_CLI_STATE_NONE` | 没有活动传输（Active Transfer）。 |
| `BT_MESH_BLOB_CLI_STATE_CAPS_GET` | 正在获取传输能力（Transfer Capabilities）。 |
| `BT_MESH_BLOB_CLI_STATE_START` | 正在发送传输开始消息（Transfer Start）。 |
| `BT_MESH_BLOB_CLI_STATE_BLOCK_START` | 正在发送块开始消息（Block Start）。 |
| `BT_MESH_BLOB_CLI_STATE_BLOCK_SEND` | 正在发送块内分块（Block Chunks）。 |
| `BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK` | 正在检查块状态（Block Status）。 |
| `BT_MESH_BLOB_CLI_STATE_XFER_CHECK` | 正在检查传输状态（Transfer Status）。 |
| `BT_MESH_BLOB_CLI_STATE_CANCEL` | 正在取消传输（Cancelling Transfer）。 |
| `BT_MESH_BLOB_CLI_STATE_SUSPENDED` | 传输已挂起（Transfer is suspended）。 |
| `BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET` | 正在检查传输进度（Transfer Progress）。 |

<a id="ga222c650657e9a7958b119d4dddd55783"></a>

### `bt_mesh_blob_cli_cancel()`

```c
void bt_mesh_blob_cli_cancel ( struct bt_mesh_blob_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

取消（Cancel）正在进行的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

<a id="gac401336775dc6274450d5e27ea1cd720"></a>

### `bt_mesh_blob_cli_caps_get()`

```c
int bt_mesh_blob_cli_caps_get ( struct bt_mesh_blob_cli * cli, const struct bt_mesh_blob_cli_inputs * inputs )
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

获取目标节点（Target Node）列表的传输能力（Transfer Capabilities）。

查询全部目标节点（Target Nodes）的可用性和能力，汇总生成适用于这些目标节点的传输能力集合（Transfer Capabilities），并通过 `bt_mesh_blob_cli_cb::caps` 回调返回。

获取能力可能耗时数秒，取决于目标节点（Target Nodes）数量和 Mesh 网络性能。通过 `bt_mesh_blob_cli_cb::caps` 回调指示流程结束。

此流程不是必需的，但强烈建议在传输前执行，以提高性能及成功概率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `inputs` | 静态分配的 BLOB 传输客户端传输输入（Transfer Inputs）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga37bbc559b48ea8cfe7cb3ddf8cad24da"></a>

### `bt_mesh_blob_cli_is_busy()`

```c
bool bt_mesh_blob_cli_is_busy ( struct bt_mesh_blob_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

获取 BLOB 传输客户端（BLOB Transfer Client）的当前状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

**返回（Returns）**：返回值：BLOB 传输客户端当前正在参与传输或获取能力（Capabilities）时返回 `true`，否则返回 `false`。

<a id="ga5aed01e812215d153fdfafd6375cc453"></a>

### `bt_mesh_blob_cli_resume()`

```c
int bt_mesh_blob_cli_resume ( struct bt_mesh_blob_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

恢复（Resume）已挂起的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga708e4afb3d9e1d6a8fb02d8fd5ab78c2"></a>

### `bt_mesh_blob_cli_send()`

```c
int bt_mesh_blob_cli_send ( struct bt_mesh_blob_cli * cli, const struct bt_mesh_blob_cli_inputs * inputs, const struct bt_mesh_blob_xfer * xfer, const struct bt_mesh_blob_io * io )
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

执行 BLOB 传输（BLOB Transfer）。

开始向目标节点（Target Nodes）发送传输数据。只考虑状态为 `BT_MESH_BLOB_SUCCESS` 的目标节点。

传输会持续进行，直到所有目标节点均被移除，或完整 BLOB 已发送完毕。

BLOB 传输可能耗时数分钟，取决于目标节点数量、BLOB 大小和 Mesh 网络性能。通过 `bt_mesh_blob_cli_cb::end` 回调指示传输结束。

客户端（Client）一次只支持一个传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `inputs` | 静态分配的 BLOB 传输客户端传输输入（Transfer Inputs）。 |
| `xfer` | 静态分配的传输参数（Transfer Parameters）。 |
| `io` | 用于读取待传输数据的 BLOB 数据流（Stream）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga047e0cd9817b2ff0a241b2ccfad2acf6"></a>

### `bt_mesh_blob_cli_set_chunk_interval_ms()`

```c
void bt_mesh_blob_cli_set_chunk_interval_ms ( struct bt_mesh_blob_cli * cli, uint32_t interval_ms )
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

设置块发送间隔（Chunk Sending Interval），单位为毫秒。

此函数是可选的，可用于定义 BLOB 客户端模型发送分块（Chunks）的速度。若不增加延迟，例如蓝牙 Mesh 设备固件升级（DFU）可能因持续发送后续分块而阻塞网络，特别是在将分块发送到组地址或多个单播地址时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `interval_ms` | 每次发送分块（Chunk）之前的延迟，单位为毫秒。 |

**说明（Note）**：注意：间隔过大可能导致超时，可相应增大 `timeout_base` 来避免。

<a id="ga78487f10fae6c87edaaf4e6ec8f7362c"></a>

### `bt_mesh_blob_cli_suspend()`

```c
int bt_mesh_blob_cli_suspend ( struct bt_mesh_blob_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

挂起（Suspend）正在进行的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga065196837cbf9d2626b5589ce2671441"></a>

### `bt_mesh_blob_cli_xfer_progress_active_get()`

```c
uint8_t bt_mesh_blob_cli_xfer_progress_active_get ( struct bt_mesh_blob_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

获取当前活动传输的进度，以百分比表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

**返回（Returns）**：返回值：当前传输进度；没有活动传输时返回 0。

<a id="ga17a73cb313dbfc6652b4bcf638b9a30f"></a>

### `bt_mesh_blob_cli_xfer_progress_get()`

```c
int bt_mesh_blob_cli_xfer_progress_get ( struct bt_mesh_blob_cli * cli, const struct bt_mesh_blob_cli_inputs * inputs )
```

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

获取 BLOB 传输（BLOB Transfer）进度。

仅在 BLOB 传输客户端当前未执行 BLOB 传输时，才能使用此函数。要获取活动传输的进度，请使用 `bt_mesh_blob_cli_xfer_progress_active_get`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `inputs` | 静态分配的 BLOB 传输客户端传输输入（Transfer Inputs）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。


## 3.7\_原页交叉引用（Cross References）

- [blob_cli.h](../api_file_transfer_device_reference/P001_zephyr__bluetooth__mesh__blob_cli.h_文件参考.md)
- [bt_mesh_blob_target_pull](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md)
- [bt_mesh_blob_target](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md)
- [bt_mesh_blob_xfer_info](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_blob_cli_caps](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md)
- [bt_mesh_blob_cli_cb](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md)
- [bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_BLOB_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga17e2e59a1344e623fe9fec6e27b7f22e)
- [蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API](P003_蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API.md)
- [bt_mesh_blob_cli_cb::caps](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a58e749cadeb464299495ee74456c592c)
- [BT_MESH_BLOB_SUCCESS](../api_audio_path_topic_reference/P005_蓝牙 Mesh BLOB 模型 API.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)
- [bt_mesh_blob_cli_cb::end](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a60bc49eab376b055a8c21099f86fdde7)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga17e2e59a1344e623fe9fec6e27b7f22e"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9"></a>
<a id="ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_BAP 单播服务器 API（Unicast Server APIs）.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md)
