---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-62
title: ADC仿真器头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__emul_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第62章\_ADC仿真器头文件源码

原文：[adc__emul_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc__emul_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/adc/adc_emul.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P061_ADC仿真器头文件参考.md)。

## 62.1\_原始可见源码

仅去除展示行号和行末空白，原版权、许可证、声明、函数签名及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c


/*
 * Copyright 2021 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_EMUL_H_

#include <zephyr/types.h>
#include <zephyr/drivers/adc.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*adc_emul_value_func)(const struct device *dev, unsigned int chan,
                                   void *data, uint32_t *result);

int adc_emul_const_value_set(const struct device *dev, unsigned int chan,
                             uint32_t value);

int adc_emul_const_raw_value_set(const struct device *dev, unsigned int chan, uint32_t raw_value);

int adc_emul_value_func_set(const struct device *dev, unsigned int chan,
                            adc_emul_value_func func, void *data);

int adc_emul_raw_value_func_set(const struct device *dev, unsigned int chan,
                                adc_emul_value_func func, void *data);

int adc_emul_ref_voltage_set(const struct device *dev, enum adc_reference ref,
                             uint16_t value);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_EMUL_H_ */
```

## 62.2\_注释与阅读说明

原页隐藏了Doxygen说明，文件参考和完整后端接口已分别翻译。这里保留1个函数指针类型、5个函数声明及C++编译条件下的C语言链接（C Language Linkage）声明。原始值与毫伏值的入口保持区分。

版权与 `SPDX-License-Identifier: Apache-2.0` 为原法律标识，保持原样。头文件保护（Header Guard）避免重复包含。

---

[上一章：ADC仿真器头文件参考](P061_ADC仿真器头文件参考.md) · [下一章：ADC公共头文件参考](P063_ADC公共头文件参考.md) · [返回大纲](大纲.md)
