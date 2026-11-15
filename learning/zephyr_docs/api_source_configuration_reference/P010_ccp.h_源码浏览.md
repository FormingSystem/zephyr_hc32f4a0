---
id: learning.zephyr-docs.api-source-configuration-reference.page-10
title: ccp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ccp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h.html)。

## 10.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00215"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga4bf3f820b493361a9a3b393d0282420f"></a>
<a id="agroup__bt__ccp__call__control__client_html_ga2a5bce65e39ba05625423308f996021d"></a>
<a id="agroup__bt__ccp__call__control__client_html_ga31455b659d7b20053624f79c71cefa84"></a>
<a id="agroup__bt__ccp__call__control__client_html_ga534a15db3e87d63942de6ba4bd8377db"></a>
<a id="agroup__bt__ccp__call__control__client_html_ga8c5c3907759fe02745339b9456cca05f"></a>
<a id="agroup__bt__ccp__call__control__client_html_ga9b146acb76b6e40ae639da92c5d50941"></a>
<a id="agroup__bt__ccp__call__control__client_html_gac106a4de174d941e6390a1743d11f01d"></a>
<a id="agroup__bt__ccp__call__control__client_html_gac8aa850b1e77bff1058e63be8c07c4c8"></a>
<a id="agroup__bt__ccp__call__control__client_html_gaf8df0504479ac519328d98f2ddf6db15"></a>
<a id="agroup__bt__ccp__call__control__server_html_ga0b775c233dcfd08f57322afaf6fa9bcf"></a>
<a id="agroup__bt__ccp__call__control__server_html_ga4c250633e8a9ff479952f9300c8eeddd"></a>
<a id="agroup__bt__ccp__call__control__server_html_ga5e5acb90cc39b5f8a4e25d8ab8a11b10"></a>
<a id="agroup__bt__ccp__call__control__server_html_ga84efc07e1703536ad6a005b5c5d9fb16"></a>
<a id="agroup__bt__ccp__call__control__server_html_gaa2486dec8a47bd7f4cd4076477e8ac4a"></a>
<a id="agroup__bt__ccp__call__control__server_html_gaae263e42d76d99d950ac535c22fe64c2"></a>
<a id="agroup__bt__ccp__call__control__server_html_gac670cf57d2f02df44ea0d82a58524242"></a>
<a id="agroup__bt__ccp__call__control__server_html_gad8525ac242806efd70d6adbd0148a0ba"></a>
<a id="agroup__bt__ccp__call__control__server_html_gaf7880d2e467b0931d894231312b7ed9b"></a>
<a id="agroup__bt__tbs_html_ga42b72d7aef36cc7ea0d5dd4ec3d7a717"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astructbt__ccp__call__control__client__bearer_html"></a>
<a id="astructbt__ccp__call__control__client__bearers_html"></a>
<a id="astructbt__ccp__call__control__client__bearers_html_a0d5936c39146ec97875c01a6d6bf1b26"></a>
<a id="astructbt__ccp__call__control__client__bearers_html_a100c4024c0086016ec87bc9feebacc52"></a>
<a id="astructbt__ccp__call__control__client__bearers_html_a1574714c19259a291c4557c0176462a4"></a>
<a id="astructbt__ccp__call__control__client__cb_html"></a>
<a id="astructbt__ccp__call__control__client__cb_html_a1d4af4ea50002e2f3d24ed0d4bf21d83"></a>
<a id="astructbt__ccp__call__control__client__cb_html_a3830ba768a1300df7aee272a2d3ec00e"></a>
<a id="astructbt__ccp__call__control__client__cb_html_a3c6d22aefdbef40ac42fb05e9656789a"></a>
<a id="astructbt__ccp__call__control__client__cb_html_a4ad442e0f84327a7d02b5bfd5bbf09c7"></a>
<a id="astructbt__ccp__call__control__client__cb_html_aba44cdf2667ca7622d7a8c70164cd847"></a>
<a id="astructbt__ccp__call__control__client__cb_html_aed9802f73963157a9f45ee35e50ad8ac"></a>
<a id="astructbt__ccp__call__control__client_html"></a>
<a id="astructbt__ccp__call__control__server__bearer_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__tbs__register__param_html"></a>
<a id="atbs_8h_html"></a>

