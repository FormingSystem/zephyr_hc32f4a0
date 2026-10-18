---
id: learning.zephyr-docs.api-file-display-chat-reference.page-5
title: zephyr__bluetooth__audio__csip.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_audio\_\_csip.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙协调集合标识配置文件（Coordinated Set Identification Profile，CSIP）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙协调集合标识配置文件（Coordinated Set Identification Profile，CSIP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga1633e4caaa03a21da0a5431f5f263076"></a>

```c
#define BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE K_SECONDS(10)
```

相关声明：[BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga1633e4caaa03a21da0a5431f5f263076)、[K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)。

用于成员发现（Member Discovery）的建议定时器。

<a id="r_ga42702049524f7ce24dfb6061120414df"></a>

```c
#define BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES 0U
```

相关声明：[BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga42702049524f7ce24dfb6061120414df)。

定义协调集合标识集合协调器（Coordinated Set Identification Set Coordinator）的协调集合标识服务（Coordinated Set Identification Service）实例数量上限。

<a id="r_gac2aa2ce09ff4aad8bc423dd5b5643038"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT 0x00U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gac2aa2ce09ff4aad8bc423dd5b5643038)。

接受以明文（Plaintext）读取 SIRK 的请求。

<a id="r_gae6422e7e38bacc39ed2f8d52efe9d6db"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC 0x01U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gae6422e7e38bacc39ed2f8d52efe9d6db)。

接受读取 SIRK 的请求，但返回加密的 SIRK（Encrypted SIRK）。

<a id="r_ga0175e269097a2b6f8f303ee97527db4a"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_REJECT 0x02U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0175e269097a2b6f8f303ee97527db4a)。

拒绝读取 SIRK 的请求。

<a id="r_gaa245a416becaaaeb118b440f9ba2431d"></a>

```c
#define BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY 0x03U
```

相关声明：[BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaa245a416becaaaeb118b440f9ba2431d)。

SIRK 只能通过带外过程（Out-of-Band Procedure，OOB）获取。

<a id="r_ga33069821c84e9b4c16c9d95d88c23158"></a>

```c
#define BT_CSIP_SIRK_SIZE 16U
```

相关声明：[BT_CSIP_SIRK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga33069821c84e9b4c16c9d95d88c23158)。

集合标识解析密钥（Set Identification Resolving Key，SIRK）的大小。

<a id="r_ga5b0149fec5d38e7003593c227b561506"></a>

```c
#define BT_CSIP_RSI_SIZE 6U
```

相关声明：[BT_CSIP_RSI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5b0149fec5d38e7003593c227b561506)。

可解析集合标识符（Resolvable Set Identifier，RSI）的大小。

<a id="r_ga00f382d9fe9afb55acfd6f758cef6389"></a>

```c
#define BT_CSIP_ERROR_LOCK_DENIED 0x80U
```

相关声明：[BT_CSIP_ERROR_LOCK_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga00f382d9fe9afb55acfd6f758cef6389)。

服务已锁定（Already Locked）。

<a id="r_gac6eda3e7a9a06f86bc715df20e14daa1"></a>

```c
#define BT_CSIP_ERROR_LOCK_RELEASE_DENIED 0x81U
```

相关声明：[BT_CSIP_ERROR_LOCK_RELEASE_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gac6eda3e7a9a06f86bc715df20e14daa1)。

服务未锁定（Not Locked）。

<a id="r_gaeca8a3a9e136882c200c432b9f83203e"></a>

```c
#define BT_CSIP_ERROR_LOCK_INVAL_VALUE 0x82U
```

相关声明：[BT_CSIP_ERROR_LOCK_INVAL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeca8a3a9e136882c200c432b9f83203e)。

锁定值（Lock Value）无效。

<a id="r_ga4e0da5f82ef943e660f669a2962bcc7a"></a>

```c
#define BT_CSIP_ERROR_SIRK_OOB_ONLY 0x83U
```

相关声明：[BT_CSIP_ERROR_SIRK_OOB_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga4e0da5f82ef943e660f669a2962bcc7a)。

SIRK 只能通过带外（Out-of-Band）方式获取。

<a id="r_gaabd5b74d0e805bfb0b492a45445ec4c4"></a>

```c
#define BT_CSIP_ERROR_LOCK_ALREADY_GRANTED 0x84U
```

相关声明：[BT_CSIP_ERROR_LOCK_ALREADY_GRANTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaabd5b74d0e805bfb0b492a45445ec4c4)。

