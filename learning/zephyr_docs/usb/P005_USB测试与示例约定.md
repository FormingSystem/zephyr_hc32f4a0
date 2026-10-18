---
id: learning.zephyr-docs.usb.usb-guidelines
title: USB测试与示例约定
kind: reference
status: maintained
domains: [zephyr, usb]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/guidelines.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_USB测试与示例约定

原文：[Common guidelines for USB tests and samples](https://docs.zephyrproject.org/latest/services/connectivity/usb/guidelines.html)。读取日期：2026-10-12，`latest`。

## 5.1\_概述

总体而言，所有 **通用串行总线（Universal Serial Bus，USB）** 示例和测试都应与平台无关，不应要求平台专用的覆盖文件。现有代码树中可能已经存在例外，但目标仍是避免平台专用覆盖。USB 示例或测试没有必须支持某个特定平台的义务。

## 5.2\_开发板配置

开发板通过默认控制器节点标签和元数据中的能力声明，接入公共示例与测试。

### 5.2.1\_默认USB设备与主机控制器

USB 支持使用 `zephyr_udc0` 节点标签指定默认 USB 设备控制器，使用 `zephyr_uhc0` 节点标签指定默认 USB 主机控制器。开发板应按照实际支持的功能赋予这些节点标签，才能执行代码树中的对应示例和测试。

### 5.2.2\_开发板元数据中的支持特性

开发板元数据文件中，供 Twister 选择 USB 示例或测试的支持特性只有两个：

| 控制器支持的模式 | 特性名称 |
| --- | --- |
| USB 设备模式 | `usbd` |
| USB 主机模式 | `usbh` |

详情见 [Twister 开发板配置](https://docs.zephyrproject.org/latest/develop/twister/index.html#twister-board-configuration)。

### 5.2.3\_已弃用的特性

不应再使用 `usb_device` 特性。它属于旧版 USB 设备栈；该栈已经弃用，将被移除。

## 5.3\_USB测试的Twister配置

USB 测试可能需要额外的硬件或软件环境。此类测试应使用下表的 [fixture（测试配套条件）](https://docs.zephyrproject.org/latest/develop/twister/index.html#twister-fixtures)。

| Fixture | 用途 |
| --- | --- |
| `usb_host_connected` | 测试实现 USB **设备**功能，需要向被测开发板连接一个 USB **主机** |
| `usb_device_connected` | 测试实现 USB **主机**功能，需要向被测开发板连接一个 USB **设备** |

> 译注：fixture 名称描述连接到被测板的对端。元数据声明与 fixture 配置只是测试选择和运行条件，不代表控制器驱动、VBUS、电源或枚举已通过实板验证。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB厂商与产品标识](P004_USB厂商与产品标识.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USBIP协议支持](P006_USBIP协议支持.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：USB厂商与产品标识](P004_USB厂商与产品标识.md) · [后续参考：USB设备API](P013_USB设备API目录.md) · [返回大纲](大纲.md) · [下一章](P006_USBIP协议支持.md)

</details>

<!-- reading-navigation:end -->
