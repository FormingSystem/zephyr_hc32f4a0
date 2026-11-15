---
id: learning.zephyr-docs.system-service-model-reference.page-64
title: mcumgr_image_upload_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__upload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_mcumgr\_image\_upload\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__upload.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr的映像上传响应（Image Upload Response）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

MCUmgr的映像上传响应（Image Upload Response）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_a5522d2958df295c72fd00212155c7eee"></a>

```c
enum mcumgr_err_t status
```

相关声明：[mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)、[status](#a5522d2958df295c72fd00212155c7eee)。

状态（Status）。

<a id="r_ade29d2b559d9709b7372874e993e267c"></a>

```c
size_t image_upload_offset
```

相关声明：[image_upload_offset](#ade29d2b559d9709b7372874e993e267c)。

报告的映像偏移量。

## 64.2\_详细说明（Detailed Documentation）

<a id="ade29d2b559d9709b7372874e993e267c"></a>

### `image_upload_offset`

```c
size_t mcumgr_image_upload::image_upload_offset
```

报告的映像偏移量。

<a id="a5522d2958df295c72fd00212155c7eee"></a>

### `status`

```c
enum mcumgr_err_t mcumgr_image_upload::status
```

状态（Status）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_mcumgr_image_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_mcumgr_serial_rx_ctxt_结构体.md)
