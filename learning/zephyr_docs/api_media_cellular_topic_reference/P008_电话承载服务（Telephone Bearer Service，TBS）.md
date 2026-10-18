---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-8
title: 电话承载服务（Telephone Bearer Service，TBS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_电话承载服务（Telephone Bearer Service，TBS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话承载服务（Telephone Bearer Service，TBS）

<a id="details"></a>

电话承载服务（Telephone Bearer Service，TBS）。自 3.0 引入，版本 0.8.0。TBS 提供发现电话承载（Telephone Bearers）和控制呼叫（Calls）的过程。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_bt_5Ftbs_5Fcb"></a>

```c
struct bt_tbs_cb
```

相关声明：[bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service）回调的结构。

<a id="r_bt_5Ftbs_5Fregister_5Fparam"></a>

```c
struct bt_tbs_register_param
```

相关声明：[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)。

注册电话承载服务（Telephone Bearer Service）的参数。

<a id="r_bt_5Ftbs_5Fclient_5Fcall_5Fstate"></a>

```c
struct bt_tbs_client_call_state
```

相关声明：[bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)。

保存呼叫状态（Call State）的结构。

<a id="r_bt_5Ftbs_5Fclient_5Fcall"></a>

```c
struct bt_tbs_client_call
```

相关声明：[bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)。

电话承载服务客户端（Telephone Bearer Service Client）保存一次呼叫的结构。

<a id="r_bt_5Ftbs_5Fclient_5Fcb"></a>

```c
struct bt_tbs_client_cb
```

相关声明：[bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

<a id="r_bt_5Ftbs_5Finstance"></a>

```c
struct bt_tbs_instance
```

相关声明：[bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)。

不透明的电话承载服务（Telephone Bearer Service）实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_gaeb2eadb4f5559f55734797a4d700e2fe"></a>

```c
#define BT_TBS_ERR_VAL_CHANGED 0x80U
```

相关声明：[BT_TBS_ERR_VAL_CHANGED](#gaeb2eadb4f5559f55734797a4d700e2fe)。

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="r_ga25aa807f2e3a01d030edf4f064a4fbfd"></a>

```c
#define BT_TBS_GTBS_INDEX 0xFFU
```

相关声明：[BT_TBS_GTBS_INDEX](#ga25aa807f2e3a01d030edf4f064a4fbfd)。

GTBS 索引表示回调来自通用电话承载服务（Generic Telephone Bearer Service，GTBS）实例，或者表示客户端应对服务器的 GTBS 实例执行动作，而非对某个特定电话承载服务（Telephone Bearer Service）实例执行动作。

<a id="r_ga42b72d7aef36cc7ea0d5dd4ec3d7a717"></a>

```c
#define BT_TBS_MAX_UCI_SIZE 6U
```

相关声明：[BT_TBS_MAX_UCI_SIZE](#ga42b72d7aef36cc7ea0d5dd4ec3d7a717)。

承载统一呼叫者标识符（Bearer Uniform Caller Identifier，UCI）的最大大小。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga60e9e143f247bb7e668293f0233ce300"></a>

```c
typedef bool(* bt_tbs_originate_call_cb) (struct bt_conn *conn, uint8_t call_index, const char *uri)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_tbs_originate_call_cb](#ga60e9e143f247bb7e668293f0233ce300)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端发起呼叫（Originating a Call）的回调函数。

<a id="r_ga69e93b48b2a48e8a6552882660b791cc"></a>

```c
typedef void(* bt_tbs_terminate_call_cb) (struct bt_conn *conn, uint8_t call_index, uint8_t reason)
```

相关声明：[bt_tbs_terminate_call_cb](#ga69e93b48b2a48e8a6552882660b791cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端终止呼叫（Terminating a Call）的回调函数。

<a id="r_gaa45b3f4837165d722c2df6f202a39058"></a>

```c
typedef void(* bt_tbs_join_calls_cb) (struct bt_conn *conn, uint8_t call_index_count, const uint8_t *call_indexes)
```

相关声明：[bt_tbs_join_calls_cb](#gaa45b3f4837165d722c2df6f202a39058)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端合并呼叫（Joining Calls）的回调函数。

<a id="r_ga2fa85f3cd96f25f6bb4f449fc9210fa1"></a>

```c
typedef void(* bt_tbs_call_change_cb) (struct bt_conn *conn, uint8_t call_index)
```

相关声明：[bt_tbs_call_change_cb](#ga2fa85f3cd96f25f6bb4f449fc9210fa1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端请求改变呼叫状态（Call State Change）的回调函数。

<a id="r_ga1cc9e7140531b07bf6a8dedbc17f24c0"></a>

```c
typedef bool(* bt_tbs_authorize_cb) (struct bt_conn *conn)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_tbs_authorize_cb](#ga1cc9e7140531b07bf6a8dedbc17f24c0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

授权客户端（Authorizing a Client）的回调函数。

<a id="r_ga9cac11cc696be9fb387f2f7685e0d8a7"></a>

```c
typedef void(* bt_tbs_client_discover_cb) (struct bt_conn *conn, int err, uint8_t tbs_count, bool gtbs_found)
```

相关声明：[bt_tbs_client_discover_cb](#ga9cac11cc696be9fb387f2f7685e0d8a7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

ccp_discover 的回调函数（Callback Function）。

<a id="r_gaf77231168e4444da7aef203cc9eaca95"></a>

```c
typedef void(* bt_tbs_client_write_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index)
```

相关声明：[bt_tbs_client_write_value_cb](#gaf77231168e4444da7aef203cc9eaca95)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向对端设备写入值（Writing Values）的回调函数。

<a id="r_ga40b8b3d1b318a1b5c5524877bbc2f90f"></a>

```c
typedef void(* bt_tbs_client_cp_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_cp_cb](#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

CCP 呼叫控制函数（Call Control Functions）的回调函数。

<a id="r_ga4d7632de7c2006e478880950076908a9"></a>

```c
typedef void(* bt_tbs_client_read_string_cb) (struct bt_conn *conn, int err, uint8_t inst_index, const char *value)
```

相关声明：[bt_tbs_client_read_string_cb](#ga4d7632de7c2006e478880950076908a9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取字符串值（String Value）的函数使用的回调函数。

<a id="r_ga600051910ed538a2da823554df23dd20"></a>

```c
typedef void(* bt_tbs_client_read_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint32_t value)
```

相关声明：[bt_tbs_client_read_value_cb](#ga600051910ed538a2da823554df23dd20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取整数值（Integer Value）的函数使用的回调函数。

<a id="r_gab881b3caaaa4425e52afd84e53adee78"></a>

```c
typedef void(* bt_tbs_client_termination_reason_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index, uint8_t reason)
```

相关声明：[bt_tbs_client_termination_reason_cb](#gab881b3caaaa4425e52afd84e53adee78)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

ccp_read_termination_reason 的回调函数（Callback Function）。

<a id="r_ga7b31e1c30fa96081a3ef38e1a481b64f"></a>

```c
typedef void(* bt_tbs_client_current_calls_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call *calls)
```

相关声明：[bt_tbs_client_current_calls_cb](#ga7b31e1c30fa96081a3ef38e1a481b64f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)。

ccp_read_current_calls 的回调函数（Callback Function）。

<a id="r_ga262ca74b7ae2f0c52657066549fa4f92"></a>

```c
typedef void(* bt_tbs_client_call_states_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call_state *call_states)
```

相关声明：[bt_tbs_client_call_states_cb](#ga262ca74b7ae2f0c52657066549fa4f92)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)。

ccp_read_call_state 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_ga1b942bcf8287641f9cd53824b4d6e77b"></a>

```c
int bt_tbs_accept (uint8_t call_index)
```

相关声明：[bt_tbs_accept](#ga1b942bcf8287641f9cd53824b4d6e77b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接听正在振铃的呼叫（Alerting Call）。

<a id="r_gab72044a1f5466114b5efb88dfcd2f097"></a>

```c
int bt_tbs_hold (uint8_t call_index)
```

相关声明：[bt_tbs_hold](#gab72044a1f5466114b5efb88dfcd2f097)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

保持呼叫（Hold a Call）。

<a id="r_gad0b45af09b82d6cd66a8481c0e67e04e"></a>

```c
int bt_tbs_retrieve (uint8_t call_index)
```

相关声明：[bt_tbs_retrieve](#gad0b45af09b82d6cd66a8481c0e67e04e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

恢复呼叫（Retrieve a Call）。

<a id="r_ga82553640882ac74f9af84bfe09ff47ee"></a>

```c
int bt_tbs_terminate (uint8_t call_index)
```

相关声明：[bt_tbs_terminate](#ga82553640882ac74f9af84bfe09ff47ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

终止呼叫（Terminate a Call）。

<a id="r_gadeae51d7cecd80abcdcde1195bb1dfba"></a>

```c
int bt_tbs_originate (uint8_t bearer_index, char *uri, uint8_t *call_index)
```

相关声明：[bt_tbs_originate](#gadeae51d7cecd80abcdcde1195bb1dfba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发起呼叫（Originate a Call）。

<a id="r_ga23226d41e3b98a53ec9a9c2fa346c9ac"></a>

```c
int bt_tbs_join (uint8_t call_index_cnt, uint8_t *call_indexes)
```

相关声明：[bt_tbs_join](#ga23226d41e3b98a53ec9a9c2fa346c9ac)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

合并呼叫（Join Calls）。

<a id="r_ga868b83450f7425e8a0c8cfb7c1de45d8"></a>

```c
int bt_tbs_remote_answer (uint8_t call_index)
```

相关声明：[bt_tbs_remote_answer](#ga868b83450f7425e8a0c8cfb7c1de45d8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已接听呼叫（Answered the Call）。

<a id="r_ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e"></a>

```c
int bt_tbs_remote_hold (uint8_t call_index)
```

相关声明：[bt_tbs_remote_hold](#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已保持呼叫（Held the Call）。

<a id="r_ga09a3e64040819b6b8b694b94d2f62ca0"></a>

```c
int bt_tbs_remote_retrieve (uint8_t call_index)
```

相关声明：[bt_tbs_remote_retrieve](#ga09a3e64040819b6b8b694b94d2f62ca0)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已恢复呼叫（Retrieved the Call）。

<a id="r_ga52afc7b8a22b071dbac10057579f319c"></a>

```c
int bt_tbs_remote_terminate (uint8_t call_index)
```

相关声明：[bt_tbs_remote_terminate](#ga52afc7b8a22b071dbac10057579f319c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已终止呼叫（Terminated the Call）。

<a id="r_ga47939f557e4d6503af9b7b85aff9d60f"></a>

```c
int bt_tbs_remote_incoming (uint8_t bearer_index, const char *to, const char *from, const char *friendly_name)
```

相关声明：[bt_tbs_remote_incoming](#ga47939f557e4d6503af9b7b85aff9d60f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向服务器通知来电（Incoming Call）。

<a id="r_ga5118db6b23b387956e75eda8aecd53d5"></a>

```c
int bt_tbs_set_bearer_provider_name (uint8_t bearer_index, const char *name)
```

相关声明：[bt_tbs_set_bearer_provider_name](#ga5118db6b23b387956e75eda8aecd53d5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置新的承载提供者（Bearer Provider）。

<a id="r_gaa77ea977fca9833d1755d5084a3f352c"></a>

```c
int bt_tbs_set_bearer_technology (uint8_t bearer_index, enum bt_bearer_tech new_technology)
```

相关声明：[bt_tbs_set_bearer_technology](#gaa77ea977fca9833d1755d5084a3f352c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

设置新的承载技术（Bearer Technology）。

<a id="r_gac316adedf7fda441ee55feb9d24d1a94"></a>

```c
int bt_tbs_set_signal_strength (uint8_t bearer_index, uint8_t new_signal_strength)
```

相关声明：[bt_tbs_set_signal_strength](#gac316adedf7fda441ee55feb9d24d1a94)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新服务器报告的信号强度（Signal Strength）。

<a id="r_ga838e51a85f9833e0822090cd3df09e00"></a>

```c
int bt_tbs_set_status_flags (uint8_t bearer_index, uint16_t status_flags)
```

相关声明：[bt_tbs_set_status_flags](#ga838e51a85f9833e0822090cd3df09e00)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置特性与状态值（Feature and Status Value）。

<a id="r_gae413f94b141b6fa8233de15c36f6327a"></a>

```c
int bt_tbs_set_uri_scheme_list (uint8_t bearer_index, const char *uri_scheme_list)
```

相关声明：[bt_tbs_set_uri_scheme_list](#gae413f94b141b6fa8233de15c36f6327a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置承载的 URI 方案列表（URI Scheme List）。

<a id="r_ga76f120dba549225a6f2c2c22be08edfc"></a>

```c
void bt_tbs_register_cb (struct bt_tbs_cb *cbs)
```

相关声明：[bt_tbs_register_cb](#ga76f120dba549225a6f2c2c22be08edfc)、[bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)。

注册电话承载服务（TBS）的回调。

<a id="r_ga970c970bedd6e94aa4c92479183554e9"></a>

```c
int bt_tbs_register_bearer (const struct bt_tbs_register_param *param)
```

相关声明：[bt_tbs_register_bearer](#ga970c970bedd6e94aa4c92479183554e9)、[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)。

注册电话承载（Telephone Bearer）。

<a id="r_ga8edd4d31478ed9e0aedbd1a34bdfca96"></a>

```c
int bt_tbs_unregister_bearer (uint8_t bearer_index)
```

相关声明：[bt_tbs_unregister_bearer](#ga8edd4d31478ed9e0aedbd1a34bdfca96)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销电话承载（Telephone Bearer）。

<a id="r_ga62f5008cbfba158fe399cfaf683d1d2e"></a>

```c
void bt_tbs_dbg_print_calls (void)
```

相关声明：[bt_tbs_dbg_print_calls](#ga62f5008cbfba158fe399cfaf683d1d2e)。

将所有服务的全部呼叫（Calls）打印到调试日志。

<a id="r_gac59f3dec092a14bdf234039e3dcd12eb"></a>

```c
int bt_tbs_client_discover (struct bt_conn *conn)
```

相关声明：[bt_tbs_client_discover](#gac59f3dec092a14bdf234039e3dcd12eb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现某个连接上的电话承载服务（TBS）。

<a id="r_ga3a71c51d464aa19fbfbd2d60fc4901bc"></a>

```c
int bt_tbs_client_set_outgoing_uri (struct bt_conn *conn, uint8_t inst_index, const char *uri)
```

相关声明：[bt_tbs_client_set_outgoing_uri](#ga3a71c51d464aa19fbfbd2d60fc4901bc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置对端设备上 TBS 实例的呼出 URI（Outgoing URI）。

<a id="r_gaa1dcb9908057d75a54fa447639826f3c"></a>

```c
int bt_tbs_client_set_signal_strength_interval (struct bt_conn *conn, uint8_t inst_index, uint8_t interval)
```

相关声明：[bt_tbs_client_set_signal_strength_interval](#gaa1dcb9908057d75a54fa447639826f3c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

<a id="r_ga0aac704008ffc92ce6609d3ffffc4523"></a>

```c
int bt_tbs_client_originate_call (struct bt_conn *conn, uint8_t inst_index, const char *uri)
```

相关声明：[bt_tbs_client_originate_call](#ga0aac704008ffc92ce6609d3ffffc4523)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求发起呼叫（Originate a Call）。

<a id="r_ga25b803bb5cae2e1a8b0398bc48137d80"></a>

```c
int bt_tbs_client_terminate_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_terminate_call](#ga25b803bb5cae2e1a8b0398bc48137d80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求终止呼叫（Terminate a Call）。

<a id="r_ga23e825de6af71d4e456b63c3a621fb61"></a>

```c
int bt_tbs_client_hold_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_hold_call](#ga23e825de6af71d4e456b63c3a621fb61)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求保持呼叫（Hold a Call）。

<a id="r_ga625fc73885c2bfd63f0f4b2d7f72eaef"></a>

```c
int bt_tbs_client_accept_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_accept_call](#ga625fc73885c2bfd63f0f4b2d7f72eaef)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接听来电（Incoming Call）。

<a id="r_gabbe194a63da0b95dc1dca0337560a585"></a>

```c
int bt_tbs_client_retrieve_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_retrieve_call](#gabbe194a63da0b95dc1dca0337560a585)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从本地保持状态恢复呼叫（Retrieve Call from Local Hold）。

<a id="r_gaae1925deb0b5865af601aa8278ffb10a"></a>

```c
int bt_tbs_client_join_calls (struct bt_conn *conn, uint8_t inst_index, const uint8_t *call_indexes, uint8_t count)
```

相关声明：[bt_tbs_client_join_calls](#gaae1925deb0b5865af601aa8278ffb10a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

合并多个呼叫（Join Multiple Calls）。

<a id="r_ga2053a9eb7cf28f66febd365f0b682be0"></a>

```c
int bt_tbs_client_read_bearer_provider_name (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_bearer_provider_name](#ga2053a9eb7cf28f66febd365f0b682be0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的承载提供者名称（Bearer Provider Name）。

<a id="r_gaba92039d3b44da9163a22400951fafa7"></a>

```c
int bt_tbs_client_read_bearer_uci (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_bearer_uci](#gaba92039d3b44da9163a22400951fafa7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的统一呼叫者标识符（UCI）。

<a id="r_ga7684dbcb78e407f7002d44fbdb805e5d"></a>

```c
int bt_tbs_client_read_technology (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_technology](#ga7684dbcb78e407f7002d44fbdb805e5d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的技术类型（Technology）。

<a id="r_gad19db25591c7ae5bd0b4c2bbaefc9bed"></a>

```c
int bt_tbs_client_read_uri_list (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_uri_list](#gad19db25591c7ae5bd0b4c2bbaefc9bed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的 URI 方案列表（URI Schemes List）。

<a id="r_gaabe97df55817b8e36c79de4bf30fc83f"></a>

```c
int bt_tbs_client_read_signal_strength (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_signal_strength](#gaabe97df55817b8e36c79de4bf30fc83f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的当前信号强度（Signal Strength）。

<a id="r_ga38046c5c715d451b21a3076742268010"></a>

```c
int bt_tbs_client_read_signal_interval (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_signal_interval](#ga38046c5c715d451b21a3076742268010)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

<a id="r_ga895c7f54300e5452fb8d0c9d4b3306ae"></a>

```c
int bt_tbs_client_read_current_calls (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_current_calls](#ga895c7f54300e5452fb8d0c9d4b3306ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的当前呼叫列表（Current Calls List）。

<a id="r_gac070ec0590df5820b7721d579ceeeb15"></a>

```c
int bt_tbs_client_read_ccid (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_ccid](#gac070ec0590df5820b7721d579ceeeb15)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的内容 ID（Content ID）。

<a id="r_ga4238a37b80b7d7ff611fe9b02b7cf54d"></a>

```c
int bt_tbs_client_read_call_uri (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_call_uri](#ga4238a37b80b7d7ff611fe9b02b7cf54d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的呼叫目标 URI（Call Target URI）。

<a id="r_ga9fe91df1a31ce59401347fc0eac2b701"></a>

```c
int bt_tbs_client_read_status_flags (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_status_flags](#ga9fe91df1a31ce59401347fc0eac2b701)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的特性与状态值（Feature and Status Value）。

<a id="r_gafeaaaefb9d4eb773dd0cbdfebe26e0b7"></a>

```c
int bt_tbs_client_read_call_state (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_call_state](#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例当前呼叫的状态（Call States）。

<a id="r_gab04f8355c32fce501bd757b75ee9d38a"></a>

```c
int bt_tbs_client_read_remote_uri (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_remote_uri](#gab04f8355c32fce501bd757b75ee9d38a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的远端 URI（Remote URI）。

<a id="r_ga99549dd6244580e157006fb17772fd8f"></a>

```c
int bt_tbs_client_read_friendly_name (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_friendly_name](#ga99549dd6244580e157006fb17772fd8f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例中某个呼叫的友好名称（Friendly Name）。

<a id="r_gaf504e1a11352d77a36aa087b587e4ba8"></a>

```c
int bt_tbs_client_read_optional_opcodes (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_optional_opcodes](#gaf504e1a11352d77a36aa087b587e4ba8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例支持的操作码（Supported Opcode）。

<a id="r_gabe2251d4ea88306793dc68ae683886bb"></a>

```c
int bt_tbs_client_register_cb (struct bt_tbs_client_cb *cbs)
```

相关声明：[bt_tbs_client_register_cb](#gabe2251d4ea88306793dc68ae683886bb)、[bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)。

注册呼叫控制配置文件（CCP）的回调。

<a id="r_gaadae501fa6f7771bb9661af829805a5f"></a>

```c
struct bt_tbs_instance * bt_tbs_client_get_by_ccid (const struct bt_conn *conn, uint8_t ccid)
```

相关声明：[bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)、[bt_tbs_client_get_by_ccid](#gaadae501fa6f7771bb9661af829805a5f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据 CCID 查找电话承载服务实例（Telephone Bearer Service Instance）。

<a id="r_ga20c6780a4624707a537e905e889510ca"></a>

```c
struct bt_tbs_instance * bt_tbs_client_get_by_index (const struct bt_conn *conn, uint8_t index)
```

相关声明：[bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)、[bt_tbs_client_get_by_index](#ga20c6780a4624707a537e905e889510ca)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据索引查找电话承载服务实例（Telephone Bearer Service Instance）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 8.5\_呼叫状态（Call States）

<a id="r_ga829309945831c0e8ac36c3dd79ae26f3"></a>

```c
#define BT_TBS_CALL_STATE_INCOMING 0x00U
```

相关声明：[BT_TBS_CALL_STATE_INCOMING](#ga829309945831c0e8ac36c3dd79ae26f3)。

远端正在呼叫，即来电（Incoming Call）。

<a id="r_ga482f9627308cad1e56a4a5a5906c2308"></a>

```c
#define BT_TBS_CALL_STATE_DIALING 0x01U
```

相关声明：[BT_TBS_CALL_STATE_DIALING](#ga482f9627308cad1e56a4a5a5906c2308)。

服务器已开始呼叫远端，但尚未提醒远端，即呼出（Outgoing Call）。

<a id="r_gada61fd749f2119452429dd712d283dad"></a>

```c
#define BT_TBS_CALL_STATE_ALERTING 0x02U
```

相关声明：[BT_TBS_CALL_STATE_ALERTING](#gada61fd749f2119452429dd712d283dad)。

正在提醒远端，即呼出（Outgoing Call）。

<a id="r_ga3100ab7a7db823d86198847ec0df4adc"></a>

```c
#define BT_TBS_CALL_STATE_ACTIVE 0x03U
```

相关声明：[BT_TBS_CALL_STATE_ACTIVE](#ga3100ab7a7db823d86198847ec0df4adc)。

呼叫正在通话（Active Conversation）。

<a id="r_gac900fe331fe5b81d7ed0b21796d3e16c"></a>

```c
#define BT_TBS_CALL_STATE_LOCALLY_HELD 0x04U
```

相关声明：[BT_TBS_CALL_STATE_LOCALLY_HELD](#gac900fe331fe5b81d7ed0b21796d3e16c)。

呼叫已连接，但被本地保持（Held Locally）。

<a id="r_ga76acd3539931a32361fd0deb3bbe8243"></a>

```c
#define BT_TBS_CALL_STATE_REMOTELY_HELD 0x05U
```

相关声明：[BT_TBS_CALL_STATE_REMOTELY_HELD](#ga76acd3539931a32361fd0deb3bbe8243)。

呼叫已连接，但被远端保持（Held Remotely）。

<a id="r_ga0d28984faadc6904f72068df6ab6c97d"></a>

```c
#define BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD 0x06U
```

相关声明：[BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD](#ga0d28984faadc6904f72068df6ab6c97d)。

呼叫已连接，但同时被本地和远端保持（Held Locally and Remotely）。

## 8.6\_终止原因（Terminate Reason）

<a id="r_gaf7f2abd7e794806ab6b119bee47db6c6"></a>

```c
#define BT_TBS_REASON_BAD_REMOTE_URI 0x00U
```

相关声明：[BT_TBS_REASON_BAD_REMOTE_URI](#gaf7f2abd7e794806ab6b119bee47db6c6)。

用于发起呼叫（Originate a Call）的 URI 值格式不正确。

<a id="r_gacd5a09f5786e01662e29d49aa5307046"></a>

```c
#define BT_TBS_REASON_CALL_FAILED 0x01U
```

相关声明：[BT_TBS_REASON_CALL_FAILED](#gacd5a09f5786e01662e29d49aa5307046)。

呼叫失败（Call Failed）。

<a id="r_ga4bc073b85c6eca1f0a4b0757e1050dde"></a>

```c
#define BT_TBS_REASON_REMOTE_ENDED_CALL 0x02U
```

相关声明：[BT_TBS_REASON_REMOTE_ENDED_CALL](#ga4bc073b85c6eca1f0a4b0757e1050dde)。

远端结束了呼叫（Call）。

<a id="r_gaa4f89b5fa61dcc4ee7e4fb6ae0e12384"></a>

```c
#define BT_TBS_REASON_SERVER_ENDED_CALL 0x03U
```

相关声明：[BT_TBS_REASON_SERVER_ENDED_CALL](#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)。

服务器端结束了呼叫（Call）。

<a id="r_ga3105e7b0b91b71eb55c1ea5c3bfd6df3"></a>

```c
#define BT_TBS_REASON_LINE_BUSY 0x04U
```

相关声明：[BT_TBS_REASON_LINE_BUSY](#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)。

线路忙（Line Busy）。

<a id="r_gae195db56d2cd949a29d261c5473eea89"></a>

```c
#define BT_TBS_REASON_NETWORK_CONGESTED 0x05U
```

相关声明：[BT_TBS_REASON_NETWORK_CONGESTED](#gae195db56d2cd949a29d261c5473eea89)。

网络拥塞（Network Congestion）。

<a id="r_ga614adc266444030ac83dc6f4d2e89563"></a>

```c
#define BT_TBS_REASON_CLIENT_TERMINATED 0x06U
```

相关声明：[BT_TBS_REASON_CLIENT_TERMINATED](#ga614adc266444030ac83dc6f4d2e89563)。

客户端终止了呼叫（Call）。

<a id="r_ga137b813cf902c8209a624c6ae8d4a93b"></a>

```c
#define BT_TBS_REASON_NO_SERVICE 0x07U
```

相关声明：[BT_TBS_REASON_NO_SERVICE](#ga137b813cf902c8209a624c6ae8d4a93b)。

无服务（No Service）。

<a id="r_ga893d3c79ca62c5e5487d7ca7cd403ce2"></a>

```c
#define BT_TBS_REASON_NO_ANSWER 0x08U
```

相关声明：[BT_TBS_REASON_NO_ANSWER](#ga893d3c79ca62c5e5487d7ca7cd403ce2)。

无人应答（No Answer）。

<a id="r_gaa4dab0b5c08dcf092a125986519a7d55"></a>

```c
#define BT_TBS_REASON_UNSPECIFIED 0x09U
```

相关声明：[BT_TBS_REASON_UNSPECIFIED](#gaa4dab0b5c08dcf092a125986519a7d55)。

未指定（Unspecified）。

## 8.7\_控制点错误码（Control point error codes）

<a id="r_gaa92fdb19227ee0b268f2395f3f6a5f63"></a>

```c
#define BT_TBS_RESULT_CODE_SUCCESS 0x00U
```

相关声明：[BT_TBS_RESULT_CODE_SUCCESS](#gaa92fdb19227ee0b268f2395f3f6a5f63)。

操作码写入（Opcode Write）成功。

<a id="r_gafac3c970b36f37c815c4370dfef89f09"></a>

```c
#define BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED 0x01U
```

相关声明：[BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED](#gafac3c970b36f37c815c4370dfef89f09)。

写入呼叫控制点（Call Control Point）时使用了无效操作码。

<a id="r_gae83a73a5a0474a62dfbcb5ced6eb3f78"></a>

```c
#define BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE 0x02U
```

相关声明：[BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE](#gae83a73a5a0474a62dfbcb5ced6eb3f78)。

无法完成请求的操作（Requested Operation）。

<a id="r_gadc371a3a898b3ecac56d8778109f315d"></a>

```c
#define BT_TBS_RESULT_CODE_INVALID_CALL_INDEX 0x03U
```

相关声明：[BT_TBS_RESULT_CODE_INVALID_CALL_INDEX](#gadc371a3a898b3ecac56d8778109f315d)。

写入呼叫控制点（Call Control Point）时使用的呼叫索引（Call Index）无效。

<a id="r_ga3fa49179525369502018912115c1ccce"></a>

```c
#define BT_TBS_RESULT_CODE_STATE_MISMATCH 0x04U
```

相关声明：[BT_TBS_RESULT_CODE_STATE_MISMATCH](#ga3fa49179525369502018912115c1ccce)。

收到写入呼叫控制点（Call Control Point）的操作码时，该呼叫索引（Call Index）对应的当前呼叫状态（Call State）并非预期状态。

<a id="r_ga148585f5cfe8b1cd7f8db404dac91cdd"></a>

```c
#define BT_TBS_RESULT_CODE_OUT_OF_RESOURCES 0x05U
```

相关声明：[BT_TBS_RESULT_CODE_OUT_OF_RESOURCES](#ga148585f5cfe8b1cd7f8db404dac91cdd)。

内部资源不足，无法完成请求的动作（Requested Action）。

<a id="r_gaa60f75b90f461246b2f470930a60efc2"></a>

```c
#define BT_TBS_RESULT_CODE_INVALID_URI 0x06U
```

相关声明：[BT_TBS_RESULT_CODE_INVALID_URI](#gaa60f75b90f461246b2f470930a60efc2)。

发送发起呼叫（Originate）操作码时，呼出 URI（Outgoing URI）不正确或无效。

## 8.8\_可选操作码位（Optional opcodes bits）

可以支持的可选操作码（Optional Opcodes）。

有关如何从远端设备读取这些值，参见 bt_tbs_client_read_optional_opcodes()。

<a id="r_gaf13a663330c8d1902765c208c028ee50"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_HOLD BIT(0U)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_HOLD](#gaf13a663330c8d1902765c208c028ee50)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持呼叫控制点的本地保持（Local Hold）和本地恢复（Local Retrieve）操作码。

<a id="r_ga06f41e27d2dfc92f31306938005a9058"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_JOIN BIT(1U)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_JOIN](#ga06f41e27d2dfc92f31306938005a9058)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持呼叫控制点的合并（Join）操作码。

<a id="r_ga07a7bad80edea037cba34198c5c9c193"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_ALL (BT_TBS_OPTIONAL_OPCODE_HOLD | BT_TBS_OPTIONAL_OPCODE_JOIN)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_ALL](#ga07a7bad80edea037cba34198c5c9c193)、[BT_TBS_OPTIONAL_OPCODE_HOLD](#gaf13a663330c8d1902765c208c028ee50)、[BT_TBS_OPTIONAL_OPCODE_JOIN](#ga06f41e27d2dfc92f31306938005a9058)。

支持全部控制点操作码（Control Point Opcodes）。

## 8.9\_信号强度值界限（Signal strength value limits）

<a id="r_ga310c1cdffee350fe5235b3ad929ac715"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_NO_SERVICE 0U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_NO_SERVICE](#ga310c1cdffee350fe5235b3ad929ac715)。

无服务（No Service）。

<a id="r_gae619d9096b41690ba77ee3e7bd838be3"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_MAX 100U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_MAX](#gae619d9096b41690ba77ee3e7bd838be3)。

最大信号强度（Maximum Signal Strength）。

<a id="r_gab8a433da27a61cf1c7be2fc7b006e298"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_UNKNOWN 255U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_UNKNOWN](#gab8a433da27a61cf1c7be2fc7b006e298)。

信号强度未知（Unknown Signal Strength）。

## 8.10\_呼叫状态标志位域（Call status flags bitfield）

<a id="r_gadc590b9f5813e190fa14644412aee25c"></a>

```c
#define BT_TBS_STATUS_FLAG_INBAND_RINGTONE BIT(0U)
```

相关声明：[BT_TBS_STATUS_FLAG_INBAND_RINGTONE](#gadc590b9f5813e190fa14644412aee25c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

已启用带内铃声（Inband Ringtone）。

<a id="r_ga53dfa36830f8c562711d9c6f9111929e"></a>

```c
#define BT_TBS_STATUS_FLAG_SILENT_MOD BIT(1U)
```

相关声明：[BT_TBS_STATUS_FLAG_SILENT_MOD](#ga53dfa36830f8c562711d9c6f9111929e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

服务器处于静音模式（Silent Mode；原文写作 silent mod）。

## 8.11\_呼叫标志位域（Call flags bitfield）

<a id="r_ga74344c01327304f1d2da050ddc589735"></a>

```c
#define BT_TBS_CALL_FLAG_OUTGOING BIT(0U)
```

相关声明：[BT_TBS_CALL_FLAG_OUTGOING](#ga74344c01327304f1d2da050ddc589735)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼出（Outgoing），否则表示来电（Incoming）。

<a id="r_ga25ff3c36aaabc5e37b08acc62ac21be6"></a>

```c
#define BT_TBS_CALL_FLAG_WITHHELD BIT(1U)
```

相关声明：[BT_TBS_CALL_FLAG_WITHHELD](#ga25ff3c36aaabc5e37b08acc62ac21be6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼叫信息被隐藏（Withheld），否则未隐藏。

<a id="r_ga466c1c3c50e82fee9e5c8323e89be414"></a>

```c
#define BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK BIT(2U)
```

相关声明：[BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK](#ga466c1c3c50e82fee9e5c8323e89be414)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼叫信息被网络隐藏（Withheld by Network），否则由网络提供。

## 8.12\_详细说明（Detailed Documentation）

<a id="ga74344c01327304f1d2da050ddc589735"></a>

### `BT_TBS_CALL_FLAG_OUTGOING`

```c
#define BT_TBS_CALL_FLAG_OUTGOING BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置时表示呼出（Outgoing），否则表示来电（Incoming）。

<a id="ga25ff3c36aaabc5e37b08acc62ac21be6"></a>

### `BT_TBS_CALL_FLAG_WITHHELD`

```c
#define BT_TBS_CALL_FLAG_WITHHELD BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置时表示呼叫信息被隐藏（Withheld），否则未隐藏。

<a id="ga466c1c3c50e82fee9e5c8323e89be414"></a>

### `BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK`

```c
#define BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK BIT(2U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置时表示呼叫信息被网络隐藏（Withheld by Network），否则由网络提供。

<a id="ga3100ab7a7db823d86198847ec0df4adc"></a>

### `BT_TBS_CALL_STATE_ACTIVE`

```c
#define BT_TBS_CALL_STATE_ACTIVE 0x03U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

呼叫正在通话（Active Conversation）。

<a id="gada61fd749f2119452429dd712d283dad"></a>

### `BT_TBS_CALL_STATE_ALERTING`

```c
#define BT_TBS_CALL_STATE_ALERTING 0x02U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

正在提醒远端，即呼出（Outgoing Call）。

<a id="ga482f9627308cad1e56a4a5a5906c2308"></a>

### `BT_TBS_CALL_STATE_DIALING`

```c
#define BT_TBS_CALL_STATE_DIALING 0x01U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

服务器已开始呼叫远端，但尚未提醒远端，即呼出（Outgoing Call）。

<a id="ga829309945831c0e8ac36c3dd79ae26f3"></a>

### `BT_TBS_CALL_STATE_INCOMING`

```c
#define BT_TBS_CALL_STATE_INCOMING 0x00U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

远端正在呼叫，即来电（Incoming Call）。

<a id="ga0d28984faadc6904f72068df6ab6c97d"></a>

### `BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD`

```c
#define BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD 0x06U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

呼叫已连接，但同时被本地和远端保持（Held Locally and Remotely）。

<a id="gac900fe331fe5b81d7ed0b21796d3e16c"></a>

### `BT_TBS_CALL_STATE_LOCALLY_HELD`

```c
#define BT_TBS_CALL_STATE_LOCALLY_HELD 0x04U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

呼叫已连接，但被本地保持（Held Locally）。

本地保持（Locally Held）意味着服务器或客户端都可影响此状态。

<a id="ga76acd3539931a32361fd0deb3bbe8243"></a>

### `BT_TBS_CALL_STATE_REMOTELY_HELD`

```c
#define BT_TBS_CALL_STATE_REMOTELY_HELD 0x05U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

呼叫已连接，但被远端保持（Held Remotely）。

远端保持（Remotely Held）意味着状态由通话的远端一方控制。

<a id="gaeb2eadb4f5559f55734797a4d700e2fe"></a>

### `BT_TBS_ERR_VAL_CHANGED`

```c
#define BT_TBS_ERR_VAL_CHANGED 0x80U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="ga25aa807f2e3a01d030edf4f064a4fbfd"></a>

### `BT_TBS_GTBS_INDEX`

```c
#define BT_TBS_GTBS_INDEX 0xFFU
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

GTBS 索引表示回调来自通用电话承载服务（Generic Telephone Bearer Service，GTBS）实例，或者表示客户端应对服务器的 GTBS 实例执行动作，而非对某个特定电话承载服务（Telephone Bearer Service）实例执行动作。

<a id="ga42b72d7aef36cc7ea0d5dd4ec3d7a717"></a>

### `BT_TBS_MAX_UCI_SIZE`

```c
#define BT_TBS_MAX_UCI_SIZE 6U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

承载统一呼叫者标识符（Bearer Uniform Caller Identifier，UCI）的最大大小。

包括 NULL 终止符。允许值由蓝牙分配编号（Bluetooth Assigned Numbers）定义。

<a id="ga07a7bad80edea037cba34198c5c9c193"></a>

### `BT_TBS_OPTIONAL_OPCODE_ALL`

```c
#define BT_TBS_OPTIONAL_OPCODE_ALL (BT_TBS_OPTIONAL_OPCODE_HOLD | BT_TBS_OPTIONAL_OPCODE_JOIN)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

支持全部控制点操作码（Control Point Opcodes）。

<a id="gaf13a663330c8d1902765c208c028ee50"></a>

### `BT_TBS_OPTIONAL_OPCODE_HOLD`

```c
#define BT_TBS_OPTIONAL_OPCODE_HOLD BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

支持呼叫控制点的本地保持（Local Hold）和本地恢复（Local Retrieve）操作码。

<a id="ga06f41e27d2dfc92f31306938005a9058"></a>

### `BT_TBS_OPTIONAL_OPCODE_JOIN`

```c
#define BT_TBS_OPTIONAL_OPCODE_JOIN BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

支持呼叫控制点的合并（Join）操作码。

<a id="gaf7f2abd7e794806ab6b119bee47db6c6"></a>

### `BT_TBS_REASON_BAD_REMOTE_URI`

```c
#define BT_TBS_REASON_BAD_REMOTE_URI 0x00U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

用于发起呼叫（Originate a Call）的 URI 值格式不正确。

<a id="gacd5a09f5786e01662e29d49aa5307046"></a>

### `BT_TBS_REASON_CALL_FAILED`

```c
#define BT_TBS_REASON_CALL_FAILED 0x01U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

呼叫失败（Call Failed）。

<a id="ga614adc266444030ac83dc6f4d2e89563"></a>

### `BT_TBS_REASON_CLIENT_TERMINATED`

```c
#define BT_TBS_REASON_CLIENT_TERMINATED 0x06U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

客户端终止了呼叫（Call）。

<a id="ga3105e7b0b91b71eb55c1ea5c3bfd6df3"></a>

### `BT_TBS_REASON_LINE_BUSY`

```c
#define BT_TBS_REASON_LINE_BUSY 0x04U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

线路忙（Line Busy）。

<a id="gae195db56d2cd949a29d261c5473eea89"></a>

### `BT_TBS_REASON_NETWORK_CONGESTED`

```c
#define BT_TBS_REASON_NETWORK_CONGESTED 0x05U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

网络拥塞（Network Congestion）。

<a id="ga893d3c79ca62c5e5487d7ca7cd403ce2"></a>

### `BT_TBS_REASON_NO_ANSWER`

```c
#define BT_TBS_REASON_NO_ANSWER 0x08U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

无人应答（No Answer）。

<a id="ga137b813cf902c8209a624c6ae8d4a93b"></a>

### `BT_TBS_REASON_NO_SERVICE`

```c
#define BT_TBS_REASON_NO_SERVICE 0x07U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

无服务（No Service）。

<a id="ga4bc073b85c6eca1f0a4b0757e1050dde"></a>

### `BT_TBS_REASON_REMOTE_ENDED_CALL`

```c
#define BT_TBS_REASON_REMOTE_ENDED_CALL 0x02U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

远端结束了呼叫（Call）。

<a id="gaa4f89b5fa61dcc4ee7e4fb6ae0e12384"></a>

### `BT_TBS_REASON_SERVER_ENDED_CALL`

```c
#define BT_TBS_REASON_SERVER_ENDED_CALL 0x03U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

服务器端结束了呼叫（Call）。

<a id="gaa4dab0b5c08dcf092a125986519a7d55"></a>

### `BT_TBS_REASON_UNSPECIFIED`

```c
#define BT_TBS_REASON_UNSPECIFIED 0x09U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

未指定（Unspecified）。

<a id="gadc371a3a898b3ecac56d8778109f315d"></a>

### `BT_TBS_RESULT_CODE_INVALID_CALL_INDEX`

```c
#define BT_TBS_RESULT_CODE_INVALID_CALL_INDEX 0x03U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

写入呼叫控制点（Call Control Point）时使用的呼叫索引（Call Index）无效。

<a id="gaa60f75b90f461246b2f470930a60efc2"></a>

### `BT_TBS_RESULT_CODE_INVALID_URI`

```c
#define BT_TBS_RESULT_CODE_INVALID_URI 0x06U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

发送发起呼叫（Originate）操作码时，呼出 URI（Outgoing URI）不正确或无效。

<a id="gafac3c970b36f37c815c4370dfef89f09"></a>

### `BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED`

```c
#define BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED 0x01U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

写入呼叫控制点（Call Control Point）时使用了无效操作码。

<a id="gae83a73a5a0474a62dfbcb5ced6eb3f78"></a>

### `BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE`

```c
#define BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE 0x02U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

无法完成请求的操作（Requested Operation）。

<a id="ga148585f5cfe8b1cd7f8db404dac91cdd"></a>

### `BT_TBS_RESULT_CODE_OUT_OF_RESOURCES`

```c
#define BT_TBS_RESULT_CODE_OUT_OF_RESOURCES 0x05U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

内部资源不足，无法完成请求的动作（Requested Action）。

<a id="ga3fa49179525369502018912115c1ccce"></a>

### `BT_TBS_RESULT_CODE_STATE_MISMATCH`

```c
#define BT_TBS_RESULT_CODE_STATE_MISMATCH 0x04U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

收到写入呼叫控制点（Call Control Point）的操作码时，该呼叫索引（Call Index）对应的当前呼叫状态（Call State）并非预期状态。

<a id="gaa92fdb19227ee0b268f2395f3f6a5f63"></a>

### `BT_TBS_RESULT_CODE_SUCCESS`

```c
#define BT_TBS_RESULT_CODE_SUCCESS 0x00U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

操作码写入（Opcode Write）成功。

<a id="gae619d9096b41690ba77ee3e7bd838be3"></a>

### `BT_TBS_SIGNAL_STRENGTH_MAX`

```c
#define BT_TBS_SIGNAL_STRENGTH_MAX 100U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

最大信号强度（Maximum Signal Strength）。

<a id="ga310c1cdffee350fe5235b3ad929ac715"></a>

### `BT_TBS_SIGNAL_STRENGTH_NO_SERVICE`

```c
#define BT_TBS_SIGNAL_STRENGTH_NO_SERVICE 0U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

无服务（No Service）。

<a id="gab8a433da27a61cf1c7be2fc7b006e298"></a>

### `BT_TBS_SIGNAL_STRENGTH_UNKNOWN`

```c
#define BT_TBS_SIGNAL_STRENGTH_UNKNOWN 255U
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

信号强度未知（Unknown Signal Strength）。

<a id="gadc590b9f5813e190fa14644412aee25c"></a>

### `BT_TBS_STATUS_FLAG_INBAND_RINGTONE`

```c
#define BT_TBS_STATUS_FLAG_INBAND_RINGTONE BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

已启用带内铃声（Inband Ringtone）。

<a id="ga53dfa36830f8c562711d9c6f9111929e"></a>

### `BT_TBS_STATUS_FLAG_SILENT_MOD`

```c
#define BT_TBS_STATUS_FLAG_SILENT_MOD BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

服务器处于静音模式（Silent Mode；原文写作 silent mod）。

<a id="ga1cc9e7140531b07bf6a8dedbc17f24c0"></a>

### `bt_tbs_authorize_cb`

```c
typedef bool(* bt_tbs_authorize_cb) (struct bt_conn *conn)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

授权客户端（Authorizing a Client）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 使用的连接（Connection）。 |

**返回（Returns）**：返回：获授权（Authorized）时为 true，否则为 false。

<a id="ga2fa85f3cd96f25f6bb4f449fc9210fa1"></a>

### `bt_tbs_call_change_cb`

```c
typedef void(* bt_tbs_call_change_cb) (struct bt_conn *conn, uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

客户端请求改变呼叫状态（Call State Change）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 使用的连接（Connection）。 |
| `call_index` | 呼叫索引（Call Index）。 |

<a id="ga262ca74b7ae2f0c52657066549fa4f92"></a>

### `bt_tbs_client_call_states_cb`

```c
typedef void(* bt_tbs_client_call_states_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call_state *call_states)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

ccp_read_call_state 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `call_count` | 读取的呼叫状态（Call States）数量。 |
| `call_states` | 呼叫状态数组（Call State Array）。客户端不保留此数组，因此需要保存时必须复制。 |

<a id="ga40b8b3d1b318a1b5c5524877bbc2f90f"></a>

### `bt_tbs_client_cp_cb`

```c
typedef void(* bt_tbs_client_cp_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

CCP 呼叫控制函数（Call Control Functions）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `call_index` | 呼叫索引（Call Index）。对于 bt_tbs_client_originate_call，此值始终为 0，并不反映实际呼叫索引。 |

<a id="ga7b31e1c30fa96081a3ef38e1a481b64f"></a>

### `bt_tbs_client_current_calls_cb`

```c
typedef void(* bt_tbs_client_current_calls_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call *calls)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

ccp_read_current_calls 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `call_count` | 读取的呼叫（Calls）数量。 |
| `calls` | 呼叫数组（Call Array）。客户端不保留此数组，因此需要保存时必须复制。 |

<a id="ga9cac11cc696be9fb387f2f7685e0d8a7"></a>

### `bt_tbs_client_discover_cb`

```c
typedef void(* bt_tbs_client_discover_cb) (struct bt_conn *conn, int err, uint8_t tbs_count, bool gtbs_found)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

ccp_discover 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于发现设备的呼叫控制配置文件（CCP）的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `tbs_count` | 对端设备上的 TBS 实例数量（Number of Instances）。 |
| `gtbs_found` | 服务器是否具有通用电话承载服务实例（Generic TBS Instance）。 |

<a id="ga4d7632de7c2006e478880950076908a9"></a>

### `bt_tbs_client_read_string_cb`

```c
typedef void(* bt_tbs_client_read_string_cb) (struct bt_conn *conn, int err, uint8_t inst_index, const char *value)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取字符串值（String Value）的函数使用的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `value` | 以 NULL 结尾的字符串值（Null-terminated String Value）。客户端不保留此值，因此需要保存时必须复制。 |

<a id="ga600051910ed538a2da823554df23dd20"></a>

### `bt_tbs_client_read_value_cb`

```c
typedef void(* bt_tbs_client_read_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint32_t value)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取整数值（Integer Value）的函数使用的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `value` | 整数值（Integer Value）。 |

<a id="gab881b3caaaa4425e52afd84e53adee78"></a>

### `bt_tbs_client_termination_reason_cb`

```c
typedef void(* bt_tbs_client_termination_reason_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index, uint8_t reason)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

ccp_read_termination_reason 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `call_index` | 呼叫索引（Call Index）。 |
| `reason` | 终止原因（Termination Reason）。 |

<a id="gaf77231168e4444da7aef203cc9eaca95"></a>

### `bt_tbs_client_write_value_cb`

```c
typedef void(* bt_tbs_client_write_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

向对端设备写入值（Writing Values）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值（Error Value），为 BT_TBS_CLIENT_RESULT_CODE_*、GATT 错误或 errno 值。 |
| `inst_index` | 已更新的 TBS 实例索引。 |

<a id="gaa45b3f4837165d722c2df6f202a39058"></a>

### `bt_tbs_join_calls_cb`

```c
typedef void(* bt_tbs_join_calls_cb) (struct bt_conn *conn, uint8_t call_index_count, const uint8_t *call_indexes)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

客户端合并呼叫（Joining Calls）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 使用的连接（Connection）。 |
| `call_index_count` | 要合并的呼叫索引（Call Indexes）数量。 |
| `call_indexes` | 呼叫索引（Call Indexes）。 |

<a id="ga60e9e143f247bb7e668293f0233ce300"></a>

### `bt_tbs_originate_call_cb`

```c
typedef bool(* bt_tbs_originate_call_cb) (struct bt_conn *conn, uint8_t call_index, const char *uri)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

客户端发起呼叫（Originating a Call）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 使用的连接（Connection）。 |
| `call_index` | 呼叫索引（Call Index）。 |
| `uri` | URI。其值可能变化，需要持久保存时应复制。 |

**返回（Returns）**：返回：呼叫请求已接受并已提醒远端时为 true。

<a id="ga69e93b48b2a48e8a6552882660b791cc"></a>

### `bt_tbs_terminate_call_cb`

```c
typedef void(* bt_tbs_terminate_call_cb) (struct bt_conn *conn, uint8_t call_index, uint8_t reason)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

客户端终止呼叫（Terminating a Call）的回调函数。

客户端或服务器均可终止呼叫（Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 使用的连接（Connection）。 |
| `call_index` | 呼叫索引（Call Index）。 |
| `reason` | 终止原因（Termination Reason），使用 BT_TBS_REASON_*。 |

<a id="ga1b942bcf8287641f9cd53824b4d6e77b"></a>

### `bt_tbs_accept()`

```c
int bt_tbs_accept ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

接听正在振铃的呼叫（Alerting Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 将要接听的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga625fc73885c2bfd63f0f4b2d7f72eaef"></a>

### `bt_tbs_client_accept_call()`

```c
int bt_tbs_client_accept_call ( struct bt_conn * conn, uint8_t inst_index, uint8_t call_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

接听来电（Incoming Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `call_index` | 要接听的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_ACCEPT_CALL`，此函数才能生效。

<a id="gac59f3dec092a14bdf234039e3dcd12eb"></a>

### `bt_tbs_client_discover()`

```c
int bt_tbs_client_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

发现某个连接上的电话承载服务（TBS）。

这将启动 GATT 发现（Discovery），并设置句柄与订阅（Handles and Subscriptions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要在其上发现 TBS 的连接（Connection）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 GATT 错误值。

<a id="gaadae501fa6f7771bb9661af829805a5f"></a>

### `bt_tbs_client_get_by_ccid()`

```c
struct bt_tbs_instance * bt_tbs_client_get_by_ccid ( const struct bt_conn * conn, uint8_t ccid )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

根据 CCID 查找电话承载服务实例（Telephone Bearer Service Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `ccid` | 用于查找服务实例（Service Instance）的 CCID。 |

**返回（Returns）**：返回：找到时返回指向电话承载服务实例（Telephone Bearer Service Instance）的指针，否则为 NULL。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_CCID`，此函数才能生效。

<a id="ga20c6780a4624707a537e905e889510ca"></a>

### `bt_tbs_client_get_by_index()`

```c
struct bt_tbs_instance * bt_tbs_client_get_by_index ( const struct bt_conn * conn, uint8_t index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

根据索引查找电话承载服务实例（Telephone Bearer Service Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `index` | 用于查找服务实例（Service Instance）的索引。 |

**返回（Returns）**：返回：找到时返回指向电话承载服务实例（Telephone Bearer Service Instance）的指针，否则为 NULL。

<a id="ga23e825de6af71d4e456b63c3a621fb61"></a>

### `bt_tbs_client_hold_call()`

```c
int bt_tbs_client_hold_call ( struct bt_conn * conn, uint8_t inst_index, uint8_t call_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

请求保持呼叫（Hold a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `call_index` | 要保持的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_HOLD_CALL`，此函数才能生效。

<a id="gaae1925deb0b5865af601aa8278ffb10a"></a>

### `bt_tbs_client_join_calls()`

```c
int bt_tbs_client_join_calls ( struct bt_conn * conn, uint8_t inst_index, const uint8_t * call_indexes, uint8_t count )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

合并多个呼叫（Join Multiple Calls）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `call_indexes` | 呼叫索引数组（Call Index Array）。 |
| `count` | call_indexes 数组中的呼叫索引数量。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_JOIN_CALLS`，此函数才能生效。

<a id="ga0aac704008ffc92ce6609d3ffffc4523"></a>

### `bt_tbs_client_originate_call()`

```c
int bt_tbs_client_originate_call ( struct bt_conn * conn, uint8_t inst_index, const char * uri )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

请求发起呼叫（Originate a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `uri` | 被叫方（Callee）的 URI。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL`，此函数才能生效。

<a id="ga2053a9eb7cf28f66febd365f0b682be0"></a>

### `bt_tbs_client_read_bearer_provider_name()`

```c
int bt_tbs_client_read_bearer_provider_name ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的承载提供者名称（Bearer Provider Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME`，此函数才能生效。

<a id="gaba92039d3b44da9163a22400951fafa7"></a>

### `bt_tbs_client_read_bearer_uci()`

```c
int bt_tbs_client_read_bearer_uci ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的统一呼叫者标识符（UCI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_UCI`，此函数才能生效。

<a id="gafeaaaefb9d4eb773dd0cbdfebe26e0b7"></a>

### `bt_tbs_client_read_call_state()`

```c
int bt_tbs_client_read_call_state ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例当前呼叫的状态（Call States）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

<a id="ga4238a37b80b7d7ff611fe9b02b7cf54d"></a>

### `bt_tbs_client_read_call_uri()`

```c
int bt_tbs_client_read_call_uri ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的呼叫目标 URI（Call Target URI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_INCOMING_URI`，此函数才能生效。

<a id="gac070ec0590df5820b7721d579ceeeb15"></a>

### `bt_tbs_client_read_ccid()`

```c
int bt_tbs_client_read_ccid ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的内容 ID（Content ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_CCID`，此函数才能生效。

<a id="ga895c7f54300e5452fb8d0c9d4b3306ae"></a>

### `bt_tbs_client_read_current_calls()`

```c
int bt_tbs_client_read_current_calls ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的当前呼叫列表（Current Calls List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS`，此函数才能生效。

<a id="ga99549dd6244580e157006fb17772fd8f"></a>

### `bt_tbs_client_read_friendly_name()`

```c
int bt_tbs_client_read_friendly_name ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例中某个呼叫的友好名称（Friendly Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME`，此函数才能生效。

<a id="gaf504e1a11352d77a36aa087b587e4ba8"></a>

### `bt_tbs_client_read_optional_opcodes()`

```c
int bt_tbs_client_read_optional_opcodes ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例支持的操作码（Supported Opcode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES`，此函数才能生效。

<a id="gab04f8355c32fce501bd757b75ee9d38a"></a>

### `bt_tbs_client_read_remote_uri()`

```c
int bt_tbs_client_read_remote_uri ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的远端 URI（Remote URI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_INCOMING_CALL`，此函数才能生效。

<a id="ga38046c5c715d451b21a3076742268010"></a>

### `bt_tbs_client_read_signal_interval()`

```c
int bt_tbs_client_read_signal_interval ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL`，此函数才能生效。

<a id="gaabe97df55817b8e36c79de4bf30fc83f"></a>

### `bt_tbs_client_read_signal_strength()`

```c
int bt_tbs_client_read_signal_strength ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的当前信号强度（Signal Strength）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH`，此函数才能生效。

<a id="ga9fe91df1a31ce59401347fc0eac2b701"></a>

### `bt_tbs_client_read_status_flags()`

```c
int bt_tbs_client_read_status_flags ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的特性与状态值（Feature and Status Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_STATUS_FLAGS`，此函数才能生效。

<a id="ga7684dbcb78e407f7002d44fbdb805e5d"></a>

### `bt_tbs_client_read_technology()`

```c
int bt_tbs_client_read_technology ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的技术类型（Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY`，此函数才能生效。

<a id="gad19db25591c7ae5bd0b4c2bbaefc9bed"></a>

### `bt_tbs_client_read_uri_list()`

```c
int bt_tbs_client_read_uri_list ( struct bt_conn * conn, uint8_t inst_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

读取 TBS 实例的 URI 方案列表（URI Schemes List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST`，此函数才能生效。

<a id="gabe2251d4ea88306793dc68ae683886bb"></a>

### `bt_tbs_client_register_cb()`

```c
int bt_tbs_client_register_cb ( struct bt_tbs_client_cb * cbs)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

注册呼叫控制配置文件（CCP）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cbs` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cbs 为 NULL。 |
| `-EEXIST` | cbs 已注册（Registered）。 |

<a id="gabbe194a63da0b95dc1dca0337560a585"></a>

### `bt_tbs_client_retrieve_call()`

```c
int bt_tbs_client_retrieve_call ( struct bt_conn * conn, uint8_t inst_index, uint8_t call_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

从本地保持状态恢复呼叫（Retrieve Call from Local Hold）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `call_index` | 要恢复的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL`，此函数才能生效。

<a id="ga3a71c51d464aa19fbfbd2d60fc4901bc"></a>

### `bt_tbs_client_set_outgoing_uri()`

```c
int bt_tbs_client_set_outgoing_uri ( struct bt_conn * conn, uint8_t inst_index, const char * uri )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置对端设备上 TBS 实例的呼出 URI（Outgoing URI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `uri` | 以 NULL 结尾的 URI 字符串（Null-terminated URI String）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

<a id="gaa1dcb9908057d75a54fa447639826f3c"></a>

### `bt_tbs_client_set_signal_strength_interval()`

```c
int bt_tbs_client_set_signal_strength_interval ( struct bt_conn * conn, uint8_t inst_index, uint8_t interval )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `interval` | 要写入的间隔（Interval），0–255 秒。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL`，此函数才能生效。

<a id="ga25b803bb5cae2e1a8b0398bc48137d80"></a>

### `bt_tbs_client_terminate_call()`

```c
int bt_tbs_client_terminate_call ( struct bt_conn * conn, uint8_t inst_index, uint8_t call_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

请求终止呼叫（Terminate a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与 TBS 服务器的连接（Connection）。 |
| `inst_index` | TBS 实例的索引（Instance Index）。 |
| `call_index` | 要终止的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；成功时为 0，失败时为 errno 值。

**说明（Note）**：注意：必须设置 `CONFIG_BT_TBS_CLIENT_TERMINATE_CALL`，此函数才能生效。

<a id="ga62f5008cbfba158fe399cfaf683d1d2e"></a>

### `bt_tbs_dbg_print_calls()`

```c
void bt_tbs_dbg_print_calls ( void )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

将所有服务的全部呼叫（Calls）打印到调试日志。

<a id="gab72044a1f5466114b5efb88dfcd2f097"></a>

### `bt_tbs_hold()`

```c
int bt_tbs_hold ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

保持呼叫（Hold a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 将要保持的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga23226d41e3b98a53ec9a9c2fa346c9ac"></a>

### `bt_tbs_join()`

```c
int bt_tbs_join ( uint8_t call_index_cnt, uint8_t * call_indexes )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

合并呼叫（Join Calls）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index_cnt` | 要合并的呼叫索引（Call Indexes）数量。 |
| `call_indexes` | 要合并的呼叫索引数组（Call Index Array）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="gadeae51d7cecd80abcdcde1195bb1dfba"></a>

### `bt_tbs_originate()`

```c
int bt_tbs_originate ( uint8_t bearer_index, char * uri, uint8_t * call_index )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

发起呼叫（Originate a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bearer_index` | 电话承载索引（Telephone Bearer Index）。 |
| `[in] uri` | 远端 URI（Remote URI）。 |
| `[out] call_index` | 指向用于保存新 call_index 的值的指针。 |

**返回（Returns）**：返回：int 类型；成功时为正的呼叫索引（Call Index），失败时为 errno 值。

<a id="ga970c970bedd6e94aa4c92479183554e9"></a>

### `bt_tbs_register_bearer()`

```c
int bt_tbs_register_bearer ( const struct bt_tbs_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

注册电话承载（Telephone Bearer）。

使用提供的参数注册电话承载服务（Telephone Bearer Service，TBS）或通用电话承载服务（Generic Telephone Bearer Service，GTBS）。

根据 TBS 规范，此功能须实例化通用电话承载服务（GTBS），因此必须先注册 GTBS，才能注册任何 TBS。同样，必须先注销全部 TBS，才能通过 bt_tbs_unregister_bearer() 注销 GTBS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于初始化承载（Bearer）的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 返回值大于或等于 0 时，表示承载索引（Bearer Index）。 |
| `-EINVAL` | param 包含无效数据（Invalid Data）。 |
| `-EALREADY` | param.gtbs 为 true，且 GTBS 已注册。 |
| `-EAGAIN` | param.gtbs 为 false，且 GTBS 尚未注册。 |
| `-ENOMEM` | param.gtbs 为 false，且无法再注册更多 TBS，参见 CONFIG_BT_TBS_BEARER_COUNT。 |
| `-ENOEXEC` | 服务注册（Register Service）失败。 |

<a id="ga76f120dba549225a6f2c2c22be08edfc"></a>

### `bt_tbs_register_cb()`

```c
void bt_tbs_register_cb ( struct bt_tbs_cb * cbs)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

注册电话承载服务（TBS）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cbs` | 指向回调结构体（Callback Structure）的指针。 |

<a id="ga868b83450f7425e8a0c8cfb7c1de45d8"></a>

### `bt_tbs_remote_answer()`

```c
int bt_tbs_remote_answer ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

通知服务器远端已接听呼叫（Answered the Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 已接听的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e"></a>

### `bt_tbs_remote_hold()`

```c
int bt_tbs_remote_hold ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

通知服务器远端已保持呼叫（Held the Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 已保持的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga47939f557e4d6503af9b7b85aff9d60f"></a>

### `bt_tbs_remote_incoming()`

```c
int bt_tbs_remote_incoming ( uint8_t bearer_index, const char * to, const char * from, const char * friendly_name )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

向服务器通知来电（Incoming Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）。 |
| `to` | 接收该呼叫的 URI。 |
| `from` | 远端呼叫者（Remote Caller）的 URI。 |
| `friendly_name` | 远端呼叫者的友好名称（Friendly Name）。 |

**返回（Returns）**：返回：int 类型；非负值表示新呼叫索引（Call Index），负值表示 errno 错误。

<a id="ga09a3e64040819b6b8b694b94d2f62ca0"></a>

### `bt_tbs_remote_retrieve()`

```c
int bt_tbs_remote_retrieve ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

通知服务器远端已恢复呼叫（Retrieved the Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 已恢复的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga52afc7b8a22b071dbac10057579f319c"></a>

### `bt_tbs_remote_terminate()`

```c
int bt_tbs_remote_terminate ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

通知服务器远端已终止呼叫（Terminated the Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 已终止的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="gad0b45af09b82d6cd66a8481c0e67e04e"></a>

### `bt_tbs_retrieve()`

```c
int bt_tbs_retrieve ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

恢复呼叫（Retrieve a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 将要恢复的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga5118db6b23b387956e75eda8aecd53d5"></a>

### `bt_tbs_set_bearer_provider_name()`

```c
int bt_tbs_set_bearer_provider_name ( uint8_t bearer_index, const char * name )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置新的承载提供者（Bearer Provider）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）；对于 GTBS，使用 BT_TBS_GTBS_INDEX。 |
| `name` | 新的承载提供方名称（Bearer Provider Name）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="gaa77ea977fca9833d1755d5084a3f352c"></a>

### `bt_tbs_set_bearer_technology()`

```c
int bt_tbs_set_bearer_technology ( uint8_t bearer_index, enum bt_bearer_tech new_technology )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置新的承载技术（Bearer Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）；对于 GTBS，使用 BT_TBS_GTBS_INDEX。 |
| `new_technology` | 新的承载技术类型（Bearer Technology）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="gac316adedf7fda441ee55feb9d24d1a94"></a>

### `bt_tbs_set_signal_strength()`

```c
int bt_tbs_set_signal_strength ( uint8_t bearer_index, uint8_t new_signal_strength )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

更新服务器报告的信号强度（Signal Strength）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）；对于 GTBS，使用 BT_TBS_GTBS_INDEX。 |
| `new_signal_strength` | 新的信号强度（Signal Strength）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga838e51a85f9833e0822090cd3df09e00"></a>

### `bt_tbs_set_status_flags()`

```c
int bt_tbs_set_status_flags ( uint8_t bearer_index, uint16_t status_flags )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置特性与状态值（Feature and Status Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）；对于 GTBS，使用 BT_TBS_GTBS_INDEX。 |
| `status_flags` | 新的特性与状态值（Feature and Status Value）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="gae413f94b141b6fa8233de15c36f6327a"></a>

### `bt_tbs_set_uri_scheme_list()`

```c
int bt_tbs_set_uri_scheme_list ( uint8_t bearer_index, const char * uri_scheme_list )
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

设置承载的 URI 方案列表（URI Scheme List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 电话承载索引（Telephone Bearer Index）。 |
| `uri_scheme_list` | 逗号分隔的 URI 前缀列表（URI Prefix List），例如 "skype,tel"。 |

**返回（Returns）**：返回：非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga82553640882ac74f9af84bfe09ff47ee"></a>

### `bt_tbs_terminate()`

```c
int bt_tbs_terminate ( uint8_t call_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

终止呼叫（Terminate a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call_index` | 将要终止的呼叫索引（Call Index）。 |

**返回（Returns）**：返回：int 类型；非负值表示 BT_TBS_RESULT_CODE_*，负值表示 errno 错误。

<a id="ga8edd4d31478ed9e0aedbd1a34bdfca96"></a>

### `bt_tbs_unregister_bearer()`

```c
int bt_tbs_unregister_bearer ( uint8_t bearer_index)
```

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

注销电话承载（Telephone Bearer）。

使用所提供参数注销电话承载服务（TBS）或通用电话承载服务（GTBS）。承载必须先通过 bt_tbs_register_bearer() 注册，才能注销。

同样，必须先注销全部 TBS，才能注销 GTBS。（原文句末 “with” 后未给出内容。）

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer_index` | 要注销的承载索引（Bearer Index）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer_index 无效。 |
| `-EALREADY` | bearer_index 标识的承载尚未注册（Registered）。 |
| `-EAGAIN` | bearer_index 标识的承载为 GTBS，且仍有已注册的 TBS 实例。 |
| `-ENOEXEC` | 服务注销（Unregister Service）失败。 |


## 8.13\_原页交叉引用（Cross References）

- [bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)
- [bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)
- [bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)
- [bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/bluetooth/audio/tbs.h](../api_file_bluetooth_media_reference/P012_zephyr__bluetooth__audio__tbs.h_文件参考.md)
- [CONFIG_BT_TBS_CLIENT_ACCEPT_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_ACCEPT_CALL)
- [CONFIG_BT_TBS_CLIENT_CCID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_CCID)
- [CONFIG_BT_TBS_CLIENT_HOLD_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_HOLD_CALL)
- [CONFIG_BT_TBS_CLIENT_JOIN_CALLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_JOIN_CALLS)
- [CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL)
- [CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME)
- [CONFIG_BT_TBS_CLIENT_BEARER_UCI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_UCI)
- [CONFIG_BT_TBS_CLIENT_INCOMING_URI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_INCOMING_URI)
- [CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS)
- [CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME)
- [CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES)
- [CONFIG_BT_TBS_CLIENT_INCOMING_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_INCOMING_CALL)
- [CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL)
- [CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH)
- [CONFIG_BT_TBS_CLIENT_STATUS_FLAGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_STATUS_FLAGS)
- [CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY)
- [CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST)
- [CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL)
- [CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL)
- [CONFIG_BT_TBS_CLIENT_TERMINATE_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_TERMINATE_CALL)
- [CONFIG_BT_TBS_BEARER_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_BEARER_COUNT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_媒体代理（Media Proxy）.md) · [返回大纲](大纲.md) · [下一章](P009_蜂窝通信（Cellular）.md)
