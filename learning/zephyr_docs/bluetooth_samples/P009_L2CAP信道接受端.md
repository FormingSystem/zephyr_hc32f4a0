---
id: learning.zephyr-docs.bluetooth-samples.page-9
title: L2CAP信道接受端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/l2cap_coc_acceptor/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_l2cap_coc_acceptor"></a>

# 第9章\_L2CAP信道接受端

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/l2cap_coc_acceptor/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/l2cap_coc_acceptor)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 9.1\_概览（Overview）

本示例创建逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）的面向连接信道（Connection Oriented Channel，CoC）服务器，在动态协议／服务复用值（Protocol/Service Multiplexer，PSM）上监听传入连接。客户端连接时，服务器接受连接并接收通过L2CAP信道发送的数据。

示例采用固定分配策略：根据 `CONFIG_BT_MAX_CONN`，为每个可能的蓝牙连接预先分配一个L2CAP信道实例，避免动态内存分配并简化资源管理。

<a id="requirements"></a>

## 9.2\_要求（Requirements）

支持低功耗蓝牙（Bluetooth Low Energy，BLE）的开发板。

<a id="building-and-running"></a>

## 9.3\_构建与运行（Building and Running）

本示例可以在支持LE的开发板上构建和运行。官方构建及烧录示例使用nRF52840DK：

```bash
west build -b nrf52840dk/nrf52840 samples/bluetooth/l2cap_coc_acceptor
west flash
```

烧录后，设备在PSM `0x29` 注册L2CAP服务器并等待传入连接。与[L2CAP面向连接信道发起端](P010_L2CAP信道发起端.md#bluetooth_l2cap_coc_initiator)搭配，建立连接并交换数据。

发起端自动扫描、连接并建立L2CAP信道；观察两端串口输出，确认连接和数据交换过程。

<a id="sample-output"></a>

### 9.3.1\_示例输出（Sample Output）

初始化成功时：

```text
L2CAP server registered, PSM 41
```

客户端连接时：

```text
L2CAP channel accepted, assigned chan[0]
L2CAP channel connected
```

收到数据时：

```text
L2CAP channel received 17 bytes
```

> 译注——输出对照：`L2CAP server registered, PSM 41`表示服务器已注册，十进制41就是十六进制0x29。`channel accepted, assigned chan[0]`表示已接受信道并分配第0项实例；`channel connected`表示信道连接完成；`received 17 bytes`表示收到17字节。这些为官方预期输出，不是本批实测记录。

<a id="see-also"></a>

## 9.4\_另请参阅（See also）

[L2CAP API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)。


对应官方文档源码：[samples/bluetooth/l2cap_coc_acceptor/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/l2cap_coc_acceptor/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/l2cap_coc_acceptor/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P008_心率中心设备.md) · [返回大纲](大纲.md) · [下一章](P010_L2CAP信道发起端.md)
