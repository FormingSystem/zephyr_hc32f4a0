---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-6
title: 健康客户端模型（Health Client Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_健康客户端模型（Health Client Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康客户端模型（Health Client Model）

<a id="details"></a>

健康客户端模型（Health Client Model）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fhealth_5Fcli"></a>

```c
struct bt_mesh_health_cli
```

相关声明：[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)。

健康客户端（Health Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga0f869fc7d19f5e8be5953a8ece6e07f6"></a>

```c
#define BT_MESH_MODEL_HEALTH_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_HEALTH_CLI](#ga0f869fc7d19f5e8be5953a8ece6e07f6)。

通用健康客户端（Generic Health Client）模型的组成数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_ga2951f45aaaee75f4c77c4381b1ddd617"></a>

```c
int bt_mesh_health_cli_fault_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t *test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_get](#ga2951f45aaaee75f4c77c4381b1ddd617)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取给定公司 ID（Company ID）的已登记故障状态（Registered Fault State）。

<a id="r_ga77cc4e97193cca60d79a8076f3761ef5"></a>

```c
int bt_mesh_health_cli_fault_clear (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t *test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_clear](#ga77cc4e97193cca60d79a8076f3761ef5)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

清除给定公司 ID（Company ID）的已登记故障（Registered Faults）。

<a id="r_gafb0a46136f82f1aff4273704f1c47ac4"></a>

```c
int bt_mesh_health_cli_fault_clear_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid)
```

相关声明：[bt_mesh_health_cli_fault_clear_unack](#gafb0a46136f82f1aff4273704f1c47ac4)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

清除给定公司 ID（Company ID）的已登记故障（Registered Faults），无需确认（Unacknowledged）。

<a id="r_ga00cef275cdf90876f1381ffaff04b25c"></a>

```c
int bt_mesh_health_cli_fault_test (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t test_id, uint8_t *faults, size_t *fault_count)
```

相关声明：[bt_mesh_health_cli_fault_test](#ga00cef275cdf90876f1381ffaff04b25c)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure）。

<a id="r_ga8e58519ef78946e88258b335c350d754"></a>

```c
int bt_mesh_health_cli_fault_test_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint16_t cid, uint8_t test_id)
```

相关声明：[bt_mesh_health_cli_fault_test_unack](#ga8e58519ef78946e88258b335c350d754)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure），无需确认（Unacknowledged）。

<a id="r_ga1e8e25681b9fcbc6584a29336924a78a"></a>

```c
int bt_mesh_health_cli_period_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t *divisor)
```

相关声明：[bt_mesh_health_cli_period_get](#ga1e8e25681b9fcbc6584a29336924a78a)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标节点的健康快速周期除数（Health Fast Period Divisor）。

<a id="r_ga2ef46f0b5059a959d5b06d6e49c4f552"></a>

```c
int bt_mesh_health_cli_period_set (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t divisor, uint8_t *updated_divisor)
```

相关声明：[bt_mesh_health_cli_period_set](#ga2ef46f0b5059a959d5b06d6e49c4f552)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的健康快速周期除数（Health Fast Period Divisor）。

<a id="r_ga536c631d87daaca017af078d49094fc1"></a>

```c
int bt_mesh_health_cli_period_set_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t divisor)
```

相关声明：[bt_mesh_health_cli_period_set_unack](#ga536c631d87daaca017af078d49094fc1)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标节点的健康快速周期除数（Health Fast Period Divisor），无需确认（Unacknowledged）。

<a id="r_gad6f322f506b8577c56bb0613f7dcbd93"></a>

```c
int bt_mesh_health_cli_attention_get (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t *attention)
```

相关声明：[bt_mesh_health_cli_attention_get](#gad6f322f506b8577c56bb0613f7dcbd93)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前注意计时器值（Attention Timer Value）。

<a id="r_ga1b910d0849ce4c33d6de4bf1ff47ece8"></a>

```c
int bt_mesh_health_cli_attention_set (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t attention, uint8_t *updated_attention)
```

相关声明：[bt_mesh_health_cli_attention_set](#ga1b910d0849ce4c33d6de4bf1ff47ece8)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置注意计时器（Attention Timer）。

<a id="r_ga3a528688e340edf49b4bd62317284834"></a>

```c
int bt_mesh_health_cli_attention_set_unack (struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t attention)
```

相关声明：[bt_mesh_health_cli_attention_set_unack](#ga3a528688e340edf49b4bd62317284834)、[bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置注意计时器（Attention Timer），无需确认（Unacknowledged）。

<a id="r_ga9abc0db22da327d02d23371bba59b46a"></a>

```c
int32_t bt_mesh_health_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_health_cli_timeout_get](#ga9abc0db22da327d02d23371bba59b46a)。

获取当前传输超时值（transmission timeout）。

<a id="r_gaf3d54597a74a458df0053bd0599d39e9"></a>

```c
void bt_mesh_health_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_health_cli_timeout_set](#gaf3d54597a74a458df0053bd0599d39e9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 6.4\_详细说明（Detailed Documentation）

<a id="ga0f869fc7d19f5e8be5953a8ece6e07f6"></a>

### `BT_MESH_MODEL_HEALTH_CLI`

```c
#define BT_MESH_MODEL_HEALTH_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_HEALTH_CLI, bt_mesh_health_cli_op,   \
                 &(cli_data)->pub, cli_data, &bt_mesh_health_cli_cb)
