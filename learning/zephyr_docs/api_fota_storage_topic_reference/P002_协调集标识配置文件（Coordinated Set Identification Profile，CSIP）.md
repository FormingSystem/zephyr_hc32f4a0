---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-2
title: 协调集标识配置文件（Coordinated Set Identification Profile，CSIP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_协调集标识配置文件（Coordinated Set Identification Profile，CSIP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

协调集标识配置文件（Coordinated Set Identification Profile，CSIP）

<a id="details"></a>

协同集标识配置文件（Coordinated Set Identification Profile，CSIP）。自（Since）3.0 起提供，版本（Version）0.8.0。CSIP 提供发现与协调设备集合的流程。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fcsip_5Fset_5Fmember_5Fcb"></a>

```c
struct bt_csip_set_member_cb
```

相关声明：[bt_csip_set_member_cb](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md)。

协调集合标识服务（Coordinated Set Identification Service，CSIS）的回调结构体。

<a id="r_bt_5Fcsip_5Fset_5Fmember_5Fregister_5Fparam"></a>

```c
struct bt_csip_set_member_register_param
```

相关声明：[bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)。

协调集合标识服务（CSIS）的注册结构体。

<a id="r_bt_5Fcsip_5Fset_5Fmember_5Fset_5Finfo"></a>

```c
struct bt_csip_set_member_set_info
```

相关声明：[bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)。

保存服务实例（Service Instance）信息的结构体。

<a id="r_bt_5Fcsip_5Fset_5Fcoordinator_5Fset_5Finfo"></a>

```c
struct bt_csip_set_coordinator_set_info
```

相关声明：[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)。

特定集合（Set）的信息。

<a id="r_bt_5Fcsip_5Fset_5Fcoordinator_5Fcsis_5Finst"></a>

```c
struct bt_csip_set_coordinator_csis_inst
```

