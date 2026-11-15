---
id: learning.zephyr-docs.hardware.uartevent-1
title: UART接收事件结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第336章\_UART接收事件结构

原文：[structuart__event__rx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html)。读取日期：2026-10-13，`latest`。

## 336.1\_本次收到的数据范围

[`uart_event_rx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html) 保存通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的接收（Receive，RX）事件数据，声明来自 `zephyr/drivers/uart.h`。

原文将事件代表的数据范围写作从 `rx.buf[rx.offset]` 到 `rx.buf[rx.offset+rx.len]`，并强调长度相对于偏移量（Offset）计算。

> 译注：[`len`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html#a96414b96e63503336f8cf0d2249cd3bd) 明确表示新收到的字节数，所以这段数据应按从 [`offset`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html#aa483e719298c30b9f5e6c57d3d161281) 开始的 `len` 个字节理解，即半开区间 `[offset, offset + len)`；不能把原文“到”字后的表达式当成还要额外读取一个末尾字节。

## 336.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a2d9dfa9d9b25ff976cf2e937c72eb245"></a>[`buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__event__rx.html#a2d9dfa9d9b25ff976cf2e937c72eb245) | `uint8_t *` | 当前缓冲区指针 |
| <a id="aa483e719298c30b9f5e6c57d3d161281"></a>`offset` | `size_t` | 当前收到的数据在缓冲区中的偏移，以字节计 |
| <a id="a96414b96e63503336f8cf0d2249cd3bd"></a>`len` | `size_t` | 新收到的字节数 |

---

[上一章：UART发送事件结构](P335_UART发送事件结构.md) · [下一章：UART缓冲区释放事件结构](P337_UART缓冲区释放事件结构.md) · [返回大纲](大纲.md)
