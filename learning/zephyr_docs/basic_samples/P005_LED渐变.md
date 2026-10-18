---
id: learning.zephyr-docs.basic-samples.basic-fade
title: LED渐变
kind: reference
status: maintained
domains: [zephyr, development, samples]
source_url: https://docs.zephyrproject.org/latest/samples/basic/fade_led/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_LED渐变

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/basic/fade_led/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/fade_led)。本仓库的[源码参照](../../../samples/basic/fade_led/src/main.c)采用相对链接；参照版本不自动等同于官网版本。

<a id="fade-led"></a>
<a id="overview"></a>

## 5.1\_概述

本应用使用[脉宽调制（Pulse Width Modulation，PWM）API](https://docs.zephyrproject.org/latest/hardware/peripherals/pwm.html#pwm-api)使LED亮度渐变。

LED从熄灭状态逐渐变亮，直到完全或接近完全点亮；随后亮度逐渐降低，直到熄灭，完成一次渐变循环。每个循环持续2.5秒，并不断重复。PWM周期取自设备树（Devicetree），对应频率应足够高，超过闪烁融合阈值（Flicker Fusion Threshold）。

<a id="requirements-and-wiring"></a>

## 5.2\_要求与接线

本示例的要求和接线注意事项与[PWM闪烁LED示例](P004_PWM闪烁LED.md#pwm-blinky)相同。

<a id="building-and-running"></a>

## 5.3\_构建与运行

为[nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)构建并烧录：

```shell
west build -b nrf52840dk/nrf52840 samples/basic/fade_led
west flash
```

其他受支持开发板应相应替换`nrf52840dk/nrf52840`。

烧录后，示例按前述方式改变LED亮度，同时向开发板控制台打印信息。

<a id="see-also"></a>

## 5.4\_另请参阅

- [PWM API](../hardware/P255_PWM公共接口.md)

[上一章：PWM闪烁LED](P004_PWM闪烁LED.md) · [返回大纲](大纲.md) · [下一章：PWM RGB LED](P006_RGB_LED.md)
