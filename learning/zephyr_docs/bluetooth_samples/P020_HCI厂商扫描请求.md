---
id: learning.zephyr-docs.bluetooth-samples.page-20
title: HCI厂商扫描请求
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_vs_scan_req/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_hci_vs_scan_req"></a>

# 第20章\_HCI厂商扫描请求

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_vs_scan_req/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/hci_vs_scan_req)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 20.1\_概览（Overview）

本应用演示如何使用主机控制器接口（Host Controller Interface，HCI）的厂商专用（Vendor-Specific，VS）命令：即使使用传统广播（Legacy Advertising），也能取得扫描请求（Scan Request）事件。与采用扩展广播（Extended Advertising）相比，这种方式可能占用更少的随机存取存储器（Random Access Memory，RAM）。

当应用在中心设备（Central）角色之外再增加广播者（Broadcaster）角色时，这一点尤其重要，因为可能节省更多RAM。本示例只实现广播者角色；根据配置选择，也可以增加支持连接的外设（Peripheral）角色。

<a id="requirements"></a>

## 20.2\_要求（Requirements）

- 支持低功耗蓝牙（Bluetooth Low Energy，LE）的开发板，并运行Zephyr内置LE控制器。示例依赖Zephyr专用HCI厂商扩展，**不支持外部HCI控制器**。
- 中心设备及监视工具，例如nRF Connect，用于检查广播并发送扫描请求。

<a id="building-and-running"></a>

## 20.3\_构建与运行（Building and Running）

将 `<board>` 替换为目标板，构建并烧录：

```bash
west build -b <board> samples/bluetooth/hci_vs_scan_req
west flash
```

烧录后，示例开始广播。使用启用主动扫描（Active Scanning）的LE中心设备，例如运行nRF Connect的手机，扫描该设备并触发扫描请求；在控制台输出中观察扫描请求事件。

<a id="see-also"></a>

## 20.4\_另请参阅（See also）

[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。


对应官方文档源码：[samples/bluetooth/hci_vs_scan_req/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_vs_scan_req/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/hci_vs_scan_req/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P019_HCI功率控制.md) · [返回大纲](大纲.md) · [下一章](P021_Nordic_UART服务外设.md)
