---
id: learning.zephyr-docs.api-source-reference.page-83
title: callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h.html)。

## 83.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00045"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="acallback__defines_8h_html"></a>
<a id="aenum__mgmt__callbacks_8h_html"></a>
<a id="afs__mgmt__callbacks_8h_html"></a>
<a id="agroup__mcumgr__callback__api_html_ga1ba636c0efb7a91630ed9743e6fd4d6c"></a>
<a id="agroup__mcumgr__callback__api_html_ga24d97d6d17c5586a45abacb59d906bd2"></a>
<a id="agroup__mcumgr__callback__api_html_ga590788274b4508c6203685d9e9252184"></a>
<a id="agroup__mcumgr__callback__api_html_gaaf698627904995930784c96fb48a1d7b"></a>
<a id="agroup__mcumgr__callback__api_html_gab309008a29ddcde95654ad812463d3bc"></a>
<a id="agroup__mcumgr__callback__api_html_gae61f705224a859776ee5161dfda5ed7d"></a>
<a id="agroup__mcumgr__callback__api_html_gaf9308502f8137f7fb80667941cdd46ca"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c"></a>
<a id="agroup__mcumgr__callback__api_html_gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28"></a>
<a id="agroup__mcumgr__callback__api_html_gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70"></a>
<a id="agroup__mcumgr__callback__api_html_gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12"></a>
<a id="agroup__mcumgr__callback__api_html_gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aimg__mgmt__callbacks_8h_html"></a>
<a id="ainttypes_8h_html"></a>
<a id="amgmt_8h_html"></a>
<a id="aos__mgmt__callbacks_8h_html"></a>
<a id="asettings__mgmt__callbacks_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructgroup_html"></a>
<a id="astructmgmt__callback_html"></a>
<a id="astructmgmt__callback_html_a3dc18e5f7e3e00c1c05cc104bb1f3ab1"></a>
<a id="astructmgmt__callback_html_a4595cb6a72ebf8b9396e63a8f31c497f"></a>
<a id="astructmgmt__callback_html_acd79e73a2a3d44697bbda2b401d1e7df"></a>
<a id="astructmgmt__evt__op__cmd__arg_html"></a>
<a id="astructmgmt__evt__op__cmd__arg_html_a0607126986dc0a1e9a0dae348d278741"></a>
<a id="astructmgmt__evt__op__cmd__arg_html_a4d08fca41a60aee6c458d510d528a307"></a>
<a id="astructmgmt__evt__op__cmd__arg_html_a7e7a469f944d27d92e25e42d56fa32d2"></a>
<a id="astructmgmt__evt__op__cmd__arg_html_ac461e832ea0997ae19be72df4caf0bb7"></a>
<a id="astructmgmt__evt__op__cmd__arg_html_acbd58ae2efe86685df33e58450753fe1"></a>

```c
/*
 * Copyright (c) 2022-2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACKS_H_

#include <inttypes.h>
#include <zephyr/sys/slist.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include "callback_defines.h"

#if defined(CONFIG_MCUMGR_GRP_FS) || defined(__DOXYGEN__)
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h>
#endif

#if defined(CONFIG_MCUMGR_GRP_IMG) || defined(__DOXYGEN__)
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
#endif

#if defined(CONFIG_MCUMGR_GRP_OS) || defined(__DOXYGEN__)
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h>
#endif

#if defined(CONFIG_MCUMGR_GRP_SETTINGS) || defined(__DOXYGEN__)
#include <zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h>
#endif

#if defined(CONFIG_MCUMGR_GRP_ENUM) || defined(__DOXYGEN__)
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif


typedef enum mgmt_cb_return (*mgmt_cb)(uint32_t event, enum mgmt_cb_return prev_status,
                                       int32_t *rc, uint16_t *group, bool *abort_more, void *data,
                                       size_t data_size);

enum smp_group_events {
        MGMT_EVT_OP_CMD_RECV                    = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 0),

        MGMT_EVT_OP_CMD_STATUS                  = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 1),

        MGMT_EVT_OP_CMD_DONE                    = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_SMP, 2),

        MGMT_EVT_OP_CMD_ALL                     = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_SMP),
};

struct mgmt_callback {
        sys_snode_t node;

        mgmt_cb callback;

        uint32_t event_id;
};

struct mgmt_evt_op_cmd_arg {
        uint16_t group;

        uint8_t id;

        union {
                uint8_t op;

                int err;

                int status;
        };
};

uint8_t mgmt_evt_get_index(uint32_t event);

enum mgmt_cb_return mgmt_callback_notify(uint32_t event, void *data, size_t data_size,
                                         int32_t *err_rc, uint16_t *err_group);

void mgmt_callback_register(struct mgmt_callback *callback);

void mgmt_callback_unregister(struct mgmt_callback *callback);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACKS_H_ */
```

