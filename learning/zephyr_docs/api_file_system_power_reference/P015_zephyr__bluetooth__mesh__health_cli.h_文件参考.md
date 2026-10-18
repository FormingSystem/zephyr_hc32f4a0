---
id: learning.zephyr-docs.api-file-system-power-reference.page-15
title: zephyr__bluetooth__mesh__health_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_bluetooth\_\_mesh\_\_health\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康客户端模型（Health Client Model）的API。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

健康客户端模型（Health Client Model）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fhealth_5Fcli"></a>

```c
struct bt_mesh_health_cli
```

相关声明：[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)。

健康客户端（Health Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga0f869fc7d19f5e8be5953a8ece6e07f6"></a>

```c
#define BT_MESH_MODEL_HEALTH_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_HEALTH_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga0f869fc7d19f5e8be5953a8ece6e07f6)。

通用健康客户端（Generic Health Client）模型的组成数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga2951f45aaaee75f4c77c4381b1ddd617"></a>

```c
int bt_mesh_health_cli_fault_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t *test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2951f45aaaee75f4c77c4381b1ddd617)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取给定公司 ID（Company ID）的已登记故障状态（Registered Fault State）。

<a id="r_ga77cc4e97193cca60d79a8076f3761ef5"></a>

```c
int bt_mesh_health_cli_fault_clear (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t *test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga77cc4e97193cca60d79a8076f3761ef5)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

清除给定公司 ID（Company ID）的已登记故障（Registered Faults）。

<a id="r_gafb0a46136f82f1aff4273704f1c47ac4"></a>

```c
int bt_mesh_health_cli_fault_clear_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid)
```

相关声明：[bt_mesh_health_cli_fault_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gafb0a46136f82f1aff4273704f1c47ac4)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

清除给定公司 ID（Company ID）的已登记故障（Registered Faults），无需确认（Unacknowledged）。

<a id="r_ga00cef275cdf90876f1381ffaff04b25c"></a>

```c
int bt_mesh_health_cli_fault_test (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga00cef275cdf90876f1381ffaff04b25c)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure）。

<a id="r_ga8e58519ef78946e88258b335c350d754"></a>

```c
int bt_mesh_health_cli_fault_test_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t test_id)
```

相关声明：[bt_mesh_health_cli_fault_test_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga8e58519ef78946e88258b335c350d754)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure），无需确认（Unacknowledged）。

<a id="r_ga1e8e25681b9fcbc6584a29336924a78a"></a>

```c
int bt_mesh_health_cli_period_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t *divisor)
```

相关声明：[bt_mesh_health_cli_period_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1e8e25681b9fcbc6584a29336924a78a)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的健康快速周期除数（Health Fast Period Divisor）。

<a id="r_ga2ef46f0b5059a959d5b06d6e49c4f552"></a>

```c
int bt_mesh_health_cli_period_set (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t divisor, uint8_t *updated_divisor)
```

相关声明：[bt_mesh_health_cli_period_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2ef46f0b5059a959d5b06d6e49c4f552)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的健康快速周期除数（Health Fast Period Divisor）。

<a id="r_ga536c631d87daaca017af078d49094fc1"></a>

```c
int bt_mesh_health_cli_period_set_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t divisor)
```

相关声明：[bt_mesh_health_cli_period_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga536c631d87daaca017af078d49094fc1)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的健康快速周期除数（Health Fast Period Divisor），无需确认（Unacknowledged）。

<a id="r_gad6f322f506b8577c56bb0613f7dcbd93"></a>

```c
int bt_mesh_health_cli_attention_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t *attention)
```

相关声明：[bt_mesh_health_cli_attention_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gad6f322f506b8577c56bb0613f7dcbd93)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前注意计时器值（Attention Timer Value）。

<a id="r_ga1b910d0849ce4c33d6de4bf1ff47ece8"></a>

```c
int bt_mesh_health_cli_attention_set (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t attention, uint8_t *updated_attention)
```

相关声明：[bt_mesh_health_cli_attention_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1b910d0849ce4c33d6de4bf1ff47ece8)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置注意计时器（Attention Timer）。

<a id="r_ga3a528688e340edf49b4bd62317284834"></a>

```c
int bt_mesh_health_cli_attention_set_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t attention)
```

相关声明：[bt_mesh_health_cli_attention_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga3a528688e340edf49b4bd62317284834)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置注意计时器（Attention Timer），无需确认（Unacknowledged）。

<a id="r_ga9abc0db22da327d02d23371bba59b46a"></a>

```c
int32_t bt_mesh_health_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_health_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga9abc0db22da327d02d23371bba59b46a)。

获取当前传输超时值（transmission timeout）。

<a id="r_gaf3d54597a74a458df0053bd0599d39e9"></a>

```c
void bt_mesh_health_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_health_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gaf3d54597a74a458df0053bd0599d39e9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 15.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P314_health_cli.h_源码浏览.md)
- [bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)
- [BT_MESH_MODEL_HEALTH_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga0f869fc7d19f5e8be5953a8ece6e07f6)
- [bt_mesh_health_cli_fault_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2951f45aaaee75f4c77c4381b1ddd617)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_health_cli_fault_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga77cc4e97193cca60d79a8076f3761ef5)
- [bt_mesh_health_cli_fault_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gafb0a46136f82f1aff4273704f1c47ac4)
- [bt_mesh_health_cli_fault_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga00cef275cdf90876f1381ffaff04b25c)
- [bt_mesh_health_cli_fault_test_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga8e58519ef78946e88258b335c350d754)
- [bt_mesh_health_cli_period_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1e8e25681b9fcbc6584a29336924a78a)
- [bt_mesh_health_cli_period_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2ef46f0b5059a959d5b06d6e49c4f552)
- [bt_mesh_health_cli_period_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga536c631d87daaca017af078d49094fc1)
- [bt_mesh_health_cli_attention_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gad6f322f506b8577c56bb0613f7dcbd93)
- [bt_mesh_health_cli_attention_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1b910d0849ce4c33d6de4bf1ff47ece8)
- [bt_mesh_health_cli_attention_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga3a528688e340edf49b4bd62317284834)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_health_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga9abc0db22da327d02d23371bba59b46a)
- [bt_mesh_health_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gaf3d54597a74a458df0053bd0599d39e9)

<a id="header-details"></a>

---

[上一章](P014_zephyr__drivers__misc__grove_lcd__grove_lcd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__dt-bindings__sensor__icm42686.h_文件参考.md)
