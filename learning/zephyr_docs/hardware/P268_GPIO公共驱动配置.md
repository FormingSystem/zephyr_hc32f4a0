---
id: learning.zephyr-docs.hardware.gpiostruct-1
title: GPIO公共驱动配置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第268章\_GPIO公共驱动配置

原文：[structgpio__driver__config](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__config.html)。读取日期：2026-10-13，`latest`。

## 268.1\_结构布局

结构 [`gpio_driver_config`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__config.html) 是所有 **通用输入/输出（General Purpose Input/Output，GPIO）**驱动共享的配置，声明来自 `zephyr/drivers/gpio.h`。它应作为设备结构 `config` 字段所指对象的首成员（First Element）。

## 268.2\_支持引脚掩码

<a id="af73c0d9d433b86b9d0e0c6703e737052"></a>

字段 [`port_pin_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__config.html#af73c0d9d433b86b9d0e0c6703e737052) 的类型为 [`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f)，它是标识控制器支持哪些引脚的位掩码（Bitmask）。驱动生成设备实例时负责初始化这个掩码。

---

[上一章：GPIO设备树描述](P267_GPIO设备树描述.md) · [下一章：GPIO公共驱动数据](P269_GPIO公共驱动数据.md) · [返回大纲](大纲.md)
