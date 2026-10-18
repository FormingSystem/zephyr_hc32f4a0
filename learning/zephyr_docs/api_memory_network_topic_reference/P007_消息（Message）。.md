---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-7
title: 消息（Message）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_消息（Message）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息（Message）。

<a id="details"></a>

消息（Message）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

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

## 7.2\_宏定义（Macros）

<a id="r_ga658d38a7be18355f6ecd5f7fb4dcabed"></a>

```c
#define BT_MESH_MIC_SHORT 4
```

相关声明：[BT_MESH_MIC_SHORT](#ga658d38a7be18355f6ecd5f7fb4dcabed)。

短 Mesh 消息完整性检查值（MIC）的长度。

<a id="r_ga6e8fc0bb4ed35870c0f1652c18a8117d"></a>

```c
#define BT_MESH_MIC_LONG 8
```

相关声明：[BT_MESH_MIC_LONG](#ga6e8fc0bb4ed35870c0f1652c18a8117d)。

长 Mesh 消息完整性检查值（MIC）的长度。

<a id="r_gad0b5f56cc9741fcd5dadf157c5e62701"></a>

```c
#define BT_MESH_MODEL_OP_LEN(_op)
```

相关声明：[BT_MESH_MODEL_OP_LEN](#gad0b5f56cc9741fcd5dadf157c5e62701)。

用于确定操作码长度（Opcode Length）的辅助接口。

<a id="r_ga5352d6fa05808722eba8a76e2446eddb"></a>

```c
#define BT_MESH_MODEL_BUF_LEN(_op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_LEN](#ga5352d6fa05808722eba8a76e2446eddb)。

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

<a id="r_gabb16a024db39706af46ad86e2b04b00d"></a>

```c
#define BT_MESH_MODEL_BUF_LEN_LONG_MIC(_op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_LEN_LONG_MIC](#gabb16a024db39706af46ad86e2b04b00d)。

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

<a id="r_ga6a61ace773e331d82860b343d51f62e7"></a>

```c
#define BT_MESH_MODEL_BUF_DEFINE(_buf, _op, _payload_len)
```

相关声明：[BT_MESH_MODEL_BUF_DEFINE](#ga6a61ace773e331d82860b343d51f62e7)。

使用 `NET_BUF_SIMPLE_DEFINE` 定义 Mesh 模型消息缓冲区（Model Message Buffer）。

<a id="r_ga90200861df2575a974e7414e3642058a"></a>

```c
#define BT_MESH_MSG_CTX_INIT(net_key_idx, app_key_idx, dst, ttl)
```

相关声明：[BT_MESH_MSG_CTX_INIT](#ga90200861df2575a974e7414e3642058a)。

用于初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga98470d8a351528f4ccb8c0ef2edbc030"></a>

```c
#define BT_MESH_MSG_CTX_INIT_APP(app_key_idx, dst)
```

相关声明：[BT_MESH_MSG_CTX_INIT_APP](#ga98470d8a351528f4ccb8c0ef2edbc030)。

用于初始化由应用密钥（Application Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga3cab6b5e400a205befdc5a6c7609c453"></a>

```c
#define BT_MESH_MSG_CTX_INIT_DEV(net_key_idx, dst)
```

相关声明：[BT_MESH_MSG_CTX_INIT_DEV](#ga3cab6b5e400a205befdc5a6c7609c453)。

用于初始化由远端设备的设备密钥（Device Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="r_ga4afe7dad3e38f7e54d65ca608adc9ba3"></a>

```c
#define BT_MESH_MSG_CTX_INIT_PUB(pub)
```

相关声明：[BT_MESH_MSG_CTX_INIT_PUB](#ga4afe7dad3e38f7e54d65ca608adc9ba3)。

使用模型发布上下文（Model Publication Context）初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_gaa26850aebc9bfc97d1dafb66ba02021c"></a>

```c
void bt_mesh_model_msg_init (struct net_buf_simple *msg, uint32_t opcode)
```

相关声明：[bt_mesh_model_msg_init](#gaa26850aebc9bfc97d1dafb66ba02021c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化模型消息（Model Message）。

<a id="r_gadd25e335133fe29f234243a39f4d7626"></a>

```c
static void bt_mesh_msg_ack_ctx_init (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_init](#gadd25e335133fe29f234243a39f4d7626)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

初始化需确认消息上下文（Acknowledged Message Context）。

<a id="r_ga86d3803bde26f496b7de3fa348a04525"></a>

```c
static void bt_mesh_msg_ack_ctx_reset (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_reset](#ga86d3803bde26f496b7de3fa348a04525)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

复位需确认消息上下文（Acknowledged Message Context）中的同步信号量（Synchronization Semaphore）。

<a id="r_ga3da92606640cdba69a676c2a03c72311"></a>

```c
void bt_mesh_msg_ack_ctx_clear (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_clear](#ga3da92606640cdba69a676c2a03c72311)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

清除需确认消息上下文（Acknowledged Message Context）的参数。

<a id="r_ga1bb34a904103933140e2159cb53d49f5"></a>

```c
int bt_mesh_msg_ack_ctx_prepare (struct bt_mesh_msg_ack_ctx *ack, uint32_t op, uint16_t dst, void *user_data)
```

相关声明：[bt_mesh_msg_ack_ctx_prepare](#ga1bb34a904103933140e2159cb53d49f5)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

准备需确认消息上下文（Acknowledged Message Context），用于等待传入消息。

<a id="r_ga974ba5d7df597a21945b75ac5919debd"></a>

```c
static bool bt_mesh_msg_ack_ctx_busy (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_msg_ack_ctx_busy](#ga974ba5d7df597a21945b75ac5919debd)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

检查需确认消息上下文（Acknowledged Message Context）是否已使用某个操作码（Opcode）初始化。

<a id="r_ga83561f4d003c6c3c2b91a6afd180d1fd"></a>

```c
int bt_mesh_msg_ack_ctx_wait (struct bt_mesh_msg_ack_ctx *ack, k_timeout_t timeout)
```

相关声明：[bt_mesh_msg_ack_ctx_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待消息确认（Message Acknowledge）。

<a id="r_ga2b054f7dc01daeef067cd3d819a7c42c"></a>

```c
static void bt_mesh_msg_ack_ctx_rx (struct bt_mesh_msg_ack_ctx *ack)
```

相关声明：[bt_mesh_msg_ack_ctx_rx](#ga2b054f7dc01daeef067cd3d819a7c42c)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)。

将消息标记为已确认（Acknowledged）。

<a id="r_gae10c4229cabf7774684c99154d4ed8ae"></a>

```c
bool bt_mesh_msg_ack_ctx_match (const struct bt_mesh_msg_ack_ctx *ack, uint32_t op, uint16_t addr, void **user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_msg_ack_ctx_match](#gae10c4229cabf7774684c99154d4ed8ae)、[bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查消息的操作码（Opcode）和地址是否与预期值匹配。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga6e8fc0bb4ed35870c0f1652c18a8117d"></a>

### `BT_MESH_MIC_LONG`

```c
#define BT_MESH_MIC_LONG 8
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

长 Mesh 消息完整性检查值（MIC）的长度。

<a id="ga658d38a7be18355f6ecd5f7fb4dcabed"></a>

### `BT_MESH_MIC_SHORT`

```c
#define BT_MESH_MIC_SHORT 4
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

短 Mesh 消息完整性检查值（MIC）的长度。

<a id="ga6a61ace773e331d82860b343d51f62e7"></a>

### `BT_MESH_MODEL_BUF_DEFINE`

```c
#define BT_MESH_MODEL_BUF_DEFINE ( _buf, _op, _payload_len )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
NET_BUF_SIMPLE_DEFINE(_buf, BT_MESH_MODEL_BUF_LEN(_op, (_payload_len)))
```

使用 `NET_BUF_SIMPLE_DEFINE` 定义 Mesh 模型消息缓冲区（Model Message Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_buf` | 缓冲区名称（Buffer Name）。 |
| `_op` | 消息操作码（Opcode）。 |
| `_payload_len` | 模型消息载荷长度（Model Message Payload Length）。 |

<a id="ga5352d6fa05808722eba8a76e2446eddb"></a>

### `BT_MESH_MODEL_BUF_LEN`

```c
#define BT_MESH_MODEL_BUF_LEN ( _op, _payload_len )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
(BT_MESH_MODEL_OP_LEN(_op) + (_payload_len) + BT_MESH_MIC_SHORT)
```

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

返回 Mesh 模型消息缓冲区长度，包括操作码长度和短消息完整性校验码（Short MIC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_op` | 消息操作码（Opcode）。 |
| `_payload_len` | 模型载荷长度（Model Payload Length）。 |

<a id="gabb16a024db39706af46ad86e2b04b00d"></a>

### `BT_MESH_MODEL_BUF_LEN_LONG_MIC`

```c
#define BT_MESH_MODEL_BUF_LEN_LONG_MIC ( _op, _payload_len )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
(BT_MESH_MODEL_OP_LEN(_op) + (_payload_len) + BT_MESH_MIC_LONG)
```

用于确定模型消息缓冲区长度（Model Message Buffer Length）的辅助接口。

返回 Mesh 模型消息缓冲区长度，包括操作码长度和长消息完整性校验码（Long MIC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_op` | 消息操作码（Opcode）。 |
| `_payload_len` | 模型载荷长度（Model Payload Length）。 |

<a id="gad0b5f56cc9741fcd5dadf157c5e62701"></a>

### `BT_MESH_MODEL_OP_LEN`

```c
#define BT_MESH_MODEL_OP_LEN ( _op)
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
((_op) <= 0xff ? 1 : (_op) <= 0xffff ? 2 : 3)
```

用于确定操作码长度（Opcode Length）的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_op` | 操作码（Opcode）。 |

<a id="ga90200861df2575a974e7414e3642058a"></a>

### `BT_MESH_MSG_CTX_INIT`

```c
#define BT_MESH_MSG_CTX_INIT ( net_key_idx, app_key_idx, dst, ttl )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
{ \
        .net_idx = (net_key_idx), \
        .app_idx = (app_key_idx), \
        .addr = (dst), \
        .send_ttl = (ttl), \
}
```

用于初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_key_idx` | 用于发送消息的子网网络密钥索引（NetKey Index），仅在 app_key_idx 指向 devkey 时使用。 |
| `app_key_idx` | 加密消息所用的应用密钥索引（AppKey Index）。 |
| `dst` | 远端地址（Remote Address）。 |
| `ttl` | 生存时间（Time To Live，TTL）。 |

**说明（Note）**：注意（Note）：dst 为虚拟地址（Virtual Address）时，必须单独初始化标签 UUID（Label UUID）。

<a id="ga98470d8a351528f4ccb8c0ef2edbc030"></a>

### `BT_MESH_MSG_CTX_INIT_APP`

```c
#define BT_MESH_MSG_CTX_INIT_APP ( app_key_idx, dst )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
BT_MESH_MSG_CTX_INIT(0, app_key_idx, dst, BT_MESH_TTL_DEFAULT)
```

用于初始化由应用密钥（Application Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_key_idx` | 加密消息所用的应用密钥索引（AppKey Index）。 |
| `dst` | 远端地址（Remote Address）。 |

<a id="ga3cab6b5e400a205befdc5a6c7609c453"></a>

### `BT_MESH_MSG_CTX_INIT_DEV`

```c
#define BT_MESH_MSG_CTX_INIT_DEV ( net_key_idx, dst )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
BT_MESH_MSG_CTX_INIT(net_key_idx, BT_MESH_KEY_DEV_REMOTE, dst, BT_MESH_TTL_DEFAULT)
```

用于初始化由远端设备的设备密钥（Device Key）保护的 `bt_mesh_msg_ctx` 结构体的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_key_idx` | 发送消息所用子网的网络密钥索引（NetKey Index）。 |
| `dst` | 远端地址（Remote Address）。 |

<a id="ga4afe7dad3e38f7e54d65ca608adc9ba3"></a>

### `BT_MESH_MSG_CTX_INIT_PUB`

```c
#define BT_MESH_MSG_CTX_INIT_PUB ( pub)
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

展开值（Value）：

```c
{ \
        .app_idx = (pub)->key, \
        .addr = (pub)->addr, \
        .send_ttl = (pub)->ttl, \
        .uuid = (pub)->uuid, \
}
```

使用模型发布上下文（Model Publication Context）初始化 `bt_mesh_msg_ctx` 结构体的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pub` | 指向模型发布上下文（Model Publication Context）的指针。 |

<a id="gaa26850aebc9bfc97d1dafb66ba02021c"></a>

### `bt_mesh_model_msg_init()`

```c
void bt_mesh_model_msg_init ( struct net_buf_simple * msg, uint32_t opcode )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

初始化模型消息（Model Message）。

清空消息缓冲区内容并编码给定操作码（Opcode），随后可向消息缓冲区填入载荷数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `msg` | 消息缓冲区（Message Buffer）。 |
| `opcode` | 待编码的操作码（Opcode）。 |

<a id="ga974ba5d7df597a21945b75ac5919debd"></a>

### `bt_mesh_msg_ack_ctx_busy()`

```c
bool bt_mesh_msg_ack_ctx_busy ( struct bt_mesh_msg_ack_ctx * ack)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

检查需确认消息上下文（Acknowledged Message Context）是否已使用某个操作码（Opcode）初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 需确认消息上下文（Acknowledged Message Context）。 |

**返回（Returns）**：返回值（Returns）：需确认消息上下文已用操作码初始化时返回 true，否则返回 false。

<a id="ga3da92606640cdba69a676c2a03c72311"></a>

### `bt_mesh_msg_ack_ctx_clear()`

```c
void bt_mesh_msg_ack_ctx_clear ( struct bt_mesh_msg_ack_ctx * ack)
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

清除需确认消息上下文（Acknowledged Message Context）的参数。

清除 bt_mesh_msg_ack_ctx_prepare 设置的操作码、远端地址及用户数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待清除的需确认消息上下文（Acknowledged Message Context）。 |

<a id="gadd25e335133fe29f234243a39f4d7626"></a>

### `bt_mesh_msg_ack_ctx_init()`

```c
void bt_mesh_msg_ack_ctx_init ( struct bt_mesh_msg_ack_ctx * ack)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

初始化需确认消息上下文（Acknowledged Message Context）。

初始化用于在 bt_mesh_msg_ack_ctx_wait 与 bt_mesh_msg_ack_ctx_rx 调用之间同步的信号量（Semaphore）。使用 bt_mesh_msg_ack_ctx 前调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待初始化的需确认消息上下文（Acknowledged Message Context）。 |

<a id="gae10c4229cabf7774684c99154d4ed8ae"></a>

### `bt_mesh_msg_ack_ctx_match()`

```c
bool bt_mesh_msg_ack_ctx_match ( const struct bt_mesh_msg_ack_ctx * ack, uint32_t op, uint16_t addr, void ** user_data )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

检查消息的操作码（Opcode）和地址是否与预期值匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待检查的需确认消息上下文（Acknowledged Message Context）。 |
| `op` | 入站消息操作码（OpCode）。 |
| `addr` | 入站消息源地址（Source Address）。 |
| `user_data` | 非 NULL 时，返回由 bt_mesh_msg_ack_ctx_prepare 存入需确认消息上下文的用户数据。 |

**返回（Returns）**：返回值（Returns）：入站消息与预期消息匹配时返回 true，否则返回 false。

<a id="ga1bb34a904103933140e2159cb53d49f5"></a>

### `bt_mesh_msg_ack_ctx_prepare()`

```c
int bt_mesh_msg_ack_ctx_prepare ( struct bt_mesh_msg_ack_ctx * ack, uint32_t op, uint16_t dst, void * user_data )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

准备需确认消息上下文（Acknowledged Message Context），用于等待传入消息。

设置入站消息的操作码和远端地址，并存储用户数据。在调用 bt_mesh_msg_ack_ctx_wait 前使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待准备的需确认消息上下文（Acknowledged Message Context）。 |
| `op` | 消息操作码（OpCode）。 |
| `dst` | 消息目标地址（Destination Address）。 |
| `user_data` | 需确认消息上下文的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga86d3803bde26f496b7de3fa348a04525"></a>

### `bt_mesh_msg_ack_ctx_reset()`

```c
void bt_mesh_msg_ack_ctx_reset ( struct bt_mesh_msg_ack_ctx * ack)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

复位需确认消息上下文（Acknowledged Message Context）中的同步信号量（Synchronization Semaphore）。

中止对 bt_mesh_msg_ack_ctx_wait 的调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待重置的需确认消息上下文（Acknowledged Message Context）。 |

<a id="ga2b054f7dc01daeef067cd3d819a7c42c"></a>

### `bt_mesh_msg_ack_ctx_rx()`

```c
void bt_mesh_msg_ack_ctx_rx ( struct bt_mesh_msg_ack_ctx * ack)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

将消息标记为已确认（Acknowledged）。

解除对 bt_mesh_msg_ack_ctx_wait 调用的阻塞。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待确认消息的上下文（Message Context）。 |

<a id="ga83561f4d003c6c3c2b91a6afd180d1fd"></a>

### `bt_mesh_msg_ack_ctx_wait()`

```c
int bt_mesh_msg_ack_ctx_wait ( struct bt_mesh_msg_ack_ctx * ack, k_timeout_t timeout )
```

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

等待消息确认（Message Acknowledge）。

阻塞执行，直到调用 bt_mesh_msg_ack_ctx_rx 或超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ack` | 待等待消息的需确认消息上下文（Acknowledged Message Context）。 |
| `timeout` | 等待超时（Wait Timeout）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 7.5\_原页交叉引用（Cross References）

- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [NET_BUF_SIMPLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf85aa0b705bb4fbe2630191fde802501)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/bluetooth/mesh/msg.h](../api_file_mesh_interrupt_reference/P017_zephyr__bluetooth__mesh__msg.h_文件参考.md)
- [BT_MESH_TTL_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga16516272b42420263b1c47c3ea16c0c8)
- [BT_MESH_KEY_DEV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaaa6ffb62df5d6d55c831d4d9860fc7eb)
- [uuid](../data_utilities/P026_UUID二进制结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__mesh__msg_html_ga5352d6fa05808722eba8a76e2446eddb"></a>
<a id="agroup__net__buf_html_gaf85aa0b705bb4fbe2630191fde802501"></a>
<a id="agroup__bt__mesh__msg_html_ga658d38a7be18355f6ecd5f7fb4dcabed"></a>
<a id="agroup__bt__mesh__msg_html_gad0b5f56cc9741fcd5dadf157c5e62701"></a>
<a id="agroup__bt__mesh__msg_html_ga6e8fc0bb4ed35870c0f1652c18a8117d"></a>
<a id="agroup__bt__mesh__access_html_ga16516272b42420263b1c47c3ea16c0c8"></a>
<a id="agroup__bt__mesh__msg_html_ga90200861df2575a974e7414e3642058a"></a>
<a id="agroup__bt__mesh__access_html_gaaa6ffb62df5d6d55c831d4d9860fc7eb"></a>
<a id="astructuuid_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）.md) · [返回大纲](大纲.md) · [下一章](P008_RFCOMM API主题.md)
