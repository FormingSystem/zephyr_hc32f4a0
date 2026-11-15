---
id: learning.zephyr-docs.hardware.uartirq-0
title: UART中断驱动接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第333章\_UART中断驱动接口

原文：[group__uart__interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html)。读取日期：2026-10-13，`latest`。

## 333.1\_中断处理的前提

本页描述通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的中断驱动（Interrupt-Driven）接口，声明来自 `zephyr/drivers/uart.h`。中断请求（Interrupt Request，IRQ）触发后，由中断服务程序（Interrupt Service Routine，ISR）查询状态、搬运数据并确认中断。

发送（Transmit，TX）和接收（Receive，RX）数据经过先进先出队列（First In, First Out，FIFO）。下文 `dev` 均为 UART 设备实例；除单独声明的中断使能/禁用函数外，所列函数均为 `static inline` 辅助接口。

## 333.2\_回调类型与安装

<a id="gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>

应用回调（Callback）类型 [`uart_irq_callback_user_data_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gad7a26b1a1d6212d7d39c05c8ad4ec926) 用于 [`uart_irq_callback_user_data_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gaf469966a56d1fc9f50108201597ee0a0)，参数是设备实例和任意用户数据：

```c
typedef void (*uart_irq_callback_user_data_t)(const struct device *dev,
                                             void *user_data);
int uart_irq_callback_user_data_set(const struct device *dev,
                                    uart_irq_callback_user_data_t cb,
                                    void *user_data);
int uart_irq_callback_set(const struct device *dev,
                          uart_irq_callback_user_data_t cb);
```

<a id="gaf469966a56d1fc9f50108201597ee0a0"></a>

`uart_irq_callback_user_data_set` 设置 IRQ 回调函数指针 `cb`。IRQ 触发时，将指定的 `user_data` 传给回调；ISR 的约束见下文 [`uart_irq_update`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga20cf50f53fb9e09e760c6499fd156ff2)。

<a id="ga5f7af3f7f0d9155349ea3b4fad78956c"></a>

[`uart_irq_callback_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga5f7af3f7f0d9155349ea3b4fad78956c) 是旧式（Legacy）接口，设置 IRQ 回调，在 IRQ 触发时使用设备指针调用所指定函数。它没有单独的用户数据参数；原页没有进一步解释其用户数据取值，不应假定它能传递任意上下文。

两者成功返回 0；`-ENOSYS` 表示函数未实现，`-ENOTSUP` 表示应用程序编程接口（Application Programming Interface，API）未启用。

## 333.3\_先更新中断状态

<a id="ga20cf50f53fb9e09e760c6499fd156ff2"></a>

`uart_irq_update` 必须是 ISR 开始执行的第一项操作，之后才允许调用 [`uart_irq_rx_ready`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gad04073b1b8e3de13b43ae1194561377b)、[`uart_irq_tx_ready`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga5e126b5f19549eb7f5b785b98ebe7638)、[`uart_irq_tx_complete`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga917935a13bf6a5d1e32ef34339e96455) 和 [`uart_irq_is_pending`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gacd8c2978e0f1316dd79bb42baad1c5a7)：

```c
void uart_irq_update(const struct device *dev);
```

该函数根据硬件中断确认（Acknowledgement）方式承担不同职责：

- 对读取寄存器时自动确认中断的设备，缓存状态寄存器值；后续就绪查询等使用缓存值。原文 `use this case` 按上下文理解为使用该缓存。
- 对需要显式确认中断的设备，确认待处理中断，同时缓存原始状态值。
- 对隐式确认中断的设备，可能没有该函数的具体实现；ISR 仍必须执行确认中断所需的动作，通常为接收就绪时调用 [`uart_fifo_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gab10942076ac47ecff29e924098049398)，发送就绪时调用 [`uart_fifo_fill`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gafe42e4719eada7e25904bc9ebfe87791)。

## 333.4\_向发送FIFO填入数据

<a id="gafe42e4719eada7e25904bc9ebfe87791"></a>

<a id="gaa89f58818d8428ad6a11abf692c54c0d"></a>

字节与宽数据的填充函数如下：

```c
int uart_fifo_fill(const struct device *dev, const uint8_t *tx_data, int size);
int uart_fifo_fill_u16(const struct device *dev, const uint16_t *tx_data, int size);
```

两者都应在 UART ISR 中、`uart_irq_tx_ready` 返回真时调用。在 ISR 以外调用，其结果未定义并依赖硬件。反过来，ISR 中已经检测到发送就绪却不调用填充函数，也可能导致未定义行为，例如无限中断循环。

必须检查返回值，因为各硬件的 FIFO 深度不同，常常只有 1。`tx_data` 指向待发数据；普通版本的 `size` 为待发字节数，返回已发送字节数；`_u16` 版本的 `size` 为待发 16 位数据项数量，返回已发送数据项数量。

两者均以 `-ENOSYS` 表示操作不支持或未实现，以 `-ENOTSUP` 表示 API 未启用。

## 333.5\_读取接收FIFO

<a id="gab10942076ac47ecff29e924098049398"></a>

<a id="ga4a3c25dad2290f1f40e4b847e3b83f64"></a>

接收缓冲区通过 `rx_data` 提供，`size` 是该容器大小：

```c
int uart_fifo_read(const struct device *dev, uint8_t *rx_data, const int size);
int uart_fifo_read_u16(const struct device *dev, uint16_t *rx_data, const int size);
```

