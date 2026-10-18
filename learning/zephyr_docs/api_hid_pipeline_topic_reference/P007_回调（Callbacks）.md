---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-7
title: 回调（Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_回调（Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 回调 API

<a id="details"></a>

MCUmgr 回调 API

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Fenum_5Fmgmt"></a>

相关声明：[枚举管理回调（Enumeration Management Callbacks）](../api_extension_topic_reference/P014_枚举管理回调（Enumeration Management Callbacks）.md)。

MCUmgr 枚举管理回调 API

<a id="r_mcumgr_5Fcallback_5Fapi_5Ffs_5Fmgmt"></a>

相关声明：[文件系统管理回调（File System Management Callbacks）](../api_device_topic_reference/P014_文件系统管理回调（File System Management Callbacks）.md)。

MCUmgr 文件系统管理回调 API

<a id="r_mcumgr_5Fcallback_5Fapi_5Fimg_5Fmgmt"></a>

相关声明：[映像管理回调（Image Management Callbacks）](../api_update_memory_topic_reference/P010_映像管理回调（Image Management Callbacks）.md)。

MCUmgr 映像管理回调 API

<a id="r_mcumgr_5Fcallback_5Fapi_5Fos_5Fmgmt"></a>

相关声明：[操作系统管理回调（OS Management Callbacks）](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md)。

MCUmgr 操作系统管理回调 API

<a id="r_mcumgr_5Fcallback_5Fapi_5Fsettings_5Fmgmt"></a>

相关声明：[设置管理回调（Settings Management Callbacks）](../api_auxiliary_topic_reference/P011_设置管理回调（Settings Management Callbacks）.md)。

MCUmgr 设置管理回调 API

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

<a id="r_mgmt_5Fcallback"></a>

```c
struct mgmt_callback
```

相关声明：[mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)。

管理（MGMT）的回调结构。

<a id="r_mgmt_5Fevt_5Fop_5Fcmd_5Farg"></a>

```c
struct mgmt_evt_op_cmd_arg
```

相关声明：[mgmt_evt_op_cmd_arg](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md)。

MGMT_EVT_OP_CMD_RECV、MGMT_EVT_OP_CMD_STATUS和MGMT_EVT_OP_CMD_DONE的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.3\_宏定义（Macros）

<a id="r_gaa3290bd9a21f9718adac92bfe313161f"></a>

```c
#define MGMT_EVT_GET_GROUP(event)
```