```c


/*
 * Copyright (c) 2024-2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCP_H_


#include <stddef.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/tbs.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif
struct bt_ccp_call_control_server_bearer;

int bt_ccp_call_control_server_register_bearer(const struct bt_tbs_register_param *param,
                                               struct bt_ccp_call_control_server_bearer **bearer);

int bt_ccp_call_control_server_unregister_bearer(struct bt_ccp_call_control_server_bearer *bearer);

int bt_ccp_call_control_server_set_bearer_provider_name(
        struct bt_ccp_call_control_server_bearer *bearer, const char *name);

int bt_ccp_call_control_server_get_bearer_provider_name(
        struct bt_ccp_call_control_server_bearer *bearer, char *name, size_t name_size);

int bt_ccp_call_control_server_get_bearer_uci(struct bt_ccp_call_control_server_bearer *bearer,
                                              char uci[BT_TBS_MAX_UCI_SIZE]);

int bt_ccp_call_control_server_set_bearer_tech(struct bt_ccp_call_control_server_bearer *bearer,
                                               enum bt_bearer_tech tech);

int bt_ccp_call_control_server_get_bearer_tech(
        const struct bt_ccp_call_control_server_bearer *bearer, enum bt_bearer_tech *tech);

int bt_ccp_call_control_server_set_bearer_uri_schemes(
        struct bt_ccp_call_control_server_bearer *bearer, const char *uri_schemes);

int bt_ccp_call_control_server_get_bearer_uri_schemes(
        struct bt_ccp_call_control_server_bearer *bearer, char *uri_schemes,
        size_t uri_schemes_size); /* End of group bt_ccp_call_control_server */


struct bt_ccp_call_control_client;

struct bt_ccp_call_control_client_bearer;

struct bt_ccp_call_control_client_bearers {
#if defined(CONFIG_BT_TBS_CLIENT_GTBS) || defined(__DOXYGEN__)
        struct bt_ccp_call_control_client_bearer *gtbs_bearer;
#endif /* CONFIG_BT_TBS_CLIENT_GTBS */

#if defined(CONFIG_BT_TBS_CLIENT_TBS) || defined(__DOXYGEN__)
        size_t tbs_count;

        struct bt_ccp_call_control_client_bearer
                *tbs_bearers[CONFIG_BT_CCP_CALL_CONTROL_CLIENT_BEARER_COUNT];
#endif /* CONFIG_BT_TBS_CLIENT_TBS */
};

struct bt_ccp_call_control_client_cb {
        void (*discover)(struct bt_ccp_call_control_client *client, int err,
                         struct bt_ccp_call_control_client_bearers *bearers, void *user_data);

#if defined(CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME) || defined(__DOXYGEN__)
        void (*bearer_provider_name)(struct bt_ccp_call_control_client_bearer *bearer, int err,
                                     const char *name, void *user_data);
#endif /* CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME */

#if defined(CONFIG_BT_TBS_CLIENT_BEARER_UCI) || defined(__DOXYGEN__)
        void (*bearer_uci)(struct bt_ccp_call_control_client_bearer *bearer, int err,
                           const char *uci, void *user_data);
#endif /* CONFIG_BT_TBS_CLIENT_BEARER_UCI */

#if defined(CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY) || defined(__DOXYGEN__)
        void (*bearer_tech)(struct bt_ccp_call_control_client_bearer *bearer, int err,
                            enum bt_bearer_tech tech, void *user_data);
#endif /* CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY */

#if defined(CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST) || defined(__DOXYGEN__)
        void (*bearer_uri_schemes)(struct bt_ccp_call_control_client_bearer *bearer, int err,
                                   const char *uri_schemes, void *user_data);
#endif /* CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST */

#if defined(CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA) || defined(__DOXYGEN__)
        void *user_data;
#endif /* CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA */

        sys_snode_t _node;
};

int bt_ccp_call_control_client_discover(struct bt_conn *conn,
                                        struct bt_ccp_call_control_client **out_client);

int bt_ccp_call_control_client_register_cb(struct bt_ccp_call_control_client_cb *cb);

int bt_ccp_call_control_client_unregister_cb(struct bt_ccp_call_control_client_cb *cb);

int bt_ccp_call_control_client_get_bearers(struct bt_ccp_call_control_client *client,
                                           struct bt_ccp_call_control_client_bearers *bearers);

int bt_ccp_call_control_client_read_bearer_provider_name(
        struct bt_ccp_call_control_client_bearer *bearer);

int bt_ccp_call_control_client_read_bearer_uci(struct bt_ccp_call_control_client_bearer *bearer);

int bt_ccp_call_control_client_read_bearer_tech(struct bt_ccp_call_control_client_bearer *bearer);

int bt_ccp_call_control_client_read_bearer_uri_schemes(
        struct bt_ccp_call_control_client_bearer *bearer); /* End of group bt_ccp_call_control_client */
#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCP_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2024-2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 207 行

`bt_ccp_call_control_server` 分组结束。

### 注释 3：原第 233 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_GTBS`。

