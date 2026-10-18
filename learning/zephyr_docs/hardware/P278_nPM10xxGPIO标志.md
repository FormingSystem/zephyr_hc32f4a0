---
id: learning.zephyr-docs.hardware.gpioext-4
title: nPM10xxGPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第278章\_nPM10xxGPIO标志

原文：[group__gpio__interface__npm10xx](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html)。读取日期：2026-10-13，`latest`。

## 278.1\_驱动强度与去抖

本页定义 nPM10xx 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/nordic-npm10xx-gpio.h`。

标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位选择驱动强度（Drive Strength），0为正常（Normal）2 mA、1为高驱动（High）4 mA；第9位控制去抖（Debounce），0关闭、1开启。

## 278.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`NPM10XX_GPIO_DRIVE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gaa453cd596eca9e14d222457506d805d5) | `(0U << 8U)` | 正常2 mA驱动 |
| [`NPM10XX_GPIO_DRIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga83f0e8761270947b758546c259206f0d) | `(1U << 8U)` | 高4 mA驱动 |
| [`NPM10XX_GPIO_DEBOUNCE_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga52154f1315bad8d24afbacb0d3924bc9) | `(0U << 9U)` | 关闭去抖 |
| [`NPM10XX_GPIO_DEBOUNCE_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gae76b53ec23c6515a7761c517fb35fe3a) | `(1U << 9U)` | 开启去抖 |

---

[上一章：MAX32GPIO标志](P277_MAX32GPIO标志.md) · [下一章：nPM13xxGPIO标志](P279_nPM13xxGPIO标志.md) · [返回大纲](大纲.md)
