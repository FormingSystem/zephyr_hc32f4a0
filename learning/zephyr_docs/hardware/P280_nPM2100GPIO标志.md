---
id: learning.zephyr-docs.hardware.gpioext-6
title: nPM2100GPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第280章\_nPM2100GPIO标志

原文：[group__gpio__interface__npm2100](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html)。读取日期：2026-10-13，`latest`。

## 280.1\_驱动强度与去抖

本页定义 nPM2100 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/nordic-npm2100-gpio.h`。

标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位选择驱动强度（Drive Strength），0为正常（Normal）1 mA、1为高驱动（High）6 mA；第9位控制去抖（Debounce），0关闭、1开启。

## 280.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`NPM2100_GPIO_DRIVE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#gaaba391246c0041ce40cf9a9826cc2dbd) | `(0U << 8U)` | 正常驱动 |
| [`NPM2100_GPIO_DRIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga281cd37a16ba12b56850ea98d9b543d5) | `(1U << 8U)` | 高驱动 |
| [`NPM2100_GPIO_DEBOUNCE_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga79471e04dd5ed29a8a819403ab6d83d0) | `(0U << 9U)` | 去抖关闭；原单项说明为“正常驱动” |
| [`NPM2100_GPIO_DEBOUNCE_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga4b1336ed15dc7ed906d1aa69fddff33d) | `(1U << 9U)` | 去抖开启；原单项说明为“高驱动” |

> 译注：去抖宏的单项文字说明在原文中写成“Normal drive / High drive”，与宏名和第9位的整体说明不一致。表中保留原单项说明，并依据同页位定义标明去抖开关含义。

---

[上一章：nPM13xxGPIO标志](P279_nPM13xxGPIO标志.md) · [下一章：nPM6001GPIO标志](P281_nPM6001GPIO标志.md) · [返回大纲](大纲.md)
