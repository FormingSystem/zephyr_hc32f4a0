---
id: learning.zephyr-docs.usb.page-9
title: USBC示例目录
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb_c/usbc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_USBC示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb_c/usbc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 9.1\_USB-C设备支持示例

本组示例展示[USB-C 设备栈](P007_USBC设备栈.md#usbc-api)的用法。

| 官方示例 | 用途 |
| --- | --- |
| [基础 USB-C DRP](P010_USBC双电源角色示例.md#usb-c-drp) | 以双电源角色（Dual Role Power，DRP）设备的形式实现 USB 电力传输（USB Power Delivery，USB PD）应用。 |
| [基础 USB-C Sink](P011_USBC受电端示例.md#usb-c-sink) | 以受电端（Sink）的形式实现 USB-C PD 应用。 |
| [基础 USB-C Source](P012_USBC供电端示例.md#usb-c-source) | 以供电端（Source）的形式实现 USB-C PD 应用。 |

> 译注：先读设备栈指南中的连接状态机、设备树及策略回调，再按实际硬件支持的供电角色选择示例。以下页面翻译的是官方样例及其测试条件，不表示本仓库涉及的所有开发板均已实现这些功能。


<a id="usb-c-device-support"></a>

[上一章](P008_旧版USB设备支持.md) · [返回大纲](大纲.md) · [下一章](P010_USBC双电源角色示例.md)
