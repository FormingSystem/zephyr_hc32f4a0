---
id: learning.zephyr-docs.adc_reference.adcheadernordic-22
title: SmartBondADC设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond-adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第22章\_SmartBondADC设备树常量源码

原文：[smartbond-adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器中 `zephyr/dt-bindings/adc/smartbond-adc.h` 的可见内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）宏（Macro）说明见[对应参考页](P021_SmartBondADC设备树常量参考.md)。

## 22.1\_原始可见源码

仅去除展示行号及行末空白，原版权、许可证、宏名称、数值、表达式和可见注释全部保留。源码浏览器可能隐藏文档注释，本页不声称是仓库原文件的逐字节副本。

```c
/*
 * Copyright (c) 2023 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SMARTBOND_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SMARTBOND_ADC_H_

#include <zephyr/dt-bindings/dt-util.h>

/* Values for DT zephyr,input-positive */
#define SMARTBOND_GPADC_P1_09           0
#define SMARTBOND_GPADC_P0_25           1
#define SMARTBOND_GPADC_P0_08           2
#define SMARTBOND_GPADC_P0_09           3
#define SMARTBOND_GPADC_VDD             4
#define SMARTBOND_GPADC_V30             5
#define SMARTBOND_GPADC_VBAT            8
#define SMARTBOND_GPADC_VSSA            9
#define SMARTBOND_GPADC_P1_13           16
#define SMARTBOND_GPADC_P1_12           17
#define SMARTBOND_GPADC_P1_18           18
#define SMARTBOND_GPADC_P1_19           19
#define SMARTBOND_GPADC_TEMP            20

/* Values for DT zephyr,input-positive or input-negative */
#define SMARTBOND_SDADC_P1_09           0
#define SMARTBOND_SDADC_P0_25           1
#define SMARTBOND_SDADC_P0_08           2
#define SMARTBOND_SDADC_P0_09           3
#define SMARTBOND_SDADC_P1_14           4
#define SMARTBOND_SDADC_P1_20           5
#define SMARTBOND_SDADC_P1_21           6
#define SMARTBOND_SDADC_P1_22           7
/* Values for DT zephyr,input-positive only */
#define SMARTBOND_SDADC_VBAT            8

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_SMARTBOND_ADC_H_ */
```

## 22.2\_注释与阅读说明

原注释依次为：“设备树zephyr,input-positive的值”；“设备树zephyr,input-positive或input-negative的值”；“仅用于设备树zephyr,input-positive的值”。前一组对应GPADC；第二组对应SDADC引脚输入；最后一条单独约束SDADC的VBAT选择。

版权和 `SPDX-License-Identifier: Apache-2.0` 保持原法律标识；头文件保护（Header Guard）避免重复包含。

---

[上一章：SmartBondADC设备树常量参考](P021_SmartBondADC设备树常量参考.md) · [下一章：MCUXADC16设备树常量参考](P023_MCUXADC16设备树常量参考.md) · [返回大纲](大纲.md)
