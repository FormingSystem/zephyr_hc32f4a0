---
id: learning.zephyr-docs.adc_reference.adcheaderextra-11
title: GD32F3x0ADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc_2gd32f3x0_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第11章\_GD32F3x0ADC设备树常量参考

原文：[adc_2gd32f3x0_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc_2gd32f3x0_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/gd32f3x0.h` 定义GD32F3x0模数转换器（Analog-to-Digital Converter，ADC）的时钟和预分频（Prescaler）选择。设备树（Devicetree）使用的宏（Macro）定义来源于GD32F3X0复位与时钟单元（Reset and Clock Unit，RCU）硬件抽象层（Hardware Abstraction Layer，HAL）中的 `rcu_adc_clock_enum`，这是[原源码注释](P012_GD32F3x0ADC设备树常量源码.md)给出的来源关系。

## 11.1\_时钟源与分频编码

IRC28M表示内部RC振荡器（Internal RC Oscillator）的28 MHz时钟；APB2为高级外设总线2（Advanced Peripheral Bus 2），AHB为高级高性能总线（Advanced High-performance Bus）。表中中文选择说明按宏名称给出，原始值是选择编码。

| 宏 | 原始值 | 中文释义 |
| --- | --- | --- |
| `GD32_RCU_ADCCK_IRC28M_DIV2` | `0` | IRC28M时钟2分频 |
| `GD32_RCU_ADCCK_IRC28M` | `1` | IRC28M时钟，不分频 |
| `GD32_RCU_ADCCK_APB2_DIV2` | `2` | APB2时钟2分频 |
| `GD32_RCU_ADCCK_AHB_DIV3` | `3` | AHB时钟3分频 |
| `GD32_RCU_ADCCK_APB2_DIV4` | `4` | APB2时钟4分频 |
| `GD32_RCU_ADCCK_AHB_DIV5` | `5` | AHB时钟5分频 |
| `GD32_RCU_ADCCK_APB2_DIV6` | `6` | APB2时钟6分频 |
| `GD32_RCU_ADCCK_AHB_DIV7` | `7` | AHB时钟7分频 |
| `GD32_RCU_ADCCK_APB2_DIV8` | `8` | APB2时钟8分频 |
| `GD32_RCU_ADCCK_AHB_DIV9` | `9` | AHB时钟9分频 |

## 11.2\_使用范围

`DIV2`、`DIV3` 等后缀表示除数，原始值列则是设备树传递的编码，两者不能混用。原页没有头文件包含项、函数或更多宏说明；完整定义见[源码页](P012_GD32F3x0ADC设备树常量源码.md)。具体ADC节点的时钟配置要求见[GD32绑定](../hardware/P844_GD32模数转换器绑定.md)。

---

[上一章：MCP356xR设备树常量源码](P010_MCP356xR设备树常量源码.md) · [下一章：GD32F3x0ADC设备树常量源码](P012_GD32F3x0ADC设备树常量源码.md) · [返回大纲](大纲.md)