客户端已是锁的所有者（Owner of the Lock）。

<a id="r_ga04fcc2431bec35d53664c8f5ab18100d"></a>

```c
#define BT_CSIP_DATA_RSI(_rsi)
```

相关声明：[BT_CSIP_DATA_RSI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga04fcc2431bec35d53664c8f5ab18100d)。

声明包含 RSI 的 bt_data 数组的辅助宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gaeee5f0691ba0d63a370ac5dd94cb4d5c"></a>

```c
typedef void(* bt_csip_set_coordinator_discover_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_set_member *member, int err, size_t set_count)
```

相关声明：[bt_csip_set_coordinator_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeee5f0691ba0d63a370ac5dd94cb4d5c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

用于发现协调集合标识服务（Coordinated Set Identification Services）的回调。

<a id="r_ga994431ea69920d9e84f35ca6e1e5f634"></a>

```c
typedef void(* bt_csip_set_coordinator_lock_set_cb) (int err)
```

相关声明：[bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)。

用于跨一个或多个设备锁定集合（Lock a Set）的回调。

<a id="r_ga991ee886c814e0b72fa12ed58ef4a90b"></a>

```c
typedef void(* bt_csip_set_coordinator_lock_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst, bool locked)
```

相关声明：[bt_csip_set_coordinator_lock_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga991ee886c814e0b72fa12ed58ef4a90b)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

已连接设备上的集合锁定值（Lock Value）发生变化时的回调。

<a id="r_gacdb98c9ae3248064e90352387df7cef2"></a>

```c
typedef void(* bt_csip_set_coordinator_sirk_changed_cb) (struct bt_csip_set_coordinator_csis_inst *inst)
```

相关声明：[bt_csip_set_coordinator_sirk_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacdb98c9ae3248064e90352387df7cef2)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

已连接设备上的集合 SIRK 值发生变化时的回调。

<a id="r_gaee24f364c90cdcd0b6f49c8b297a34a7"></a>

```c
typedef void(* bt_csip_set_coordinator_size_changed_cb) (struct bt_conn *conn, const struct bt_csip_set_coordinator_csis_inst *inst)
```

相关声明：[bt_csip_set_coordinator_size_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaee24f364c90cdcd0b6f49c8b297a34a7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)。

已连接设备上的集合大小（Set Size）发生变化时的回调。

<a id="r_ga0f2e0b610a4db975a72c6d9a645964cb"></a>

```c
typedef void(* bt_csip_set_coordinator_ordered_access_cb_t) (const struct bt_csip_set_coordinator_set_info *set_info, int err, bool locked, struct bt_csip_set_coordinator_set_member *member)
```

相关声明：[bt_csip_set_coordinator_ordered_access_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0f2e0b610a4db975a72c6d9a645964cb)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

bt_csip_set_coordinator_ordered_access() 的回调（Callback）。

<a id="r_ga2ce69e3bf51622fd41389a12d26e2ba9"></a>

```c
typedef bool(* bt_csip_set_coordinator_ordered_access_t) (const struct bt_csip_set_coordinator_set_info *set_info, struct bt_csip_set_coordinator_set_member *members[], size_t count)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_ordered_access_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2ce69e3bf51622fd41389a12d26e2ba9)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)。

bt_csip_set_coordinator_ordered_access() 的回调函数定义（Callback Function Definition）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_gabc8d9c8d2b2f73f5e18e7fdbce95389c"></a>

```c
void * bt_csip_set_member_svc_decl_get (const struct bt_csip_set_member_svc_inst *svc_inst)
```

相关声明：[bt_csip_set_member_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gabc8d9c8d2b2f73f5e18e7fdbce95389c)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_gab11184ace9246d4c5ead6bdc98ffa2ac"></a>

```c
int bt_csip_set_member_register (const struct bt_csip_set_member_register_param *param, struct bt_csip_set_member_svc_inst **svc_inst)
```

相关声明：[bt_csip_set_member_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gab11184ace9246d4c5ead6bdc98ffa2ac)、[bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注册协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga9ee48e36fb33ee27e689d32f08f071a1"></a>

```c
int bt_csip_set_member_unregister (struct bt_csip_set_member_svc_inst *svc_inst)
```

相关声明：[bt_csip_set_member_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9ee48e36fb33ee27e689d32f08f071a1)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注销协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga9a897ace4906a5df99cffd6cabc1b3e5"></a>

```c
int bt_csip_set_member_sirk (struct bt_csip_set_member_svc_inst *svc_inst, const uint8_t sirk[16U])
```

相关声明：[bt_csip_set_member_sirk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9a897ace4906a5df99cffd6cabc1b3e5)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置服务实例（Service Instance）的 SIRK。

<a id="r_gaef51ab05dbe9d8a69674f7020e8f837f"></a>

```c
int bt_csip_set_member_set_size_and_rank (struct bt_csip_set_member_svc_inst *svc_inst, uint8_t size, uint8_t rank)
```

相关声明：[bt_csip_set_member_set_size_and_rank](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaef51ab05dbe9d8a69674f7020e8f837f)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为服务实例设置新的大小（Size）和顺序号（Rank）。

<a id="r_gad80917089bc7e629cc3cb9d7fbf6cf45"></a>

```c
int bt_csip_set_member_get_info (const struct bt_csip_set_member_svc_inst *svc_inst, struct bt_csip_set_member_set_info *info)
```

相关声明：[bt_csip_set_member_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gad80917089bc7e629cc3cb9d7fbf6cf45)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)。

获取服务实例（Service Instances）的信息。

<a id="r_gae020da1a92d3babf47954c12dbbde56b"></a>

```c
int bt_csip_set_member_generate_rsi (const struct bt_csip_set_member_svc_inst *svc_inst, uint8_t rsi[6U])
```

相关声明：[bt_csip_set_member_generate_rsi](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gae020da1a92d3babf47954c12dbbde56b)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

生成可解析集合标识符（Resolvable Set Identifier，RSI）值。

<a id="r_ga95e2ba4b65ec42eedb26bf5ad181b606"></a>

```c
int bt_csip_set_member_lock (struct bt_csip_set_member_svc_inst *svc_inst, bool lock, bool force)
```

相关声明：[bt_csip_set_member_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga95e2ba4b65ec42eedb26bf5ad181b606)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

锁定服务器上的特定协调集合标识服务（Coordinated Set Identification Service）实例。

<a id="r_ga7e7ea4a92bb76aded86807571a2cbb73"></a>

```c
int bt_csip_set_coordinator_discover (struct bt_conn *conn)
```

相关声明：[bt_csip_set_coordinator_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga7e7ea4a92bb76aded86807571a2cbb73)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接（Connection）初始化 csip_set_coordinator 实例。

<a id="r_ga8c3666d8f20f909dd4fa2010ae02c9a5"></a>

```c
struct bt_csip_set_coordinator_set_member * bt_csip_set_coordinator_set_member_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[bt_csip_set_coordinator_set_member_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga8c3666d8f20f909dd4fa2010ae02c9a5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通过连接指针（Connection Pointer）获取集合成员（Set Member）。

<a id="r_ga6b35d73b102ef7b1db26dbd86aaf6a36"></a>

```c
bool bt_csip_set_coordinator_is_set_member (const uint8_t sirk[16U], struct bt_data *data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_csip_set_coordinator_is_set_member](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga6b35d73b102ef7b1db26dbd86aaf6a36)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

检查广播数据（Advertising Data）是否表示集合成员（Set Member）。

<a id="r_ga08c514fda44e5a9b5cfc16be629c2b37"></a>

```c
int bt_csip_set_coordinator_register_cb (struct bt_csip_set_coordinator_cb *cb)
```

相关声明：[bt_csip_set_coordinator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga08c514fda44e5a9b5cfc16be629c2b37)、[bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)。

注册 csip_set_coordinator 的回调（Callbacks）。

<a id="r_gacd83494562a62fbdbc7282107d4454b4"></a>

```c
int bt_csip_set_coordinator_ordered_access (const struct bt_csip_set_coordinator_set_member *members[], uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info, bt_csip_set_coordinator_ordered_access_t cb)
```

相关声明：[bt_csip_set_coordinator_ordered_access](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacd83494562a62fbdbc7282107d4454b4)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)、[bt_csip_set_coordinator_ordered_access_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2ce69e3bf51622fd41389a12d26e2ba9)。

以客户端身份按顺序访问协调集合设备（Coordinated Set Devices）。

<a id="r_ga2d61e25d131631479e34a2c2edf3ebfa"></a>

```c
int bt_csip_set_coordinator_lock (const struct bt_csip_set_coordinator_set_member **members, uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info)
```

相关声明：[bt_csip_set_coordinator_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2d61e25d131631479e34a2c2edf3ebfa)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)。

锁定一个集合成员（Set Members）数组。

<a id="r_ga5391b625fbcfd66ab07e014659dc2e45"></a>

```c
int bt_csip_set_coordinator_release (const struct bt_csip_set_coordinator_set_member **members, uint8_t count, const struct bt_csip_set_coordinator_set_info *set_info)
```

相关声明：[bt_csip_set_coordinator_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5391b625fbcfd66ab07e014659dc2e45)、[bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)。

释放一个集合成员（Set Members）数组。


## 5.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/gap.h](../api_source_transport_clock_reference/P016_gap.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P014_csip.h_源码浏览.md)
- [bt_csip_set_member_cb](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)
- [bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)
- [bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)
- [bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)
- [BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga1633e4caaa03a21da0a5431f5f263076)
- [K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga42702049524f7ce24dfb6061120414df)
- [BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gac2aa2ce09ff4aad8bc423dd5b5643038)
- [BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gae6422e7e38bacc39ed2f8d52efe9d6db)
- [BT_CSIP_READ_SIRK_REQ_RSP_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0175e269097a2b6f8f303ee97527db4a)
- [BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaa245a416becaaaeb118b440f9ba2431d)
- [BT_CSIP_SIRK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga33069821c84e9b4c16c9d95d88c23158)
- [BT_CSIP_RSI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5b0149fec5d38e7003593c227b561506)
- [BT_CSIP_ERROR_LOCK_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga00f382d9fe9afb55acfd6f758cef6389)
- [BT_CSIP_ERROR_LOCK_RELEASE_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gac6eda3e7a9a06f86bc715df20e14daa1)
- [BT_CSIP_ERROR_LOCK_INVAL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeca8a3a9e136882c200c432b9f83203e)
- [BT_CSIP_ERROR_SIRK_OOB_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga4e0da5f82ef943e660f669a2962bcc7a)
- [BT_CSIP_ERROR_LOCK_ALREADY_GRANTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaabd5b74d0e805bfb0b492a45445ec4c4)
- [BT_CSIP_DATA_RSI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga04fcc2431bec35d53664c8f5ab18100d)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_csip_set_coordinator_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeee5f0691ba0d63a370ac5dd94cb4d5c)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)
- [bt_csip_set_coordinator_lock_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga991ee886c814e0b72fa12ed58ef4a90b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_csip_set_coordinator_sirk_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacdb98c9ae3248064e90352387df7cef2)
- [bt_csip_set_coordinator_size_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaee24f364c90cdcd0b6f49c8b297a34a7)
- [bt_csip_set_coordinator_ordered_access_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0f2e0b610a4db975a72c6d9a645964cb)
- [bt_csip_set_coordinator_ordered_access()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacd83494562a62fbdbc7282107d4454b4)
- [bt_csip_set_coordinator_ordered_access_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2ce69e3bf51622fd41389a12d26e2ba9)
- [bt_csip_set_member_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gabc8d9c8d2b2f73f5e18e7fdbce95389c)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [bt_csip_set_member_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gab11184ace9246d4c5ead6bdc98ffa2ac)
- [bt_csip_set_member_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9ee48e36fb33ee27e689d32f08f071a1)
- [bt_csip_set_member_sirk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9a897ace4906a5df99cffd6cabc1b3e5)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_csip_set_member_set_size_and_rank](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaef51ab05dbe9d8a69674f7020e8f837f)
- [bt_csip_set_member_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gad80917089bc7e629cc3cb9d7fbf6cf45)
- [bt_csip_set_member_generate_rsi](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gae020da1a92d3babf47954c12dbbde56b)
- [bt_csip_set_member_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga95e2ba4b65ec42eedb26bf5ad181b606)
- [bt_csip_set_coordinator_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga7e7ea4a92bb76aded86807571a2cbb73)
- [bt_csip_set_coordinator_set_member_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga8c3666d8f20f909dd4fa2010ae02c9a5)
- [bt_csip_set_coordinator_is_set_member](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga6b35d73b102ef7b1db26dbd86aaf6a36)
- [bt_csip_set_coordinator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga08c514fda44e5a9b5cfc16be629c2b37)
- [bt_csip_set_coordinator_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2d61e25d131631479e34a2c2edf3ebfa)
- [bt_csip_set_coordinator_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5391b625fbcfd66ab07e014659dc2e45)

<a id="header-details"></a>

---

[上一章](P004_zephyr__modem__chat.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__display.h_文件参考.md)
