---
id: learning.zephyr-docs.hardware.uart
title: 通用异步收发器UART
kind: reference
status: maintained
domains: [zephyr, uart, driver]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="uart-api"></a>

# 第6章\_通用异步收发器UART

原文：[Universal Asynchronous Receiver-Transmitter (UART)](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html)。读取日期：2026-10-12，`latest`。

Zephyr 提供三种访问**通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）**的方式：轮询 **应用程序编程接口（Application Programming Interface，API）**、中断驱动 API，以及使用**直接内存访问（Direct Memory Access，DMA）**的异步 API。不同方式使用不同接口。

## 6.1\_三种访问方式

轮询是最基本的方式。接收函数 `uart_poll_in()` 不阻塞，没有有效数据时返回 `-1`；发送函数 `uart_poll_out()` 会阻塞，调用线程等待指定字符发送完毕。

> 译注：原文把 `uart_poll_in()` 描述为“返回一个字符或 -1”。实际接口通过字符指针参数交付数据，函数返回状态，成功为 `0`，无数据为 `-1`；不要把返回值直接当收到的字符。具体扩展错误条件以驱动/API 参考为准。

中断驱动方式允许较慢的通信在后台进行，线程继续执行其他工作。线程与 UART 驱动之间可通过内核[数据传递机制](https://docs.zephyrproject.org/latest/kernel/services/index.html#kernel-data-passing-api)交换数据。

异步 API 通过 DMA 在后台读写数据，但配置比前两种方式复杂。原文将其描述为不需要中断 MCU。

> 译注：DMA 可免去 **中央处理器（Central Processing Unit，CPU）** 对每个字节的搬运，但不能把这句话理解为异步 UART 完全不使用中断。原文下一段也明确说明异步 API 需要硬件中断；完成、错误或缓冲区相关事件仍可能通过中断处理。

**同一个硬件外设不能同时使用中断驱动 API 和异步 API。** 两者都需要硬件中断，同时启用各自回调会互相干扰。`CONFIG_UART_EXCLUSIVE_API_CALLBACKS` 默认启用，确保同一时刻只有一组 API 回调处于活动状态。

## 6.2\_配置选项

Kconfig 决定是否可使用默认的轮询、中断驱动或异步 API。为了减小内存占用，只启用需要的功能。原文列出的配置项如下：

- [CONFIG_SERIAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)
- [CONFIG_UART_INTERRUPT_DRIVEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)
- [CONFIG_UART_ASYNC_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)
- [CONFIG_UART_WIDE_DATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_WIDE_DATA)
- [CONFIG_UART_USE_RUNTIME_CONFIGURE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)
- [CONFIG_UART_LINE_CTRL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LINE_CTRL)
- [CONFIG_UART_DRV_CMD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_DRV_CMD)

## 6.3\_接口参考

原文按以下四个入口组织 API：

- [UART 总体 API](P330_UART公共接口.md)
- [轮询 API](P332_UART轮询接口.md)
- [中断驱动 API](P333_UART中断驱动接口.md)
- [异步 API](P334_UART异步接口.md)

这些自动生成参考为独立页面，本章完整翻译 UART 说明页，不将外链页面计作已完成。

## 6.4\_相关示例

原文列出的全部相关示例如下：

| 示例 | 内容 |
| --- | --- |
| [802.15.4 serial-radio](https://docs.zephyrproject.org/latest/samples/net/wpan_serial/README.html) | 为基于 Contiki 的边界路由器实现 slip-radio 设备。 |
| [AT 命令客户端](../driver_samples/P019_AT命令客户端示例.md) | 在控制台与调制解调器之间建立双向 UART 桥，用于 AT 命令通信。 |
| [USB CDC ACM 控制台](../usb/P055_CDCACM控制台示例.md) | 通过 **通用串行总线（Universal Serial Bus，USB）** CDC ACM 控制台输出 Hello World。 |
| [HCI 三线 H:5](../bluetooth_samples/P017_HCI三线传输.md) | 通过 H5:**主机控制器接口（Host Controller Interface，HCI）** 传输向另一设备或 CPU 暴露蓝牙控制器。 |
| [HCI UART](../bluetooth_samples/P016_HCI_UART传输.md) | 通过 UART 向另一设备或 CPU 暴露蓝牙控制器。 |
| [HCI 异步 UART](../bluetooth_samples/P018_HCI异步UART传输.md) | 通过异步 UART 暴露蓝牙控制器。 |
| [旧版 USB CDC ACM UART](../usb/P131_旧版CDC_ACM串口回显示例.md) | 使用旧版 USB CDC ACM UART 驱动实现串口回显。 |
| [Native TTY UART](P351_UART原生TTY示例.md) | 使用主机 TTY 驱动，在两个 UART 转 USB 适配器间收发数据。 |
| [单线 UART](https://docs.zephyrproject.org/latest/samples/boards/st/uart/single_wire/README.html) | 使用 STM32 的单线、半双工 UART。 |
| [UART 异步 API](P349_UART异步API示例.md) | 演示异步 API 的使用。 |
| [UART 循环模式](https://docs.zephyrproject.org/latest/samples/boards/st/uart/circular_dma/README.html) | 采用循环 DMA 从控制台读取数据并回显。 |
| [UART 回显](P350_UART回显示例.md) | 读取控制台数据并原样返回。 |
| [UART 直通](P352_UART透传示例.md) | 在控制台与另一个 UART 接口间直接传递数据。 |
| [USB CDC ACM UART](../usb/P054_CDCACM串口示例.md) | 使用 USB CDC ACM UART 驱动实现串口回显。 |
| [USB CDC-ACM 桥](../usb/P056_CDCACM桥接示例.md) | 使用 USB CDC-ACM 驱动实现串口桥。 |

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：通用输入输出GPIO](P005_GPIO.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：时钟控制](P007_时钟控制.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：GPIO](P005_GPIO.md) · [下一章：时钟控制](P007_时钟控制.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
