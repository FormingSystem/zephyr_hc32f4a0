---
id: learning.zephyr-docs.hardware.uartsample-0
title: UART示例目录
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/uart/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第348章\_UART示例目录

原文：[Universal Asynchronous Receiver-Transmitter (UART)](https://docs.zephyrproject.org/latest/samples/drivers/uart/README.html)。读取日期：2026-10-13，`latest`。

## 348.1\_示例范围

这些示例演示通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）驱动的应用程序编程接口（Application Programming Interface，API）。

## 348.2\_选择示例

- [原生 TTY UART](P351_UART原生TTY示例.md)：通过两个 UART 转通用串行总线（Universal Serial Bus，USB）桥接适配器，使用主机原生终端设备驱动收发数据。TTY 是来自 Teletype 的终端设备名称。
- [UART 异步 API](P349_UART异步API示例.md)：演示异步（Asynchronous）API 的用法。
- [UART 回显](P350_UART回显示例.md)：读取控制台（Console）数据并原样发回。
- [UART 透传](P352_UART透传示例.md)：在控制台与另一 UART 接口之间直接转发数据。

相关接口见 [UART 官方驱动说明](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html#uart-api)。

---

[上一章：UART异步接收配置结构](P347_UART异步接收配置结构.md) · [下一章：UART异步API示例](P349_UART异步API示例.md) · [返回大纲](大纲.md)
