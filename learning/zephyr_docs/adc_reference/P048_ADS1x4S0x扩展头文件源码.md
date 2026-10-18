---
id: learning.zephyr-docs.adc_reference.adcheaderti-48
title: ADS1x4S0x扩展头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第48章\_ADS1x4S0x扩展头文件源码

原文：[ads1x4s0x_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/adc/ads1x4s0x.h` 内容。模数转换器（Analog-to-Digital Converter，ADC）的文件说明见[对应参考页](P047_ADS1x4S0x扩展头文件参考.md)。

## 48.1\_原始可见源码

仅去除展示行号及行末空白；版权、许可证、标识符、数值、函数签名、包含项和可见注释原样保留。源码浏览器可能隐藏文档注释，本页不声称是原始仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2023 SILA Embedded Solutions GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_ADS1X4S0X_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_ADS1X4S0X_H_

#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>


int ads1x4s0x_gpio_set_output(const struct device *dev, uint8_t pin, bool initial_value);

int ads1x4s0x_gpio_set_input(const struct device *dev, uint8_t pin);

int ads1x4s0x_gpio_deconfigure(const struct device *dev, uint8_t pin);

int ads1x4s0x_gpio_set_pin_value(const struct device *dev, uint8_t pin,
                                bool value);

int ads1x4s0x_gpio_get_pin_value(const struct device *dev, uint8_t pin,
                                bool *value);

int ads1x4s0x_gpio_port_get_raw(const struct device *dev,
                               gpio_port_value_t *value);

int ads1x4s0x_gpio_port_set_masked_raw(const struct device *dev,
                                      gpio_port_pins_t mask,
                                      gpio_port_value_t value);

int ads1x4s0x_gpio_port_toggle_bits(const struct device *dev,
                                   gpio_port_pins_t pins);


#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_ADS1X4S0X_H_ */
```

## 48.2\_注释与阅读说明

原页隐藏了函数的Doxygen说明；8个函数的声明和原始类型、指针、参数顺序完整保留。对应参考页给出每个函数的中文用途，并链接完整参数及返回值说明。

`SPDX-License-Identifier: Apache-2.0` 和版权行保留原法律标识。头文件保护（Header Guard）避免重复包含。

---

[上一章：ADS1x4S0x扩展头文件参考](P047_ADS1x4S0x扩展头文件参考.md) · [下一章：ADS1x4S0x设备树常量参考](P049_ADS1x4S0x设备树常量参考.md) · [返回大纲](大纲.md)
