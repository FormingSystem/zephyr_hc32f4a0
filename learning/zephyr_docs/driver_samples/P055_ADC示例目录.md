---
id: learning.zephyr-docs.driver_samples.page-55
title: ADC示例目录
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/adc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="adc"></a>

# 第55章\_ADC示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/adc/index.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 55.1\_示例范围

这些示例演示如何使用模数转换器（Analog-to-Digital Converter，ADC）驱动API。

| 示例 | 功能 |
| --- | --- |
| [ADC采样序列（Sequence）示例](../hardware/P440_ADC采样序列示例.md#adc_sequence) | 通过采样序列读取ADC通道的模拟输入 |
| [通过设备树配置ADC](../hardware/P439_ADC设备树示例.md#adc_dt) | 读取ADC通道的模拟输入 |
| [通用ADC流（Stream）](../hardware/P441_ADC通用流示例.md#adc_stream) | 通过流式接口取得ADC数据 |

> 译注——目录边界：三个入口链接到已有完整译文，分别说明序列、设备树和流式采集用法；此处只登记官方目录页。


对应官方文档源码：[samples/drivers/adc/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/adc/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/adc/index.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P054_nRF内部存储示例.md) · [返回大纲](大纲.md) · [下一章](P056_蜂鸣器示例目录.md)
