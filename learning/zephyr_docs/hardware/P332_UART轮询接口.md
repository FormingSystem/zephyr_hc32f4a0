---
id: learning.zephyr-docs.hardware.uartapi-2
title: UART轮询接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第332章\_UART轮询接口

原文：[group__uart__polling](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html)。读取日期：2026-10-13，`latest`。

## 332.1\_轮询读取与阻塞发送

本组提供通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的轮询（Polling）收发函数，声明来自 `zephyr/drivers/uart.h`。读取函数检查当前是否已有数据，没有数据便立即返回；发送函数等待发送器具备空间，会阻塞调用线程。

<a id="gae81ac8cc976a20d774cfbda09e9c983d"></a>

## 332.2\_读取字符

[`uart_poll_in`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html#gae81ac8cc976a20d774cfbda09e9c983d) 从设备读取一个字符：

```c
int uart_poll_in(const struct device *dev, unsigned char *p_char);
```

`dev` 是 UART 设备实例，`p_char` 指向字符存储位置。接收器有有效数据时，函数读取字符并存入 `*p_char`，向调用线程返回 0；否则返回 -1。这是非阻塞（Non-Blocking）调用。

| 返回值 | 含义 |
| --- | --- |
| 0 | 收到一个字符 |
| -1 | 无字符可读，即 UART 输入缓冲区为空 |
| `-ENOSYS` | 未实现该操作 |
| `-EBUSY` | 已通过 [`uart_rx_enable`](P334_UART异步接口.md) 启用异步接收 |

## 332.3\_读取16位数据

<a id="gaad39c1358019bfdcb919da7982743553"></a>

[`uart_poll_in_u16`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html#gaad39c1358019bfdcb919da7982743553) 读取一个 16 位数据项：

```c
int uart_poll_in_u16(const struct device *dev, uint16_t *p_u16);
```

`dev` 为设备实例，`p_u16` 指向 16 位数据存储位置。接收器有有效数据时，将它存入 `*p_u16` 并返回 0；否则返回 -1。此函数同样非阻塞。

| 返回值 | 含义 |
| --- | --- |
| 0 | 数据已到达 |
| -1 | 无数据可读，即 UART 输入缓冲区为空 |
| `-ENOTSUP` | 应用程序编程接口（Application Programming Interface，API）未启用 |
| `-ENOSYS` | 函数未实现 |
| `-EBUSY` | 已通过 [`uart_rx_enable`](P334_UART异步接口.md) 启用异步接收 |

<a id="ga06ba27ba772a7a18462b8cdbc7f9353c"></a>

## 332.4\_发送字符和16位数据

发送函数声明如下：

```c
void uart_poll_out(const struct device *dev, unsigned char out_char);
void uart_poll_out_u16(const struct device *dev, uint16_t out_u16);
```

两者均接收 UART 实例 `dev`。[`uart_poll_out`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html#ga06ba27ba772a7a18462b8cdbc7f9353c) 发送 `out_char` 字符：发送器未满时写入数据寄存器，已满时等待并阻塞调用线程。原文明确指出，该函数阻塞调用线程直到字符发送完毕。

<a id="ga8faa3f58b9098c97e288e9c5f3367fd9"></a>

[`uart_poll_out_u16`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html#ga8faa3f58b9098c97e288e9c5f3367fd9) 发送 `out_u16` 宽数据：发送器未满时向数据寄存器写入一个 16 位数据项，否则等待并阻塞调用线程。原文将其定义为阻塞调用，没有返回状态值。

两者在启用硬件流控制（Hardware Flow Control）时，都要求握手信号允许发送（Clear To Send，CTS）处于有效状态，才能发送数据。

---

[上一章：UART配置结构](P331_UART配置结构.md) · [下一章：UART中断驱动接口](P333_UART中断驱动接口.md) · [返回大纲](大纲.md)
