---
id: learning.zephyr-docs.adc_reference.adcheader-2
title: ADC通用设备树常量源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2adc_2adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_ADC通用设备树常量源码

原文：[dt-bindings_2adc_2adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2adc_2adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/dt-bindings/adc/adc.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的设备树（Devicetree）常量说明见[对应参考页](P001_ADC通用设备树常量参考.md)。

## 2.1\_原始可见源码

以下只去除网页展示行号和行末空白；版权、许可证、预处理指令、宏名称、数值及可见英文注释原样保留。源码浏览器可能隐藏文档注释，因此本段对应网页可见内容，不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright 2021 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADC_H_

#include <zephyr/dt-bindings/dt-util.h>

#define ADC_ACQ_TIME_MICROSECONDS  (1)
#define ADC_ACQ_TIME_NANOSECONDS   (2)
#define ADC_ACQ_TIME_TICKS         (3)
#define ADC_ACQ_TIME(unit, value)  (((unit) << 14) | ((value) & BIT_MASK(14)))
#define ADC_ACQ_TIME_DEFAULT       0
#define ADC_ACQ_TIME_MAX           BIT_MASK(14)

#define ADC_ACQ_TIME_UNIT(time)    (((time) >> 14) & BIT_MASK(2))
#define ADC_ACQ_TIME_VALUE(time)   ((time) & BIT_MASK(14))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ADC_ADC_H_ */
```

## 2.2\_注释与阅读说明

原页源码浏览器没有显示采集时间宏的Doxygen说明注释；其中文说明已在参考页逐项给出。

版权行和 `SPDX-License-Identifier: Apache-2.0` 属于原文件法律标识，保持原样。头文件保护（Header Guard）避免重复包含；`#include` 引入设备树辅助宏头文件。

---

[上一章：ADC通用设备树常量参考](P001_ADC通用设备树常量参考.md) · [下一章：AD4130设备树常量参考](P003_AD4130设备树常量参考.md) · [返回大纲](大纲.md)
