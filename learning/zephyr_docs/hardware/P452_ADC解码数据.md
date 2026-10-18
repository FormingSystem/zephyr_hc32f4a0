---
id: learning.zephyr-docs.hardware.adcstream-5
title: ADC解码数据
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第452章\_ADC解码数据

原文：[structadc__data](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html)。读取日期：2026-10-13，`latest`。

## 452.1\_结构与字段

`struct adc_data` 保存**模数转换器（Analog-to-Digital Converter，ADC）**通道的数据，位于 `zephyr/drivers/adc.h`。它还定义嵌套的 `struct adc_sample_data` 样本数据类型。

| 字段 | 原始类型 | 译注：含义 |
| --- | --- | --- |
| [`header`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html#aae165ffa0f53716f1fc2855b49a553e9) | `struct adc_data_header` | ADC 数据头 |
| [`shift`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html#a30708ba0dfeabbc87b7a854e10f5bee8) | [`int8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6) | 移位值（Shift） |
| [`readings`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data.html#a8299c4e783eb3cda1318fff57833a994) | `struct adc_data::adc_sample_data [1]` | 样本读数数组（Sample Readings） |

## 452.2\_嵌套类型与声明范围

数据头见[ADC数据头](P450_ADC数据头.md)，嵌套样本类型见[ADC样本数据](P453_ADC样本数据.md)。

原页面没有逐字段的进一步行为说明。译注：表中 [`adc_data::adc_sample_data`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data_1_1adc__sample__data.html) 是 Doxygen 用于展示嵌套类型的限定写法；保留 `readings[1]` 的原声明，不将其替换为指针或擅自修改为零长度数组。

---

[上一章：ADC通用数据头](P451_ADC通用数据头.md) · [下一章：ADC样本数据](P453_ADC样本数据.md) · [返回大纲](大纲.md)
