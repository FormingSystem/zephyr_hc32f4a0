---
id: learning.zephyr-docs.api-file-supplement-reference.page-82
title: zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_os\_mgmt\_\_os\_mgmt\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr操作系统管理回调（OS Management Callback）定义的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr操作系统管理回调（OS Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 82.1\_数据结构（Data Structures）

<a id="r_os_5Fmgmt_5Freset_5Fdata"></a>

```c
struct os_mgmt_reset_data
```

相关声明：[os_mgmt_reset_data](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md)。

MGMT_EVT_OP_OS_MGMT_RESET通知回调中提供的结构。该回调用于将待处理的设备重启请求（Device Reboot Request）通知应用，并授权或拒绝该请求。

<a id="r_os_5Fmgmt_5Fbootloader_5Finfo_5Fdata"></a>

```c
struct os_mgmt_bootloader_info_data
```

相关声明：[os_mgmt_bootloader_info_data](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md)。

MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO通知回调中提供的结构。该回调用于向引导加载程序信息（Bootloader Info）响应添加新字段。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 82.2\_枚举（Enumerations）

<a id="r_ga261346c700a2522542d8282ca76f88a5"></a>

```c
enum os_mgmt_group_events { MGMT_EVT_OP_OS_MGMT_RESET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 0) , MGMT_EVT_OP_OS_MGMT_INFO_CHECK = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 1) , MGMT_EVT_OP_OS_MGMT_INFO_APPEND = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 2) , MGMT_EVT_OP_OS_MGMT_DATETIME_GET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 3) , MGMT_EVT_OP_OS_MGMT_DATETIME_SET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 4) , MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 5) , MGMT_EVT_OP_OS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_OS) }
```

相关声明：[os_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#ga261346c700a2522542d8282ca76f88a5)、[MGMT_EVT_OP_OS_MGMT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)、[MGMT_EVT_OP_OS_MGMT_INFO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)、[MGMT_EVT_OP_OS_MGMT_INFO_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f)、[MGMT_EVT_OP_OS_MGMT_DATETIME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d)、[MGMT_EVT_OP_OS_MGMT_DATETIME_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b)、[MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)、[MGMT_EVT_OP_OS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a)。

操作系统管理组（Operating System Management Group）的管理事件操作码（MGMT Event Opcodes）。


## 82.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P637_os_mgmt_callbacks.h_源码浏览.md)
- [os_mgmt_reset_data](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md)
- [MGMT_EVT_OP_OS_MGMT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)
- [os_mgmt_bootloader_info_data](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md)
- [MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)
- [os_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#ga261346c700a2522542d8282ca76f88a5)
- [MGMT_EVT_OP_OS_MGMT_INFO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)
- [MGMT_EVT_OP_OS_MGMT_INFO_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f)
- [MGMT_EVT_OP_OS_MGMT_DATETIME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d)
- [MGMT_EVT_OP_OS_MGMT_DATETIME_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b)
- [MGMT_EVT_OP_OS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a)

<a id="header-details"></a>

---

[上一章](P081_zephyr__bluetooth__mesh__op_agg_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P083_zephyr__dt-bindings__flash_controller__ospi.h_文件参考.md)
