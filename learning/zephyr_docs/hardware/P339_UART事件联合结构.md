---
id: learning.zephyr-docs.hardware.uartevent-4
title: UART事件联合结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第339章\_UART事件联合结构

原文：[structuart__event](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html)。读取日期：2026-10-13，`latest`。

## 339.1\_当前事件信息

[`uart_event`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html) 保存通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的当前事件信息，声明来自 `zephyr/drivers/uart.h`。事件类型决定哪部分事件数据有效。

## 339.2\_字段与嵌套联合体

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a2fb82a30e414a74943067cd0784f4b44"></a>[`type`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html#a2fb82a30e414a74943067cd0784f4b44) | `enum uart_event_type` | 事件类型 |
| <a id="a07e3eebb7642ab52c73baba514704c69"></a>[`data`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html#a07e3eebb7642ab52c73baba514704c69) | `union uart_event::uart_event_data` | 事件数据；有效成员取决于 [`type`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html#a2fb82a30e414a74943067cd0784f4b44) |

嵌套联合体（Union）[`uart_event_data`](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html) 保存各类事件的数据成员。联合体成员共享存储，使用时应根据 [`type`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event.html#a2fb82a30e414a74943067cd0784f4b44) 选择当前有效的成员。

---

[上一章：UART接收停止事件结构](P338_UART接收停止事件结构.md) · [下一章：UART事件数据联合体](P340_UART事件数据联合体.md) · [返回大纲](大纲.md)