相关声明：[MGMT_EVT_GET_GROUP](#gaa3290bd9a21f9718adac92bfe313161f)。

从事件（event）中提取组（group）。

<a id="r_ga4c6ff3fb3b14a31e65248cec9840b1dd"></a>

```c
#define MGMT_EVT_GET_ID(event)
```

相关声明：[MGMT_EVT_GET_ID](#ga4c6ff3fb3b14a31e65248cec9840b1dd)。

从事件中提取事件标识符（event ID）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.4\_类型定义（Typedefs）

<a id="r_gae61f705224a859776ee5161dfda5ed7d"></a>

```c
typedef enum mgmt_cb_return(* mgmt_cb) (uint32_t event, enum mgmt_cb_return prev_status, int32_t *rc, uint16_t *group, bool *abort_more, void *data, size_t data_size)
```

相关声明：[mgmt_cb_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[mgmt_cb](#gae61f705224a859776ee5161dfda5ed7d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mgmt_cb_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[group](../posix_system_model_reference/P003_group_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

收到管理（MGMT）通知／事件时调用的函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.5\_枚举（Enumerations）

<a id="r_ga1ba636c0efb7a91630ed9743e6fd4d6c"></a>

```c
enum mgmt_cb_return { MGMT_CB_OK , MGMT_CB_ERROR_RC , MGMT_CB_ERROR_ERR }
```

相关声明：[mgmt_cb_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[MGMT_CB_OK](#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da)、[MGMT_CB_ERROR_RC](#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990)、[MGMT_CB_ERROR_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d)。

管理（MGMT）事件回调的返回值。

<a id="r_ga40ecf8933112abe76d7fedb3dcc7cdbe"></a>

```c
enum mgmt_cb_groups { MGMT_EVT_GRP_ALL = 0 , MGMT_EVT_GRP_SMP , MGMT_EVT_GRP_OS , MGMT_EVT_GRP_IMG , MGMT_EVT_GRP_FS , MGMT_EVT_GRP_SETTINGS , MGMT_EVT_GRP_ENUM , MGMT_EVT_GRP_USER_CUSTOM_START = MGMT_GROUP_ID_PERUSER }
```

相关声明：[mgmt_cb_groups](#ga40ecf8933112abe76d7fedb3dcc7cdbe)、[MGMT_EVT_GRP_ALL](#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a)、[MGMT_EVT_GRP_SMP](#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)、[MGMT_EVT_GRP_OS](#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)、[MGMT_EVT_GRP_IMG](#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)、[MGMT_EVT_GRP_FS](#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)、[MGMT_EVT_GRP_SETTINGS](#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)、[MGMT_EVT_GRP_ENUM](#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)、[MGMT_EVT_GRP_USER_CUSTOM_START](#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d)。

MGMT 事件回调的组标识符（group IDs）。

<a id="r_gaab6470007be89e5aab88838456f9561a"></a>

```c
enum smp_all_events { MGMT_EVT_OP_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ALL) }
```

相关声明：[smp_all_events](#gaab6470007be89e5aab88838456f9561a)、[MGMT_EVT_OP_ALL](#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)。

所有命令处理操作所用的 MGMT 事件操作码（opcodes）。

<a id="r_ga590788274b4508c6203685d9e9252184"></a>

```c
enum smp_group_events { MGMT_EVT_OP_CMD_RECV = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 0) , MGMT_EVT_OP_CMD_STATUS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 1) , MGMT_EVT_OP_CMD_DONE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 2) , MGMT_EVT_OP_CMD_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SMP) }
```

相关声明：[smp_group_events](#ga590788274b4508c6203685d9e9252184)、[MGMT_EVT_OP_CMD_RECV](#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)、[MGMT_EVT_OP_CMD_STATUS](#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)、[MGMT_EVT_OP_CMD_DONE](#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)、[MGMT_EVT_OP_CMD_ALL](#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70)。

基础简单管理协议（SMP）命令处理所用的 MGMT 事件操作码（opcodes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.6\_函数（Functions）

<a id="r_gab309008a29ddcde95654ad812463d3bc"></a>

```c
uint8_t mgmt_evt_get_index (uint32_t event)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mgmt_evt_get_index](#gab309008a29ddcde95654ad812463d3bc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从事件中提取事件 ID 索引（event ID index）。

<a id="r_gaf9308502f8137f7fb80667941cdd46ca"></a>

```c
enum mgmt_cb_return mgmt_callback_notify (uint32_t event, void *data, size_t data_size, int32_t *err_rc, uint16_t *err_group)
```

相关声明：[mgmt_cb_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[mgmt_callback_notify](#gaf9308502f8137f7fb80667941cdd46ca)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

调用此函数，将 mcumgr 通知／事件告知已注册的回调函数。

<a id="r_gaaf698627904995930784c96fb48a1d7b"></a>

```c
void mgmt_callback_register (struct mgmt_callback *callback)
```

相关声明：[mgmt_callback_register](#gaaf698627904995930784c96fb48a1d7b)、[mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)。

注册事件回调函数（event callback function）。

<a id="r_ga24d97d6d17c5586a45abacb59d906bd2"></a>

```c
void mgmt_callback_unregister (struct mgmt_callback *callback)
```

相关声明：[mgmt_callback_unregister](#ga24d97d6d17c5586a45abacb59d906bd2)、[mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)。

注销事件回调函数。

## 7.7\_详细说明（Detailed Documentation）

<a id="gaa3290bd9a21f9718adac92bfe313161f"></a>

### `MGMT_EVT_GET_GROUP`

```c
#define MGMT_EVT_GET_GROUP ( event)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callback_defines.h>
```

展开值（Value）：

```c
((event >> 16) & MGMT_EVT_OP_ID_ALL)
```

从事件（event）中提取组（group）。

<a id="ga4c6ff3fb3b14a31e65248cec9840b1dd"></a>

### `MGMT_EVT_GET_ID`

```c
#define MGMT_EVT_GET_ID ( event)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callback_defines.h>
```

展开值（Value）：

```c
(event & MGMT_EVT_OP_ID_ALL)
```

从事件中提取事件标识符（event ID）。

<a id="gae61f705224a859776ee5161dfda5ed7d"></a>

### `mgmt_cb`

```c
typedef enum mgmt_cb_return(* mgmt_cb) (uint32_t event, enum mgmt_cb_return prev_status, int32_t *rc, uint16_t *group, bool *abort_more, void *data, size_t data_size)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

收到管理（MGMT）通知／事件时调用的函数。

此回调函数（Callback Function）用于向应用或系统通知 MCUmgr 管理事件（mgmt Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | `mcumgr_op_t` 操作类型。 |
| `prev_status` | 前面处理函数调用返回的 `mgmt_cb_return`。若为错误，则是某个处理函数首次返回的错误；此时当前处理函数仅接收通知，其返回码将被忽略。 |
| `rc` | 若 `prev_status` 为 `MGMT_CB_ERROR_RC`，则此值是首个失败处理函数返回的 SMP 错误；若为 `MGMT_CB_ERROR_ERR`，则此值是首个失败处理函数返回的组错误 `rc` 码。处理函数若要报告 SMP 错误，必须将此值设为 `mcumgr_err_t` 状态，并返回 `MGMT_CB_ERROR_RC`；若要报告组 `ret` 错误，必须将此值设为该组的 `ret` 状态，并返回 `MGMT_CB_ERROR_ERR`。 |
| `group` | 若 `prev_status` 为 `MGMT_CB_ERROR_ERR`，则此值是首个失败处理函数返回的 `ret` 错误所属组。处理函数若要报告 `ret` 错误，原文要求将此值设为组 `ret` 状态，并返回 `MGMT_CB_ERROR_ERR`。译注：此参数用于错误所属组；原文这里的“group ret status”措辞按原样保留。 |
| `abort_more` | 设为 `true`，以中止后续其他处理函数（Handlers）的处理。 |
| `data` | 可选事件参数（Optional Event Argument）。 |
| `data_size` | 可选事件参数大小（Size）；未提供数据时为 0。 |

**返回（Returns）**：返回值：`mgmt_cb_return`，表示要返回给调用代码的状态。仅当这是处理函数报告的首次失败时，才会检查此返回值。

<a id="ga40ecf8933112abe76d7fedb3dcc7cdbe"></a>

### `mgmt_cb_groups`

```c
enum mgmt_cb_groups
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callback_defines.h>
```

MGMT 事件回调的组标识符（group IDs）。

注意：这与 `mcumgr_group_t` 的取值不是一一对应关系（1:1 Mapping）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_GRP_ALL` |  |
| `MGMT_EVT_GRP_SMP` |  |
| `MGMT_EVT_GRP_OS` |  |
| `MGMT_EVT_GRP_IMG` |  |
| `MGMT_EVT_GRP_FS` |  |
| `MGMT_EVT_GRP_SETTINGS` |  |
| `MGMT_EVT_GRP_ENUM` |  |
| `MGMT_EVT_GRP_USER_CUSTOM_START` |  |

<a id="ga1ba636c0efb7a91630ed9743e6fd4d6c"></a>

### `mgmt_cb_return`

```c
enum mgmt_cb_return
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callback_defines.h>
```

管理（MGMT）事件回调的返回值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_CB_OK` | 无错误（No Error）。 |
| `MGMT_CB_ERROR_RC` | SMP 协议错误（Protocol Error）；`err_rc` 包含 `mcumgr_err_t` 错误码。 |
| `MGMT_CB_ERROR_ERR` | 组级应用层错误（Group/Application-level Error）；`err_group` 包含造成错误的组 ID，`err_rc` 包含要返回的该组错误码。 |

<a id="gaab6470007be89e5aab88838456f9561a"></a>

### `smp_all_events`

```c
enum smp_all_events
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callback_defines.h>
```

所有命令处理操作所用的 MGMT 事件操作码（opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_ALL` | 用于启用所有事件（All Events）。 |

<a id="ga590788274b4508c6203685d9e9252184"></a>

### `smp_group_events`

```c
enum smp_group_events
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

基础简单管理协议（SMP）命令处理所用的 MGMT 事件操作码（opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_CMD_RECV` | 收到命令时的回调（Callback），数据为 `mgmt_evt_op_cmd_arg`。 |
| `MGMT_EVT_OP_CMD_STATUS` | 更新状态时的回调（Callback），数据为 `mgmt_evt_op_cmd_arg`。 |
| `MGMT_EVT_OP_CMD_DONE` | 命令处理完成时的回调（Callback），数据为 `mgmt_evt_op_cmd_arg`。 |
| `MGMT_EVT_OP_CMD_ALL` | 用于启用所有 `smp_group` 事件（Events）。 |

<a id="gaf9308502f8137f7fb80667941cdd46ca"></a>

### `mgmt_callback_notify()`

```c
enum mgmt_cb_return mgmt_callback_notify ( uint32_t event, void * data, size_t data_size, int32_t * err_rc, uint16_t * err_group )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

调用此函数，将 mcumgr 通知／事件告知已注册的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | `mcumgr_op_t` 操作类型。 |
| `data` | 可选事件参数（Optional Event Argument）。 |
| `data_size` | 可选事件参数大小（Size），没有参数时为 0。 |
| `err_rc` | 指向 `rc` 值的指针。 |
| `err_group` | 指向 `group` 值的指针。 |

**返回（Returns）**：返回值：`mgmt_cb_return`。若所有处理函数均返回成功，则为 `MGMT_CB_OK`；若首个失败处理函数返回 SMP 错误，则为 `MGMT_CB_ERROR_RC`，此时 `err_rc` 更新为该 SMP 错误；若首个失败处理函数返回 `ret` 组及错误，则为 `MGMT_CB_ERROR_ERR`，此时 `err_group` 更新为失败的组 ID，`err_rc` 更新为该组专用错误码。

<a id="gaaf698627904995930784c96fb48a1d7b"></a>

### `mgmt_callback_register()`

```c
void mgmt_callback_register ( struct mgmt_callback * callback)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

注册事件回调函数（event callback function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 回调结构体（Callback Struct）。 |

<a id="ga24d97d6d17c5586a45abacb59d906bd2"></a>

### `mgmt_callback_unregister()`

```c
void mgmt_callback_unregister ( struct mgmt_callback * callback)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

注销事件回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callback` | 回调结构体（Callback Struct）。 |

<a id="gab309008a29ddcde95654ad812463d3bc"></a>

### `mgmt_evt_get_index()`

```c
uint8_t mgmt_evt_get_index ( uint32_t event)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

从事件中提取事件 ID 索引（event ID index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | 要获取其 ID 索引的事件（Event）。 |

**返回（Returns）**：返回值：事件索引（Event Index）。


## 7.8\_原页交叉引用（Cross References）

- [枚举管理回调（Enumeration Management Callbacks）](../api_extension_topic_reference/P014_枚举管理回调（Enumeration Management Callbacks）.md)
- [文件系统管理回调（File System Management Callbacks）](../api_device_topic_reference/P014_文件系统管理回调（File System Management Callbacks）.md)
- [映像管理回调（Image Management Callbacks）](../api_update_memory_topic_reference/P010_映像管理回调（Image Management Callbacks）.md)
- [操作系统管理回调（OS Management Callbacks）](../api_device_topic_reference/P015_操作系统管理回调（OS Management Callbacks）.md)
- [设置管理回调（Settings Management Callbacks）](../api_auxiliary_topic_reference/P011_设置管理回调（Settings Management Callbacks）.md)
- [mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)
- [mgmt_evt_op_cmd_arg](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/mgmt/mcumgr/mgmt/callback_defines.h](../api_file_interface_reference/P006_zephyr__mgmt__mcumgr__mgmt__callback_defines.h_文件参考.md)
- [zephyr/mgmt/mcumgr/mgmt/callbacks.h](../api_file_management_reference/P003_zephyr__mgmt__mcumgr__mgmt__callbacks.h_文件参考.md)
- [mcumgr_op_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae06a618f492f18e856742b4affab80dd)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [mcumgr_group_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3"></a>
<a id="gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d"></a>
<a id="gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da"></a>
<a id="gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990"></a>
<a id="gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d"></a>
<a id="ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a"></a>
<a id="gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28"></a>
<a id="gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770"></a>
<a id="gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12"></a>
<a id="gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_MC3419 API主题.md) · [返回大纲](大纲.md) · [下一章](P008_容器（Bins）.md)
