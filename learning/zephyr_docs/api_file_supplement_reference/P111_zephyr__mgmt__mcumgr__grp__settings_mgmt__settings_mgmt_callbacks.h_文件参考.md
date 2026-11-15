---
id: learning.zephyr-docs.api-file-supplement-reference.page-111
title: zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt_callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_settings\_mgmt\_\_settings\_mgmt\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 111.1\_数据结构（Data Structures）

<a id="r_settings_5Fmgmt_5Faccess"></a>

```c
struct settings_mgmt_access
```

相关声明：[settings_mgmt_access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md)。

MGMT_EVT_OP_SETTINGS_MGMT_ACCESS通知回调中提供的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 111.2\_枚举（Enumerations）

<a id="r_ga1711bc9f45a8114a6b0c89db4a40e3de"></a>

```c
enum settings_mgmt_group_events { MGMT_EVT_OP_SETTINGS_MGMT_ACCESS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SETTINGS, 0) , MGMT_EVT_OP_SETTINGS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SETTINGS) }
```

相关声明：[settings_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga1711bc9f45a8114a6b0c89db4a40e3de)、[MGMT_EVT_OP_SETTINGS_MGMT_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)、[MGMT_EVT_OP_SETTINGS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2)。

设置管理组（Settings Management Group）的管理事件操作码（MGMT Event Opcodes）。

<a id="enum-members-0"></a>

### 设置访问类型（Settings Access Types）

<a id="r_ga40c179f978718409c7db43448efc8f47"></a>

```c
enum settings_mgmt_access_types { SETTINGS_ACCESS_READ , SETTINGS_ACCESS_WRITE , SETTINGS_ACCESS_DELETE , SETTINGS_ACCESS_COMMIT , SETTINGS_ACCESS_LOAD , SETTINGS_ACCESS_SAVE }
```

相关声明：[settings_mgmt_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga40c179f978718409c7db43448efc8f47)、[SETTINGS_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)、[SETTINGS_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)、[SETTINGS_ACCESS_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)、[SETTINGS_ACCESS_COMMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de)、[SETTINGS_ACCESS_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce)、[SETTINGS_ACCESS_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)。


## 111.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P772_settings_mgmt_callbacks.h_源码浏览.md)
- [settings_mgmt_access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md)
- [MGMT_EVT_OP_SETTINGS_MGMT_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)
- [settings_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga1711bc9f45a8114a6b0c89db4a40e3de)
- [MGMT_EVT_OP_SETTINGS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2)
- [settings_mgmt_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#ga40c179f978718409c7db43448efc8f47)
- [SETTINGS_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)
- [SETTINGS_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)
- [SETTINGS_ACCESS_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)
- [SETTINGS_ACCESS_COMMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de)
- [SETTINGS_ACCESS_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce)
- [SETTINGS_ACCESS_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)

---

[上一章](P110_zephyr__drivers__sensor__tle9104.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P112_zephyr__drivers__sip_svc__sip_svc_agilex_mailbox.h_文件参考.md)
