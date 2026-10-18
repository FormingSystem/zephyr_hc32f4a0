---
id: learning.zephyr-docs.bluetooth-samples.page-10
title: L2CAP信道发起端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/l2cap_coc_initiator/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_l2cap_coc_initiator"></a>

# 第10章\_L2CAP信道发起端

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/l2cap_coc_initiator/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/l2cap_coc_initiator)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 10.1\_概览（Overview）

本示例创建逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）的面向连接信道（Connection Oriented Channel，CoC）客户端，扫描蓝牙设备、连接其中一个，并建立与服务器通信的L2CAP信道。

示例周期性发送简短文本，演示基本数据传输。

<a id="requirements"></a>

## 10.2\_要求（Requirements）

- 支持低功耗蓝牙（Bluetooth Low Energy，BLE）的开发板。
- 运行L2CAP服务器的对端设备，例如运行[L2CAP面向连接信道接受端](P009_L2CAP信道接受端.md#bluetooth_l2cap_coc_acceptor)示例的设备。

<a id="building-and-running"></a>

## 10.3\_构建与运行（Building and Running）

本示例可以在支持LE的开发板上构建和运行。官方命令使用nRF52840DK：

```bash
west build -b nrf52840dk/nrf52840 samples/bluetooth/l2cap_coc_initiator
west flash
```

烧录后，设备扫描附近蓝牙设备，连接找到的第一个，并尝试在协议／服务复用值（Protocol/Service Multiplexer，PSM）`0x29`上建立L2CAP信道。

在另一设备运行[接受端示例](P009_L2CAP信道接受端.md#bluetooth_l2cap_coc_acceptor)。发起端自动扫描、连接并建立信道；观察两端串口，了解连接和数据交换过程。

<a id="sample-output"></a>

### 10.3.1\_示例输出（Sample Output）

连接与信道建立成功时：

```text
Scanning...
Found device: XX:XX:XX:XX:XX:XX (RSSI -45)
Connecting to XX:XX:XX:XX:XX:XX ...
Connected
L2CAP channel connection initiated
L2CAP channel connected
Sent: Hello from client
```

之后周期性发送 `Hello from client`（来自客户端的问候）。

> 译注——输出对照：Scanning为正在扫描；Found device为发现设备，RSSI为接收信号强度指示（Received Signal Strength Indicator）；Connecting为正在连接，Connected为连接完成；channel connection initiated为已发起信道连接，channel connected为信道已连接，Sent为已发送。`XX:XX:XX:XX:XX:XX`是原文地址占位符，不是实际目标设备地址。

<a id="see-also"></a>

## 10.4\_另请参阅（See also）

[L2CAP API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)。


对应官方文档源码：[samples/bluetooth/l2cap_coc_initiator/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/l2cap_coc_initiator/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/l2cap_coc_initiator/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P009_L2CAP信道接受端.md) · [返回大纲](大纲.md) · [下一章](P011_MTU更新.md)
