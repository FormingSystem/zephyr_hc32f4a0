---
id: learning.zephyr-docs.hardware.uartutil-1
title: UART模拟控制接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第359章\_UART模拟控制接口

原文：[serial_2uart__emul_8h](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html)。读取日期：2026-10-13，`latest`。

## 359.1\_模拟UART的后端操作

`zephyr/drivers/serial/uart_emul.h` 提供模拟（Emulated）通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的后端应用程序编程接口（Application Programming Interface，API），包含 `zephyr/device.h` 和 `zephyr/types.h`。

这些函数在模拟设备的接收（Receive，RX）缓冲区中注入数据，从发送（Transmit，TX）缓冲区提取数据，并控制模拟的错误和超时释放行为。下文 `dev` 均为模拟 UART 设备实例。

## 359.2\_发送数据就绪回调

应用回调（Callback）类型及设置函数如下：

```c
typedef void (*uart_emul_callback_tx_data_ready_t)(const struct device *dev,
                                                  size_t size,
                                                  void *user_data);
void uart_emul_callback_tx_data_ready_set(const struct device *dev,
                                          uart_emul_callback_tx_data_ready_t cb,
                                          void *user_data);
```

回调中的 `size` 为发送缓冲区中可用的字节数，`user_data` 为任意用户数据。设置函数用 `cb` 指定回调指针，`user_data` 指定转交给回调的数据。此后每次向 TX 缓冲区追加数据，都会调用该回调。

## 359.3\_注入接收与读取发送

数据搬运接口为：

```c
uint32_t uart_emul_put_rx_data(const struct device *dev,
                               const uint8_t *data, size_t size);
uint32_t uart_emul_get_tx_data(const struct device *dev,
                               uint8_t *data, size_t size);
```

[`uart_emul_put_rx_data`](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#ad0a91bf5b91639c912f41bd93aeacd69) 向 RX 缓冲区写入并复制数据；`data` 指向待追加内容，`size` 为请求追加的字节数，返回实际追加字节数。

[`uart_emul_get_tx_data`](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#ae8aba3de78a625318524abfd46da1daa) 从 TX 缓冲区读取数据；`data` 为输出缓冲区地址，`size` 为请求读取的字节数，返回实际写入输出缓冲区的字节数。

## 359.4\_清空缓冲区与模拟错误

清空函数声明如下：

```c
uint32_t uart_emul_flush_rx_data(const struct device *dev);
uint32_t uart_emul_flush_tx_data(const struct device *dev);
```

两者分别清空 RX 或 TX 缓冲区内容，并返回清除的字节数。

```c
void uart_emul_set_errors(const struct device *dev, int errors);
void uart_emul_set_release_buffer_on_timeout(const struct device *dev,
                                              bool release_on_timeout);
```

[`uart_emul_set_errors`](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#a305c155ed8a824e7ddec0ad078669aa0) 设置一个或多个驱动错误，`errors` 使用 [`uart_rx_stop_reason`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gadeba6c5485e01dfc1c8a6e1c21668a88) 定义的错误标志。

[`uart_emul_set_release_buffer_on_timeout`](https://docs.zephyrproject.org/latest/doxygen/html/serial_2uart__emul_8h.html#af15ff078214f0c7a96fc8c0091a8f922) 配置 RX 缓冲区超时后是否释放，即使只填充了部分内容。`release_on_timeout` 为 `true` 时，超时会释放缓冲区。

---

[上一章：UART桥接接口](P358_UART桥接接口.md) · [下一章：UART异步转中断接口](P360_UART异步转中断接口.md) · [返回大纲](大纲.md)
