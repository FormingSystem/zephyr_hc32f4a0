---
id: learning.zephyr-docs.bluetooth-samples.page-19
title: HCI功率控制
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_pwr_ctrl/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_hci_pwr_ctrl"></a>

# 第19章\_HCI功率控制

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_pwr_ctrl/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/hci_pwr_ctrl)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 19.1\_概览（Overview）

本示例通过Zephyr主机控制器接口（Host Controller Interface，HCI）的厂商专用（Vendor-Specific，VS）命令，演示低功耗蓝牙（Bluetooth Low Energy，LE）控制器链路层（Link Layer，LL）的动态发射功率（Tx Power）控制。

应用实现一个广播时改变发射功率的外设（Peripheral）。启动后的前5秒，广播者使用Kconfig设置的默认发射功率。之后功率按阶梯从−4 dBm逐步下降至−30 dBm，每5秒降低一级，并反复循环。

连接成功后，应用监测连接的接收信号强度指示（Received Signal Strength Indicator，RSSI），按每条连接的信号强度调整外设发射功率，以节省能量。外设实现简单的通用属性配置文件（Generic Attribute Profile，GATT），提供心率服务（Heart Rate Service，HRS），每2秒向已连接的中心设备（Central）通知一个模拟心率值。

<a id="requirements"></a>

## 19.2\_要求（Requirements）

- 主机运行BlueZ，或者使用支持Bluetooth LE的开发板。
- 另需中心设备及监视工具，例如nRF Connect，用于检查从外设获得的RSSI值。

<a id="building-and-running"></a>

## 19.3\_构建与运行（Building and Running）

将 `<board>` 替换为目标板后构建并烧录：

```bash
west build -b <board> samples/bluetooth/hci_pwr_ctrl
west flash
```

<a id="see-also"></a>

## 19.4\_另请参阅（See also）

[心率服务（HRS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html)、[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。


对应官方文档源码：[samples/bluetooth/hci_pwr_ctrl/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_pwr_ctrl/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/hci_pwr_ctrl/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P018_HCI异步UART传输.md) · [返回大纲](大纲.md) · [下一章](P020_HCI厂商扫描请求.md)
