---
id: learning.zephyr-docs.power.pmsamples-11
title: STM32挂起到RAM示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/suspend_to_ram/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="stm32_pm_suspend_to_ram"></a>

# 第59章\_STM32挂起到RAM示例

原文：[Suspend to RAM](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/suspend_to_ram/README.html)。读取日期：2026-10-13，`latest`。

## 59.1\_概述

本最小应用在低功耗环境中使用通用输入输出（General-Purpose Input/Output，GPIO）应用程序编程接口（Application Programming Interface，API）闪烁发光二极管（Light-Emitting Diode，LED），并执行模数转换器（Analog-to-Digital Converter，ADC）测量及熵（Entropy）相关操作，展示基本电源管理（Power Management，PM）。

示例还提供串行外设接口回环（Serial Peripheral Interface Loopback，SPI Loopback），但尚未为挂起到随机存取存储器（Suspend to RAM，RAM 为 Random Access Memory）PM模式实现。

## 59.2\_要求

开发板必须支持启用PM。STM32目标需要替代Cortex SysTick系统节拍定时器、且可在核心睡眠状态下工作的时钟源，例如低功耗定时器（Low-Power Timer，LPTIM），见 [st,stm32-lptim绑定](../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim)。

开发板还需要实时时钟（Real-Time Clock，RTC），在待机期间替代已禁用的LPTIM；同时必须具有RAM保持（RAM Retention）能力，以便在待机后恢复上下文（Context）。

## 59.3\_构建与运行

以下构建并烧录闪灯示例，将 `stm32wba55cg` 替换为自己的开发板：

```shell
west build -b stm32wba55cg samples/boards/st/power_mgmt/suspend_to_ram
west flash
```

烧录后LED开始闪烁。

## 59.4\_PM配置与参考

默认启用 Kconfig 选项 [`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE) 和 [`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)。另见[设备运行时电源管理接口](P037_设备运行时电源管理接口.md)。

---

[上一章：STM32_STOP3示例](P058_STM32_STOP3示例.md) · [下一章：STM32唤醒引脚示例](P060_STM32唤醒引脚示例.md) · [返回大纲](大纲.md)
