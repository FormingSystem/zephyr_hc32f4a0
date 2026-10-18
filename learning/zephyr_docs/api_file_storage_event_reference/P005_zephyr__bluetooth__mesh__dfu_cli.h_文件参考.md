---
id: learning.zephyr-docs.api-file-storage-event-reference.page-5
title: zephyr__bluetooth__mesh__dfu_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_mesh\_\_dfu\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob_cli.h>
#include <zephyr/bluetooth/mesh/dfu.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfu_5Ftarget"></a>

```c
struct bt_mesh_dfu_target
```

相关声明：[bt_mesh_dfu_target](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md)。

设备固件更新（DFU）的目标节点。

<a id="r_bt_5Fmesh_5Fdfu_5Fmetadata_5Fstatus"></a>

```c
struct bt_mesh_dfu_metadata_status
```

相关声明：[bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)。

元数据状态（Metadata Status）的响应。

<a id="r_bt_5Fmesh_5Fdfu_5Ftarget_5Fstatus"></a>

```c
struct bt_mesh_dfu_target_status
```

相关声明：[bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)。

设备固件更新（DFU）目标节点的状态参数。

<a id="r_bt_5Fmesh_5Fdfu_5Fcli_5Fcb"></a>

```c
struct bt_mesh_dfu_cli_cb
```

相关声明：[bt_mesh_dfu_cli_cb](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md)。

固件更新客户端（Firmware Update Client）的事件回调。

<a id="r_bt_5Fmesh_5Fdfu_5Fcli"></a>

```c
struct bt_mesh_dfu_cli
```

相关声明：[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

固件更新客户端（Firmware Update Client）的模型实例。

<a id="r_bt_5Fmesh_5Fdfu_5Fcli_5Fxfer_5Fblob_5Fparams"></a>

```c
struct bt_mesh_dfu_cli_xfer_blob_params
```

相关声明：[bt_mesh_dfu_cli_xfer_blob_params](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)。

固件更新客户端（Firmware Update Client）传输所用的BLOB参数：

<a id="r_bt_5Fmesh_5Fdfu_5Fcli_5Fxfer"></a>

```c
struct bt_mesh_dfu_cli_xfer
```

相关声明：[bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)。

固件更新客户端（Firmware Update Client）的传输参数：

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga0b10a95f9b7c806bfd8649280f535c96"></a>

```c
#define BT_MESH_DFU_CLI_INIT(_handlers)
```

相关声明：[BT_MESH_DFU_CLI_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0b10a95f9b7c806bfd8649280f535c96)。

固件更新客户端（Firmware Update Client）模型的初始化参数（Initialization Parameters）。

<a id="r_gadee3710bb46d907a51232ca42cca7c2d"></a>

```c
#define BT_MESH_MODEL_DFU_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_DFU_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gadee3710bb46d907a51232ca42cca7c2d)。

固件更新客户端（Firmware Update Client）模型的组成数据（Composition Data）条目。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_ga2967b89e8fc3b848b70e493f6e821761"></a>

```c
typedef enum bt_mesh_dfu_iter(* bt_mesh_dfu_img_cb_t) (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t idx, uint8_t total, const struct bt_mesh_dfu_img *img, void *cb_data)
```

相关声明：[bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)、[bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)。

设备固件更新（DFU）镜像回调（Image Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga20764694315adb4f846dcff20f377417"></a>

```c
int bt_mesh_dfu_cli_send (struct bt_mesh_dfu_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs, const struct bt_mesh_blob_io *io, const struct bt_mesh_dfu_cli_xfer *xfer)
```

相关声明：[bt_mesh_dfu_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20764694315adb4f846dcff20f377417)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)。

开始分发设备固件更新（DFU）。

<a id="r_gaa1ed22da058839c9f3234ce2e41eda32"></a>

```c
int bt_mesh_dfu_cli_suspend (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaa1ed22da058839c9f3234ce2e41eda32)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

挂起（Suspend）DFU 传输。

<a id="r_ga0011fb5c03e6e8c2babfb677d528033b"></a>

```c
int bt_mesh_dfu_cli_resume (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0011fb5c03e6e8c2babfb677d528033b)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

恢复（Resume）已挂起的传输。

<a id="r_ga4c7353f45a6e33884844fd9d2f443750"></a>

```c
int bt_mesh_dfu_cli_cancel (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx)
```

相关声明：[bt_mesh_dfu_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c7353f45a6e33884844fd9d2f443750)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)。

取消（Cancel）DFU 传输。

<a id="r_ga2904ba992a00ee9fba6704c1efc8f074"></a>

```c
int bt_mesh_dfu_cli_apply (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2904ba992a00ee9fba6704c1efc8f074)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

应用（Apply）已完成传输的 DFU。

<a id="r_gaf76f0cdb5c6b0df12ddb495c718c3c93"></a>

```c
int bt_mesh_dfu_cli_confirm (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaf76f0cdb5c6b0df12ddb495c718c3c93)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

确认活动传输已在目标节点（Target Nodes）上应用。

<a id="r_ga073c5bc227040f1f33e7b3f2fe69a309"></a>

```c
uint8_t bt_mesh_dfu_cli_progress (struct bt_mesh_dfu_cli *cli)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_cli_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga073c5bc227040f1f33e7b3f2fe69a309)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