```

通用健康客户端（Generic Health Client）模型的组成数据（Composition Data）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli_data` | 指向健康客户端模型实例（Health Client Model Instance）的指针。 |

<a id="gad6f322f506b8577c56bb0613f7dcbd93"></a>

### `bt_mesh_health_cli_attention_get()`

```c
int bt_mesh_health_cli_attention_get ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t * attention )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

获取当前注意计时器值（Attention Timer Value）。

将 `attention` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `attention_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `attention` | 关注定时器（Attention Timer）的响应缓冲区，以秒为单位。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga1b910d0849ce4c33d6de4bf1ff47ece8"></a>

### `bt_mesh_health_cli_attention_set()`

```c
int bt_mesh_health_cli_attention_set ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t attention, uint8_t * updated_attention )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

设置注意计时器（Attention Timer）。

将 `updated_attention` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `attention_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `attention` | 新的关注定时器（Attention Timer）时长，单位为秒。 |
| `updated_attention` | 关注定时器（Attention Timer）的响应缓冲区，以秒为单位。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga3a528688e340edf49b4bd62317284834"></a>

### `bt_mesh_health_cli_attention_set_unack()`

```c
int bt_mesh_health_cli_attention_set_unack ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t attention )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

设置注意计时器（Attention Timer），无需确认（Unacknowledged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `attention` | 新的关注定时器（Attention Timer）时长，单位为秒。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga77cc4e97193cca60d79a8076f3761ef5"></a>

### `bt_mesh_health_cli_fault_clear()`

```c
int bt_mesh_health_cli_fault_clear ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint16_t cid, uint8_t * test_id, uint8_t * faults, size_t * fault_count )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

清除给定公司 ID（Company ID）的已登记故障（Registered Faults）。

将 `test_id` 以及 `faults` 或 `fault_count` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `fault_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `cid` | 要清除其已登记故障（Registered Faults）的公司 ID（Company ID）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |
| `faults` | 故障数组响应缓冲区（Fault Array Response Buffer）。 |
| `fault_count` | 故障数量响应缓冲区（Fault Count Response Buffer）。 |

**参阅（See Also）**：另见（See also）：健康故障（Health faults）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gafb0a46136f82f1aff4273704f1c47ac4"></a>

### `bt_mesh_health_cli_fault_clear_unack()`

```c
int bt_mesh_health_cli_fault_clear_unack ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint16_t cid )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

清除给定公司 ID（Company ID）的已登记故障（Registered Faults），无需确认（Unacknowledged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `cid` | 要清除其已登记故障（Registered Faults）的公司 ID（Company ID）。 |

**参阅（See Also）**：另见（See also）：健康故障（Health faults）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2951f45aaaee75f4c77c4381b1ddd617"></a>

### `bt_mesh_health_cli_fault_get()`

```c
int bt_mesh_health_cli_fault_get ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint16_t cid, uint8_t * test_id, uint8_t * faults, size_t * fault_count )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

获取给定公司 ID（Company ID）的已登记故障状态（Registered Fault State）。

将 `test_id` 以及 `faults` 或 `fault_count` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `fault_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `cid` | 要获取其已登记故障（Registered Faults）的公司 ID（Company ID）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |
| `faults` | 故障数组响应缓冲区（Fault Array Response Buffer）。 |
| `fault_count` | 故障数量响应缓冲区（Fault Count Response Buffer）。 |

**参阅（See Also）**：另见（See also）：健康故障（Health faults）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga00cef275cdf90876f1381ffaff04b25c"></a>

