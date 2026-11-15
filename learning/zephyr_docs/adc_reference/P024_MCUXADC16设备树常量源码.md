---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-24
title: MCUXADC16设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux-adc16_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第24章\_MCUXADC16设备树常量源码

原文：[mcux-adc16_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mcux-adc16_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/mcux-adc16.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P023_MCUXADC16设备树常量参考.md)。

## 24.1\_原始可见源码

仅移除展示行号和行末空白；原版权、许可证、名称、数值、表达式及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原仓库文件的逐字节副本。

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_ADC16_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_ADC16_H_

#define MCUX_ADC16_ACQUISITION_TIME_6CYCLE      (0x3)
#define MCUX_ADC16_ACQUISITION_TIME_10CYCLE     (0x2)
#define MCUX_ADC16_ACQUISITION_TIME_16CYCLE     (0x1)
#define MCUX_ADC16_ACQUISITION_TIME_24CYCLE     (0x0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_MCUX_ADC16_H_ */
```

## 24.2\_注释与阅读说明

原页没有额外的功能说明注释。4个采集时间宏的编码与周期数不同，具体对应关系见参考页。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：MCUXADC16设备树常量参考](P023_MCUXADC16设备树常量参考.md) · [下一章：MCUXLPADC设备树常量参考](P025_MCUXLPADC设备树常量参考.md) · [返回大纲](大纲.md)
