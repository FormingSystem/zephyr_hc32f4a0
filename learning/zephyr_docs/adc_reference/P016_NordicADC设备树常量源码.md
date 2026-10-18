---
id: learning.zephyr-docs.adc_reference.adcheadernordic-16
title: NordicADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第16章\_NordicADC设备树常量源码

原文：[nrf-adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nrf-adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器中 `zephyr/dt-bindings/adc/nrf-adc.h` 的可见内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P015_NordicADC设备树常量参考.md)。

## 16.1\_原始可见源码

仅去除展示行号及行末空白，原版权、许可证、宏名称、数值、表达式和可见注释全部保留。源码浏览器可能隐藏文档注释，本页不声称是仓库原文件的逐字节副本。

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2022 Nordic Semiconductor ASA
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_ADC_H_

#include <zephyr/dt-bindings/dt-util.h>

#define NRF_ADC_AIN0 BIT(0)
#define NRF_ADC_AIN1 BIT(1)
#define NRF_ADC_AIN2 BIT(2)
#define NRF_ADC_AIN3 BIT(3)
#define NRF_ADC_AIN4 BIT(4)
#define NRF_ADC_AIN5 BIT(5)
#define NRF_ADC_AIN6 BIT(6)
#define NRF_ADC_AIN7 BIT(7)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_ADC_H_ */
```

## 16.2\_注释与阅读说明

原页没有额外的功能说明注释。8个模拟输入宏使用 `BIT(n)` 位值（Bit Value），原表达式不改写成序号。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：NordicADC设备树常量参考](P015_NordicADC设备树常量参考.md) · [下一章：NordicSAADC设备树常量参考](P017_NordicSAADC设备树常量参考.md) · [返回大纲](大纲.md)
