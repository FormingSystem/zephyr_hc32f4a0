---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-76
title: Infineon自主模拟SAR驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon__autanalog__sar_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第76章\_Infineon自主模拟SAR驱动头文件源码

原文：[infineon__autanalog__sar_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/infineon__autanalog__sar_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页的全部可见代码、注释与版权许可。仅去掉网页行号和行尾空白；网页折叠或未显示的文档注释不在可见源码中补造。接口中文说明见[对应参考页](P075_Infineon自主模拟SAR驱动头文件参考.md)。

## 76.1\_完整可见源码

以下代码保持原标识符和法律声明，便于与官方文件逐项对照。此处FIFO指先进先出（First In, First Out）缓冲区。

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_INFINEON_AUTANALOG_SAR_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_INFINEON_AUTANALOG_SAR_H_

#include <zephyr/device.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


int adc_ifx_autanalog_sar_fir_read_result(const struct device *dev, uint8_t fir_idx,
                                          int32_t *result);

int adc_ifx_autanalog_sar_fir_get_limit_status(const struct device *dev, uint8_t fir_idx,
                                               uint8_t *status);

int adc_ifx_autanalog_sar_fir_clear_limit_status(const struct device *dev, uint8_t fir_idx);

int adc_ifx_autanalog_sar_fir_load_coefficients(const struct device *dev, uint8_t fir_idx,
                                                const int16_t *coefficients,
                                                uint8_t num_coefficients);

int adc_ifx_autanalog_sar_fifo_read(const struct device *dev, uint8_t buf_idx, int32_t *data_out,
                                    uint16_t max_words);

int adc_ifx_autanalog_sar_fifo_read_all(const struct device *dev, uint8_t buf_idx,
                                        int32_t *data_out);

int adc_ifx_autanalog_sar_fifo_read_chan_id(const struct device *dev, uint8_t buf_idx,
                                            uint8_t input, int32_t *data_out, uint8_t *chan_id_out);

int adc_ifx_autanalog_sar_fifo_get_size(const struct device *dev, uint8_t buf_idx, uint16_t *size);

typedef void (*adc_ifx_autanalog_sar_fifo_callback_t)(const struct device *dev,
                                                      uint32_t fifo_status, void *user_data);

int adc_ifx_autanalog_sar_fifo_set_callback(const struct device *dev,
                                            adc_ifx_autanalog_sar_fifo_callback_t callback,
                                            void *user_data);

int adc_ifx_autanalog_sar_stream_stop(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_INFINEON_AUTANALOG_SAR_H_ */
```

## 76.2\_注释与阅读说明

该源码浏览页保留十个函数声明、FIFO水位中断回调类型，以及供C++使用的 `extern "C"` 条件包装；没有函数实现或额外的计算注释。回调返回类型为 `void`，各操作函数返回类型为 `int`，二者不可混淆。

---

[上一章：Infineon自主模拟SAR驱动头文件参考](P075_Infineon自主模拟SAR驱动头文件参考.md) · [下一章：InfineonSARMUX常量参考](P077_InfineonSARMUX常量参考.md) · [返回大纲](大纲.md)
