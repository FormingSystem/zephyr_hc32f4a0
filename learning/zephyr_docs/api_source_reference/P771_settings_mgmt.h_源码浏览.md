---
id: learning.zephyr-docs.api-source-reference.page-771
title: settings_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第771章\_settings\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h.html)。

## 771.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="agroup__mcumgr__settings__mgmt_html_gafb39b95aec3183531602aa6964ceb1cc"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca36e5122bfe84f95b67bcf416120c288b"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f"></a>
<a id="agroup__mcumgr__settings__mgmt_html_ggafb39b95aec3183531602aa6964ceb1ccad057ffe9283331020142bbeac6d8c925"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_H_


#ifdef __cplusplus
extern "C" {
#endif

#define SETTINGS_MGMT_ID_READ_WRITE 0
#define SETTINGS_MGMT_ID_DELETE     1
#define SETTINGS_MGMT_ID_COMMIT     2
#define SETTINGS_MGMT_ID_LOAD_SAVE  3

enum settings_mgmt_ret_code_t {
        SETTINGS_MGMT_ERR_OK = 0,

        SETTINGS_MGMT_ERR_UNKNOWN,

        SETTINGS_MGMT_ERR_KEY_TOO_LONG,

        SETTINGS_MGMT_ERR_KEY_NOT_FOUND,

        SETTINGS_MGMT_ERR_READ_NOT_SUPPORTED,

        SETTINGS_MGMT_ERR_ROOT_KEY_NOT_FOUND,

        SETTINGS_MGMT_ERR_WRITE_NOT_SUPPORTED,

        SETTINGS_MGMT_ERR_DELETE_NOT_SUPPORTED,

        SETTINGS_MGMT_ERR_SAVE_NOT_SUPPORTED,

        SETTINGS_MGMT_ERR_SAVE_FAILED_VALUE_TOO_LONG_TO_READ,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_H_ */
```

## 771.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_H_`。

## 771.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt_8h.html)
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

---

[上一章](P770_serial.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P772_settings_mgmt_callbacks.h_源码浏览.md)
