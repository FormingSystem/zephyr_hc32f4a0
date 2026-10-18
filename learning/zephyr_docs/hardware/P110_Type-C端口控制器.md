---
id: learning.zephyr-docs.hardware.powerper-4
title: Type-C端口控制器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/tcpc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第110章\_Type-C端口控制器

原文：[USB Type-C Port Controller (TCPC)](https://docs.zephyrproject.org/latest/hardware/peripherals/tcpc.html)。读取日期：2026-10-13，`latest`。

## 110.1\_端口控制器的三类功能

**USB Type-C端口控制器（USB Type-C Port Controller，TCPC）**用于简化USB-C系统实现。USB表示 **通用串行总线（Universal Serial Bus）**；控制器的规范入口见[USB Type-C端口控制器接口规范](https://www.usb.org/document-library/usb-type-cr-port-controller-interface-specification)。原页归纳三类功能。

第一类是VBUS与VCONN控制。VBUS是USB连接的总线供电线路，VCONN是供连接线缆使用的电源名称。TCPC可为 **供电端（Source）**提供控制VBUS供电的机制，为 **受电端（Sink）**提供控制VBUS受电的机制，并为VCONN提供类似控制。原文链接[USB Type-C线缆与连接器规范2.1](https://www.usb.org/document-library/usb-type-cr-cable-and-connector-specification-revision-21)。

第二类是 **配置通道（Configuration Channel，CC）**的控制与检测。TCPC实现控制CC引脚上拉、下拉电阻的逻辑，并提供检测与报告CC引脚所接电阻的方式。

第三类是 **电力传输（Power Delivery，PD）**消息的收发。TCPC负责收发由 **Type-C端口管理器（Type-C Port Manager，TCPM）**构造的消息，并通过CC线路传输；相关规范见[USB Power Delivery](https://www.usb.org/document-library/usb-power-delivery)。

## 110.2\_驱动接口与配置

TCPC设备驱动连接TCPC设备与应用软件。驱动提供Zephyr **应用程序编程接口（Application Programming Interface，API）**，用于与TCPC设备通信并控制它。

相关Kconfig配置项为 [`CONFIG_USBC_TCPC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_TCPC_DRIVER)；Kconfig是Zephyr配置系统。

## 110.3\_参考入口

原页保留三个参考入口：[USB Type-C](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html)、[USB Type-C端口控制器API](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html)以及[USB Power Delivery](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html)。VBUS独立驱动概览见[下一章](P111_USB-C总线电源.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：BC1.2充电识别](P109_BC1.2充电识别.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：USB-C总线电源](P111_USB-C总线电源.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：BC1.2充电识别](P109_BC1.2充电识别.md) · [下一章：USB-C总线电源](P111_USB-C总线电源.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
