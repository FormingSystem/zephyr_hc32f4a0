---
id: learning.zephyr-docs.hardware.gpioext-2
title: nRFGPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第276章\_nRFGPIO标志

原文：[group__gpio__interface__nrf](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html)。读取日期：2026-10-13，`latest`。

## 276.1\_驱动能力

本页定义 nRF 的通用输入/输出（General Purpose Input/Output，GPIO）驱动标志，声明来自 `zephyr/dt-bindings/gpio/nordic-nrf-gpio.h`。标准驱动（Standard Drive，S）和高驱动（High Drive，H）可分别应用于0、1两个电平。高驱动会提高引脚电流能力，具体范围参照各片上系统（System on Chip，SoC）的参考手册。

开漏（Open Drain，线与 Wired AND）模式对应宏 `GPIO_OPEN_DRAIN`，此时电平1为断开状态，只能选择电平0的驱动能力。开源极（Open Source，线或 Wired OR）模式对应宏 `GPIO_OPEN_SOURCE`，此时电平0为断开状态，只能选择电平1的驱动能力。

标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位选择电平0的驱动，0为标准、1为高驱动；第9位以同样方式选择电平1的驱动。

## 276.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`NRF_GPIO_DRIVE_S0`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga00ce8b0f371e41899b0379adc4647036) | `(0U << 8U)` | 电平0标准驱动，默认，配合开漏使用 |
| [`NRF_GPIO_DRIVE_H0`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#gaa21a50e68b9018384dc7b409673cd047) | `(1U << 8U)` | 电平0高驱动，配合开漏使用 |
| [`NRF_GPIO_DRIVE_S1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga5909d23af54ccd8bea797e0f74871cb3) | `(0U << 9U)` | 电平1标准驱动，默认，配合开源极使用 |
| [`NRF_GPIO_DRIVE_H1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga8adac513c62dfc12b9f4d7272d73a99f) | `(1U << 9U)` | 电平1高驱动，配合开源极使用 |
| [`NRF_GPIO_DRIVE_S0S1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga0b03a6717cc2e5d57aba54379188a884) | `(NRF_GPIO_DRIVE_S0 \| NRF_GPIO_DRIVE_S1)` | 电平0和1均标准驱动，默认 |
| [`NRF_GPIO_DRIVE_S0H1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga43697400db8d8cba4dd4bbaaae59a551) | `(NRF_GPIO_DRIVE_S0 \| NRF_GPIO_DRIVE_H1)` | 电平0标准，电平1高驱动 |
| [`NRF_GPIO_DRIVE_H0S1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga4426bd906d7e2965f53e21a246ec0bbc) | `(NRF_GPIO_DRIVE_H0 \| NRF_GPIO_DRIVE_S1)` | 电平0高驱动，电平1标准 |
| [`NRF_GPIO_DRIVE_H0H1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga905a8813a86d8cf1087a47eadc089987) | `(NRF_GPIO_DRIVE_H0 \| NRF_GPIO_DRIVE_H1)` | 电平0和1均高驱动 |

---

[上一章：STM32GPIO标志](P275_STM32GPIO标志.md) · [下一章：MAX32GPIO标志](P277_MAX32GPIO标志.md) · [返回大纲](大纲.md)
