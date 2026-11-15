---
id: learning.zephyr-docs.hardware.adcstruct-0
title: ADC通道配置结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第443章\_ADC通道配置结构

原文：[structadc__channel__cfg](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html)。读取日期：2026-10-13，`latest`。

## 443.1\_用途与字段

`struct adc_channel_cfg` 指定**模数转换器（Analog-to-Digital Converter，ADC）**通道的配置。头文件为 `zephyr/drivers/adc.h`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`gain`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html#a20996396fa5b1d27eeea7da9ea9df848) | `enum adc_gain` | 增益选择（Gain Selection） |
| [`reference`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html#a73d11ad6411a62f8f21cbfa492bc1b20) | `enum adc_reference` | 参考源选择（Reference Selection） |
| [`acquisition_time`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html#a426a74cf53a4b801e91c2eeb1db3477d) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 采集时间（Acquisition Time） |
| [`channel_id`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html#aeec90a3fb60f93427a92e083326c8fcf) | `uint8_t : 5` | 通道标识符（Channel Identifier），5 位位域 |
| [`differential`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__channel__cfg.html#a372f298a2dd87660b9508ca1387084b6) | `uint8_t : 1` | 通道类型，单端（Single-ended）或差分（Differential），1 位位域 |

## 443.2\_采集时间

使用 `ADC_ACQ_TIME` 宏组合 `acquisition_time` 的值；也可以使用 `ADC_ACQ_TIME_DEFAULT`，采用给定硬件的默认设置，例如硬件不允许配置采集时间时。

具体驱动不一定支持所有可选单位。对于所选单位，数值范围为 0—16383。

## 443.3\_通道标识与模拟输入

`channel_id` 首先用于 ADC 应用程序接口（Application Programming Interface，API）中的通道识别。提交读取请求时，必须在 `adc_sequence` 结构的 `channels` 位掩码中置位相应位，才能把该通道包含在采样中。序列结构见[ADC采样序列结构](P445_ADC采样序列结构.md)。

如果硬件为每个通道提供固定模拟输入、不能另选输入，那么这个标识符也选择实际参与采样的物理 ADC 输入。

如果硬件需要为通道显式选择模拟输入，或为差分通道选择两个输入，则分别通过 `input_positive`、`input_negative` 字段指定正、负输入。

驱动是否选择隐藏的 Kconfig 选项 `ADC_CONFIGURABLE_INPUTS`，表明它支持上述哪种情况。未选择此选项时，不会定义 `CONFIG_ADC_CONFIGURABLE_INPUTS` 宏，因此结构中也不存在这两个输入字段。译注：本页面生成的字段总表没有列出它们，但原文的通道说明明确保留了这个条件，不能据此假定所有构建都具有这两个字段。

API 允许的通道标识范围为 0—31；具体驱动可能只支持其中一部分，限制取决于底层硬件能力或专门的 Kconfig 配置。

---

[上一章：RTIO的I2C标志](P442_RTIO的I2C标志.md) · [下一章：ADC设备树规格](P444_ADC设备树规格.md) · [返回大纲](大纲.md)
