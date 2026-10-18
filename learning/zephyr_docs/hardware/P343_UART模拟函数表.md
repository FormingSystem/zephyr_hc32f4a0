---
id: learning.zephyr-docs.hardware.uartemul-2
title: UART模拟函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul__device__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第343章\_UART模拟函数表

原文：[structuart__emul__device__api](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul__device__api.html)。读取日期：2026-10-13，`latest`。

## 343.1\_模拟器操作接口

[`uart_emul_device_api`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul__device__api.html) 定义通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）模拟器（Emulator）的应用程序编程接口（Application Programming Interface，API），声明来自 `zephyr/drivers/uart_emul.h`。

## 343.2\_数据就绪操作

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`tx_data_ready`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__emul__device__api.html#ab44f47b71ef668357bcc5531d287ae9a) | [`uart_emul_device_tx_data_ready_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gab4b5940f6e0c55c594a9ccddae04c8ae) | 发送（Transmit，TX）缓冲区中出现新数据时调用 |

该回调（Callback）的具体参数与签名见 [`uart_emul_device_tx_data_ready_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gab4b5940f6e0c55c594a9ccddae04c8ae)。

---

[上一章：UART模拟器结构](P342_UART模拟器结构.md) · [下一章：UART异步接收辅助接口](P344_UART异步接收辅助接口.md) · [返回大纲](大纲.md)
