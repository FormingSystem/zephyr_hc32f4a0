---
id: learning.zephyr-docs.hardware.uartsample-3
title: UART原生TTY示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/uart/native_tty/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="uart-native-tty"></a>

# 第351章\_UART原生TTY示例

原文：[Native TTY UART](https://docs.zephyrproject.org/latest/samples/drivers/uart/native_tty/README.html)。读取日期：2026-10-13，`latest`。

## 351.1\_主机串口桥接实验

本示例演示原生终端设备（Native TTY）UART 驱动。TTY 名称来自 Teletype；通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）通过两个转通用串行总线（Universal Serial Bus，USB）的桥接适配器与主机相连。两个适配器彼此接线，程序向其中一个写入演示数据，再从另一个读取。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/uart/native_tty)位于 `samples/drivers/uart/native_tty`。驱动的深入说明见 [native_sim 的 TTY UART 小节](../native_reference/P004_Native_Simulator本机模拟器.md#native-tty-uart)；[`native_sim`](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 是在主机运行 Zephyr 程序的原生模拟目标名称。

## 351.2\_硬件与设备树要求

需要两个 UART 转 USB 桥接适配器。每个适配器的发送（Transmit，TX）引脚连接另一个适配器的接收（Receive，RX）引脚；两个适配器都必须插入同一台主机。原文说明该接线场景不需要额外接地线。

> 译注：上述接地表述仅对应原示例的主机连接场景，不是不同供电或隔离串口之间可省略参考地的普遍规则。

示例随附的设备树覆盖文件（Devicetree Overlay）预期设备分别出现在 `/dev/ttyUSB0` 和 `/dev/ttyUSB1`。在 Linux 主机终端执行 `ls -l /dev/tty*`，检查实际串口设备名；这些是系统设备节点名称，不是文档的本机文件链接。

若实际名称不同，可修改示例内 `boards/native_sim.overlay` 的 `serial-port` 属性，或者通过命令行选项 `-uart_port`、`-uart_port2` 指定。

## 351.3\_构建并在主机运行

原文使用 `native_sim` 构建和执行：

> 执行说明：使用具备该目标构建环境的 Linux Bash，在实验源码根目录执行。先确认两个设备名与接线对应；编译成功后运行。设备打不开时先回查上一节设备名和访问权限，编译失败则先解决构建错误。本步骤在主机运行程序，无固件烧录命令。

```sh
west build -b native_sim samples/drivers/uart/native_tty
west build -t run
```

## 351.4\_官方输出示例

原输出先显示串口连接，再展示两轮从 9 到 0 的数据收发；第二轮前把两个 UART 的波特率（Baud Rate）都改为 9600。伪终端（Pseudo Terminal）名称和版本号是原例的运行结果，实际系统可能不同：

```text
uart_1 connected to pseudotty: /dev/pts/6
uart2 connected to the serial port: /dev/ttyUSB1
uart connected to the serial port: /dev/ttyUSB0
*** Booting Zephyr OS build v3.4.0-rc2-97-ge586d02c137d ***
Device uart sent: "Hello from device uart, num 9"
Device uart2 received: "Hello from device uart, num 9"
Device uart sent: "Hello from device uart, num 8"
Device uart2 received: "Hello from device uart, num 8"
Device uart sent: "Hello from device uart, num 7"
Device uart2 received: "Hello from device uart, num 7"
Device uart sent: "Hello from device uart, num 6"
Device uart2 received: "Hello from device uart, num 6"
Device uart sent: "Hello from device uart, num 5"
Device uart2 received: "Hello from device uart, num 5"
Device uart sent: "Hello from device uart, num 4"
Device uart2 received: "Hello from device uart, num 4"
Device uart sent: "Hello from device uart, num 3"
Device uart2 received: "Hello from device uart, num 3"
Device uart sent: "Hello from device uart, num 2"
Device uart2 received: "Hello from device uart, num 2"
Device uart sent: "Hello from device uart, num 1"
Device uart2 received: "Hello from device uart, num 1"
Device uart sent: "Hello from device uart, num 0"
Device uart2 received: "Hello from device uart, num 0"

Changing baudrate of both uart devices to 9600!

Device uart sent: "Hello from device uart, num 9"
Device uart2 received: "Hello from device uart, num 9"
Device uart sent: "Hello from device uart, num 8"
Device uart2 received: "Hello from device uart, num 8"
Device uart sent: "Hello from device uart, num 7"
Device uart2 received: "Hello from device uart, num 7"
Device uart sent: "Hello from device uart, num 6"
Device uart2 received: "Hello from device uart, num 6"
Device uart sent: "Hello from device uart, num 5"
Device uart2 received: "Hello from device uart, num 5"
Device uart sent: "Hello from device uart, num 4"
Device uart2 received: "Hello from device uart, num 4"
Device uart sent: "Hello from device uart, num 3"
Device uart2 received: "Hello from device uart, num 3"
Device uart sent: "Hello from device uart, num 2"
Device uart2 received: "Hello from device uart, num 2"
Device uart sent: "Hello from device uart, num 1"
Device uart2 received: "Hello from device uart, num 1"
Device uart sent: "Hello from device uart, num 0"
Device uart2 received: "Hello from device uart, num 0"
```

原例中的 `uart` 为发送设备，`uart2` 打印对应接收内容；这些输出并非本次执行结果。相关接口见 [UART 驱动说明](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html#uart-api)。

---

[上一章：UART回显示例](P350_UART回显示例.md) · [下一章：UART透传示例](P352_UART透传示例.md) · [返回大纲](大纲.md)
