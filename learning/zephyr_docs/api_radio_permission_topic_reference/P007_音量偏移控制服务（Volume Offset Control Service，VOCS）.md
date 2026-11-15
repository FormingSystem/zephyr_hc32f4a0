---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-7
title: 音量偏移控制服务（Volume Offset Control Service，VOCS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_音量偏移控制服务（Volume Offset Control Service，VOCS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音量偏移控制服务（Volume Offset Control Service，VOCS）

<a id="details"></a>

音量偏移控制服务（Volume Offset Control Service，VOCS）。引入版本（Since）：2.6；API 版本（Version）：0.8.0。此服务是次级服务（Secondary Service），不应独立使用，而应在另一主服务（Primary Service）的上下文中使用。本 API 同时实现服务器和客户端功能。API 隐藏音量偏移控制状态中的变更计数器（Change Counter），并自动处理其变化。若计数器已过期，客户端实现在执行写请求时会自行读取计数器值。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_bt_5Fvocs_5Fregister_5Fparam"></a>

```c
struct bt_vocs_register_param
```

相关声明：[bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)。

用于注册音量偏移控制服务（Volume Offset Control Service）实例的结构。

<a id="r_bt_5Fvocs_5Fdiscover_5Fparam"></a>

```c
struct bt_vocs_discover_param
```

相关声明：[bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)。

用于发现音量偏移控制服务（Volume Offset Control Service）实例的结构。

<a id="r_bt_5Fvocs_5Fcb"></a>

```c
struct bt_vocs_cb
```

相关声明：[bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)。

保存音量偏移控制服务（Volume Offset Control Service）回调的结构。

<a id="r_bt_5Fvocs"></a>

```c
struct bt_vocs
```

