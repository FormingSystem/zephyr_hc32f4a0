---
id: learning.zephyr-docs.hardware.adcconvert-5
title: ADC分压器设备树规格
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvoltage__divider__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第462章\_ADC分压器设备树规格

原文：[structvoltage__divider__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structvoltage__divider__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 462.1\_用途与来源

`struct voltage_divider_dt_spec` 保存从设备树（Devicetree，DT）取得的分压器（Voltage Divider）信息，供**模数转换器（Analog-to-Digital Converter，ADC）**扩展接口使用。

头文件为 `zephyr/drivers/adc/voltage_divider.h`。相关静态初始化宏 [`VOLTAGE_DIVIDER_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html#ga4ed91297930bbf6b865075a9e9ba2bce) 见[分压器接口](P459_ADC分压器接口.md)。

## 462.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`port`](https://docs.zephyrproject.org/latest/doxygen/html/structvoltage__divider__dt__spec.html#a3492bc4b95943a2848dbb05f0b3fb355) | `const struct adc_dt_spec` | ADC 通道信息 |
| [`full_ohms`](https://docs.zephyrproject.org/latest/doxygen/html/structvoltage__divider__dt__spec.html#a22eb443d2dd34dcf04c2badb94f00816) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 完整电阻值（Full Resistance），单位为欧姆（Ohm） |
| [`output_ohms`](https://docs.zephyrproject.org/latest/doxygen/html/structvoltage__divider__dt__spec.html#a8960e3614c0a3d9ddc543037a51e7a8e) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 输出电阻值（Output Resistance），单位为欧姆 |

译注：`port` 按原声明保留为带 `const` 限定的结构体成员，不改为指针。

---

[上一章：ADC分流器设备树规格](P461_ADC分流器设备树规格.md) · [下一章：ADC公共接口参考](P463_ADC公共接口参考.md) · [返回大纲](大纲.md)
