---
id: learning.zephyr-docs.adc_reference.adcheadernpcx-61
title: ADC仿真器头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adc__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第61章\_ADC仿真器头文件参考

原文：[adc__emul_8h](https://docs.zephyrproject.org/latest/doxygen/html/adc__emul_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/adc_emul.h` 提供仿真模数转换器（Emulated Analog-to-Digital Converter，Emulated ADC）的后端应用程序接口（Backend Application Programming Interface，Backend API）。包含项为：

```c
#include <zephyr/types.h>
#include <zephyr/drivers/adc.h>
```

完整后端配置、参数与返回值说明见[ADC模拟器接口](../hardware/P464_ADC模拟器接口.md)；参考源枚举 `adc_reference` 属于[ADC公共接口](../hardware/P463_ADC公共接口参考.md)。本页保留文件参考中的全部类型及函数入口。

## 61.1\_输入值回调类型

```c
typedef int (*adc_emul_value_func)(const struct device *dev,
                                  unsigned int chan, void *data,
                                  uint32_t *result);
```

函数指针类型（Function Pointer Type）`adc_emul_value_func` 定义用于取得ADC毫伏（Millivolt，mV）输入值的回调（Callback）。`dev` 指向设备，`chan` 为通道，`data` 为用户数据，`result` 为结果指针。具体返回约定见完整接口页。

## 61.2\_设置固定毫伏输入

```c
int adc_emul_const_value_set(const struct device *dev, unsigned int chan,
                             uint32_t value);
```

给仿真ADC通道设置固定毫伏输入值，`value` 为新的毫伏值。

## 61.3\_设置固定原始输入

```c
int adc_emul_const_raw_value_set(const struct device *dev, unsigned int chan, uint32_t raw_value);
```

给仿真ADC通道设置固定原始值（Raw Value）输入，`raw_value` 为该原始值。

## 61.4\_设置电压输入函数

```c
int adc_emul_value_func_set(const struct device *dev, unsigned int chan,
                            adc_emul_value_func func, void *data);
```

设置为仿真ADC通道取得输入电压的函数。`func` 指定回调，`data` 为传给它的用户数据。

## 61.5\_设置原始输入函数

```c
int adc_emul_raw_value_func_set(const struct device *dev, unsigned int chan,
                                adc_emul_value_func func, void *data);
```

设置仿真ADC通道的原始输入值获取函数。原摘要同时使用“voltage”和“raw input value”；译注：该入口表示原始输入值，不能仅因复用同一回调类型就把结果当作毫伏。

## 61.6\_设置参考电压

```c
int adc_emul_ref_voltage_set(const struct device *dev, enum adc_reference ref,
                             uint16_t value);
```

设置参考电压（Reference Voltage）；`ref` 选择参考源，`value` 为新的参考毫伏值。

上述函数中 `dev` 为设备指针，带有 `chan` 的函数用它选择通道；`uint16_t`、`uint32_t` 分别为16位、32位无符号整数。完整可见声明见[源码页](P062_ADC仿真器头文件源码.md)。

---

[上一章：NPCXADC温度转换扩展源码](P060_NPCXADC温度转换扩展源码.md) · [下一章：ADC仿真器头文件源码](P062_ADC仿真器头文件源码.md) · [返回大纲](大纲.md)
