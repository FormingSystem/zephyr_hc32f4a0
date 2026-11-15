---
id: learning.zephyr-docs.power.pmsamples-9
title: STM32WB蓝牙低功耗示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/stm32wb_ble/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="stm32_pm_stm32wb_ble"></a>

# 第57章\_STM32WB蓝牙低功耗示例

原文：[Bluetooth Low Energy Power Management on STM32WB](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/stm32wb_ble/README.html)。读取日期：2026-10-13，`latest`。

## 57.1\_概述

本应用在启用 Zephyr 电源管理（Power Management，PM）的情况下演示低功耗蓝牙（Bluetooth Low Energy，BLE）广播（Advertising），对应 Kconfig 选项 [`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)。

启动后先发送2秒信标（Beacon），暂停1秒，再次开始信标。随后关闭BLE链路，2秒后重新启动，并重复同样的信标序列。

最后触发平台关闭（Shutdown），按开发板复位键可以重新启动。

使用功耗测量工具，可观察到平台在信标开始之前和广播峰值之间进入STOP2模式，并在请求关闭时进入SHUTDOWN模式。

## 57.2\_要求

原文当前只列出 `nucleo_wb55rg` 为兼容开发板。

## 57.3\_另请参阅

[系统关机接口](P063_系统关机接口.md)、[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)与[蓝牙应用程序编程接口（Application Programming Interface，API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。

---

[上一章：STM32串口唤醒示例](P056_STM32串口唤醒示例.md) · [下一章：STM32_STOP3示例](P058_STM32_STOP3示例.md) · [返回大纲](大纲.md)