### 注释 4：原第 242 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_TBS`。

### 注释 5：原第 284 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME`。

### 注释 6：原第 302 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_BEARER_UCI`。

### 注释 7：原第 321 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY`。

### 注释 8：原第 341 行

条件编译配置（Configuration）标记：`CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST`。

### 注释 9：原第 346 行

条件编译配置（Configuration）标记：`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA`。

### 注释 10：原第 481 行

`bt_ccp_call_control_client` 分组结束。

### 注释 11：原第 491 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCP_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)
- [bt_ccp_call_control_server_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [bt_ccp_call_control_server_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaa2486dec8a47bd7f4cd4076477e8ac4a)
- [bt_ccp_call_control_server_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaae263e42d76d99d950ac535c22fe64c2)
- [bt_ccp_call_control_server_get_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga0b775c233dcfd08f57322afaf6fa9bcf)
- [bt_ccp_call_control_server_get_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga4c250633e8a9ff479952f9300c8eeddd)
- [BT_TBS_MAX_UCI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga42b72d7aef36cc7ea0d5dd4ec3d7a717)
- [bt_ccp_call_control_server_set_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gac670cf57d2f02df44ea0d82a58524242)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_ccp_call_control_server_get_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga84efc07e1703536ad6a005b5c5d9fb16)
- [bt_ccp_call_control_server_set_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaf7880d2e467b0931d894231312b7ed9b)
- [bt_ccp_call_control_server_get_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gad8525ac242806efd70d6adbd0148a0ba)
- [bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)
- [bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)
- [bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)
- [gtbs_bearer](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a0d5936c39146ec97875c01a6d6bf1b26)
- [tbs_count](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a100c4024c0086016ec87bc9feebacc52)
- [tbs_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a1574714c19259a291c4557c0176462a4)
- [bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a4ad442e0f84327a7d02b5bfd5bbf09c7)
- [user_data](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a1d4af4ea50002e2f3d24ed0d4bf21d83)
- [bearer_provider_name](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a3830ba768a1300df7aee272a2d3ec00e)
- [bearer_uci](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#aed9802f73963157a9f45ee35e50ad8ac)
- [bearer_tech](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#aba44cdf2667ca7622d7a8c70164cd847)
- [bearer_uri_schemes](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a3c6d22aefdbef40ac42fb05e9656789a)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_ccp_call_control_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga2a5bce65e39ba05625423308f996021d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_ccp_call_control_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga8c5c3907759fe02745339b9456cca05f)
- [bt_ccp_call_control_client_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga534a15db3e87d63942de6ba4bd8377db)
- [bt_ccp_call_control_client_get_bearers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac8aa850b1e77bff1058e63be8c07c4c8)
- [bt_ccp_call_control_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga31455b659d7b20053624f79c71cefa84)
- [bt_ccp_call_control_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac106a4de174d941e6390a1743d11f01d)
- [bt_ccp_call_control_client_read_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gaf8df0504479ac519328d98f2ddf6db15)
- [bt_ccp_call_control_client_read_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga9b146acb76b6e40ae639da92c5d50941)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_ccp_call_control_client_bearers::gtbs_bearer](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a0d5936c39146ec97875c01a6d6bf1b26)
- [bt_ccp_call_control_client_bearers::tbs_count](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a100c4024c0086016ec87bc9feebacc52)
- [bt_ccp_call_control_client_bearers::tbs_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md#a1574714c19259a291c4557c0176462a4)
- [bt_ccp_call_control_client_cb::user_data](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a1d4af4ea50002e2f3d24ed0d4bf21d83)
- [bt_ccp_call_control_client_cb::bearer_provider_name](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a3830ba768a1300df7aee272a2d3ec00e)
- [bt_ccp_call_control_client_cb::bearer_uri_schemes](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a3c6d22aefdbef40ac42fb05e9656789a)
- [bt_ccp_call_control_client_cb::discover](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#a4ad442e0f84327a7d02b5bfd5bbf09c7)
- [bt_ccp_call_control_client_cb::bearer_tech](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#aba44cdf2667ca7622d7a8c70164cd847)
- [bt_ccp_call_control_client_cb::bearer_uci](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md#aed9802f73963157a9f45ee35e50ad8ac)
- [tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html)

---

[上一章](P009_cc1200.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_cfg.h_源码浏览.md)
