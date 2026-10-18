---
id: learning.zephyr-docs.hardware.adcstruct-2
title: ADC采样序列结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第445章\_ADC采样序列结构

原文：[structadc__sequence](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html)。读取日期：2026-10-13，`latest`。

## 445.1\_用途与字段

`struct adc_sequence` 定义**模数转换器（Analog-to-Digital Converter，ADC）**的采样序列（Sampling Sequence）。头文件为 `zephyr/drivers/adc.h`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`options`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a379c6f92153dfa97439d39cbef222451) | `const struct adc_sequence_options *` | 序列附加选项的结构体指针 |
| [`channels`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a5c497c4a5de20e8591063ca8661f79c1) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 每次采样包含哪些通道的位掩码（Bit Mask） |
| [`buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a5df0ee0e6d3215aa052f108476bd57ec) | `void *` | 接收样本的缓冲区指针 |
| [`buffer_size`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a8e1bc9a4361e274bbdaedeb3151b71e5) | `size_t` | 缓冲区的实际字节数 |
| [`priority`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a4e76d19d0b033f767f076d6d2a3abbb4) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 硬件/驱动仲裁（Arbitration）的通道优先级提示 |
| [`resolution`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#ad5480691be25ed9ee81130b775743125) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | ADC 分辨率（Resolution） |
| [`oversampling`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a233e8b20b57bb2fdbebf2c85f076c802) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 过采样（Oversampling）设置 |
| [`calibrate`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a6023e3bec29deaa11b44c4df40eb7b04) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 是否请求在读取前进行校准（Calibration） |

## 445.2\_通道与采样次数

使用 `channels` 选择每次采样涉及的通道，最低有效位对应通道 0。**所有被选通道必须先通过 [`adc_channel_setup()`](P463_ADC公共接口参考.md) 配置，然后才能用于序列。**

`options` 指向[ADC采样序列选项](P446_ADC采样序列选项.md)。如果为 `NULL`，序列只执行一次采样。

## 445.3\_缓冲区布局与大小

`buffer` 指向样本写入位置。后续各次采样的数据依次写入缓冲区；每次采样写入的样本数由 `channels` 中选中的通道数决定。每次采样内部，按通道标识从低到高保存各通道的样本。

缓冲区必须足够大，需要同时考虑所选通道数、ADC 分辨率和序列包含的采样次数。

`buffer_size` 明确给出缓冲区的实际大小，单位为字节。驱动必须保证不越界写入；如果缓冲区不足以保存全部请求样本，必须返回错误。

## 445.4\_分辨率与过采样

`resolution` 指定 ADC 分辨率。单端（Single-ended）通道的取值范围为 `0 .. 2^resolution - 1`；差分（Differential）通道为 `-2^(resolution-1) .. 2^(resolution-1) - 1`。

译注：官方生成的网页将差分范围开头的负号排成了列表项目符号，正文文本因而看似缺少负号；源码注释中的范围具有负下限，这里按负下限保留其数学含义。

每个输出样本由 `2^oversampling` 次转换结果取平均得到。具体 ADC 硬件可能不支持此功能，或只在部分模式下支持，例如多通道采样时可能不支持。

## 445.5\_仲裁优先级

`priority` 仅在启用 [`CONFIG_ADC_SEQUENCE_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_SEQUENCE_PRIORITY) 时可用。0 是默认/最低优先级，数字越大优先级越高，相同值表示没有偏好。可用优先级数量由硬件决定。

这只是硬件或驱动仲裁的提示，**不保证内核优先级那样的抢占（Preemption）或完全阻塞语义**。

## 445.6\_读取前校准

设置 `calibrate` 可以请求在读取前校准。通道配置怎样影响校准过程取决于底层硬件。不支持校准的 ADC 实现应忽略这个标志。

---

[上一章：ADC设备树规格](P444_ADC设备树规格.md) · [下一章：ADC采样序列选项](P446_ADC采样序列选项.md) · [返回大纲](大纲.md)
