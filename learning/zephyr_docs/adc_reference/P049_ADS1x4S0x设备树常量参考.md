---
id: learning.zephyr-docs.adc_reference.adcheaderti-49
title: ADS1x4S0x设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x__adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第49章\_ADS1x4S0x设备树常量参考

原文：[ads1x4s0x__adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x__adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/ads1x4s0x_adc.h` 定义ADS1x4s0x模数转换器（Analog-to-Digital Converter，ADC）的可用数据率（Data Rate）常量。原文件参考页列出14个宏（Macro）；[源码页](P050_ADS1x4S0x设备树常量源码.md)的注释说明，这些数据率以每秒采样数（Samples per Second，SPS）描述，可与采集时间（Acquisition Time）的ticks时间单位搭配使用。

## 49.1\_数据率与编码

| 宏 | 原始编码 | 数据率（SPS） |
| --- | --- | --- |
| `ADS1X4S0X_CONFIG_DR_2_5` | `0` | 2.5 |
| `ADS1X4S0X_CONFIG_DR_5` | `1` | 5 |
| `ADS1X4S0X_CONFIG_DR_10` | `2` | 10 |
| `ADS1X4S0X_CONFIG_DR_16_6` | `3` | 16.6 |
| `ADS1X4S0X_CONFIG_DR_20` | `4` | 20 |
| `ADS1X4S0X_CONFIG_DR_50` | `5` | 50 |
| `ADS1X4S0X_CONFIG_DR_60` | `6` | 60 |
| `ADS1X4S0X_CONFIG_DR_100` | `7` | 100 |
| `ADS1X4S0X_CONFIG_DR_200` | `8` | 200 |
| `ADS1X4S0X_CONFIG_DR_400` | `9` | 400 |
| `ADS1X4S0X_CONFIG_DR_800` | `10` | 800 |
| `ADS1X4S0X_CONFIG_DR_1000` | `11` | 1000 |
| `ADS1X4S0X_CONFIG_DR_2000` | `12` | 2000 |
| `ADS1X4S0X_CONFIG_DR_4000` | `13` | 4000 |

## 49.2\_采集时间单位

本文件把数据率选择编码用于采集时间的ticks单位；通用单位宏 `ADC_ACQ_TIME_TICKS` 与时间编码表达式见[ADC通用常量](P001_ADC通用设备树常量参考.md)。译注：原始编码0至13不是采样率本身，例如 `ADS1X4S0X_CONFIG_DR_2_5` 的编码为0，表示的数据率为2.5 SPS，不能将0解释为停止采样。

---

[上一章：ADS1x4S0x扩展头文件源码](P048_ADS1x4S0x扩展头文件源码.md) · [下一章：ADS1x4S0x设备树常量源码](P050_ADS1x4S0x设备树常量源码.md) · [返回大纲](大纲.md)
