---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-10
title: 映像管理回调（Image Management Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_映像管理回调（Image Management Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 映像管理回调 API

<a id="details"></a>

MCUmgr 映像管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_img_5Fmgmt_5Fcallbacks_2Eh"></a>

```c
file img_mgmt_callbacks.h
```

相关声明：[img_mgmt_callbacks.h](../api_file_supplement_reference/P044_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_callbacks.h_文件参考.md)。

MCUmgr映像管理回调（Image Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_img_5Fmgmt_5Fupload_5Fcheck"></a>

```c
struct img_mgmt_upload_check
```

相关声明：[img_mgmt_upload_check](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md)。

MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK通知回调中提供的结构。该回调用于将来自客户端的待处理固件上传包通知应用，并授权或拒绝该上传。

<a id="r_img_5Fmgmt_5Fimage_5Fconfirmed"></a>

```c
struct img_mgmt_image_confirmed
```

相关声明：[img_mgmt_image_confirmed](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md)。

MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED通知回调中提供的结构。该回调用于通知应用映像确认（Image Confirmation）已成功执行。

<a id="r_img_5Fmgmt_5Fstate_5Fslot_5Fencode"></a>

```c
struct img_mgmt_state_slot_encode
```

相关声明：[img_mgmt_state_slot_encode](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md)。

MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE通知回调中提供的结构。该回调允许应用或模块向映像槽位状态（Image Slot State）响应追加自定义字段。

<a id="r_img_5Fmgmt_5Fslot_5Finfo_5Fimage"></a>

```c
struct img_mgmt_slot_info_image
```

相关声明：[img_mgmt_slot_info_image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md)。

MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE通知回调中提供的结构。使用槽位信息命令（Slot Info Command）时，每个映像调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="r_img_5Fmgmt_5Fslot_5Finfo_5Fslot"></a>

```c
struct img_mgmt_slot_info_slot
```

相关声明：[img_mgmt_slot_info_slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md)。

MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT通知回调中提供的结构。使用槽位信息命令（Slot Info Command）时，每个映像的每个槽位调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_ga3fa2c42bade08cca1122e32f6315f107"></a>

```c
enum img_mgmt_group_events { MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 0) , MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 1) , MGMT_EVT_OP_IMG_MGMT_DFU_STARTED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 2) , MGMT_EVT_OP_IMG_MGMT_DFU_PENDING = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 3) , MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 4) , MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 5) , MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 6) , MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 7) , MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 8) , MGMT_EVT_OP_IMG_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_IMG) }
```

相关声明：[img_mgmt_group_events](#ga3fa2c42bade08cca1122e32f6315f107)、[MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK](#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)、[MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED](#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8)、[MGMT_EVT_OP_IMG_MGMT_DFU_STARTED](#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf)、[MGMT_EVT_OP_IMG_MGMT_DFU_PENDING](#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4)、[MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED](#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)、[MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE](#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88)、[MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE](#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)、[MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE](#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)、[MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT](#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0)、[MGMT_EVT_OP_IMG_MGMT_ALL](#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf)。

镜像管理组（Image Management Group）的管理事件操作码（MGMT Event Opcodes）。

## 10.4\_详细说明（Detailed Documentation）

<a id="ga3fa2c42bade08cca1122e32f6315f107"></a>

### `img_mgmt_group_events`

```c
enum img_mgmt_group_events
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
```

镜像管理组（Image Management Group）的管理事件操作码（MGMT Event Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK` | 客户端发送文件上传分块（File Upload Chunk）时的回调，`data` 为 `img_mgmt_upload_check`。 |
| `MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED` | 设备固件更新（DFU）操作停止时的回调。 |
| `MGMT_EVT_OP_IMG_MGMT_DFU_STARTED` | 设备固件更新（DFU）操作开始时的回调。 |
| `MGMT_EVT_OP_IMG_MGMT_DFU_PENDING` | 设备固件更新（DFU）操作完成传输时的回调。 |
| `MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED` | 镜像确认（Image Confirmation）时的回调，`data` 为 `img_mgmt_image_confirmed`。 |
| `MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE` | 镜像写入命令完成闪存写入（Flash Write）时的回调。 |
| `MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE` | 为响应编码镜像槽状态（Image Slot State）时的回调，`data` 为 `img_mgmt_state_slot_encode`。 |
| `MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE` | 槽列表命令为镜像输出字段时的回调，`data` 为 `img_mgmt_slot_info_image`。 |
| `MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT` | 槽列表命令为镜像的某个槽输出字段时的回调，`data` 为 `img_mgmt_slot_info_slot`。 |
| `MGMT_EVT_OP_IMG_MGMT_ALL` | 用于启用所有 `img_mgmt_group` 事件（Events）。 |


## 10.5\_原页交叉引用（Cross References）

- [img_mgmt_callbacks.h](../api_file_supplement_reference/P044_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_callbacks.h_文件参考.md)
- [img_mgmt_upload_check](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md)
- [img_mgmt_image_confirmed](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md)
- [img_mgmt_state_slot_encode](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md)
- [img_mgmt_slot_info_image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md)
- [img_mgmt_slot_info_slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0"></a>
<a id="gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf"></a>

---

[上一章](P009_向量缩放（Vector Scale）.md) · [返回大纲](大纲.md) · [下一章](P011_内存组（Memory Banks）的驱动API。.md)
