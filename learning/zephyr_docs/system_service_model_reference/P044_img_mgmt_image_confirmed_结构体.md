---
id: learning.zephyr-docs.system-service-model-reference.page-44
title: img_mgmt_image_confirmed_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__image__confirmed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_img\_mgmt\_image\_confirmed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__image__confirmed.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED通知回调中提供的结构。该回调用于通知应用映像确认（Image Confirmation）已成功执行。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED通知回调中提供的结构。该回调用于通知应用映像确认（Image Confirmation）已成功执行。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a2cd305cbe1446fd26b97a25cacad0e5c"></a>

```c
const uint8_t image
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[image](#a2cd305cbe1446fd26b97a25cacad0e5c)。

已确认的映像编号。

## 44.2\_详细说明（Detailed Documentation）

<a id="a2cd305cbe1446fd26b97a25cacad0e5c"></a>

### `image`

```c
const uint8_t img_mgmt_image_confirmed::image
```

已确认的映像编号。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h`

## 44.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_img_mgmt_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_img_mgmt_slot_info_image_结构体.md)
