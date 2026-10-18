---
id: learning.zephyr-docs.api-file-management-reference.page-3
title: zephyr__mgmt__mcumgr__mgmt__callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_mgmt\_\_mcumgr\_\_mgmt\_\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <inttypes.h>
#include <zephyr/sys/slist.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include "callback_defines.h"
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h>
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h>
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h>
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_gae61f705224a859776ee5161dfda5ed7d"></a>

```c
typedef enum mgmt_cb_return(* mgmt_cb) (uint32_t event, enum mgmt_cb_return prev_status, int32_t *rc, uint16_t *group, bool *abort_more, void *data, size_t data_size)
```

相关声明：[mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[group](../posix_system_model_reference/P003_group_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

收到管理（MGMT）通知／事件时调用的函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_ga590788274b4508c6203685d9e9252184"></a>

```c
enum smp_group_events { MGMT_EVT_OP_CMD_RECV = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 0) , MGMT_EVT_OP_CMD_STATUS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 1) , MGMT_EVT_OP_CMD_DONE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 2) , MGMT_EVT_OP_CMD_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SMP) }
```

相关声明：[smp_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga590788274b4508c6203685d9e9252184)、[MGMT_EVT_OP_CMD_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)、[MGMT_EVT_OP_CMD_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)、[MGMT_EVT_OP_CMD_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)、[MGMT_EVT_OP_CMD_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70)。

基础简单管理协议（SMP）命令处理所用的 MGMT 事件操作码（opcodes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gab309008a29ddcde95654ad812463d3bc"></a>

```c
uint8_t mgmt_evt_get_index (uint32_t event)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mgmt_evt_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gab309008a29ddcde95654ad812463d3bc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从事件中提取事件 ID 索引（event ID index）。

<a id="r_gaf9308502f8137f7fb80667941cdd46ca"></a>

```c
enum mgmt_cb_return mgmt_callback_notify (uint32_t event, void *data, size_t data_size, int32_t *err_rc, uint16_t *err_group)
```

相关声明：[mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)、[mgmt_callback_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaf9308502f8137f7fb80667941cdd46ca)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

调用此函数，将 mcumgr 通知／事件告知已注册的回调函数。

<a id="r_gaaf698627904995930784c96fb48a1d7b"></a>

```c
void mgmt_callback_register (struct mgmt_callback *callback)
```

相关声明：[mgmt_callback_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaaf698627904995930784c96fb48a1d7b)、[mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)。

注册事件回调函数（event callback function）。

<a id="r_ga24d97d6d17c5586a45abacb59d906bd2"></a>

```c
void mgmt_callback_unregister (struct mgmt_callback *callback)
```

相关声明：[mgmt_callback_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga24d97d6d17c5586a45abacb59d906bd2)、[mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)。

注销事件回调函数。


## 3.5\_原页交叉引用（Cross References）

- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](../api_source_reference/P521_mgmt.h_源码浏览.md)
- [callback_defines.h](../api_source_reference/P082_callback_defines.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h](../api_source_reference/P275_fs_mgmt_callbacks.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](../api_source_supplement_reference/P091_img_mgmt_callbacks.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h](../api_source_reference/P637_os_mgmt_callbacks.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h](../api_source_reference/P772_settings_mgmt_callbacks.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h](../api_source_reference/P231_enum_mgmt_callbacks.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P083_callbacks.h_源码浏览.md)
- [mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)
- [mgmt_evt_op_cmd_arg](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md)
- [MGMT_EVT_OP_CMD_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)
- [MGMT_EVT_OP_CMD_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)
- [MGMT_EVT_OP_CMD_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)
- [mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)
- [mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga590788274b4508c6203685d9e9252184)
- [MGMT_EVT_OP_CMD_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mgmt_evt_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gab309008a29ddcde95654ad812463d3bc)
- [mgmt_callback_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaf9308502f8137f7fb80667941cdd46ca)
- [mgmt_callback_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaaf698627904995930784c96fb48a1d7b)
- [mgmt_callback_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga24d97d6d17c5586a45abacb59d906bd2)

---

[上一章](P002_zephyr__bluetooth__mesh__blob_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__prometheus__collector.h_文件参考.md)
