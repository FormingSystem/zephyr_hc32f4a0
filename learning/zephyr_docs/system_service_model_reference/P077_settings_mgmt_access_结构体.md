---
id: learning.zephyr-docs.system-service-model-reference.page-77
title: settings_mgmt_access_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsettings__mgmt__access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_settings\_mgmt\_access\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__mgmt__access.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_SETTINGS_MGMT_ACCESS通知回调中提供的结构。

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h>
```

<a id="details"></a>

在 `MGMT_EVT_OP_SETTINGS_MGMT_ACCESS` 通知回调中提供的结构体。此回调用于向应用通知待处理的设置读取、写入、删除、加载、保存或提交请求，并允许应用授权或拒绝它。只要所有处理函数均未返回错误，就允许访问；只要有一个返回错误，就拒绝访问。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a9b798a118844083d77af6db53df5eb37"></a>

```c
enum settings_mgmt_access_types access
```

相关声明：[settings_mgmt_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga40c179f978718409c7db43448efc8f47)、[access](#a9b798a118844083d77af6db53df5eb37)。

访问类型（Type of access）。

<a id="r_ae0f02e70ee2da823801d4d475f4a2e76"></a>

```c
char * name
```

相关声明：[name](#ae0f02e70ee2da823801d4d475f4a2e76)。

要访问的键名（key name）；仅对 `SETTINGS_ACCESS_READ`、`SETTINGS_ACCESS_WRITE`、`SETTINGS_ACCESS_DELETE` 和 `SETTINGS_ACCESS_SAVE` 设置。

<a id="r_aeb23615be870929a987c6cfbd3f445de"></a>

```c
const uint8_t * val
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[val](#aeb23615be870929a987c6cfbd3f445de)。

用户提供的数据；仅对 `SETTINGS_ACCESS_WRITE` 设置。

<a id="r_ab13bdcd8763dca5a99d3d52270f9b4d2"></a>

```c
const size_t * val_length
```

相关声明：[val_length](#ab13bdcd8763dca5a99d3d52270f9b4d2)。

用户提供的数据长度；仅对 `SETTINGS_ACCESS_WRITE` 设置。

## 77.2\_详细说明（Detailed Documentation）

<a id="a9b798a118844083d77af6db53df5eb37"></a>

### `access`

```c
enum settings_mgmt_access_types settings_mgmt_access::access
```

访问类型（Type of access）。

<a id="ae0f02e70ee2da823801d4d475f4a2e76"></a>

### `name`

```c
char* settings_mgmt_access::name
```

要访问的键名（key name）；仅对 `SETTINGS_ACCESS_READ`、`SETTINGS_ACCESS_WRITE`、`SETTINGS_ACCESS_DELETE` 和 `SETTINGS_ACCESS_SAVE` 设置。

注意：选择 `CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK` 时，必要时处理函数可以更改此项以重定向设置访问，但不得超过设置字符串的最大长度，即 `CONFIG_MCUMGR_GRP_SETTINGS_NAME_LEN`。

注意：此字符串必须以空字符终止。

<a id="aeb23615be870929a987c6cfbd3f445de"></a>

### `val`

```c
const uint8_t* settings_mgmt_access::val
```

用户提供的数据；仅对 `SETTINGS_ACCESS_WRITE` 设置。

<a id="ab13bdcd8763dca5a99d3d52270f9b4d2"></a>

### `val_length`

```c
const size_t* settings_mgmt_access::val_length
```

用户提供的数据长度；仅对 `SETTINGS_ACCESS_WRITE` 设置。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h`

## 77.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_SETTINGS_MGMT_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)
- [zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h_source.html)
- [settings_mgmt_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga40c179f978718409c7db43448efc8f47)
- [SETTINGS_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)
- [SETTINGS_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)
- [SETTINGS_ACCESS_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)
- [SETTINGS_ACCESS_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_regset_target_lib_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_smp_client_object_结构体.md)
