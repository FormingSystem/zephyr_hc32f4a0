---
id: learning.zephyr-docs.hardware.emulback-0
title: eSPI仿真器链表节点
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第488章\_eSPI仿真器链表节点

原文：[structespi__emul](P488_eSPI仿真器链表节点.md)。读取日期：2026-10-13，`latest`。

`struct espi_emul` 是**增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）**设备仿真器链表中的节点，定义于 `zephyr/drivers/espi_emul.h`。

## 488.1\_节点字段

每个节点关联一个目标仿真器、该设备提供的**应用程序编程接口（Application Programming Interface，API）**和**片选（Chip Select）**值。字段顺序及类型如下：

| 类型与字段 | 官方说明译文 |
| --- | --- |
| `sys_snode_t node` | 原页未提供字段说明；译注：类型为单向链表节点（Singly Linked List Node） |
| `const struct emul *target` | 目标仿真器；所有类型的仿真总线节点都**必须**提供该字段 |
| `const struct emul_espi_device_api *api` | 为该设备提供的 API |
| `uint16_t chipsel` | 被仿真设备的 eSPI 片选值 |

> 译注：[`target`](P488_eSPI仿真器链表节点.md) 指向仿真器实例，[`api`](P488_eSPI仿真器链表节点.md) 指向设备侧接口结构，二者对应不同对象；[`chipsel`](P488_eSPI仿真器链表节点.md) 是 16 位无符号值。

---

[上一章：MSPI总线仿真接口](P487_MSPI总线仿真接口.md) · [下一章：MSPI仿真器链表节点](P489_MSPI仿真器链表节点.md) · [返回大纲](大纲.md)
