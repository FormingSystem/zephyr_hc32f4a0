---
id: learning.zephyr-docs.hardware.emulstruct-7
title: MSPI仿真驱动API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第484章\_MSPI仿真驱动API结构

原文：[structemul__mspi__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html)。读取日期：2026-10-13，`latest`。

`struct emul_mspi_driver_api` 定义**多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**控制器仿真器的**应用程序编程接口（Application Programming Interface，API）**。结构位于 `zephyr/drivers/mspi_emul.h`。

## 484.1\_字段顺序与仿真器扩展

控制器接口把普通 MSPI 驱动接口放在首位，再提供仿真器专用的事件触发与查找功能。首字段的位置是原文明确要求，不能任意调整。

| 类型与字段 | 官方说明译文 |
| --- | --- |
| `struct mspi_driver_api mspi_api` | 必须是 `struct emul_mspi_driver_api` 的第一个字段，以使指针类型转换正确工作 |
| `mspi_emul_trigger_event trigger_event` | 仿真器专用：在被仿真的 MSPI 控制器上触发一个事件 |
| `mspi_emul_find_emul find_emul` | 仿真器专用：查找 MSPI 总线上存在的仿真器 |

> 译注：**指针类型转换（Pointer Casting）**依赖这里约定的结构布局。原页没有提供这两个扩展处理函数的完整签名，参数及返回值由相应类型定义说明。

---

[上一章：MSPI仿真设备API结构](P483_MSPI仿真设备API结构.md) · [下一章：仿真器总线联合体](P485_仿真器总线联合体.md) · [返回大纲](大纲.md)
