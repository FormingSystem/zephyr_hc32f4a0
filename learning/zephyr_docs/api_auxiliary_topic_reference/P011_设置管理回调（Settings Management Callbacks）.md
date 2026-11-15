---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-11
title: 设置管理回调（Settings Management Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_设置管理回调（Settings Management Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 设置管理回调 API

<a id="details"></a>

MCUmgr 设置管理回调 API

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_settings_5Fmgmt_5Faccess"></a>

```c
struct settings_mgmt_access
```

相关声明：[settings_mgmt_access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md)。

MGMT_EVT_OP_SETTINGS_MGMT_ACCESS通知回调中提供的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.2\_枚举（Enumerations）

<a id="r_ga1711bc9f45a8114a6b0c89db4a40e3de"></a>

```c
enum settings_mgmt_group_events { MGMT_EVT_OP_SETTINGS_MGMT_ACCESS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SETTINGS, 0) , MGMT_EVT_OP_SETTINGS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SETTINGS) }
```

相关声明：[settings_mgmt_group_events](#ga1711bc9f45a8114a6b0c89db4a40e3de)、[MGMT_EVT_OP_SETTINGS_MGMT_ACCESS](#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)、[MGMT_EVT_OP_SETTINGS_MGMT_ALL](#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2)。

设置管理组（Settings Management Group）的管理事件操作码（MGMT Event Opcodes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.3\_设置访问类型（Settings Access Types）

<a id="r_ga40c179f978718409c7db43448efc8f47"></a>

```c
enum settings_mgmt_access_types { SETTINGS_ACCESS_READ , SETTINGS_ACCESS_WRITE , SETTINGS_ACCESS_DELETE , SETTINGS_ACCESS_COMMIT , SETTINGS_ACCESS_LOAD , SETTINGS_ACCESS_SAVE }
```

相关声明：[settings_mgmt_access_types](#ga40c179f978718409c7db43448efc8f47)、[SETTINGS_ACCESS_READ](#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)、[SETTINGS_ACCESS_WRITE](#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)、[SETTINGS_ACCESS_DELETE](#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)、[SETTINGS_ACCESS_COMMIT](#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de)、[SETTINGS_ACCESS_LOAD](#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce)、[SETTINGS_ACCESS_SAVE](#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)。

## 11.4\_详细说明（Detailed Documentation）

<a id="ga40c179f978718409c7db43448efc8f47"></a>

### `settings_mgmt_access_types`

```c
enum settings_mgmt_access_types
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SETTINGS_ACCESS_READ` | 正在读取设置项（setting）。 |
| `SETTINGS_ACCESS_WRITE` | 正在写入设置项。 |
| `SETTINGS_ACCESS_DELETE` | 正在删除设置项。 |
| `SETTINGS_ACCESS_COMMIT` | 正在提交设置（commit）。 |
| `SETTINGS_ACCESS_LOAD` | 正在加载设置（load）。 |
| `SETTINGS_ACCESS_SAVE` | 正在保存设置（save）。 |

<a id="ga1711bc9f45a8114a6b0c89db4a40e3de"></a>

### `settings_mgmt_group_events`

```c
enum settings_mgmt_group_events
```

```c
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h>
```

设置管理组（Settings Management Group）的管理事件操作码（MGMT Event Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_SETTINGS_MGMT_ACCESS` | 读取／写入／删除设置项时触发的回调。 |
| `MGMT_EVT_OP_SETTINGS_MGMT_ALL` | 用于启用全部 `settings_mgmt_group` 事件。 |


## 11.5\_原页交叉引用（Cross References）

- [settings_mgmt_access](../system_service_model_reference/P077_settings_mgmt_access_结构体.md)
- [zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h](../api_file_supplement_reference/P111_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt_callbacks.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00"></a>
<a id="gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590"></a>
<a id="gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd"></a>
<a id="gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de"></a>
<a id="gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce"></a>
<a id="gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543"></a>
<a id="gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0"></a>
<a id="gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2"></a>

---

[上一章](P010_向量限幅（Vector Clipping）.md) · [返回大纲](大纲.md) · [下一章](P012_设置管理（Settings Management）.md)
