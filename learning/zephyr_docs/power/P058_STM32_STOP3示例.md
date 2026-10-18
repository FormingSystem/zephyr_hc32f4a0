---
id: learning.zephyr-docs.power.pmsamples-10
title: STM32_STOP3示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/stop3/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="stm32_pm_stop3"></a>

# 第58章\_STM32_STOP3示例

原文：[STOP3 mode](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/stop3/README.html)。读取日期：2026-10-13，`latest`。

## 58.1\_概述与要求

本最小应用用闪烁的发光二极管（Light-Emitting Diode，LED）演示基本电源管理（Power Management，PM）和STM32U5的STOP3低功耗模式。

原文当前仅支持 `nucleo_u575zi_q`。开发板需要实时时钟（Real-Time Clock，RTC），在待机（Standby）模式中替代已经禁用的低功耗定时器（Low-Power Timer，LPTIM）。

## 58.2\_构建与运行

```shell
west build -b nucleo_u575zi_q samples/boards/st/power_mgmt/stop3
west flash
```

烧录后，LED开始闪烁。

## 58.3\_PM配置

默认启用设备PM的 Kconfig 选项 [`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE) 和设备运行时PM选项 [`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)。

---

[上一章：STM32WB蓝牙低功耗示例](P057_STM32WB蓝牙低功耗示例.md) · [下一章：STM32挂起到RAM示例](P059_STM32挂起到RAM示例.md) · [返回大纲](大纲.md)
