---
id: learning.zephyr-docs.usb.usb-vidpid
title: USB厂商与产品标识
kind: reference
status: maintained
domains: [zephyr, usb]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/vid_pid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="usbd-vid-pid"></a>

# 第4章\_USB厂商与产品标识

原文：[USB Vendor and Product identifiers](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/vid_pid.html)。读取日期：2026-10-12，`latest`。

## 4.1\_厂商标识与分配原则

Zephyr 项目的 **通用串行总线（Universal Serial Bus，USB）** **厂商标识符（Vendor ID，VID）**为 `0x2FE3`。厂商将 Zephyr USB 设备支持集成到自己的产品中时，不得使用 Zephyr 的 USB VID。

每个 [USB 示例](P065_USB示例目录.md#usb)都有唯一的**产品标识符（Product ID，PID）**。如已指定 USB 维护者，由维护者分配其他 PID；否则由 Zephyr **技术指导委员会（Technical Steering Committee，TSC）**负责。分配须基于理由充分并形成文档的申请。

## 4.2\_当前使用的产品ID

以下为原文读取时的分配表。

| 示例 | PID |
| --- | --- |
| [USB CDC ACM UART](P054_CDCACM串口示例.md#usb-cdc-acm) | `0x0001` |
| 保留（原用途：`usb-cdc-acm-composite`） | `0x0002` |
| 保留（原用途：`usb-hid-cdc`） | `0x0003` |
| [通过 USB CDC ACM 使用控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console) | `0x0004` |
| [USB DFU（运行时模式）](P064_USB设备固件升级示例.md#usb-dfu) | `0x0005` |
| 保留（原用途：`usb-hid`） | `0x0006` |
| [USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse) | `0x0007` |
| [USB 大容量存储](P060_USB大容量存储示例.md#usb-mass) | `0x0008` |
| [USB 设备测试应用](P067_USB设备测试示例.md#testusb-app) | `0x0009` |
| [WebUSB](P069_WebUSB示例.md#webusb) | `0x000A` |
| [HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb) | `0x000B` |
| 保留（原用途：`bluetooth_hci_usb_h4`） | `0x000C` |
| 保留（原用途：`wpan-usb`） | `0x000D` |
| [USB Audio 异步显式反馈](P091_USB音频显式反馈示例.md#uac2-explicit-feedback) | `0x000E` |
| [USB Audio 异步隐式反馈](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback) | `0x000F` |
| [USB Video 摄像头](P124_USB视频摄像头示例.md#uvc) | `0x0011` |
| [FIDO2 身份验证器](../basic_samples/P057_FIDO2认证器示例.md#fido2) | `0x0012` |
| [I2C-Tiny-USB 桥接](P068_USB转I2C桥接示例.md#i2c-tiny-usb) | `0x0013` |
| [USB DFU（DFU 模式）](P064_USB设备固件升级示例.md#usb-dfu) | `0xFFFF` |

> 译注：保留项仍是保留分配；表中未列出的数值也不能自行认定为可随意使用。**设备固件升级（Device Firmware Upgrade，DFU）** 表示设备固件升级，运行时模式与 DFU 模式在此使用不同 PID。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB_CDC_ACM](P003_USB_CDC_ACM.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB测试与示例约定](P005_USB测试与示例约定.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：USB CDC ACM](P003_USB_CDC_ACM.md) · [下一章：USB测试与示例约定](P005_USB测试与示例约定.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
