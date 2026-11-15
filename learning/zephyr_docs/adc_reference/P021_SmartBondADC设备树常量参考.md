---
id: learning.zephyr-docs.adc_reference.adcheadernordic-21
title: SmartBondADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第21章\_SmartBondADC设备树常量参考

原文：[smartbond-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/smartbond-adc.h` 定义SmartBond模数转换器（Analog-to-Digital Converter，ADC）的输入常量，分为通用ADC（General-Purpose ADC，GPADC）与Σ-Δ ADC（Sigma-Delta ADC，SDADC）两组。文件包含设备树（Devicetree）辅助头文件：

```c
#include <zephyr/dt-bindings/dt-util.h>
```

原参考页列出22个宏（Macro）。下文把[源码页](P022_SmartBondADC设备树常量源码.md)中的属性适用范围注释一并翻译，表内中文输入释义为帮助阅读宏名而补充的译注。

## 21.1\_GPADC正输入常量

原源码注释说明：本组用于设备树 `zephyr,input-positive` 正输入属性。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `SMARTBOND_GPADC_P1_09` | `0` | 引脚P1_09输入 |
| `SMARTBOND_GPADC_P0_25` | `1` | 引脚P0_25输入 |
| `SMARTBOND_GPADC_P0_08` | `2` | 引脚P0_08输入 |
| `SMARTBOND_GPADC_P0_09` | `3` | 引脚P0_09输入 |
| `SMARTBOND_GPADC_VDD` | `4` | VDD电源输入 |
| `SMARTBOND_GPADC_V30` | `5` | V30电源输入 |
| `SMARTBOND_GPADC_VBAT` | `8` | 电池电压（Battery Voltage，VBAT）输入 |
| `SMARTBOND_GPADC_VSSA` | `9` | VSSA模拟地输入 |
| `SMARTBOND_GPADC_P1_13` | `16` | 引脚P1_13输入 |
| `SMARTBOND_GPADC_P1_12` | `17` | 引脚P1_12输入 |
| `SMARTBOND_GPADC_P1_18` | `18` | 引脚P1_18输入 |
| `SMARTBOND_GPADC_P1_19` | `19` | 引脚P1_19输入 |
| `SMARTBOND_GPADC_TEMP` | `20` | 温度（Temperature）输入 |

## 21.2\_SDADC输入常量

原源码注释说明：P1_09至P1_22这8个引脚选择可用于 `zephyr,input-positive` 正输入或 `zephyr,input-negative` 负输入属性；**VBAT选择仅能用于正输入属性**。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `SMARTBOND_SDADC_P1_09` | `0` | 引脚P1_09输入 |
| `SMARTBOND_SDADC_P0_25` | `1` | 引脚P0_25输入 |
| `SMARTBOND_SDADC_P0_08` | `2` | 引脚P0_08输入 |
| `SMARTBOND_SDADC_P0_09` | `3` | 引脚P0_09输入 |
| `SMARTBOND_SDADC_P1_14` | `4` | 引脚P1_14输入 |
| `SMARTBOND_SDADC_P1_20` | `5` | 引脚P1_20输入 |
| `SMARTBOND_SDADC_P1_21` | `6` | 引脚P1_21输入 |
| `SMARTBOND_SDADC_P1_22` | `7` | 引脚P1_22输入 |
| `SMARTBOND_SDADC_VBAT` | `8` | 电池电压（Battery Voltage，VBAT）输入；**仅限正输入属性** |

## 21.3\_两组常量的使用边界

两组宏分别属于GPADC和SDADC，不能仅因为数值相同就互换。特别是GPADC的VDD、V30、VSSA、TEMP以及第二组VBAT的属性限制，应按对应外设使用。原页没有进一步给出输入电压范围或分压系数。

---

[上一章：NXPGAUADC设备树常量源码](P020_NXPGAUADC设备树常量源码.md) · [下一章：SmartBondADC设备树常量源码](P022_SmartBondADC设备树常量源码.md) · [返回大纲](大纲.md)
