---
id: learning.zephyr-docs.usb.page-14
title: USB设备栈API说明
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/usbd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_USB设备栈API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/usbd.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 14.1\_接口稳定性

USB 设备栈 API 尚不稳定，可能在没有事先通知的情况下发生变化。

## 14.2\_API参考

[USB 设备核心 API](P015_USB设备核心API.md)。

## 14.3\_相关代码示例

| 官方示例 | 用途 |
| --- | --- |
| [USB CDC ACM 控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console) | 通过 USB CDC ACM 向控制台输出“Hello World!”。 |
| [HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb) | 将 Zephyr 开发板作为 USB 蓝牙适配器使用；原页描述为兼容全部操作系统。 |
| [I2C-Tiny-USB 桥接](P068_USB转I2C桥接示例.md#i2c-tiny-usb) | 将 Zephyr I2C 控制器作为 USB 转 I2C 适配器提供给主机。 |
| [MCTP USB 端点节点](P191_MCTPUSB端点示例.md#mctp-usb-endpoint) | 使用 USB 设备接口创建管理组件传输协议（Management Component Transport Protocol，MCTP）端点节点。 |
| [USB 音频异步显式反馈](P091_USB音频显式反馈示例.md#uac2-explicit-feedback) | USB Audio 2 显式反馈示例，通过 I2S 播放音频。 |
| [USB 音频异步隐式反馈](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback) | USB Audio 2 隐式反馈示例，通过 I2S 播放立体声音频并录制单声道音频。 |
| [USB CDC ACM UART 示例](P054_CDCACM串口示例.md#usb-cdc-acm) | 使用 USB CDC ACM UART 驱动实现串口回显。 |
| [USB 设备测试应用](P067_USB设备测试示例.md#testusb-app) | 通过回环功能（Loopback Function）测试 USB 设备驱动。 |
| [USB DFU](P064_USB设备固件升级示例.md#usb-dfu) | 实现一个基础 USB DFU 设备。 |
| [USB HID 键盘](P051_HID键盘示例.md#usb-hid-keyboard) | 实现一个基础 HID 键盘设备。 |
| [USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse) | 实现一个基础 HID 鼠标设备。 |
| [USB 大容量存储](P060_USB大容量存储示例.md#usb-mass) | 使用 USB 大容量存储驱动，将开发板 RAM 或 Flash 暴露为 USB 磁盘。 |
| [USB MIDI2 设备](P096_USBMIDI2设备示例.md#usb-midi2-device) | 实现简单的 USB MIDI 回环和键盘设备。 |
| [USB Shell](P066_USB命令行示例.md#usb-shell) | 使用命令行解释器（Shell）命令与 USB 设备栈交互。 |
| [USB 视频摄像头](P124_USB视频摄像头示例.md#uvc) | 通过 USB 发送视频帧。 |
| [WebUSB](P069_WebUSB示例.md#webusb) | 使用 WebUSB API 接收网页数据并回送。 |

> 译注：CDC ACM 为通信设备类／抽象控制模型（Communications Device Class / Abstract Control Model）；HCI 为主机控制器接口（Host Controller Interface）；UART 为通用异步收发器（Universal Asynchronous Receiver-Transmitter）。I2C 为集成电路间总线（Inter-Integrated Circuit），I2S 为集成电路间音频接口（Inter-IC Sound）。本表保留官方示例范围，不代表本批已运行这些应用或核验所有宿主系统。

## 14.4\_设备消息参考

原页末尾另一个名为“USB device core API”的入口实际指向消息组，译文见[USB设备消息API](P016_USB设备消息API.md)。其中包括设备状态、VBUS、CDC ACM 和 DFU 通知；消息载荷结构另见[USB设备消息结构](P017_USB设备消息结构.md)。这一标题区分为本地译注，原链接指向保持一致。


<a id="usb-device-stack-api"></a>
<a id="usbd-api"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB设备API目录](P013_USB设备API目录.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB设备控制器API说明](P029_USB设备控制器API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_USB设备API目录.md) · [返回大纲](大纲.md) · [下一章](P015_USB设备核心API.md)

</details>

<!-- reading-navigation:end -->
