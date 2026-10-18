---
id: learning.zephyr-docs.hardware.uartevent-5
title: UART事件数据联合体
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第340章\_UART事件数据联合体

原文：[unionuart__event_1_1uart__event__data](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html)。读取日期：2026-10-13，`latest`。

## 340.1\_按事件类型选择数据

`uart_event::uart_event_data` 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的事件数据联合体（Union），声明来自 `zephyr/drivers/uart.h`。发送（Transmit，TX）、接收（Receive，RX）、缓冲区释放和接收停止使用不同成员。

## 340.2\_成员与事件对应关系

| 字段 | 类型 | 对应事件 |
| --- | --- | --- |
| <a id="a79fb6b799d5574c6aa38a211e020035f"></a>[`tx`](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html#a79fb6b799d5574c6aa38a211e020035f) | `struct uart_event_tx` | [`UART_TX_DONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) 发送完成及 [`UART_TX_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) 发送中止 |
| <a id="afac00624290b8fe5cf7b59516567b972"></a>[`rx`](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html#afac00624290b8fe5cf7b59516567b972) | `struct uart_event_rx` | [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) 接收数据就绪 |
| <a id="ac03cdaeccba5f693337fa19299101863"></a>[`rx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html#ac03cdaeccba5f693337fa19299101863) | `struct uart_event_rx_buf` | [`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) 接收缓冲区释放 |
| <a id="aad7488a2a3d91cea0ea874a08d7b88f6"></a>[`rx_stop`](https://docs.zephyrproject.org/latest/doxygen/html/unionuart__event_1_1uart__event__data.html#aad7488a2a3d91cea0ea874a08d7b88f6) | `struct uart_event_rx_stop` | [`UART_RX_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) 接收停止 |

---

[上一章：UART事件联合结构](P339_UART事件联合结构.md) · [下一章：UART模拟接口](P341_UART模拟接口.md) · [返回大纲](大纲.md)
