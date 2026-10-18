---
id: learning.zephyr-docs.hardware.uartsample-1
title: UART异步API示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/uart/async_api/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="uart_async"></a>

# 第349章\_UART异步API示例

原文：[UART ASYNC API](https://docs.zephyrproject.org/latest/samples/drivers/uart/async_api/README.html)。读取日期：2026-10-13，`latest`。

## 349.1\_示例行为

本示例通过简单的数据包发送程序演示通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）串口驱动的异步应用程序编程接口（Asynchronous Application Programming Interface，API）。[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/uart/async_api)位于官方源码树 `samples/drivers/uart/async_api`。

每 5 秒生成 1 到 4 份数据负载（Payload）并排队发送。在交替的 5 秒周期内，通过异步 API 启用接收。默认使用通常分配给 Zephyr 命令行交互器（Shell）的 UART 外设，因此理论上应支持几乎所有开发板。

## 349.2\_构建与运行

原文构建和烧录命令如下，将 `nrf52840dk/nrf52840` 替换为实际开发板目标。

> 执行说明：在已经准备好 Zephyr 开发环境的实验源码根目录执行；终端使用 Linux Bash 或 Windows UCRT64 Bash。示例目录为官方已有内容。`west build` 编译固件，`west flash` 将其烧录到选定开发板；编译失败先处理首个构建错误，不继续烧录。

```sh
west build -b nrf52840dk/nrf52840 samples/drivers/uart/async_api
west flash
```

## 349.3\_官方输出示例

以下为官方预期输出，用来辨认周期、发送包数和接收状态，并非本仓库的实板执行记录。日志中的 `RX` 表示接收（Receive），`RX_RDY` 表示接收数据就绪：

```text
Loop 0: Packet: 0
Loop 0: Packet: 1
Loop 0: Packet: 2
[00:00:05.001,919] <inf> sample: Loop 0: Sending 3 packets
[00:00:05.002,008] <inf> sample: RX is now enabled
Loop 1: Packet: 0
[00:00:10.002,086] <inf> sample: Loop 1: Sending 1 packets
[00:00:10.002,138] <inf> sample: RX is now disabled
Loop 2: Packet: 0
Loop 2: Packet: 1
[00:00:15.002,215] <inf> sample: Loop 2: Sending 2 packets
[00:00:15.002,293] <inf> sample: RX is now enabled
[00:00:15.009,010] <inf> sample: RX_RDY
                              68 65 6c 6c 6f 0a                                |hello.
Loop 3: Packet: 0
Loop 3: Packet: 1
Loop 3: Packet: 2
[00:00:20.002,343] <inf> sample: Loop 3: Sending 3 packets
[00:00:20.002,424] <inf> sample: RX is now disabled
```

UART 发送直接触发，因此串口日志中的实际发送数据会出现在循环开头的 `LOG_INF` 信息日志之前；日志写入通常会延迟数秒。不要仅按显示先后顺序推断代码执行顺序。

相关接口见 [UART 驱动说明](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html#uart-api)。

---

[上一章：UART示例目录](P348_UART示例目录.md) · [下一章：UART回显示例](P350_UART回显示例.md) · [返回大纲](大纲.md)