### `bt_mesh_health_cli_fault_test()`

```c
int bt_mesh_health_cli_fault_test ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint16_t cid, uint8_t test_id, uint8_t * faults, size_t * fault_count )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure）。

将 `faults` 或 `fault_count` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `fault_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `cid` | 要为其执行测试的公司 ID（Company ID）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |
| `faults` | 故障数组响应缓冲区（Fault Array Response Buffer）。 |
| `fault_count` | 故障数量响应缓冲区（Fault Count Response Buffer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga8e58519ef78946e88258b335c350d754"></a>

### `bt_mesh_health_cli_fault_test_unack()`

```c
int bt_mesh_health_cli_fault_test_unack ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint16_t cid, uint8_t test_id )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

为给定公司 ID（Company ID）调用自检流程（Self-test Procedure），无需确认（Unacknowledged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `cid` | 要为其执行测试的公司 ID（Company ID）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga1e8e25681b9fcbc6584a29336924a78a"></a>

### `bt_mesh_health_cli_period_get()`

```c
int bt_mesh_health_cli_period_get ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t * divisor )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

获取目标节点的健康快速周期除数（Health Fast Period Divisor）。

健康周期除数（Health Period Divisor）用于在登记故障时提高发布速率。通常，健康服务器（Health Server）按已配置发布参数中的周期发布；登记故障后，发布周期会除以 `(1 << divisor)`。例如，目标节点的健康服务器配置为每 16 秒发布一次，健康快速周期除数（Health Fast Period Divisor）为 5，则登记故障后，健康服务器会以 500 ms 的间隔发布。

将 `divisor` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `period_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `divisor` | 健康周期除数（Health Period Divisor）响应缓冲区。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga2ef46f0b5059a959d5b06d6e49c4f552"></a>

### `bt_mesh_health_cli_period_set()`

```c
int bt_mesh_health_cli_period_set ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t divisor, uint8_t * updated_divisor )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

设置目标节点的健康快速周期除数（Health Fast Period Divisor）。

健康周期除数（Health Period Divisor）用于在登记故障时提高发布速率。通常，健康服务器（Health Server）按已配置发布参数中的周期发布；登记故障后，发布周期会除以 `(1 << divisor)`。例如，目标节点的健康服务器配置为每 16 秒发布一次，健康快速周期除数（Health Fast Period Divisor）为 5，则登记故障后，健康服务器会以 500 ms 的间隔发布。

将 `updated_divisor` 设为 `NULL` 可以异步（Asynchronously）使用此方法。这样不会等待响应，而是在发送命令后立即返回。

若要处理异步方法（Async Method）的响应参数，请在 `bt_mesh_health_cli` 结构体中注册 `period_status` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `divisor` | 新的健康周期除数（Health Period Divisor）。 |
| `updated_divisor` | 健康周期除数（Health Period Divisor）响应缓冲区。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga536c631d87daaca017af078d49094fc1"></a>

### `bt_mesh_health_cli_period_set_unack()`

```c
int bt_mesh_health_cli_period_set_unack ( struct bt_mesh_health_cli * cli, struct bt_mesh_msg_ctx * ctx, uint8_t divisor )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

设置目标节点的健康快速周期除数（Health Fast Period Divisor），无需确认（Unacknowledged）。

这是此 API 的无需确认版本（Unacknowledged Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 用于发送的客户端模型（Client Model）。 |
| `ctx` | 消息上下文（Message Context）；为 `NULL` 时使用已配置的发布参数（Publish Parameters）。 |
| `divisor` | 新的健康周期除数（Health Period Divisor）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga9abc0db22da327d02d23371bba59b46a"></a>

### `bt_mesh_health_cli_timeout_get()`

```c
int32_t bt_mesh_health_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="gaf3d54597a74a458df0053bd0599d39e9"></a>

### `bt_mesh_health_cli_timeout_set()`

```c
void bt_mesh_health_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |


## 6.5\_原页交叉引用（Cross References）

- [bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/bluetooth/mesh/health_cli.h](../api_file_system_power_reference/P015_zephyr__bluetooth__mesh__health_cli.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_HEALTH_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gab58b85b7a77feeb579973177c12bb446)
- [健康客户端模型（Health Client Model）](P006_健康客户端模型（Health Client Model）.md)
- [健康故障（Health Faults）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gab58b85b7a77feeb579973177c12bb446"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_蓝牙 Mesh BLOB 模型 API.md) · [返回大纲](大纲.md) · [下一章](P007_电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）.md)
