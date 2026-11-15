---
id: learning.zephyr-docs.adc_reference.adcheaderextra-12
title: GD32F3x0ADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc_2gd32f3x0_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第12章\_GD32F3x0ADC设备树常量源码

原文：[adc_2gd32f3x0_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc_2gd32f3x0_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器中 `zephyr/dt-bindings/adc/gd32f3x0.h` 的可见内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）含义见[对应参考页](P011_GD32F3x0ADC设备树常量参考.md)。

## 12.1\_原始可见源码

仅移除展示行号和行末空白；版权、许可证、预处理指令、宏名、数值和可见注释原样保留。此处保留网页可见源码，不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright 2022 BrainCo Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_GD32F3X0_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_GD32F3X0_H_

/*
 * ADC clock and prescaler definition refer from rcu_adc_clock_enum which
 * defined at GD32F3X0 RCU HAL.
 */
#define GD32_RCU_ADCCK_IRC28M_DIV2      0
#define GD32_RCU_ADCCK_IRC28M           1
#define GD32_RCU_ADCCK_APB2_DIV2        2
#define GD32_RCU_ADCCK_AHB_DIV3         3
#define GD32_RCU_ADCCK_APB2_DIV4        4
#define GD32_RCU_ADCCK_AHB_DIV5         5
#define GD32_RCU_ADCCK_APB2_DIV6        6
#define GD32_RCU_ADCCK_AHB_DIV7         7
#define GD32_RCU_ADCCK_APB2_DIV8        8
#define GD32_RCU_ADCCK_AHB_DIV9         9

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_GD32F3X0_H_ */
```

## 12.2\_注释与阅读说明

原注释译文：ADC时钟及预分频器（Prescaler）的定义参考了GD32F3X0复位与时钟单元（Reset and Clock Unit，RCU）硬件抽象层（Hardware Abstraction Layer，HAL）中的 `rcu_adc_clock_enum`。

`SPDX-License-Identifier: Apache-2.0` 及版权行保持原法律标识。头文件保护（Header Guard）通过条件预处理避免重复包含。

---

[上一章：GD32F3x0ADC设备树常量参考](P011_GD32F3x0ADC设备树常量参考.md) · [下一章：B91ADC设备树常量参考](P013_B91ADC设备树常量参考.md) · [返回大纲](大纲.md)
