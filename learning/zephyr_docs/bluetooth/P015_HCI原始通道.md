---
id: learning.zephyr-docs.bluetooth.page-15
title: HCI原始通道
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/hci_raw.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="hci-raw-channel"></a>
<a id="bt-hci-raw"></a>

# 第15章\_HCI原始通道

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/hci_raw.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 15.1\_概览（Overview）

主机控制器接口原始通道（Host Controller Interface RAW channel，HCI RAW channel）用于把HCI接口提供给远端实体。此时本地蓝牙控制器由远端实体控制，不使用本地蓝牙Host协议栈。RAW API可以直接访问蓝牙HCI驱动发送和接收的数据包。

<a id="api-reference"></a>

## 15.2\_API参考（API Reference）

[HCI原始通道API（HCI RAW channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。

## 15.3\_相关代码示例（Related code samples）

| 示例 | 用途 |
| --- | --- |
| [三线HCI（HCI 3-wire，H:5）](../bluetooth_samples/P017_HCI三线传输.md#bluetooth_hci_uart_3wire) | 通过H5 HCI传输向另一设备或CPU提供蓝牙控制器 |
| [HCI IPC](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) | 使用进程间通信（Inter-Process Communication，IPC）子系统向另一设备或CPU提供控制器 |
| [HCI SPI](../bluetooth_samples/P015_HCI_SPI传输.md#bluetooth_hci_spi) | 通过串行外设接口（Serial Peripheral Interface，SPI）向另一设备或CPU提供控制器 |
| [HCI UART](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth_hci_uart) | 通过通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）向另一设备或CPU提供控制器 |
| [异步UART HCI（HCI UART async）](../bluetooth_samples/P018_HCI异步UART传输.md#bluetooth_hci_uart_async) | 通过异步UART向另一设备或CPU提供控制器 |
| [HCI USB](../usb/P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb) | 将Zephyr开发板变为USB蓝牙适配器；原文说明与所有操作系统兼容 |
| [旧版HCI USB（Legacy HCI USB）](../usb/P137_旧版USB蓝牙控制器示例.md#legacy_bluetooth_hci_usb) | 使用旧版USB支持将开发板变为USB蓝牙适配器；原文说明与所有操作系统兼容 |

> 译注：上述是官方示例的用途描述，不构成本次在所有主机系统或本仓库开发板上的兼容性测试结论。RAW模式把控制权交给外部Host，与[一般Host应用接口](P014_HCI数据包辅助接口.md)的使用场景不同。


对应官方文档源码：[doc/services/connectivity/bluetooth/api/hci_raw.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/hci_raw.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/api/hci_raw.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HCI数据包辅助接口](P014_HCI数据包辅助接口.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：L2CAP接口](P016_L2CAP接口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_HCI数据包辅助接口.md) · [返回大纲](大纲.md) · [下一章](P016_L2CAP接口.md)

</details>

<!-- reading-navigation:end -->
