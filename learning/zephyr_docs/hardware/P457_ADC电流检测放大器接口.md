---
id: learning.zephyr-docs.hardware.adcconvert-0
title: ADC电流检测放大器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第457章\_ADC电流检测放大器接口

原文：[group__adc__current__sense__amplifier__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html)。读取日期：2026-10-13，`latest`。

## 457.1\_用途与头文件

本组是**模数转换器（Analog-to-Digital Converter，ADC）**的电流检测放大器（Current Sense Amplifier）扩展应用程序接口（Application Programming Interface，API），通过测得电压计算实际电流。

```c
#include <zephyr/drivers/adc/current_sense_amplifier.h>
```

## 457.2\_从设备树取得规格

`CURRENT_SENSE_AMPLIFIER_DT_SPEC_GET(node_id)` 从设备树（Devicetree）节点取得电流传感器信息，返回 `struct current_sense_amplifier_dt_spec` 的静态初始化器（Static Initializer）。参数 `node_id` 为设备树节点标识符。结构字段见[电流放大器设备树规格](P460_ADC电流放大器设备树规格.md)。

原始展开式保留如下。其中 [`ADC_DT_SPEC_GET`](P463_ADC公共接口参考.md) 取得 ADC 规格，[`GPIO_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga26b2205aa82819df1d80a22761352e71) 取得通用输入输出（General-Purpose Input/Output，GPIO）规格或后备值；[`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b) 读取属性，[`DT_PROP_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f) 提供后备值，[`DT_STRING_TOKEN_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c) 取得字符串标记或后备值。

```c
{                                                                                          \
        .port = ADC_DT_SPEC_GET(node_id),                                                  \
        .power_gpio = GPIO_DT_SPEC_GET_OR(node_id, power_gpios, {0}),                      \
        .sense_milli_ohms = DT_PROP(node_id, sense_resistor_milli_ohms),                   \
        .sense_gain_mult = DT_PROP(node_id, sense_gain_mult),                              \
        .sense_gain_div = DT_PROP(node_id, sense_gain_div),                                \
        .noise_threshold = DT_PROP(node_id, zephyr_noise_threshold),                       \
        .zero_current_voltage_mv = DT_PROP(node_id, zero_current_voltage_mv),              \
        .gain_extended_range = DT_STRING_TOKEN_OR(node_id, gain_extended_range, 0xFF),     \
        .enable_calibration = DT_PROP_OR(node_id, enable_calibration, false),              \
}
```

## 457.3\_从毫伏换算为毫安

[`current_sense_amplifier_scale_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html#gaeaa2149527103e5c0e6a636cb3e9aad4) 根据测得电压计算实际电流。

```c
static inline void current_sense_amplifier_scale_dt(
    const struct current_sense_amplifier_dt_spec *spec, int32_t *v_to_i);
```

输入参数 `spec` 指向设备树取得的电流传感器规格。输入/输出参数 `v_to_i` 指向的值在调用前为测量电压，单位为毫伏（Millivolt）；调用后变为按规格换算的电流，单位为毫安（Milliampere）。函数返回类型为 `void`。

## 457.4\_从微伏换算为微安

[`current_sense_amplifier_scale_ua_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html#ga53684c1b68c4797e33b558a642019bf4) 也根据测得电压计算实际电流，但使用微量级单位并直接返回换算结果。

```c
static inline int32_t current_sense_amplifier_scale_ua_dt(
    const struct current_sense_amplifier_dt_spec *spec, int32_t microvolts);
```

`spec` 为设备树取得的电流传感器规格，`microvolts` 为测得电压，单位为微伏（Microvolt）。返回 [`int32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2) 类型的换算后电流，单位为微安（Microampere）。

---

[上一章：ADC驱动后端](P456_ADC驱动后端.md) · [下一章：ADC电流检测分流器接口](P458_ADC电流检测分流器接口.md) · [返回大纲](大纲.md)