两者都应在 UART ISR 中、`uart_irq_rx_ready` 返回真时调用；在 ISR 之外调用的结果未定义并依赖硬件。

接收就绪条件是电平触发（Level-Triggered）还是边沿触发（Edge-Triggered），接口没有规定。因此，一旦检测到接收就绪，就必须持续读取 FIFO 中所有可用数据，直到某次读取返回的数据量小于请求量。不能只读一次就假定中断源已经被处理完。

普通版本返回读取的字节数，`_u16` 版本返回读取的 16 位数据项数量。`-ENOSYS` 表示函数未实现，`-ENOTSUP` 表示 API 未启用。

> 译注：原 `_u16` 段落在重复读取要求中仍写 [`uart_fifo_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gab10942076ac47ecff29e924098049398)；这里保留该要求的含义，宽数据应使用匹配的宽数据读取接口与缓冲区。

## 333.6\_使能或禁用中断

以下函数没有返回值，参数均为 UART 实例。发送中断在中断使能寄存器（Interrupt Enable Register，IER）中控制：

```c
void uart_irq_tx_enable(const struct device *dev);
void uart_irq_tx_disable(const struct device *dev);
void uart_irq_rx_enable(const struct device *dev);
void uart_irq_rx_disable(const struct device *dev);
void uart_irq_err_enable(const struct device *dev);
void uart_irq_err_disable(const struct device *dev);
```

<a id="ga9cbd6e33dce6a5b06233cf10077e19cc"></a>

<a id="gaf8a5bc26cd7c32e7bc6516c6f873c45a"></a>

<a id="ga4ec3ae3974da2b3ab94ae7b835d17bad"></a>

<a id="gaa759d7935fdd9ab6ca0761f161389a29"></a>

<a id="ga7c24daae3326bc2959ea13a2be79969f"></a>

<a id="gaaf8a88361807e204f7227fbd1d0e75b2"></a>

[`uart_irq_tx_enable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga9cbd6e33dce6a5b06233cf10077e19cc) / [`uart_irq_tx_disable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gaf8a5bc26cd7c32e7bc6516c6f873c45a) 分别使能或禁用发送中断；[`uart_irq_rx_enable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga4ec3ae3974da2b3ab94ae7b835d17bad) / [`uart_irq_rx_disable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gaa759d7935fdd9ab6ca0761f161389a29) 分别使能或禁用接收中断；[`uart_irq_err_enable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#ga7c24daae3326bc2959ea13a2be79969f) / [`uart_irq_err_disable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gaaf8a88361807e204f7227fbd1d0e75b2) 分别使能或禁用错误中断。

## 333.7\_查询待处理中断与接收就绪

<a id="gad04073b1b8e3de13b43ae1194561377b"></a>

<a id="gacd8c2978e0f1316dd79bb42baad1c5a7"></a>

`uart_irq_is_pending` 判断是否有待处理的 IRQ；`uart_irq_rx_ready` 判断接收缓冲区中是否至少有一个待取字符，即 FIFO 读取能够成功并返回非零数据量：

```c
int uart_irq_is_pending(const struct device *dev);
int uart_irq_rx_ready(const struct device *dev);
```

两者都必须在 UART 中断处理函数中调用，否则结果未定义。调用 `uart_irq_is_pending` 前必须先执行 `uart_irq_update`，否则状态可能过时；`uart_irq_rx_ready` 要求每次进入处理函数时先执行一次 `uart_irq_update`。

`uart_irq_is_pending` 有待处理中断返回 1，没有返回 0；`uart_irq_rx_ready` 有收到的字符可取返回 1，没有返回 0。两者均以 `-ENOSYS` 表示未实现、`-ENOTSUP` 表示 API 未启用。

接收就绪条件可能表示“FIFO 非空”，也可能表示“自上次查询以来收到新字符”，接口不保证是哪一种。这正是前文要求读到本次返回量小于请求量的原因。

## 333.8\_区分可继续填充与全部发送完成

发送状态有两类不同查询：

```c
int uart_irq_tx_ready(const struct device *dev);
int uart_irq_tx_complete(const struct device *dev);
```

<a id="ga5e126b5f19549eb7f5b785b98ebe7638"></a>

`uart_irq_tx_ready` 检查发送缓冲区能否接收更多待发字节，即 [`uart_fifo_fill`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html#gafe42e4719eada7e25904bc9ebfe87791) 是否能成功并返回非零。未就绪返回 0；已就绪时返回单次 `uart_fifo_fill` 至少可以写入的字节数；失败返回负错误码，其中 `-ENOSYS` 为未实现，`-ENOTSUP` 为 API 未启用。

<a id="ga917935a13bf6a5d1e32ef34339e96455"></a>

`uart_irq_tx_complete` 检查发送模块中缓存的全部数据是否已经完整发出，而且发送模块处于空闲状态。满足此条件后，UART 设备或整个系统可以关闭电源。它不能用来判断是否还能填入更多数据；该判断应使用 `uart_irq_tx_ready`。没有剩余待发数据返回 1，尚未传完返回 0；`-ENOSYS` 和 `-ENOTSUP` 含义同上。

两者均必须在 UART ISR 中调用，否则结果未定义；每次进入中断处理函数，在查询前必须先执行一次 `uart_irq_update`。

---

[上一章：UART轮询接口](P332_UART轮询接口.md) · [下一章：UART异步接口](P334_UART异步接口.md) · [返回大纲](大纲.md)
