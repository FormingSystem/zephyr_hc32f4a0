---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-23
title: MCUXADC16设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux-adc16_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第23章\_MCUXADC16设备树常量参考

原文：[mcux-adc16_8h](https://docs.zephyrproject.org/latest/doxygen/html/mcux-adc16_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/mcux-adc16.h` 定义MCUX ADC16模数转换器（Analog-to-Digital Converter，ADC）的采集时间（Acquisition Time）选择宏（Macro）。原页只列出4个定义，中文释义按宏名称补充，原始编码保留。

## 23.1\_采集周期选择

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `MCUX_ADC16_ACQUISITION_TIME_6CYCLE` | `(0x3)` | 采集时间为6个周期（Cycles） |
| `MCUX_ADC16_ACQUISITION_TIME_10CYCLE` | `(0x2)` | 采集时间为10个周期（Cycles） |
| `MCUX_ADC16_ACQUISITION_TIME_16CYCLE` | `(0x1)` | 采集时间为16个周期（Cycles） |
| `MCUX_ADC16_ACQUISITION_TIME_24CYCLE` | `(0x0)` | 采集时间为24个周期（Cycles） |

## 23.2\_编码与周期数

原始编码 `0x3`、`0x2`、`0x1`、`0x0` 分别对应6、10、16、24个周期。不能把编码值直接当作周期数，也不能把宏值改为其名称中的周期数。原页没有额外的头文件包含项或函数；完整定义见[源码页](P024_MCUXADC16设备树常量源码.md)。

---

[上一章：SmartBondADC设备树常量源码](P022_SmartBondADC设备树常量源码.md) · [下一章：MCUXADC16设备树常量源码](P024_MCUXADC16设备树常量源码.md) · [返回大纲](大纲.md)
