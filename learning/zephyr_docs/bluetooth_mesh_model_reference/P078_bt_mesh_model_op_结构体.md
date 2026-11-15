---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-78
title: bt_mesh_model_op_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_bt\_mesh\_model\_op\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模型操作码（Model Opcode）的处理程序。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

模型操作码（Model Opcode）的处理程序。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_a09c18a889e08bc708b9dc623f8177e39"></a>

```c
const uint32_t opcode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[opcode](#a09c18a889e08bc708b9dc623f8177e39)。

使用 `BT_MESH_MODEL_OP_*` 宏编码的操作码（OpCode）。

<a id="r_a25445fe2e937a321942c312bd675e486"></a>

```c
const ssize_t len
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[len](#a25445fe2e937a321942c312bd675e486)。

消息长度（Message length）。

<a id="r_a4a5de7a12f2f8743048aafc81af0cece"></a>

```c
int(*const func )(const struct bt_mesh_model *model, struct bt_mesh_msg_ctx *ctx, struct net_buf_simple *buf)
```

相关声明：[func](#a4a5de7a12f2f8743048aafc81af0cece)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[bt_mesh_msg_ctx](P082_bt_mesh_msg_ctx_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

此操作码的处理函数（Opcode handler function）。

## 78.2\_详细说明（Detailed Documentation）

<a id="a4a5de7a12f2f8743048aafc81af0cece"></a>

### `func`

```c
int(*const bt_mesh_model_op::func) (const struct bt_mesh_model *model, struct bt_mesh_msg_ctx *ctx, struct net_buf_simple *buf)
```

此操作码的处理函数（Opcode handler function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 接收消息的模型实例（Model instance）。 |
| `ctx` | 该消息的消息上下文（Message context）。 |
| `buf` | 包含消息载荷（Message payload）的消息缓冲区，不包含操作码（Opcode）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="a25445fe2e937a321942c312bd675e486"></a>

### `len`

```c
const ssize_t bt_mesh_model_op::len
```

消息长度（Message length）。

若消息长度可变，此值表示最小消息长度（Minimum message length），应为正值；处理函数应根据消息内容验证精确长度。若消息长度固定，此值应为负值。定义此值时使用 `BT_MESH_LEN_*` 宏。

<a id="a09c18a889e08bc708b9dc623f8177e39"></a>

### `opcode`

```c
const uint32_t bt_mesh_model_op::opcode
```

使用 `BT_MESH_MODEL_OP_*` 宏编码的操作码（OpCode）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ctx](P082_bt_mesh_msg_ctx_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_bt_mesh_model_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_bt_mesh_model_pub_结构体.md)
