---
id: learning.zephyr-docs.hardware.uartevent-0
title: UART发送事件结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__tx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第335章\_UART发送事件结构

原文：[structuart__event__tx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__tx.html)。读取日期：2026-10-13，`latest`。

## 335.1\_发送结果数据

[`uart_event_tx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__tx.html) 保存通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX）事件数据，声明来自 `zephyr/drivers/uart.h`。

## 335.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a314a676a4050b2438b6f41485656bdbd"></a>[`buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__tx.html#a314a676a4050b2438b6f41485656bdbd) | `const uint8_t *` | 指向当前缓冲区 |
| <a id="a7d844b2c0833d24accf82d58ee3408ff"></a>[`len`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__tx.html#a7d844b2c0833d24accf82d58ee3408ff) | `size_t` | 已发送的字节数 |

---

[上一章：UART异步接口](P334_UART异步接口.md) · [下一章：UART接收事件结构](P336_UART接收事件结构.md) · [返回大纲](大纲.md)
