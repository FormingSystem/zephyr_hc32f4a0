---
id: learning.zephyr-docs.power.pmsamples-6
title: STM32_ADC电源管理示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/adc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="stm32_pm_adc"></a>

# 第54章\_STM32_ADC电源管理示例

原文：[ADC power management](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/adc/README.html)。读取日期：2026-10-13，`latest`。

## 54.1\_概述与要求

这是一个最小应用，在低功耗环境中以基本模数转换器（Analog-to-Digital Converter，ADC）配置演示电源管理（Power Management，PM）行为。

开发板必须支持启用 PM。对 STM32 目标，意味着支持一种替代 Cortex SysTick 系统节拍定时器、且在核心睡眠状态下仍可使用的时钟源，例如低功耗定时器（Low-Power Timer，LPTIM），对应绑定 [st,stm32-lptim](../stm32_ti_silabs_timer_binding_reference/P007_st_stm32-lptim.md#std-dtcompatible-st-stm32-lptim)。

## 54.2\_构建与运行

按以下命令构建和烧录，将 `nucleo_wb55rg` 替换为自己的开发板：

```shell
west build -b nucleo_wb55rg samples/boards/st/power_mgmt/adc
west flash
```

烧录后，控制台显示类似以下ADC测量结果；原页以普通文本列出：

```text
ADC reading[0]:
- adc@50040000, channel 3: 1158 = 932 mV
```

## 54.3\_PM配置

默认启用 Kconfig 选项 [`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE) 和 [`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)，分别用于设备PM与运行时PM。原文在STM32WB上观察到：两项都启用时约25 µA，两项都未启用时约27.5 µA；两种测量均启用了 [`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)。

另见[ADC接口](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html)。

---

[上一章：STM32电源管理示例目录](P053_STM32电源管理示例目录.md) · [下一章：STM32低功耗闪灯示例](P055_STM32低功耗闪灯示例.md) · [返回大纲](大纲.md)
