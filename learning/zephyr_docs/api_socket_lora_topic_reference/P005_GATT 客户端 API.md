---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-5
title: GATT 客户端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_GATT 客户端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fgatt_5Fexchange_5Fparams"></a>

```c
struct bt_gatt_exchange_params
```

相关声明：[bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)。

GATT 最大传输单元交换（Exchange MTU）参数。

<a id="r_bt_5Fgatt_5Fdiscover_5Fparams"></a>

```c
struct bt_gatt_discover_params
```

相关声明：[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

GATT 属性发现（Discover Attributes）参数。

<a id="r_bt_5Fgatt_5Fread_5Fparams"></a>

```c
struct bt_gatt_read_params
```

相关声明：[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)。

GATT 读取（Read）参数。

<a id="r_bt_5Fgatt_5Fwrite_5Fparams"></a>

```c
struct bt_gatt_write_params
```

相关声明：[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

GATT 写入（Write）参数。

<a id="r_bt_5Fgatt_5Fsubscribe_5Fparams"></a>

```c
struct bt_gatt_subscribe_params
```

相关声明：[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

GATT 订阅（Subscribe）参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga7ca44e95989a143ae0b21e4a5316561d"></a>

```c
#define BT_GATT_AUTO_DISCOVER_CCC_HANDLE 0x0000U
```

相关声明：[BT_GATT_AUTO_DISCOVER_CCC_HANDLE](#ga7ca44e95989a143ae0b21e4a5316561d)。

用于表示自动发现客户端特征配置（CCC）的句柄值（Handle Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gabd3bcd3c1560956726574faed332fb13"></a>

```c
typedef uint8_t(* bt_gatt_discover_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, struct bt_gatt_discover_params *params)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_discover_func_t](#gabd3bcd3c1560956726574faed332fb13)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

发现属性回调函数（Discover Attribute Callback Function）。

<a id="r_ga1ca94b4f2b6c456b6134e05127993569"></a>

```c
typedef uint8_t(* bt_gatt_read_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_read_params *params, const void *data, uint16_t length)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_read_func_t](#ga1ca94b4f2b6c456b6134e05127993569)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取回调函数（Read Callback Function）。

<a id="r_ga2bca8c4a45f41e0400a9e0147f4baf50"></a>

```c
typedef void(* bt_gatt_write_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_write_params *params)
```

相关声明：[bt_gatt_write_func_t](#ga2bca8c4a45f41e0400a9e0147f4baf50)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

写入回调函数（Write Callback Function）。

<a id="r_gab3e53eb5f9bb1eda7bf612ef95755b4d"></a>

```c
typedef uint8_t(* bt_gatt_notify_func_t) (struct bt_conn *conn, struct bt_gatt_subscribe_params *params, const void *data, uint16_t length)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_notify_func_t](#gab3e53eb5f9bb1eda7bf612ef95755b4d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通知回调函数（Notification Callback Function）。

<a id="r_ga2e914e63b4b91fa56bc3295283c43714"></a>

```c
typedef void(* bt_gatt_subscribe_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_subscribe_func_t](#ga2e914e63b4b91fa56bc3295283c43714)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

订阅回调函数（Subscription Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_gaea89c65f17050820d54568f636b6554a"></a>

```c
enum bt_gatt_discover_type { BT_GATT_DISCOVER_PRIMARY , BT_GATT_DISCOVER_SECONDARY , BT_GATT_DISCOVER_INCLUDE , BT_GATT_DISCOVER_CHARACTERISTIC , BT_GATT_DISCOVER_DESCRIPTOR , BT_GATT_DISCOVER_ATTRIBUTE , BT_GATT_DISCOVER_STD_CHAR_DESC }
```

相关声明：[bt_gatt_discover_type](#gaea89c65f17050820d54568f636b6554a)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_PRIMARY`。](#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_SECONDARY`。](#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_INCLUDE`。](#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_CHARACTERISTIC`。](#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_DESCRIPTOR`。](#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_ATTRIBUTE`。](#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c)、[发现类型（Discovery Type）：`BT_GATT_DISCOVER_STD_CHAR_DESC`。](#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61)。

GATT 发现类型（Discover Types）。

<a id="r_gaa43f45658809908baa72bf4e0ea745ac"></a>

```c
enum bt_gatt_sub_flag { BT_GATT_SUBSCRIBE_FLAG_VOLATILE , BT_GATT_SUBSCRIBE_FLAG_NO_RESUB , BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING , BT_GATT_SUBSCRIBE_FLAG_SENT , BT_GATT_SUBSCRIBE_NUM_FLAGS }
```

相关声明：[bt_gatt_sub_flag](#gaa43f45658809908baa72bf4e0ea745ac)、[BT_GATT_SUBSCRIBE_FLAG_VOLATILE](#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb)、[BT_GATT_SUBSCRIBE_FLAG_NO_RESUB](#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6)、[BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING](#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad)、[BT_GATT_SUBSCRIBE_FLAG_SENT](#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab)、[BT_GATT_SUBSCRIBE_NUM_FLAGS](#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)。

订阅标志（Subscription Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_ga0f41da23c6559a8254b04295aff8198d"></a>

```c
int bt_gatt_exchange_mtu (struct bt_conn *conn, struct bt_gatt_exchange_params *params)
```

相关声明：[函数（Function）：`bt_gatt_exchange_mtu`。](#ga0f41da23c6559a8254b04295aff8198d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)。

交换最大传输单元（MTU）。

<a id="r_gac06a945e5f7939b6716bc4f2cea781bd"></a>

```c
int bt_gatt_discover (struct bt_conn *conn, struct bt_gatt_discover_params *params)
```

相关声明：[函数（Function）：`bt_gatt_discover`。](#gac06a945e5f7939b6716bc4f2cea781bd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)。

GATT 发现函数（Discover Function）。

<a id="r_ga1a18dd726ab960a88d7f85f2a014141a"></a>

```c
int bt_gatt_read (struct bt_conn *conn, struct bt_gatt_read_params *params)
```

相关声明：[函数（Function）：`bt_gatt_read`。](#ga1a18dd726ab960a88d7f85f2a014141a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)。

按句柄读取属性值（Attribute Value）。

<a id="r_ga843a42e68e0497d88d3f655f8ffd58d4"></a>

```c
int bt_gatt_write (struct bt_conn *conn, struct bt_gatt_write_params *params)
```

相关声明：[函数（Function）：`bt_gatt_write`。](#ga843a42e68e0497d88d3f655f8ffd58d4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)。

按句柄写入属性值（Attribute Value）。

<a id="r_ga49439413d12b5a8a1c68735e961ab6fa"></a>

```c
int bt_gatt_write_without_response_cb (struct bt_conn *conn, uint16_t handle, const void *data, uint16_t length, bool sign, bt_gatt_complete_func_t func, void *user_data)
```

相关声明：[bt_gatt_write_without_response_cb](#ga49439413d12b5a8a1c68735e961ab6fa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)。

按句柄执行无响应属性值写入（Write Without Response），带回调。

<a id="r_ga9fc78e32230637a6f092da2400c50fe7"></a>

```c
static int bt_gatt_write_without_response (struct bt_conn *conn, uint16_t handle, const void *data, uint16_t length, bool sign)
```

相关声明：[bt_gatt_write_without_response](#ga9fc78e32230637a6f092da2400c50fe7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

按句柄执行无响应属性值写入（Write Without Response）。

<a id="r_ga7d4a8e18f51ba6476886a15f81f48e5c"></a>

```c
int bt_gatt_subscribe (struct bt_conn *conn, struct bt_gatt_subscribe_params *params)
```

相关声明：[函数（Function）：`bt_gatt_subscribe`。](#ga7d4a8e18f51ba6476886a15f81f48e5c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

订阅属性值通知（Attribute Value Notification）。

<a id="r_ga791b8bb8a4c085b022fafc0535a63511"></a>

```c
int bt_gatt_resubscribe (uint8_t id, const bt_addr_le_t *peer, struct bt_gatt_subscribe_params *params)
```

相关声明：[bt_gatt_resubscribe](#ga791b8bb8a4c085b022fafc0535a63511)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

重新订阅属性值通知（Attribute Value Notification）。

<a id="r_ga56509c9b8f73f729cfa5e75be22d79ae"></a>

```c
int bt_gatt_unsubscribe (struct bt_conn *conn, struct bt_gatt_subscribe_params *params)
```

相关声明：[函数（Function）：`bt_gatt_unsubscribe`。](#ga56509c9b8f73f729cfa5e75be22d79ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)。

取消订阅属性值通知（Attribute Value Notification）。

<a id="r_ga5193dea59a016692f94cf950d6b4f4f7"></a>

```c
void bt_gatt_cancel (struct bt_conn *conn, void *params)
```

相关声明：[bt_gatt_cancel](#ga5193dea59a016692f94cf950d6b4f4f7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

尝试取消 params 标识的第一个待处理请求（Pending Request）。

## 5.6\_详细说明（Detailed Documentation）

<a id="ga7ca44e95989a143ae0b21e4a5316561d"></a>

### `BT_GATT_AUTO_DISCOVER_CCC_HANDLE`

```c
#define BT_GATT_AUTO_DISCOVER_CCC_HANDLE 0x0000U
```

```c
#include <zephyr/bluetooth/gatt.h>
```

用于表示自动发现客户端特征配置（CCC）的句柄值（Handle Value）。

<a id="gabd3bcd3c1560956726574faed332fb13"></a>

### `bt_gatt_discover_func_t`

```c
typedef uint8_t(* bt_gatt_discover_func_t) (struct bt_conn *conn, const struct bt_gatt_attr *attr, struct bt_gatt_discover_params *params)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

发现属性回调函数（Discover Attribute Callback Function）。

发现过程（Discovery Procedure）完成时，将以 `attr` 为 `NULL` 调用此回调。如果过程通过返回 `BT_GATT_ITER_STOP` 而停止，则不会发生此次调用。

属性对象（Attribute Object）及其 UUID 和值对象都是临时对象；若要缓存其信息，必须复制这些对象。

`attr->user_data` 的实际类型（Effective Type）由 `params` 决定。注意，发现过程（Discovery Procedure）不会修改 `params->type` 和 `params->uuid` 字段。

也应考虑按类型读取（Read-by-type）是否比发现（Discovery）更方便。参见将 `bt_gatt_read_params::handle_count` 设为 `0` 的 `bt_gatt_read` 用法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 找到的属性（Attribute）；未找到时为 `NULL`。 |
| `params` | 提供的发现参数（Discovery Parameters）。 |

| 参数字段（Parameter Field）：`params->type`。 | 参数字段（Parameter Field）：`params->uuid`。 | `attr->user_data` 的类型（Type）。 |
| --- | --- | --- |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_PRIMARY`。 | 任意（Any）。 | 类型（Type）：`bt_gatt_service_val`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_SECONDARY`。 | 任意（Any）。 | 类型（Type）：`bt_gatt_service_val`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_INCLUDE`。 | 任意（Any）。 | 类型（Type）：`bt_gatt_include`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_CHARACTERISTIC`。 | 任意（Any）。 | 类型（Type）：`bt_gatt_chrc`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_STD_CHAR_DESC`。 | 特征扩展属性 UUID（Characteristic Extended Properties UUID）：`BT_UUID_GATT_CEP`。 | 类型（Type）：`bt_gatt_cep`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_STD_CHAR_DESC`。 | 客户端特征配置 UUID（Client Characteristic Configuration UUID）：`BT_UUID_GATT_CCC`。 | 类型（Type）：`bt_gatt_ccc`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_STD_CHAR_DESC`。 | 服务器特征配置 UUID（Server Characteristic Configuration UUID）：`BT_UUID_GATT_SCC`。 | 类型（Type）：`bt_gatt_scc`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_STD_CHAR_DESC`。 | 特征呈现格式 UUID（Characteristic Presentation Format UUID）：`BT_UUID_GATT_CPF`。 | 类型（Type）：`bt_gatt_cpf`。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_DESCRIPTOR`。 | 任意（Any）。 | 空指针（`NULL`）。 |
| 发现类型（Discovery Type）：`BT_GATT_DISCOVER_ATTRIBUTE`。 | 任意（Any）。 | 空指针（`NULL`）。 |

**说明（Note）**：注意（Note）：虽然 `bt_gatt_attr` 作为参数传给 `bt_gatt_discover` 函数，但它并不是该类型的完整对象。`bt_gatt_attr::perm` 以及 `bt_gatt_attr.read()`、`bt_gatt_attr.write()` 方法不可用，将此指针传给 GATT 服务器 API 是不安全的。属性中只有以下字段包含有效信息：`uuid` 是表示属性类型的 UUID；`handle` 是远端数据库中的句柄（Handle）；`user_data` 是属性值，但仅当发现类型映射到能够提供该信息的 ATT 操作时有效，否则为 `NULL`。详见下文。

**返回（Returns）**：返回值（Returns）：`BT_GATT_ITER_CONTINUE` 表示继续发现过程（Discovery Procedure），`BT_GATT_ITER_STOP` 表示停止发现过程。

<a id="gab3e53eb5f9bb1eda7bf612ef95755b4d"></a>

### `bt_gatt_notify_func_t`

```c
typedef uint8_t(* bt_gatt_notify_func_t) (struct bt_conn *conn, struct bt_gatt_subscribe_params *params, const void *data, uint16_t length)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

通知回调函数（Notification Callback Function）。

对于空通知（Empty Notification），`data` 指针不为 `NULL`，但 `length` 为 `0`；这是因为 `data` 为 `NULL` 有特殊含义，表示已经取消订阅（Unsubscribed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。可以为 NULL，表示正在取消与对端的配对。 |
| `params` | 订阅参数（Subscription Parameters）。 |
| `data` | 属性值数据（Attribute Value Data）。若为 NULL，表示订阅已移除。 |
| `length` | 属性值长度（Attribute Value Length）。 |

**返回（Returns）**：返回值（Returns）：`BT_GATT_ITER_CONTINUE` 表示继续接收值通知（Value Notifications），`BT_GATT_ITER_STOP` 表示取消值通知订阅。

<a id="ga1ca94b4f2b6c456b6134e05127993569"></a>

### `bt_gatt_read_func_t`

```c
typedef uint8_t(* bt_gatt_read_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_read_params *params, const void *data, uint16_t length)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

读取回调函数（Read Callback Function）。

使用 `by_uuid` 读取时，`params->start_handle` 为该数据项的属性句柄（Attribute Handle）。

如果接收的数据长度无效，将以错误码 `BT_ATT_ERR_INVALID_PDU` 调用回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `err` | ATT 错误码（Error Code）。 |
| `params` | 所使用的读取参数（Read Parameters）。 |
| `data` | 属性值数据（Attribute Value Data）。`NULL` 表示读取已经完成。 |
| `length` | 属性值长度（Attribute Value Length）。 |

**返回（Returns）**：返回值（Returns）：需要继续读取下一个属性（Attribute）时返回 `BT_GATT_ITER_CONTINUE`；停止时返回 `BT_GATT_ITER_STOP`。

<a id="ga2e914e63b4b91fa56bc3295283c43714"></a>

### `bt_gatt_subscribe_func_t`

```c
typedef void(* bt_gatt_subscribe_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_subscribe_params *params)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

订阅回调函数（Subscription Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `err` | ATT 错误码（Error Code）。 |
| `params` | 所使用的订阅参数（Subscription Parameters）。 |

<a id="ga2bca8c4a45f41e0400a9e0147f4baf50"></a>

### `bt_gatt_write_func_t`

```c
typedef void(* bt_gatt_write_func_t) (struct bt_conn *conn, uint8_t err, struct bt_gatt_write_params *params)
```

```c
#include <zephyr/bluetooth/gatt.h>
```

写入回调函数（Write Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `err` | ATT 错误码（Error Code）。 |
| `params` | 所使用的写入参数（Write Parameters）。 |

<a id="gaea89c65f17050820d54568f636b6554a"></a>

### `bt_gatt_discover_type`

```c
enum bt_gatt_discover_type
```

```c
#include <zephyr/bluetooth/gatt.h>
```

GATT 发现类型（Discover Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GATT_DISCOVER_PRIMARY` | 发现主服务（Primary Services）。 |
| `BT_GATT_DISCOVER_SECONDARY` | 发现次服务（Secondary Services）。 |
| `BT_GATT_DISCOVER_INCLUDE` | 发现包含服务（Included Services）。 |
| `BT_GATT_DISCOVER_CHARACTERISTIC` | 发现特征值（Characteristic Values）。发现特征值及其性质（Properties）。 |
| `BT_GATT_DISCOVER_DESCRIPTOR` | 发现描述符（Descriptors）。发现既不是服务（Service）也不是特征（Characteristic）的属性（Attribute）。注意（Note）：不建议在跨越多个服务／特征的范围内使用此发现类型，因为可能增加额外的往返交互（Round Trips）。 |
| `BT_GATT_DISCOVER_ATTRIBUTE` | 发现属性（Attributes）。发现任意类型的属性。注意（Note）：不建议在跨越多个服务／特征的范围内使用此发现类型，因为可能增加往返交互（Round Trips）。 |
| `BT_GATT_DISCOVER_STD_CHAR_DESC` | 发现标准特征描述符值（Standard Characteristic Descriptor Values）。发现标准特征描述符值及其性质（Properties）。支持的描述符包括：特征扩展属性（Characteristic Extended Properties）、客户端特征配置（Client Characteristic Configuration）、服务器特征配置（Server Characteristic Configuration）、特征呈现格式（Characteristic Presentation Format）。 |

**说明（Note）**：注意（Note）：不建议在跨越多个服务（Service）／特征（Characteristic）的范围内使用此发现类型，因为可能增加额外的往返交互（Round Trips）。

**说明（Note）**：注意（Note）：不建议在跨越多个服务（Service）／特征（Characteristic）的范围内使用此发现类型，因为可能增加往返交互（Round Trips）。

<a id="gaa43f45658809908baa72bf4e0ea745ac"></a>

### `bt_gatt_sub_flag`

```c
enum bt_gatt_sub_flag
```

```c
#include <zephyr/bluetooth/gatt.h>
```

订阅标志（Subscription Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GATT_SUBSCRIBE_FLAG_VOLATILE` | 持久性标志（Persistence Flag）。设置此标志表示订阅（Subscription）不会保存在 GATT 服务器端。因此，断开连接时，订阅会自动从客户端订阅列表移除；客户端重新连接时必须重新发起订阅。 |
| `BT_GATT_SUBSCRIBE_FLAG_NO_RESUB` | 禁止重新订阅标志（No Resubscribe Flag）。默认情况下，未设置 `BT_GATT_SUBSCRIBE_FLAG_VOLATILE` 时，客户端重新连接会自动续订（Renew Subscription），以兼容不会持久保存订阅的 GATT 服务器。此标志禁用自动重新订阅。如果应用层知道 GATT 服务器会记住先前连接的订阅，并希望避免重新续订，则可以使用此标志。 |
| `BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING` | 写入待处理标志（Write Pending Flag）。设置此标志表示写操作（Write Operation）处于待处理状态，正在等待远端响应。注意（Note）：仅供内部使用。 |
| `BT_GATT_SUBSCRIBE_FLAG_SENT` | 已发送标志（Sent Flag）。设置此标志表示已在当前活动连接中发送订阅请求（Subscription Request，即 CCC 写入）。启用 `CONFIG_BT_GATT_AUTO_RESUBSCRIBE` 兼容处理（Quirk）时，用于避免多次发送订阅请求。注意（Note）：仅供内部使用。 |
| `BT_GATT_SUBSCRIBE_NUM_FLAGS` |  |

**说明（Note）**：注意（Note）：仅供内部使用（Internal Use Only）。

**说明（Note）**：注意（Note）：仅供内部使用（Internal Use Only）。

<a id="ga5193dea59a016692f94cf950d6b4f4f7"></a>

### `bt_gatt_cancel()`

```c
void bt_gatt_cancel ( struct bt_conn * conn, void * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

尝试取消 params 标识的第一个待处理请求（Pending Request）。

此函数不会释放 `params` 以供复用；请求的常规回调（Callback）仍然适用。成功取消时会模拟服务器返回 `BT_ATT_ERR_UNLIKELY` 响应。

此函数可以取消以下请求函数（Request Functions）发起的请求：

- 函数（Function）：`bt_gatt_exchange_mtu`。
- 函数（Function）：`bt_gatt_discover`。
- 函数（Function）：`bt_gatt_read`。
- 函数（Function）：`bt_gatt_write`。
- 函数（Function）：`bt_gatt_subscribe`。
- 函数（Function）：`bt_gatt_unsubscribe`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求所使用的连接（Connection）。 |
| `params` | 请求函数调用中使用的 `params` 地址。 |

<a id="gac06a945e5f7939b6716bc4f2cea781bd"></a>

### `bt_gatt_discover()`

```c
int bt_gatt_discover ( struct bt_conn * conn, struct bt_gatt_discover_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

GATT 发现函数（Discover Function）。

客户端（Client）使用此过程发现服务器（Server）上的属性（Attributes）。

主服务发现（Primary Service Discovery）：通过发现全部主服务（Discover All Primary Services）或按服务 UUID 发现主服务（Discover Primary Services by Service UUID）来发现主服务。包含服务发现（Include Service Discovery）：发现指定范围内的全部包含服务。特征发现（Characteristic Discovery）：发现指定句柄范围内的全部特征，也可以发现具有指定 UUID 的特征。描述符发现（Descriptors Discovery）：发现指定范围内的全部特征描述符。

每找到一个属性（Attribute），就调用一次回调（Callback），由回调决定继续发现还是停止。

响应通过 `params->func` 回调返回。回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。`params` 必须一直保持有效，直到 `attr` 为 `NULL` 的迭代回调开始，或回调将返回 `BT_GATT_ITER_STOP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 发现参数（Discover Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->func`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |

<a id="ga0f41da23c6559a8254b04295aff8198d"></a>

### `bt_gatt_exchange_mtu()`

```c
int bt_gatt_exchange_mtu ( struct bt_conn * conn, struct bt_gatt_exchange_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

交换最大传输单元（MTU）。

此客户端过程每个连接只能使用一次，用于将最大传输单元（MTU）设为缓冲区能够容纳的最大大小。

响应通过 `params->func` 回调返回。例如，可在 MTU 交换回调（MTU Exchange Callback）中调用 `bt_gatt_get_mtu`，读取新协商的 ATT 连接 MTU。回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。`params` 必须保持有效，直到回调开始。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 最大传输单元交换参数（Exchange MTU Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->func`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |
| `-EALREADY` | 已经执行过最大传输单元交换过程（MTU Exchange Procedure）。 |

<a id="ga1a18dd726ab960a88d7f85f2a014141a"></a>

### `bt_gatt_read()`

```c
int bt_gatt_read ( struct bt_conn * conn, struct bt_gatt_read_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

按句柄读取属性值（Attribute Value）。

此过程读取属性值（Attribute Value），并通过回调（Callback）返回。

按 UUID 读取属性（Attribute）时，回调可能被调用多次，次数取决于给定 UUID 的实例数量；每个实例都会更新 `start_handle`。

要执行 GATT 长读取过程（Long Read Procedure），先发起特征值读取（Characteristic Value Read），即设置 `offset` 为 `0`、`handle_count` 为 `1`，随后从回调返回 `BT_GATT_ITER_CONTINUE`。这相当于再次调用 `bt_gatt_read`，但会使用继续读取所需的正确偏移量。可重复此过程直到读取完成；完成时会以 `data` 为 `NULL` 调用回调。

注意，返回 `BT_GATT_ITER_CONTINUE` 实际上会启动一次新的 ATT 操作，因此可能因资源分配失败而失败。但所有 API 错误都会按服务器返回了 `BT_ATT_ERR_UNLIKELY` 的方式报告，无法区分此类情况与服务器自身返回的 `BT_ATT_ERR_UNLIKELY` 响应。

注意，从回调（Callback）返回 `BT_GATT_ITER_CONTINUE` 的效果取决于读取操作（Read Operation）的类型。

响应通过 `params->func` 回调返回。回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。`params` 必须保持有效，直到回调开始。如果收到的数据长度无效，会以错误码 `BT_ATT_ERR_INVALID_PDU` 调用 `params->func`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 读取参数（Read Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->func`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |

<a id="ga791b8bb8a4c085b022fafc0535a63511"></a>

### `bt_gatt_resubscribe()`

```c
int bt_gatt_resubscribe ( uint8_t id, const bt_addr_le_t * peer, struct bt_gatt_subscribe_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

重新订阅属性值通知（Attribute Value Notification）。

如果先前连接中已经订阅过，则重新订阅属性值通知（Attribute Value Notification）。建立绑定（Bonding）后，GATT 服务器会记住先前连接的订阅，因此在断电重启后可以重新关联订阅，而无需执行新的订阅过程（Subscribe Procedure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份（Local Identity），多数情况下为 `BT_ID_DEFAULT`。 |
| `peer` | 远端地址（Remote address）。 |
| `params` | 订阅参数（Subscribe Parameters）。 |

**说明（Note）**：注意（Note）：通知（Notification）是异步的，因此参数在整个订阅期间都必须保持有效。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7d4a8e18f51ba6476886a15f81f48e5c"></a>

### `bt_gatt_subscribe()`

```c
int bt_gatt_subscribe ( struct bt_conn * conn, struct bt_gatt_subscribe_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

订阅属性值通知（Attribute Value Notification）。

此过程使用客户端特征配置句柄（Client Characteristic Configuration Handle）订阅值通知（Value Notification）。收到通知时，会调用订阅值回调，返回通知中的值；可在该回调中直接决定取消订阅。如果以此方式移除订阅，则不会再以 `data` 为 `NULL` 调用通知回调。

响应通过 `params->subscribe` 回调返回，通知通过 `params->notify` 返回。这两个回调都在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 订阅参数（Subscribe Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->write`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |
| `-EALREADY` | 已经存在使用该 `params` 的订阅（Subscription）时。 |
| `-EBUSY` | `params.ccc_handle` 为 `0`、启用了 `CONFIG_BT_GATT_AUTO_DISCOVER_CCC`，并且该 `params` 的发现过程（Discovery）已经在进行时。 |

**说明（Note）**：注意（Note）：通知（Notification）是异步的，因此 `params` 在整个订阅期间都必须保持有效；订阅仍然活动时，不能将它复用于额外订阅。

<a id="ga56509c9b8f73f729cfa5e75be22d79ae"></a>

### `bt_gatt_unsubscribe()`

```c
int bt_gatt_unsubscribe ( struct bt_conn * conn, struct bt_gatt_subscribe_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

取消订阅属性值通知（Attribute Value Notification）。

此过程使用客户端特征配置句柄（Client Characteristic Configuration Handle）取消值通知订阅（Value Notification Subscription）。如果此次调用移除了订阅，将以 `data` 为 `NULL` 调用通知回调；在此之前，不能复用参数。

响应通过 `params->notify` 回调返回，`data` 为 `NULL`；回调可能在此函数内部执行，也可能在协议栈（Stack）选定的线程上下文中执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 订阅参数（Subscribe Parameters）。这些参数必须是先前调用 `bt_gatt_subscribe()` 时使用的 `bt_gatt_subscribe_params`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->write`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |

<a id="ga843a42e68e0497d88d3f655f8ffd58d4"></a>

### `bt_gatt_write()`

```c
int bt_gatt_write ( struct bt_conn * conn, struct bt_gatt_write_params * params )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

按句柄写入属性值（Attribute Value）。

响应通过 `params->func` 回调返回。回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。`params` 必须保持有效，直到回调开始。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 写入参数（Write Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。请求处理完成后将调用 `params->func`。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |

<a id="ga9fc78e32230637a6f092da2400c50fe7"></a>

### `bt_gatt_write_without_response()`

```c
int bt_gatt_write_without_response ( struct bt_conn * conn, uint16_t handle, const void * data, uint16_t length, bool sign )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/gatt.h>
```

按句柄执行无响应属性值写入（Write Without Response）。

此过程写入属性值（Attribute Value），不要求对写入已成功执行给出确认（Acknowledgment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `handle` | 属性句柄（Attribute handle）。 |
| `data` | 要写入的数据（Data to be written）。 |
| `length` | 数据长度（Data Length）。 |
| `sign` | 是否对数据签名（Sign Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |

<a id="ga49439413d12b5a8a1c68735e961ab6fa"></a>

### `bt_gatt_write_without_response_cb()`

```c
int bt_gatt_write_without_response_cb ( struct bt_conn * conn, uint16_t handle, const void * data, uint16_t length, bool sign, bt_gatt_complete_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/gatt.h>
```

按句柄执行无响应属性值写入（Write Without Response），带回调。

此函数的工作方式与 `bt_gatt_write_without_response` 相同，额外行为是在发送写入后调用回调函数（Callback Function）。

回调在线程上下文（Thread Context）运行，绝不在中断服务程序（ISR）中运行；参见回调执行上下文（Callback Execution Contexts）。从系统工作队列上下文（System Workqueue Context）调用时，此 API 不会等待供回调使用的资源，而会返回错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `handle` | 属性句柄（Attribute handle）。 |
| `data` | 要写入的数据（Data to be written）。 |
| `length` | 数据长度（Data Length）。 |
| `sign` | 是否对数据签名（Sign Data）。 |
| `func` | 传输完成回调（Transmission Complete Callback）。 |
| `user_data` | 要传回给回调（Callback）的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功排入队列（Queued Request）。 |
| `-ENOMEM` | ATT 请求队列（Request Queue）已满，阻塞将导致死锁（Deadlock）。应等一个待处理请求完成后再重试，或者从独立线程调用此函数，以获得阻塞行为。队列大小由 `CONFIG_BT_ATT_TX_COUNT` 控制。 |


## 5.7\_原页交叉引用（Cross References）

- [bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)
- [bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)
- [bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)
- [bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [zephyr/bluetooth/gatt.h](../api_file_bluetooth_media_reference/P004_zephyr__bluetooth__gatt.h_文件参考.md)
- [bt_gatt_attr::perm](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a0849a40254622080d05e8559c4fdb9e2)
- [bt_gatt_attr.read()](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a074abc719494ca35997a452f526e7ecc)
- [bt_gatt_attr.write()](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a1ecd78536067f4bded506e0daccefd35)
- [类型（Type）：`bt_gatt_service_val`。](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)
- [类型（Type）：`bt_gatt_include`。](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)
- [类型（Type）：`bt_gatt_chrc`。](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)
- [特征扩展属性 UUID（Characteristic Extended Properties UUID）：`BT_UUID_GATT_CEP`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga6aa143b721d810f1536d7431a9bf7cc7)
- [类型（Type）：`bt_gatt_cep`。](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)
- [客户端特征配置 UUID（Client Characteristic Configuration UUID）：`BT_UUID_GATT_CCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga03a2d3f0ce89508b794d5c87a4303057)
- [类型（Type）：`bt_gatt_ccc`。](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)
- [服务器特征配置 UUID（Server Characteristic Configuration UUID）：`BT_UUID_GATT_SCC`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga82567cdce8c4411cd3daf26711ba9685)
- [类型（Type）：`bt_gatt_scc`。](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)
- [特征呈现格式 UUID（Characteristic Presentation Format UUID）：`BT_UUID_GATT_CPF`。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga331a61702ffe9b15bac0de3d60414022)
- [类型（Type）：`bt_gatt_cpf`。](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)
- [bt_gatt_read_params::handle_count](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a0a36063ac0b110fbf57ef6a66f7bece8)
- [BT_ATT_ERR_INVALID_PDU](../api_memory_network_topic_reference/P002_属性协议（Attribute Protocol，ATT）.md#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)
- [CONFIG_BT_GATT_AUTO_RESUBSCRIBE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_RESUBSCRIBE)
- [BT_ATT_ERR_UNLIKELY](../api_memory_network_topic_reference/P002_属性协议（Attribute Protocol，ATT）.md#ga992baa1f0d763a00f314bdcf59965bdd)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [BT_GATT_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)
- [CONFIG_BT_ATT_TX_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ATT_TX_COUNT)
- [bt_gatt_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga351fd7658eaecbbfa60f1769119ef733)
- [BT_GATT_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)
- [CONFIG_BT_GATT_AUTO_DISCOVER_CCC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f"></a>
<a id="ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97"></a>
<a id="ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da"></a>
<a id="ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae"></a>
<a id="ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe"></a>
<a id="ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c"></a>
<a id="ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61"></a>
<a id="ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb"></a>
<a id="ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6"></a>
<a id="ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad"></a>
<a id="ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab"></a>
<a id="ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）.md) · [返回大纲](大纲.md) · [下一章](P006_配置客户端模型（Configuration Client Model）.md)
