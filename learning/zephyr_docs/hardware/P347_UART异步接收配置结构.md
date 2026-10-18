---
id: learning.zephyr-docs.hardware.uartrx-3
title: UART异步接收配置结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第347章\_UART异步接收配置结构

原文：[structuart__async__rx__config](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html)。读取日期：2026-10-13，`latest`。

## 347.1\_辅助模块配置

[`uart_async_rx_config`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html) 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）异步接收（Asynchronous Receive，RX）辅助模块的配置结构，声明来自 `zephyr/drivers/serial/uart_async_rx.h`。

## 347.2\_字段声明

原页仅列出以下成员，没有逐字段文字说明：

| 字段 | 原类型 |
| --- | --- |
| [`buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a2d5d07f7e98ae6743378f75ce3afc4f2) | `uint8_t *` |
| [`length`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#ad4eabc44a27b06f93b0d6194903b6b97) | `size_t` |
| [`buf_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a73a1c096f5aac03f3426c7320241fcf2) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |

配置对象通过 `uart_async_rx_init` 传给辅助实例；该初始化接口明确要求配置持久有效。缓冲区划分及每块管理开销的说明见[异步接收辅助接口](P344_UART异步接收辅助接口.md)。

---

[上一章：UART异步接收块结构](P346_UART异步接收块结构.md) · [下一章：UART示例目录](P348_UART示例目录.md) · [返回大纲](大纲.md)
