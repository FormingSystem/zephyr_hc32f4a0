---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-54
title: NPCXADC比较器扩展源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第54章\_NPCXADC比较器扩展源码

原文：[adc__cmp__npcx_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/sensor/adc_cmp_npcx.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P053_NPCXADC比较器扩展参考.md)。

## 54.1\_原始可见源码

仅去除展示行号和行末空白，原版权、许可证、声明、函数签名及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_CMP_NPCX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_CMP_NPCX_H_

enum adc_cmp_npcx_comparison {
        ADC_CMP_NPCX_GREATER,
        ADC_CMP_NPCX_LESS_OR_EQUAL,
};

/* Supported ADC threshold controllers in NPCX series */
enum npcx_adc_cmp_thrctl {
        ADC_CMP_NPCX_THRCTL1,
        ADC_CMP_NPCX_THRCTL2,
        ADC_CMP_NPCX_THRCTL3,
        ADC_CMP_NPCX_THRCTL4,
        ADC_CMP_NPCX_THRCTL5,
        ADC_CMP_NPCX_THRCTL6,
        ADC_CMP_NPCX_THRCTL_COUNT,
};

enum adc_cmp_npcx_sensor_attribute {
        SENSOR_ATTR_LOWER_VOLTAGE_THRESH = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_UPPER_VOLTAGE_THRESH,
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_CMP_NPCX_H_ */
```

## 54.2\_注释与阅读说明

原可见注释译文：“NPCX系列支持的ADC阈值控制器”（Supported ADC Threshold Controllers in NPCX Series）。三个枚举及私有传感器属性起点赋值原样保留。

版权与 `SPDX-License-Identifier: Apache-2.0` 为原法律标识，保持原样。头文件保护（Header Guard）避免重复包含。

---

[上一章：NPCXADC比较器扩展参考](P053_NPCXADC比较器扩展参考.md) · [下一章：NPCXADC阈值参数头文件参考](P055_NPCXADC阈值参数头文件参考.md) · [返回大纲](大纲.md)
