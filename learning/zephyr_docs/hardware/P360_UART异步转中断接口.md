---
id: learning.zephyr-docs.hardware.uartutil-2
title: UART异步转中断接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第360章\_UART异步转中断接口

原文：[uart__async__to__irq_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html)。读取日期：2026-10-13，`latest`。

## 360.1\_适配层及头文件

`zephyr/drivers/serial/uart_async_to_irq.h` 将通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的异步应用程序编程接口（Asynchronous Application Programming Interface，API）适配成中断驱动（Interrupt-Driven）接口。中断请求（Interrupt Request，IRQ）上下文由下文跳转函数接入。

原页列出的包含文件为：

```c
#include <zephyr/drivers/uart.h>
#include <zephyr/logging/log.h>
#include <zephyr/spinlock.h>
#include <zephyr/sys/util.h>
#include <zephyr/drivers/serial/uart_async_rx.h>
```

## 360.2\_配置初始化器

`UART_ASYNC_TO_IRQ_API_CONFIG_INITIALIZER(_api, _trampoline, _baudrate, _tx_buf, _tx_len, _rx_buf, _rx_len, _rx_cnt, _log)` 生成配置结构初始化器。

发送（Transmit，TX）和接收（Receive，RX）各自有缓冲区及长度；接收缓冲区会被划分成多个块。跳转函数（Trampoline）负责转入中断上下文。参数逐项如下：

| 参数 | 含义 |
| --- | --- |
| `_api` | 保存 UART 异步 API 的结构 |
| `_trampoline` | 转入中断上下文的函数 |
| `_baudrate` | UART 波特率（Baud Rate） |
| `_tx_buf` | TX 缓冲区 |
| `_tx_len` | TX 缓冲区长度 |
| `_rx_buf` | RX 缓冲区 |
| `_rx_len` | RX 缓冲区长度 |
| `_rx_cnt` | RX 缓冲区分成的块数 |
| `_log` | 日志实例，留空时使用默认实例 |

下面是原展开式。其中 [`IS_EMPTY`](../util_reference/P001_通用工具公共接口.md#gab9487eea703d51cb1f235432dab4a1c7) 检测参数是否为空，[`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 按条件选择默认或指定日志对象；`LOG_OBJECT_PTR_INIT`、`LOG_OBJECT_PTR` 是对应日志对象指针初始化/取值宏。

```c
{                                                                                       \
        .tx_buf = _tx_buf,                                                              \
        .tx_len = _tx_len,                                                              \
        .async_rx = {                                                                   \
                .buffer = _rx_buf,                                                      \
                .length = _rx_len,                                                      \
                .buf_cnt = _rx_cnt                                                      \
        },                                                                              \
        .api = _api,                                                                    \
        .trampoline = _trampoline,                                                      \
        .baudrate = _baudrate,                                                          \
        LOG_OBJECT_PTR_INIT(log,                                                        \
                        COND_CODE_1(IS_EMPTY(_log),                                     \
                                    (LOG_OBJECT_PTR(UART_ASYNC_TO_IRQ_LOG_NAME)),       \
                                    (_log)                                              \
                                   )                                                    \
                           )                                                            \
}
```

## 360.3\_中断API初始化器

[`UART_ASYNC_TO_IRQ_API_INIT()`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#a9cad504475c43ca9578285fa3d332c70) 应用于驱动 UART API 结构的初始化，为其提供中断驱动接口函数。它把先进先出队列（First In, First Out，FIFO）的读写以及中断控制、就绪查询和回调设置映射到适配层函数：

```c
.fifo_fill        = z_uart_async_to_irq_fifo_fill,      \
.fifo_read        = z_uart_async_to_irq_fifo_read,      \
.irq_tx_enable    = z_uart_async_to_irq_irq_tx_enable,  \
.irq_tx_disable   = z_uart_async_to_irq_irq_tx_disable, \
.irq_tx_ready     = z_uart_async_to_irq_irq_tx_ready,   \
.irq_rx_enable    = z_uart_async_to_irq_irq_rx_enable,  \
.irq_rx_disable   = z_uart_async_to_irq_irq_rx_disable, \
.irq_tx_complete  = z_uart_async_to_irq_irq_tx_complete,\
.irq_rx_ready     = z_uart_async_to_irq_irq_rx_ready,   \
.irq_err_enable   = z_uart_async_to_irq_irq_err_enable, \
.irq_err_disable  = z_uart_async_to_irq_irq_err_disable,\
.irq_is_pending   = z_uart_async_to_irq_irq_is_pending, \
.irq_update       = NULL,                               \
.irq_callback_set = z_uart_async_to_irq_irq_callback_set
```

原展开式中的 `irq_update` 为 `NULL`，其余字段按所列 `z_uart_async_to_irq_*` 函数初始化。

## 360.4\_跳转类型与适配层初始化

跳转函数类型与对应回调如下，原页仅给出类型签名；回调（Callback）应从跳转上下文中调用：

```c
typedef void (*uart_async_to_irq_trampoline)(const struct device *dev);
void uart_async_to_irq_trampoline_cb(const struct device *dev);
int uart_async_to_irq_init(const struct device *dev);
```

各函数的 `dev` 为 UART 设备。[`uart_async_to_irq_init`](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#aae442237aa3432348c256807df3ffa1c) 初始化适配层，该设备必须支持异步 API；初始化成功返回 0，原页未列其他返回码。

## 360.5\_接收控制声明

原页还列出以下两个函数，没有参数、返回值或行为的详细文字说明：

```c
int uart_async_to_irq_rx_enable(const struct device *dev);
int uart_async_to_irq_rx_disable(const struct device *dev);
```

名称分别表示接收启用与禁用；这里保留声明，不额外假定其错误码或同步完成条件。

---

[上一章：UART模拟控制接口](P359_UART模拟控制接口.md) · [下一章：CAN公共接口](P361_CAN公共接口.md) · [返回大纲](大纲.md)
