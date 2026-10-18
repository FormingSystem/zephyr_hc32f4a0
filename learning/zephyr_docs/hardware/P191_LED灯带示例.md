---
id: learning.zephyr-docs.hardware.ledsamp-4
title: LED灯带示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/led_strip/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="led-strip"></a>

# 第191章\_LED灯带示例

原文：[LED strip](https://docs.zephyrproject.org/latest/samples/drivers/led/led_strip/README.html)。读取日期：2026-10-13，`latest`。

## 191.1\_概述（Overview）

本示例演示 **发光二极管灯带（Light-Emitting Diode Strip，LED Strip）**的基本用法。

## 191.2\_要求（Requirements）

Zephyr 支持多种 LED 灯带芯片，例如：

- WS2812，例如 Adafruit 的 [NeoPixel兼容灯带](https://www.adafruit.com/product/3919)。
- APA102，例如 Adafruit 的 [DotStar兼容灯带](https://www.adafruit.com/product/2242)。
- LPD8806，例如 Adafruit 的 [LPD8806灯带](https://www.adafruit.com/product/1948)。

还需要供电电源，这些灯带通常使用 5 V 电源。如果灯带连接到 **串行外设接口（Serial Peripheral Interface，SPI）**总线，通信信号通常采用 5 V 电平，可能需要 **电平转换器（Level Translator）**，例如原文所列的 [74AHCT125资料](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf)。

## 191.3\_APA020与LPD880x接线

译注：本小节标题保留原文的 `APA020`；原文前面的器件清单使用 `APA102`，两处名称不同，具体器件应以所用芯片为准。

1. Zephyr 开发板、5 V 电源和 LED 灯带必须共地（Common Ground）。
2. 将开发板 SPI 控制器的 **串行数据输出（Serial Data Output，SDO）**引脚连接到灯带第一个 **集成电路（Integrated Circuit，IC）**的数据输入引脚。
3. 将 SPI 控制器的 **串行时钟（Serial Clock，SCLK）**引脚连接到灯带第一个 IC 的时钟输入引脚。
4. 将 5 V 电源接到灯带的 5 V 输入。

## 191.4\_WS2812接线

1. Zephyr 开发板与 LED 灯带共地。
2. 把开发板的灯带控制引脚连接到第一个 WS2812 IC 的数据输入。控制引脚可以是 **芯片间数字音频接口（Inter-IC Sound，I2S）**的 SDOUT 串行数据输出，也可以是 SPI 的 SDO，或 **通用输入输出（General-Purpose Input/Output，GPIO）**。
3. 灯带供电应使其 **输入输出（Input/Output，I/O）**电平与控制引脚信号兼容。

## 191.5\_thingy52说明

`thingy52` 集成了 **N沟道金属氧化物半导体晶体管（N-channel Metal-Oxide-Semiconductor Transistor，NMOS）**，可代替电平转换器。I2S 驱动可通过设备树（Devicetree）的 `out-active-low` 属性反转输出，以适应该电路。

详细配置见官方已有叠加文件 [`samples/drivers/led/led_strip/boards/thingy52_nrf52832.overlay`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led/led_strip/boards/thingy52_nrf52832.overlay)。

## 191.6\_构建与运行（Building and Running）

示例周期性更新灯带，可通过 `CONFIG_SAMPLE_LED_UPDATE_DELAY` 修改更新间隔，从而改变更新频率；可通过 `CONFIG_SAMPLE_LED_BRIGHTNESS` 调整每个 LED 的亮度。

随后构建并烧录应用。译注：在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行以下官方命令；将 `<board>` 替换为实际目标板。示例源码由官方仓库提供，west 生成构建产物，`west flash` 执行烧录。

```bash
west build -b <board> samples/drivers/led/led_strip
west flash
```

连接开发板的串行控制台（Serial Console）后，应看到类似下面的输出。OS 为 **操作系统（Operating System）**；保留原文启动日志中的历史版本：

```text
***** Booting Zephyr OS build v2.1.0-rc1-191-gd2466cdaf045 *****
[00:00:00.005,920] <inf> main: Found LED strip device WS2812
[00:00:00.005,950] <inf> main: Displaying pattern on strip
```

## 191.7\_参考资料（References）

- [WS2812数据手册](https://cdn-shop.adafruit.com/datasheets/WS2812.pdf)。
- [LPD8806数据手册](https://cdn-shop.adafruit.com/datasheets/lpd8806+english.pdf)。
- [APA102C数据手册](https://cdn-shop.adafruit.com/product-files/2477/APA102C-iPixelLED.pdf)。
- [原文标为74AHCT125的数据手册](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf)，链接文件名为 `74AHC125.pdf`，按官方原链接保留。
- [LED灯带结构讲解](https://littleanvil.com/journal/2020/4/16/led-strip-anatomy-explained)。
- [维基百科：LED灯带](https://en.wikipedia.org/wiki/LED_strip_light)。
- [原文推荐的WS2812时序文章](https://wp.josh.com/2014/05/13/ws2812-neopixels-are-not-so-finicky-once-you-get-to-know-them/)。

[LED灯带应用程序编程接口（Application Programming Interface，API）](P208_LED灯带公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/led/led_strip)

[上一章：IS31FL3733灯矩阵示例](P190_IS31FL3733灯矩阵示例.md) · [下一章：LP3943四色LED示例](P192_LP3943四色LED示例.md) · [返回大纲](大纲.md)
