---
id: learning.zephyr-docs.api-file-interface-reference.page-52
title: zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_settings\_mgmt\_\_settings\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr设置管理组（Settings Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr设置管理组（Settings Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 52.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 设置管理组命令标识符（Command IDs for Settings Management group）

<a id="r_gaff2f915e03116c35567dfa3b61353e34"></a>

```c
#define SETTINGS_MGMT_ID_READ_WRITE 0
```

相关声明：[SETTINGS_MGMT_ID_READ_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#gaff2f915e03116c35567dfa3b61353e34)。

读取或写入设置项（setting）。

<a id="r_ga1c3751a9b7a6b267f78fcc8b2b8954fb"></a>

```c
#define SETTINGS_MGMT_ID_DELETE 1
```

相关声明：[SETTINGS_MGMT_ID_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga1c3751a9b7a6b267f78fcc8b2b8954fb)。

删除设置项。

<a id="r_ga85687e53d63edfe4d3bd55988d863e9d"></a>

```c
#define SETTINGS_MGMT_ID_COMMIT 2
```

相关声明：[SETTINGS_MGMT_ID_COMMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga85687e53d63edfe4d3bd55988d863e9d)。

提交设置（commit settings）。

<a id="r_ga3add3a2acfcd23eb7af5df404378050c"></a>

```c
#define SETTINGS_MGMT_ID_LOAD_SAVE 3
```

相关声明：[SETTINGS_MGMT_ID_LOAD_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga3add3a2acfcd23eb7af5df404378050c)。

加载或保存设置。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 52.2\_枚举（Enumerations）

<a id="r_gafb39b95aec3183531602aa6964ceb1cc"></a>

```c
enum settings_mgmt_ret_code_t { SETTINGS_MGMT_ERR_OK = 0 , SETTINGS_MGMT_ERR_UNKNOWN , SETTINGS_MGMT_ERR_KEY_TOO_LONG , SETTINGS_MGMT_ERR_KEY_NOT_FOUND , SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED , SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND , SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED , SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ }
```

相关声明：[settings_mgmt_ret_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#gafb39b95aec3183531602aa6964ceb1cc)、[SETTINGS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f)、[SETTINGS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d)、[SETTINGS_MGMT_ERR_KEY_TOO_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28)、[SETTINGS_MGMT_ERR_KEY_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f)、[SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2)、[SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55)、[SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b)、[SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d)、[SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccad057ffe9283331020142bbeac6d8c925)、[SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca36e5122bfe84f95b67bcf416120c288b)。

设置管理组（settings management group）的命令结果码。


## 52.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P771_settings_mgmt.h_源码浏览.md)
- [SETTINGS_MGMT_ID_READ_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#gaff2f915e03116c35567dfa3b61353e34)
- [SETTINGS_MGMT_ID_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga1c3751a9b7a6b267f78fcc8b2b8954fb)
- [SETTINGS_MGMT_ID_COMMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga85687e53d63edfe4d3bd55988d863e9d)
- [SETTINGS_MGMT_ID_LOAD_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ga3add3a2acfcd23eb7af5df404378050c)
- [settings_mgmt_ret_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#gafb39b95aec3183531602aa6964ceb1cc)
- [SETTINGS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f)
- [SETTINGS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d)
- [SETTINGS_MGMT_ERR_KEY_TOO_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28)
- [SETTINGS_MGMT_ERR_KEY_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f)
- [SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2)
- [SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55)
- [SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b)
- [SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d)
- [SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1ccad057ffe9283331020142bbeac6d8c925)
- [SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__settings__mgmt.html#ggafb39b95aec3183531602aa6964ceb1cca36e5122bfe84f95b67bcf416120c288b)

<a id="header-details"></a>

---

[上一章](P051_zephyr__sensing__sensing_sensor.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__net__socketcan_utils.h_文件参考.md)
