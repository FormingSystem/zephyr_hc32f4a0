---
id: learning.zephyr-docs.hardware.adcstream-0
title: ADC通道规格
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__chan__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第447章\_ADC通道规格

原文：[structadc__chan__spec](https://docs.zephyrproject.org/latest/doxygen/html/structadc__chan__spec.html)。读取日期：2026-10-13，`latest`。

## 447.1\_用途

`struct adc_chan_spec` 表示**模数转换器（Analog-to-Digital Converter，ADC）**通道规格（Channel Specification）。对每个 ADC 设备而言，它是描述一个测量通道的唯一标识。头文件为 `zephyr/drivers/adc.h`。

## 447.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`chan_idx`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__chan__spec.html#aee81c5e448e882dc8db0b37a175708b2) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | ADC 通道索引（Channel Index） |
| [`chan_resolution`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__chan__spec.html#a44252a2c02821fd578a1fd764c0c2123) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | ADC 通道分辨率（Channel Resolution） |

---

[上一章：ADC采样序列选项](P446_ADC采样序列选项.md) · [下一章：ADC读取配置](P448_ADC读取配置.md) · [返回大纲](大纲.md)
