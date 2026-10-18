---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-26
title: MCUXLPADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux-lpadc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第26章\_MCUXLPADC设备树常量源码

原文：[mcux-lpadc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mcux-lpadc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/mcux-lpadc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P025_MCUXLPADC设备树常量参考.md)。

## 26.1\_原始可见源码

仅移除展示行号和行末空白；原版权、许可证、名称、数值、表达式及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原仓库文件的逐字节副本。

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright 2023,2025 NXP
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_LPADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_LPADC_H_

#define MCUX_LPADC_CH0A (0x0)
#define MCUX_LPADC_CH0B (0x20)
#define MCUX_LPADC_CH1A (0x1)
#define MCUX_LPADC_CH1B (0x21)
#define MCUX_LPADC_CH2A (0x2)
#define MCUX_LPADC_CH2B (0x22)
#define MCUX_LPADC_CH3A (0x3)
#define MCUX_LPADC_CH3B (0x23)
#define MCUX_LPADC_CH4A (0x4)
#define MCUX_LPADC_CH4B (0x24)
#define MCUX_LPADC_CH5A (0x5)
#define MCUX_LPADC_CH5B (0x25)
#define MCUX_LPADC_CH6A (0x6)
#define MCUX_LPADC_CH6B (0x26)
#define MCUX_LPADC_CH7A (0x7)
#define MCUX_LPADC_CH7B (0x27)
#define MCUX_LPADC_CH8A (0x8)
#define MCUX_LPADC_CH8B (0x28)
#define MCUX_LPADC_CH9A (0x9)
#define MCUX_LPADC_CH9B (0x29)
#define MCUX_LPADC_CH10A (0x0A)
#define MCUX_LPADC_CH10B (0x2A)
#define MCUX_LPADC_CH11A (0x0B)
#define MCUX_LPADC_CH11B (0x2B)
#define MCUX_LPADC_CH12A (0x0C)
#define MCUX_LPADC_CH12B (0x2C)
#define MCUX_LPADC_CH13A (0x0D)
#define MCUX_LPADC_CH13B (0x2D)
#define MCUX_LPADC_CH14A (0x0E)
#define MCUX_LPADC_CH14B (0x2E)
#define MCUX_LPADC_CH15A (0x0F)
#define MCUX_LPADC_CH15B (0x2F)
#define MCUX_LPADC_CH16A (0x10)
#define MCUX_LPADC_CH16B (0x30)
#define MCUX_LPADC_CH17A (0x11)
#define MCUX_LPADC_CH17B (0x31)
#define MCUX_LPADC_CH18A (0x12)
#define MCUX_LPADC_CH18B (0x32)
#define MCUX_LPADC_CH19A (0x13)
#define MCUX_LPADC_CH19B (0x33)
#define MCUX_LPADC_CH20A (0x14)
#define MCUX_LPADC_CH20B (0x34)
#define MCUX_LPADC_CH21A (0x15)
#define MCUX_LPADC_CH21B (0x35)
#define MCUX_LPADC_CH22A (0x16)
#define MCUX_LPADC_CH22B (0x36)
#define MCUX_LPADC_CH23A (0x17)
#define MCUX_LPADC_CH23B (0x37)
#define MCUX_LPADC_CH24A (0x18)
#define MCUX_LPADC_CH24B (0x38)
#define MCUX_LPADC_CH25A (0x19)
#define MCUX_LPADC_CH25B (0x39)
#define MCUX_LPADC_CH26A (0x1A)
#define MCUX_LPADC_CH26B (0x3A)
#define MCUX_LPADC_CH27A (0x1B)
#define MCUX_LPADC_CH27B (0x3B)
#define MCUX_LPADC_CH28A (0x1C)
#define MCUX_LPADC_CH28B (0x3C)
#define MCUX_LPADC_CH29A (0x1D)
#define MCUX_LPADC_CH29B (0x3D)
#define MCUX_LPADC_CH30A (0x1E)
#define MCUX_LPADC_CH30B (0x3E)
#define MCUX_LPADC_CH31A (0x1F)
#define MCUX_LPADC_CH31B (0x3F)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_LPADC_H_ */
```

## 26.2\_注释与阅读说明

原页没有额外的功能说明注释。全部64个通道A／B侧选择宏按原顺序保留。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：MCUXLPADC设备树常量参考](P025_MCUXLPADC设备树常量参考.md) · [下一章：SilabsADC设备树常量参考](P027_SilabsADC设备树常量参考.md) · [返回大纲](大纲.md)
