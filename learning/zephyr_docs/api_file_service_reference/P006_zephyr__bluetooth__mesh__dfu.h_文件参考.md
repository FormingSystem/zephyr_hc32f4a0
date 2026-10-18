---
id: learning.zephyr-docs.api-file-service-reference.page-6
title: zephyr__bluetooth__mesh__dfu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_bluetooth\_\_mesh\_\_dfu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh设备固件更新（Device Firmware Update，DFU）API的头文件。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/blob.h>
```

查看此文件的源码。

蓝牙Mesh设备固件更新（Device Firmware Update，DFU）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

## 6.2\_宏定义（Macros）

<a id="r_gacd0f7b01837809a0a92d27f248a9fdd3"></a>

```c
#define CONFIG_BT_MESH_DFU_FWID_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_FWID_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gacd0f7b01837809a0a92d27f248a9fdd3)。

<a id="r_ga8f2afd35a2215f51cd08debe6e1c8ae4"></a>

```c
#define CONFIG_BT_MESH_DFU_METADATA_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_METADATA_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga8f2afd35a2215f51cd08debe6e1c8ae4)。

<a id="r_gaa0812409217dd069b00d386d8ab17f5c"></a>

```c
#define CONFIG_BT_MESH_DFU_URI_MAXLEN 0
```

相关声明：[CONFIG_BT_MESH_DFU_URI_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gaa0812409217dd069b00d386d8ab17f5c)。

<a id="r_gab517e917ec3279ba50f1ac92ec62b8cf"></a>

```c
#define CONFIG_BT_MESH_DFU_SLOT_CNT 0
```

相关声明：[CONFIG_BT_MESH_DFU_SLOT_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gab517e917ec3279ba50f1ac92ec62b8cf)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_ga99919dcee1e41bc74bd59e33bec2ded2"></a>

```c
enum bt_mesh_dfu_phase { BT_MESH_DFU_PHASE_IDLE , BT_MESH_DFU_PHASE_TRANSFER_ERR , BT_MESH_DFU_PHASE_TRANSFER_ACTIVE , BT_MESH_DFU_PHASE_VERIFY , BT_MESH_DFU_PHASE_VERIFY_OK , BT_MESH_DFU_PHASE_VERIFY_FAIL , BT_MESH_DFU_PHASE_APPLYING , BT_MESH_DFU_PHASE_TRANSFER_CANCELED , BT_MESH_DFU_PHASE_APPLY_SUCCESS , BT_MESH_DFU_PHASE_APPLY_FAIL , BT_MESH_DFU_PHASE_UNKNOWN }
```

相关声明：[bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)、[BT_MESH_DFU_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156)、[BT_MESH_DFU_PHASE_TRANSFER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771)、[BT_MESH_DFU_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad)、[BT_MESH_DFU_PHASE_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65)、[BT_MESH_DFU_PHASE_VERIFY_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8)、[BT_MESH_DFU_PHASE_VERIFY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e)、[BT_MESH_DFU_PHASE_APPLYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f)、[BT_MESH_DFU_PHASE_TRANSFER_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51)、[BT_MESH_DFU_PHASE_APPLY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca)、[BT_MESH_DFU_PHASE_APPLY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266)、[BT_MESH_DFU_PHASE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)。

设备固件更新传输阶段（DFU Transfer Phase）。

<a id="r_ga9e627a3c15de782faa11ef6c4ec5e05d"></a>

```c
enum bt_mesh_dfu_status { BT_MESH_DFU_SUCCESS , BT_MESH_DFU_ERR_RESOURCES , BT_MESH_DFU_ERR_WRONG_PHASE , BT_MESH_DFU_ERR_INTERNAL , BT_MESH_DFU_ERR_FW_IDX , BT_MESH_DFU_ERR_METADATA , BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE , BT_MESH_DFU_ERR_BLOB_XFER_BUSY }
```

相关声明：[bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)、[BT_MESH_DFU_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad)、[BT_MESH_DFU_ERR_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27)、[BT_MESH_DFU_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047)、[BT_MESH_DFU_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806)、[BT_MESH_DFU_ERR_FW_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c)、[BT_MESH_DFU_ERR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934)、[BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a)、[BT_MESH_DFU_ERR_BLOB_XFER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)。

设备固件更新状态（DFU Status）。

<a id="r_gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>

```c
enum bt_mesh_dfu_effect { BT_MESH_DFU_EFFECT_NONE , BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR , BT_MESH_DFU_EFFECT_COMP_CHANGE , BT_MESH_DFU_EFFECT_UNPROV }
```

相关声明：[bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)、[BT_MESH_DFU_EFFECT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e)、[BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc)、[BT_MESH_DFU_EFFECT_COMP_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8)、[BT_MESH_DFU_EFFECT_UNPROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)。

设备固件更新传输（DFU Transfer）的预期影响（Expected Effect）。

<a id="r_ga82475cb72f2ea8b60e70d6987eca2ff6"></a>

```c
enum bt_mesh_dfu_iter { BT_MESH_DFU_ITER_STOP , BT_MESH_DFU_ITER_CONTINUE }
```

相关声明：[bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)、[BT_MESH_DFU_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)、[BT_MESH_DFU_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)。

设备固件更新遍历回调（DFU Iteration Callbacks）的动作（Action）。


## 6.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/bluetooth/mesh/blob.h](../api_source_reference/P068_blob.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P126_dfu.h_源码浏览.md)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [CONFIG_BT_MESH_DFU_FWID_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gacd0f7b01837809a0a92d27f248a9fdd3)
- [CONFIG_BT_MESH_DFU_METADATA_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga8f2afd35a2215f51cd08debe6e1c8ae4)
- [CONFIG_BT_MESH_DFU_URI_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gaa0812409217dd069b00d386d8ab17f5c)
- [CONFIG_BT_MESH_DFU_SLOT_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gab517e917ec3279ba50f1ac92ec62b8cf)
- [bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)
- [BT_MESH_DFU_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156)
- [BT_MESH_DFU_PHASE_TRANSFER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771)
- [BT_MESH_DFU_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad)
- [BT_MESH_DFU_PHASE_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65)
- [BT_MESH_DFU_PHASE_VERIFY_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8)
- [BT_MESH_DFU_PHASE_VERIFY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e)
- [BT_MESH_DFU_PHASE_APPLYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f)
- [BT_MESH_DFU_PHASE_TRANSFER_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51)
- [BT_MESH_DFU_PHASE_APPLY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca)
- [BT_MESH_DFU_PHASE_APPLY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266)
- [BT_MESH_DFU_PHASE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [BT_MESH_DFU_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad)
- [BT_MESH_DFU_ERR_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27)
- [BT_MESH_DFU_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047)
- [BT_MESH_DFU_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806)
- [BT_MESH_DFU_ERR_FW_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c)
- [BT_MESH_DFU_ERR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934)
- [BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a)
- [BT_MESH_DFU_ERR_BLOB_XFER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [BT_MESH_DFU_EFFECT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e)
- [BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc)
- [BT_MESH_DFU_EFFECT_COMP_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8)
- [BT_MESH_DFU_EFFECT_UNPROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)
- [bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)
- [BT_MESH_DFU_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)
- [BT_MESH_DFU_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dap__dap_link.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__net__dhcpv6_server.h_文件参考.md)
