---
id: learning.zephyr-docs.hardware.uartrx-2
title: UART异步接收块结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第346章\_UART异步接收块结构

原文：[structuart__async__rx__buf](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html)。读取日期：2026-10-13，`latest`。

## 346.1\_单块缓冲区的声明

[`uart_async_rx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html) 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）异步接收辅助模块使用的结构，声明来自 `zephyr/drivers/serial/uart_async_rx.h`。原页没有整体或逐字段的文字说明，以下保留其成员布局。

## 346.2\_位域与数据成员

| 字段 | 原声明 |
| --- | --- |
| [`wr_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a4dbeb091bddcd92e1fe242517f53bb93) | `uint8_t wr_idx : 7` |
| [`completed`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a1baa442e23d9babb701a7fc28d8408a4) | `uint8_t completed : 1` |
| [`buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#ad03eb3023829258581e54c75e0a66942) | `uint8_t buffer[]` |

前两个字段是位域（Bit Field），分别占 7 位和 1 位；`buffer[]` 为柔性数组成员（Flexible Array Member）。这里只解释原声明的 C 语法，不据名称额外承诺状态转换规则。

---

[上一章：UART异步接收状态结构](P345_UART异步接收状态结构.md) · [下一章：UART异步接收配置结构](P347_UART异步接收配置结构.md) · [返回大纲](大纲.md)
