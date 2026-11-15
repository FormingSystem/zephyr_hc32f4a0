---
id: learning.zephyr-docs.api-file-supplement-reference.page-44
title: zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_img\_mgmt\_\_img\_mgmt\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr映像管理回调（Image Management Callback）定义的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zcbor_common.h>
```

查看此文件的源码。

MCUmgr映像管理回调（Image Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 44.1\_数据结构（Data Structures）

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

## 44.2\_枚举（Enumerations）

<a id="r_ga3fa2c42bade08cca1122e32f6315f107"></a>

```c
enum img_mgmt_group_events { MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 0) , MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 1) , MGMT_EVT_OP_IMG_MGMT_DFU_STARTED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 2) , MGMT_EVT_OP_IMG_MGMT_DFU_PENDING = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 3) , MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 4) , MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 5) , MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 6) , MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 7) , MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 8) , MGMT_EVT_OP_IMG_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_IMG) }
```

相关声明：[img_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#ga3fa2c42bade08cca1122e32f6315f107)、[MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)、[MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8)、[MGMT_EVT_OP_IMG_MGMT_DFU_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf)、[MGMT_EVT_OP_IMG_MGMT_DFU_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4)、[MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)、[MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88)、[MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)、[MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)、[MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0)、[MGMT_EVT_OP_IMG_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf)。

镜像管理组（Image Management Group）的管理事件操作码（MGMT Event Opcodes）。


## 44.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P091_img_mgmt_callbacks.h_源码浏览.md)
- [img_mgmt_upload_check](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)
- [img_mgmt_image_confirmed](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)
- [img_mgmt_state_slot_encode](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md)
- [MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)
- [img_mgmt_slot_info_image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md)
- [MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)
- [img_mgmt_slot_info_slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md)
- [MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0)
- [img_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#ga3fa2c42bade08cca1122e32f6315f107)
- [MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8)
- [MGMT_EVT_OP_IMG_MGMT_DFU_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf)
- [MGMT_EVT_OP_IMG_MGMT_DFU_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88)
- [MGMT_EVT_OP_IMG_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf)

<a id="header-details"></a>

---

[上一章](P043_zephyr__net__ieee802154_pkt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__arch__tricore__error.h_文件参考.md)
