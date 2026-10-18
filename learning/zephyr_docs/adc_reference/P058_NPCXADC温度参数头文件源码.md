---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-58
title: NPCXADC温度参数头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__v2t_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第58章\_NPCXADC温度参数头文件源码

原文：[adc__npcx__v2t_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__v2t_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/adc/adc_npcx_v2t.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P057_NPCXADC温度参数头文件参考.md)。

## 58.1\_原始可见源码

仅去除展示行号和行末空白，原版权、许可证、声明、函数签名及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_V2T_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_V2T_H_

#include <zephyr/device.h>

int adc_npcx_v2t_set_channels(const struct device *dev, uint32_t channels);

uint32_t adc_npcx_v2t_get_channels(const struct device *dev);

#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_V2T_H_ */
```

## 58.2\_注释与阅读说明

原页隐藏了函数文档，已在参考页翻译，包括CONFIG_ADC_V2T_NPCX的配置前提，以及通道位为0表示ADC模式、为1表示电压转温度（Voltage to Temperature，V2T）模式。

版权与 `SPDX-License-Identifier: Apache-2.0` 为原法律标识，保持原样。头文件保护（Header Guard）避免重复包含。

---

[上一章：NPCXADC温度参数头文件参考](P057_NPCXADC温度参数头文件参考.md) · [下一章：NPCXADC温度转换扩展参考](P059_NPCXADC温度转换扩展参考.md) · [返回大纲](大纲.md)
