---
id: learning.zephyr-docs.hardware.adcstream-2
title: ADC流触发配置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__stream__trigger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第449章\_ADC流触发配置

原文：[structadc__stream__trigger](https://docs.zephyrproject.org/latest/doxygen/html/structadc__stream__trigger.html)。读取日期：2026-10-13，`latest`。

## 449.1\_结构与头文件

`struct adc_stream_trigger` 是**模数转换器（Analog-to-Digital Converter，ADC）**流触发配置（Stream Trigger）结构，位于 `zephyr/drivers/adc.h`。

## 449.2\_成员声明

官方页面列出以下两个成员，没有进一步的文字行为说明。

| 成员 | 类型 | 译注：含义 |
| --- | --- | --- |
| [`trigger`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__stream__trigger.html#ab4ff901c839b45fa5ce12c822e68d56b) | `enum adc_trigger_type` | 触发类型（Trigger Type） |
| [`opt`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__stream__trigger.html#a7aee5cff29ffdfddb686412678947638) | `enum adc_stream_data_opt` | 流数据选项（Stream Data Option） |

具体枚举取值应参照相应类型定义；本结构页不为它们增补默认值或执行顺序。

---

[上一章：ADC读取配置](P448_ADC读取配置.md) · [下一章：ADC数据头](P450_ADC数据头.md) · [返回大纲](大纲.md)
