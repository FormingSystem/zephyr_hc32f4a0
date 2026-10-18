---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-1
title: zephyr__bluetooth__mesh__blob_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_mesh\_\_blob\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh BLOB传输客户端（Transfer Client）模型API的头文件。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob.h>
```

查看此文件的源码。

蓝牙Mesh BLOB传输客户端（Transfer Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga882e9cec348625c7990de4ee5eb7ed5a"></a>

```c
#define BT_MESH_MODEL_BLOB_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_BLOB_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga882e9cec348625c7990de4ee5eb7ed5a)。

BLOB 传输客户端（BLOB Transfer Client）模型的组成数据（Composition Data）条目。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_gac86db11f09e53adb2e012bf9e446d073"></a>

```c
enum bt_mesh_blob_cli_state { BT_MESH_BLOB_CLI_STATE_NONE , BT_MESH_BLOB_CLI_STATE_CAPS_GET , BT_MESH_BLOB_CLI_STATE_START , BT_MESH_BLOB_CLI_STATE_BLOCK_START , BT_MESH_BLOB_CLI_STATE_BLOCK_SEND , BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK , BT_MESH_BLOB_CLI_STATE_XFER_CHECK , BT_MESH_BLOB_CLI_STATE_CANCEL , BT_MESH_BLOB_CLI_STATE_SUSPENDED , BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET }
```

相关声明：[bt_mesh_blob_cli_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac86db11f09e53adb2e012bf9e446d073)、[BT_MESH_BLOB_CLI_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67)、[BT_MESH_BLOB_CLI_STATE_CAPS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de)、[BT_MESH_BLOB_CLI_STATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2)、[BT_MESH_BLOB_CLI_STATE_BLOCK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2)、[BT_MESH_BLOB_CLI_STATE_BLOCK_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9)、[BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c)、[BT_MESH_BLOB_CLI_STATE_XFER_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96)、[BT_MESH_BLOB_CLI_STATE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646)、[BT_MESH_BLOB_CLI_STATE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9)、[BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)。

BLOB 传输客户端（BLOB Transfer Client）状态。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gac401336775dc6274450d5e27ea1cd720"></a>

```c
int bt_mesh_blob_cli_caps_get (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs)
```

相关声明：[bt_mesh_blob_cli_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac401336775dc6274450d5e27ea1cd720)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)。

获取目标节点（Target Node）列表的传输能力（Transfer Capabilities）。

<a id="r_ga708e4afb3d9e1d6a8fb02d8fd5ab78c2"></a>

```c
int bt_mesh_blob_cli_send (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_io *io)
```

相关声明：[bt_mesh_blob_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)、[bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)。

执行 BLOB 传输（BLOB Transfer）。

<a id="r_ga78487f10fae6c87edaaf4e6ec8f7362c"></a>

```c
int bt_mesh_blob_cli_suspend (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga78487f10fae6c87edaaf4e6ec8f7362c)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

挂起（Suspend）正在进行的传输。

<a id="r_ga5aed01e812215d153fdfafd6375cc453"></a>

```c
int bt_mesh_blob_cli_resume (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga5aed01e812215d153fdfafd6375cc453)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

恢复（Resume）已挂起的传输。

<a id="r_ga222c650657e9a7958b119d4dddd55783"></a>

```c
void bt_mesh_blob_cli_cancel (struct bt_mesh_blob_cli *cli)
```

相关声明：[bt_mesh_blob_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga222c650657e9a7958b119d4dddd55783)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

取消（Cancel）正在进行的传输。

<a id="r_ga17a73cb313dbfc6652b4bcf638b9a30f"></a>

```c
int bt_mesh_blob_cli_xfer_progress_get (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs)
```

相关声明：[bt_mesh_blob_cli_xfer_progress_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga17a73cb313dbfc6652b4bcf638b9a30f)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)。

获取 BLOB 传输（BLOB Transfer）进度。

<a id="r_ga065196837cbf9d2626b5589ce2671441"></a>

```c
uint8_t bt_mesh_blob_cli_xfer_progress_active_get (struct bt_mesh_blob_cli *cli)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_blob_cli_xfer_progress_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga065196837cbf9d2626b5589ce2671441)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

获取当前活动传输的进度，以百分比表示。

<a id="r_ga37bbc559b48ea8cfe7cb3ddf8cad24da"></a>

```c
bool bt_mesh_blob_cli_is_busy (struct bt_mesh_blob_cli *cli)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_blob_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga37bbc559b48ea8cfe7cb3ddf8cad24da)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)。

获取 BLOB 传输客户端（BLOB Transfer Client）的当前状态。

<a id="r_ga047e0cd9817b2ff0a241b2ccfad2acf6"></a>

```c
void bt_mesh_blob_cli_set_chunk_interval_ms (struct bt_mesh_blob_cli *cli, uint32_t interval_ms)
```

相关声明：[bt_mesh_blob_cli_set_chunk_interval_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga047e0cd9817b2ff0a241b2ccfad2acf6)、[bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置块发送间隔（Chunk Sending Interval），单位为毫秒。


## 1.5\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/bluetooth/mesh/access.h](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob.h](../api_source_reference/P068_blob.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P003_blob_cli.h_源码浏览.md)
- [bt_mesh_blob_target_pull](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md)
- [bt_mesh_blob_target](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md)
- [bt_mesh_blob_xfer_info](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_blob_cli_caps](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md)
- [bt_mesh_blob_cli_cb](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md)
- [bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)
- [BT_MESH_MODEL_BLOB_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga882e9cec348625c7990de4ee5eb7ed5a)
- [bt_mesh_blob_cli_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac86db11f09e53adb2e012bf9e446d073)
- [BT_MESH_BLOB_CLI_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67)
- [BT_MESH_BLOB_CLI_STATE_CAPS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de)
- [BT_MESH_BLOB_CLI_STATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c)
- [BT_MESH_BLOB_CLI_STATE_XFER_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96)
- [BT_MESH_BLOB_CLI_STATE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646)
- [BT_MESH_BLOB_CLI_STATE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9)
- [BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)
- [bt_mesh_blob_cli_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac401336775dc6274450d5e27ea1cd720)
- [bt_mesh_blob_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_blob_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga78487f10fae6c87edaaf4e6ec8f7362c)
- [bt_mesh_blob_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga5aed01e812215d153fdfafd6375cc453)
- [bt_mesh_blob_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga222c650657e9a7958b119d4dddd55783)
- [bt_mesh_blob_cli_xfer_progress_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga17a73cb313dbfc6652b4bcf638b9a30f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_blob_cli_xfer_progress_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga065196837cbf9d2626b5589ce2671441)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_blob_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga37bbc559b48ea8cfe7cb3ddf8cad24da)
- [bt_mesh_blob_cli_set_chunk_interval_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga047e0cd9817b2ff0a241b2ccfad2acf6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__clock_control__sf32lb.h_文件参考.md)
