---
id: learning.zephyr-docs.hardware.powerper-5
title: USB-C总线电源
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/usbc_vbus.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第111章\_USB-C总线电源

原文：[USB-C VBUS](https://docs.zephyrproject.org/latest/hardware/peripherals/usbc_vbus.html)。读取日期：2026-10-13，`latest`。

## 111.1\_从供电端到受电端的电源线路

USB-C的VBUS是USB Type-C连接中，将电能从 **供电端（Source）**传送至 **受电端（Sink）**的线路。USB为 **通用串行总线（Universal Serial Bus）**；VBUS在本文表示 **总线电源（Bus Power）**线路名称。

## 111.2\_控制、测量与配置

USB-C VBUS设备驱动提供用于控制、测量VBUS的 **应用程序编程接口（Application Programming Interface，API）**。

相关Kconfig配置项为 [`CONFIG_USBC_VBUS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_VBUS_DRIVER)；Kconfig是Zephyr配置系统。完整接口见[USB-C VBUS API](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Type-C端口控制器](P110_Type-C端口控制器.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：错误检测与纠正](P112_错误检测与纠正.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Type-C端口控制器](P110_Type-C端口控制器.md) · [下一章：错误检测与纠正](P112_错误检测与纠正.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
