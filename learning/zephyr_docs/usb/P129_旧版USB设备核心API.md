---
id: learning.zephyr-docs.usb.page-129
title: 旧版USB设备核心API
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_旧版USB设备核心API

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_device.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 129.1\_API 参考

数据传输有两种方式：使用低层读写 API（Low Level Read/Write API），或使用高层传输 API（High Level Transfer API）。

### 129.1.1\_低层 API

类驱动（Class Driver）向主机发送数据时应调用 `usb_write()`。传输完成后，系统会调用已注册的端点回调（Endpoint Callback）。发送下一个数据包之前，类驱动应等待前一次写入完成。

收到数据时，系统同样调用已注册的端点回调；应用应使用 `usb_read()` 取出收到的数据。对于 CDC ACM 示例驱动，这一过程由端点数组 `cdc_acm_ep_data` 中指定的批量 OUT 端点处理函数 `cdc_acm_bulk_out` 完成。CDC ACM 是通信设备类（Communication Device Class，CDC）的抽象控制模型（Abstract Control Model，ACM）。

### 129.1.2\_高层 API

可以使用 `usb_transfer` 方法在设备与主机之间传输数据。传输 API 根据端点最大包大小（Maximum Packet Size）自动把数据拆分为一个或多个 USB 事务（USB Transaction）。类驱动无需自行实现端点回调，应将该回调设置为通用的 `usb_transfer_ep_callback`。

- [USB 设备核心 API（USB Device Core API）](P155_旧版USB设备栈核心API.md)。

> 译注：这里的高层／低层是旧版设备栈内部的两种传输接口，不是新旧两套设备栈。调用返回与数据传输完成需要区分；等待写入完成的要求对应端点完成回调，不能仅凭 `usb_write()` 返回就认定数据已全部送达主机应用。

## 129.2\_相关代码示例

| 官方示例 | 功能 |
| --- | --- |
| [旧版 USB CDC ACM 控制台](P132_旧版USB串口控制台示例.md#legacy-usb-cdc-acm-console) | 经 USB CDC ACM 向控制台输出“Hello World!”。 |
| [旧版 HCI USB](P137_旧版USB蓝牙控制器示例.md#legacy_bluetooth_hci_usb) | 把 Zephyr 开发板变为 USB 蓝牙适配器；原文说明其兼容所有操作系统。HCI 为主机控制器接口（Host Controller Interface）。 |
| [旧版 USB 音频耳机](P138_旧版USB音频耳麦示例.md#usb-audio-headset) | 实现 USB 音频耳机设备，并对音频 IN／OUT 进行环回。 |
| [旧版 USB 音频麦克风与耳机](P139_旧版USB麦克风与耳机示例.md#usb-audio-headphones-microphone) | 实现 USB 音频麦克风加耳机设备，并对音频 IN／OUT 进行环回。 |
| [旧版 USB CDC ACM UART 示例](P131_旧版CDC_ACM串口回显示例.md#legacy-usb-cdc-acm) | 使用 USB CDC ACM 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）驱动实现串口回显。 |
| [旧版 USB 网络设备示例](P136_旧版USB网络设备示例.md#legacy-netusb) | 使用 CDC 以太网仿真模型（Ethernet Emulation Model，EEM）、以太网控制模型（Ethernet Control Model，ECM）或远程网络驱动接口规范（Remote Network Driver Interface Specification，RNDIS）实现。 |
| [旧版 USB 设备固件升级](P133_旧版USB固件升级示例.md#legacy-usb-dfu) | 使用 USB 设备固件升级（Device Firmware Upgrade，DFU）类驱动更新固件。 |
| [旧版 USB HID 鼠标](P053_旧版HID鼠标示例.md#legacy-usb-hid-mouse) | 实现基本的人机接口设备（Human Interface Device，HID）鼠标。 |
| [旧版 USB 大容量存储](P135_旧版USB大容量存储示例.md#legacy-usb-mass) | 使用 USB 大容量存储（Mass Storage）驱动，把开发板 RAM 呈现为 USB 磁盘。 |
| [旧版 WebUSB](P140_旧版WebUSB示例.md#legacy-webusb) | 使用 WebUSB API 接收网页数据并回显。 |


译注核对来源：[include/zephyr/usb/usb_device.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[subsys/usb/device/usb_transfer.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)。

本仓库的[对应源码](../../../include/zephyr/usb/usb_device.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-device-stack-api-deprecated"></a>
<a id="usb-device-stack-api"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：旧版USB设备控制器API](P128_旧版USB设备控制器API.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：旧版USB设备BOS描述符API](P130_旧版USB设备BOS描述符API.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P128_旧版USB设备控制器API.md) · [返回大纲](大纲.md) · [下一章](P130_旧版USB设备BOS描述符API.md)

</details>

<!-- reading-navigation:end -->
