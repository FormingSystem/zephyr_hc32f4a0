---
id: learning.zephyr-docs.hardware.ledsamp-1
title: IS31FL319x三色LED示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/is31fl319x/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="is31fl319x"></a>

# 第188章\_IS31FL319x三色LED示例

原文：[IS31FL319x RGB LED](https://docs.zephyrproject.org/latest/samples/drivers/led/is31fl319x/README.html)。读取日期：2026-10-13，`latest`。

## 188.1\_概述（Overview）

本示例遍历器件上定义的各个 **发光二极管（Light-Emitting Diode，LED）**，打印各灯的信息，包括已定义的颜色；随后输出这些颜色，并逐渐变暗直到熄灭。

枚举所有 LED 索引后，程序使用 `led_write_channels()` **应用程序编程接口（Application Programming Interface，API）**使所有已定义的 LED 渐变。

接下来检查是否存在同时定义红、绿、蓝（Red, Green, Blue，RGB）三个颜色分量的 LED。如果存在，先按红、绿、蓝的顺序使颜色渐变，再循环显示若干不同颜色。

辅助函数负责把 RGB 分量映射到实际硬件的正确顺序。有的 LED 使用 RGB 顺序，有的使用蓝、绿、红（Blue, Green, Red，BGR）等顺序；映射完成后再调用 LED 库显示颜色。

只有一种颜色的 LED 使用亮度设置接口，从 0% 逐渐增加到 100%，再降低到 0%。渐亮渐暗的重复次数与这个 LED 在器件中的索引相同。

译注：原文把亮度函数写作 `led_set brightness`，正式 [LED接口](P202_LED公共接口.md)中的名称为 `led_set_brightness()`。

## 188.2\_构建与运行（Building and Running）

可以使用 Arduino Nicla Sense ME，或带 Arduino Giga Display 扩展板（Shield）的 Arduino Giga。也可使用其他开发板，只要 **设备树（Devicetree）**中已启用对应的 **内部集成电路总线（Inter-Integrated Circuit，I2C）**器件节点及其总线控制器，并采用以下兼容标识（Compatible）之一：

- [`issi,is31fl3193`](../led_issi_nordic_nxp_binding_reference/P005_issi_is31fl3193.md#std-dtcompatible-issi-is31fl3193)。
- [`issi,is31fl3194`](../led_issi_nordic_nxp_binding_reference/P006_issi_is31fl3194.md#std-dtcompatible-issi-is31fl3194)。
- [`issi,is31fl3197`](../led_issi_nordic_nxp_binding_reference/P007_issi_is31fl3197.md#std-dtcompatible-issi-is31fl3197)。

译注：以下是两个独立的官方构建分支，在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行。示例由官方仓库提供，west 生成构建产物，`west flash` 将固件烧录到开发板。

Arduino Nicla Sense ME：

```bash
west build -b arduino_nicla_sense_me samples/drivers/led/is31fl319x
west flash
```

Arduino Giga 配合显示扩展板：

```bash
west build -b arduino_giga_r1//m7 --shield arduino_giga_display_shield samples/drivers/led/is31fl319x
west flash
```

烧录后，LED 开始切换颜色，控制台打印当前颜色。如果发生运行时错误，示例会退出，且不向控制台打印该错误。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/led/is31fl319x)

[上一章：LED驱动示例目录](P187_LED驱动示例目录.md) · [下一章：IS31FL3216A发光二极管示例](P189_IS31FL3216A发光二极管示例.md) · [返回大纲](大纲.md)
