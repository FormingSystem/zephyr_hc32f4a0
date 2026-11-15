---
id: learning.zephyr-docs.adc_reference.adcheadermcu-35
title: PIC32CMJHADC常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第35章\_PIC32CMJHADC常量参考

原文：[mchp__pic32cm__jh__adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/mchp_pic32cm_jh_adc.h` 定义PIC32CM_JH器件的模数转换器（Analog-to-Digital Converter，ADC）输入选择。原页版权与许可声明保留如下：

```text
Copyright (c) 2026 Microchip Technology Inc.
SPDX-License-Identifier: Apache-2.0
```

## 35.1\_外部模拟输入

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_AIN0` | `0x00` | ADC模拟输入（Analog Input）AIN0 |
| `MCHP_ADC_AIN1` | `0x01` | ADC模拟输入（Analog Input）AIN1 |
| `MCHP_ADC_AIN2` | `0x02` | ADC模拟输入（Analog Input）AIN2 |
| `MCHP_ADC_AIN3` | `0x03` | ADC模拟输入（Analog Input）AIN3 |
| `MCHP_ADC_AIN4` | `0x04` | ADC模拟输入（Analog Input）AIN4 |
| `MCHP_ADC_AIN5` | `0x05` | ADC模拟输入（Analog Input）AIN5 |
| `MCHP_ADC_AIN6` | `0x06` | ADC模拟输入（Analog Input）AIN6 |
| `MCHP_ADC_AIN7` | `0x07` | ADC模拟输入（Analog Input）AIN7 |
| `MCHP_ADC_AIN8` | `0x08` | ADC模拟输入（Analog Input）AIN8 |
| `MCHP_ADC_AIN9` | `0x09` | ADC模拟输入（Analog Input）AIN9 |
| `MCHP_ADC_AIN10` | `0x0A` | ADC模拟输入（Analog Input）AIN10 |
| `MCHP_ADC_AIN11` | `0x0B` | ADC模拟输入（Analog Input）AIN11 |

## 35.2\_内部输入源

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_SCALEDCOREVCC` | `0x1A` | 缩小至1/4的内核供电（Core Supply） |
| `MCHP_ADC_SCALEDIOVCC` | `0x1B` | 缩小至1/4的VDDANA |
| `MCHP_ADC_BANDGAP` | `0x19` | 内部带隙参考电压（Internal Bandgap Reference Voltage） |

## 35.3\_正负输入有效掩码

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_MUXPOS_VALID_MASK` | `(GENMASK(0x1B, 0x19) \| GENMASK(0x0B, 0x00))` | 正输入（Positive Input，MUXPOS）有效值的位掩码（Bit Mask） |
| `MCHP_ADC_MUXNEG_VALID_MASK` | `(BIT(0x18) \| GENMASK(0x05, 0x00))` | 负输入（Negative Input，MUXNEG）有效值的位掩码（Bit Mask） |

译注：`BIT(n)` 生成第n位的位值；`GENMASK(h, l)` 生成从位l到位h的连续掩码。它们表达哪些输入编码有效，不是引脚号列表。表内竖线是原表达式的按位或（Bitwise OR）。

## 35.4\_参考电压选择

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_REF_INTREF` | `0x00` | 内部带隙参考（Internal Bandgap Reference），SUPC.VREF.SEL设为2.048 V |
| `MCHP_ADC_REF_INTVCC0` | `0x01` | VDDANA的1/1.6 |
| `MCHP_ADC_REF_INTVCC1` | `0x02` | VDDANA的1/2；**VDDANA > 4.0 V** |
| `MCHP_ADC_REF_AREFA` | `0x03` | 外部参考A（External Reference A） |
| `MCHP_ADC_REF_DAC` | `0x04` | 数模转换器（Digital-to-Analog Converter，DAC）参考 |
| `MCHP_ADC_REF_INTVCC2` | `0x05` | VDDANA |

完整可见定义见[源码页](P036_PIC32CMJHADC常量源码.md)。VDDANA及 `SUPC.VREF.SEL` 保留原电源节点与寄存器字段名称；各型号的参考选择编码、分压比例及供电条件分别按本页使用。

---

[上一章：Infineon自主模拟SAR常量源码](P034_Infineon自主模拟SAR常量源码.md) · [下一章：PIC32CMJHADC常量源码](P036_PIC32CMJHADC常量源码.md) · [返回大纲](大纲.md)
