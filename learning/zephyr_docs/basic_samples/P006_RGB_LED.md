---
id: learning.zephyr-docs.basic-samples.basic-rgb
title: PWM RGB LED
kind: reference
status: maintained
domains: [zephyr, development, samples]
source_url: https://docs.zephyrproject.org/latest/samples/basic/rgb_led/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_PWM RGB LED

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/basic/rgb_led/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/rgb_led)。本仓库的[源码参照](../../../samples/basic/rgb_led/src/main.c)采用相对链接；参照版本不自动等同于官网版本。

<a id="rgb-led"></a>
<a id="overview"></a>

## 6.1\_概述

本示例使用[脉宽调制（Pulse Width Modulation，PWM）API](https://docs.zephyrproject.org/latest/hardware/peripherals/pwm.html#pwm-api)驱动红绿蓝（Red, Green, Blue，RGB）LED。

RGB LED内部有三个单色LED分量。每个分量由一个PWM端口驱动，脉宽从零变化到设备树中指定的周期值。对应频率应足够高，超过闪烁融合阈值（Flicker Fusion Threshold），即人眼感觉LED保持稳定所需的最低闪烁频率。

示例让每个LED分量从暗逐步变化到最大亮度。三个`for`循环分别控制一个分量，使RGB LED呈现渐变的颜色范围，并不断重复。

<a id="requirements"></a>

## 6.2\_要求

开发板必须有通过PWM输出通道连接的红、绿、蓝LED。LED的PWM通道必须通过下列[设备树别名](https://docs.zephyrproject.org/latest/build/dts/index.html#dt-guide)配置，通常位于[`BOARD.dts`文件](https://docs.zephyrproject.org/latest/build/dts/intro-input-output.html#devicetree-in-out-files)中：

- `red-pwm-led`
- `green-pwm-led`
- `blue-pwm-led`

为不支持的开发板构建时，会看到以下错误中的至少一个：

```text
Unsupported board: red-pwm-led devicetree alias is not defined
Unsupported board: green-pwm-led devicetree alias is not defined
Unsupported board: blue-pwm-led devicetree alias is not defined
```

支持该示例的`BOARD.dts`文件可参考[boards/mikroe/hexiwear/hexiwear_mk64f12.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/hexiwear/hexiwear_mk64f12.dts)。

<a id="wiring"></a>

## 6.3\_接线

如果所需的设备树别名指向已经连接到板载LED的硬件，则不需要额外接线。否则，应将LED连接到适当的PWM通道。

<a id="building-and-running"></a>

## 6.4\_构建与运行

例如，为[Hexiwear](https://docs.zephyrproject.org/latest/boards/mikroe/hexiwear/doc/index.html#hexiwear)构建并烧录：

```shell
west build -b hexiwear/mk64f12 samples/basic/rgb_led
west flash
```

其他受支持开发板应相应替换`hexiwear/mk64f12`。

<a id="see-also"></a>

## 6.5\_另请参阅

- [PWM API](../hardware/P255_PWM公共接口.md)

[上一章：LED渐变](P005_LED渐变.md) · [返回大纲](大纲.md) · [下一章：舵机控制](P007_舵机控制.md)
