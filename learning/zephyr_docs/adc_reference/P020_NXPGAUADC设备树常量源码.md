---
id: learning.zephyr-docs.adc_reference.adcheadernordic-20
title: NXPGAUADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp_00gau-adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第20章\_NXPGAUADC设备树常量源码

原文：[nxp_00gau-adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nxp_00gau-adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器中 `zephyr/dt-bindings/adc/nxp,gau-adc.h` 的可见内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P019_NXPGAUADC设备树常量参考.md)。

## 20.1\_原始可见源码

仅去除展示行号及行末空白，原版权、许可证、宏名称、数值、表达式和可见注释全部保留。源码浏览器可能隐藏文档注释，本页不声称是仓库原文件的逐字节副本。

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright 2022 NXP
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NXP_GAU_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NXP_GAU_ADC_H_

#include <zephyr/dt-bindings/adc/adc.h>

/* Channel Sources */
#define GAU_ADC_CH0 0
#define GAU_ADC_CH1 1
#define GAU_ADC_CH2 2
#define GAU_ADC_CH3 3
#define GAU_ADC_CH4 4
#define GAU_ADC_CH5 5
#define GAU_ADC_CH6 6
#define GAU_ADC_CH7 7
#define GAU_ADC_VBATS 8
#define GAU_ADC_VREF 9
#define GAU_ADC_DACA 10
#define GAU_ADC_DACB 11
#define GAU_ADC_VSSA 12
#define GAU_ADC_TEMPP 15

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NXP_GAU_ADC_H_ */
```

## 20.2\_注释与阅读说明

原注释Channel Sources译为“通道源”，其下14个宏定义输入选择编码。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：NXPGAUADC设备树常量参考](P019_NXPGAUADC设备树常量参考.md) · [下一章：SmartBondADC设备树常量参考](P021_SmartBondADC设备树常量参考.md) · [返回大纲](大纲.md)