相关声明：[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

不透明的音量偏移控制服务（Volume Offset Control Service）实例。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.2\_类型定义（Typedefs）

<a id="r_gaa329fd8931add8fd4f6c59b48c91ef75"></a>

```c
typedef void(* bt_vocs_state_cb) (struct bt_vocs *inst, int err, int16_t offset)
```

相关声明：[bt_vocs_state_cb](#gaa329fd8931add8fd4f6c59b48c91ef75)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

偏移状态（Offset State）的回调函数。

<a id="r_ga2630344190f12f911bb2b01c4b95ded6"></a>

```c
typedef void(* bt_vocs_set_offset_cb) (struct bt_vocs *inst, int err)
```

相关声明：[bt_vocs_set_offset_cb](#ga2630344190f12f911bb2b01c4b95ded6)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

设置偏移（Offset）的回调函数。

<a id="r_ga84983707e04eae75f18017072b647115"></a>

```c
typedef void(* bt_vocs_location_cb) (struct bt_vocs *inst, int err, uint32_t location)
```

相关声明：[bt_vocs_location_cb](#ga84983707e04eae75f18017072b647115)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

位置（Location）的回调函数。

<a id="r_gaa351c3ab631b16272e27cbb837d9e49c"></a>

```c
typedef void(* bt_vocs_description_cb) (struct bt_vocs *inst, int err, char *description)
```

相关声明：[bt_vocs_description_cb](#gaa351c3ab631b16272e27cbb837d9e49c)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

用于描述（Description）的回调函数。

<a id="r_gad50fd539190b5c64b5262d3830699365"></a>

```c
typedef void(* bt_vocs_discover_cb) (struct bt_vocs *inst, int err)
```

相关声明：[bt_vocs_discover_cb](#gad50fd539190b5c64b5262d3830699365)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

bt_vocs_discover 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_gadde50c3eb90ea7b7aa9b9c4b3672710f"></a>

```c
struct bt_vocs * bt_vocs_free_instance_get (void)
```

相关声明：[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_free_instance_get](#gadde50c3eb90ea7b7aa9b9c4b3672710f)。

从池中获取空闲的音量偏移控制服务（Volume Offset Control Service）实例。

<a id="r_ga9f7ff4c0521686ded011758ddd8ea95e"></a>

```c
void * bt_vocs_svc_decl_get (struct bt_vocs *vocs)
```

相关声明：[bt_vocs_svc_decl_get](#ga9f7ff4c0521686ded011758ddd8ea95e)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_gafcf7ecea73c8c199b38c7291ce4a648f"></a>

```c
int bt_vocs_client_conn_get (const struct bt_vocs *vocs, struct bt_conn **conn)
```

相关声明：[bt_vocs_client_conn_get](#gafcf7ecea73c8c199b38c7291ce4a648f)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_gac011ddd93bb3240148a789f1ee9ef7da"></a>

```c
int bt_vocs_register (struct bt_vocs *vocs, const struct bt_vocs_register_param *param)
```

相关声明：[bt_vocs_register](#gac011ddd93bb3240148a789f1ee9ef7da)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)。

注册音量偏移控制服务（Volume Offset Control Service）实例。

<a id="r_ga6c835234a5530bae3bb0f5bd03a0bdd7"></a>

```c
int bt_vocs_state_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_state_get](#ga6c835234a5530bae3bb0f5bd03a0bdd7)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的偏移状态。

<a id="r_ga28ea337e439b5872abab8f5b98719da4"></a>

```c
int bt_vocs_state_set (struct bt_vocs *inst, int16_t offset)
```

相关声明：[bt_vocs_state_set](#ga28ea337e439b5872abab8f5b98719da4)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置音量偏移控制服务（Volume Offset Control Service）的偏移状态。

<a id="r_ga90ba394e6be138d6052b95d73ab2f409"></a>

```c
int bt_vocs_location_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_location_get](#ga90ba394e6be138d6052b95d73ab2f409)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的位置。

<a id="r_ga02b036f060eee947c8924bbea846bc29"></a>

```c
int bt_vocs_location_set (struct bt_vocs *inst, uint32_t location)
```

相关声明：[bt_vocs_location_set](#ga02b036f060eee947c8924bbea846bc29)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置音量偏移控制服务（Volume Offset Control Service）的位置。

<a id="r_gaac1c1292cae4c5845a376d2f4db3d661"></a>

```c
int bt_vocs_description_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_description_get](#gaac1c1292cae4c5845a376d2f4db3d661)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的输出描述。

<a id="r_gac17cb7101233605834ec6b66d7417f91"></a>

```c
int bt_vocs_description_set (struct bt_vocs *inst, const char *description)
```

相关声明：[bt_vocs_description_set](#gac17cb7101233605834ec6b66d7417f91)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

设置音量偏移控制服务（Volume Offset Control Service）的描述。

<a id="r_gaace802556eca3d634a13dd8f2bf3c544"></a>

```c
void bt_vocs_client_cb_register (struct bt_vocs *inst, struct bt_vocs_cb *cb)
```

相关声明：[bt_vocs_client_cb_register](#gaace802556eca3d634a13dd8f2bf3c544)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)。

注册音量偏移控制服务（Volume Offset Control Service）客户端的回调。

<a id="r_ga6182120b1bece7f5851bb6295c81b562"></a>

```c
struct bt_vocs * bt_vocs_client_free_instance_get (void)
```

相关声明：[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_client_free_instance_get](#ga6182120b1bece7f5851bb6295c81b562)。

返回指向音量偏移控制服务（Volume Offset Control Service）客户端实例的指针。

<a id="r_gaf210fd531117b9a22a52746266c72c08"></a>

```c
int bt_vocs_client_free_instance (struct bt_vocs *inst)
```

相关声明：[bt_vocs_client_free_instance](#gaf210fd531117b9a22a52746266c72c08)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

释放从 bt_vocs_client_free_instance_get() 获得的实例。

<a id="r_ga45efa872e07ac8051379caf5aa8d0133"></a>

```c
int bt_vocs_discover (struct bt_conn *conn, struct bt_vocs *inst, const struct bt_vocs_discover_param *param)
```

相关声明：[bt_vocs_discover](#ga45efa872e07ac8051379caf5aa8d0133)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)。

发现音量偏移控制服务（Volume Offset Control Service）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.4\_音量偏移控制服务错误码（Volume Offset Control Service Error Codes）

<a id="r_ga17c81394b9b4d601768e72d8c360992f"></a>

```c
#define BT_VOCS_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_VOCS_ERR_INVALID_COUNTER](#ga17c81394b9b4d601768e72d8c360992f)。

Change_Counter 操作数（Operand）值与音量偏移状态特征（Volume Offset State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_gadd01a04e3c4336a13a4760e2448131b1"></a>

```c
#define BT_VOCS_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_VOCS_ERR_OP_NOT_SUPPORTED](#gadd01a04e3c4336a13a4760e2448131b1)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="r_ga2ecb7e0408bb1767c2d51c816f4b273d"></a>

```c
#define BT_VOCS_ERR_OUT_OF_RANGE 0x82U
```

相关声明：[BT_VOCS_ERR_OUT_OF_RANGE](#ga2ecb7e0408bb1767c2d51c816f4b273d)。

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

## 7.5\_音量偏移控制服务的偏移限值（Volume Offset Control Service Offset Limits）

<a id="r_ga64d4e32f9d92a58b3229b3aa2e8fcc4d"></a>

```c
#define BT_VOCS_MIN_OFFSET -255
```

相关声明：[BT_VOCS_MIN_OFFSET](#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)。

最小偏移值（Minimum Offset Value）。

<a id="r_ga800092562173fd37826b5537feaac3ae"></a>

```c
#define BT_VOCS_MAX_OFFSET 255
```

相关声明：[BT_VOCS_MAX_OFFSET](#ga800092562173fd37826b5537feaac3ae)。

最大偏移值（Maximum Offset Value）。

## 7.6\_详细说明（Detailed Documentation）

<a id="ga17c81394b9b4d601768e72d8c360992f"></a>

### `BT_VOCS_ERR_INVALID_COUNTER`

```c
#define BT_VOCS_ERR_INVALID_COUNTER 0x80U
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

Change_Counter 操作数（Operand）值与音量偏移状态特征（Volume Offset State Characteristic）的 Change_Counter 字段值不匹配。

<a id="gadd01a04e3c4336a13a4760e2448131b1"></a>

### `BT_VOCS_ERR_OP_NOT_SUPPORTED`

```c
#define BT_VOCS_ERR_OP_NOT_SUPPORTED 0x81U
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="ga2ecb7e0408bb1767c2d51c816f4b273d"></a>

### `BT_VOCS_ERR_OUT_OF_RANGE`

```c
#define BT_VOCS_ERR_OUT_OF_RANGE 0x82U
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

<a id="ga800092562173fd37826b5537feaac3ae"></a>

### `BT_VOCS_MAX_OFFSET`

```c
#define BT_VOCS_MAX_OFFSET 255
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

最大偏移值（Maximum Offset Value）。

<a id="ga64d4e32f9d92a58b3229b3aa2e8fcc4d"></a>

### `BT_VOCS_MIN_OFFSET`

```c
#define BT_VOCS_MIN_OFFSET -255
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

最小偏移值（Minimum Offset Value）。

<a id="gaa351c3ab631b16272e27cbb837d9e49c"></a>

### `bt_vocs_description_cb`

```c
typedef void(* bt_vocs_description_cb) (struct bt_vocs *inst, int err, char *description)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

用于描述（Description）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `description` | 描述（Description），以 UTF-8 编码字符串表示。 |

<a id="gad50fd539190b5c64b5262d3830699365"></a>

### `bt_vocs_discover_cb`

```c
typedef void(* bt_vocs_discover_cb) (struct bt_vocs *inst, int err)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

bt_vocs_discover 的回调函数（Callback Function）。

此回调应由包含音量偏移控制服务（Volume Offset Control Service）客户端的主服务覆盖，因此应用不应设置它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |

<a id="ga84983707e04eae75f18017072b647115"></a>

### `bt_vocs_location_cb`

```c
typedef void(* bt_vocs_location_cb) (struct bt_vocs *inst, int err, uint32_t location)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

位置（Location）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `location` | 位置值（Location Value）。 |

<a id="ga2630344190f12f911bb2b01c4b95ded6"></a>

### `bt_vocs_set_offset_cb`

```c
typedef void(* bt_vocs_set_offset_cb) (struct bt_vocs *inst, int err)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

设置偏移（Offset）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="gaa329fd8931add8fd4f6c59b48c91ef75"></a>

### `bt_vocs_state_cb`

```c
typedef void(* bt_vocs_state_cb) (struct bt_vocs *inst, int err, int16_t offset)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

偏移状态（Offset State）的回调函数。

读取此值时，或服务器、客户端任一方更改此值时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例指针（Instance Pointer）。 |
| `err` | 错误值（Error Value）：0 表示成功；正值为 GATT 错误，负值为 errno 错误。对于通知（Notifications），始终为 0。 |
| `offset` | 偏移值（Offset Value）。 |

<a id="gaace802556eca3d634a13dd8f2bf3c544"></a>

### `bt_vocs_client_cb_register()`

```c
void bt_vocs_client_cb_register ( struct bt_vocs * inst, struct bt_vocs_cb * cb )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

注册音量偏移控制服务（Volume Offset Control Service）客户端的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）客户端实例的指针。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

<a id="gafcf7ecea73c8c199b38c7291ce4a648f"></a>

### `bt_vocs_client_conn_get()`

```c
int bt_vocs_client_conn_get ( const struct bt_vocs * vocs, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

获取客户端实例的连接指针（Connection Pointer）。

获取音量偏移控制服务（Volume Offset Control Service）客户端实例的蓝牙连接指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vocs` | 音量偏移控制服务（Volume Offset Control Service）客户端实例指针。 |
| `conn` | 连接指针（Connection Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaf210fd531117b9a22a52746266c72c08"></a>

### `bt_vocs_client_free_instance()`

```c
int bt_vocs_client_free_instance ( struct bt_vocs * inst)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

释放从 bt_vocs_client_free_instance_get() 获得的实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 待释放的实例（Instance） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | inst 为 NULL 或不是客户端实例。 |
| `-EALREADY` | inst 已处于空闲状态。 |
| `-EBUSY` | inst 正忙。 |

<a id="ga6182120b1bece7f5851bb6295c81b562"></a>

### `bt_vocs_client_free_instance_get()`

```c
struct bt_vocs * bt_vocs_client_free_instance_get ( void )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

返回指向音量偏移控制服务（Volume Offset Control Service）客户端实例的指针。

**返回（Returns）**：返回值（Returns）：指向实例的指针；无剩余空闲实例时返回 NULL。

<a id="gaac1c1292cae4c5845a376d2f4db3d661"></a>

### `bt_vocs_description_get()`

```c
int bt_vocs_description_get ( struct bt_vocs * inst)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

读取音量偏移控制服务（Volume Offset Control Service）的输出描述。

通过 bt_vocs_cb.description 回调返回该值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="gac17cb7101233605834ec6b66d7417f91"></a>

### `bt_vocs_description_set()`

```c
int bt_vocs_description_set ( struct bt_vocs * inst, const char * description )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

设置音量偏移控制服务（Volume Offset Control Service）的描述。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |
| `description` | 要设置的描述，为 UTF-8 编码字符串。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga45efa872e07ac8051379caf5aa8d0133"></a>

### `bt_vocs_discover()`

```c
int bt_vocs_discover ( struct bt_conn * conn, struct bt_vocs * inst, const struct bt_vocs_discover_param * param )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

发现音量偏移控制服务（Volume Offset Control Service）。

根据 param，尝试在服务器上发现音量偏移控制服务（Volume Offset Control Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与提供音量偏移控制服务（Volume Offset Control Service）的对端的连接。 |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）客户端实例的指针。 |
| `param` | 指向参数（Parameters）的指针。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回 errno。

<a id="gadde50c3eb90ea7b7aa9b9c4b3672710f"></a>

### `bt_vocs_free_instance_get()`

```c
struct bt_vocs * bt_vocs_free_instance_get ( void )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

从池中获取空闲的音量偏移控制服务（Volume Offset Control Service）实例。

**返回（Returns）**：返回值（Returns）：成功返回音量偏移控制服务（Volume Offset Control Service）实例，错误时返回 NULL。

<a id="ga90ba394e6be138d6052b95d73ab2f409"></a>

### `bt_vocs_location_get()`

```c
int bt_vocs_location_get ( struct bt_vocs * inst)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

读取音量偏移控制服务（Volume Offset Control Service）的位置。

通过 bt_vocs_cb.location 回调返回该值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga02b036f060eee947c8924bbea846bc29"></a>

### `bt_vocs_location_set()`

```c
int bt_vocs_location_set ( struct bt_vocs * inst, uint32_t location )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

设置音量偏移控制服务（Volume Offset Control Service）的位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |
| `location` | 要设置的位置（Location）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="gac011ddd93bb3240148a789f1ee9ef7da"></a>

### `bt_vocs_register()`

```c
int bt_vocs_register ( struct bt_vocs * vocs, const struct bt_vocs_register_param * param )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

注册音量偏移控制服务（Volume Offset Control Service）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vocs` | 音量偏移控制服务（Volume Offset Control Service）实例。 |
| `param` | 音量偏移控制服务注册参数（Register Parameters）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga6c835234a5530bae3bb0f5bd03a0bdd7"></a>

### `bt_vocs_state_get()`

```c
int bt_vocs_state_get ( struct bt_vocs * inst)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

读取音量偏移控制服务（Volume Offset Control Service）的偏移状态。

通过 bt_vocs_cb.state 回调返回该值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga28ea337e439b5872abab8f5b98719da4"></a>

### `bt_vocs_state_set()`

```c
int bt_vocs_state_set ( struct bt_vocs * inst, int16_t offset )
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

设置音量偏移控制服务（Volume Offset Control Service）的偏移状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 指向音量偏移控制服务（Volume Offset Control Service）实例的指针。 |
| `offset` | 要设置的偏移（Offset），范围为 -255～255。 |

**返回（Returns）**：返回值：成功返回 0，失败返回通用属性配置文件（GATT）错误值。

<a id="ga9f7ff4c0521686ded011758ddd8ea95e"></a>

### `bt_vocs_svc_decl_get()`

```c
void * bt_vocs_svc_decl_get ( struct bt_vocs * vocs)
```

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

获取服务声明属性（Service Declaration Attribute）。

返回的首个服务属性（Service Attribute）可包含在其他任意 GATT 服务中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vocs` | 音量偏移控制服务（Volume Offset Control Service）实例。 |

**返回（Returns）**：返回值（Returns）：指向服务属性（Attributes）的指针。


## 7.7\_原页交叉引用（Cross References）

- [bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)
- [bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)
- [bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)
- [bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/vocs.h](../api_file_audio_gateway_reference/P027_zephyr__bluetooth__audio__vocs.h_文件参考.md)
- [bt_vocs_cb.description](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ac508b1e6dda00c607aa1cbe52423ec52)
- [bt_vocs_cb.location](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a50d1d429089456267b06d4450712b897)
- [bt_vocs_cb.state](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ae633c1f6cd8aa03d89287e783179460e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_固件更新客户端模型（原文：Firmware Uppdate Client model）.md) · [返回大纲](大纲.md) · [下一章](P008_英飞凌（Infineon）CAT1.md)
