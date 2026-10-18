---
id: learning.zephyr-docs.adc_reference.adcheadermcu-37
title: PIC32CXSGADC常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cx__sg__adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第37章\_PIC32CXSGADC常量参考

原文：[mchp__pic32cx__sg__adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cx__sg__adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/mchp_pic32cx_sg_adc.h` 定义PIC32CX_SG器件的模数转换器（Analog-to-Digital Converter，ADC）输入选择。原页版权与许可声明保留如下：

```text
Copyright (c) 2026 Microchip Technology Inc.
SPDX-License-Identifier: Apache-2.0
```

## 37.1\_外部模拟输入

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
| `MCHP_ADC_AIN12` | `0x0C` | ADC模拟输入（Analog Input）AIN12 |
| `MCHP_ADC_AIN13` | `0x0D` | ADC模拟输入（Analog Input）AIN13 |
| `MCHP_ADC_AIN14` | `0x0E` | ADC模拟输入（Analog Input）AIN14 |
| `MCHP_ADC_AIN15` | `0x0F` | ADC模拟输入（Analog Input）AIN15 |

## 37.2\_内部输入源

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_SCALEDCOREVCC` | `0x18` | 缩小至1/4的内核供电（Core Supply） |
| `MCHP_ADC_SCALEDVBAT` | `0x19` | 缩小至1/4的电池电压（Battery Voltage，VBAT） |
| `MCHP_ADC_SCALEDIOVCC` | `0x1A` | 缩小至1/4的输入输出供电（I/O Supply） |
| `MCHP_ADC_BANDGAP` | `0x1B` | 带隙电压（Bandgap Voltage） |
| `MCHP_ADC_PTAT` | `0x1C` | 与绝对温度成正比（Proportional To Absolute Temperature，PTAT）的温度传感器 |
| `MCHP_ADC_CTAT` | `0x1D` | 与绝对温度互补（Complementary To Absolute Temperature，CTAT）的温度传感器 |
| `MCHP_ADC_DAC0` | `0x1E` | 数模转换器（Digital-to-Analog Converter，DAC）0输出 |

## 37.3\_正负输入有效掩码

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_MUXPOS_VALID_MASK` | `(BIT(0x1E) \| GENMASK(0x1B, 0x18) \| GENMASK(0x0F, 0x00))` | 正输入（Positive Input，MUXPOS）有效值的位掩码（Bit Mask） |
| `MCHP_ADC_MUXNEG_VALID_MASK` | `(BIT(0x18) \| GENMASK(0x07, 0x00))` | 负输入（Negative Input，MUXNEG）有效值的位掩码（Bit Mask） |

译注：`BIT(n)` 生成第n位的位值；`GENMASK(h, l)` 生成从位l到位h的连续掩码。它们表达哪些输入编码有效，不是引脚号列表。表内竖线是原表达式的按位或（Bitwise OR）。

原始正输入掩码只包含0x00至0x0F、0x18至0x1B及0x1E，**没有包含0x1C、0x1D**。虽然本文件也定义PTAT、CTAT常量，译文仍保留掩码的原始范围，不自行把这两位加回。

## 37.4\_参考电压选择

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `MCHP_ADC_REF_INTREF` | `0x00` | 内部带隙参考（Internal Bandgap Reference），SUPC.VREF.SEL |
| `MCHP_ADC_REF_INTVCC0` | `0x02` | VDDANA的1/2；**VDDANA > 2.0 V** |
| `MCHP_ADC_REF_INTVCC1` | `0x03` | VDDANA |
| `MCHP_ADC_REF_AREFA` | `0x04` | 外部参考A（External Reference A） |
| `MCHP_ADC_REF_AREFB` | `0x05` | 外部参考B（External Reference B） |
| `MCHP_ADC_REF_AREFC` | `0x06` | 外部参考C（External Reference C）；**仅限ADC1** |

完整可见定义见[源码页](P038_PIC32CXSGADC常量源码.md)。VDDANA及 `SUPC.VREF.SEL` 保留原电源节点与寄存器字段名称；各型号的参考选择编码、分压比例及供电条件分别按本页使用。

---

[上一章：PIC32CMJHADC常量源码](P036_PIC32CMJHADC常量源码.md) · [下一章：PIC32CXSGADC常量源码](P038_PIC32CXSGADC常量源码.md) · [返回大纲](大纲.md)
