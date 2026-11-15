---
id: learning.zephyr-docs.hardware.adcdevice-4
title: WisBlock_ADC通道
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第471章\_WisBlock_ADC通道

原文：[group__wisblock-adc](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html)。读取日期：2026-10-13，`latest`。

## 471.1\_用途与头文件

本页定义 WisBlock Core 模块引出的**模数转换器（Analog-to-Digital Converter，ADC）**通道常量。AIN 表示模拟输入（Analog Input），IO 表示输入输出（Input/Output）引脚标识。

```c
#include <zephyr/dt-bindings/adc/wisblock-adc.h>
```

## 471.2\_通道常量

| 宏 | 值 | 含义 |
| --- | --- | --- |
| [`WISBLOCK_ADC_AIN0`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#ga8d51dfb72aaa31aa544c55163904675e) | `0` | 模拟输入 0（AIN0） |
| [`WISBLOCK_ADC_AIN1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#gace27d9fde144dc553f4d095e6d5a5a09) | `1` | 模拟输入 1（AIN1） |
| [`WISBLOCK_ADC_IO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#ga054acb787bdc4309cd6252b1bc5eda27) | `2` | 可选的具有模拟能力的 IO1 |
| [`WISBLOCK_ADC_IO2`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#ga2815653bea4aa9b06290722cf1cc298d) | `3` | 可选的具有模拟能力的 IO2 |
| [`WISBLOCK_ADC_IO3`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#gaf7a866ce0060b405c4259f06f40d1055) | `4` | 可选的具有模拟能力的 IO3 |
| [`WISBLOCK_ADC_IO4`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#gaff967a1b17f3e944e630bd668717ea5b) | `5` | 可选的具有模拟能力的 IO4 |
| [`WISBLOCK_ADC_IO5`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#ga213a36c69e8e3d904a8beb000e2f6bf5) | `6` | 可选的具有模拟能力的 IO5 |
| [`WISBLOCK_ADC_IO6`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#gaba251af1a7070abb04331320c93fd151) | `7` | 可选的具有模拟能力的 IO6 |
| [`WISBLOCK_ADC_IO7`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-adc.html#ga744ea4bf827a84a473a3760c16a33a75) | `8` | 可选的具有模拟能力的 IO7 |

译注：原文对 IO1—IO7 均使用“可选”（Optional）；这些常量的存在不表示每个 WisBlock Core 模块都提供所有对应的模拟输入。


---

[上一章：LMP90xxx扩展接口](P470_LMP90xxx扩展接口.md) · [下一章：ADS126X驱动接口](P472_ADS126X驱动接口.md) · [返回大纲](大纲.md)
