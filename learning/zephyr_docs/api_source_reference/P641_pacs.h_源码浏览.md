---
id: learning.zephyr-docs.api-source-reference.page-641
title: pacs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第641章\_pacs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h.html)。

## 641.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00039"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga61230848c02098352320fe751332c4e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gafb379ffa88388cc1397960155bbb2ab3"></a>
<a id="agroup__bt__audio_html_ga5bd899fb5e4d844058184913866e462f"></a>
<a id="agroup__bt__pacs_html_ga12f283d2daf72302a01cefb4a4a8fc70"></a>
<a id="agroup__bt__pacs_html_ga251b36d4f5775eea1f69873709f847cc"></a>
<a id="agroup__bt__pacs_html_ga29a1ec26c1e5e82e02eac39e1088332c"></a>
<a id="agroup__bt__pacs_html_ga31e2c7e9a4b5b6a291b96832c1218a49"></a>
<a id="agroup__bt__pacs_html_ga437d824d0a944b6c30db492dbe28514f"></a>
<a id="agroup__bt__pacs_html_ga452591f80b6be5d79609b25ade2154a9"></a>
<a id="agroup__bt__pacs_html_ga4f6015eba63ffc7a9377afe54a290da1"></a>
<a id="agroup__bt__pacs_html_ga7b28aa42525344445b20bb90a19441aa"></a>
<a id="agroup__bt__pacs_html_gabae9cf025f32ce80b660ebd7f95241b2"></a>
<a id="agroup__bt__pacs_html_gac23d3c4e850394194871e8daaa44545b"></a>
<a id="agroup__bt__pacs_html_gac77a3dd5015058145b51db5fef2c9485"></a>
<a id="agroup__bt__pacs_html_gaff290fd59bb05012abcf405dbdc72884"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astructbt__audio__codec__cap_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__pacs__cap_html"></a>
<a id="astructbt__pacs__cap_html_a2f311677a17aacec91f1ab7e1a7c787f"></a>
<a id="astructbt__pacs__register__param_html"></a>
<a id="astructbt__pacs__register__param_html_a3eda569266531da60342f0a170c4d152"></a>
<a id="astructbt__pacs__register__param_html_a7b5d14b7206a593821af96343120edbb"></a>
<a id="astructbt__pacs__register__param_html_a922188bb4e989aabb6b4cbba43d457c8"></a>
<a id="astructbt__pacs__register__param_html_af377b54efe30f22f4bfb1677964a1f00"></a>

```c


/* Copyright (c) 2021 Intel Corporation
 * Copyright (c) 2021-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PACS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PACS_H_


#include <stdbool.h>

#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_pacs_cap {
        const struct bt_audio_codec_cap *codec_cap;

        sys_snode_t _node;
};

struct bt_pacs_register_param {
#if defined(CONFIG_BT_PAC_SNK) || defined(__DOXYGEN__)
        bool snk_pac;
#endif /* CONFIG_BT_PAC_SNK */

#if defined(CONFIG_BT_PAC_SNK_LOC) || defined(__DOXYGEN__)
        bool snk_loc;
#endif /* CONFIG_BT_PAC_SNK_LOC */

#if defined(CONFIG_BT_PAC_SRC) || defined(__DOXYGEN__)
        bool src_pac;
#endif /* CONFIG_BT_PAC_SRC */

#if defined(CONFIG_BT_PAC_SRC_LOC) || defined(__DOXYGEN__)
        bool src_loc;
#endif /* CONFIG_BT_PAC_SRC_LOC */
};

typedef bool (*bt_pacs_cap_foreach_func_t)(const struct bt_pacs_cap *cap,
                                           void *user_data);

void bt_pacs_cap_foreach(enum bt_audio_dir dir,
                         bt_pacs_cap_foreach_func_t func,
                         void *user_data);

int bt_pacs_register(const struct bt_pacs_register_param *param);

int bt_pacs_unregister(void);

int bt_pacs_cap_register(enum bt_audio_dir dir, struct bt_pacs_cap *cap);

int bt_pacs_cap_unregister(enum bt_audio_dir dir, struct bt_pacs_cap *cap);

int bt_pacs_set_location(enum bt_audio_dir dir,
                         enum bt_audio_location location);

int bt_pacs_set_available_contexts(enum bt_audio_dir dir,
                                   enum bt_audio_context contexts);

enum bt_audio_context bt_pacs_get_available_contexts(enum bt_audio_dir dir);

int bt_pacs_conn_set_available_contexts_for_conn(struct bt_conn *conn, enum bt_audio_dir dir,
                                                 enum bt_audio_context *contexts);

enum bt_audio_context bt_pacs_get_available_contexts_for_conn(struct bt_conn *conn,
                                                              enum bt_audio_dir dir);

int bt_pacs_set_supported_contexts(enum bt_audio_dir dir,
                                   enum bt_audio_context contexts);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PACS_H_ */
```

## 641.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2021 Intel Corporation。

版权（Copyright）：© 2021-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 58 行

条件编译配置（Configuration）标记：`CONFIG_BT_PAC_SNK`。

### 注释 3：原第 68 行

条件编译配置（Configuration）标记：`CONFIG_BT_PAC_SNK_LOC`。

### 注释 4：原第 75 行

条件编译配置（Configuration）标记：`CONFIG_BT_PAC_SRC`。

### 注释 5：原第 85 行

条件编译配置（Configuration）标记：`CONFIG_BT_PAC_SRC_LOC`。

### 注释 6：原第 239 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PACS_H_`。

## 641.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [codec_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md#a2f311677a17aacec91f1ab7e1a7c787f)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)
- [snk_pac](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a7b5d14b7206a593821af96343120edbb)
- [snk_loc](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a3eda569266531da60342f0a170c4d152)
- [src_pac](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a922188bb4e989aabb6b4cbba43d457c8)
- [src_loc](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#af377b54efe30f22f4bfb1677964a1f00)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_pacs_cap_foreach_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga452591f80b6be5d79609b25ade2154a9)
- [bt_pacs_cap_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga31e2c7e9a4b5b6a291b96832c1218a49)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_pacs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac77a3dd5015058145b51db5fef2c9485)
- [bt_pacs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac23d3c4e850394194871e8daaa44545b)
- [bt_pacs_cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga251b36d4f5775eea1f69873709f847cc)
- [bt_pacs_cap_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga4f6015eba63ffc7a9377afe54a290da1)
- [bt_pacs_set_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gaff290fd59bb05012abcf405dbdc72884)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_pacs_set_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga29a1ec26c1e5e82e02eac39e1088332c)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_pacs_get_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga437d824d0a944b6c30db492dbe28514f)
- [bt_pacs_conn_set_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga12f283d2daf72302a01cefb4a4a8fc70)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_pacs_get_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga7b28aa42525344445b20bb90a19441aa)
- [bt_pacs_set_supported_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gabae9cf025f32ce80b660ebd7f95241b2)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_pacs_cap::codec_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md#a2f311677a17aacec91f1ab7e1a7c787f)
- [bt_pacs_register_param::snk_loc](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a3eda569266531da60342f0a170c4d152)
- [bt_pacs_register_param::snk_pac](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a7b5d14b7206a593821af96343120edbb)
- [bt_pacs_register_param::src_pac](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#a922188bb4e989aabb6b4cbba43d457c8)
- [bt_pacs_register_param::src_loc](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md#af377b54efe30f22f4bfb1677964a1f00)

---

[上一章](P640_packet.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P642_panel.h_源码浏览.md)
