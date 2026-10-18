---
id: learning.zephyr-docs.adc_reference.adcheadermcu-42
title: RenesasADCB常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-adc-b_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第42章\_RenesasADCB常量源码

原文：[renesas-adc-b_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/renesas-adc-b_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/renesas-adc-b.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P041_RenesasADCB常量参考.md)。

## 42.1\_原始可见源码

仅去除展示行号和行末空白，原定义、表达式及可见注释原样保留。此处是网页可见源码，不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_RENESAS_ADC_B_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_RENESAS_ADC_B_H_


#define RENESAS_ADC_B_CH0  0
#define RENESAS_ADC_B_CH1  1
#define RENESAS_ADC_B_CH2  2
#define RENESAS_ADC_B_CH3  3
#define RENESAS_ADC_B_CH4  4
#define RENESAS_ADC_B_CH5  5
#define RENESAS_ADC_B_CH6  6
#define RENESAS_ADC_B_CH7  7
#define RENESAS_ADC_B_CH8  8
#define RENESAS_ADC_B_CH9  9
#define RENESAS_ADC_B_CH10 10
#define RENESAS_ADC_B_CH11 11
#define RENESAS_ADC_B_CH12 12
#define RENESAS_ADC_B_CH13 13
#define RENESAS_ADC_B_CH14 14
#define RENESAS_ADC_B_CH15 15
#define RENESAS_ADC_B_CH16 16
#define RENESAS_ADC_B_CH17 17
#define RENESAS_ADC_B_CH18 18
#define RENESAS_ADC_B_CH19 19
#define RENESAS_ADC_B_CH20 20
#define RENESAS_ADC_B_CH21 21
#define RENESAS_ADC_B_CH22 22


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_RENESAS_ADC_B_H_ */
```

## 42.2\_注释与阅读说明

原页隐藏了Doxygen的文件说明及各物理输入通道说明，已在对应参考页翻译；23个选择宏及可见版权、许可证原样保留。

头文件保护（Header Guard）通过条件预处理避免重复包含。

---

[上一章：RenesasADCB常量参考](P041_RenesasADCB常量参考.md) · [下一章：ADS126x扩展头文件参考](P043_ADS126x扩展头文件参考.md) · [返回大纲](大纲.md)
