---
id: learning.zephyr-docs.hardware.hwapi-can-counter
title: CAN计数器示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/can/counter/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="can-counter"></a>

# 第44章\_CAN计数器示例

原文：[Controller Area Network (CAN) counter](https://docs.zephyrproject.org/latest/samples/drivers/can/counter/README.html)。读取日期：2026-10-13，`latest`。

## 44.1\_发送、接收与回环

本示例展示 **控制器局域网（Controller Area Network，CAN）**的 **应用程序编程接口（Application Programming Interface，API）**。它发送使用标准标识符和扩展标识符的消息，通过 **消息队列（Message Queue）**与 **工作队列（Work Queue）**接收消息，并在控制台输出收到的计数值；如果板上有 **发光二极管（Light-Emitting Diode，LED）**，还会通过闪烁指示接收。

在 **回环模式（Loopback Mode）**下，板会收到自己发送的消息，可用于单板测试。LED输出引脚由板的设备树定义。示例既可用于具有集成CAN控制器的 **片上系统（System on Chip，SoC）**，也可用于外接独立CAN控制器的系统。

## 44.2\_使用集成CAN控制器

原文以NXP TWR-KE18F为例。先准备Zephyr环境、板工具链和烧录工具，并连接目标板；在Ubuntu Bash或已准备好的UCRT64 Bash中，从实验Zephyr源码根目录执行。官方示例位于 `samples/drivers/can/counter`，构建产物由工具写入 `build`。

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/drivers/can/counter
west flash
```

第一步成功后再烧录。若板或控制器配置不满足要求，应先检查目标板支持及CAN配置，不能把构建失败当作总线通信故障。

## 44.3\_使用独立CAN控制器

原文另一配置为 `nrf52dk/nrf52832`，搭配提供MCP2515 CAN控制器的DFRobot CAN bus V2.0 **扩展板（Shield）**。环境与执行位置同上一节，但实际硬件连接和烧录目标必须切换到对应组合。

```shell
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 --shield dfrobot_can_bus_v2_0 samples/drivers/can/counter
west flash
```

切换板时应选择独立构建目录或按构建章节清理旧配置；不要沿用另一目标的构建缓存。

## 44.4\_观察过滤器与计数输出

ID是 **标识符（Identifier）**，这里用于显示接收过滤器编号。原文控制台输出如下：

```text
Change LED filter ID: 0
Finished init.
Counter filter id: 4

uart:~$ Counter received: 0
Counter received: 1
Counter received: 2
Counter received: 3
```

输出中的filter ID表示接收 **过滤器标识（Filter Identifier）**，随后显示收到的计数值。原文说明具体值可能不同，因此不能把0和4当作所有平台固定的过滤器编号。`uart:~$` 是串行控制台提示符；UART为 **通用异步收发器（Universal Asynchronous Receiver/Transmitter）**。

本次未执行固件烧录或总线测试；上面保留的是官方输出示例。控制器状态、发送、过滤与接收约束见[CAN控制器](P030_CAN控制器.md)。

[上一章：EEPROM计数示例](P043_EEPROM计数示例.md) · [下一章：CAN持续发送示例](P045_CAN持续发送示例.md) · [返回大纲](大纲.md)
