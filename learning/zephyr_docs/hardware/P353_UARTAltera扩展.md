---
id: learning.zephyr-docs.hardware.uartext-0
title: UARTAltera扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第353章\_UARTAltera扩展

原文：[uart__altera_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h.html)。读取日期：2026-10-13，`latest`。

## 353.1\_专用头文件

`zephyr/drivers/serial/uart_altera.h` 是 Altera 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的头文件；Altera 是此驱动的硬件系列名称。原生成页面只列出两个命令宏，没有逐项参数说明。

## 353.2\_包结束命令

| 宏 | 原定义 |
| --- | --- |
| [`CMD_ENABLE_EOP`](https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h.html#acd0b56a568b2ee566e3749a07baa4ded) | `0x01` |
| [`CMD_DISABLE_EOP`](https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h.html#adcc3a86b997151efa6970b2a12d4ecc2) | `0x02` |

> 译注：以下解释来自同一官方头文件中未进入生成页面的普通注释，参见[官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/serial/uart_altera.h)。包结束（End Of Packet，EOP）功能在收到包结束字符时触发中断；须启用 Kconfig 配置项 `CONFIG_UART_DRV_CMD` 和 `CONFIG_UART_ALTERA_EOP`。通过 `uart_drv_cmd` 传入 `CMD_ENABLE_EOP` 启用。该命令写入硬件寄存器，并在驱动设置一个标志，使下一次 `uart_irq_callback_user_data_set` 设置 EOP 中断回调；该设置函数调用后，标志清除。`CMD_DISABLE_EOP` 为禁用命令。

---

[上一章：UART透传示例](P352_UART透传示例.md) · [下一章：UARTInfineonCAT1扩展](P354_UARTInfineonCAT1扩展.md) · [返回大纲](大纲.md)
