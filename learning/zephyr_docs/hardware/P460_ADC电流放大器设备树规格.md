---
id: learning.zephyr-docs.hardware.adcconvert-3
title: ADC电流放大器设备树规格
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第460章\_ADC电流放大器设备树规格

原文：[structcurrent__sense__amplifier__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 460.1\_用途与来源

`struct current_sense_amplifier_dt_spec` 保存从设备树（Devicetree，DT）取得的电流检测放大器（Current Sense Amplifier）信息，供**模数转换器（Analog-to-Digital Converter，ADC）**扩展接口使用。

头文件为 `zephyr/drivers/adc/current_sense_amplifier.h`，相关静态初始化宏为 [`CURRENT_SENSE_AMPLIFIER_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__amplifier__interface.html#ga17093e63c3ccd1e08e38ad1e0aeb9d8c)，见[电流检测放大器接口](P457_ADC电流检测放大器接口.md)。

## 460.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`port`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#aed51d08ce3824d91f31b7ad64926c667) | `struct adc_dt_spec` | ADC 通道信息 |
| [`power_gpio`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#af35fab6c94e4d95ba850e8ba2e4a0961) | `struct gpio_dt_spec` | 启用放大器的通用输入输出（General-Purpose Input/Output，GPIO） |
| [`sense_milli_ohms`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#ad6efaf2c197a7ca3db1085aa900aed23) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 检测电阻值（Sense Resistor），单位为毫欧（Milliohm） |
| [`sense_gain_mult`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#a8c7af3b111721f0b654a3943670c5614) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 检测放大器增益乘数（Gain Multiplier） |
| [`sense_gain_div`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#a3f94f49afc001c36ed42ae640bb7b157) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 检测放大器增益除数（Gain Divider） |
| [`noise_threshold`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#a140af0a4a6bcf73149dc7eec69b87e7b) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 噪声阈值（Noise Threshold） |
| [`zero_current_voltage_mv`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#a4f1e3b2bba6178fa5d36f1d734ce1111) | [`int16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf) | 零电流时的电压，单位为毫伏（Millivolt） |
| [`gain_extended_range`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#ad6dc4b19ad153cce1970d39d3bf2e70d) | `enum adc_gain` | 增益范围（Gain Range） |
| [`enable_calibration`](https://docs.zephyrproject.org/latest/doxygen/html/structcurrent__sense__amplifier__dt__spec.html#a37f6a98c94ec822854608fef74df8ee7) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 启用校准（Calibration） |

---

[上一章：ADC分压器接口](P459_ADC分压器接口.md) · [下一章：ADC分流器设备树规格](P461_ADC分流器设备树规格.md) · [返回大纲](大纲.md)
