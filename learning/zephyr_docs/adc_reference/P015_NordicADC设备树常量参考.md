---
id: learning.zephyr-docs.adc_reference.adcheadernordic-15
title: NordicADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第15章\_NordicADC设备树常量参考

原文：[nrf-adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/nrf-adc.h` 为Nordic模数转换器（Analog-to-Digital Converter，ADC）提供设备树（Devicetree）模拟输入选择宏（Macro）。其依赖项为：

```c
#include <zephyr/dt-bindings/dt-util.h>
```

## 15.1\_模拟输入位选择

原页列出下列8个定义，没有附加段落；中文说明为按名称补充的译注。`BIT(n)` 表示仅第n位置1的位值（Bit Value）。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `NRF_ADC_AIN0` | `BIT(0)` | 模拟输入（Analog Input）AIN0 |
| `NRF_ADC_AIN1` | `BIT(1)` | 模拟输入（Analog Input）AIN1 |
| `NRF_ADC_AIN2` | `BIT(2)` | 模拟输入（Analog Input）AIN2 |
| `NRF_ADC_AIN3` | `BIT(3)` | 模拟输入（Analog Input）AIN3 |
| `NRF_ADC_AIN4` | `BIT(4)` | 模拟输入（Analog Input）AIN4 |
| `NRF_ADC_AIN5` | `BIT(5)` | 模拟输入（Analog Input）AIN5 |
| `NRF_ADC_AIN6` | `BIT(6)` | 模拟输入（Analog Input）AIN6 |
| `NRF_ADC_AIN7` | `BIT(7)` | 模拟输入（Analog Input）AIN7 |

## 15.2\_与SAADC常量区分

译注：本文件使用 `BIT(0)` 至 `BIT(7)`，不能直接替换为0至7。另一份[Nordic SAADC参考](P017_NordicSAADC设备树常量参考.md)使用不同的常量定义，设备树应选择对应驱动的头文件。原始定义见[源码页](P016_NordicADC设备树常量源码.md)。

---

[上一章：B91ADC设备树常量源码](P014_B91ADC设备树常量源码.md) · [下一章：NordicADC设备树常量源码](P016_NordicADC设备树常量源码.md) · [返回大纲](大纲.md)
