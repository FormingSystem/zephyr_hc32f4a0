---
id: learning.zephyr-docs.hardware.adcbackend-0
title: ADC驱动API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第454章\_ADC驱动API结构

原文：[structadc__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html)。读取日期：2026-10-13，`latest`。

## 454.1\_用途与必选成员

`struct adc_driver_api` 是任何**模数转换器（Analog-to-Digital Converter，ADC）**驱动都需要定义的驱动应用程序接口（Application Programming Interface，API）结构。它包含驱动所实现操作的函数指针，以及其他驱动专用常量数据。头文件为 `zephyr/drivers/adc.h`。

标记为必选（Required，REQ）的成员必须由驱动设置；可选（Optional，OPT）成员可以省略。对于受 Kconfig 条件控制的成员，该要求适用于相应功能启用的构建。

| 成员 | 类型 | 要求 | 功能与可用条件 |
| --- | --- | --- | --- |
| [`channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#ad14fe480ff7a0c4efe78e2fcb9bf6ee2) | [`adc_api_channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga871680cf9f390bfe19a10a61eb1ca092) | REQ | 配置 ADC 通道 |
| [`read`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#a489ba3478e4d36379e591fa1a3fc425b) | [`adc_api_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga4d4484e52ff7727fd316f50b2f404adf) | REQ | 设置读取请求 |
| [`read_async`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#aee03999f3427d9a77da23aa2f822fdc7) | [`adc_api_read_async`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#gad0160f455d1901ebfe06568e8418a22c) | REQ | 设置异步读取（Asynchronous Read）请求；仅在 [`CONFIG_ADC_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_ASYNC) 启用时可用 |
| [`submit`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#aed517d72a0885c8b865c8747017acb60) | [`adc_api_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga68510e2ee40bd0e49cf8794129ee64a2) | REQ | 提交流式请求（Stream Request）；仅在 [`CONFIG_ADC_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STREAM) 启用时可用 |
| [`get_decoder`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#aaf64d53d094f3be563dd2fe56b7fcd9d) | [`adc_api_get_decoder`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga16f50c49c3f874f80eb07d3abad2e967) | OPT | 获取此设备的解码器（Decoder）API；仅在 [`CONFIG_ADC_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STREAM) 启用时可用 |
| [`ref_internal`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#ad12d4f5fa0eb0e45e14553deab0edbed) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | REQ | 内部参考电压（Internal Reference Voltage），以毫伏（Millivolt）表示 |
| [`ref_get`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#a1566edae1939a32d5ff712e38c4bb998) | [`adc_api_ref_get`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#gaee2c915c2545baeb745b1e668b7da49c) | OPT | 获取所选参考源的当前电压，以毫伏表示 |

## 454.2\_参考电压及后备行为

不支持内部参考源时，将 `ref_internal` 设为 0。当 `ref_get` 为 `NULL` 时，公共函数 [`adc_ref_get()`](P463_ADC公共接口参考.md) 对内部参考源枚举值 [`ADC_REF_INTERNAL`](P463_ADC公共接口参考.md) 使用 `ref_internal` 作为后备值，对其他参考源返回 `-ENOTSUP`（不支持，Not Supported）。

实现 `ref_get` 时，应返回实时/运行期的参考电压值，例如缓存的测量值。如果设备支持该参考源，但尚不知道毫伏值，则返回 `-ENODATA`（无可用数据，No Data）；如果设备不支持该参考源，则返回 `-ENOTSUP`。

## 454.3\_相关接口

驱动操作的完整函数指针类型见[ADC驱动后端](P456_ADC驱动后端.md)，解码器见[ADC解码器API结构](P455_ADC解码器API结构.md)。官方同时引用设备定义宏 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 和 API 定义宏 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

---

[上一章：ADC样本数据](P453_ADC样本数据.md) · [下一章：ADC解码器API结构](P455_ADC解码器API结构.md) · [返回大纲](大纲.md)
