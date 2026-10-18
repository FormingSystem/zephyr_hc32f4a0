---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-17
title: zephyr__bluetooth__mesh__msg.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_bluetooth\_\_mesh\_\_msg.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息（Message）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

消息（Message）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fmsg_5Fctx"></a>

```c
struct bt_mesh_msg_ctx
```

相关声明：[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)。

消息发送上下文（Message Sending Context）。

<a id="r_bt_5Fmesh_5Fmsg_5Fack_5Fctx"></a>

```c
struct bt_mesh_msg_ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

已确认消息（Acknowledged Message）的上下文，用于跟踪等待响应的模型消息状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_ga658d38a7be18355f6ecd5f7fb4dcabed"></a>

```c
#define BT_MESH_MIC_SHORT 4
```

相关声明：[BT_MESH_MIC_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga658d38a7be18355f6ecd5f7fb4dcabed)。

短 Mesh 消息完整性检查值（MIC）的长度。

<a id="r_ga6e8fc0bb4ed35870c0f1652c18a8117d"></a>

```c
#define BT_MESH_MIC_LONG 8
```

相关声明：[BT_MESH_MIC_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga6e8fc0bb4ed35870c0f1652c18a8117d)。

长 Mesh 消息完整性检查值（MIC）的长度。

<a id="r_gad0b5f56cc9741fcd5dadf157c5e62701"></a>

```c
#define BT_MESH_MODEL_OP_LEN(_op)
```

相关声明：[BT_MESH_MODEL_OP_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gad0b5f56cc9741fcd5dadf157c5e62701)。

用于确定操作码长度（Opcode Length）的辅助接口。

<a id="r_ga5352d6fa05808722eba8a76e2446eddb"></a>

```c
#define BT_MESH_MODEL_BUF_LEN(_op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga5352d6fa05808722eba8a76e2446eddb)。

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

<a id="r_gabb16a024db39706af46ad86e2b04b00d"></a>

```c
#define BT_MESH_MODEL_BUF_LEN_LONG_MIC(_op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_LEN_LONG_MIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gabb16a024db39706af46ad86e2b04b00d)。

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

<a id="r_ga6a61ace773e331d82860b343d51f62e7"></a>

```c
#define BT_MESH_MODEL_BUF_DEFINE(_buf, _op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga6a61ace773e331d82860b343d51f62e7)。

使用 `NET_BUF_SIMPLE_DEFINE` 定义 Mesh 模型消息缓冲区（Model Message Buffer）。

<a id="r_ga90200861df2575a974e7414e3642058a"></a>

```c
#define BT_MESH_MSG_CTX_INIT(net_key_idx, app_key_idx, dst, ttl)
```

相关声明：[BT_MESH_MSG_CTX_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga90200861df2575a974e7414e3642058a)。

用于初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga98470d8a351528f4ccb8c0ef2edbc030"></a>

```c
#define BT_MESH_MSG_CTX_INIT_APP(app_key_idx, dst)
```

相关声明：[BT_MESH_MSG_CTX_INIT_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga98470d8a351528f4ccb8c0ef2edbc030)。

用于初始化由应用密钥（Application Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga3cab6b5e400a205befdc5a6c7609c453"></a>

```c
#define BT_MESH_MSG_CTX_INIT_DEV(net_key_idx, dst)
```

相关声明：[BT_MESH_MSG_CTX_INIT_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga3cab6b5e400a205befdc5a6c7609c453)。

用于初始化由远端设备的设备密钥（Device Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga4afe7dad3e38f7e54d65ca608adc9ba3"></a>

```c
#define BT_MESH_MSG_CTX_INIT_PUB(pub)
```

相关声明：[BT_MESH_MSG_CTX_INIT_PUB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga4afe7dad3e38f7e54d65ca608adc9ba3)。

使用模型发布上下文（Model Publication Context）初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_gaa26850aebc9bfc97d1dafb66ba02021c"></a>

```c
void bt_mesh_model_msg_init (struct net_buf_simple *msg, uint32_t opcode)
```

