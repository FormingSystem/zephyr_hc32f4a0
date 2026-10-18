---
id: learning.zephyr-docs.adc_reference.adcheadernordic-19
title: NXPGAUADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp_00gau-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第19章\_NXPGAUADC设备树常量参考

原文：[nxp_00gau-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/nxp_00gau-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/nxp,gau-adc.h` 定义NXP GAU模数转换器（Analog-to-Digital Converter，ADC）的通道源（Channel Sources）常量。GAU保留原外设名称；原页列出14个宏（Macro），并包含[ADC通用设备树头文件](P001_ADC通用设备树常量参考.md)：

```c
#include <zephyr/dt-bindings/adc/adc.h>
```

## 19.1\_通道源常量

原页没有逐项解释性段落。表中中文为按标识符补充的译注，VBATS、VSSA、TEMPP等原节点拼写保留，不额外补出其测量比例或单位。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `GAU_ADC_CH0` | `0` | 输入通道（Input Channel）CH0 |
| `GAU_ADC_CH1` | `1` | 输入通道（Input Channel）CH1 |
| `GAU_ADC_CH2` | `2` | 输入通道（Input Channel）CH2 |
| `GAU_ADC_CH3` | `3` | 输入通道（Input Channel）CH3 |
| `GAU_ADC_CH4` | `4` | 输入通道（Input Channel）CH4 |
| `GAU_ADC_CH5` | `5` | 输入通道（Input Channel）CH5 |
| `GAU_ADC_CH6` | `6` | 输入通道（Input Channel）CH6 |
| `GAU_ADC_CH7` | `7` | 输入通道（Input Channel）CH7 |
| `GAU_ADC_VBATS` | `8` | VBATS电池电压相关输入 |
| `GAU_ADC_VREF` | `9` | 参考电压（Reference Voltage）输入 |
| `GAU_ADC_DACA` | `10` | 数模转换器A（Digital-to-Analog Converter A）相关输入 |
| `GAU_ADC_DACB` | `11` | 数模转换器B（Digital-to-Analog Converter B）相关输入 |
| `GAU_ADC_VSSA` | `12` | VSSA模拟地相关输入 |
| `GAU_ADC_TEMPP` | `15` | TEMPP温度相关输入 |

## 19.2\_编码范围

这些数值是通道源选择编码。原定义从VSSA的12跳到TEMPP的15，没有定义13、14；本译文保持这一空缺。完整可见定义和原注释见[源码页](P020_NXPGAUADC设备树常量源码.md)。

---

[上一章：NordicSAADC设备树常量源码](P018_NordicSAADC设备树常量源码.md) · [下一章：NXPGAUADC设备树常量源码](P020_NXPGAUADC设备树常量源码.md) · [返回大纲](大纲.md)
