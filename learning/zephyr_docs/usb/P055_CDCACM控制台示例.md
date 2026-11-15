---
id: learning.zephyr-docs.usb.page-55
title: CDCACM控制台示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_CDCACM控制台示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/console/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 55.1\_概述

本示例将新版实验性 USB 设备栈提供的 CDC ACM UART 用作控制台的串行后端（Serial Backend）。CDC ACM 即通信设备类（Communication Device Class）的抽象控制模型（Abstract Control Model）。

## 55.2\_要求

需要支持 UDC API 的实验性 USB 设备驱动。

## 55.3\_构建与运行

此示例可为多种开发板构建，原文以 `reel_board` 为例：

> 译注：在已准备工具链和依赖的 Zephyr 源码根目录、Bash中执行。确认构建成功和目标板连接后再烧录；构建失败时先检查UDC及CDC ACM支持。原命令中的开发板不是其他板型的占位别名。

```bash
west build -b reel_board samples/subsys/usb/console
west flash
```

将开发板接入主机，例如运行 Linux 的 PC。开发板会枚举为 CDC ACM 串口设备。要查看示例控制台输出，可使用类似 `minicom -D /dev/ttyACM1` 的命令：

```text
Hello World! arm
Hello World! arm
Hello World! arm
Hello World! arm
```

> 译注（源码核对）：app.overlay 将 chosen 中的 zephyr,console 指向CDC ACM节点；prj.conf 启用 CDC_ACM_SERIAL_INITIALIZE_AT_BOOT。main.c 每100毫秒检查一次DTR，主机打开端口并置位后，才每秒打印一次 Hello World! 与 CONFIG_ARCH。上面的 arm 是原例目标架构，实际设备节点编号和架构文本可不同。若一直没有输出，先检查主机是否连接了正确端口及DTR状态。

> 译注：本页把控制台输出送到USB串口；[CDC ACM串口示例](P054_CDCACM串口示例.md)则在CDC ACM端口回显数据，并使用单独的调试控制台说明状态。二者的端口用途不同。

## 55.4\_参阅

- [USB设备核心API](P015_USB设备核心API.md)。
- [UART API](../hardware/P330_UART公共接口.md)。


译注核对来源：[samples/subsys/usb/console/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/console/src/main.c)、[samples/subsys/usb/console/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/console/prj.conf)、[samples/subsys/usb/console/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/console/app.overlay)、[samples/subsys/usb/console/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/console/CMakeLists.txt)。

本仓库的[对应源码](../../../samples/subsys/usb/console/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-cdc-acm-console"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P054_CDCACM串口示例.md) · [返回大纲](大纲.md) · [下一章](P056_CDCACM桥接示例.md)
