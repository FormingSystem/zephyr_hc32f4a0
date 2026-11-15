---
id: learning.zephyr-docs.adc_reference.adcheadermcu-34
title: Infineon自主模拟SAR常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-sar_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第34章\_Infineon自主模拟SAR常量源码

原文：[infineon-autanalog-sar_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-sar_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/infineon-autanalog-sar.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P033_Infineon自主模拟SAR常量参考.md)。

## 34.1\_原始可见源码

仅去除展示行号和行末空白，原定义、表达式及可见注释原样保留。此处是网页可见源码，不声称是原始仓库文件的逐字节副本。

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_AUTANALOG_SAR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_AUTANALOG_SAR_H_

#define IFX_AUTANALOG_SAR_VREF_VDDA      0
#define IFX_AUTANALOG_SAR_VREF_EXT       1
#define IFX_AUTANALOG_SAR_VREF_VBGR      2
#define IFX_AUTANALOG_SAR_VREF_VDDA_BY_2 3
#define IFX_AUTANALOG_SAR_VREF_PRB_OUT0  4
#define IFX_AUTANALOG_SAR_VREF_PRB_OUT1  5

#define IFX_AUTANALOG_SAR_ACC_DISABLED  0
#define IFX_AUTANALOG_SAR_ACC_ACCUNDUMP 1

#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN1    0
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN4    1
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN6    2
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN7    3
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN1    4
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN4    5
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN6    6
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN7    7
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_OA0_OUT 8
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB0_OA1_OUT 9
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_OA0_OUT 10
#define IFX_AUTANALOG_SAR_PIN_MUX_CTB1_OA1_OUT 11
#define IFX_AUTANALOG_SAR_PIN_MUX_DAC0         12
#define IFX_AUTANALOG_SAR_PIN_MUX_DAC1         13
#define IFX_AUTANALOG_SAR_PIN_MUX_TEMP_SENSOR  14
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO0        15
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO1        16
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO2        17
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO3        18
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO4        19
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO5        20
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO6        21
#define IFX_AUTANALOG_SAR_PIN_MUX_GPIO7        22
#define IFX_AUTANALOG_SAR_PIN_MUX_VSSA         25

#define IFX_AUTANALOG_SAR_MUX_DISABLED           0
#define IFX_AUTANALOG_SAR_MUX0_SINGLE_ENDED      1
#define IFX_AUTANALOG_SAR_MUX1_SINGLE_ENDED      2
#define IFX_AUTANALOG_SAR_MUX0_MUX1_SINGLE_ENDED 3
#define IFX_AUTANALOG_SAR_MUX0_PSEUDO_DIFF       4

#define IFX_AUTANALOG_SAR_BUF_PWR_OFF             0
#define IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW       1
#define IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW_RAIL  2
#define IFX_AUTANALOG_SAR_BUF_PWR_LOW_RAIL        4
#define IFX_AUTANALOG_SAR_BUF_PWR_MEDIUM_RAIL     6
#define IFX_AUTANALOG_SAR_BUF_PWR_HIGH_RAIL       8
#define IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_HIGH_RAIL 10

#define IFX_AUTANALOG_SAR_FIR_CH_DISABLED 0
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO0    1
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO1    2
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO2    3
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO3    4
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO4    5
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO5    6
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO6    7
#define IFX_AUTANALOG_SAR_FIR_CH_GPIO7    8
#define IFX_AUTANALOG_SAR_FIR_CH_MUX0     9
#define IFX_AUTANALOG_SAR_FIR_CH_MUX1     10
#define IFX_AUTANALOG_SAR_FIR_CH_MUX2     11
#define IFX_AUTANALOG_SAR_FIR_CH_MUX3     12
#define IFX_AUTANALOG_SAR_FIR_CH_MUX4     13
#define IFX_AUTANALOG_SAR_FIR_CH_MUX5     14
#define IFX_AUTANALOG_SAR_FIR_CH_MUX6     15
#define IFX_AUTANALOG_SAR_FIR_CH_MUX7     16
#define IFX_AUTANALOG_SAR_FIR_CH_MUX8     17
#define IFX_AUTANALOG_SAR_FIR_CH_MUX9     18
#define IFX_AUTANALOG_SAR_FIR_CH_MUX10    19
#define IFX_AUTANALOG_SAR_FIR_CH_MUX11    20
#define IFX_AUTANALOG_SAR_FIR_CH_MUX12    21
#define IFX_AUTANALOG_SAR_FIR_CH_MUX13    22
#define IFX_AUTANALOG_SAR_FIR_CH_MUX14    23
#define IFX_AUTANALOG_SAR_FIR_CH_MUX15    24

#define IFX_AUTANALOG_SAR_FIFO_DISABLED 0
#define IFX_AUTANALOG_SAR_FIFO_0        1
#define IFX_AUTANALOG_SAR_FIFO_1        2
#define IFX_AUTANALOG_SAR_FIFO_2        3
#define IFX_AUTANALOG_SAR_FIFO_3        4
#define IFX_AUTANALOG_SAR_FIFO_4        5
#define IFX_AUTANALOG_SAR_FIFO_5        6
#define IFX_AUTANALOG_SAR_FIFO_6        7
#define IFX_AUTANALOG_SAR_FIFO_7        8

#define IFX_AUTANALOG_SAR_LIMIT_DISABLED 0
#define IFX_AUTANALOG_SAR_LIMIT_STC0     1
#define IFX_AUTANALOG_SAR_LIMIT_STC1     2
#define IFX_AUTANALOG_SAR_LIMIT_STC2     3
#define IFX_AUTANALOG_SAR_LIMIT_STC3     4

#define IFX_AUTANALOG_SAR_FIFO_SPLIT1 0
#define IFX_AUTANALOG_SAR_FIFO_SPLIT2 1
#define IFX_AUTANALOG_SAR_FIFO_SPLIT4 2
#define IFX_AUTANALOG_SAR_FIFO_SPLIT8 3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_INFINEON_AUTANALOG_SAR_H_ */
```

## 34.2\_注释与阅读说明

原页隐藏了Doxygen的9组标题和逐项说明，已在对应参考页完整翻译，包括缓冲器电荷泵状态、推荐模式以及FIFO分割容量。可见版权和许可证行原样保留。

头文件保护（Header Guard）通过条件预处理避免重复包含。

---

[上一章：Infineon自主模拟SAR常量参考](P033_Infineon自主模拟SAR常量参考.md) · [下一章：PIC32CMJHADC常量参考](P035_PIC32CMJHADC常量参考.md) · [返回大纲](大纲.md)
