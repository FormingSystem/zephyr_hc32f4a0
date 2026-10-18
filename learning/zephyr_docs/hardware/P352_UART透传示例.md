---
id: learning.zephyr-docs.hardware.uartsample-4
title: UART透传示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/uart/passthrough/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="uart-passthrough"></a>

# 第352章\_UART透传示例

原文：[UART Passthrough](https://docs.zephyrproject.org/latest/samples/drivers/uart/passthrough/README.html)。读取日期：2026-10-13，`latest`。

## 352.1\_双向转发

本示例将两个通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）接口在软件中连通，效果仿佛没有 Zephyr 和处理器居中。控制台（Console）读到的数据发送到“另一”接口，另一接口读到的数据则转发到控制台，这称为透传（Passthrough）。

[官方源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/uart/passthrough)位于 `samples/drivers/uart/passthrough`。

## 352.2\_硬件要求

需要一个用作 Zephyr 控制台的 UART，以及连接到另一个设备的第二个 UART，例如全球定位系统（Global Positioning System，GPS）接收器。第二个 UART 由设备树的已选设备（Chosen Device）项 `uart,passthrough` 指定；必须正确配置其引脚及波特率（Baud Rate）。

## 352.3\_构建与烧录

原文命令如下，将 `nucleo_l476rg` 替换为实际开发板：

> 执行说明：在已准备好 Zephyr 开发环境的实验源码根目录，使用 Linux Bash 或 Windows UCRT64 Bash。先按上一节配置第二个 UART，编译成功后再烧录。失败时先修复对应配置、构建或烧录错误，再重做该步骤。

```sh
west build -b nucleo_l476rg samples/drivers/uart/passthrough
west flash
```

## 352.4\_官方输出示例

原输出显示控制台与另一接口的设备对象地址，随后显示被转发的 GPS 数据：

```text
*** Booting Zephyr OS build zephyr-v3.5.0-2988-gb84bab36b941 ***
Console Device: 0x8003940
Other Device:   0x800392c
$GNGSA,A,3,31,29,25,26,,,,,,,,,11.15,10.66,3.29,1*06
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,2*0F
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,3*0E
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,4*09
$GNGSA,A,3,,,,,,,,,,,,,11.15,10.66,3.29,5*08
```

版本、对象地址和接收内容均取自官方原例，不是本次实板验证结果。相关接口见 [UART 驱动说明](https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html#uart-api)。

---

[上一章：UART原生TTY示例](P351_UART原生TTY示例.md) · [下一章：UARTAltera扩展](P353_UARTAltera扩展.md) · [返回大纲](大纲.md)
