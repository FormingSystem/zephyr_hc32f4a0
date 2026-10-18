---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-27
title: zephyr__bluetooth__audio__vocs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_bluetooth\_\_audio\_\_vocs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音量偏移控制服务（Volume Offset Control Service，VOCS）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/conn.h>
```

查看此文件的源码。

蓝牙音量偏移控制服务（Volume Offset Control Service，VOCS）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 音量偏移控制服务错误码（Volume Offset Control Service Error Codes）

<a id="r_ga17c81394b9b4d601768e72d8c360992f"></a>

```c
#define BT_VOCS_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_VOCS_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga17c81394b9b4d601768e72d8c360992f)。

Change_Counter 操作数（Operand）值与音量偏移状态特征（Volume Offset State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_gadd01a04e3c4336a13a4760e2448131b1"></a>

```c
#define BT_VOCS_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_VOCS_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gadd01a04e3c4336a13a4760e2448131b1)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="r_ga2ecb7e0408bb1767c2d51c816f4b273d"></a>

```c
#define BT_VOCS_ERR_OUT_OF_RANGE 0x82U
```

相关声明：[BT_VOCS_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2ecb7e0408bb1767c2d51c816f4b273d)。

控制点过程（Control Point Procedure）使用的操作数（Operand）值超出允许范围。

<a id="define-members-1"></a>

### 音量偏移控制服务的偏移限值（Volume Offset Control Service Offset Limits）

<a id="r_ga64d4e32f9d92a58b3229b3aa2e8fcc4d"></a>

```c
#define BT_VOCS_MIN_OFFSET -255
```

相关声明：[BT_VOCS_MIN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)。

最小偏移值（Minimum Offset Value）。

<a id="r_ga800092562173fd37826b5537feaac3ae"></a>

```c
#define BT_VOCS_MAX_OFFSET 255
```

相关声明：[BT_VOCS_MAX_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga800092562173fd37826b5537feaac3ae)。

最大偏移值（Maximum Offset Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.3\_类型定义（Typedefs）

<a id="r_gaa329fd8931add8fd4f6c59b48c91ef75"></a>

```c
typedef void(* bt_vocs_state_cb) (struct bt_vocs *inst, int err, int16_t offset)
```

相关声明：[bt_vocs_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa329fd8931add8fd4f6c59b48c91ef75)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

偏移状态（Offset State）的回调函数。

<a id="r_ga2630344190f12f911bb2b01c4b95ded6"></a>

```c
typedef void(* bt_vocs_set_offset_cb) (struct bt_vocs *inst, int err)
```

相关声明：[bt_vocs_set_offset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2630344190f12f911bb2b01c4b95ded6)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

设置偏移（Offset）的回调函数。

<a id="r_ga84983707e04eae75f18017072b647115"></a>

```c
typedef void(* bt_vocs_location_cb) (struct bt_vocs *inst, int err, uint32_t location)
```

相关声明：[bt_vocs_location_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga84983707e04eae75f18017072b647115)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

位置（Location）的回调函数。

<a id="r_gaa351c3ab631b16272e27cbb837d9e49c"></a>

```c
typedef void(* bt_vocs_description_cb) (struct bt_vocs *inst, int err, char *description)
```

相关声明：[bt_vocs_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa351c3ab631b16272e27cbb837d9e49c)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

用于描述（Description）的回调函数。

<a id="r_gad50fd539190b5c64b5262d3830699365"></a>

```c
typedef void(* bt_vocs_discover_cb) (struct bt_vocs *inst, int err)
```

相关声明：[bt_vocs_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gad50fd539190b5c64b5262d3830699365)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

bt_vocs_discover 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.4\_函数（Functions）

<a id="r_gadde50c3eb90ea7b7aa9b9c4b3672710f"></a>

```c
struct bt_vocs * bt_vocs_free_instance_get (void)
```

相关声明：[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gadde50c3eb90ea7b7aa9b9c4b3672710f)。

从池中获取空闲的音量偏移控制服务（Volume Offset Control Service）实例。

<a id="r_ga9f7ff4c0521686ded011758ddd8ea95e"></a>

```c
void * bt_vocs_svc_decl_get (struct bt_vocs *vocs)
```

相关声明：[bt_vocs_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga9f7ff4c0521686ded011758ddd8ea95e)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

获取服务声明属性（Service Declaration Attribute）。

<a id="r_gafcf7ecea73c8c199b38c7291ce4a648f"></a>

```c
int bt_vocs_client_conn_get (const struct bt_vocs *vocs, struct bt_conn **conn)
```

相关声明：[bt_vocs_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gafcf7ecea73c8c199b38c7291ce4a648f)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_gac011ddd93bb3240148a789f1ee9ef7da"></a>

```c
int bt_vocs_register (struct bt_vocs *vocs, const struct bt_vocs_register_param *param)
```

相关声明：[bt_vocs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac011ddd93bb3240148a789f1ee9ef7da)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)。

注册音量偏移控制服务（Volume Offset Control Service）实例。

<a id="r_ga6c835234a5530bae3bb0f5bd03a0bdd7"></a>

```c
int bt_vocs_state_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6c835234a5530bae3bb0f5bd03a0bdd7)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的偏移状态。

