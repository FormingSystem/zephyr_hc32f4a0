---
id: learning.zephyr-docs.system-service-model-reference.page-50
title: img_mgmt_upload_check_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__check.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_img\_mgmt\_upload\_check\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__check.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK通知回调中提供的结构。该回调用于将来自客户端的待处理固件上传包通知应用，并授权或拒绝该上传。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
```

<a id="details"></a>

在 `MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK` 通知回调中提供的结构体。此回调用于向应用通知客户端待处理的固件上传数据包，并允许应用授权或拒绝它。只有所有通知处理函数都返回 `MGMT_ERR_EOK` 时，才允许上传；只要有一个返回错误，就拒绝上传。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_aea96e650e2701e6064638dd4c384df55"></a>

```c
struct img_mgmt_upload_action * action
```

相关声明：[img_mgmt_upload_action](P049_img_mgmt_upload_action_结构体.md)、[action](#aea96e650e2701e6064638dd4c384df55)。

要执行的动作（action）。

<a id="r_ab8a3e937302b1def309508eace664793"></a>

```c
struct img_mgmt_upload_req * req
```

相关声明：[img_mgmt_upload_req](P051_img_mgmt_upload_req_结构体.md)、[req](#ab8a3e937302b1def309508eace664793)。

上传请求信息。

## 50.2\_详细说明（Detailed Documentation）

<a id="aea96e650e2701e6064638dd4c384df55"></a>

### `action`

```c
struct img_mgmt_upload_action* img_mgmt_upload_check::action
```

要执行的动作（action）。

<a id="ab8a3e937302b1def309508eace664793"></a>

### `req`

```c
struct img_mgmt_upload_req* img_mgmt_upload_check::req
```

上传请求信息。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h`

## 50.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html)
- [img_mgmt_upload_action](P049_img_mgmt_upload_action_结构体.md)
- [img_mgmt_upload_req](P051_img_mgmt_upload_req_结构体.md)
- [MGMT_ERR_EOK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_img_mgmt_upload_action_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_img_mgmt_upload_req_结构体.md)
