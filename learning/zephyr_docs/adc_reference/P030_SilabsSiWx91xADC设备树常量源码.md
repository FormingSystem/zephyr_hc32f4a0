---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-30
title: SilabsSiWx91xADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-siwx91x-adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第30章\_SilabsSiWx91xADC设备树常量源码

原文：[silabs-siwx91x-adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/silabs-siwx91x-adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/silabs-siwx91x-adc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P029_SilabsSiWx91xADC设备树常量参考.md)。

## 30.1\_原始可见源码

仅移除展示行号和行末空白；原版权、许可证、名称、数值、表达式及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2025 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SILABS_SIWX91X_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SILABS_SIWX91X_ADC_H_

/*
 * These macros define the positive input selection values used in
 * zephyr,input-positive  for the SiWx91x ADC driver to map GPIO
 * pins to ADC channels.
 *
 * Mapping:
 * - ULP GPIO (0-15): Ultra Low Power GPIO pins
 * - HP GPIO (25-30): High Power GPIO pins
 *
 * Usage in device tree:
 * @code{.dts}
 *   zephyr,input-positive = <SIWX91X_ADC_INPUT_ULP4>;  // Maps to ULP4 pin
 * @endcode
 *
 * Note: Pin configuration (pinctrl) must be set separately in device tree
 *       to enable analog mode on the GPIO pin.
 */

#define SIWX91X_ADC_INPUT_ULP0      0
#define SIWX91X_ADC_INPUT_ULP2      1
#define SIWX91X_ADC_INPUT_ULP4      2
#define SIWX91X_ADC_INPUT_ULP6      3
#define SIWX91X_ADC_INPUT_ULP8      4
#define SIWX91X_ADC_INPUT_ULP10     5
#define SIWX91X_ADC_INPUT_HP25      6
#define SIWX91X_ADC_INPUT_HP27      7
#define SIWX91X_ADC_INPUT_HP29      8
#define SIWX91X_ADC_INPUT_ULP1      10
#define SIWX91X_ADC_INPUT_ULP3      11
#define SIWX91X_ADC_INPUT_ULP5      12
#define SIWX91X_ADC_INPUT_ULP11     13
#define SIWX91X_ADC_INPUT_ULP9      14
#define SIWX91X_ADC_INPUT_ULP7      15
#define SIWX91X_ADC_INPUT_HP26      16
#define SIWX91X_ADC_INPUT_HP28      17
#define SIWX91X_ADC_INPUT_HP30      18

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SILABS_SIWX91X_ADC_H_ */
```

## 30.2\_注释与阅读说明

原注释译文：这些宏定义SiWx91x ADC驱动在 `zephyr,input-positive` 中使用的正输入选择值，用于将GPIO引脚映射到ADC通道。ULP GPIO（0至15）为超低功耗GPIO（Ultra Low Power GPIO）；HP GPIO（25至30）为高功率GPIO（High Power GPIO）。原设备树示例把正输入映射到ULP4。必须单独配置引脚控制（Pin Control，pinctrl），才能启用GPIO的模拟模式（Analog Mode）。GPIO为通用输入输出（General-Purpose Input/Output）。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：SilabsSiWx91xADC设备树常量参考](P029_SilabsSiWx91xADC设备树常量参考.md) · [下一章：WisBlockADC设备树常量参考](P031_WisBlockADC设备树常量参考.md) · [返回大纲](大纲.md)
