---
id: learning.zephyr-docs.hardware.ledsamp-0
title: LED驱动示例目录
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第187章\_LED驱动示例目录

原文：[Light-Emitting Diode (LED)](https://docs.zephyrproject.org/latest/samples/drivers/led/index.html)。读取日期：2026-10-13，`latest`。

## 187.1\_示例范围

这些示例展示 **发光二极管（Light-Emitting Diode，LED）**驱动的 **应用程序编程接口（Application Programming Interface，API）**用法。下表的 RGB 为红、绿、蓝（Red, Green, Blue），RGBW 还包含白色（White）；PWM 为 **脉冲宽度调制（Pulse Width Modulation）**。

| 示例 | 原页给出的功能摘要 |
| --- | --- |
| [呼吸闪烁灯（Breathing-Blinking LED，BBLED）](P201_XEC呼吸闪烁灯示例.md) | 使用 Microchip XEC 驱动控制 BBLED。 |
| [IS31FL319x三色灯](P188_IS31FL319x三色LED示例.md) | 控制接在 IS31FL3193、IS31FL3194 或 IS31FL3197 上的 RGB LED，循环切换颜色。 |
| [IS31FL3216A](P189_IS31FL3216A发光二极管示例.md) | 控制最多 16 个 PWM LED。 |
| [IS31FL3733灯矩阵](P190_IS31FL3733灯矩阵示例.md) | 控制最多 192 个 LED 组成的矩阵。 |
| [LED PWM](P198_PWM发光二极管示例.md) | 通过 LED API 控制 PWM LED。 |
| [LED灯带](P191_LED灯带示例.md) | 控制 LED 灯带（LED Strip）。 |
| [LP3943 RGBW](P192_LP3943四色LED示例.md) | 原页摘要：控制最多 16 个 RGBW LED。 |
| [LP50XX RGB](P193_LP50XX三色LED示例.md) | 控制最多 12 个 RGB LED。 |
| [LP5562 RGB](P194_LP5562三色LED示例.md) | 原页摘要：控制 4 个 RGB LED。 |
| [LP5569九通道控制器](P195_LP5569九通道LED示例.md) | 控制 9 个 LED。 |
| [LP586x灯矩阵](P196_LP586x灯矩阵示例.md) | 控制 LP586x 矩阵控制器上的 LED 点。 |
| [PCA9633](P197_PCA9633发光二极管示例.md) | 控制 4 个 LED。 |
| [SCT2024](P199_SCT2024发光二极管示例.md) | 控制最多 16 个 LED。 |
| [SX1509B RGB](P200_SX1509B三色LED示例.md) | 控制一个 RGB LED。 |

译注：表中保留官方目录的功能摘要与数量表述；具体的灯、颜色分量和输出通道关系应以各示例正文及器件定义为准。

[上一章：字符帧缓冲坐标结构](P186_字符帧缓冲坐标结构.md) · [下一章：IS31FL319x三色LED示例](P188_IS31FL319x三色LED示例.md) · [返回大纲](大纲.md)
