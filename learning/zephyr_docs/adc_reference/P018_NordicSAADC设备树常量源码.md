---
id: learning.zephyr-docs.adc_reference.adcheadernordic-18
title: NordicSAADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-saadc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第18章\_NordicSAADC设备树常量源码

原文：[nrf-saadc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nrf-saadc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器中 `zephyr/dt-bindings/adc/nrf-saadc.h` 的可见内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P017_NordicSAADC设备树常量参考.md)。

## 18.1\_原始可见源码

仅去除展示行号及行末空白，原版权、许可证、宏名称、数值、表达式和可见注释全部保留。源码浏览器可能隐藏文档注释，本页不声称是仓库原文件的逐字节副本。

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Nordic Semiconductor ASA
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_SAADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_SAADC_H_

#define NRF_SAADC_AIN0 0
#define NRF_SAADC_AIN1 1
#define NRF_SAADC_AIN2 2
#define NRF_SAADC_AIN3 3
#define NRF_SAADC_AIN4 4
#define NRF_SAADC_AIN5 5
#define NRF_SAADC_AIN6 6
#define NRF_SAADC_AIN7 7
#define NRF_SAADC_AIN8 8
#define NRF_SAADC_AIN9 9
#define NRF_SAADC_AIN10 10
#define NRF_SAADC_AIN11 11
#define NRF_SAADC_AIN12 12
#define NRF_SAADC_AIN13 13

#define NRF_SAADC_GND  (NRF_SAADC_AIN_VDD_SHIM_OFFSET - 1)

#define NRF_SAADC_AIN_TEST_SHIM_OFFSET 64
#define NRF_SAADC_AVSS                (NRF_SAADC_AIN_TEST_SHIM_OFFSET + 0)

#define NRF_SAADC_AIN_VDD_SHIM_OFFSET 128
#define NRF_SAADC_VDD                 (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 0)
#define NRF_SAADC_VDDDIV2             (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 1)
#define NRF_SAADC_AVDD                (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 2)
#define NRF_SAADC_DVDD                (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 3)
#define NRF_SAADC_VDDHDIV5            (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 4)
#define NRF_SAADC_VDDL                (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 5)
#define NRF_SAADC_DECB                (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 6)
#define NRF_SAADC_VSS                 (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 7)
#define NRF_SAADC_VDDAO3V0            (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 8)
#define NRF_SAADC_VDDAO1V8            (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 9)
#define NRF_SAADC_VDDAO0V8            (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 10)
#define NRF_SAADC_VDDRF               (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 11)
#define NRF_SAADC_VBAT                (NRF_SAADC_AIN_VDD_SHIM_OFFSET + 12)
#define NRF_SAADC_AIN_DISABLED        255 /* UINT8_MAX */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_NRF_SAADC_H_ */
```

## 18.2\_注释与阅读说明

原源码浏览页隐藏了GND单端模式、测试输入偏移及AVSS的Doxygen说明注释；这些说明及两个原始设备树示例已完整翻译到对应参考页。`UINT8_MAX` 注释表示8位无符号整数的最大值。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：NordicSAADC设备树常量参考](P017_NordicSAADC设备树常量参考.md) · [下一章：NXPGAUADC设备树常量参考](P019_NXPGAUADC设备树常量参考.md) · [返回大纲](大纲.md)
