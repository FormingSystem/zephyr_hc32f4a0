---
id: learning.zephyr-docs.api-video-event-topic-reference.page-4
title: 蓝牙 Mesh 设备固件更新（Device Firmware Update）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙 Mesh 设备固件更新（Device Firmware Update）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-groups"></a>
<a id="groups"></a>

## 4.1\_主题（Topics）

<a id="r_bt_5Fmesh_5Fdfu_5Fmetadata"></a>

相关声明：[蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据](../api_vector_pipeline_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据.md)。

蓝牙 Mesh DFU 元数据的公共类型与函数。

<a id="r_bt_5Fmesh_5Fdfu_5Fsrv"></a>

相关声明：[固件更新服务器模型（Firmware Update Server model）](../api_update_memory_topic_reference/P001_固件更新服务器模型（Firmware Update Server model）.md)。

蓝牙 Mesh 固件更新服务器模型的 API。

<a id="r_bt_5Fmesh_5Fdfu_5Fcli"></a>

相关声明：[固件更新客户端模型（原文：Firmware Uppdate Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html)。

蓝牙 Mesh 固件更新客户端模型的 API。

<a id="header-files"></a>
<a id="files"></a>

## 4.2\_文件（Files）

<a id="r_dfu_2Eh"></a>

```c
file dfu.h
```

相关声明：[dfu.h](../api_file_service_reference/P006_zephyr__bluetooth__mesh__dfu.h_文件参考.md)。

蓝牙Mesh设备固件更新（Device Firmware Update，DFU）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.3\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfu_5Fimg"></a>

```c
struct bt_mesh_dfu_img
```

相关声明：[bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)。

设备固件更新（DFU）的映像实例。

<a id="r_bt_5Fmesh_5Fdfu_5Fslot"></a>

```c
struct bt_mesh_dfu_slot
```

相关声明：[bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)。

设备固件更新（DFU）分发使用的映像槽位。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.4\_宏定义（Macros）

<a id="r_gacd0f7b01837809a0a92d27f248a9fdd3"></a>

```c
#define CONFIG_BT_MESH_DFU_FWID_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_FWID_MAXLEN](#gacd0f7b01837809a0a92d27f248a9fdd3)。

<a id="r_ga8f2afd35a2215f51cd08debe6e1c8ae4"></a>

```c
#define CONFIG_BT_MESH_DFU_METADATA_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_METADATA_MAXLEN](#ga8f2afd35a2215f51cd08debe6e1c8ae4)。

<a id="r_gaa0812409217dd069b00d386d8ab17f5c"></a>

