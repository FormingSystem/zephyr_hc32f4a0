---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-56
title: NPCXADC阈值参数头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__threshold_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第56章\_NPCXADC阈值参数头文件源码

原文：[adc__npcx__threshold_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__threshold_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/adc/adc_npcx_threshold.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P055_NPCXADC阈值参数头文件参考.md)。

## 56.1\_原始可见源码

仅去除展示行号和行末空白，原版权、许可证、声明、函数签名及可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_THRESHOLD_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_THRESHOLD_H_

#include <zephyr/device.h>

enum adc_npcx_threshold_param_l_h {
        ADC_NPCX_THRESHOLD_PARAM_L_H_HIGHER,
        ADC_NPCX_THRESHOLD_PARAM_L_H_LOWER,
};

enum adc_npcx_threshold_param_type {
        ADC_NPCX_THRESHOLD_PARAM_CHNSEL,
        ADC_NPCX_THRESHOLD_PARAM_L_H,
        ADC_NPCX_THRESHOLD_PARAM_THVAL,
        ADC_NPCX_THRESHOLD_PARAM_WORK,
        ADC_NPCX_THRESHOLD_PARAM_MAX,
};

struct adc_npcx_threshold_param {
        enum adc_npcx_threshold_param_type type;
        uint32_t val;
};

int adc_npcx_threshold_mv_to_thrval(const struct device *dev, uint32_t val_mv,
                                                                uint32_t *thrval);

int adc_npcx_threshold_ctrl_set_param(const struct device *dev,
                                      const uint8_t th_sel,
                                      const struct adc_npcx_threshold_param
                                      *param);

int adc_npcx_threshold_ctrl_enable(const struct device *dev, uint8_t th_sel,
                                   const bool enable);

#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_ADC_NPCX_THRESHOLD_H_ */
```

## 56.2\_注释与阅读说明

原页隐藏了Doxygen参数说明和函数文档，已在对应参考页完整翻译。源码还显示 `ADC_NPCX_THRESHOLD_PARAM_MAX` 枚举成员，虽然原参考列表未显示它，这里仍完整保留。参数结构的type与val字段，以及所有const、指针和原参数类型保持原样。

版权与 `SPDX-License-Identifier: Apache-2.0` 为原法律标识，保持原样。头文件保护（Header Guard）避免重复包含。

---

[上一章：NPCXADC阈值参数头文件参考](P055_NPCXADC阈值参数头文件参考.md) · [下一章：NPCXADC温度参数头文件参考](P057_NPCXADC温度参数头文件参考.md) · [返回大纲](大纲.md)
