---
id: learning.zephyr-docs.api-source-reference.page-521
title: mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第521章\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)。

## 521.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga125e3a6d076cade80f2080915a06ac67"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga1346d5160823c5e43fce3e6cba9f8607"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga620862436fad440b9d2b9d8112be4ad1"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga70379f21faacddb5cc4a66f37a576ea0"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga87e98bdf47d1c7798098444f69ccf8b8"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga9f63f42cd468ce85d0f800dc1472a5c8"></a>
<a id="agroup__mcumgr__mgmt__api_html_gaaafc2c73e1616340e29df6a1ba94c241"></a>
<a id="agroup__mcumgr__mgmt__api_html_gae88bc30026fbff6530179a94ba8f11ae"></a>
<a id="agroup__mcumgr__mgmt__api_html_gaec6ccbcaf28404b4b3662d5059f0a32b"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainttypes_8h_html"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html"></a>
<a id="amgmt__defines_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructgroup_html"></a>
<a id="astructmgmt__group_html"></a>
<a id="astructmgmt__group_html_a7a6e90e500716095b9a22e3f56edac03"></a>
<a id="astructmgmt__group_html_a8b2de48e97c0de4c902d72aba4e920b4"></a>
<a id="astructmgmt__group_html_a9d55dbf947096eed7cacfb9087d304d4"></a>
<a id="astructmgmt__group_html_ac150809b03f73c4c2f94742504af772c"></a>
<a id="astructmgmt__handler_html"></a>
<a id="astructmgmt__handler_html_a1bc6b52645f6eb1d0e0b0c695d972c15"></a>
<a id="astructmgmt__handler_html_a7cc4917fa24afef79f1a8de8549a21e4"></a>
<a id="astructsmp__streamer_html"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2022-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_H_

#include <inttypes.h>
#include <zephyr/sys/slist.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef void *(*mgmt_alloc_rsp_fn)(const void *src_buf, void *arg);

typedef void (*mgmt_reset_buf_fn)(void *buf, void *arg);

#ifdef CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE
#define MGMT_CTXT_SET_RC_RSN(mc, rsn) ((mc->rc_rsn) = (rsn))
#define MGMT_CTXT_RC_RSN(mc) ((mc)->rc_rsn)
#else
#define MGMT_CTXT_SET_RC_RSN(mc, rsn)
#define MGMT_CTXT_RC_RSN(mc) NULL
#endif

typedef int (*mgmt_handler_fn)(struct smp_streamer *ctxt);

struct mgmt_handler {
        mgmt_handler_fn mh_read;
        mgmt_handler_fn mh_write;
#if defined(CONFIG_MCUMGR_MGMT_HANDLER_USER_DATA)
        void *user_data;
#endif
};

struct mgmt_group {
        sys_snode_t node;

        const struct mgmt_handler *mg_handlers;
        uint16_t mg_handlers_count;

        uint16_t mg_group_id;

#if defined(CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)
        smp_translate_error_fn mg_translate_error;
#endif

#if defined(CONFIG_MCUMGR_MGMT_CUSTOM_PAYLOAD)
        bool custom_payload;
#endif

#if IS_ENABLED(CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME)
        const char *mg_group_name;
#endif
};

void mgmt_register_group(struct mgmt_group *group);

void mgmt_unregister_group(struct mgmt_group *group);

typedef bool (*mgmt_groups_cb_t)(const struct mgmt_group *group, void *user_data);

void mgmt_groups_foreach(mgmt_groups_cb_t user_cb, void *user_data);

const struct mgmt_handler *mgmt_find_handler(uint16_t group_id, uint16_t command_id);

const struct mgmt_group *mgmt_find_group(uint16_t group_id);

const struct mgmt_handler *mgmt_get_handler(const struct mgmt_group *group, uint16_t command_id);

#if defined(CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)
smp_translate_error_fn mgmt_find_error_translation_function(uint16_t group_id);
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_H_ */
```

## 521.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2022-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 201 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_H_`。

## 521.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/mgmt/mcumgr/smp/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [mgmt_reset_buf_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga1346d5160823c5e43fce3e6cba9f8607)
- [mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)
- [mh_read](../system_service_model_reference/P069_mgmt_handler_结构体.md#a7cc4917fa24afef79f1a8de8549a21e4)
- [mh_write](../system_service_model_reference/P069_mgmt_handler_结构体.md#a1bc6b52645f6eb1d0e0b0c695d972c15)
- [mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../system_service_model_reference/P068_mgmt_group_结构体.md#ac150809b03f73c4c2f94742504af772c)
- [mg_handlers](../system_service_model_reference/P068_mgmt_group_结构体.md#a7a6e90e500716095b9a22e3f56edac03)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mg_handlers_count](../system_service_model_reference/P068_mgmt_group_结构体.md#a8b2de48e97c0de4c902d72aba4e920b4)
- [mg_group_id](../system_service_model_reference/P068_mgmt_group_结构体.md#a9d55dbf947096eed7cacfb9087d304d4)
- [mgmt_register_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga70379f21faacddb5cc4a66f37a576ea0)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [mgmt_unregister_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga87e98bdf47d1c7798098444f69ccf8b8)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mgmt_groups_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga9f63f42cd468ce85d0f800dc1472a5c8)
- [mgmt_groups_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga125e3a6d076cade80f2080915a06ac67)
- [mgmt_find_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga620862436fad440b9d2b9d8112be4ad1)
- [mgmt_find_group](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae88bc30026fbff6530179a94ba8f11ae)
- [mgmt_get_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaec6ccbcaf28404b4b3662d5059f0a32b)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [mgmt_group::mg_handlers](../system_service_model_reference/P068_mgmt_group_结构体.md#a7a6e90e500716095b9a22e3f56edac03)
- [mgmt_group::mg_handlers_count](../system_service_model_reference/P068_mgmt_group_结构体.md#a8b2de48e97c0de4c902d72aba4e920b4)
- [mgmt_group::mg_group_id](../system_service_model_reference/P068_mgmt_group_结构体.md#a9d55dbf947096eed7cacfb9087d304d4)
- [mgmt_group::node](../system_service_model_reference/P068_mgmt_group_结构体.md#ac150809b03f73c4c2f94742504af772c)
- [mgmt_handler::mh_write](../system_service_model_reference/P069_mgmt_handler_结构体.md#a1bc6b52645f6eb1d0e0b0c695d972c15)
- [mgmt_handler::mh_read](../system_service_model_reference/P069_mgmt_handler_结构体.md#a7cc4917fa24afef79f1a8de8549a21e4)

---

[上一章](P520_mfd_mchp_sam_flexcom.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P522_mgmt_defines.h_源码浏览.md)