```c
#define CONFIG_BT_MESH_DFU_URI_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_URI_MAXLEN](#gaa0812409217dd069b00d386d8ab17f5c)。

<a id="r_gab517e917ec3279ba50f1ac92ec62b8cf"></a>

```c
#define CONFIG_BT_MESH_DFU_SLOT_CNT 0
```

相关声明：[CONFIG_BT_MESH_DFU_SLOT_CNT](#gab517e917ec3279ba50f1ac92ec62b8cf)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.5\_枚举（Enumerations）

<a id="r_ga99919dcee1e41bc74bd59e33bec2ded2"></a>

```c
enum bt_mesh_dfu_phase { BT_MESH_DFU_PHASE_IDLE , BT_MESH_DFU_PHASE_TRANSFER_ERR , BT_MESH_DFU_PHASE_TRANSFER_ACTIVE , BT_MESH_DFU_PHASE_VERIFY , BT_MESH_DFU_PHASE_VERIFY_OK , BT_MESH_DFU_PHASE_VERIFY_FAIL , BT_MESH_DFU_PHASE_APPLYING , BT_MESH_DFU_PHASE_TRANSFER_CANCELED , BT_MESH_DFU_PHASE_APPLY_SUCCESS , BT_MESH_DFU_PHASE_APPLY_FAIL , BT_MESH_DFU_PHASE_UNKNOWN }
```

相关声明：[bt_mesh_dfu_phase](#ga99919dcee1e41bc74bd59e33bec2ded2)、[BT_MESH_DFU_PHASE_IDLE](#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156)、[BT_MESH_DFU_PHASE_TRANSFER_ERR](#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771)、[BT_MESH_DFU_PHASE_TRANSFER_ACTIVE](#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad)、[BT_MESH_DFU_PHASE_VERIFY](#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65)、[BT_MESH_DFU_PHASE_VERIFY_OK](#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8)、[BT_MESH_DFU_PHASE_VERIFY_FAIL](#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e)、[BT_MESH_DFU_PHASE_APPLYING](#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f)、[BT_MESH_DFU_PHASE_TRANSFER_CANCELED](#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51)、[BT_MESH_DFU_PHASE_APPLY_SUCCESS](#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca)、[BT_MESH_DFU_PHASE_APPLY_FAIL](#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266)、[BT_MESH_DFU_PHASE_UNKNOWN](#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)。

设备固件更新传输阶段（DFU Transfer Phase）。

<a id="r_ga9e627a3c15de782faa11ef6c4ec5e05d"></a>

```c
enum bt_mesh_dfu_status { BT_MESH_DFU_SUCCESS , BT_MESH_DFU_ERR_RESOURCES , BT_MESH_DFU_ERR_WRONG_PHASE , BT_MESH_DFU_ERR_INTERNAL , BT_MESH_DFU_ERR_FW_IDX , BT_MESH_DFU_ERR_METADATA , BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE , BT_MESH_DFU_ERR_BLOB_XFER_BUSY }
```

相关声明：[bt_mesh_dfu_status](#ga9e627a3c15de782faa11ef6c4ec5e05d)、[BT_MESH_DFU_SUCCESS](#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad)、[BT_MESH_DFU_ERR_RESOURCES](#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27)、[BT_MESH_DFU_ERR_WRONG_PHASE](#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047)、[BT_MESH_DFU_ERR_INTERNAL](#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806)、[BT_MESH_DFU_ERR_FW_IDX](#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c)、[BT_MESH_DFU_ERR_METADATA](#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934)、[BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE](#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a)、[BT_MESH_DFU_ERR_BLOB_XFER_BUSY](#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)。

设备固件更新状态（DFU Status）。

<a id="r_gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>

```c
enum bt_mesh_dfu_effect { BT_MESH_DFU_EFFECT_NONE , BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR , BT_MESH_DFU_EFFECT_COMP_CHANGE , BT_MESH_DFU_EFFECT_UNPROV }
```

相关声明：[bt_mesh_dfu_effect](#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)、[BT_MESH_DFU_EFFECT_NONE](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e)、[BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc)、[BT_MESH_DFU_EFFECT_COMP_CHANGE](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8)、[BT_MESH_DFU_EFFECT_UNPROV](#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)。

设备固件更新传输（DFU Transfer）的预期影响（Expected Effect）。

<a id="r_ga82475cb72f2ea8b60e70d6987eca2ff6"></a>

```c
enum bt_mesh_dfu_iter { BT_MESH_DFU_ITER_STOP , BT_MESH_DFU_ITER_CONTINUE }
```

相关声明：[bt_mesh_dfu_iter](#ga82475cb72f2ea8b60e70d6987eca2ff6)、[BT_MESH_DFU_ITER_STOP](#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)、[BT_MESH_DFU_ITER_CONTINUE](#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)。

设备固件更新遍历回调（DFU Iteration Callbacks）的动作（Action）。

## 4.6\_详细说明（Detailed Documentation）

<a id="gacd0f7b01837809a0a92d27f248a9fdd3"></a>

### `CONFIG_BT_MESH_DFU_FWID_MAXLEN`

```c
#define CONFIG_BT_MESH_DFU_FWID_MAXLEN 0
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="ga8f2afd35a2215f51cd08debe6e1c8ae4"></a>

### `CONFIG_BT_MESH_DFU_METADATA_MAXLEN`

```c
#define CONFIG_BT_MESH_DFU_METADATA_MAXLEN 0
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="gab517e917ec3279ba50f1ac92ec62b8cf"></a>

### `CONFIG_BT_MESH_DFU_SLOT_CNT`

```c
#define CONFIG_BT_MESH_DFU_SLOT_CNT 0
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="gaa0812409217dd069b00d386d8ab17f5c"></a>

### `CONFIG_BT_MESH_DFU_URI_MAXLEN`

```c
#define CONFIG_BT_MESH_DFU_URI_MAXLEN 0
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>

### `bt_mesh_dfu_effect`

```c
enum bt_mesh_dfu_effect
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

