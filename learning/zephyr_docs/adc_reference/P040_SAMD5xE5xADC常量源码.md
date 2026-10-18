---
id: learning.zephyr-docs.adc_reference.adcheadermcu-40
title: SAMD5xE5xADC常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第40章\_SAMD5xE5xADC常量源码

原文：[mchp__sam__d5x__e5x__adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__d5x__e5x__adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/mchp_sam_d5x_e5x_adc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P039_SAMD5xE5xADC常量参考.md)。

原源码浏览页隐藏了文件头的Doxygen版权与许可证注释；以下声明从对应官方文件参考页照录，单独保留，不伪装成源码浏览页可见行：

```text
Copyright (c) 2025-2026 Microchip Technology Inc.
SPDX-License-Identifier: Apache-2.0
```

## 40.1\_原始可见源码

仅去除展示行号和行末空白，原定义、表达式及可见注释原样保留。此处是网页可见源码，不声称是原始仓库文件的逐字节副本。

```c



#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCHP_SAM_D5X_E5X_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCHP_SAM_D5X_E5X_ADC_H_

/* External analog inputs */
#define MCHP_ADC_AIN0  0x00
#define MCHP_ADC_AIN1  0x01
#define MCHP_ADC_AIN2  0x02
#define MCHP_ADC_AIN3  0x03
#define MCHP_ADC_AIN4  0x04
#define MCHP_ADC_AIN5  0x05
#define MCHP_ADC_AIN6  0x06
#define MCHP_ADC_AIN7  0x07
#define MCHP_ADC_AIN8  0x08
#define MCHP_ADC_AIN9  0x09
#define MCHP_ADC_AIN10 0x0A
#define MCHP_ADC_AIN11 0x0B
#define MCHP_ADC_AIN12 0x0C
#define MCHP_ADC_AIN13 0x0D
#define MCHP_ADC_AIN14 0x0E
#define MCHP_ADC_AIN15 0x0F

/* Internal ADC sources */
#define MCHP_ADC_SCALEDCOREVCC 0x18
#define MCHP_ADC_SCALEDVBAT    0x19
#define MCHP_ADC_SCALEDIOVCC   0x1A
#define MCHP_ADC_BANDGAP       0x1B
#define MCHP_ADC_PTAT          0x1C
#define MCHP_ADC_CTAT          0x1D
#define MCHP_ADC_DAC0          0x1E

#define MCHP_ADC_MUXPOS_VALID_MASK (GENMASK(0x1E, 0x18) | GENMASK(0x0F, 0x00))

#define MCHP_ADC_MUXNEG_VALID_MASK (BIT(0x18) | GENMASK(0x07, 0x00))

/* ADC reference selection */
#define MCHP_ADC_REF_INTREF  0x00
#define MCHP_ADC_REF_INTVCC0 0x02
#define MCHP_ADC_REF_INTVCC1 0x03
#define MCHP_ADC_REF_AREFA   0x04
#define MCHP_ADC_REF_AREFB   0x05
#define MCHP_ADC_REF_AREFC   0x06

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCHP_SAM_D5X_E5X_ADC_H_ */
```

## 40.2\_注释与阅读说明

可见注释依次译为“外部模拟输入”（External Analog Inputs）、“内部ADC源”（Internal ADC Sources）与“ADC参考选择”（ADC Reference Selection）。源码页隐藏的逐宏说明已在对应参考页翻译。

头文件保护（Header Guard）通过条件预处理避免重复包含。

---

[上一章：SAMD5xE5xADC常量参考](P039_SAMD5xE5xADC常量参考.md) · [下一章：RenesasADCB常量参考](P041_RenesasADCB常量参考.md) · [返回大纲](大纲.md)
