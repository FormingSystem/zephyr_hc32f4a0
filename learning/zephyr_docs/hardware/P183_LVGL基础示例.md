---
id: learning.zephyr-docs.hardware.cfbsamp-3
title: LVGL基础示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/display/lvgl/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="lvgl"></a>

# 第183章\_LVGL基础示例

原文：[LVGL basic sample](https://docs.zephyrproject.org/latest/samples/subsys/display/lvgl/README.html)。读取日期：2026-10-13，`latest`。

## 183.1\_概述（Overview）

本示例使用图形库 LVGL，在屏幕中央显示“Hello World”，并在底部显示一个每秒递增的计数器。根据开发板上可用的输入设备，程序还会显示其他 **界面控件（Widget）**，启用相应交互。

**指针（Pointer）：**如果开发板具有触摸面板控制器，通过设备树兼容标识 [`zephyr,lvgl-pointer-input`](../input_touch_lvgl_gesture_binding_reference/P020_zephyr_lvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input) 接入，则在屏幕中央显示按钮控件（Button Widget）；否则显示标签控件（Label Widget）。

**按钮（Button）：**按钮伪设备（Pseudo Device）[`zephyr,lvgl-button-input`](../input_touch_lvgl_gesture_binding_reference/P017_zephyr_lvgl-button-input.md#std-dtcompatible-zephyr-lvgl-button-input) 将按下/释放动作映射为屏幕上的特定坐标。在本示例中，该坐标位于屏幕中央。

**编码器（Encoder）：**编码器伪设备 [`zephyr,lvgl-encoder-input`](../input_touch_lvgl_gesture_binding_reference/P018_zephyr_lvgl-encoder-input.md#std-dtcompatible-zephyr-lvgl-encoder-input) 用于在控件之间导航并编辑其值。如果开发板包含编码器，示例会显示一个可编辑的圆弧控件（Arc Widget）。

**键盘（Keypad）：**键盘伪设备 [`zephyr,lvgl-keypad-input`](../input_touch_lvgl_gesture_binding_reference/P019_zephyr_lvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input) 用于移动焦点（Focus Shifting），也可在文本区域等可编辑控件内输入字符。如果开发板具有键盘设备，示例会在屏幕底部显示按钮矩阵（Button Matrix），演示焦点切换。

## 183.2\_要求（Requirements）

可以使用显示扩展板（Display Shield），配合已为相应连接器提供配置的开发板。例如下列组合；其中 TFT 指 **薄膜晶体管（Thin-Film Transistor）**显示技术。

| 显示扩展板 | 开发板 |
| --- | --- |
| [Adafruit 2.8英寸TFT触摸扩展板v2](https://docs.zephyrproject.org/latest/boards/shields/adafruit_2_8_tft_touch_v2/doc/index.html#adafruit-2-8-tft-touch-v2) | [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)。 |
| [带Arduino适配器的Buydisplay 2.8英寸TFT触摸扩展板](https://docs.zephyrproject.org/latest/boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.html#buydisplay-2-8-tft-touch-arduino) | nRF52840 DK。 |
| [SSD1306 128×64或128×32像素通用扩展板](https://docs.zephyrproject.org/latest/boards/shields/ssd1306/doc/index.html#ssd1306-128-shield) | [FRDM-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)。 |
| [Seeed Studio XIAO圆形显示扩展板](https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_round_display/doc/index.html#seeed-xiao-round-display) | [XIAO BLE (Sense)](https://docs.zephyrproject.org/latest/boards/seeed/xiao_ble/doc/index.html#xiao_ble)。 |

也可使用集成显示器的开发板：

- [ESP-WROVER-KIT](https://docs.zephyrproject.org/latest/boards/espressif/esp_wrover_kit/doc/index.html#esp_wrover_kit)。
- [Adafruit Feather ESP32S3 TFT](https://docs.zephyrproject.org/latest/boards/adafruit/feather_esp32s3_tft/doc/index.html#adafruit_feather_esp32s3_tft)。

不使用真实显示器时，可在 [native_sim原生仿真目标](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)中使用 **简单直接媒体层第二版（Simple DirectMedia Layer 2，SDL2）**模拟显示环境。

原文还列出另外两种组合：

- [MIMXRT1050-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1050_evk/doc/index.html#mimxrt1050_evk) 与 RK043FN02H-CT 显示面板。
- [MIMXRT1060-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1060_evk/doc/index.html#mimxrt1060_evk) 与 RK043FN02H-CT 显示面板。

## 183.3\_构建与运行（Building and Running）

为 nRF52840 DK 构建的例子如下。译注：以下命令在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行；示例由官方仓库提供，west 生成构建产物，`west flash` 将固件烧录到开发板。

```bash
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield adafruit_2_8_tft_touch_v2 samples/subsys/display/lvgl
west flash
```

为 [`native_sim`](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 构建并运行：

```bash
# From the root of the zephyr repository
west build -b native_sim samples/subsys/display/lvgl
west build -t run
```

如果构建主机是 64 位机器，也可以把上一条构建命令中的目标板参数替换为 `native_sim/native/64`。

## 183.4\_参考资料（References）

1. [SDL官方项目](https://www.libsdl.org)。
2. [RK043FN02H-CT液晶面板资料](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/4.3-lcd-panel:RK043FN02H-CT)。

相关 **应用程序编程接口（Application Programming Interface，API）**：[显示接口](P214_显示公共接口.md)、[输入接口](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)。[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/display/lvgl)。

[上一章：字符帧缓冲命令行示例](P182_字符帧缓冲命令行示例.md) · [下一章：单色字符帧缓冲接口](P184_单色字符帧缓冲接口.md) · [返回大纲](大纲.md)
