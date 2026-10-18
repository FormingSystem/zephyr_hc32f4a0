---
id: learning.zephyr-docs.hardware.adcconvert-2
title: ADC分压器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第459章\_ADC分压器接口

原文：[group__adc__voltage__divider__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html)。读取日期：2026-10-13，`latest`。

## 459.1\_用途与头文件

本组提供分压器（Voltage Divider）扩展应用程序接口（Application Programming Interface，API），根据**模数转换器（Analog-to-Digital Converter，ADC）**测得的电压计算实际电压。

```c
#include <zephyr/drivers/adc/voltage_divider.h>
```

## 459.2\_从设备树取得分压器规格

`VOLTAGE_DIVIDER_DT_SPEC_GET(node_id)` 从设备树（Devicetree）取得分压器信息。输入 `node_id` 是设备树节点标识符，返回值为 `struct voltage_divider_dt_spec` 的静态初始化器（Static Initializer）。结构见[分压器设备树规格](P462_ADC分压器设备树规格.md)。

原始展开式如下。[`ADC_DT_SPEC_GET`](P463_ADC公共接口参考.md) 取得 ADC 通道规格，[`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b) 读取属性，[`DT_PROP_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f) 在属性不存在时使用后备值：

```c
{                                                                                          \
        .port = ADC_DT_SPEC_GET(node_id),                                                  \
        .full_ohms = DT_PROP_OR(node_id, full_ohms, 0),                                    \
        .output_ohms = DT_PROP(node_id, output_ohms),                                      \
}
```

## 459.3\_32位电压值换算

[`voltage_divider_scale_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html#ga891c6ee6073582761e63cadeaf228563) 根据测得的电压计算实际电压。

```c
static inline int voltage_divider_scale_dt(
    const struct voltage_divider_dt_spec *spec, int32_t *v_to_v);
```

`spec` 为输入的设备树分压器规格。`v_to_v` 是输入/输出指针：调用前指向测量电压，调用后为对应的换算电压。

成功返回 0；没有指定 `full_ohms` 时返回 `-ENOTSUP`（不支持，Not Supported）。

## 459.4\_64位电压值换算

[`voltage_divider_scale64_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__voltage__divider__interface.html#ga34d51b5628e43cab25cffc0e4e8ea2fe) 对 64 位值执行同样的换算，另见上述 32 位接口。

```c
static inline int voltage_divider_scale64_dt(
    const struct voltage_divider_dt_spec *spec, int64_t *v_to_v);
```

输入 `spec` 为设备树分压器规格；输入/输出 `v_to_v` 在调用前为测量电压，调用后为对应的换算电压。成功返回 0；没有指定 `full_ohms` 时返回 `-ENOTSUP`。

译注：两个分压接口的原页面均未把电压值限定为毫伏或微伏，因此这里保留原说明，不套用电流检测接口的单位约定。

---

[上一章：ADC电流检测分流器接口](P458_ADC电流检测分流器接口.md) · [下一章：ADC电流放大器设备树规格](P460_ADC电流放大器设备树规格.md) · [返回大纲](大纲.md)
