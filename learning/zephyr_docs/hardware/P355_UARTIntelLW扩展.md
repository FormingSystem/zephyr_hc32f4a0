---
id: learning.zephyr-docs.hardware.uartext-2
title: UARTIntelLW扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第355章\_UARTIntelLW扩展

原文：[uart__intel__lw_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html)。读取日期：2026-10-13，`latest`。

## 355.1\_驱动命令定义

`zephyr/drivers/serial/uart_intel_lw.h` 是 Intel LW 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的头文件，Intel LW 为此驱动的硬件名称。原生成页面仅列出六个命令宏。

| 宏 | 原定义 |
| --- | --- |
| [`CMD_ENABLE_EOP`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#acd0b56a568b2ee566e3749a07baa4ded) | `0x01` |
| [`CMD_DISABLE_EOP`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#adcc3a86b997151efa6970b2a12d4ecc2) | `0x02` |
| [`CMD_TRBK_EN`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#a6f9a2c319edecf29eeed485a84d408c3) | `0x03` |
| [`CMD_TRBK_DIS`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#a492530b2df4cbb9771c2e068ed872173) | `0x04` |
| [`CMD_POLL_ASSERT_RTS`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#a18ee5cdca3047268a54e9a228d5b4d16) | `0x05` |
| [`CMD_POLL_DEASSERT_RTS`](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h.html#af2d3ec81ffd531601140f0bbfd01d0af) | `0x06` |

## 355.2\_源码注释补充

> 译注：本节翻译[同一官方头文件的普通注释](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/serial/uart_intel_lw.h)，这些说明未显示在原生成页面。

包结束（End Of Packet，EOP）功能在收到包结束字符时产生中断，需要启用 Kconfig 配置项 `CONFIG_UART_INTEL_LW_EOP`。调用 `uart_drv_cmd` 并传入 `CMD_ENABLE_EOP` 启用：它写入硬件寄存器并设置驱动标志，让下一次 `uart_irq_callback_user_data_set` 设置 EOP 中断回调；调用该设置函数后标志清除。`CMD_DISABLE_EOP` 禁用该功能。

发送断线（Transmit Break，宏中写作 TRBK）功能通过 `uart_drv_cmd` 的 `CMD_TRBK_EN` 中断正在进行的发送；此后 UART 无法发送任何数据。使用 `CMD_TRBK_DIS` 恢复正常工作。原源码注释还要求调用 `uart_intel_lw_err_check` 清除发送 Break 导致的错误；此处保留原函数名，不把它当成公共头文件已经声明的通用函数。

该驱动支持中断驱动（Interrupt-Driven）应用程序编程接口（Application Programming Interface，API）。在正常操作期间直接轮询数据可能产生意外行为。需要轮询收发时，先用 `uart_drv_cmd` 发送 `CMD_POLL_ASSERT_RTS`，使请求发送（Request To Send，RTS）有效；轮询结束后再发送 `CMD_POLL_DEASSERT_RTS`，恢复正常操作。

---

[上一章：UARTInfineonCAT1扩展](P354_UARTInfineonCAT1扩展.md) · [下一章：UARTNS16550扩展](P356_UARTNS16550扩展.md) · [返回大纲](大纲.md)
