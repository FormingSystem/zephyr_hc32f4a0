---
id: learning.zephyr-docs.hardware.gpiostruct-2
title: GPIO公共驱动数据
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第269章\_GPIO公共驱动数据

原文：[structgpio__driver__data](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__data.html)。读取日期：2026-10-13，`latest`。

## 269.1\_结构布局

结构 [`gpio_driver_data`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__data.html) 是所有 **通用输入/输出（General Purpose Input/Output，GPIO）**驱动共享的数据，声明来自 `zephyr/drivers/gpio.h`。它应作为驱动 `struct driver_data` 声明的首成员（First Element）。

## 269.2\_反相掩码

<a id="ab62038a3c7c341cafda6665dfab3f169"></a>

字段 [`invert`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__data.html#ab62038a3c7c341cafda6665dfab3f169) 的类型为 [`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f)，它是标识哪些引脚配置为低电平有效（Active Low）的位掩码（Bitmask）。该掩码由头文件中的封装函数（Wrapper Functions）负责管理。

---

[上一章：GPIO公共驱动配置](P268_GPIO公共驱动配置.md) · [下一章：GPIO回调结构](P270_GPIO回调结构.md) · [返回大纲](大纲.md)
