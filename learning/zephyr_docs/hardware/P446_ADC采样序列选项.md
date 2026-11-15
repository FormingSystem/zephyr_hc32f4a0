---
id: learning.zephyr-docs.hardware.adcstruct-3
title: ADC采样序列选项
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第446章\_ADC采样序列选项

原文：[structadc__sequence__options](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html)。读取日期：2026-10-13，`latest`。

## 446.1\_用途与字段

`struct adc_sequence_options` 定义**模数转换器（Analog-to-Digital Converter，ADC）**采样序列（Sampling Sequence）的附加选项。头文件为 `zephyr/drivers/adc.h`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`interval_us`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html#ad2f11727ab0eb7e32a5fbd07f04a85b2) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 连续两次采样之间的间隔，单位为微秒（Microsecond） |
| [`callback`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html#a71bd082c14f01a1b5d1b491e7510aa91) | [`adc_sequence_callback`](P463_ADC公共接口参考.md) | 每次采样完成后调用的回调函数（Callback） |
| [`user_data`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html#a262fd6daefb22df02c726aafcddc6d47) | `void *` | 用户数据指针 |
| [`extra_samplings`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html#a29f8ac4cdf6740f56bcd70a0a027e56a) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 要执行的额外采样次数 |

## 446.2\_采样间隔与精度

`interval_us` 为 0 时，不使用任何定时器，尽可能快地采样。

采样间隔的精度取决于驱动实现。默认的间隔处理使用内核定时器（Kernel Timer），因此精度等于内核系统时钟（System Clock）的精度。具体驱动可以使用专用硬件定时器（Hardware Timer），实现更高精度。

## 446.3\_回调与用户数据

每次采样完成后调用 `callback`；此项可选，不需要时设为 `NULL`。

`user_data` 可以把序列与回调所需的任意其他数据关联起来。

## 446.4\_额外采样次数

`extra_samplings` 表示第一次采样之外还要执行的次数。因此，总采样次数为 `1 + extra_samplings`。

---

[上一章：ADC采样序列结构](P445_ADC采样序列结构.md) · [下一章：ADC通道规格](P447_ADC通道规格.md) · [返回大纲](大纲.md)
