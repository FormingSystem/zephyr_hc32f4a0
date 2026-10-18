---
id: learning.zephyr-docs.hardware.emulback-1
title: MSPI仿真器链表节点
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第489章\_MSPI仿真器链表节点

原文：[structmspi__emul](P489_MSPI仿真器链表节点.md)。读取日期：2026-10-13，`latest`。

`struct mspi_emul` 是**多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**设备仿真器链表中的节点，定义于 `zephyr/drivers/mspi_emul.h`。

## 489.1\_控制器链表中的设备引用

节点关联目标仿真器及其**应用程序编程接口（Application Programming Interface，API）**，并记录设备索引（Device Index）。字段如下：

| 类型与字段 | 官方说明译文 |
| --- | --- |
| `sys_snode_t node` | 控制器仿真器链表中的节点 |
| `const struct emul *target` | 目标仿真器；所有类型的仿真总线节点都**必须**提供该字段 |
| `const struct emul_mspi_device_api *api` | 为该设备提供的 API |
| `uint16_t dev_idx` | 设备索引 |

> 译注：[`sys_snode_t`](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493) 是单向链表节点（Singly Linked List Node）类型，[`dev_idx`](P489_MSPI仿真器链表节点.md) 是 16 位无符号值。原页用设备索引标识目标，不应擅自将字段改为其他总线的片选名称。

---

[上一章：eSPI仿真器链表节点](P488_eSPI仿真器链表节点.md) · [下一章：BBRAM仿真后端接口](P490_BBRAM仿真后端接口.md) · [返回大纲](大纲.md)