以完成百分比（Percentage of Completion）获取进度。

<a id="r_gad6308700322d96676635bcf0b70c74f7"></a>

```c
bool bt_mesh_dfu_cli_is_busy (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_dfu_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gad6308700322d96676635bcf0b70c74f7)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

检查是否正在进行 DFU 传输（Transfer）。

<a id="r_ga4c33f9457d4f367760a51a771dfd2671"></a>

```c
int bt_mesh_dfu_cli_imgs_get (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, bt_mesh_dfu_img_cb_t cb, void *cb_data, uint8_t max_count)
```

相关声明：[bt_mesh_dfu_cli_imgs_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c33f9457d4f367760a51a771dfd2671)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 DFU 镜像列表请求（Image List Request）。

<a id="r_ga20b3e7d3d3640149a20d698a6aa7dca5"></a>

```c
int bt_mesh_dfu_cli_metadata_check (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t img_idx, const struct bt_mesh_dfu_slot *slot, struct bt_mesh_dfu_metadata_status *rsp)
```

相关声明：[bt_mesh_dfu_cli_metadata_check](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20b3e7d3d3640149a20d698a6aa7dca5)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)、[bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)。

对给定 DFU 镜像槽（Image Slot）执行元数据检查（Metadata Check）。

<a id="r_gab754da11705a2d6a24ec828aa7862579"></a>

```c
int bt_mesh_dfu_cli_status_get (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, struct bt_mesh_dfu_target_status *rsp)
```

相关声明：[bt_mesh_dfu_cli_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gab754da11705a2d6a24ec828aa7862579)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)。

获取目标节点状态（Target Node Status）。

<a id="r_ga3dd10bd1e8673973fd6db98d3ebda354"></a>

```c
int32_t bt_mesh_dfu_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_dfu_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga3dd10bd1e8673973fd6db98d3ebda354)。

获取当前流程超时值（Procedure Timeout Value）。

<a id="r_ga603adf5b40b6e382c9035c9f2bad99a9"></a>

```c
void bt_mesh_dfu_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_dfu_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga603adf5b40b6e382c9035c9f2bad99a9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置流程超时值（Procedure Timeout Value）。


## 5.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_cli.h](../api_source_architecture_reference/P003_blob_cli.h_源码浏览.md)
- [zephyr/bluetooth/mesh/dfu.h](../api_source_reference/P126_dfu.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P039_dfu_cli.h_源码浏览.md)
- [bt_mesh_dfu_target](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md)
- [bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)
- [bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)
- [bt_mesh_dfu_cli_cb](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md)
- [bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)
- [bt_mesh_dfu_cli_xfer_blob_params](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)
- [bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)
- [BT_MESH_DFU_CLI_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0b10a95f9b7c806bfd8649280f535c96)
- [固件更新客户端模型（原文：Firmware Uppdate Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html)
- [BT_MESH_MODEL_DFU_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gadee3710bb46d907a51232ca42cca7c2d)
- [bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)
- [bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [bt_mesh_dfu_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20764694315adb4f846dcff20f377417)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_dfu_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaa1ed22da058839c9f3234ce2e41eda32)
- [bt_mesh_dfu_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0011fb5c03e6e8c2babfb677d528033b)
- [bt_mesh_dfu_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c7353f45a6e33884844fd9d2f443750)
- [bt_mesh_dfu_cli_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2904ba992a00ee9fba6704c1efc8f074)
- [bt_mesh_dfu_cli_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaf76f0cdb5c6b0df12ddb495c718c3c93)
- [bt_mesh_dfu_cli_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga073c5bc227040f1f33e7b3f2fe69a309)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_dfu_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gad6308700322d96676635bcf0b70c74f7)
- [bt_mesh_dfu_cli_imgs_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c33f9457d4f367760a51a771dfd2671)
- [bt_mesh_dfu_cli_metadata_check](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20b3e7d3d3640149a20d698a6aa7dca5)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [bt_mesh_dfu_cli_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gab754da11705a2d6a24ec828aa7862579)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_dfu_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga3dd10bd1e8673973fd6db98d3ebda354)
- [bt_mesh_dfu_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga603adf5b40b6e382c9035c9f2bad99a9)

---

[上一章](P004_zephyr__bluetooth__services__cts.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__net__dns_sd.h_文件参考.md)
