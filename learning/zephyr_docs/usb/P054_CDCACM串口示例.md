---
id: learning.zephyr-docs.usb.page-54
title: CDCACM串口示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/cdc_acm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_CDCACM串口示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/cdc_acm/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 54.1\_概述

本示例演示 Zephyr 的 USB 通信设备类（Communication Device Class，CDC）抽象控制模型（Abstract Control Model，ACM）驱动。该驱动提供串口；从串口收到的数据会回显（Echo）到同一端口。

## 54.2\_要求

需要 USB 设备驱动；Zephyr 支持的多种开发板提供此驱动。

## 54.3\_构建与运行

### 54.3.1\_Reel Board

要查看应用控制台输出，打开串口终端并连接 USB 转晶体管-晶体管逻辑（Transistor-Transistor Logic，TTL）电平的串口线。随后构建并烧录：

> 译注：下列构建命令在已准备依赖与工具链的 Zephyr 源码根目录、Bash中执行，烧录前须确认构建成功及目标板连接。这里的USB转TTL调试串口与待测CDC ACM端口承担不同用途，不能把两个端口当成同一个。控制台具体落在哪个UART由板级配置决定，原文下称UART1并不是所有板的固定外设编号。

```bash
west build -b reel_board samples/subsys/usb/cdc_acm
west flash
```

### 54.3.2\_运行

将开发板接入主机，例如运行 Linux 的 PC。Linux 的 `dmesg` 可显示如下枚举信息：

```text
usb 9-1: new full-speed USB device number 112 using uhci_hcd
usb 9-1: New USB device found, idVendor=8086, idProduct=f8a1
usb 9-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 9-1: Product: CDC-ACM
usb 9-1: Manufacturer: Intel
usb 9-1: SerialNumber: 00.01
cdc_acm 9-1:1.0: ttyACM1: USB ACM device
```

> 译注（版本对照）：这是原页保留的历史枚举日志。当前示例 prj.conf 设置 PID 为0x0001、产品字符串为 USBD CDC ACM sample；公共示例配置默认 VID 为0x2fe3、厂商字符串为 Zephyr Project。实际值以最终构建配置和主机枚举结果为准，不应要求它与上方 Intel／8086:f8a1 日志逐字一致。

应用会在用作控制台的串行输出（原文称 UART1）打印：

```text
Wait for DTR
```

打开串口终端，例如 `minicom`，连接检测到的 CDC ACM 设备：

> 译注：下面命令在Linux主机执行；`/dev/ttyACM1` 是原文设备节点示例，应替换成这次枚举的节点。终端需使数据终端就绪信号（Data Terminal Ready，DTR）置位，否则示例继续等待。

```bash
minicom --device /dev/ttyACM1
```

原文给出的串口控制台响应是：

```text
DTR set, start test
Baudrate detected: 115200
```

在 Zephyr USB 设备栈提供的 `ttyACM` 端口上，原文给出以下提示：

```text
Send characters to the UART device
Characters read:
```

在串口终端输入的字符将回显。

> 译注（源码核对）：当前 main.c 的启动日志是 Wait for DTR、DTR set，波特率日志为 Baudrate 后接数值；它没有发送上面的 Send characters／Characters read 提示。当前实现通过CDC ACM控制线状态消息释放DTR信号量，再启用UART接收中断；收到的数据经环形缓冲区（Ring Buffer）返回同一CDC ACM端口。判断运行是否正常应观察实际回显，不把旧提示缺失当作失败。

## 54.4\_故障排查

如果主机运行 ModemManager，它可能尝试访问 CDC ACM 设备，连接该端口的终端可能出现包含“AT”的字符。可新增或扩展开发板的 udev 规则，通知 ModemManager 跳过此设备。原文示例为：

```text
ATTRS{idVendor}=="8086" ATTRS{idProduct}=="f8a1", ENV{ID_MM_DEVICE_IGNORE}="1"
```

> 译注：规则中的VID/PID必须匹配当前真实设备，不能照抄历史日志中的值；规则是Linux主机的配置内容，不是直接输入终端的命令。原示例在两个 ATTRS 匹配项之间缺少逗号，实际规则应按[udev官方手册源码](https://raw.githubusercontent.com/systemd/systemd/main/man/udev.xml)的逗号分隔语法书写。本批仅保留原文并说明问题，没有写入主机规则或更改服务。

## 54.5\_参阅

- [USB设备核心API](P015_USB设备核心API.md)。
- [通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）API](../hardware/P330_UART公共接口.md)。


译注核对来源：[samples/subsys/usb/cdc_acm/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm/src/main.c)、[samples/subsys/usb/cdc_acm/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm/prj.conf)、[samples/subsys/usb/cdc_acm/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm/app.overlay)、[samples/subsys/usb/cdc_acm/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm/CMakeLists.txt)、[samples/subsys/usb/common/Kconfig.sample_usbd](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/common/Kconfig.sample_usbd)、[samples/subsys/usb/common/sample_usbd_init.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/common/sample_usbd_init.c)。

本仓库的[对应源码](../../../samples/subsys/usb/cdc_acm/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-cdc-acm"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="reel-board"></a>
<a id="running"></a>
<a id="troubleshooting"></a>
<a id="see-also"></a>

[上一章](P053_旧版HID鼠标示例.md) · [返回大纲](大纲.md) · [下一章](P055_CDCACM控制台示例.md)
