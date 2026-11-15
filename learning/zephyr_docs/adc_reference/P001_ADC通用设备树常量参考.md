---
id: learning.zephyr-docs.adc_reference.adcheader-1
title: ADC通用设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2adc_2adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第1章\_ADC通用设备树常量参考

原文：[dt-bindings_2adc_2adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2adc_2adc_8h.html)。读取日期：2026-10-13，`latest`。

模数转换器（Analog-to-Digital Converter，ADC）的采集时间（Acquisition Time）需要同时表达数值和单位。设备树（Devicetree）头文件 `zephyr/dt-bindings/adc/adc.h` 定义了编码和拆分这种时间值的宏（Macro）。本页对应文件参考，完整可见源码见[下一章](P002_ADC通用设备树常量源码.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

## 1.1\_单位与特殊值

| 宏 | 原始值 | 含义 |
| --- | --- | --- |
| `ADC_ACQ_TIME_MICROSECONDS` | `(1)` | 采集时间以微秒（Microseconds）表示 |
| `ADC_ACQ_TIME_NANOSECONDS` | `(2)` | 采集时间以纳秒（Nanoseconds）表示 |
| `ADC_ACQ_TIME_TICKS` | `(3)` | 采集时间以ADC时钟计数（ADC Ticks）表示 |
| `ADC_ACQ_TIME_DEFAULT` | `0` | 表示使用默认采集时间（Default Acquisition Time） |
| `ADC_ACQ_TIME_MAX` | `BIT_MASK(14)` | 原页给出的最大值宏；原页没有额外说明 |

译注：`BIT_MASK(n)` 为低n位掩码（Bit Mask）。这里的三个单位常量是编码值；特别是 `ADC_ACQ_TIME_TICKS` 的值3不表示采集固定持续3个周期。

## 1.2\_组合采集时间

`ADC_ACQ_TIME(unit, value)` 按给定单位组合采集时间值。`unit` 为单位，`value` 为该单位下的数值；原始宏展开表达式为：

```c
(((unit) << 14) | ((value) & BIT_MASK(14)))
```

译注：表达式将单位左移14位，将数值与14位掩码按位与，再用按位或合并。因此，超出低14位的数值位会被屏蔽；该表达式本身没有范围报错逻辑。这是对原定义的解释，不额外规定某款ADC支持的采集时间。

## 1.3\_提取单位与数值

宏 `ADC_ACQ_TIME_UNIT(time)` 的展开表达式如下：

```c
(((time) >> 14) & BIT_MASK(2))
```

宏 `ADC_ACQ_TIME_VALUE(time)` 的展开表达式如下：

```c
((time) & BIT_MASK(14))
```

译注：前者右移14位并取低2位，后者直接取低14位。实际支持的单位、数值及默认行为由具体驱动确定；本头文件只提供编码常量和表达式。

---

[下一章：ADC通用设备树常量源码](P002_ADC通用设备树常量源码.md) · [返回大纲](大纲.md)
