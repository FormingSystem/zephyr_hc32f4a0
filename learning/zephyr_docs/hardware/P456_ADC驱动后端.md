---
id: learning.zephyr-docs.hardware.adcbackend-2
title: ADC驱动后端
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第456章\_ADC驱动后端

原文：[group__adc__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 456.1\_范围与头文件

本组包含实现**模数转换器（Analog-to-Digital Converter，ADC）**驱动所需的应用程序接口（Application Programming Interface，API）类型定义、回调签名（Callback Signature）和其他辅助定义。它们由[ADC驱动API结构](P454_ADC驱动API结构.md)组织。

```c
#include <zephyr/drivers/adc.h>
```

## 456.2\_配置通道

[`adc_api_channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga871680cf9f390bfe19a10a61eb1ca092) 是配置 ADC 通道的函数指针类型，参数说明见 [`adc_channel_setup()`](P463_ADC公共接口参考.md)。

```c
typedef int (*adc_api_channel_setup)(const struct device *dev,
                                    const struct adc_channel_cfg *channel_cfg);
```

## 456.3\_设置读取请求

[`adc_api_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga4d4484e52ff7727fd316f50b2f404adf) 是设置读取请求的函数指针类型，参数说明见 [`adc_read()`](P463_ADC公共接口参考.md)。

```c
typedef int (*adc_api_read)(const struct device *dev,
                           const struct adc_sequence *sequence);
```

## 456.4\_设置异步读取请求

[`adc_api_read_async`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#gad0160f455d1901ebfe06568e8418a22c) 是设置异步读取（Asynchronous Read）请求的函数指针类型，参数说明见 [`adc_read_async()`](P463_ADC公共接口参考.md)。

```c
typedef int (*adc_api_read_async)(const struct device *dev,
                                 const struct adc_sequence *sequence,
                                 struct k_poll_signal *async);
```

## 456.5\_提交流式请求

[`adc_api_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga68510e2ee40bd0e49cf8794129ee64a2) 是提交流式请求（Stream Request）的函数指针类型。`struct rtio_iodev_sqe` 表示实时输入输出（Real-Time Input/Output，RTIO）设备提交队列项（Submission Queue Entry，SQE）。

```c
typedef void (*adc_api_submit)(const struct device *dev,
                              struct rtio_iodev_sqe *sqe);
```

## 456.6\_获取解码器

[`adc_api_get_decoder`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#ga16f50c49c3f874f80eb07d3abad2e967) 获取与给定设备关联的解码器（Decoder），进一步说明见 [`adc_get_decoder()`](P463_ADC公共接口参考.md)。

```c
typedef int (*adc_api_get_decoder)(const struct device *dev,
                                  const struct adc_decoder_api **api);
```

## 456.7\_获取参考电压

[`adc_api_ref_get`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface__backend.html#gaee2c915c2545baeb745b1e668b7da49c) 是以毫伏（Millivolt）为单位获取参考电压（Reference Voltage）的函数指针类型；相关公共辅助接口为 [`adc_ref_get()`](P463_ADC公共接口参考.md)。

```c
typedef int (*adc_api_ref_get)(const struct device *dev,
                              enum adc_reference ref, uint16_t *vref_mv);
```

---

[上一章：ADC解码器API结构](P455_ADC解码器API结构.md) · [下一章：ADC电流检测放大器接口](P457_ADC电流检测放大器接口.md) · [返回大纲](大纲.md)
