---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-60
title: NPCXADC温度转换扩展源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__v2t__npcx_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第60章\_NPCXADC温度转换扩展源码

原文：[adc__v2t__npcx_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc__v2t__npcx_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/sensor/adc_v2t_npcx.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P059_NPCXADC温度转换扩展参考.md)。

## 60.1\_原始可见源码

仅去除展示行号和行末空白，原版权、许可证、声明、函数签名及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_V2T_NPCX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_V2T_NPCX_H_

#include <zephyr/drivers/sensor.h>

/* V2T sensor attributes */
enum npcx_adc_v2t_sensor_attr {
        SENSOR_ATTR_NPCX_V2T_CHANNEL_CFG = SENSOR_ATTR_PRIV_START,
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_ADC_V2T_NPCX_H_ */
```

## 60.2\_注释与阅读说明

原可见注释“V2T sensor attributes”译为“电压转温度（Voltage to Temperature，V2T）传感器属性”。属性枚举以SENSOR_ATTR_PRIV_START为起点的赋值原样保留。

版权与 `SPDX-License-Identifier: Apache-2.0` 为原法律标识，保持原样。头文件保护（Header Guard）避免重复包含。

---

[上一章：NPCXADC温度转换扩展参考](P059_NPCXADC温度转换扩展参考.md) · [下一章：ADC仿真器头文件参考](P061_ADC仿真器头文件参考.md) · [返回大纲](大纲.md)
