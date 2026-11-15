---
id: learning.zephyr-docs.hardware.uartevent-2
title: UART缓冲区释放事件结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第337章\_UART缓冲区释放事件结构

原文：[structuart__event__rx__buf](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__buf.html)。读取日期：2026-10-13，`latest`。

## 337.1\_释放的缓冲区

[`uart_event_rx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__buf.html) 保存通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的接收（Receive，RX）缓冲区释放事件数据，声明来自 `zephyr/drivers/uart.h`。

## 337.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a2547c84b742f454cfedf1de6d433297b"></a>[`buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__buf.html#a2547c84b742f454cfedf1de6d433297b) | `uint8_t *` | 指向已经不再使用的缓冲区 |

---

[上一章：UART接收事件结构](P336_UART接收事件结构.md) · [下一章：UART接收停止事件结构](P338_UART接收停止事件结构.md) · [返回大纲](大纲.md)
