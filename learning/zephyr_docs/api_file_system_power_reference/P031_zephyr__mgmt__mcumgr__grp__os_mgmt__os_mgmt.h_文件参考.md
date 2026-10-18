---
id: learning.zephyr-docs.api-file-system-power-reference.page-31
title: zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_os\_mgmt\_\_os\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr操作系统管理组（OS Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr操作系统管理组（OS Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 31.1\_数据结构（Data Structures）

<a id="r_os_5Fmgmt_5Finfo_5Fcheck"></a>

```c
struct os_mgmt_info_check
```

相关声明：[os_mgmt_info_check](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md)。

MGMT_EVT_OP_OS_MGMT_INFO_CHECK通知回调中提供的结构。

<a id="r_os_5Fmgmt_5Finfo_5Fappend"></a>

```c
struct os_mgmt_info_append
```

相关声明：[os_mgmt_info_append](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md)。

MGMT_EVT_OP_OS_MGMT_INFO_APPEND通知回调中提供的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 操作系统管理组命令 ID（Command IDs for OS Management Group）

<a id="r_ga24751ec5a8ba224238f484e2048f152a"></a>

```c
#define OS_MGMT_ID_ECHO 0
```

相关声明：[OS_MGMT_ID_ECHO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga24751ec5a8ba224238f484e2048f152a)。

回显（Echo）。

<a id="r_ga0093a8df477e7114ffa195a022851cbe"></a>

```c
#define OS_MGMT_ID_CONS_ECHO_CTRL 1
```

相关声明：[OS_MGMT_ID_CONS_ECHO_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga0093a8df477e7114ffa195a022851cbe)。

控制台／终端回显控制（Console/Terminal Echo Control）。

<a id="r_ga067886d5d5d1d8979f93bab61fc2a670"></a>

```c
#define OS_MGMT_ID_TASKSTAT 2
```

相关声明：[OS_MGMT_ID_TASKSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga067886d5d5d1d8979f93bab61fc2a670)。

任务统计（Task Statistics）。

<a id="r_gaa2918e287d063fb2a82bd87d5c29aba4"></a>

```c
#define OS_MGMT_ID_MPSTAT 3
```

相关声明：[OS_MGMT_ID_MPSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gaa2918e287d063fb2a82bd87d5c29aba4)。

内存池统计（Memory Pool Statistics）。

<a id="r_gaf4370119858111637ee80af735b0e50c"></a>

```c
#define OS_MGMT_ID_DATETIME_STR 4
```

相关声明：[OS_MGMT_ID_DATETIME_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gaf4370119858111637ee80af735b0e50c)。

日期时间字符串（Date-time String）。

<a id="r_ga4447fa2fa0c5f37713f7ef555174e814"></a>

```c
#define OS_MGMT_ID_RESET 5
```

相关声明：[OS_MGMT_ID_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga4447fa2fa0c5f37713f7ef555174e814)。

系统复位（System Reset）。

<a id="r_ga6eb9918c2e6d1564fc362fe3dcdc63d5"></a>

```c
#define OS_MGMT_ID_MCUMGR_PARAMS 6
```

相关声明：[OS_MGMT_ID_MCUMGR_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga6eb9918c2e6d1564fc362fe3dcdc63d5)。

MCUMgr 参数（Parameters）。

<a id="r_ga0103b1f0d37106c5166b1793c7743513"></a>

```c
#define OS_MGMT_ID_INFO 7
```

相关声明：[OS_MGMT_ID_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga0103b1f0d37106c5166b1793c7743513)。

操作系统／应用信息（OS/Application Information）。

<a id="r_ga142393f94135f1dd91b8cf098e01aa6b"></a>

```c
#define OS_MGMT_ID_BOOTLOADER_INFO 8
```

相关声明：[OS_MGMT_ID_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga142393f94135f1dd91b8cf098e01aa6b)。

引导加载程序信息（Bootloader Information）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.3\_枚举（Enumerations）

<a id="r_ga14dc9256e6585450ea34b13666aa8765"></a>

```c
enum os_mgmt_err_code_t { OS_MGMT_ERR_OK = 0 , OS_MGMT_ERR_UNKNOWN , OS_MGMT_ERR_INVALID_FORMAT , OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER , OS_MGMT_ERR_RTC_NOT_SET , OS_MGMT_ERR_RTC_COMMAND_FAILED , OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID , OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED }
```

