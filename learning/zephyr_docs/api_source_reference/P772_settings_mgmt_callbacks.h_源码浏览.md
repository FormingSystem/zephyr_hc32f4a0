---
id: learning.zephyr-docs.api-source-reference.page-772
title: settings_mgmt_callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第772章\_settings\_mgmt\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html)。

## 772.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00021"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_ga1711bc9f45a8114a6b0c89db4a40e3de"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_ga40c179f978718409c7db43448efc8f47"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce"></a>
<a id="agroup__mcumgr__callback__api__settings__mgmt_html_gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsettings__mgmt__access_html"></a>
<a id="astructsettings__mgmt__access_html_a9b798a118844083d77af6db53df5eb37"></a>
<a id="astructsettings__mgmt__access_html_ab13bdcd8763dca5a99d3d52270f9b4d2"></a>
<a id="astructsettings__mgmt__access_html_ae0f02e70ee2da823801d4d475f4a2e76"></a>
<a id="astructsettings__mgmt__access_html_aeb23615be870929a987c6cfbd3f445de"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_CALLBACKS_H_

#ifdef __cplusplus
extern "C" {
#endif


enum settings_mgmt_group_events {
        MGMT_EVT_OP_SETTINGS_MGMT_ACCESS        = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SETTINGS, 0),

        MGMT_EVT_OP_SETTINGS_MGMT_ALL           = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SETTINGS),
};

enum settings_mgmt_access_types {
        SETTINGS_ACCESS_READ,
        SETTINGS_ACCESS_WRITE,
        SETTINGS_ACCESS_DELETE,
        SETTINGS_ACCESS_COMMIT,
        SETTINGS_ACCESS_LOAD,
        SETTINGS_ACCESS_SAVE,
};


struct settings_mgmt_access {
        enum settings_mgmt_access_types access;

#ifdef CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP
        const char *name;
#else
        char *name;
#endif

        const uint8_t *val;

        const size_t *val_length;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_CALLBACKS_H_ */
```

## 772.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SETTINGS_MGMT_SETTINGS_MGMT_CALLBACKS_H_`。

## 772.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html)
- [settings_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga1711bc9f45a8114a6b0c89db4a40e3de)
- [MGMT_EVT_OP_SETTINGS_MGMT_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)
- [MGMT_EVT_GRP_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)
- [MGMT_EVT_OP_SETTINGS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2)
- [settings_mgmt_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga40c179f978718409c7db43448efc8f47)
- [SETTINGS_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)
- [SETTINGS_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)
- [SETTINGS_ACCESS_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)
- [SETTINGS_ACCESS_COMMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de)
- [SETTINGS_ACCESS_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce)
- [SETTINGS_ACCESS_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)
- [settings_mgmt_access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md)
- [access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#a9b798a118844083d77af6db53df5eb37)
- [name](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#ae0f02e70ee2da823801d4d475f4a2e76)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [val](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#aeb23615be870929a987c6cfbd3f445de)
- [val_length](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#ab13bdcd8763dca5a99d3d52270f9b4d2)
- [settings_mgmt_access::access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#a9b798a118844083d77af6db53df5eb37)
- [settings_mgmt_access::val_length](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#ab13bdcd8763dca5a99d3d52270f9b4d2)
- [settings_mgmt_access::name](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#ae0f02e70ee2da823801d4d475f4a2e76)
- [settings_mgmt_access::val](../system_service_model_reference/P077_settings_mgmt_access_结构体.md#aeb23615be870929a987c6cfbd3f445de)

---

[上一章](P771_settings_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P773_sf32lb-clocks-common.h_源码浏览.md)