相关声明：[bt_mesh_model_msg_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gaa26850aebc9bfc97d1dafb66ba02021c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化模型消息（Model Message）。

<a id="r_gadd25e335133fe29f234243a39f4d7626"></a>

```c
static void bt_mesh_msg_ack_ctx_init (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gadd25e335133fe29f234243a39f4d7626)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

初始化需确认消息上下文（Acknowledged Message Context）。

<a id="r_ga86d3803bde26f496b7de3fa348a04525"></a>

```c
static void bt_mesh_msg_ack_ctx_reset (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga86d3803bde26f496b7de3fa348a04525)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

复位需确认消息上下文（Acknowledged Message Context）中的同步信号量（Synchronization Semaphore）。

<a id="r_ga3da92606640cdba69a676c2a03c72311"></a>

```c
void bt_mesh_msg_ack_ctx_clear (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga3da92606640cdba69a676c2a03c72311)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

清除需确认消息上下文（Acknowledged Message Context）的参数。

<a id="r_ga1bb34a904103933140e2159cb53d49f5"></a>

```c
int bt_mesh_msg_ack_ctx_prepare (struct bt_mesh_msg_ack_ctx *ack, uint32_t op, uint16_t dst, void *user_data)
```

相关声明：[bt_mesh_msg_ack_ctx_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga1bb34a904103933140e2159cb53d49f5)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

准备需确认消息上下文（Acknowledged Message Context），用于等待传入消息。

<a id="r_ga974ba5d7df597a21945b75ac5919debd"></a>

```c
static bool bt_mesh_msg_ack_ctx_busy (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_msg_ack_ctx_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga974ba5d7df597a21945b75ac5919debd)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

检查需确认消息上下文（Acknowledged Message Context）是否已使用某个操作码（Opcode）初始化。

<a id="r_ga83561f4d003c6c3c2b91a6afd180d1fd"></a>

```c
int bt_mesh_msg_ack_ctx_wait (struct bt_mesh_msg_ack_ctx *ack, k_timeout_t timeout)
```

相关声明：[bt_mesh_msg_ack_ctx_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga83561f4d003c6c3c2b91a6afd180d1fd)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待消息确认（Message Acknowledge）。

<a id="r_ga2b054f7dc01daeef067cd3d819a7c42c"></a>

```c
static void bt_mesh_msg_ack_ctx_rx (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga2b054f7dc01daeef067cd3d819a7c42c)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

将消息标记为已确认（Acknowledged）。

<a id="r_gae10c4229cabf7774684c99154d4ed8ae"></a>

```c
bool bt_mesh_msg_ack_ctx_match (const struct bt_mesh_msg_ack_ctx *ack, uint32_t op, uint16_t addr, void **user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_msg_ack_ctx_match](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gae10c4229cabf7774684c99154d4ed8ae)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查消息的操作码（Opcode）和地址是否与预期值匹配。


## 17.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P566_msg.h_源码浏览.md)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [BT_MESH_MIC_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga658d38a7be18355f6ecd5f7fb4dcabed)
- [BT_MESH_MIC_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga6e8fc0bb4ed35870c0f1652c18a8117d)
- [BT_MESH_MODEL_OP_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gad0b5f56cc9741fcd5dadf157c5e62701)
- [BT_MESH_MODEL_BUF_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga5352d6fa05808722eba8a76e2446eddb)
- [BT_MESH_MODEL_BUF_LEN_LONG_MIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gabb16a024db39706af46ad86e2b04b00d)
- [BT_MESH_MODEL_BUF_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga6a61ace773e331d82860b343d51f62e7)
- [NET_BUF_SIMPLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf85aa0b705bb4fbe2630191fde802501)
- [BT_MESH_MSG_CTX_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga90200861df2575a974e7414e3642058a)
- [BT_MESH_MSG_CTX_INIT_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga98470d8a351528f4ccb8c0ef2edbc030)
- [BT_MESH_MSG_CTX_INIT_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga3cab6b5e400a205befdc5a6c7609c453)
- [BT_MESH_MSG_CTX_INIT_PUB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga4afe7dad3e38f7e54d65ca608adc9ba3)
- [bt_mesh_model_msg_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gaa26850aebc9bfc97d1dafb66ba02021c)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_msg_ack_ctx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gadd25e335133fe29f234243a39f4d7626)
- [bt_mesh_msg_ack_ctx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga86d3803bde26f496b7de3fa348a04525)
- [bt_mesh_msg_ack_ctx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga3da92606640cdba69a676c2a03c72311)
- [bt_mesh_msg_ack_ctx_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga1bb34a904103933140e2159cb53d49f5)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_msg_ack_ctx_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga974ba5d7df597a21945b75ac5919debd)
- [bt_mesh_msg_ack_ctx_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga83561f4d003c6c3c2b91a6afd180d1fd)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_mesh_msg_ack_ctx_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga2b054f7dc01daeef067cd3d819a7c42c)
- [bt_mesh_msg_ack_ctx_match](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gae10c4229cabf7774684c99154d4ed8ae)

<a id="header-details"></a>

---

[上一章](P016_zephyr__kernel__mm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__comparator__nrf_lpcomp.h_文件参考.md)