相关声明：[os_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga14dc9256e6585450ea34b13666aa8765)、[OS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4)、[OS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752)、[OS_MGMT_ERR_INVALID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd)、[OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)、[OS_MGMT_ERR_RTC_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517)、[OS_MGMT_ERR_RTC_COMMAND_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)、[OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf)、[OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f)。

操作系统管理组（OS Management Group）的命令结果码（Command Result Codes）。

<a id="r_ga54512f3d774835d1d277872835a3b26f"></a>

```c
enum os_mgmt_info_formats { OS_MGMT_INFO_FORMAT_KERNEL_NAME = BIT(0) , OS_MGMT_INFO_FORMAT_NODE_NAME = BIT(1) , OS_MGMT_INFO_FORMAT_KERNEL_RELEASE = BIT(2) , OS_MGMT_INFO_FORMAT_KERNEL_VERSION = BIT(3) , OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME = BIT(4) , OS_MGMT_INFO_FORMAT_MACHINE = BIT(5) , OS_MGMT_INFO_FORMAT_PROCESSOR = BIT(6) , OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM = BIT(7) , OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM = BIT(8) , OS_MGMT_INFO_FORMAT_USER_CUSTOM_START = BIT(9) }
```

相关声明：[os_mgmt_info_formats](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga54512f3d774835d1d277872835a3b26f)、[OS_MGMT_INFO_FORMAT_KERNEL_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0)、[OS_MGMT_INFO_FORMAT_NODE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3)、[OS_MGMT_INFO_FORMAT_KERNEL_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd)、[OS_MGMT_INFO_FORMAT_KERNEL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328)、[OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d)、[OS_MGMT_INFO_FORMAT_MACHINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848)、[OS_MGMT_INFO_FORMAT_PROCESSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082)、[OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5)、[OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76)、[OS_MGMT_INFO_FORMAT_USER_CUSTOM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2)。

操作系统／应用信息格式（OS/Application Information Formats）。


## 31.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P636_os_mgmt.h_源码浏览.md)
- [os_mgmt_info_check](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md)
- [MGMT_EVT_OP_OS_MGMT_INFO_CHECK](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)
- [os_mgmt_info_append](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md)
- [OS_MGMT_ID_ECHO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga24751ec5a8ba224238f484e2048f152a)
- [OS_MGMT_ID_CONS_ECHO_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga0093a8df477e7114ffa195a022851cbe)
- [OS_MGMT_ID_TASKSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga067886d5d5d1d8979f93bab61fc2a670)
- [OS_MGMT_ID_MPSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gaa2918e287d063fb2a82bd87d5c29aba4)
- [OS_MGMT_ID_DATETIME_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gaf4370119858111637ee80af735b0e50c)
- [OS_MGMT_ID_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga4447fa2fa0c5f37713f7ef555174e814)
- [OS_MGMT_ID_MCUMGR_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga6eb9918c2e6d1564fc362fe3dcdc63d5)
- [OS_MGMT_ID_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga0103b1f0d37106c5166b1793c7743513)
- [OS_MGMT_ID_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga142393f94135f1dd91b8cf098e01aa6b)
- [os_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga14dc9256e6585450ea34b13666aa8765)
- [OS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4)
- [OS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752)
- [OS_MGMT_ERR_INVALID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd)
- [OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)
- [OS_MGMT_ERR_RTC_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517)
- [OS_MGMT_ERR_RTC_COMMAND_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)
- [OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf)
- [OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f)
- [os_mgmt_info_formats](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#ga54512f3d774835d1d277872835a3b26f)
- [OS_MGMT_INFO_FORMAT_KERNEL_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0)
- [OS_MGMT_INFO_FORMAT_NODE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3)
- [OS_MGMT_INFO_FORMAT_KERNEL_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd)
- [OS_MGMT_INFO_FORMAT_KERNEL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328)
- [OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d)
- [OS_MGMT_INFO_FORMAT_MACHINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848)
- [OS_MGMT_INFO_FORMAT_PROCESSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082)
- [OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5)
- [OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76)
- [OS_MGMT_INFO_FORMAT_USER_CUSTOM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2)

<a id="header-details"></a>

---

[上一章](P030_zephyr__dt-bindings__gpio__nordic-nrf-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__bluetooth__audio__pacs.h_文件参考.md)
