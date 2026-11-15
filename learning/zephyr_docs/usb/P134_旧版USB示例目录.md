---
id: learning.zephyr-docs.usb.page-134
title: 旧版USB示例目录
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/legacy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_旧版USB示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/legacy.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

这些示例演示 Zephyr 实时操作系统（Real-Time Operating System，RTOS）中的旧版 USB 设备支持。

> 原文注：这些示例使用正处于弃用过程中的[旧版 USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 134.1\_示例目录

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

> 译注：此目录按原页的十项示例逐项翻译，目录完成不代替各示例正文或相关 API 的完成状态。旧版源码保留用于理解已有应用；迁移时需要分别核对新设备栈与对应功能类的接口。


<a id="legacy-usb-device-support"></a>

[上一章](P133_旧版USB固件升级示例.md) · [返回大纲](大纲.md) · [下一章](P135_旧版USB大容量存储示例.md)
