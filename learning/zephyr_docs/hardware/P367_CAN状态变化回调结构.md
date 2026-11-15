---
id: learning.zephyr-docs.hardware.canstruct-4
title: CAN状态变化回调结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__state__change__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第367章\_CAN状态变化回调结构

原文：[structcan__state__change__callback](https://docs.zephyrproject.org/latest/doxygen/html/structcan__state__change__callback.html)。读取日期：2026-10-13，`latest`。

## 367.1\_注册状态变化通知

[`can_state_change_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__state__change__callback.html) 用于注册控制器局域网（Controller Area Network，CAN）的状态变化回调（Callback），声明来自 `zephyr/drivers/can.h`。可按需要添加多个回调，但每个都必须使用唯一的结构指针。

**注意：**不要在栈上分配这个结构。该类型是不透明（Opaque）的，应用不应直接访问其成员；应通过 `can_init_state_change_callback`、`can_add_state_change_callback`、`can_remove_state_change_callback` 管理。

> 译注：原描述将唯一指针的结构名写为 `struct can_state_callback`；当前页面及字段定义使用 `can_state_change_callback`，这里明确记录原名称差异。

## 367.2\_原页列出的字段

| 字段 | 类型 | 官方说明 |
| --- | --- | --- |
| <a id="a20e10ceff66aefd6e77340687cab3f40"></a>[`node`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__state__change__callback.html#a20e10ceff66aefd6e77340687cab3f40) | [`sys_snode_t`](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493) | 单向链表（Singly Linked List）节点 |
| <a id="a3bf66a334174307bde9c0fe12939a503"></a>[`handler`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__state__change__callback.html#a3bf66a334174307bde9c0fe12939a503) | [`can_state_change_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga1dc18f69fe06a1d919b13f929100fa85) | 回调函数 |

此表保留生成页面的字段信息，不改变应用不得直接访问成员的约束。

---

[上一章：CAN时序结构](P366_CAN时序结构.md) · [下一章：CAN设备状态结构](P368_CAN设备状态结构.md) · [返回大纲](大纲.md)
