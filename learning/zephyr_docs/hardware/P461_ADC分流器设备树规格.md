---
id: learning.zephyr-docs.hardware.adcconvert-4
title: ADC分流器设备树规格
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__shunt__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第461章\_ADC分流器设备树规格

原文：[structcurrent__sense__shunt__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__shunt__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 461.1\_用途与来源

`struct current_sense_shunt_dt_spec` 保存从设备树（Devicetree，DT）取得的电流检测分流器（Current Sense Shunt）信息，供**模数转换器（Analog-to-Digital Converter，ADC）**接口使用。

头文件为 `zephyr/drivers/adc/current_sense_shunt.h`。相关静态初始化宏 [`CURRENT_SENSE_SHUNT_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__shunt__interface.html#ga104c330fc7acfd17c7778aef24f399b8) 见[电流检测分流器接口](P458_ADC电流检测分流器接口.md)。

## 461.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`port`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__shunt__dt__spec.html#ae57fb2bf3633908eef2597e33fd61d95) | `const struct adc_dt_spec` | ADC 通道信息 |
| [`shunt_micro_ohms`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__shunt__dt__spec.html#ae58c3e0159b056cb0370141665869bf1) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 分流电阻值（Shunt Resistance），单位为微欧（Micro-ohm） |

译注：本结构的 `port` 是带 `const` 限定的结构体成员，原声明不是指针；电阻单位为微欧，应与电流放大器规格中的毫欧区分。

---

[上一章：ADC电流放大器设备树规格](P460_ADC电流放大器设备树规格.md) · [下一章：ADC分压器设备树规格](P462_ADC分压器设备树规格.md) · [返回大纲](大纲.md)