<a id="r_ga28ea337e439b5872abab8f5b98719da4"></a>

```c
int bt_vocs_state_set (struct bt_vocs *inst, int16_t offset)
```

相关声明：[bt_vocs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga28ea337e439b5872abab8f5b98719da4)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置音量偏移控制服务（Volume Offset Control Service）的偏移状态。

<a id="r_ga90ba394e6be138d6052b95d73ab2f409"></a>

```c
int bt_vocs_location_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga90ba394e6be138d6052b95d73ab2f409)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的位置。

<a id="r_ga02b036f060eee947c8924bbea846bc29"></a>

```c
int bt_vocs_location_set (struct bt_vocs *inst, uint32_t location)
```

相关声明：[bt_vocs_location_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga02b036f060eee947c8924bbea846bc29)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置音量偏移控制服务（Volume Offset Control Service）的位置。

<a id="r_gaac1c1292cae4c5845a376d2f4db3d661"></a>

```c
int bt_vocs_description_get (struct bt_vocs *inst)
```

相关声明：[bt_vocs_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaac1c1292cae4c5845a376d2f4db3d661)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

读取音量偏移控制服务（Volume Offset Control Service）的输出描述。

<a id="r_gac17cb7101233605834ec6b66d7417f91"></a>

```c
int bt_vocs_description_set (struct bt_vocs *inst, const char *description)
```

相关声明：[bt_vocs_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac17cb7101233605834ec6b66d7417f91)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

设置音量偏移控制服务（Volume Offset Control Service）的描述。

<a id="r_gaace802556eca3d634a13dd8f2bf3c544"></a>

```c
void bt_vocs_client_cb_register (struct bt_vocs *inst, struct bt_vocs_cb *cb)
```

相关声明：[bt_vocs_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaace802556eca3d634a13dd8f2bf3c544)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)。

注册音量偏移控制服务（Volume Offset Control Service）客户端的回调。

<a id="r_ga6182120b1bece7f5851bb6295c81b562"></a>

```c
struct bt_vocs * bt_vocs_client_free_instance_get (void)
```

相关声明：[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6182120b1bece7f5851bb6295c81b562)。

返回指向音量偏移控制服务（Volume Offset Control Service）客户端实例的指针。

<a id="r_gaf210fd531117b9a22a52746266c72c08"></a>

```c
int bt_vocs_client_free_instance (struct bt_vocs *inst)
```

相关声明：[bt_vocs_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaf210fd531117b9a22a52746266c72c08)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)。

释放从 bt_vocs_client_free_instance_get() 获得的实例。

<a id="r_ga45efa872e07ac8051379caf5aa8d0133"></a>

```c
int bt_vocs_discover (struct bt_conn *conn, struct bt_vocs *inst, const struct bt_vocs_discover_param *param)
```

相关声明：[bt_vocs_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga45efa872e07ac8051379caf5aa8d0133)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)、[bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)。

发现音量偏移控制服务（Volume Offset Control Service）。


## 27.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P914_vocs.h_源码浏览.md)
- [bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)
- [bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)
- [bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)
- [BT_VOCS_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga17c81394b9b4d601768e72d8c360992f)
- [BT_VOCS_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gadd01a04e3c4336a13a4760e2448131b1)
- [BT_VOCS_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2ecb7e0408bb1767c2d51c816f4b273d)
- [BT_VOCS_MIN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)
- [BT_VOCS_MAX_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga800092562173fd37826b5537feaac3ae)
- [bt_vocs_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa329fd8931add8fd4f6c59b48c91ef75)
- [bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_vocs_set_offset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2630344190f12f911bb2b01c4b95ded6)
- [bt_vocs_location_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga84983707e04eae75f18017072b647115)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_vocs_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa351c3ab631b16272e27cbb837d9e49c)
- [bt_vocs_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gad50fd539190b5c64b5262d3830699365)
- [bt_vocs_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gadde50c3eb90ea7b7aa9b9c4b3672710f)
- [bt_vocs_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga9f7ff4c0521686ded011758ddd8ea95e)
- [bt_vocs_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gafcf7ecea73c8c199b38c7291ce4a648f)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_vocs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac011ddd93bb3240148a789f1ee9ef7da)
- [bt_vocs_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6c835234a5530bae3bb0f5bd03a0bdd7)
- [bt_vocs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga28ea337e439b5872abab8f5b98719da4)
- [bt_vocs_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga90ba394e6be138d6052b95d73ab2f409)
- [bt_vocs_location_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga02b036f060eee947c8924bbea846bc29)
- [bt_vocs_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaac1c1292cae4c5845a376d2f4db3d661)
- [bt_vocs_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac17cb7101233605834ec6b66d7417f91)
- [bt_vocs_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaace802556eca3d634a13dd8f2bf3c544)
- [bt_vocs_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6182120b1bece7f5851bb6295c81b562)
- [bt_vocs_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaf210fd531117b9a22a52746266c72c08)
- [bt_vocs_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga45efa872e07ac8051379caf5aa8d0133)

<a id="header-details"></a>

---

[上一章](P026_zephyr__sd__sdmmc.h_文件参考.md) · [返回大纲](大纲.md)