相关声明：[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

表示远端设备上协调集合（Coordinated Set）实例的结构体。

<a id="r_bt_5Fcsip_5Fset_5Fcoordinator_5Fset_5Fmember"></a>

```c
struct bt_csip_set_coordinator_set_member
```

相关声明：[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

将远端设备表示为集合成员（Set Member）的结构体。

<a id="r_bt_5Fcsip_5Fset_5Fcoordinator_5Fcb"></a>

```c
struct bt_csip_set_coordinator_cb
```

相关声明：[bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)。

保存协调集合标识配置文件（Coordinated Set Identification Profile，CSIP）的集合协调器（Set Coordinator）回调的结构体。

<a id="r_bt_5Fcsip_5Fset_5Fmember_5Fsvc_5Finst"></a>

```c
struct bt_csip_set_member_svc_inst
```

相关声明：[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

不透明的协调集合标识服务（CSIS）实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga1633e4caaa03a21da0a5431f5f263076"></a>

```c
#define BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE K_SECONDS(10)
```

相关声明：[BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE](#ga1633e4caaa03a21da0a5431f5f263076)、[K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)。

用于成员发现（Member Discovery）的建议定时器。

<a id="r_ga42702049524f7ce24dfb6061120414df"></a>

```c
#define BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES 0U
```

相关声明：[BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES](#ga42702049524f7ce24dfb6061120414df)。

定义协调集合标识集合协调器（Coordinated Set Identification Set Coordinator）的协调集合标识服务（Coordinated Set Identification Service）实例数量上限。

<a id="r_gac2aa2ce09ff4aad8bc423dd5b5643038"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT 0x00U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT](#gac2aa2ce09ff4aad8bc423dd5b5643038)。

接受以明文（Plaintext）读取 SIRK 的请求。

<a id="r_gae6422e7e38bacc39ed2f8d52efe9d6db"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC 0x01U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC](#gae6422e7e38bacc39ed2f8d52efe9d6db)。

接受读取 SIRK 的请求，但返回加密的 SIRK（Encrypted SIRK）。

<a id="r_ga0175e269097a2b6f8f303ee97527db4a"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_REJECT 0x02U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_REJECT](#ga0175e269097a2b6f8f303ee97527db4a)。

拒绝读取 SIRK 的请求。

<a id="r_gaa245a416becaaaeb118b440f9ba2431d"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY 0x03U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY](#gaa245a416becaaaeb118b440f9ba2431d)。

SIRK 只能通过带外过程（Out-of-Band Procedure，OOB）获取。

<a id="r_ga33069821c84e9b4c16c9d95d88c23158"></a>

```c
#define BT_CSIP_SIRK_SIZE 16U
```

相关声明：[BT_CSIP_SIRK_SIZE](#ga33069821c84e9b4c16c9d95d88c23158)。

集合标识解析密钥（Set Identification Resolving Key，SIRK）的大小。

<a id="r_ga5b0149fec5d38e7003593c227b561506"></a>

```c
#define BT_CSIP_RSI_SIZE 6U
```

相关声明：[BT_CSIP_RSI_SIZE](#ga5b0149fec5d38e7003593c227b561506)。

可解析集合标识符（Resolvable Set Identifier，RSI）的大小。

<a id="r_ga00f382d9fe9afb55acfd6f758cef6389"></a>

```c
#define BT_CSIP_ERROR_LOCK_DENIED 0x80U
```

相关声明：[BT_CSIP_ERROR_LOCK_DENIED](#ga00f382d9fe9afb55acfd6f758cef6389)。

服务已锁定（Already Locked）。

<a id="r_gac6eda3e7a9a06f86bc715df20e14daa1"></a>

```c
#define BT_CSIP_ERROR_LOCK_RELEASE_DENIED 0x81U
```

相关声明：[BT_CSIP_ERROR_LOCK_RELEASE_DENIED](#gac6eda3e7a9a06f86bc715df20e14daa1)。

服务未锁定（Not Locked）。

<a id="r_gaeca8a3a9e136882c200c432b9f83203e"></a>

```c
#define BT_CSIP_ERROR_LOCK_INVAL_VALUE 0x82U
```

相关声明：[BT_CSIP_ERROR_LOCK_INVAL_VALUE](#gaeca8a3a9e136882c200c432b9f83203e)。

锁定值（Lock Value）无效。

<a id="r_ga4e0da5f82ef943e660f669a2962bcc7a"></a>

```c
#define BT_CSIP_ERROR_SIRK_OOB_ONLY 0x83U
```

相关声明：[BT_CSIP_ERROR_SIRK_OOB_ONLY](#ga4e0da5f82ef943e660f669a2962bcc7a)。

SIRK 只能通过带外（Out-of-Band）方式获取。

<a id="r_gaabd5b74d0e805bfb0b492a45445ec4c4"></a>

```c
#define BT_CSIP_ERROR_LOCK_ALREADY_GRANTED 0x84U
```

相关声明：[BT_CSIP_ERROR_LOCK_ALREADY_GRANTED](#gaabd5b74d0e805bfb0b492a45445ec4c4)。

客户端已是锁的所有者（Owner of the Lock）。

<a id="r_ga04fcc2431bec35d53664c8f5ab18100d"></a>

```c
#define BT_CSIP_DATA_RSI(_rsi)
```

相关声明：[BT_CSIP_DATA_RSI](#ga04fcc2431bec35d53664c8f5ab18100d)。

声明包含 RSI 的 bt_data 数组的辅助宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gaeee5f0691ba0d63a370ac5dd94cb4d5c"></a>

```c
typedef void(* bt_csip_set_coordinator_discover_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_set_member *member, int err, size_t set_count)
```

相关声明：[bt_csip_set_coordinator_discover_cb](#gaeee5f0691ba0d63a370ac5dd94cb4d5c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

用于发现协调集合标识服务（Coordinated Set Identification Services）的回调。

<a id="r_ga994431ea69920d9e84f35ca6e1e5f634"></a>

```c
typedef void(* bt_csip_set_coordinator_lock_set_cb) (int err)
```

相关声明：[bt_csip_set_coordinator_lock_set_cb](#ga994431ea69920d9e84f35ca6e1e5f634)。

用于跨一个或多个设备锁定集合（Lock a Set）的回调。

<a id="r_ga991ee886c814e0b72fa12ed58ef4a90b"></a>

```c
typedef void(* bt_csip_set_coordinator_lock_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst, bool locked)
```

相关声明：[bt_csip_set_coordinator_lock_changed_cb](#ga991ee886c814e0b72fa12ed58ef4a90b)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

已连接设备上的集合锁定值（Lock Value）发生变化时的回调。

<a id="r_gacdb98c9ae3248064e90352387df7cef2"></a>

```c
typedef void(* bt_csip_set_coordinator_sirk_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst)
```

相关声明：[bt_csip_set_coordinator_sirk_changed_cb](#gacdb98c9ae3248064e90352387df7cef2)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

已连接设备上的集合 SIRK 值发生变化时的回调。

<a id="r_gaee24f364c90cdcd0b6f49c8b297a34a7"></a>

```c
typedef void(* bt_csip_set_coordinator_size_changed_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_csis_inst *inst)
```

相关声明：[bt_csip_set_coordinator_size_changed_cb](#gaee24f364c90cdcd0b6f49c8b297a34a7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

已连接设备上的集合大小（Set Size）发生变化时的回调。

<a id="r_ga0f2e0b610a4db975a72c6d9a645964cb"></a>

```c
typedef void(* bt_csip_set_coordinator_ordered_access_cb_t) (const struct bt_csip_set_coordinator_set_info *set_info, int err, bool locked, struct bt_csip_set_coordinator_set_member *member)
```

相关声明：[bt_csip_set_coordinator_ordered_access_cb_t](#ga0f2e0b610a4db975a72c6d9a645964cb)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

bt_csip_set_coordinator_ordered_access() 的回调（Callback）。

<a id="r_ga2ce69e3bf51622fd41389a12d26e2ba9"></a>

```c
typedef bool(* bt_csip_set_coordinator_ordered_access_t) (const struct bt_csip_set_coordinator_set_info *set_info, struct bt_csip_set_coordinator_set_member *members[], size_t count)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_ordered_access_t](#ga2ce69e3bf51622fd41389a12d26e2ba9)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

bt_csip_set_coordinator_ordered_access() 的回调函数定义（Callback Function Definition）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_gabc8d9c8d2b2f73f5e18e7fdbce95389c"></a>

```c
void * bt_csip_set_member_svc_decl_get (const struct bt_csip_set_member_svc_inst *svc_inst)
```

相关声明：[bt_csip_set_member_svc_decl_get](#gabc8d9c8d2b2f73f5e18e7fdbce95389c)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_gab11184ace9246d4c5ead6bdc98ffa2ac"></a>

```c
int bt_csip_set_member_register (const struct bt_csip_set_member_register_param *param, struct bt_csip_set_member_svc_inst **svc_inst)
```

相关声明：[bt_csip_set_member_register](#gab11184ace9246d4c5ead6bdc98ffa2ac)、[bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注册协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga9ee48e36fb33ee27e689d32f08f071a1"></a>

```c
int bt_csip_set_member_unregister (struct bt_csip_set_member_svc_inst *svc_inst)
```

相关声明：[bt_csip_set_member_unregister](#ga9ee48e36fb33ee27e689d32f08f071a1)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注销协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga9a897ace4906a5df99cffd6cabc1b3e5"></a>

```c
int bt_csip_set_member_sirk (struct bt_csip_set_member_svc_inst *svc_inst, const uint8_t sirk[16U])
```

相关声明：[bt_csip_set_member_sirk](#ga9a897ace4906a5df99cffd6cabc1b3e5)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置服务实例（Service Instance）的 SIRK。

<a id="r_gaef51ab05dbe9d8a69674f7020e8f837f"></a>

```c
int bt_csip_set_member_set_size_and_rank (struct bt_csip_set_member_svc_inst *svc_inst, uint8_t size, uint8_t rank)
```

相关声明：[bt_csip_set_member_set_size_and_rank](#gaef51ab05dbe9d8a69674f7020e8f837f)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为服务实例设置新的大小（Size）和顺序号（Rank）。

<a id="r_gad80917089bc7e629cc3cb9d7fbf6cf45"></a>

```c
int bt_csip_set_member_get_info (const struct bt_csip_set_member_svc_inst *svc_inst, struct bt_csip_set_member_set_info *info)
```

相关声明：[bt_csip_set_member_get_info](#gad80917089bc7e629cc3cb9d7fbf6cf45)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)。

获取服务实例（Service Instances）的信息。

<a id="r_gae020da1a92d3babf47954c12dbbde56b"></a>

```c
int bt_csip_set_member_generate_rsi (const struct bt_csip_set_member_svc_inst *svc_inst, uint8_t rsi[6U])
```

相关声明：[bt_csip_set_member_generate_rsi](#gae020da1a92d3babf47954c12dbbde56b)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

生成可解析集合标识符（Resolvable Set Identifier，RSI）值。

<a id="r_ga95e2ba4b65ec42eedb26bf5ad181b606"></a>

```c
int bt_csip_set_member_lock (struct bt_csip_set_member_svc_inst *svc_inst, bool lock, bool force)
```

相关声明：[bt_csip_set_member_lock](#ga95e2ba4b65ec42eedb26bf5ad181b606)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

锁定服务器上的特定协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga7e7ea4a92bb76aded86807571a2cbb73"></a>

```c
int bt_csip_set_coordinator_discover (struct bt_conn *conn)
```

相关声明：[bt_csip_set_coordinator_discover](#ga7e7ea4a92bb76aded86807571a2cbb73)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接（Connection）初始化 csip_set_coordinator 实例。

<a id="r_ga8c3666d8f20f909dd4fa2010ae02c9a5"></a>

```c
struct bt_csip_set_coordinator_set_member * bt_csip_set_coordinator_set_member_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[bt_csip_set_coordinator_set_member_by_conn](#ga8c3666d8f20f909dd4fa2010ae02c9a5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通过连接指针（Connection Pointer）获取集合成员（Set Member）。

<a id="r_ga6b35d73b102ef7b1db26dbd86aaf6a36"></a>

```c
bool bt_csip_set_coordinator_is_set_member (const uint8_t sirk[16U], struct bt_data *data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_is_set_member](#ga6b35d73b102ef7b1db26dbd86aaf6a36)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

检查广播数据（Advertising Data）是否表示集合成员（Set Member）。

<a id="r_ga08c514fda44e5a9b5cfc16be629c2b37"></a>

```c
int bt_csip_set_coordinator_register_cb (struct bt_csip_set_coordinator_cb *cb)
```

相关声明：[bt_csip_set_coordinator_register_cb](#ga08c514fda44e5a9b5cfc16be629c2b37)、[bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)。

注册 csip_set_coordinator 的回调（Callbacks）。

<a id="r_gacd83494562a62fbdbc7282107d4454b4"></a>

```c
int bt_csip_set_coordinator_ordered_access (const struct bt_csip_set_coordinator_set_member *members[], uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info, bt_csip_set_coordinator_ordered_access_t cb)
```

相关声明：[bt_csip_set_coordinator_ordered_access](#gacd83494562a62fbdbc7282107d4454b4)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bt_csip_set_coordinator_ordered_access_t](#ga2ce69e3bf51622fd41389a12d26e2ba9)。

以客户端身份按顺序访问协调集合设备（Coordinated Set Devices）。

<a id="r_ga2d61e25d131631479e34a2c2edf3ebfa"></a>

```c
int bt_csip_set_coordinator_lock (const struct bt_csip_set_coordinator_set_member **members, uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info)
```

相关声明：[bt_csip_set_coordinator_lock](#ga2d61e25d131631479e34a2c2edf3ebfa)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)。

锁定一个集合成员（Set Members）数组。

<a id="r_ga5391b625fbcfd66ab07e014659dc2e45"></a>

```c
int bt_csip_set_coordinator_release (const struct bt_csip_set_coordinator_set_member **members, uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info)
```

相关声明：[bt_csip_set_coordinator_release](#ga5391b625fbcfd66ab07e014659dc2e45)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)。

释放一个集合成员（Set Members）数组。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga04fcc2431bec35d53664c8f5ab18100d"></a>

### `BT_CSIP_DATA_RSI`

```c
#define BT_CSIP_DATA_RSI ( _rsi)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

展开值（Value）：

```c
BT_DATA(BT_DATA_CSIS_RSI, _rsi, BT_CSIP_RSI_SIZE)
```

声明包含 RSI 的 bt_data 数组的辅助宏。

此宏主要用于创建由 `struct bt_data` 元素组成的数组，随后可将其传给例如 `bt_le_ext_adv_start()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_rsi` | 指向 RSI 值的指针。 |

<a id="gaabd5b74d0e805bfb0b492a45445ec4c4"></a>

### `BT_CSIP_ERROR_LOCK_ALREADY_GRANTED`

```c
#define BT_CSIP_ERROR_LOCK_ALREADY_GRANTED 0x84U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

客户端已是锁的所有者（Owner of the Lock）。

<a id="ga00f382d9fe9afb55acfd6f758cef6389"></a>

### `BT_CSIP_ERROR_LOCK_DENIED`

```c
#define BT_CSIP_ERROR_LOCK_DENIED 0x80U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

服务已锁定（Already Locked）。

<a id="gaeca8a3a9e136882c200c432b9f83203e"></a>

### `BT_CSIP_ERROR_LOCK_INVAL_VALUE`

```c
#define BT_CSIP_ERROR_LOCK_INVAL_VALUE 0x82U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

锁定值（Lock Value）无效。

<a id="gac6eda3e7a9a06f86bc715df20e14daa1"></a>

### `BT_CSIP_ERROR_LOCK_RELEASE_DENIED`

```c
#define BT_CSIP_ERROR_LOCK_RELEASE_DENIED 0x81U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

服务未锁定（Not Locked）。

<a id="ga4e0da5f82ef943e660f669a2962bcc7a"></a>

### `BT_CSIP_ERROR_SIRK_OOB_ONLY`

```c
#define BT_CSIP_ERROR_SIRK_OOB_ONLY 0x83U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

SIRK 只能通过带外（Out-of-Band）方式获取。

<a id="gac2aa2ce09ff4aad8bc423dd5b5643038"></a>

### `BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT`

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT 0x00U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

接受以明文（Plaintext）读取 SIRK 的请求。

<a id="gae6422e7e38bacc39ed2f8d52efe9d6db"></a>

### `BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC`

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC 0x01U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

接受读取 SIRK 的请求，但返回加密的 SIRK（Encrypted SIRK）。

<a id="gaa245a416becaaaeb118b440f9ba2431d"></a>

### `BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY`

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY 0x03U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

SIRK 只能通过带外过程（Out-of-Band Procedure，OOB）获取。

<a id="ga0175e269097a2b6f8f303ee97527db4a"></a>

### `BT_CSIP_READ_SIRK_REQ_RSP_REJECT`

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_REJECT 0x02U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

拒绝读取 SIRK 的请求。

<a id="ga5b0149fec5d38e7003593c227b561506"></a>

### `BT_CSIP_RSI_SIZE`

```c
#define BT_CSIP_RSI_SIZE 6U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

可解析集合标识符（Resolvable Set Identifier，RSI）的大小。

<a id="ga1633e4caaa03a21da0a5431f5f263076"></a>

### `BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE`

```c
#define BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE K_SECONDS(10)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

用于成员发现（Member Discovery）的建议定时器。

<a id="ga42702049524f7ce24dfb6061120414df"></a>

### `BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES`

```c
#define BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES 0U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

定义协调集合标识集合协调器（Coordinated Set Identification Set Coordinator）的协调集合标识服务（Coordinated Set Identification Service）实例数量上限。

<a id="ga33069821c84e9b4c16c9d95d88c23158"></a>

### `BT_CSIP_SIRK_SIZE`

```c
#define BT_CSIP_SIRK_SIZE 16U
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

集合标识解析密钥（Set Identification Resolving Key，SIRK）的大小。

<a id="gaeee5f0691ba0d63a370ac5dd94cb4d5c"></a>

### `bt_csip_set_coordinator_discover_cb`

```c
typedef void(* bt_csip_set_coordinator_discover_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_set_member *member, int err, size_t set_count)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

用于发现协调集合标识服务（Coordinated Set Identification Services）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向远端设备（Remote Device）的指针。 |
| `member` | 指向集合成员（Set Member）的指针。 |
| `err` | 成功时返回 0，出错时返回 `errno` 值。 |
| `set_count` | 该成员所属集合的数量。 |

<a id="ga991ee886c814e0b72fa12ed58ef4a90b"></a>

### `bt_csip_set_coordinator_lock_changed_cb`

```c
typedef void(* bt_csip_set_coordinator_lock_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst, bool locked)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

已连接设备上的集合锁定值（Lock Value）发生变化时的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 发生变化的协同集标识服务（Coordinated Set Identification Service）实例。 |
| `locked` | 锁处于锁定（Locked）还是释放（Released）状态。 |

<a id="ga994431ea69920d9e84f35ca6e1e5f634"></a>

### `bt_csip_set_coordinator_lock_set_cb`

```c
typedef void(* bt_csip_set_coordinator_lock_set_cb) (int err)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

用于跨一个或多个设备锁定集合（Lock a Set）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时返回 0，出错时返回 `errno` 值。 |

<a id="ga0f2e0b610a4db975a72c6d9a645964cb"></a>

### `bt_csip_set_coordinator_ordered_access_cb_t`

```c
typedef void(* bt_csip_set_coordinator_ordered_access_cb_t) (const struct bt_csip_set_coordinator_set_info *set_info, int err, bool locked, struct bt_csip_set_coordinator_set_member *member)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

bt_csip_set_coordinator_ordered_access() 的回调（Callback）。

如果传给 `bt_csip_set_coordinator_ordered_access()` 的任一集合成员已锁定，则会调用此回调，其中 `locked` 为 `true`，`member` 指向已锁定成员，并取消有序访问流程（Ordered Access Procedure）。同样，发生任何错误也会中止流程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `set_info` | 指向某个具体 `set_info` 结构体的指针。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `locked` | 锁处于锁定（Locked）还是释放（Released）状态。 |
| `member` | `locked` 为 `true` 时指向已锁定成员，否则为 `NULL`。 |

<a id="ga2ce69e3bf51622fd41389a12d26e2ba9"></a>

### `bt_csip_set_coordinator_ordered_access_t`

```c
typedef bool(* bt_csip_set_coordinator_ordered_access_t) (const struct bt_csip_set_coordinator_set_info *set_info, struct bt_csip_set_coordinator_set_member *members[], size_t count)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

bt_csip_set_coordinator_ordered_access() 的回调函数定义（Callback Function Definition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `set_info` | 指向某个具体 `set_info` 结构体的指针。 |
| `members` | 按序位（Rank）排序的成员数组。必须按成员序位从低到高执行流程。 |
| `count` | `members` 中的成员数量。 |

**返回（Returns）**：返回值（Returns）：若可成功执行这些流程则返回 `true`；返回 `false` 可停止流程。

<a id="gacdb98c9ae3248064e90352387df7cef2"></a>

### `bt_csip_set_coordinator_sirk_changed_cb`

```c
typedef void(* bt_csip_set_coordinator_sirk_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

已连接设备上的集合 SIRK 值发生变化时的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 发生变化的协同集标识服务（Coordinated Set Identification Service）实例。可通过 `inst.info` 访问新的集合标识解析密钥（Set Identity Resolving Key，SIRK）。 |

<a id="gaee24f364c90cdcd0b6f49c8b297a34a7"></a>

### `bt_csip_set_coordinator_size_changed_cb`

```c
typedef void(* bt_csip_set_coordinator_size_changed_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_csis_inst *inst)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

已连接设备上的集合大小（Set Size）发生变化时的回调。

由于集合中的所有设备必须具有相同的集合大小（Set Size），如果远端设备支持集合大小通知，则每台已连接设备都可能通过通知发送同一个新的集合大小值。

集合中各设备的序位（Rank）也可能随之变化，因此建议调用 `bt_csip_set_coordinator_discover()`，重新发现并读取各设备上集合的特征值（Characteristic Values）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向远端设备（Remote Device）的指针。 |
| `inst` | 发生变化的协同集标识服务（Coordinated Set Identification Service）实例。新的集合大小存储在 `inst->info.size` 中。 |

<a id="ga7e7ea4a92bb76aded86807571a2cbb73"></a>

### `bt_csip_set_coordinator_discover()`

```c
int bt_csip_set_coordinator_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

为连接（Connection）初始化 csip_set_coordinator 实例。

这会在设备上执行发现（Discovery），并使实例准备好接受后续命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向要执行发现（Discovery）的远端设备的指针。 |

**返回（Returns）**：返回值（Returns）：`int`；成功时返回 0，出错时返回 `errno` 值。

<a id="ga6b35d73b102ef7b1db26dbd86aaf6a36"></a>

### `bt_csip_set_coordinator_is_set_member()`

```c
bool bt_csip_set_coordinator_is_set_member ( const uint8_t sirk[16U], struct bt_data * data )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

检查广播数据（Advertising Data）是否表示集合成员（Set Member）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sirk` | 要用于比对的集合的 SIRK。 |
| `data` | 广播数据（Advertising Data）。 |

**返回（Returns）**：返回值（Returns）：广播数据表明设备是集合成员时为 `true`，否则为 `false`。

<a id="ga2d61e25d131631479e34a2c2edf3ebfa"></a>

### `bt_csip_set_coordinator_lock()`

```c
int bt_csip_set_coordinator_lock ( const struct bt_csip_set_coordinator_set_member ** members, uint8_t count, const struct bt_csip_set_coordinator_set_info * set_info )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

锁定一个集合成员（Set Members）数组。

将按序位（Rank）从低到高锁定成员。

待办（TODO）：锁定失败时，已经锁定的成员不会被解锁。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `members` | 要锁定的集合成员数组。 |
| `count` | `members` 中的集合成员数量。 |
| `set_info` | 指向某个具体 `set_info` 结构体的指针，因为一个成员可能属于多个集合。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_CSIP_SET_COORDINATOR`、`CONFIG_BT_BONDABLE`。

**返回（Returns）**：返回值（Returns）：成功时返回 0，出错时返回 `errno` 值。

<a id="gacd83494562a62fbdbc7282107d4454b4"></a>

### `bt_csip_set_coordinator_ordered_access()`

```c
int bt_csip_set_coordinator_ordered_access ( const struct bt_csip_set_coordinator_set_member * members[], uint8_t count, const struct bt_csip_set_coordinator_set_info * set_info, bt_csip_set_coordinator_ordered_access_t cb )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

以客户端身份按顺序访问协调集合设备（Coordinated Set Devices）。

此函数读取所有设备的锁状态（Lock State）。若所有设备均未锁定，则调用 `cb`，传入的成员与 `members` 提供的相同，但会按序位（Rank，若存在）排序。流程结束或发生错误后，将调用 `bt_csip_set_coordinator_cb::ordered_access`。

此流程仅在所有成员都有锁特征（Lock Characteristic），且所有成员的 `rank` 都为 0，或各成员的序位均不重复时有效。

任一成员处于锁定状态时，将取消流程。

此操作只能对已绑定（Bonded）的成员执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `members` | 要访问的集合成员数组。 |
| `count` | `members` 中的集合成员数量。 |
| `set_info` | 指向某个具体 `set_info` 结构体的指针，因为一个成员可能属于多个集合。 |
| `cb` | 对每个成员调用的回调函数（Callback Function）。 |

<a id="ga08c514fda44e5a9b5cfc16be629c2b37"></a>

### `bt_csip_set_coordinator_register_cb()`

```c
int bt_csip_set_coordinator_register_cb ( struct bt_csip_set_coordinator_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

注册 csip_set_coordinator 的回调（Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，出错时返回 `errno` 值。

<a id="ga5391b625fbcfd66ab07e014659dc2e45"></a>

### `bt_csip_set_coordinator_release()`

```c
int bt_csip_set_coordinator_release ( const struct bt_csip_set_coordinator_set_member ** members, uint8_t count, const struct bt_csip_set_coordinator_set_info * set_info )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

释放一个集合成员（Set Members）数组。

将按序位（Rank）从高到低释放成员。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `members` | 要锁定的集合成员数组。 |
| `count` | `members` 中的集合成员数量。 |
| `set_info` | 指向某个具体 `set_info` 结构体的指针，因为一个成员可能属于多个集合。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_CSIP_SET_COORDINATOR`、`CONFIG_BT_BONDABLE`。

**返回（Returns）**：返回值（Returns）：成功时返回 0，出错时返回 `errno` 值。

<a id="ga8c3666d8f20f909dd4fa2010ae02c9a5"></a>

### `bt_csip_set_coordinator_set_member_by_conn()`

```c
struct bt_csip_set_coordinator_set_member * bt_csip_set_coordinator_set_member_by_conn ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

通过连接指针（Connection Pointer）获取集合成员（Set Member）。

通过连接指针获取协同集标识配置文件（CSIP）的集合协调器（Set Coordinator）指针。只能获取已通过 `bt_csip_set_coordinator_discover()` 初始化的集合协调器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接指针（Connection Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Pointer` | 指向协同集标识配置文件（CSIP）集合协调器（Set Coordinator）实例。 |
| `NULL` | `conn` 为 `NULL`，或者连接尚未完成发现（Discovery）时。 |

<a id="gae020da1a92d3babf47954c12dbbde56b"></a>

### `bt_csip_set_member_generate_rsi()`

```c
int bt_csip_set_member_generate_rsi ( const struct bt_csip_set_member_svc_inst * svc_inst, uint8_t rsi[6U] )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

生成可解析集合标识符（Resolvable Set Identifier，RSI）值。

这会为给定的 `svc_inst` 实例生成可解析集合标识符（Resolvable Set Identifier，RSI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 指向协调集合标识服务（Coordinated Set Identification Service）的指针。 |
| `rsi` | 指向新生成的 6 八位组 RSI 数据的指针，采用小端序（Little-Endian）。 |

**返回（Returns）**：返回值（Returns）：`int`；成功时为 0，出错时为 `errno`。

<a id="gad80917089bc7e629cc3cb9d7fbf6cf45"></a>

### `bt_csip_set_member_get_info()`

```c
int bt_csip_set_member_get_info ( const struct bt_csip_set_member_svc_inst * svc_inst, struct bt_csip_set_member_set_info * info )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

获取服务实例（Service Instances）的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 服务实例（Service Instance）。 |
| `info` | 指向用于存储信息的结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `svc_inst` 或 `info` 为 `NULL`。 |
| `0` | 成功。 |

<a id="ga95e2ba4b65ec42eedb26bf5ad181b606"></a>

### `bt_csip_set_member_lock()`

```c
int bt_csip_set_member_lock ( struct bt_csip_set_member_svc_inst * svc_inst, bool lock, bool force )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

锁定服务器上的特定协调集合标识服务（Coordinated Set Identification Service）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 指向协调集合标识服务（Coordinated Set Identification Service）的指针。 |
| `lock` | 为 `true` 时锁定集合，为 `false` 时释放集合。 |
| `force` | 此参数仅在 `lock` 为 `false`（释放）时有意义；它将强制释放锁，无论锁由谁获取。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT`。

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为 GATT 错误。

<a id="gab11184ace9246d4c5ead6bdc98ffa2ac"></a>

### `bt_csip_set_member_register()`

```c
int bt_csip_set_member_register ( const struct bt_csip_set_member_register_param * param, struct bt_csip_set_member_svc_inst ** svc_inst )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

注册协调集合标识服务（Coordinated Set Identification Service）实例。

注册并启用服务，使客户端可以发现它。

此操作只能以服务器（Server）身份执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` param` | 协同集标识服务（Coordinated Set Identification Service）的注册参数。 |
| `[out] svc_inst` | 指向已注册的协同集标识服务（Coordinated Set Identification Service）的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaef51ab05dbe9d8a69674f7020e8f837f"></a>

### `bt_csip_set_member_set_size_and_rank()`

```c
int bt_csip_set_member_set_size_and_rank ( struct bt_csip_set_member_svc_inst * svc_inst, uint8_t size, uint8_t rank )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

为服务实例设置新的大小（Size）和顺序号（Rank）。

此函数可动态修改服务实例的集合大小（Size）和序位（Rank）。同一集合不能有多个设备具有相同序位，调用者必须确保这一点。同样，必须同时更新集合中所有设备的集合大小。不能单独修改设备序位；只有新的集合大小与当前大小不同时，才能设置新序位。

若启用 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_NOTIFIABLE`，还会向所有已连接或已绑定（Bonded）的客户端发送通知（Notification）。

启用 `CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT` 或 `CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT` 之一时可用。未启用支持的参数（`rank` 或 `size`）不会被设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 服务实例（Service Instance）。 |
| `size` | 新的集合大小（Set Size）。 |
| `rank` | 新的序位（Rank）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `svc_inst` 为 `NULL`，`size` 小于 1，或对于可锁定的 `svc_inst`，`rank` 小于 1 或大于 `size`。 |
| `-EALREADY` | `size` 已设置为该值。 |
| `0` | 成功。 |

<a id="ga9a897ace4906a5df99cffd6cabc1b3e5"></a>

### `bt_csip_set_member_sirk()`

```c
int bt_csip_set_member_sirk ( struct bt_csip_set_member_svc_inst * svc_inst, const uint8_t sirk[16U] )
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

设置服务实例（Service Instance）的 SIRK。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 指向已注册的协同集标识服务（Coordinated Set Identification Service）的指针。 |
| `sirk` | 新的集合标识解析密钥（Set Identity Resolving Key，SIRK）。 |

<a id="gabc8d9c8d2b2f73f5e18e7fdbce95389c"></a>

### `bt_csip_set_member_svc_decl_get()`

```c
void * bt_csip_set_member_svc_decl_get ( const struct bt_csip_set_member_svc_inst * svc_inst)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

获取服务声明属性（Service Declaration Attribute）。

第一个服务属性（Service Attribute）可包含在其他任意 GATT 服务中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 指向协调集合标识服务（Coordinated Set Identification Service）的指针。 |

**返回（Returns）**：返回值（Returns）：第一个 CSIS 属性实例。

<a id="ga9ee48e36fb33ee27e689d32f08f071a1"></a>

### `bt_csip_set_member_unregister()`

```c
int bt_csip_set_member_unregister ( struct bt_csip_set_member_svc_inst * svc_inst)
```

```c
#include <zephyr/bluetooth/audio/csip.h>
```

注销协调集合标识服务（Coordinated Set Identification Service）实例。

这将注销并禁用服务实例（Service Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc_inst` | 指向已注册的协同集标识服务（Coordinated Set Identification Service）的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。


## 2.6\_原页交叉引用（Cross References）

- [bt_csip_set_member_cb](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)
- [bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)
- [bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)
- [bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/audio/csip.h](../api_file_display_chat_reference/P005_zephyr__bluetooth__audio__csip.h_文件参考.md)
- [BT_DATA](../api_file_display_management_reference/P005_zephyr__bluetooth__data.h_文件参考.md#a8481217e632522e1f322de87d745f8f0)
- [BT_DATA_CSIS_RSI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga122da4184d606ae140f8a311aaebeedd)
- [bt_le_ext_adv_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0f436c55482d9429f674303ae3aa815)
- [CONFIG_BT_CSIP_SET_COORDINATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_COORDINATOR)
- [CONFIG_BT_BONDABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BONDABLE)
- [bt_csip_set_coordinator_cb::ordered_access](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)
- [CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_SIZE_NOTIFIABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIZE_NOTIFIABLE)
- [CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)
- [CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adata_8h_html_a8481217e632522e1f322de87d745f8f0"></a>
<a id="agroup__bt__assigned__numbers__core_html_ga122da4184d606ae140f8a311aaebeedd"></a>
<a id="agroup__bt__csip_html_ga5b0149fec5d38e7003593c227b561506"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_电池服务（Battery Service，BAS）.md) · [返回大纲](大纲.md) · [下一章](P003_基于 HTTP 的固件空中升级（FOTA HTTP）.md)
