---
id: learning.zephyr-docs.system-service-model-reference.page-63
title: mcumgr_image_state_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_mcumgr\_image\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr的映像列表响应（Image List Response）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

MCUmgr的映像列表响应（Image List Response）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_a4ec39c59f3cfe789dabf7fc361ff86ac"></a>

```c
enum mcumgr_err_t status
```

相关声明：[mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)、[status](#a4ec39c59f3cfe789dabf7fc361ff86ac)。

状态（Status）。

<a id="r_afd36103c373d709733ee928326c50343"></a>

```c
int image_list_length
```

相关声明：[image_list_length](#afd36103c373d709733ee928326c50343)。

`image_list` 的长度。

<a id="r_af7bd52b3a18ad190e0159c5e928b857e"></a>

```c
struct mcumgr_image_data * image_list
```

相关声明：[mcumgr_image_data](P061_mcumgr_image_data_结构体.md)、[image_list](#af7bd52b3a18ad190e0159c5e928b857e)。

映像列表指针。

## 63.2\_详细说明（Detailed Documentation）

<a id="af7bd52b3a18ad190e0159c5e928b857e"></a>

### `image_list`

```c
struct mcumgr_image_data* mcumgr_image_state::image_list
```

映像列表指针。

<a id="afd36103c373d709733ee928326c50343"></a>

### `image_list_length`

```c
int mcumgr_image_state::image_list_length
```

`image_list` 的长度。

<a id="a4ec39c59f3cfe789dabf7fc361ff86ac"></a>

### `status`

```c
enum mcumgr_err_t mcumgr_image_state::status
```

状态（Status）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [mcumgr_image_data](P061_mcumgr_image_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_mcumgr_image_list_flags_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_mcumgr_image_upload_结构体.md)
