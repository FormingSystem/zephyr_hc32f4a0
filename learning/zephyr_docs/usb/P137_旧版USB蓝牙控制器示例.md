---
id: learning.zephyr-docs.usb.page-137
title: 旧版USB蓝牙控制器示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/hci_usb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_旧版USB蓝牙控制器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/hci_usb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 137.1\_概述

使用 Zephyr 制作 USB 蓝牙适配器（USB Bluetooth Dongle）。HCI 指主机控制器接口（Host Controller Interface）。

## 137.2\_运行要求

- 主机运行蓝牙协议栈（Bluetooth Stack），例如 BlueZ。
- 开发板在 Zephyr 中同时具备蓝牙与 USB 支持。

## 137.3\_构建与运行

此示例位于 Zephyr 源码树的 [samples/subsys/usb/legacy/hci_usb](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/legacy/hci_usb) 目录。

> 译注：原页只给出源码入口，没有列出具体板名、构建命令或主机测试过程。当前 `prj.conf` 启用 `CONFIG_BT_HCI_RAW` 和 `CONFIG_USB_DEVICE_BLUETOOTH`，并关闭串行接口及控制台，配置注释说明这是为了避免控制台或 CDC ACM 干扰 BlueZ 检测 HCI USB。因此不能把其他 USB 串口示例的控制台配置直接套用到此例，也不能期待通过被关闭的控制台看到全部 `printk` 输出。该示例仍选择旧版 USB 设备栈。

## 137.4\_另见

- [HCI 原始通道（HCI RAW Channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。
- [蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。
- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/hci_usb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/hci_usb/src/main.c)、[samples/subsys/usb/legacy/hci_usb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/hci_usb/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/hci_usb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy_bluetooth_hci_usb"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P136_旧版USB网络设备示例.md) · [返回大纲](大纲.md) · [下一章](P138_旧版USB音频耳麦示例.md)
