---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-8
title: 操作系统管理（OS Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_操作系统管理（OS Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 操作系统管理 API

<a id="details"></a>

MCUmgr 操作系统管理 API

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Fos_5Fmgmt"></a>

相关声明：[操作系统管理回调（OS Management Callbacks）](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md)。

MCUmgr 操作系统管理回调 API

<a id="r_mcumgr_5Fos_5Fmgmt_5Fclient"></a>

相关声明：[操作系统管理客户端（OS Management Client）](../api_extension_topic_reference/P016_操作系统管理客户端（OS Management Client）.md)。

MCUmgr 操作系统管理客户端 API

<a id="header-files"></a>
<a id="files"></a>

## 8.2\_文件（Files）

<a id="r_os_5Fmgmt_2Eh"></a>

```c
file os_mgmt.h
```

相关声明：[os_mgmt.h](../api_file_system_power_reference/P031_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt.h_文件参考.md)。

MCUmgr操作系统管理组（OS Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.3\_数据结构（Data Structures）

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

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga14dc9256e6585450ea34b13666aa8765"></a>

```c
enum os_mgmt_err_code_t { OS_MGMT_ERR_OK = 0 , OS_MGMT_ERR_UNKNOWN , OS_MGMT_ERR_INVALID_FORMAT , OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER , OS_MGMT_ERR_RTC_NOT_SET , OS_MGMT_ERR_RTC_COMMAND_FAILED , OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID , OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED }
```

