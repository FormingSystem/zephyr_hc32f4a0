---
id: learning.zephyr-docs.usb.page-131
title: 旧版CDC_ACM串口回显示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/cdc_acm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_旧版CDC_ACM串口回显示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/cdc_acm/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 131.1\_概述

此应用演示 Zephyr 提供的 USB 通信设备类（Communication Device Class，CDC）抽象控制模型（Abstract Control Model，ACM）驱动。通过此驱动提供的串口收到的数据，会回显到同一个串口。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 131.2\_运行要求

此项目需要 USB 设备驱动；Zephyr 支持的多种开发板具有这类驱动。

## 131.3\_构建与运行

### 131.3.1\_Reel Board

要查看应用的控制台输出，打开串口终端模拟器，并连接 USB 转 TTL 串口线提供的端口。然后构建并烧录项目：

```shell
west build -b reel_board samples/subsys/usb/legacy/cdc_acm
west flash
```

> 译注：以上是官方 `reel_board` 示例，命令相对 Zephyr 源码根目录执行，需要已准备该板的工具链、模块及烧录器。USB 转 TTL 的日志串口与下面由开发板枚举出的 CDC ACM 回显串口是两个用途不同的端口。

### 131.3.2\_运行

把开发板连接到主机，例如运行 Linux 的 PC。Linux 的 `dmesg` 命令会显示类似的设备检测结果：

```text
usb 9-1: new full-speed USB device number 112 using uhci_hcd
usb 9-1: New USB device found, idVendor=8086, idProduct=f8a1
usb 9-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 9-1: Product: CDC-ACM
usb 9-1: Manufacturer: Intel
usb 9-1: SerialNumber: 00.01
cdc_acm 9-1:1.0: ttyACM1: USB ACM device
```

应用会在作为控制台的串行输出（UART1）上打印：

```text
Wait for DTR
```

打开串口终端模拟器，例如 minicom，并连接检测到的 CDC ACM 设备：

```shell
minicom --device /dev/ttyACM1
```

应用应在日志串口上输出：

```text
DTR set, start test
Baudrate detected: 115200
```

Zephyr USB 设备栈提供的 ttyACM 设备上应输出：

```text
Send characters to the UART device
Characters read:
```

在串口终端模拟器中输入的字符会被回显。

> 译注：数据终端就绪（Data Terminal Ready，DTR）由主机侧设置。当前示例源码在 `usb_enable(NULL)` 后轮询 DTR，随后注册 UART 中断回调，通过环形缓冲区（Ring Buffer）转发收发数据。源码当前日志为 `DTR set` 和 `Baudrate %u`，不再包含原网页的全部提示文字；上方原日志完整保留供对照。`/dev/ttyACM1` 是 Linux 设备节点示例，应采用主机实际枚举的编号，并非固定仓库路径。

## 131.4\_故障排查

如果操作系统运行了 ModemManager，它会尝试访问 CDC ACM 设备，因此连接该设备的终端可能出现包含“AT”的若干字符。可以新增或扩展开发板的 udev 规则，通知 ModemManager 跳过此 CDC ACM 设备。本例规则如下：

```text
ATTRS{idVendor}=="8086" ATTRS{idProduct}=="f8a1", ENV{ID_MM_DEVICE_IGNORE}="1"
```

可以参考 `/lib/udev/rules.d/77-mm-usb-device-blacklist.rules`。

> 译注：这是原页的规则及系统规则文件位置；匹配条件中的厂商标识（Vendor ID，VID）和产品标识（Product ID，PID）须与实际设备一致。保留系统路径用于理解原例，不要求读者把仓库放在该目录。

## 131.5\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。
- [UART API](../hardware/P330_UART公共接口.md)。


译注核对来源：[samples/subsys/usb/legacy/cdc_acm/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/cdc_acm/src/main.c)、[samples/subsys/usb/legacy/cdc_acm/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/cdc_acm/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/cdc_acm/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-usb-cdc-acm"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="reel-board"></a>
<a id="running"></a>
<a id="troubleshooting"></a>
<a id="see-also"></a>

[上一章](P130_旧版USB设备BOS描述符API.md) · [返回大纲](大纲.md) · [下一章](P132_旧版USB串口控制台示例.md)
