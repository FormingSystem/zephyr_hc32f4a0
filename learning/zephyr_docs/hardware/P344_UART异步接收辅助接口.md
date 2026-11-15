---
id: learning.zephyr-docs.hardware.uartrx-0
title: UART异步接收辅助接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第344章\_UART异步接收辅助接口

原文：[uart__async__rx_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html)。读取日期：2026-10-13，`latest`。

## 344.1\_辅助模块与缓冲区开销

`zephyr/drivers/serial/uart_async_rx.h` 是利用通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）异步应用程序编程接口（Asynchronous Application Programming Interface）进行接收（Receive，RX）的辅助模块。原头文件包含 `zephyr/kernel.h`；相关结构为辅助实例 [`uart_async_rx`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html)、配置 [`uart_async_rx_config`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html) 和单块缓冲区 [`uart_async_rx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html)。

初始化时提供的用户缓冲区会划分为多个块（Chunk），每块都要留出管理自身状态的空间。宏 [`UART_ASYNC_RX_BUF_OVERHEAD`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#ab845a83272799083bf3ecd7a9c8cf2ce) 返回每块的管理开销，单位为字节，可据此计算真正用于 UART 数据的空间：

```c
#define UART_ASYNC_RX_BUF_OVERHEAD offsetof(struct uart_async_rx_buf, buffer)
```

`offsetof` 是计算结构成员偏移的 C 宏；这里取 `buffer` 之前的字节数作为管理开销。

## 344.2\_初始化、复位与块长度

以下函数的 `async_rx` 均指向辅助模块实例：

```c
int uart_async_rx_init(struct uart_async_rx *async_rx,
                       const struct uart_async_rx_config *config);
void uart_async_rx_reset(struct uart_async_rx *async_rx);
uint8_t uart_async_rx_get_buf_len(struct uart_async_rx *async_rx);
```

[`uart_async_rx_init`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a8daddb05f11ad43c8c4510a4312cf38f) 初始化实例，`config` 为配置，而且必须持久有效；成功初始化返回 0，原页未列其他返回码。

[`uart_async_rx_reset`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#ad551b1684437c8ab48c0708fb5b0d1f6) 复位辅助实例状态，可在接收中止后调用，用于丢弃所有已接收数据并恢复初始状态。

[`uart_async_rx_get_buf_len`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a9e51885811653d21e0e8712b09ef800d) 为 `static inline` 函数，返回 RX 缓冲区长度。

## 344.3\_取得下一块并转交驱动事件

[`uart_async_rx_buf_req`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a1eede7070affe966616148924ba2c519) 取得下一块接收缓冲区：

```c
uint8_t *uart_async_rx_buf_req(struct uart_async_rx *async_rx);
```

返回指针应交给 [`uart_rx_buf_rsp`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ga3970fe2818e214b0814ea8b73a816a6a) 或 [`uart_rx_enable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ga902e18c2a727ed2988e1b6caa6a444b8)。若返回空指针，说明没有可用缓冲区：所有块都仍由驱动使用，或包含尚未消费的数据。

数据就绪和缓冲区释放通过下列函数报告给辅助模块：

```c
void uart_async_rx_on_rdy(struct uart_async_rx *async_rx,
                          uint8_t *buffer, size_t length);
void uart_async_rx_on_buf_rel(struct uart_async_rx *async_rx, uint8_t *buf);
```

[`uart_async_rx_on_rdy`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#acca21c43fa833b4789edbc1bc92bab2b) 指示已收到数据，必须在 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) 事件上下文中调用；`buffer` 和 `length` 分别来自 UART 驱动事件中的缓冲区及长度。

[`uart_async_rx_on_buf_rel`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a2064f3d760adb4cf6912caf12f7a54cc) 指示驱动不再使用某块缓冲区，必须在收到 [`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) 事件时调用；`buf` 为驱动事件携带的缓冲区指针。

## 344.4\_认领与消费数据

模块采用零拷贝（Zero Copy）方式：直接向使用者提供 UART 驱动写入过的缓冲区指针。接收数据分布在多个缓冲区中，无法一次取得全部数据，只能按块处理。

```c
size_t uart_async_rx_data_claim(struct uart_async_rx *async_rx,
                                 uint8_t **data, size_t length);
bool uart_async_rx_data_consume(struct uart_async_rx *async_rx, size_t length);
```

[`uart_async_rx_data_claim`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a8d5ed81dfa4c067f173249744b25561e) 认领（Claim）收到的数据以供处理。`data` 指向用于接收缓冲区地址的位置，没有数据可认领时该位置保持不变；`length` 是请求数据量。返回该缓冲区中的有效数据量，没有数据时返回 0。

处理完后，调用配对的 [`uart_async_rx_data_consume`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a1ac0b3ee0e1840177d07c4fbcbd635df) 表示数据已经消费（Consume）。其 `length` 必须小于或等于已认领的数据量。消费之后，缓冲池（Buffer Pool）中有空闲块时返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，没有空闲块时返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。

---

[上一章：UART模拟函数表](P343_UART模拟函数表.md) · [下一章：UART异步接收状态结构](P345_UART异步接收状态结构.md) · [返回大纲](大纲.md)
