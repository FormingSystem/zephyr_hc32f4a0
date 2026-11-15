---
id: learning.zephyr-docs.usb.page-72
title: USB主机控制器API说明
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/host/api/uhc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_USB主机控制器API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/host/api/uhc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 72.1\_USB主机控制器驱动API（USB Host Controller Driver API）

USB主机控制器驱动API在 [`include/zephyr/drivers/usb/uhc.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/uhc.h) 中描述，简称 `UHC driver` API。

UHC驱动API仍处于实验阶段（Experimental），可能不经通知就发生变更。

## 72.2\_驱动API参考（Driver API Reference）

[USB主机控制器](P073_USB主机控制器API.md)。

> 译注：控制器驱动负责总线操作及传输提交等硬件接口，上层USB主机栈负责设备管理和事件处理。它与USB设备控制器（USB Device Controller，UDC）API职责不同，不能因目标芯片有USB设备功能就推定支持主机角色。本组同时翻译驱动公共数据、能力、事件和传输结构；源码与原注释存在的差异在相应接口处说明。


译注核对来源：[include/zephyr/drivers/usb/uhc.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)。

本仓库的[对应源码](../../../include/zephyr/drivers/usb/uhc.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-host-controller-uhc-driver-api"></a>
<a id="uhc-api"></a>
<a id="driver-api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB主机API目录](P071_USB主机API目录.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB音频2设备API说明](P088_USB音频2设备API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P071_USB主机API目录.md) · [返回大纲](大纲.md) · [下一章](P073_USB主机控制器API.md)

</details>

<!-- reading-navigation:end -->