设备固件更新传输（DFU Transfer）的预期影响（Expected Effect）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_EFFECT_NONE` | 节点组成数据（Composition Data）未改变。 |
| `BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR` | 节点组成数据（Composition Data）已改变，且节点不支持远程配网（Remote Provisioning）。 |
| `BT_MESH_DFU_EFFECT_COMP_CHANGE` | 节点组成数据（Composition Data）已改变，且支持远程配网（Remote Provisioning）。节点支持组成数据页 0x80，其内容不同于 0x0 页。 |
| `BT_MESH_DFU_EFFECT_UNPROV` | 更新后节点将变为未配网状态（Unprovisioned）。 |

<a id="ga82475cb72f2ea8b60e70d6987eca2ff6"></a>

### `bt_mesh_dfu_iter`

```c
enum bt_mesh_dfu_iter
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

设备固件更新遍历回调（DFU Iteration Callbacks）的动作（Action）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_ITER_STOP` | 停止遍历（Stop Iterating）。 |
| `BT_MESH_DFU_ITER_CONTINUE` | 继续遍历（Continue Iterating）。 |

<a id="ga99919dcee1e41bc74bd59e33bec2ded2"></a>

### `bt_mesh_dfu_phase`

```c
enum bt_mesh_dfu_phase
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

设备固件更新传输阶段（DFU Transfer Phase）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_PHASE_IDLE` | 已准备好开始接收固件流程（Receive Firmware Procedure）。 |
| `BT_MESH_DFU_PHASE_TRANSFER_ERR` | 传输二进制大对象流程（Transfer BLOB Procedure）失败。 |
| `BT_MESH_DFU_PHASE_TRANSFER_ACTIVE` | 正在执行接收固件流程（Receive Firmware Procedure）。 |
| `BT_MESH_DFU_PHASE_VERIFY` | 正在执行验证固件流程（Verify Firmware Procedure）。 |
| `BT_MESH_DFU_PHASE_VERIFY_OK` | 验证固件流程（Verify Firmware Procedure）已成功完成。 |
| `BT_MESH_DFU_PHASE_VERIFY_FAIL` | 验证固件流程（Verify Firmware Procedure）失败。 |
| `BT_MESH_DFU_PHASE_APPLYING` | 正在执行应用新固件流程（Apply New Firmware Procedure）。 |
| `BT_MESH_DFU_PHASE_TRANSFER_CANCELED` | 固件传输（Firmware Transfer）已取消。 |
| `BT_MESH_DFU_PHASE_APPLY_SUCCESS` | 固件应用（Firmware Applying）成功。 |
| `BT_MESH_DFU_PHASE_APPLY_FAIL` | 固件应用（Firmware Applying）失败。 |
| `BT_MESH_DFU_PHASE_UNKNOWN` | 尚未获取节点所处阶段（Phase）。 |

<a id="ga9e627a3c15de782faa11ef6c4ec5e05d"></a>

### `bt_mesh_dfu_status`

```c
enum bt_mesh_dfu_status
```

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

设备固件更新状态（DFU Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_SUCCESS` | 消息已成功处理（Processed Successfully）。 |
| `BT_MESH_DFU_ERR_RESOURCES` | 节点上的资源不足（Insufficient Resources）。 |
| `BT_MESH_DFU_ERR_WRONG_PHASE` | 服务器处于当前阶段（Phase）时，无法执行该操作。 |
| `BT_MESH_DFU_ERR_INTERNAL` | 节点发生内部错误（Internal Error）。 |
| `BT_MESH_DFU_ERR_FW_IDX` | 消息包含非预期的固件索引（Firmware Index）值。 |
| `BT_MESH_DFU_ERR_METADATA` | 元数据检查（Metadata Check）失败。 |
| `BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE` | 服务器无法启动固件更新（Firmware Update）。 |
| `BT_MESH_DFU_ERR_BLOB_XFER_BUSY` | 另一个 BLOB 传输正在进行。 |


## 4.7\_原页交叉引用（Cross References）

- [蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据](../api_vector_pipeline_topic_reference/P004_蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据.md)
- [固件更新服务器模型（Firmware Update Server model）](../api_update_memory_topic_reference/P001_固件更新服务器模型（Firmware Update Server model）.md)
- [固件更新客户端模型（原文：Firmware Uppdate Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html)
- [dfu.h](../api_file_service_reference/P006_zephyr__bluetooth__mesh__dfu.h_文件参考.md)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e"></a>
<a id="ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc"></a>
<a id="ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8"></a>
<a id="ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211"></a>
<a id="gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be"></a>
<a id="gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266"></a>
<a id="gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a"></a>
<a id="gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25"></a>

---

[上一章](P003_蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API.md) · [返回大纲](大纲.md) · [下一章](P005_数字可寻址照明接口（DALI）.md)
