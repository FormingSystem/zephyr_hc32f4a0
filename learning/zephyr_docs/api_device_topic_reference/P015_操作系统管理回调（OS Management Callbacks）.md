---
id: learning.zephyr-docs.api-device-topic-reference.page-15
title: 操作系统管理回调（OS Management Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_操作系统管理回调（OS Management Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 操作系统管理回调 API

<a id="details"></a>

MCUmgr 操作系统管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_os_5Fmgmt_5Fcallbacks_2Eh"></a>

```c
file os_mgmt_callbacks.h
```

相关声明：[os_mgmt_callbacks.h](../api_file_supplement_reference/P082_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_callbacks.h_文件参考.md)。

MCUmgr操作系统管理回调（OS Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.2\_数据结构（Data Structures）

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

## 15.3\_枚举（Enumerations）

<a id="r_ga261346c700a2522542d8282ca76f88a5"></a>

```c
enum os_mgmt_group_events { MGMT_EVT_OP_OS_MGMT_RESET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 0) , MGMT_EVT_OP_OS_MGMT_INFO_CHECK = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 1) , MGMT_EVT_OP_OS_MGMT_INFO_APPEND = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 2) , MGMT_EVT_OP_OS_MGMT_DATETIME_GET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 3) , MGMT_EVT_OP_OS_MGMT_DATETIME_SET = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 4) , MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_OS, 5) , MGMT_EVT_OP_OS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_OS) }
```

相关声明：[os_mgmt_group_events](#ga261346c700a2522542d8282ca76f88a5)、[MGMT_EVT_OP_OS_MGMT_RESET](#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)、[MGMT_EVT_OP_OS_MGMT_INFO_CHECK](#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)、[MGMT_EVT_OP_OS_MGMT_INFO_APPEND](#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f)、[MGMT_EVT_OP_OS_MGMT_DATETIME_GET](#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d)、[MGMT_EVT_OP_OS_MGMT_DATETIME_SET](#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b)、[MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO](#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)、[MGMT_EVT_OP_OS_MGMT_ALL](#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a)。

操作系统管理组（Operating System Management Group）的管理事件操作码（MGMT Event Opcodes）。

## 15.4\_详细说明（Detailed Documentation）

<a id="ga261346c700a2522542d8282ca76f88a5"></a>

### `os_mgmt_group_events`

```c
enum os_mgmt_group_events
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h>
```

操作系统管理组（Operating System Management Group）的管理事件操作码（MGMT Event Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_OS_MGMT_RESET` | 收到复位命令（reset command）时触发的回调，数据为 `os_mgmt_reset_data`。 |
| `MGMT_EVT_OP_OS_MGMT_INFO_CHECK` | 处理信息命令（info command）时触发的回调，数据为 `os_mgmt_info_check`。 |
| `MGMT_EVT_OP_OS_MGMT_INFO_APPEND` | 信息命令需要输出数据时触发的回调，数据为 `os_mgmt_info_append`。 |
| `MGMT_EVT_OP_OS_MGMT_DATETIME_GET` | 收到日期时间获取命令（datetime get command）时触发的回调。 |
| `MGMT_EVT_OP_OS_MGMT_DATETIME_SET` | 收到日期时间设置命令（datetime set command）时触发的回调，数据为 `rtc_time`。 |
| `MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO` | 收到引导加载程序信息命令（bootloader info command）时触发的回调，数据为 `os_mgmt_bootloader_info_data()`。 |
| `MGMT_EVT_OP_OS_MGMT_ALL` | 用于启用全部 `os_mgmt_group` 事件。 |


## 15.5\_原页交叉引用（Cross References）

- [os_mgmt_callbacks.h](../api_file_supplement_reference/P082_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_callbacks.h_文件参考.md)
- [os_mgmt_reset_data](../system_service_model_reference/P074_os_mgmt_reset_data_结构体.md)
- [os_mgmt_bootloader_info_data](../system_service_model_reference/P070_os_mgmt_bootloader_info_data_结构体.md)
- [os_mgmt_info_check](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md)
- [os_mgmt_info_append](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md)
- [rtc_time](../timer_reference/P011_实时时钟时间结构.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52"></a>
<a id="gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5"></a>
<a id="gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f"></a>
<a id="gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d"></a>
<a id="gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b"></a>
<a id="gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf"></a>
<a id="gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a"></a>

---

[上一章](P014_文件系统管理回调（File System Management Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P016_MFD MAX22017 接口.md)
