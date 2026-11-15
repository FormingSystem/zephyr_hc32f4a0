---
id: learning.zephyr-docs.usb.page-56
title: CDCACM桥接示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/cdc_acm_bridge/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_CDCACM桥接示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/cdc_acm_bridge/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 56.1\_概述

本示例使用 USB CDC ACM，将受支持开发板上的标准硬件 UART 桥接（Bridge）到USB主机。CDC ACM为通信设备类（Communication Device Class）的抽象控制模型（Abstract Control Model）。

## 56.2\_要求

需要 USB 设备驱动；Zephyr 支持的多种开发板提供此驱动。

开发板必须同时具有 USB 接口和硬件 UART。硬件 UART 的设备节点取决于开发板，因此原文要求每块受支持开发板提供明确的设备树覆盖文件（Devicetree Overlay）。

> 译注（源码核对）：当前示例已随附通用 app.overlay，其中 zephyr,uart-bridge 节点的 peers 指向 cdc_acm_uart0 与 arduino_serial，并启用后者。是否还需要板专用覆盖取决于板级是否提供正确的 arduino_serial 节点及引脚配置；不能仅凭USB驱动可用就认为硬件UART也已选好。

## 56.3\_构建与运行

### 56.3.1\_Reel Board

原文要求：要查看应用控制台输出，打开串口终端并连接 USB 转晶体管-晶体管逻辑（Transistor-Transistor Logic，TTL）电平的串口线，再构建并烧录：

> 译注（配置对照）：当前 prj.conf 设置 CONFIG_UART_CONSOLE=n，硬件UART用于桥接，不能照旧文字假定它仍提供调试控制台。若需要日志，应结合实际启用的日志后端查看；不要将桥接数据与调试日志混在同一端口判断。

> 译注：下列官方命令在已准备依赖和工具链的 Zephyr 源码根目录、Bash中执行。烧录前确认构建成功及目标连接；若节点或引脚配置错误，先返回设备树检查。

```bash
west build -b reel_board samples/subsys/usb/cdc_acm_bridge
west flash
```

### 56.3.2\_运行

将开发板接入主机，例如运行 Linux 的 PC。开发板应枚举为 CDC ACM 设备，CDC ACM 的输入和输出与真实 UART 之间双向转发；修改CDC ACM串口配置，例如波特率，也会传播到硬件端口。

如果硬件端口连接到板载调试器，数据应在两个端口之间传递。如果端口引出到开发板引脚，可以把相关引脚短接，以验证驱动是否工作。

> 译注：这里的短接指已确认引脚和电平的同一UART TX与RX回环（Loopback），不包括电源、地或任意排针。先依据板级引脚配置确定端口，再比较USB端发送和接收的数据；本批没有实际接线或执行硬件实验。

> 译注（源码核对）：数据转发由通用 uart_bridge 驱动完成。示例在收到CDC ACM线路编码或控制线状态变化消息后，对桥接节点调用 uart_bridge_settings_update()；驱动读取一端配置并尝试设置另一端，再传播数据终端就绪（Data Terminal Ready，DTR）和请求发送（Request To Send，RTS）控制线状态。硬件驱动不支持对应配置时会失败或跳过不支持的控制线，因此“传播”不保证所有UART都能接受任意波特率、校验或流控组合。

## 56.4\_参阅

- [UART API](../hardware/P330_UART公共接口.md)。


译注核对来源：[samples/subsys/usb/cdc_acm_bridge/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm_bridge/src/main.c)、[samples/subsys/usb/cdc_acm_bridge/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm_bridge/prj.conf)、[samples/subsys/usb/cdc_acm_bridge/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm_bridge/app.overlay)、[samples/subsys/usb/cdc_acm_bridge/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm_bridge/CMakeLists.txt)、[drivers/serial/uart_bridge.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/serial/uart_bridge.c)。

本仓库的[对应源码](../../../samples/subsys/usb/cdc_acm_bridge/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-cdc-acm-bridge"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="reel-board"></a>
<a id="running"></a>
<a id="see-also"></a>

[上一章](P055_CDCACM控制台示例.md) · [返回大纲](大纲.md) · [下一章](P057_USB大容量存储API说明.md)
