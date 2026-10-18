---
id: learning.zephyr-docs.hardware.gpioext-7
title: nPM6001GPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第281章\_nPM6001GPIO标志

原文：[group__gpio__interface__npm6001](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html)。读取日期：2026-10-13，`latest`。

## 281.1\_驱动与输入类型

本页定义 nPM6001 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/nordic-npm6001-gpio.h`。

标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位选择驱动强度（Drive Strength），0为正常（Normal）、1为高驱动（High）；第9位选择输入类型，0为施密特触发器（Schmitt Trigger），1为互补金属氧化物半导体（Complementary Metal-Oxide-Semiconductor，CMOS）输入。

## 281.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`NPM6001_GPIO_DRIVE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#gaa127d582ea7095b4d7a435ee5ea427c9) | `(0U << 8U)` | 正常驱动 |
| [`NPM6001_GPIO_DRIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga097b6c75d981ad5ecf38a2133d076178) | `(1U << 8U)` | 高驱动 |
| [`NPM6001_GPIO_SENSE_SCHMITT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga3cde51b59da0f8bf4693ef18b9ee8a30) | `(0U << 9U)` | 施密特触发器输入 |
| [`NPM6001_GPIO_SENSE_CMOS`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga98c66bc1cf5a8c0f83b82c830a817fa2) | `(1U << 9U)` | CMOS输入 |

---

[上一章：nPM2100GPIO标志](P280_nPM2100GPIO标志.md) · [下一章：AmbiqGPIO扩展](P282_AmbiqGPIO扩展.md) · [返回大纲](大纲.md)
