---
id: learning.zephyr-docs.hardware.uartrx-1
title: UART异步接收状态结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第345章\_UART异步接收状态结构

原文：[structuart__async__rx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html)。读取日期：2026-10-13，`latest`。

## 345.1\_辅助实例状态

[`uart_async_rx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html) 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的异步接收（Asynchronous Receive，RX）辅助结构，声明来自 `zephyr/drivers/serial/uart_async_rx.h`。

原生成页面仅给出成员声明，没有逐字段的文字说明。以下保留完整字段与类型，不把字段名推测当成官方接口约定。[`atomic_t`](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8) 是 Zephyr 的原子整数（Atomic Integer）类型。

## 345.2\_字段声明

| 字段 | 原类型 |
| --- | --- |
| [`config`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#abbe20b7426175d7436470f6a26bb578e) | `const struct uart_async_rx_config *` |
| [`pending_bytes`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a1150d2c365330c4d87a22b44412611f6) | [`atomic_t`](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8) |
| [`free_buf_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a15510449c58841c7294e0359a92bf4d0) | [`atomic_t`](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8) |
| [`buf_len`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a85ea611224160caee86767b4910e17d9) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |
| [`drv_buf_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ac782b9465c3766d5217676a3a97a963b) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |
| [`rd_buf_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a9a192c4f08f6d946bb562a9bbba8f196) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |
| [`rd_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ad75410820beef5a612f602d3017df5f6) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |

这些状态由异步接收辅助接口配合维护；初始化、驱动事件通知以及认领/消费操作见[异步接收辅助接口](P344_UART异步接收辅助接口.md)。

---

[上一章：UART异步接收辅助接口](P344_UART异步接收辅助接口.md) · [下一章：UART异步接收块结构](P346_UART异步接收块结构.md) · [返回大纲](大纲.md)
