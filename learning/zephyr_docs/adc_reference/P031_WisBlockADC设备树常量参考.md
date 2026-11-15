---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-31
title: WisBlockADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wisblock-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第31章\_WisBlockADC设备树常量参考

原文：[wisblock-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/wisblock-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/wisblock-adc.h` 定义WisBlock模数转换器（Analog-to-Digital Converter，ADC）的通道常量（Channel Constants）。本页翻译原文件的说明及9个宏（Macro）条目。

## 31.1\_通道常量

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `WISBLOCK_ADC_AIN0` | `0` | 模拟输入（Analog Input）0（AIN0） |
| `WISBLOCK_ADC_AIN1` | `1` | 模拟输入（Analog Input）1（AIN1） |
| `WISBLOCK_ADC_IO1` | `2` | 可选的、支持模拟功能的IO1（Optional Analog-Capable IO1） |
| `WISBLOCK_ADC_IO2` | `3` | 可选的、支持模拟功能的IO2（Optional Analog-Capable IO2） |
| `WISBLOCK_ADC_IO3` | `4` | 可选的、支持模拟功能的IO3（Optional Analog-Capable IO3） |
| `WISBLOCK_ADC_IO4` | `5` | 可选的、支持模拟功能的IO4（Optional Analog-Capable IO4） |
| `WISBLOCK_ADC_IO5` | `6` | 可选的、支持模拟功能的IO5（Optional Analog-Capable IO5） |
| `WISBLOCK_ADC_IO6` | `7` | 可选的、支持模拟功能的IO6（Optional Analog-Capable IO6） |
| `WISBLOCK_ADC_IO7` | `8` | 可选的、支持模拟功能的IO7（Optional Analog-Capable IO7） |

## 31.2\_可选模拟输入

AIN0、AIN1为模拟输入0、1；IO1至IO7在原文中均标为可选且支持模拟功能的输入。这里保留“可选”（Optional）条件，不把这些名字解释为每种WisBlock核心板都可用的ADC引脚。完整可见定义见[源码页](P032_WisBlockADC设备树常量源码.md)。

---

[上一章：SilabsSiWx91xADC设备树常量源码](P030_SilabsSiWx91xADC设备树常量源码.md) · [下一章：WisBlockADC设备树常量源码](P032_WisBlockADC设备树常量源码.md) · [返回大纲](大纲.md)
