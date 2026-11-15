---
id: learning.zephyr-docs.hardware.adcext-0
title: ADC模拟器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第464章\_ADC模拟器接口

原文：[group__adc__emul](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html)。读取日期：2026-10-13，`latest`。

## 464.1\_用途与配置方式

本页是**模数转换器（Analog-to-Digital Converter，ADC）**模拟器（Emulator）的后端应用程序接口（Application Programming Interface，API）。模拟 ADC 的行为由应用定义。

应用可以通过设备树覆盖文件（Devicetree Overlay）指定 ADC 控制器数量以及每个控制器的通道数量；可以在设备树中或通过 [`adc_emul_ref_voltage_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga53179798ec576b329927e5b6c845aa04) 设置默认参考电压。还可以异步调用 [`adc_emul_const_value_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga564c588b71ec63aedb32f0c6221abd69) 设置模拟输入的固定毫伏值，或调用 [`adc_emul_value_func_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#gae5036c155341dd61d37558c311d3c554) 指定获取模拟输入电压的函数。

设备树示例见 [tests/drivers/adc/adc_api/boards/native_sim.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/drivers/adc/adc_api/boards/native_sim.overlay)，后端 API 使用示例见 [tests/drivers/adc/adc_emul/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/drivers/adc/adc_emul/src/main.c)。

```c
#include <zephyr/drivers/adc/adc_emul.h>
```

## 464.2\_输入值回调类型

[`adc_emul_value_func`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga8047a2a3700e085df84dc1dbc2ca155f) 定义获取 ADC 毫伏（Millivolt，mV）输入值的回调函数（Callback）。

```c
typedef int (*adc_emul_value_func)(const struct device *dev,
                                 unsigned int chan, void *data,
                                 uint32_t *result);
```

| 参数 | 含义 |
| --- | --- |
| `dev` | 驱动实例的设备结构指针 |
| `chan` | 要采样的 ADC 通道 |
| `data` | 通过 [`adc_emul_value_func_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#gae5036c155341dd61d37558c311d3c554) 传入的用户数据 |
| `result` | 输出结果指针；结果将作为 ADC 通道的输入 |

成功返回 0；其他值为错误码，会结束 ADC 上下文（Context）。

## 464.3\_设置固定毫伏输入

[`adc_emul_const_value_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga564c588b71ec63aedb32f0c6221abd69) 设置模拟 ADC 通道的固定毫伏输入值。

```c
int adc_emul_const_value_set(const struct device *dev,
                             unsigned int chan, uint32_t value);
```

`dev` 是模拟 ADC 设备，`chan` 是要设置输入的通道，`value` 为新的毫伏电压值。成功返回 0；参数无效时返回 `-EINVAL`（无效参数，Invalid Argument）。

## 464.4\_设置固定原始输入

[`adc_emul_const_raw_value_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga33dc3b494e7ac620c8cb35fd8324fd61) 设置模拟 ADC 通道的固定原始值（Raw Value）输入。

```c
int adc_emul_const_raw_value_set(const struct device *dev,
                                 unsigned int chan, uint32_t raw_value);
```

`dev` 是模拟 ADC 设备，`chan` 是要设置输入的通道，`raw_value` 是赋给该通道的新原始值。成功返回 0；参数无效时返回 `-EINVAL`。

## 464.5\_设置电压输入函数

[`adc_emul_value_func_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#gae5036c155341dd61d37558c311d3c554) 为模拟 ADC 通道设置获取输入电压的函数。

```c
int adc_emul_value_func_set(const struct device *dev, unsigned int chan,
                            adc_emul_value_func func, void *data);
```

`dev` 是模拟 ADC 设备，`chan` 为要关联函数的通道，`func` 为新函数，`data` 为调用时传给 `func` 的数据指针。成功返回 0；参数无效时返回 `-EINVAL`。

## 464.6\_设置原始输入函数

[`adc_emul_raw_value_func_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga9d3f19bd7812722d982f0ceda0418afa) 为模拟 ADC 通道设置原始输入值函数。

```c
int adc_emul_raw_value_func_set(const struct device *dev, unsigned int chan,
                                adc_emul_value_func func, void *data);
```

`dev` 是模拟 ADC 设备，`chan` 为要关联函数的通道，`func` 为新函数，`data` 为调用时传给该函数的数据指针。成功返回 0；参数无效时返回 `-EINVAL`。

译注：原摘要同时使用“voltage”和“raw input value”，本项名称及用途为原始输入值函数；不能因为它复用了 [`adc_emul_value_func`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga8047a2a3700e085df84dc1dbc2ca155f) 类型，就把原始输入值直接解释为毫伏。

## 464.7\_设置参考电压

[`adc_emul_ref_voltage_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html#ga53179798ec576b329927e5b6c845aa04) 设置参考电压（Reference Voltage）。

```c
int adc_emul_ref_voltage_set(const struct device *dev,
                             enum adc_reference ref, uint16_t value);
```

`dev` 是模拟 ADC 设备，`ref` 选择要修改的参考源配置，`value` 为新的毫伏电压值。成功返回 0；参数无效时返回 `-EINVAL`。

如果模拟器实现了 `ref_get`，更新后的参考电压也可通过 [`adc_ref_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7a4d12848b6ffb948b60f080abe3ac4d) 和 [`adc_ref_internal()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad11845f5621d0b0d03da4b6484d79aa4) 观察到。

---

[上一章：ADC公共接口参考](P463_ADC公共接口参考.md) · [下一章：ADC设备专用扩展](P465_ADC设备专用扩展.md) · [返回大纲](大纲.md)
