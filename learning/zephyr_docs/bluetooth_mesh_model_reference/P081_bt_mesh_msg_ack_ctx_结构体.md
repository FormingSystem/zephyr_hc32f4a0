---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-81
title: bt_mesh_msg_ack_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ack__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_bt\_mesh\_msg\_ack\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ack__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已确认消息（Acknowledged Message）的上下文，用于跟踪等待响应的模型消息状态。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

<a id="details"></a>

已确认消息（Acknowledged Message）的上下文，用于跟踪等待响应的模型消息状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_a53ce3e10f27da773c227de6d6eaba5e3"></a>

```c
struct k_sem sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sem](#a53ce3e10f27da773c227de6d6eaba5e3)。

同步信号量（Sync semaphore）。

<a id="r_a08f50fcae687026c45d891c9381bd9c2"></a>

```c
uint32_t op
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[op](#a08f50fcae687026c45d891c9381bd9c2)。

正在等待的操作码（Opcode）。

<a id="r_ac83626299e197dbd0a9a36a6617c3b21"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#ac83626299e197dbd0a9a36a6617c3b21)。

应作出响应的节点地址（Node address）。

<a id="r_a510baede03d53b2419ade8da6d02fa10"></a>

```c
void * user_data
```

相关声明：[user_data](#a510baede03d53b2419ade8da6d02fa10)。

用户专用参数（User specific parameter）。

## 81.2\_详细说明（Detailed Documentation）

<a id="ac83626299e197dbd0a9a36a6617c3b21"></a>

### `dst`

```c
uint16_t bt_mesh_msg_ack_ctx::dst
```

应作出响应的节点地址（Node address）。

<a id="a08f50fcae687026c45d891c9381bd9c2"></a>

### `op`

```c
uint32_t bt_mesh_msg_ack_ctx::op
```

正在等待的操作码（Opcode）。

<a id="a53ce3e10f27da773c227de6d6eaba5e3"></a>

### `sem`

```c
struct k_sem bt_mesh_msg_ack_ctx::sem
```

同步信号量（Sync semaphore）。

<a id="a510baede03d53b2419ade8da6d02fa10"></a>

### `user_data`

```c
void* bt_mesh_msg_ack_ctx::user_data
```

用户专用参数（User specific parameter）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/msg.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h_source.html)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_bt_mesh_models_metadata_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_bt_mesh_msg_ctx_结构体.md)
