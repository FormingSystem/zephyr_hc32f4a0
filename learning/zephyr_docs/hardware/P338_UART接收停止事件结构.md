---
id: learning.zephyr-docs.hardware.uartevent-3
title: UART接收停止事件结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__stop.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第338章\_UART接收停止事件结构

原文：[structuart__event__rx__stop](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__stop.html)。读取日期：2026-10-13，`latest`。

## 338.1\_停止原因与最后一段数据

[`uart_event_rx_stop`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__stop.html) 保存通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的接收（Receive，RX）停止数据，声明来自 `zephyr/drivers/uart.h`。它同时记录停止原因和最后接收到的数据。

## 338.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a96fbae85208d9b3ea0382e7e236a932d"></a>[`reason`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__stop.html#a96fbae85208d9b3ea0382e7e236a932d) | `enum uart_rx_stop_reason` | 接收停止的原因 |
| <a id="a1b361c8b7e17d1304a475235e734db48"></a>[`data`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx__stop.html#a1b361c8b7e17d1304a475235e734db48) | `struct uart_event_rx` | 最后收到的数据 |

---

[上一章：UART缓冲区释放事件结构](P337_UART缓冲区释放事件结构.md) · [下一章：UART事件联合结构](P339_UART事件联合结构.md) · [返回大纲](大纲.md)
