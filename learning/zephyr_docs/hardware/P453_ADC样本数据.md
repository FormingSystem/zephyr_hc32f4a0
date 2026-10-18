---
id: learning.zephyr-docs.hardware.adcstream-6
title: ADC样本数据
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__data_1_1adc__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第453章\_ADC样本数据

原文：[structadc__data_1_1adc__sample__data](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data_1_1adc__sample__data.html)。读取日期：2026-10-13，`latest`。

## 453.1\_结构与头文件

`struct adc_data::adc_sample_data` 是 [`adc_data`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html) 内嵌的**模数转换器（Analog-to-Digital Converter，ADC）**样本数据（Sample Data）类型，头文件为 `zephyr/drivers/adc.h`。

## 453.2\_成员与匿名联合体

官方页面列出时间差字段及包含数值字段的匿名联合体（Anonymous Union）：

```c
uint32_t timestamp_delta;
union {
    q31_t value;
};
```

译注：[`timestamp_delta`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data_1_1adc__sample__data.html#a5f99f3daec2d8098ec6fe38a9f22845e) 按名称表示时间戳差值（Timestamp Delta），原页面没有单独说明其单位；不在这里推定单位。[`value`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data_1_1adc__sample__data.html#a0375c2a0739f1f9a647f047f602ca6c7) 的类型 [`q31_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0) 表示 Q31 定点数（Q31 Fixed-point）类型，原始类型和匿名联合体布局保持不变。

包含此类型的数组见[ADC解码数据](P452_ADC解码数据.md)。

---

[上一章：ADC解码数据](P452_ADC解码数据.md) · [下一章：ADC驱动API结构](P454_ADC驱动API结构.md) · [返回大纲](大纲.md)
