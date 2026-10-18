---
id: learning.zephyr-docs.hardware.adcstruct-1
title: ADC设备树规格
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第444章\_ADC设备树规格

原文：[structadc__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 444.1\_用途与字段

`struct adc_dt_spec` 保存设备树（Devicetree）中指定的**模数转换器（Analog-to-Digital Converter，ADC）**通道信息。头文件为 `zephyr/drivers/adc.h`。这里的输入输出通道（I/O Channel）对应设备树的 `io-channel` 描述。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`dev`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#aa2656b923d105743eaee3e03691edc44) | `const struct device *` | 该输入输出通道使用的 ADC 驱动实例的设备结构指针 |
| [`channel_id`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#a083e6c5bc707606c2ea1459fb58e29a8) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 该输入输出通道使用的 ADC 通道标识符 |
| [`channel_cfg_dt_node_exists`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#aaf239b0c62b34158bac1a3b63e35f612) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 设备树是否以对应 ADC 控制器子节点的形式提供该通道配置 |
| [`channel_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#a056b22daa13da07cb3ff37bd4adf199d) | `struct adc_channel_cfg` | 设备树中指定的关联通道配置 |
| [`vref_mv`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#a9e120f52e3a905768d8e6bdc3469d20a) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 通道所选参考源的电压，以毫伏（Millivolt）表示；设备树未提供该值时为 0 |
| [`resolution`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#abbe7052a144541b8d16afee3fd231c10) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 该通道使用的 ADC 分辨率（Resolution） |
| [`oversampling`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html#aa7daf451a3438847ff989f32eae11e97) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 该通道使用的过采样（Oversampling）设置 |

## 444.2\_字段有效性

**只有 `channel_cfg_dt_node_exists` 为 `true` 时，`channel_cfg`、`vref_mv`、`resolution` 和 `oversampling` 才有效。**这项条件同时适用于上述四个字段。

通道配置的具体含义见[ADC通道配置结构](P443_ADC通道配置结构.md)。

## 444.3\_相关设备树获取宏

官方列出的相关宏如下。它们取得 ADC 设备树规格；名称中的 NAME 表示按名称、IDX 表示按索引，OR 版本提供后备值。

- [`ADC_DT_SPEC_GET_BY_NAME`](P463_ADC公共接口参考.md)
- [`ADC_DT_SPEC_GET_BY_NAME_OR`](P463_ADC公共接口参考.md)
- [`ADC_DT_SPEC_GET_BY_IDX`](P463_ADC公共接口参考.md)
- [`ADC_DT_SPEC_GET_BY_IDX_OR`](P463_ADC公共接口参考.md)
- [`ADC_DT_SPEC_GET`](P463_ADC公共接口参考.md)
- [`ADC_DT_SPEC_GET_OR`](P463_ADC公共接口参考.md)

---

[上一章：ADC通道配置结构](P443_ADC通道配置结构.md) · [下一章：ADC采样序列结构](P445_ADC采样序列结构.md) · [返回大纲](大纲.md)
