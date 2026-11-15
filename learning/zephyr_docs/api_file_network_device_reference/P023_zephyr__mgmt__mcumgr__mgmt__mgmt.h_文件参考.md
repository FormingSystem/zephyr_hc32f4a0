---
id: learning.zephyr-docs.api-file-network-device-reference.page-23
title: zephyr__mgmt__mcumgr__mgmt__mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_mgmt\_\_mcumgr\_\_mgmt\_\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <inttypes.h>
#include <zephyr/sys/slist.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_mgmt_5Fhandler"></a>

```c
struct mgmt_handler
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)。

单个命令ID的读取处理程序和写入处理程序（Read / Write Handler）。

<a id="r_mgmt_5Fgroup"></a>

```c
struct mgmt_group
```

相关声明：[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)。

整个命令组（Command Group）的处理程序集合。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.2\_宏定义（Macros）

<a id="r_ga8027c2a587a835d92450f2935e66eea0"></a>

```c
#define MGMT_CTXT_SET_RC_RSN(mc, rsn)
```

相关声明：[MGMT_CTXT_SET_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga8027c2a587a835d92450f2935e66eea0)。

<a id="r_ga4d22641395a665a911be715c2531fbd8"></a>

```c
#define MGMT_CTXT_RC_RSN(mc)
```

相关声明：[MGMT_CTXT_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga4d22641395a665a911be715c2531fbd8)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.3\_类型定义（Typedefs）

<a id="r_ga292686c742179758ca5b853fc21fe302"></a>

```c
typedef void *(* mgmt_alloc_rsp_fn) (const void *src_buf, void *arg)
```

相关声明：[mgmt_alloc_rsp_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga292686c742179758ca5b853fc21fe302)。

分配适合保存响应（Response）的缓冲区。

<a id="r_ga1346d5160823c5e43fce3e6cba9f8607"></a>

```c
typedef void(* mgmt_reset_buf_fn) (void *buf, void *arg)
```

相关声明：[mgmt_reset_buf_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga1346d5160823c5e43fce3e6cba9f8607)。

将缓冲区长度重置为 0。

<a id="r_gaaafc2c73e1616340e29df6a1ba94c241"></a>

```c
typedef int(* mgmt_handler_fn) (struct smp_streamer *ctxt)
```

相关声明：[mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)、[smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)。

处理请求（Request）并写入对应响应（Response）。

<a id="r_ga9f63f42cd468ce85d0f800dc1472a5c8"></a>

```c
typedef bool(* mgmt_groups_cb_t) (const struct mgmt_group *group, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mgmt_groups_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga9f63f42cd468ce85d0f800dc1472a5c8)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

组遍历回调（Group Iteration Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.4\_函数（Functions）

<a id="r_ga70379f21faacddb5cc4a66f37a576ea0"></a>

```c
void mgmt_register_group (struct mgmt_group *group)
```

相关声明：[mgmt_register_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga70379f21faacddb5cc4a66f37a576ea0)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注册完整命令组（Command Group）。

<a id="r_ga87e98bdf47d1c7798098444f69ccf8b8"></a>

```c
void mgmt_unregister_group (struct mgmt_group *group)
```

相关声明：[mgmt_unregister_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga87e98bdf47d1c7798098444f69ccf8b8)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注销完整命令组（Command Group）。

<a id="r_ga125e3a6d076cade80f2080915a06ac67"></a>

```c
void mgmt_groups_foreach (mgmt_groups_cb_t user_cb, void *user_data)
```

相关声明：[mgmt_groups_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga125e3a6d076cade80f2080915a06ac67)、[mgmt_groups_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga9f63f42cd468ce85d0f800dc1472a5c8)。

遍历各组（Groups）。

<a id="r_ga620862436fad440b9d2b9d8112be4ad1"></a>

```c
const struct mgmt_handler * mgmt_find_handler (uint16_t group_id, uint16_t command_id)
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)、[mgmt_find_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga620862436fad440b9d2b9d8112be4ad1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令处理程序（Command Handler）。

<a id="r_gae88bc30026fbff6530179a94ba8f11ae"></a>

```c
const struct mgmt_group * mgmt_find_group (uint16_t group_id)
```

相关声明：[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[mgmt_find_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae88bc30026fbff6530179a94ba8f11ae)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令组（Command Group）。

<a id="r_gaec6ccbcaf28404b4b3662d5059f0a32b"></a>

```c
const struct mgmt_handler * mgmt_get_handler (const struct mgmt_group *group, uint16_t command_id)
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)、[mgmt_get_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaec6ccbcaf28404b4b3662d5059f0a32b)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令处理程序（Command Handler）。


## 23.5\_原页交叉引用（Cross References）

- [inttypes.h](../api_source_http_wifi_reference/P005_inttypes.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/mgmt/mcumgr/smp/smp.h](../api_source_supplement_reference/P113_smp.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](../api_source_reference/P522_mgmt_defines.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P521_mgmt.h_源码浏览.md)
- [mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)
- [mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)
- [MGMT_CTXT_SET_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga8027c2a587a835d92450f2935e66eea0)
- [MGMT_CTXT_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga4d22641395a665a911be715c2531fbd8)
- [mgmt_alloc_rsp_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga292686c742179758ca5b853fc21fe302)
- [mgmt_reset_buf_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga1346d5160823c5e43fce3e6cba9f8607)
- [mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mgmt_groups_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga9f63f42cd468ce85d0f800dc1472a5c8)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [mgmt_register_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga70379f21faacddb5cc4a66f37a576ea0)
- [mgmt_unregister_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga87e98bdf47d1c7798098444f69ccf8b8)
- [mgmt_groups_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga125e3a6d076cade80f2080915a06ac67)
- [mgmt_find_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga620862436fad440b9d2b9d8112be4ad1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mgmt_find_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae88bc30026fbff6530179a94ba8f11ae)
- [mgmt_get_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaec6ccbcaf28404b4b3662d5059f0a32b)

---

[上一章](P022_zephyr__drivers__mfd__mc146818.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__drivers__modem__modem_cellular.h_文件参考.md)
