---
id: learning.zephyr-docs.api-file-supplement-reference.page-25
title: zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt_callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_enum\_mgmt\_\_enum\_mgmt\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr枚举管理回调（Enumeration Management Callback）定义的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr枚举管理回调（Enumeration Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_enum_5Fmgmt_5Fdetail_5Foutput"></a>

```c
struct enum_mgmt_detail_output
```

相关声明：[enum_mgmt_detail_output](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md)。

MGMT_EVT_OP_ENUM_MGMT_DETAILS通知回调中提供的结构。使用详情命令（Detail Command）时，每个命令组调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.2\_枚举（Enumerations）

<a id="r_ga7ddc4c031948a2fee56fcbdb7d675a1d"></a>

```c
enum enum_mgmt_group_events { MGMT_EVT_OP_ENUM_MGMT_DETAILS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_ENUM, 0) , MGMT_EVT_OP_ENUM_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ENUM) }
```

相关声明：[enum_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#ga7ddc4c031948a2fee56fcbdb7d675a1d)、[MGMT_EVT_OP_ENUM_MGMT_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)、[MGMT_EVT_OP_ENUM_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b)。

枚举管理组（Enumeration Management Group）的管理事件操作码（MGMT Event Opcodes）。


## 25.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P231_enum_mgmt_callbacks.h_源码浏览.md)
- [enum_mgmt_detail_output](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md)
- [MGMT_EVT_OP_ENUM_MGMT_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)
- [enum_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#ga7ddc4c031948a2fee56fcbdb7d675a1d)
- [MGMT_EVT_OP_ENUM_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b)

<a id="header-details"></a>

---

[上一章](P024_zephyr__net__dummy.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__sensor__eqdc_mcux.h_文件参考.md)
