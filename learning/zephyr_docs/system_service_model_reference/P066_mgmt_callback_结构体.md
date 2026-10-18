---
id: learning.zephyr-docs.system-service-model-reference.page-66
title: mgmt_callback_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_mgmt\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理（MGMT）的回调结构。

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

<a id="details"></a>

管理（MGMT）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a4595cb6a72ebf8b9396e63a8f31c497f"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a4595cb6a72ebf8b9396e63a8f31c497f)。

条目列表节点（Entry list node）。

<a id="r_acd79e73a2a3d44697bbda2b401d1e7df"></a>

```c
mgmt_cb callback
```

相关声明：[mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)、[callback](#acd79e73a2a3d44697bbda2b401d1e7df)。

将要调用的回调。

<a id="r_a3dc18e5f7e3e00c1c05cc104bb1f3ab1"></a>

```c
uint32_t event_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[event_id](#a3dc18e5f7e3e00c1c05cc104bb1f3ab1)。

触发此处理函数的 `MGMT_EVT_[...]` 事件 ID。

## 66.2\_详细说明（Detailed Documentation）

<a id="acd79e73a2a3d44697bbda2b401d1e7df"></a>

### `callback`

```c
mgmt_cb mgmt_callback::callback
```

将要调用的回调。

<a id="a3dc18e5f7e3e00c1c05cc104bb1f3ab1"></a>

### `event_id`

```c
uint32_t mgmt_callback::event_id
```

触发此处理函数的 `MGMT_EVT_[...]` 事件 ID。

使用 `MGMT_EVT_OP_ALL` 时具有特殊含义，覆盖所有组的所有事件；使用 `MGMT_EVT_OP_*_MGMT_ALL` 时，覆盖单个组的所有事件。对于属于同一组的事件，可以按位或（OR）组合，使一次注册在多个事件上触发。注意，这只适用于同一组；不同组的事件必须分别注册。

<a id="a4595cb6a72ebf8b9396e63a8f31c497f"></a>

### `node`

```c
sys_snode_t mgmt_callback::node
```

条目列表节点（Entry list node）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/mgmt/callbacks.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/mgmt/callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [mgmt_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gae61f705224a859776ee5161dfda5ed7d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [MGMT_EVT_OP_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_mcumgr_serial_rx_ctxt_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_mgmt_evt_op_cmd_arg_结构体.md)