## 83.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 190 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_CALLBACKS_H_`。

## 83.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [callback_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/callback__defines_8h.html)
- [zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html)
- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html)
- [zephyr/mgmt/mcumgr/grp/settings_mgmt/settings_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html)
- [zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html)
- [mgmt_cb_return](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga1ba636c0efb7a91630ed9743e6fd4d6c)
- [mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [smp_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga590788274b4508c6203685d9e9252184)
- [MGMT_EVT_OP_CMD_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)
- [MGMT_EVT_GRP_SMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)
- [MGMT_EVT_OP_CMD_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)
- [MGMT_EVT_OP_CMD_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)
- [MGMT_EVT_OP_CMD_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70)
- [mgmt_callback](../system_service_model_reference/P066_mgmt_callback_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../system_service_model_reference/P066_mgmt_callback_结构体.md#a4595cb6a72ebf8b9396e63a8f31c497f)
- [callback](../system_service_model_reference/P066_mgmt_callback_结构体.md#acd79e73a2a3d44697bbda2b401d1e7df)
- [event_id](../system_service_model_reference/P066_mgmt_callback_结构体.md#a3dc18e5f7e3e00c1c05cc104bb1f3ab1)
- [mgmt_evt_op_cmd_arg](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md)
- [group](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a0607126986dc0a1e9a0dae348d278741)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#ac461e832ea0997ae19be72df4caf0bb7)
- [op](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#acbd58ae2efe86685df33e58450753fe1)
- [err](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a7e7a469f944d27d92e25e42d56fa32d2)
- [status](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a4d08fca41a60aee6c458d510d528a307)
- [mgmt_evt_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gab309008a29ddcde95654ad812463d3bc)
- [mgmt_callback_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaf9308502f8137f7fb80667941cdd46ca)
- [mgmt_callback_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gaaf698627904995930784c96fb48a1d7b)
- [mgmt_callback_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ga24d97d6d17c5586a45abacb59d906bd2)
- [enum_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html)
- [fs_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html)
- [img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html)
- [mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [os_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h.html)
- [settings_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/settings__mgmt__callbacks_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [mgmt_callback::event_id](../system_service_model_reference/P066_mgmt_callback_结构体.md#a3dc18e5f7e3e00c1c05cc104bb1f3ab1)
- [mgmt_callback::node](../system_service_model_reference/P066_mgmt_callback_结构体.md#a4595cb6a72ebf8b9396e63a8f31c497f)
- [mgmt_callback::callback](../system_service_model_reference/P066_mgmt_callback_结构体.md#acd79e73a2a3d44697bbda2b401d1e7df)
- [mgmt_evt_op_cmd_arg::group](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a0607126986dc0a1e9a0dae348d278741)
- [mgmt_evt_op_cmd_arg::status](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a4d08fca41a60aee6c458d510d528a307)
- [mgmt_evt_op_cmd_arg::err](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#a7e7a469f944d27d92e25e42d56fa32d2)
- [mgmt_evt_op_cmd_arg::id](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#ac461e832ea0997ae19be72df4caf0bb7)
- [mgmt_evt_op_cmd_arg::op](../system_service_model_reference/P067_mgmt_evt_op_cmd_arg_结构体.md#acbd58ae2efe86685df33e58450753fe1)

---

[上一章](P082_callback_defines.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P084_can_fake.h_源码浏览.md)
