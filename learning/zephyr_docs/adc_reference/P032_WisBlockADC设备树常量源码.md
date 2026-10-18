---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-32
title: WisBlockADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wisblock-adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第32章\_WisBlockADC设备树常量源码

原文：[wisblock-adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/wisblock-adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/wisblock-adc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P031_WisBlockADC设备树常量参考.md)。

## 32.1\_原始可见源码

仅移除展示行号和行末空白；原版权、许可证、名称、数值、表达式及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2026 RAKwireless Technology Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_WISBLOCK_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_WISBLOCK_ADC_H_


#define WISBLOCK_ADC_AIN0 0
#define WISBLOCK_ADC_AIN1 1
#define WISBLOCK_ADC_IO1  2
#define WISBLOCK_ADC_IO2  3
#define WISBLOCK_ADC_IO3  4
#define WISBLOCK_ADC_IO4  5
#define WISBLOCK_ADC_IO5  6
#define WISBLOCK_ADC_IO6  7
#define WISBLOCK_ADC_IO7  8


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_WISBLOCK_ADC_H_ */
```

## 32.2\_注释与阅读说明

原页隐藏了Doxygen文档注释；参考页已完整翻译WisBlock ADC通道常量、AIN0／AIN1及可选模拟IO1至IO7的说明。此处保留网页实际展示的9个宏。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：WisBlockADC设备树常量参考](P031_WisBlockADC设备树常量参考.md) · [下一章：Infineon自主模拟SAR常量参考](P033_Infineon自主模拟SAR常量参考.md) · [返回大纲](大纲.md)
