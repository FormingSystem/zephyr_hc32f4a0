---
id: learning.zephyr-docs.api-extension-topic-reference.page-14
title: 枚举管理回调（Enumeration Management Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_枚举管理回调（Enumeration Management Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 枚举管理回调 API

<a id="details"></a>

MCUmgr 枚举管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_enum_5Fmgmt_5Fcallbacks_2Eh"></a>

```c
file enum_mgmt_callbacks.h
```

相关声明：[enum_mgmt_callbacks.h](../api_file_supplement_reference/P025_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt_callbacks.h_文件参考.md)。

MCUmgr枚举管理回调（Enumeration Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_enum_5Fmgmt_5Fdetail_5Foutput"></a>

```c
struct enum_mgmt_detail_output
```

相关声明：[enum_mgmt_detail_output](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md)。

MGMT_EVT_OP_ENUM_MGMT_DETAILS通知回调中提供的结构。使用详情命令（Detail Command）时，每个命令组调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga7ddc4c031948a2fee56fcbdb7d675a1d"></a>

```c
enum enum_mgmt_group_events { MGMT_EVT_OP_ENUM_MGMT_DETAILS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_ENUM, 0) , MGMT_EVT_OP_ENUM_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ENUM) }
```

相关声明：[enum_mgmt_group_events](#ga7ddc4c031948a2fee56fcbdb7d675a1d)、[MGMT_EVT_OP_ENUM_MGMT_DETAILS](#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)、[MGMT_EVT_OP_ENUM_MGMT_ALL](#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b)。

枚举管理组（Enumeration Management Group）的管理事件操作码（MGMT Event Opcodes）。

## 14.4\_详细说明（Detailed Documentation）

<a id="ga7ddc4c031948a2fee56fcbdb7d675a1d"></a>

### `enum_mgmt_group_events`

```c
enum enum_mgmt_group_events
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h>
```

枚举管理组（Enumeration Management Group）的管理事件操作码（MGMT Event Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_ENUM_MGMT_DETAILS` | 获取受支持命令组（Supported Command Groups）的详细信息时调用的回调（Callback）。 |
| `MGMT_EVT_OP_ENUM_MGMT_ALL` | 用于启用所有 `enum_mgmt_group` 事件（Events）。 |


## 14.5\_原页交叉引用（Cross References）

- [enum_mgmt_callbacks.h](../api_file_supplement_reference/P025_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt_callbacks.h_文件参考.md)
- [enum_mgmt_detail_output](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf"></a>
<a id="gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b"></a>

---

[上一章](P013_F75303 API主题.md) · [返回大纲](大纲.md) · [下一章](P015_处理程序（Handlers）.md)
