---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-6
title: 固件更新客户端模型（原文：Firmware Uppdate Client model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_固件更新客户端模型（原文：Firmware Uppdate Client model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh 固件更新客户端模型的 API。

<a id="details"></a>

蓝牙 Mesh 固件更新客户端模型的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

## 6.2\_宏定义（Macros）

<a id="r_ga0b10a95f9b7c806bfd8649280f535c96"></a>

```c
#define BT_MESH_DFU_CLI_INIT(_handlers)
```

相关声明：[BT_MESH_DFU_CLI_INIT](#ga0b10a95f9b7c806bfd8649280f535c96)。

固件更新客户端（Firmware Update Client）模型的初始化参数（Initialization Parameters）。

<a id="r_gadee3710bb46d907a51232ca42cca7c2d"></a>

```c
#define BT_MESH_MODEL_DFU_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_DFU_CLI](#gadee3710bb46d907a51232ca42cca7c2d)。

固件更新客户端（Firmware Update Client）模型的组成数据（Composition Data）条目。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga2967b89e8fc3b848b70e493f6e821761"></a>

```c
typedef enum bt_mesh_dfu_iter(* bt_mesh_dfu_img_cb_t) (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t idx, uint8_t total, const struct bt_mesh_dfu_img *img, void *cb_data)
```

相关声明：[bt_mesh_dfu_iter](../api_video_event_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md#ga82475cb72f2ea8b60e70d6987eca2ff6)、[bt_mesh_dfu_img_cb_t](#ga2967b89e8fc3b848b70e493f6e821761)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)。

设备固件更新（DFU）镜像回调（Image Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_ga20764694315adb4f846dcff20f377417"></a>

```c
int bt_mesh_dfu_cli_send (struct bt_mesh_dfu_cli *cli, const struct bt_mesh_blob_cli_inputs *inputs, const struct bt_mesh_blob_io *io, const struct bt_mesh_dfu_cli_xfer *xfer)
```

相关声明：[bt_mesh_dfu_cli_send](#ga20764694315adb4f846dcff20f377417)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)。

开始分发设备固件更新（DFU）。

<a id="r_gaa1ed22da058839c9f3234ce2e41eda32"></a>

```c
int bt_mesh_dfu_cli_suspend (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_suspend](#gaa1ed22da058839c9f3234ce2e41eda32)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

挂起（Suspend）DFU 传输。

<a id="r_ga0011fb5c03e6e8c2babfb677d528033b"></a>

```c
int bt_mesh_dfu_cli_resume (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_resume](#ga0011fb5c03e6e8c2babfb677d528033b)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

恢复（Resume）已挂起的传输。

<a id="r_ga4c7353f45a6e33884844fd9d2f443750"></a>

```c
int bt_mesh_dfu_cli_cancel (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx)
```

相关声明：[bt_mesh_dfu_cli_cancel](#ga4c7353f45a6e33884844fd9d2f443750)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)。

取消（Cancel）DFU 传输。

<a id="r_ga2904ba992a00ee9fba6704c1efc8f074"></a>

```c
int bt_mesh_dfu_cli_apply (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_apply](#ga2904ba992a00ee9fba6704c1efc8f074)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

应用（Apply）已完成传输的 DFU。

<a id="r_gaf76f0cdb5c6b0df12ddb495c718c3c93"></a>

```c
int bt_mesh_dfu_cli_confirm (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bt_mesh_dfu_cli_confirm](#gaf76f0cdb5c6b0df12ddb495c718c3c93)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

确认活动传输已在目标节点（Target Nodes）上应用。

<a id="r_ga073c5bc227040f1f33e7b3f2fe69a309"></a>

```c
uint8_t bt_mesh_dfu_cli_progress (struct bt_mesh_dfu_cli *cli)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_cli_progress](#ga073c5bc227040f1f33e7b3f2fe69a309)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

以完成百分比（Percentage of Completion）获取进度。

<a id="r_gad6308700322d96676635bcf0b70c74f7"></a>

```c
bool bt_mesh_dfu_cli_is_busy (struct bt_mesh_dfu_cli *cli)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_dfu_cli_is_busy](#gad6308700322d96676635bcf0b70c74f7)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)。

检查是否正在进行 DFU 传输（Transfer）。

<a id="r_ga4c33f9457d4f367760a51a771dfd2671"></a>

```c
int bt_mesh_dfu_cli_imgs_get (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, bt_mesh_dfu_img_cb_t cb, void *cb_data, uint8_t max_count)
```

相关声明：[bt_mesh_dfu_cli_imgs_get](#ga4c33f9457d4f367760a51a771dfd2671)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[bt_mesh_dfu_img_cb_t](#ga2967b89e8fc3b848b70e493f6e821761)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 DFU 镜像列表请求（Image List Request）。

<a id="r_ga20b3e7d3d3640149a20d698a6aa7dca5"></a>

```c
int bt_mesh_dfu_cli_metadata_check (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t img_idx, const struct bt_mesh_dfu_slot *slot, struct bt_mesh_dfu_metadata_status *rsp)
```

相关声明：[bt_mesh_dfu_cli_metadata_check](#ga20b3e7d3d3640149a20d698a6aa7dca5)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)、[bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)。

对给定 DFU 镜像槽（Image Slot）执行元数据检查（Metadata Check）。

<a id="r_gab754da11705a2d6a24ec828aa7862579"></a>

```c
int bt_mesh_dfu_cli_status_get (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, struct bt_mesh_dfu_target_status *rsp)
```

相关声明：[bt_mesh_dfu_cli_status_get](#gab754da11705a2d6a24ec828aa7862579)、[bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)。

获取目标节点状态（Target Node Status）。

<a id="r_ga3dd10bd1e8673973fd6db98d3ebda354"></a>

```c
int32_t bt_mesh_dfu_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_dfu_cli_timeout_get](#ga3dd10bd1e8673973fd6db98d3ebda354)。

获取当前流程超时值（Procedure Timeout Value）。

<a id="r_ga603adf5b40b6e382c9035c9f2bad99a9"></a>

```c
void bt_mesh_dfu_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_dfu_cli_timeout_set](#ga603adf5b40b6e382c9035c9f2bad99a9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置流程超时值（Procedure Timeout Value）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga0b10a95f9b7c806bfd8649280f535c96"></a>

### `BT_MESH_DFU_CLI_INIT`

```c
#define BT_MESH_DFU_CLI_INIT ( _handlers)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

展开值（Value）：

```c
{                                                                      \
        .cb = _handlers,                                               \
        .blob = { .cb = &_bt_mesh_dfu_cli_blob_handlers },             \
}
```

固件更新客户端（Firmware Update Client）模型的初始化参数（Initialization Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_handlers` | 处理函数回调结构体（Handler Callback Structure）。 |

**参阅（See Also）**：另请参阅（See Also）：bt_mesh_dfu_cli_cb。

<a id="gadee3710bb46d907a51232ca42cca7c2d"></a>

### `BT_MESH_MODEL_DFU_CLI`

```c
#define BT_MESH_MODEL_DFU_CLI ( _cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_BLOB_CLI(&(_cli)->blob),                                 \
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFU_CLI, _bt_mesh_dfu_cli_op, NULL,  \
                 _cli, &_bt_mesh_dfu_cli_cb)
```

固件更新客户端（Firmware Update Client）模型的组成数据（Composition Data）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_cli` | 指向固件更新客户端模型实例（Firmware Update Client Model Instance）的指针。 |

<a id="ga2967b89e8fc3b848b70e493f6e821761"></a>

### `bt_mesh_dfu_img_cb_t`

```c
typedef enum bt_mesh_dfu_iter(* bt_mesh_dfu_img_cb_t) (struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t idx, uint8_t total, const struct bt_mesh_dfu_img *img, void *cb_data)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

设备固件更新（DFU）镜像回调（Image Callback）。

调用 bt_mesh_dfu_cli_imgs_get 时，会针对目标节点上的每个设备固件更新镜像（DFU Image）调用镜像回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `ctx` | 收到消息的消息上下文（Message Context）。 |
| `idx` | 镜像索引（Image index）。 |
| `total` | 目标节点上的镜像总数。 |
| `img` | 给定镜像索引对应的镜像信息（Image Information）。 |
| `cb_data` | 回调数据（Callback Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_ITER_STOP` | 停止遍历镜像列表，并从 bt_mesh_dfu_cli_imgs_get 返回。 |
| `BT_MESH_DFU_ITER_CONTINUE` | 若还有剩余镜像，则继续遍历镜像列表。 |

<a id="ga2904ba992a00ee9fba6704c1efc8f074"></a>

### `bt_mesh_dfu_cli_apply()`

```c
int bt_mesh_dfu_cli_apply ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

应用（Apply）已完成传输的 DFU。

只有传输成功结束后才能应用（Apply）。应用过程结束时，调用固件更新客户端的 applied 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga4c7353f45a6e33884844fd9d2f443750"></a>

### `bt_mesh_dfu_cli_cancel()`

```c
int bt_mesh_dfu_cli_cancel ( struct bt_mesh_dfu_cli * cli, struct bt_mesh_msg_ctx * ctx )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

取消（Cancel）DFU 传输。

取消正在进行的 DFU 传输；ctx 有效时，只取消特定目标节点上的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `ctx` | 消息上下文（Message Context）；传 NULL 取消正在进行的 DFU 传输。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gaf76f0cdb5c6b0df12ddb495c718c3c93"></a>

### `bt_mesh_dfu_cli_confirm()`

```c
int bt_mesh_dfu_cli_confirm ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

确认活动传输已在目标节点（Target Nodes）上应用。

只有传输已应用后才能确认（Confirm）。确认过程结束时，调用固件更新客户端的 confirmed 回调。

对于已将影响（Effect）报告为 BT_MESH_DFU_EFFECT_UNPROV 的目标节点，预期其不响应查询；若响应，则判为失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga4c33f9457d4f367760a51a771dfd2671"></a>

### `bt_mesh_dfu_cli_imgs_get()`

```c
int bt_mesh_dfu_cli_imgs_get ( struct bt_mesh_dfu_cli * cli, struct bt_mesh_msg_ctx * ctx, bt_mesh_dfu_img_cb_t cb, void * cb_data, uint8_t max_count )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

执行 DFU 镜像列表请求（Image List Request）。

请求目标节点上的完整 DFU 镜像列表并遍历，对每个镜像调用 cb。

DFU 镜像列表请求可用于确定目标节点把不同固件存放在哪个镜像索引（Image Index）中。

等待响应，直到过程超时（Procedure Timeout）到期。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `ctx` | 消息上下文（Message Context）。 |
| `cb` | 针对每个镜像索引调用的回调（Callback）。 |
| `cb_data` | 传给 cb 的回调数据（Callback Data）。 |
| `max_count` | 返回镜像的最大数量。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gad6308700322d96676635bcf0b70c74f7"></a>

### `bt_mesh_dfu_cli_is_busy()`

```c
bool bt_mesh_dfu_cli_is_busy ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

检查是否正在进行 DFU 传输（Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

**返回（Returns）**：返回值（Returns）：BLOB 传输客户端（BLOB Transfer Client）当前正在参与传输时返回 true，否则返回 false。

<a id="ga20b3e7d3d3640149a20d698a6aa7dca5"></a>

### `bt_mesh_dfu_cli_metadata_check()`

```c
int bt_mesh_dfu_cli_metadata_check ( struct bt_mesh_dfu_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t img_idx, const struct bt_mesh_dfu_slot * slot, struct bt_mesh_dfu_metadata_status * rsp )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

对给定 DFU 镜像槽（Image Slot）执行元数据检查（Metadata Check）。

元数据检查过程（Metadata Check Procedure）允许固件更新客户端检查目标节点是否接受此 DFU 镜像槽位的传输，以及应用后的影响（Effect）。

等待响应，直到过程超时（Procedure Timeout）到期。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `ctx` | 消息上下文（Message Context）。 |
| `img_idx` | 要检查的目标节点镜像索引（Image Index）。 |
| `slot` | 待检查的 DFU 镜像槽位（Image Slot）。 |
| `rsp` | 元数据状态响应缓冲区（Metadata Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga073c5bc227040f1f33e7b3f2fe69a309"></a>

### `bt_mesh_dfu_cli_progress()`

```c
uint8_t bt_mesh_dfu_cli_progress ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

以完成百分比（Percentage of Completion）获取进度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

**返回（Returns）**：返回值（Returns）：当前传输进度的百分比；无活动传输时返回 0。

<a id="ga0011fb5c03e6e8c2babfb677d528033b"></a>

### `bt_mesh_dfu_cli_resume()`

```c
int bt_mesh_dfu_cli_resume ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

恢复（Resume）已挂起的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端实例（Firmware Update Client Instance）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga20764694315adb4f846dcff20f377417"></a>

### `bt_mesh_dfu_cli_send()`

```c
int bt_mesh_dfu_cli_send ( struct bt_mesh_dfu_cli * cli, const struct bt_mesh_blob_cli_inputs * inputs, const struct bt_mesh_blob_io * io, const struct bt_mesh_dfu_cli_xfer * xfer )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

开始分发设备固件更新（DFU）。

开始将给定槽位中的固件分发到 ctx 中的 DFU 目标节点列表。传输在后台运行，结束时通过 bt_mesh_dfu_cli_cb::ended 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `inputs` | BLOB传输客户端（BLOB Transfer Client）的传输输入。 |
| `io` | 用于读取 BLOB 的 BLOB 流（BLOB Stream）。 |
| `xfer` | 固件更新客户端传输参数（Firmware Update Client Transfer Parameters）。 |

**说明（Note）**：注意（Note）：BLOB 传输客户端输入参数的目标列表必须指向 bt_mesh_dfu_target 节点列表。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gab754da11705a2d6a24ec828aa7862579"></a>

### `bt_mesh_dfu_cli_status_get()`

```c
int bt_mesh_dfu_cli_status_get ( struct bt_mesh_dfu_cli * cli, struct bt_mesh_msg_ctx * ctx, struct bt_mesh_dfu_target_status * rsp )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

获取目标节点状态（Target Node Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `ctx` | 消息上下文（Message Context）。 |
| `rsp` | 响应数据缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gaa1ed22da058839c9f3234ce2e41eda32"></a>

### `bt_mesh_dfu_cli_suspend()`

```c
int bt_mesh_dfu_cli_suspend ( struct bt_mesh_dfu_cli * cli)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

挂起（Suspend）DFU 传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端实例（Firmware Update Client Instance）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga3dd10bd1e8673973fd6db98d3ebda354"></a>

### `bt_mesh_dfu_cli_timeout_get()`

```c
int32_t bt_mesh_dfu_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

获取当前流程超时值（Procedure Timeout Value）。

**返回（Returns）**：返回值（Returns）：已配置的过程超时（Procedure Timeout）。

<a id="ga603adf5b40b6e382c9035c9f2bad99a9"></a>

### `bt_mesh_dfu_cli_timeout_set()`

```c
void bt_mesh_dfu_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

设置流程超时值（Procedure Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的过程超时（Procedure Timeout）。 |


## 6.6\_原页交叉引用（Cross References）

- [bt_mesh_dfu_target](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md)
- [bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)
- [bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)
- [bt_mesh_dfu_cli_cb](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md)
- [bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)
- [bt_mesh_dfu_cli_xfer_blob_params](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)
- [bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)
- [固件更新客户端模型（原文：Firmware Uppdate Client model）](P006_固件更新客户端模型（原文：Firmware Uppdate Client model）.md)
- [bt_mesh_dfu_iter](../api_video_event_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md#ga82475cb72f2ea8b60e70d6987eca2ff6)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/bluetooth/mesh/dfu_cli.h](../api_file_storage_event_reference/P005_zephyr__bluetooth__mesh__dfu_cli.h_文件参考.md)
- [BT_MESH_MODEL_BLOB_CLI](../api_video_event_topic_reference/P003_蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API.md#ga882e9cec348625c7990de4ee5eb7ed5a)
- [BT_MESH_MODEL_ID_DFU_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaf477a37238ec577000a646af40862ee1)
- [BT_MESH_DFU_ITER_STOP](../api_video_event_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)
- [BT_MESH_DFU_ITER_CONTINUE](../api_video_event_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)
- [BT_MESH_DFU_EFFECT_UNPROV](../api_video_event_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)
- [bt_mesh_dfu_cli_cb::ended](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#aa3c8985490a6b2bd6fcd81dff0132060)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaf477a37238ec577000a646af40862ee1"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga882e9cec348625c7990de4ee5eb7ed5a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_应用配置（Application Configuration）.md) · [返回大纲](大纲.md) · [下一章](P007_音量偏移控制服务（Volume Offset Control Service，VOCS）.md)
