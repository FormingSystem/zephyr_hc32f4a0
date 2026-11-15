---
id: learning.zephyr-docs.hardware.adcstream-3
title: ADC数据头
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第450章\_ADC数据头

原文：[structadc__data__header](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__header.html)。读取日期：2026-10-13，`latest`。

## 450.1\_结构与字段

`struct adc_data_header` 是**模数转换器（Analog-to-Digital Converter，ADC）**数据头（Data Header），位于 `zephyr/drivers/adc.h`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`base_timestamp_ns`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__header.html#a3079cf4f530baadaa3723a30a9064d2a) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 从 [`k_uptime_ticks`](../timer_reference/P086_系统时钟公共接口.md) 所提供时间取得的、最接近第一帧生成时刻的基准时间戳（Base Timestamp） |
| [`reading_count`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__header.html#a790353efe66a2aa8f1c402531c505f2d) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | `readings` 读数数组的元素个数 |

## 450.2\_数量要求与时间来源

**`reading_count` 必须至少为 1。**数组所在结构见[ADC解码数据](P452_ADC解码数据.md)。

译注：原文中的 `:c:func:k_uptime_ticks` 是未正常呈现的文档角色标记，所指函数为 [`k_uptime_ticks()`](../timer_reference/P086_系统时钟公共接口.md)。字段名的 `_ns` 表示纳秒（Nanosecond），而该函数名称中的 ticks 指系统节拍（System Ticks）；引用它作为时间来源不等于可以跳过单位换算。

---

[上一章：ADC流触发配置](P449_ADC流触发配置.md) · [下一章：ADC通用数据头](P451_ADC通用数据头.md) · [返回大纲](大纲.md)
