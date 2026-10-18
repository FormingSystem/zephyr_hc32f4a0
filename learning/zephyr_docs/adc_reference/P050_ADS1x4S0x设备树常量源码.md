---
id: learning.zephyr-docs.adc_reference.adcheaderti-50
title: ADS1x4S0x设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x__adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第50章\_ADS1x4S0x设备树常量源码

原文：[ads1x4s0x__adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x__adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/ads1x4s0x_adc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P049_ADS1x4S0x设备树常量参考.md)。

## 50.1\_原始可见源码

仅去除展示行号及行末空白；版权、许可证、标识符、数值、函数签名、包含项和可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2023 SILA Embedded Solutions GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADS1X4S0X_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADS1X4S0X_ADC_H_

/*
 * These are the available data rates described as samples per second. They
 * can be used with the time unit ticks for the acquisition time.
 */
#define ADS1X4S0X_CONFIG_DR_2_5         0
#define ADS1X4S0X_CONFIG_DR_5           1
#define ADS1X4S0X_CONFIG_DR_10          2
#define ADS1X4S0X_CONFIG_DR_16_6        3
#define ADS1X4S0X_CONFIG_DR_20          4
#define ADS1X4S0X_CONFIG_DR_50          5
#define ADS1X4S0X_CONFIG_DR_60          6
#define ADS1X4S0X_CONFIG_DR_100         7
#define ADS1X4S0X_CONFIG_DR_200         8
#define ADS1X4S0X_CONFIG_DR_400         9
#define ADS1X4S0X_CONFIG_DR_800         10
#define ADS1X4S0X_CONFIG_DR_1000        11
#define ADS1X4S0X_CONFIG_DR_2000        12
#define ADS1X4S0X_CONFIG_DR_4000        13

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADS1X4S0X_ADC_H_ */
```

## 50.2\_注释与阅读说明

原可见注释译文：这些是以每秒采样数（Samples per Second，SPS）描述的可用数据率（Data Rates）。它们可以与采集时间（Acquisition Time）的ticks时间单位一起使用。编码与实际采样率的对应关系见参考页。

`SPDX-License-Identifier: Apache-2.0` 和版权行保留原法律标识。头文件保护（Header Guard）避免重复包含。

---

[上一章：ADS1x4S0x设备树常量参考](P049_ADS1x4S0x设备树常量参考.md) · [下一章：MCP356xR扩展头文件参考](P051_MCP356xR扩展头文件参考.md) · [返回大纲](大纲.md)