相关声明：[os_mgmt_err_code_t](#ga14dc9256e6585450ea34b13666aa8765)、[OS_MGMT_ERR_OK](#gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4)、[OS_MGMT_ERR_UNKNOWN](#gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752)、[OS_MGMT_ERR_INVALID_FORMAT](#gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd)、[OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER](#gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)、[OS_MGMT_ERR_RTC_NOT_SET](#gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517)、[OS_MGMT_ERR_RTC_COMMAND_FAILED](#gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)、[OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID](#gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf)、[OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED](#gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f)。

操作系统管理组（OS Management Group）的命令结果码（Command Result Codes）。

<a id="r_ga54512f3d774835d1d277872835a3b26f"></a>

```c
enum os_mgmt_info_formats { OS_MGMT_INFO_FORMAT_KERNEL_NAME = BIT(0) , OS_MGMT_INFO_FORMAT_NODE_NAME = BIT(1) , OS_MGMT_INFO_FORMAT_KERNEL_RELEASE = BIT(2) , OS_MGMT_INFO_FORMAT_KERNEL_VERSION = BIT(3) , OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME = BIT(4) , OS_MGMT_INFO_FORMAT_MACHINE = BIT(5) , OS_MGMT_INFO_FORMAT_PROCESSOR = BIT(6) , OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM = BIT(7) , OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM = BIT(8) , OS_MGMT_INFO_FORMAT_USER_CUSTOM_START = BIT(9) }
```

相关声明：[os_mgmt_info_formats](#ga54512f3d774835d1d277872835a3b26f)、[OS_MGMT_INFO_FORMAT_KERNEL_NAME](#gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0)、[OS_MGMT_INFO_FORMAT_NODE_NAME](#gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3)、[OS_MGMT_INFO_FORMAT_KERNEL_RELEASE](#gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd)、[OS_MGMT_INFO_FORMAT_KERNEL_VERSION](#gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328)、[OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME](#gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d)、[OS_MGMT_INFO_FORMAT_MACHINE](#gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848)、[OS_MGMT_INFO_FORMAT_PROCESSOR](#gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082)、[OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM](#gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5)、[OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM](#gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76)、[OS_MGMT_INFO_FORMAT_USER_CUSTOM_START](#gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2)。

操作系统／应用信息格式（OS/Application Information Formats）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 8.5\_操作系统管理组命令 ID（Command IDs for OS Management Group）

<a id="r_ga24751ec5a8ba224238f484e2048f152a"></a>

```c
#define OS_MGMT_ID_ECHO 0
```

相关声明：[OS_MGMT_ID_ECHO](#ga24751ec5a8ba224238f484e2048f152a)。

回显（Echo）。

<a id="r_ga0093a8df477e7114ffa195a022851cbe"></a>

```c
#define OS_MGMT_ID_CONS_ECHO_CTRL 1
```

相关声明：[OS_MGMT_ID_CONS_ECHO_CTRL](#ga0093a8df477e7114ffa195a022851cbe)。

控制台／终端回显控制（Console/Terminal Echo Control）。

<a id="r_ga067886d5d5d1d8979f93bab61fc2a670"></a>

```c
#define OS_MGMT_ID_TASKSTAT 2
```

相关声明：[OS_MGMT_ID_TASKSTAT](#ga067886d5d5d1d8979f93bab61fc2a670)。

任务统计（Task Statistics）。

<a id="r_gaa2918e287d063fb2a82bd87d5c29aba4"></a>

```c
#define OS_MGMT_ID_MPSTAT 3
```

相关声明：[OS_MGMT_ID_MPSTAT](#gaa2918e287d063fb2a82bd87d5c29aba4)。

内存池统计（Memory Pool Statistics）。

<a id="r_gaf4370119858111637ee80af735b0e50c"></a>

```c
#define OS_MGMT_ID_DATETIME_STR 4
```

相关声明：[OS_MGMT_ID_DATETIME_STR](#gaf4370119858111637ee80af735b0e50c)。

日期时间字符串（Date-time String）。

<a id="r_ga4447fa2fa0c5f37713f7ef555174e814"></a>

```c
#define OS_MGMT_ID_RESET 5
```

相关声明：[OS_MGMT_ID_RESET](#ga4447fa2fa0c5f37713f7ef555174e814)。

系统复位（System Reset）。

<a id="r_ga6eb9918c2e6d1564fc362fe3dcdc63d5"></a>

```c
#define OS_MGMT_ID_MCUMGR_PARAMS 6
```

相关声明：[OS_MGMT_ID_MCUMGR_PARAMS](#ga6eb9918c2e6d1564fc362fe3dcdc63d5)。

MCUMgr 参数（Parameters）。

<a id="r_ga0103b1f0d37106c5166b1793c7743513"></a>

```c
#define OS_MGMT_ID_INFO 7
```

相关声明：[OS_MGMT_ID_INFO](#ga0103b1f0d37106c5166b1793c7743513)。

操作系统／应用信息（OS/Application Information）。

<a id="r_ga142393f94135f1dd91b8cf098e01aa6b"></a>

```c
#define OS_MGMT_ID_BOOTLOADER_INFO 8
```

相关声明：[OS_MGMT_ID_BOOTLOADER_INFO](#ga142393f94135f1dd91b8cf098e01aa6b)。

引导加载程序信息（Bootloader Information）。

## 8.6\_详细说明（Detailed Documentation）

<a id="ga142393f94135f1dd91b8cf098e01aa6b"></a>

### `OS_MGMT_ID_BOOTLOADER_INFO`

```c
#define OS_MGMT_ID_BOOTLOADER_INFO 8
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

引导加载程序信息（Bootloader Information）。

<a id="ga0093a8df477e7114ffa195a022851cbe"></a>

### `OS_MGMT_ID_CONS_ECHO_CTRL`

```c
#define OS_MGMT_ID_CONS_ECHO_CTRL 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

控制台／终端回显控制（Console/Terminal Echo Control）。

<a id="gaf4370119858111637ee80af735b0e50c"></a>

### `OS_MGMT_ID_DATETIME_STR`

```c
#define OS_MGMT_ID_DATETIME_STR 4
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

日期时间字符串（Date-time String）。

<a id="ga24751ec5a8ba224238f484e2048f152a"></a>

### `OS_MGMT_ID_ECHO`

```c
#define OS_MGMT_ID_ECHO 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

回显（Echo）。

<a id="ga0103b1f0d37106c5166b1793c7743513"></a>

### `OS_MGMT_ID_INFO`

```c
#define OS_MGMT_ID_INFO 7
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

操作系统／应用信息（OS/Application Information）。

<a id="ga6eb9918c2e6d1564fc362fe3dcdc63d5"></a>

### `OS_MGMT_ID_MCUMGR_PARAMS`

```c
#define OS_MGMT_ID_MCUMGR_PARAMS 6
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

MCUMgr 参数（Parameters）。

<a id="gaa2918e287d063fb2a82bd87d5c29aba4"></a>

### `OS_MGMT_ID_MPSTAT`

```c
#define OS_MGMT_ID_MPSTAT 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

内存池统计（Memory Pool Statistics）。

<a id="ga4447fa2fa0c5f37713f7ef555174e814"></a>

### `OS_MGMT_ID_RESET`

```c
#define OS_MGMT_ID_RESET 5
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

系统复位（System Reset）。

<a id="ga067886d5d5d1d8979f93bab61fc2a670"></a>

### `OS_MGMT_ID_TASKSTAT`

```c
#define OS_MGMT_ID_TASKSTAT 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

任务统计（Task Statistics）。

<a id="ga14dc9256e6585450ea34b13666aa8765"></a>

### `os_mgmt_err_code_t`

```c
enum os_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

操作系统管理组（OS Management Group）的命令结果码（Command Result Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OS_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `OS_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `OS_MGMT_ERR_INVALID_FORMAT` | 提供的格式值（Format Value）无效。 |
| `OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER` | 无法识别查询（Query）。 |
| `OS_MGMT_ERR_RTC_NOT_SET` | 实时时钟（RTC）尚未设置。 |
| `OS_MGMT_ERR_RTC_COMMAND_FAILED` | 实时时钟（RTC）命令失败。 |
| `OS_MGMT_ERR_QUERY_RESPONSE_VALUE_NOT_VALID` | 已识别查询（Query），但没有可用于响应的有效值。 |
| `OS_MGMT_ERR_HEAP_STATS_FETCH_FAILED` | 获取堆统计（Heap Statistics）失败。 |

<a id="ga54512f3d774835d1d277872835a3b26f"></a>

### `os_mgmt_info_formats`

```c
enum os_mgmt_info_formats
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

操作系统／应用信息格式（OS/Application Information Formats）。

操作系统信息（OS Info）命令处理程序使用的位掩码值（Bitmask Values）。注意：此变量宽度为 32 位，可容纳 32 个标志。自定义用户层实现应从 `OS_MGMT_INFO_FORMAT_USER_CUSTOM_START` 开始，并直接引用该常量，因为此列表未来可能加入额外的格式说明符（Format Specifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `OS_MGMT_INFO_FORMAT_KERNEL_NAME` | 内核名称（Kernel Name）。 |
| `OS_MGMT_INFO_FORMAT_NODE_NAME` | 节点名称（Node Name）。 |
| `OS_MGMT_INFO_FORMAT_KERNEL_RELEASE` | 内核发行号（Kernel Release）。 |
| `OS_MGMT_INFO_FORMAT_KERNEL_VERSION` | 内核版本（Kernel Version）。 |
| `OS_MGMT_INFO_FORMAT_BUILD_DATE_TIME` | 构建日期和时间（Build Date and Time）。 |
| `OS_MGMT_INFO_FORMAT_MACHINE` | 机器（Machine）。 |
| `OS_MGMT_INFO_FORMAT_PROCESSOR` | 处理器（Processor）。 |
| `OS_MGMT_INFO_FORMAT_HARDWARE_PLATFORM` | 硬件平台（Hardware Platform）。 |
| `OS_MGMT_INFO_FORMAT_OPERATING_SYSTEM` | 操作系统（Operating System）。 |
| `OS_MGMT_INFO_FORMAT_USER_CUSTOM_START` | 自定义用户层起始位（Custom User-level Start Bit）。 |


## 8.7\_原页交叉引用（Cross References）

- [操作系统管理回调（OS Management Callbacks）](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md)
- [操作系统管理客户端（OS Management Client）](../api_extension_topic_reference/P016_操作系统管理客户端（OS Management Client）.md)
- [os_mgmt.h](../api_file_system_power_reference/P031_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt.h_文件参考.md)
- [os_mgmt_info_check](../system_service_model_reference/P073_os_mgmt_info_check_结构体.md)
- [MGMT_EVT_OP_OS_MGMT_INFO_CHECK](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)
- [os_mgmt_info_append](../system_service_model_reference/P072_os_mgmt_info_append_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a31f119f779c11a4c416a45940ce57abf"></a>
<a id="gga14dc9256e6585450ea34b13666aa8765a947e3f94cbc9bc0b9c2062dde14fc01f"></a>
<a id="gga54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328"></a>
<a id="gga54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76"></a>
<a id="gga54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2"></a>

---

[上一章](P007_文件系统管理（File System Management）.md) · [返回大纲](大纲.md) · [下一章](P009_虚拟传输（Dummy transport）.md)
