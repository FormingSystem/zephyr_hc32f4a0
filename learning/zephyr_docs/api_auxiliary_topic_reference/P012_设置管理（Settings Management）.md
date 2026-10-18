---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-12
title: 设置管理（Settings Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_设置管理（Settings Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 设置管理 API

<a id="details"></a>

MCUmgr 设置管理 API

<a id="header-groups"></a>
<a id="groups"></a>

## 12.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Fsettings_5Fmgmt"></a>

相关声明：[设置管理回调（Settings Management Callbacks）](P011_设置管理回调（Settings Management Callbacks）.md)。

MCUmgr 设置管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 12.2\_文件（Files）

<a id="r_settings_5Fmgmt_2Eh"></a>

```c
file settings_mgmt.h
```

相关声明：[settings_mgmt.h](../api_file_interface_reference/P052_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt.h_文件参考.md)。

MCUmgr设置管理组（Settings Management Group）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_gafb39b95aec3183531602aa6964ceb1cc"></a>

```c
enum settings_mgmt_ret_code_t { SETTINGS_MGMT_ERR_OK = 0 , SETTINGS_MGMT_ERR_UNKNOWN , SETTINGS_MGMT_ERR_KEY_TOO_LONG , SETTINGS_MGMT_ERR_KEY_NOT_FOUND , SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED , SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND , SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ }
```

相关声明：[settings_mgmt_ret_code_t](#gafb39b95aec3183531602aa6964ceb1cc)、[SETTINGS_MGMT_ERR_OK](#ggafb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f)、[SETTINGS_MGMT_ERR_UNKNOWN](#ggafb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d)、[SETTINGS_MGMT_ERR_KEY_TOO_LONG](#ggafb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28)、[SETTINGS_MGMT_ERR_KEY_NOT_FOUND](#ggafb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f)、[SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED](#ggafb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2)、[SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND](#ggafb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55)、[SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED](#ggafb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b)、[SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED](#ggafb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d)、[SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED](#ggafb39b95aec3183531602aa6964ceb1ccad057ffe9283331020142bbeac6d8c925)、[SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ](#ggafb39b95aec3183531602aa6964ceb1cca36e5122bfe84f95b67bcf416120c288b)。

设置管理组（settings management group）的命令结果码。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 12.4\_设置管理组命令标识符（Command IDs for Settings Management group）

<a id="r_gaff2f915e03116c35567dfa3b61353e34"></a>

```c
#define SETTINGS_MGMT_ID_READ_WRITE 0
```

相关声明：[SETTINGS_MGMT_ID_READ_WRITE](#gaff2f915e03116c35567dfa3b61353e34)。

读取或写入设置项（setting）。

<a id="r_ga1c3751a9b7a6b267f78fcc8b2b8954fb"></a>

```c
#define SETTINGS_MGMT_ID_DELETE 1
```

相关声明：[SETTINGS_MGMT_ID_DELETE](#ga1c3751a9b7a6b267f78fcc8b2b8954fb)。

删除设置项。

<a id="r_ga85687e53d63edfe4d3bd55988d863e9d"></a>

```c
#define SETTINGS_MGMT_ID_COMMIT 2
```

相关声明：[SETTINGS_MGMT_ID_COMMIT](#ga85687e53d63edfe4d3bd55988d863e9d)。

提交设置（commit settings）。

<a id="r_ga3add3a2acfcd23eb7af5df404378050c"></a>

```c
#define SETTINGS_MGMT_ID_LOAD_SAVE 3
```

相关声明：[SETTINGS_MGMT_ID_LOAD_SAVE](#ga3add3a2acfcd23eb7af5df404378050c)。

加载或保存设置。

## 12.5\_详细说明（Detailed Documentation）

<a id="ga85687e53d63edfe4d3bd55988d863e9d"></a>

### `SETTINGS_MGMT_ID_COMMIT`

```c
#define SETTINGS_MGMT_ID_COMMIT 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt.h>
```

提交设置（commit settings）。

<a id="ga1c3751a9b7a6b267f78fcc8b2b8954fb"></a>

### `SETTINGS_MGMT_ID_DELETE`

```c
#define SETTINGS_MGMT_ID_DELETE 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt.h>
```

删除设置项。

<a id="ga3add3a2acfcd23eb7af5df404378050c"></a>

### `SETTINGS_MGMT_ID_LOAD_SAVE`

```c
#define SETTINGS_MGMT_ID_LOAD_SAVE 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt.h>
```

加载或保存设置。

<a id="gaff2f915e03116c35567dfa3b61353e34"></a>

### `SETTINGS_MGMT_ID_READ_WRITE`

```c
#define SETTINGS_MGMT_ID_READ_WRITE 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt.h>
```

读取或写入设置项（setting）。

<a id="gafb39b95aec3183531602aa6964ceb1cc"></a>

### `settings_mgmt_ret_code_t`

```c
enum settings_mgmt_ret_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt.h>
```

设置管理组（settings management group）的命令结果码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SETTINGS_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `SETTINGS_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `SETTINGS_MGMT_ERR_KEY_TOO_LONG` | 提供的键名（key name）过长，无法使用。 |
| `SETTINGS_MGMT_ERR_KEY_NOT_FOUND` | 提供的键名不存在。 |
| `SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED` | 提供的键名不支持读取。 |
| `SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND` | 提供的根键名（root key name）不存在。 |
| `SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED` | 提供的键名不支持写入。 |
| `SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED` | 提供的键名不支持删除。 |
| `SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED` | 提供的键名不支持保存。 |
| `SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ` | 原文称：在值的长度超过能够安全读取的最大值大小（`CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION_VALUE_SIZE`）之前，无法保存所提供的键。译注：原文此处使用 `before`，该条件措辞按原样保留；实际限制请结合本页原始错误码及实现阅读。 |


## 12.6\_原页交叉引用（Cross References）

- [设置管理回调（Settings Management Callbacks）](P011_设置管理回调（Settings Management Callbacks）.md)
- [settings_mgmt.h](../api_file_interface_reference/P052_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1ccad057ffe9283331020142bbeac6d8c925"></a>
<a id="ggafb39b95aec3183531602aa6964ceb1cca36e5122bfe84f95b67bcf416120c288b"></a>

---

[上一章](P011_设置管理回调（Settings Management Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P013_MMC56X3 API主题.md)
