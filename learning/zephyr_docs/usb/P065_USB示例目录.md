---
id: learning.zephyr-docs.usb.page-65
title: USB示例目录
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/usb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_USB示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/usb.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 65.1\_USB示例（USB Samples）

这些示例演示Zephyr实时操作系统（Real-Time Operating System，RTOS）的USB支持。

大部分示例位于Zephyr源码树的 [samples/subsys/usb](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb)，另有几类功能的示例位于其他目录：

- 蓝牙主机控制器接口（Host Controller Interface，HCI）的USB传输层实现见 [HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb)。
- USB通信设备类（Communications Device Class，CDC）的以太网控制模型（Ethernet Control Model，ECM）和网络控制模型（Network Control Model，NCM）实现见网络示例 [zperf网络流量生成器](../networking/P097_zperf网络流量生成器示例.md#zperf) 或 [HTTP服务器](../networking/P056_HTTP服务器示例.md#sockets-http-server)。

> 译注：本页仅翻译官方示例目录及简介。已完成的条目链接到本地译文，尚未翻译的条目仍指向官方页面；目录完成不等于下列每个示例均已完成。

## 65.2\_当前USB示例

| 示例 | 原文简介译文 |
| --- | --- |
| [USB CDC ACM控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console) | 通过USB CDC抽象控制模型（Abstract Control Model，ACM）在控制台输出“Hello World!”。 |
| [I2C-Tiny-USB桥接](P068_USB转I2C桥接示例.md#i2c-tiny-usb) | 将Zephyr I²C控制器作为USB转I²C适配器提供给主机。 |
| [USB音频异步显式反馈示例](P091_USB音频显式反馈示例.md#uac2-explicit-feedback) | USB Audio 2显式反馈示例，通过集成电路间音频总线（Inter-IC Sound，I²S）播放音频。 |
| [USB音频异步隐式反馈示例](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback) | USB Audio 2隐式反馈示例，通过I²S接口播放立体声音频并录制单声道音频。 |
| [USB CDC ACM UART示例](P054_CDCACM串口示例.md#usb-cdc-acm) | 使用USB CDC ACM通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）驱动实现串口回显。 |
| [USB CDC-ACM桥接](P056_CDCACM桥接示例.md#usb-cdc-acm-bridge) | 使用USB CDC-ACM驱动实现串口桥接。 |
| [USB设备测试应用](P067_USB设备测试示例.md#testusb-app) | 通过回环（Loopback）功能测试USB设备驱动。 |
| [USB设备固件升级](P064_USB设备固件升级示例.md#usb-dfu) | 实现基本的USB设备固件升级（Device Firmware Upgrade，DFU）设备。 |
| [USB HID键盘](P051_HID键盘示例.md#usb-hid-keyboard) | 实现基本的人机接口设备（Human Interface Device，HID）键盘。 |
| [USB HID鼠标](P052_HID鼠标示例.md#usb-hid-mouse) | 实现基本的HID鼠标设备。 |
| [USB主机UVC摄像头](P125_USB主机摄像头示例.md#usb-host-uvc) | 从USB摄像头采集视频；UVC为USB视频类（USB Video Class）。 |
| [USB大容量存储](P060_USB大容量存储示例.md#usb-mass) | 使用USB大容量存储（Mass Storage）驱动将板上RAM或Flash提供为USB磁盘。 |
| [USB MIDI2设备](P096_USBMIDI2设备示例.md#usb-midi2-device) | 实现简单的USB乐器数字接口（Musical Instrument Digital Interface，MIDI）回环和键盘设备。 |
| [USB命令行](P066_USB命令行示例.md#usb-shell) | 用命令行解释器（Shell）命令与USB设备栈交互。 |
| [USB视频摄像头](P124_USB视频摄像头示例.md#uvc) | 通过USB发送视频帧。 |
| [WebUSB](P069_WebUSB示例.md#webusb) | 使用WebUSB API接收并回显网页发送的数据。 |

## 65.3\_旧版USB设备支持（Legacy USB Device Support）

完整入口见 [旧版USB设备支持](P134_旧版USB示例目录.md)。

| 示例 | 原文简介译文 |
| --- | --- |
| [旧版USB CDC ACM控制台](P132_旧版USB串口控制台示例.md#legacy-usb-cdc-acm-console) | 通过USB CDC ACM在控制台输出“Hello World!”。 |
| [旧版HCI USB](P137_旧版USB蓝牙控制器示例.md#legacy_bluetooth_hci_usb) | 将Zephyr开发板用作兼容所有操作系统的USB蓝牙适配器（Dongle）。 |
| [旧版USB音频耳麦](P138_旧版USB音频耳麦示例.md#usb-audio-headset) | 实现带音频输入／输出回环的USB音频耳麦设备。 |
| [旧版USB音频麦克风与耳机](P139_旧版USB麦克风与耳机示例.md#usb-audio-headphones-microphone) | 实现带音频输入／输出回环的USB麦克风和耳机设备。 |
| [旧版USB CDC ACM UART示例](P131_旧版CDC_ACM串口回显示例.md#legacy-usb-cdc-acm) | 使用USB CDC ACM UART驱动实现串口回显。 |
| [旧版USB网络设备示例](P136_旧版USB网络设备示例.md#legacy-netusb) | 使用USB CDC以太网仿真模型（Ethernet Emulation Model，EEM）／ECM或远程网络驱动接口规范（Remote Network Driver Interface Specification，RNDIS）实现。 |
| [旧版USB设备固件升级](P133_旧版USB固件升级示例.md#legacy-usb-dfu) | 使用USB DFU类驱动实现设备固件升级。 |
| [旧版USB HID鼠标](P053_旧版HID鼠标示例.md#legacy-usb-hid-mouse) | 实现基本的HID鼠标设备。 |
| [旧版USB大容量存储](P135_旧版USB大容量存储示例.md#legacy-usb-mass) | 使用USB大容量存储驱动，将板上RAM作为USB磁盘提供给主机。 |
| [旧版WebUSB](P140_旧版WebUSB示例.md#legacy-webusb) | 使用WebUSB API接收并回显网页发送的数据。 |


<a id="usb"></a>
<a id="usb_legacy"></a>

[上一章](P064_USB设备固件升级示例.md) · [返回大纲](大纲.md) · [下一章](P066_USB命令行示例.md)
