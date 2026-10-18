---
id: learning.zephyr-docs.hardware.adcconvert-1
title: ADC电流检测分流器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__shunt__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第458章\_ADC电流检测分流器接口

原文：[group__adc__current__sense__shunt__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__shunt__interface.html)。读取日期：2026-10-13，`latest`。

## 458.1\_用途与头文件

本组为**模数转换器（Analog-to-Digital Converter，ADC）**的电流检测分流器（Current Sense Shunt）扩展应用程序接口（Application Programming Interface，API），根据测得电压计算实际电流。

```c
#include <zephyr/drivers/adc/current_sense_shunt.h>
```

## 458.2\_设备树初始化宏

`CURRENT_SENSE_SHUNT_DT_SPEC_GET(node_id)` 从设备树（Devicetree）取得电流传感器信息。输入 `node_id` 是设备树节点标识符，结果是 `struct current_sense_shunt_dt_spec` 的静态初始化器（Static Initializer）。结构说明见[分流器设备树规格](P461_ADC分流器设备树规格.md)。

展开式如下，[`ADC_DT_SPEC_GET`](P463_ADC公共接口参考.md) 取得 ADC 通道规格，[`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b) 取得设备树属性：

```c
{                                                                                          \
        .port = ADC_DT_SPEC_GET(node_id),                                                  \
        .shunt_micro_ohms = DT_PROP(node_id, shunt_resistor_micro_ohms),                   \
}
```

## 458.3\_换算实际电流

[`current_sense_shunt_scale_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__current__sense__shunt__interface.html#ga2315a1aa2db9dafaff8c272b06d2c6b0) 根据测得电压计算实际电流。

```c
static inline void current_sense_shunt_scale_dt(
    const struct current_sense_shunt_dt_spec *spec, int32_t *v_to_i);
```

输入 `spec` 是设备树提供的电流传感器规格。输入/输出参数 `v_to_i` 在调用前指向毫伏（Millivolt）测量值，在调用后保存对应的毫安（Milliampere）电流值。函数返回类型为 `void`。

---

[上一章：ADC电流检测放大器接口](P457_ADC电流检测放大器接口.md) · [下一章：ADC分压器接口](P459_ADC分压器接口.md) · [返回大纲](大纲.md)
