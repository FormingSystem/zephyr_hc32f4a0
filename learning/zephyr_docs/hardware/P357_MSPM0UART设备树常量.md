---
id: learning.zephyr-docs.hardware.uartext-4
title: MSPM0UART设备树常量
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第357章\_MSPM0UART设备树常量

原文：[mspm0__uart_8h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html)。读取日期：2026-10-13，`latest`。

## 357.1\_FIFO阈值编码

`zephyr/dt-bindings/uart/mspm0_uart.h` 定义 Texas Instruments（TI）MSPM0 系列通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的先进先出队列（First In, First Out，FIFO）阈值。TI 是厂商名称，MSPM0 是芯片系列名称。

接收（Receive，RX）阈值描述 FIFO 已有数据的程度；发送（Transmit，TX）阈值描述 FIFO 空闲空间的程度。表中的数字是设备树（Devicetree）配置编码，不是具体 FIFO 字节容量。

## 357.2\_接收FIFO阈值

| 宏 | 原值 | 含义 |
| --- | --- | --- |
| [`MSPM0_UART_RX_FIFO_LEVEL_ONE_ENTRY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a81752114cf58619faaf7682794b8dde6) | `0` | 至少有一个数据项 |
| [`MSPM0_UART_RX_FIFO_LEVEL_1_4_FULL`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a7e197f436ea0f401112781473def306e) | `1` | 接收 FIFO 已占四分之一 |
| [`MSPM0_UART_RX_FIFO_LEVEL_1_2_FULL`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a6f3b138e5c81b06dea0b78768b257220) | `2` | 接收 FIFO 已占二分之一 |
| [`MSPM0_UART_RX_FIFO_LEVEL_3_4_FULL`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a02a6720decc03385995ec84be1ed8f51) | `3` | 接收 FIFO 已占四分之三 |
| [`MSPM0_UART_RX_FIFO_LEVEL_FULL`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a0981d920b46a32d2a2cbaa5f2744b1ad) | `4` | 接收 FIFO 已满 |

## 357.3\_发送FIFO阈值

| 宏 | 原值 | 含义 |
| --- | --- | --- |
| [`MSPM0_UART_TX_FIFO_LEVEL_ONE_ENTRY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a9f8d5ae914418712bee55e353d7a6b5a) | `0` | 发送 FIFO 至少有一个可用空位 |
| [`MSPM0_UART_TX_FIFO_LEVEL_1_4_EMPTY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a9451e776c0b74d7ebcb237c2b34dd533) | `1` | 发送 FIFO 有四分之一空闲 |
| [`MSPM0_UART_TX_FIFO_LEVEL_1_2_EMPTY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a957ae01e6884afb28d1c73b9e51c0fa5) | `2` | 发送 FIFO 有二分之一空闲 |
| [`MSPM0_UART_TX_FIFO_LEVEL_3_4_EMPTY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#a3105b9ef53f0e447f933e493a3da5819) | `3` | 发送 FIFO 有四分之三空闲 |
| [`MSPM0_UART_TX_FIFO_LEVEL_EMPTY`](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h.html#ab5126ace41380cd59218a5a46d7e607f) | `4` | 发送 FIFO 为空 |

---

[上一章：UARTNS16550扩展](P356_UARTNS16550扩展.md) · [下一章：UART桥接接口](P358_UART桥接接口.md) · [返回大纲](大纲.md)
