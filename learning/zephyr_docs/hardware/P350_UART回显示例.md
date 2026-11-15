---
id: learning.zephyr-docs.hardware.uartsample-2
title: UART回显示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/uart/echo_bot/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="uart"></a>

# 第350章\_UART回显示例

原文：[UART echo](https://docs.zephyrproject.org/latest/samples/drivers/uart/echo_bot/README.html)。读取日期：2026-10-13，`latest`。

## 350.1\_整行回显

本示例通过简单的回显程序（Echo Bot）展示通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）串口驱动的用法。它从控制台（Console）读取数据，收到行结束符，即按下回车后，再把字符原样发送回来。[官方源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/uart/echo_bot)位于 `samples/drivers/uart/echo_bot`。

发送使用轮询应用程序编程接口（Polling Application Programming Interface，API），接收使用中断驱动（Interrupt-Driven）API，因此线程理论上可以在等待输入时做其他工作。

默认使用通常供 Zephyr 命令行交互器（Shell）使用的 UART 外设，因此应支持几乎所有开发板。

## 350.2\_构建与运行

将原命令中的 `nrf52840dk/nrf52840` 替换为自己的开发板目标：

> 执行说明：已完成主机工具与工具链准备，在实验源码根目录的 Linux Bash 或 Windows UCRT64 Bash 中执行。目录为官方原有示例；先编译成功，再烧录。失败时先修复对应构建或烧录错误，然后重新执行该步骤。

```sh
west build -b nrf52840dk/nrf52840 samples/drivers/uart/echo_bot
west flash
```

## 350.3\_官方输出示例

连接所用 UART 控制台，输入例如 `Hi there!` 并按回车，应看到 `Echo:` 后跟随原输入。原输出保留如下；首行的反斜杠转义按官方网页代码块原样保留，属于示例展示内容：

```text
Hello! I\'m your echo bot.
Tell me something and press enter:
# Type e.g. "Hi there!" and hit enter!
Echo: Hi there!
```

这些是官方示例输出，不代表本次已经烧录验证。相关接口见 [UART 驱动说明](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html#uart-api)。

---

[上一章：UART异步API示例](P349_UART异步API示例.md) · [下一章：UART原生TTY示例](P351_UART原生TTY示例.md) · [返回大纲](大纲.md)
