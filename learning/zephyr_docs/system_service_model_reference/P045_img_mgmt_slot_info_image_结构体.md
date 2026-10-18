---
id: learning.zephyr-docs.system-service-model-reference.page-45
title: img_mgmt_slot_info_image_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__slot__info__image.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_img\_mgmt\_slot\_info\_image\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__slot__info__image.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE通知回调中提供的结构。使用槽位信息命令（Slot Info Command）时，每个映像调用该回调一次，可借此在响应中返回附加信息或字段。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE通知回调中提供的结构。使用槽位信息命令（Slot Info Command）时，每个映像调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a2456d0f9cc29a5cb56d5e8fb45f149d7"></a>

```c
const uint8_t image
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[image](#a2456d0f9cc29a5cb56d5e8fb45f149d7)。

当前正在枚举的映像。

<a id="r_af19f99ee4e86a586177b014c364be94c"></a>

```c
zcbor_state_t * zse
```

相关声明：[zse](#af19f99ee4e86a586177b014c364be94c)。

当前用于输出信息的 zcbor 编码器，可用它添加额外字段。

## 45.2\_详细说明（Detailed Documentation）

<a id="a2456d0f9cc29a5cb56d5e8fb45f149d7"></a>

### `image`

```c
const uint8_t img_mgmt_slot_info_image::image
```

当前正在枚举的映像。

<a id="af19f99ee4e86a586177b014c364be94c"></a>

### `zse`

```c
zcbor_state_t* img_mgmt_slot_info_image::zse
```

当前用于输出信息的 zcbor 编码器，可用它添加额外字段。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h`

## 45.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_img_mgmt_image_confirmed_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_img_mgmt_slot_info_slot_结构体.md)
