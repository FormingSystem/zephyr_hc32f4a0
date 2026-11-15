---
id: learning.zephyr-docs.hardware.adcstream-4
title: ADC通用数据头
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第451章\_ADC通用数据头

原文：[structadc__data__generic__header](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html)。读取日期：2026-10-13，`latest`。

## 451.1\_用途

`struct adc_data_generic_header` 是编码后的**模数转换器（Analog-to-Digital Converter，ADC）**流式帧（Streaming Frame）的通用数据头。头文件为 `zephyr/drivers/adc.h`。

这是一个紧凑布局结构（Packed Structure），位于 ADC **实时输入输出（Real-Time Input/Output，RTIO）**子系统生成的每一帧开头，提供重组后续样本所需的元数据（Metadata）。

## 451.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`timestamp_ns`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html#ad744a870de9366d91545fec872a1a43c) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 数据采集时的时间戳，单位为纳秒（Nanosecond） |
| [`num_channels`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html#a8ef076125bcdaae00b116529f09f7e8f) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 当前帧中的通道数 |
| [`shift`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html#aca9e7547e2523ac3ebe7e35df9d0f929) | [`int8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6) | 解码帧中全部样本的 Q 格式（Q-format）时使用的移位值 |
| [`channels`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__data__generic__header.html#afd029a0e527a305642785e7dbf9c51a2) | `struct adc_chan_spec [0]` | 当前帧中各通道的规格 |

通道项定义见[ADC通道规格](P447_ADC通道规格.md)。

译注：Q 格式是定点数（Fixed-point）表示方法。原声明的 `channels[0]` 是零长度数组形式，仍按原文保留；不能把它改成指针，也不能把 0 理解为实际帧永远没有通道项。

---

[上一章：ADC数据头](P450_ADC数据头.md) · [下一章：ADC解码数据](P452_ADC解码数据.md) · [返回大纲](大纲.md)
