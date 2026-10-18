---
id: learning.zephyr-docs.hardware.adcstream-1
title: ADC读取配置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第448章\_ADC读取配置

原文：[structadc__read__config](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html)。读取日期：2026-10-13，`latest`。

## 448.1\_结构与头文件

`struct adc_read_config` 为**模数转换器（Analog-to-Digital Converter，ADC）**读取配置（Read Configuration）结构，位于 `zephyr/drivers/adc.h`。

官方页面只列出成员声明，没有提供每个成员的详细行为说明。下表完整保留类型；中文释义按字段名称及所引用类型提供，属于译注，不额外规定缓冲区所有权、有效期或可选值。

## 448.2\_成员声明

| 成员 | 原始类型 | 译注：字段含义 |
| --- | --- | --- |
| [`adc`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a33870e17bf80b2e3bb799b295bbc4f80) | `const struct device *` | ADC 设备指针 |
| [`is_streaming`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a7aa1a944ecaef47323adca3625de6595) | `const bool` | 是否使用流式读取（Streaming） |
| [`adc_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a0d3f55ab5574eda82cf58773550aca6d) | `const struct adc_dt_spec *` | ADC 设备树规格的指针 |
| [`triggers`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a76d97b2759e8500d526f81c1e2b92d33) | `const struct adc_stream_trigger *` | ADC 流触发配置的指针 |
| [`sequence`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a4e9679e436d75bcdd405e0628885498e) | `struct adc_sequence *` | ADC 采样序列指针 |
| [`fifo_watermark_lvl`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a1ed1a8adb1135dd2f04da077733bf417) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 先进先出缓冲区（First In, First Out，FIFO）的水位级别（Watermark Level） |
| [`fifo_mode`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a1c1898966448adb7ccd57643b19d2966) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | FIFO 模式 |
| [`adc_spec_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a72c9c6b17a3074efc1e485e48ad1deb0) | `size_t` | ADC 规格项数 |
| [`trigger_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__read__config.html#a3e7ff53c3a6a2c91222b6f635da0f096) | `size_t` | 触发配置项数 |

译注：`is_streaming` 本身带 `const` 限定；指针字段上的 `const` 则限定其指向对象，不能在译文中统一删去。

相关类型见[ADC设备树规格](P444_ADC设备树规格.md)、[ADC流触发配置](P449_ADC流触发配置.md)和[ADC采样序列结构](P445_ADC采样序列结构.md)。

---

[上一章：ADC通道规格](P447_ADC通道规格.md) · [下一章：ADC流触发配置](P449_ADC流触发配置.md) · [返回大纲](大纲.md)
