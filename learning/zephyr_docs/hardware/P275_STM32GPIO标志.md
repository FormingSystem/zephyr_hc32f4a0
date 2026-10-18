---
id: learning.zephyr-docs.hardware.gpioext-1
title: STM32GPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第275章\_STM32GPIO标志

原文：[group__gpio__interface__stm32](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html)。读取日期：2026-10-13，`latest`。

## 275.1\_标志编码

本页定义 STM32 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/stm32-gpio.h`。标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位用于关机（Poweroff）后重新上电，第9—10位用于输出速度（Output Speed）。

宏 `STM32_GPIO_SPEED_SHIFT` 是速度字段的位移量。唤醒标志 [`STM32_GPIO_WKUP`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#ga9a05f736e9ee915f591a65a7f6d382d3) 仅用于通过 STM32 电源控制（Power Control，PWR）设备树节点的 `wkup-gpios` 属性关联到唤醒引脚的GPIO。

## 275.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| `STM32_GPIO_WKUP` | `(1 << 8)` | 配置为关机后重新上电的GPIO引脚 |
| [`STM32_GPIO_LOW_SPEED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaa8d19f48bfea73193ff35c06a6894df6) | `(0x0 << STM32_GPIO_SPEED_SHIFT)` | 低输出速度 |
| [`STM32_GPIO_MEDIUM_SPEED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaee4f9eb7cb958d4a55d13029658bdff3) | `(0x1 << STM32_GPIO_SPEED_SHIFT)` | 中输出速度 |
| [`STM32_GPIO_HIGH_SPEED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gac91d2b48bc764131896ebb3b0436dac1) | `(0x2 << STM32_GPIO_SPEED_SHIFT)` | 高输出速度 |
| [`STM32_GPIO_VERY_HIGH_SPEED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#gaeff690b8406b0ed24f97bbe8ab4bf31e) | `(0x3 << STM32_GPIO_SPEED_SHIFT)` | 很高输出速度 |

---

[上一章：GPIO器件扩展目录](P274_GPIO器件扩展目录.md) · [下一章：nRFGPIO标志](P276_nRFGPIO标志.md) · [返回大纲](大纲.md)
