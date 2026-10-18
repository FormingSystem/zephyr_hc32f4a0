---
id: learning.zephyr-docs.hardware.ledrest-1
title: PWM发光二极管示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/pwm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="led-pwm"></a>

# 第198章\_PWM发光二极管示例

原文：[LED PWM](https://docs.zephyrproject.org/latest/samples/drivers/led/pwm/README.html)。读取日期：2026-10-13，`latest`。

## 198.1\_概述（Overview）

本示例测试 `led-pwm` 驱动，使用 **脉冲宽度调制（Pulse Width Modulation，PWM）**控制 **发光二极管（Light-Emitting Diode，LED）**。程序选择 **设备树（Devicetree，DT）**中找到的第一个兼容标识为 `pwm-leds` 的设备实例。

对连接到该设备的每个 LED，也就是其各子节点，程序使用 LED **应用程序编程接口（Application Programming Interface，API）**执行相同的测试图案。

## 198.2\_测试图案（Test Pattern）

依次处理每个 PWM LED：

1. 点亮。
2. 关闭。
3. 逐渐增加亮度。
4. 逐渐降低亮度。
5. 按亮 0.1 秒、灭 0.1 秒闪烁。
6. 按亮 1 秒、灭 1 秒闪烁。
7. 关闭。

## 198.3\_备用闪烁延时计算（Fallback Blink Delay Calculation）

当配置的闪烁延时超过平台定时器的范围限制时，示例会根据设备树中各 LED 的 PWM 周期自动计算备用延时，使用可配置的除数：

- 短延时（Short Delay）＝ LED PWM 周期 ÷ `CONFIG_BLINK_DELAY_SHORT_LED_PERIOD_DIV` ÷ 2。
- 长延时（Long Delay）＝ LED PWM 周期 ÷ `CONFIG_BLINK_DELAY_LONG_LED_PERIOD_DIV` ÷ 2。

这样，在存在定时器限制的平台上，仍可使用适合硬件且与每个 LED 的 PWM 配置兼容的延时。

## 198.4\_构建与运行（Building and Running）

本示例可在连接了 PWM LED 的开发板上构建和执行。必须在 **设备树源（Devicetree Source，DTS）**中正确描述 LED：设备节点的 `compatible` 属性匹配 `pwm-leds`，每个 LED 定义一个子节点，并通过 `pwms` 属性中的节点引用句柄（Phandle）及其引用节点提供 PWM 配置。

[LED接口](P202_LED公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/led/pwm)

[上一章：PCA9633发光二极管示例](P197_PCA9633发光二极管示例.md) · [下一章：SCT2024发光二极管示例](P199_SCT2024发光二极管示例.md) · [返回大纲](大纲.md)
