---
id: learning.zephyr-docs.bluetooth-samples.page-21
title: Nordic_UART服务外设
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_nus/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_nus"></a>

# 第21章\_Nordic\_UART服务外设

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_nus/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/peripheral_nus)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 21.1\_概览（Overview）

本示例把Nordic串口服务（Nordic UART Service，NUS）用作交换数据的串行端点。这里UART指通用异步收发器（Universal Asynchronous Receiver/Transmitter）；服务承载的数据在本示例中按UTF-8编码理解，也可以是二进制数据。用户连接设备并订阅TX特征（Characteristic）后，会周期性收到带有“Hello World!n”的通知（Notification）；引号中的形式按官方网页显示保留。

> 译注——换行字符：所读取的[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/peripheral_nus/src/main.c)使用字符串 `"Hello World!\n"`，其中 `\n` 表示换行，不是字母n；发送循环每次等待3秒。网页显示与源码字符串有差异，实际数据以所用版本的实现为准。NUS是蓝牙服务，不要求把这段数据直接接到物理UART引脚。

<a id="requirements"></a>

## 21.2\_要求（Requirements）

主机运行BlueZ，或者使用支持低功耗蓝牙（Bluetooth Low Energy，LE）的开发板。

<a id="building-and-running"></a>

## 21.3\_构建与运行（Building and Running）

将 `<board>` 替换为目标板，构建并烧录：

```bash
west build -b <board> samples/bluetooth/peripheral_nus
west flash
```

烧录后，用蓝牙扫描应用，例如nRF Connect，连接设备并订阅NUS TX特征。设备将周期性发送 `Hello World!` 通知。

<a id="see-also"></a>

## 21.4\_另请参阅（See also）

[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。


对应官方文档源码：[samples/bluetooth/peripheral_nus/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/peripheral_nus/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/peripheral_nus/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P020_HCI厂商扫描请求.md) · [返回大纲](大纲.md) · [下一章](P022_外设身份.md)
