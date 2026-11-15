---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-74
title: LMP90xxx扩展头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lmp90xxx_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第74章\_LMP90xxx扩展头文件源码

原文：[lmp90xxx_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/lmp90xxx_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页的全部可见代码、注释与版权许可。仅去掉网页行号和行尾空白；网页折叠或未显示的文档注释不在可见源码中补造。接口中文说明见[对应参考页](P073_LMP90xxx扩展头文件参考.md)。

## 74.1\_完整可见源码

以下代码保持原标识符和法律声明，便于与官方文件逐项对照。

```c
/*
 * Copyright (c) 2019 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_LMP90XXX_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_LMP90XXX_H_

#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>


#define LMP90XXX_GPIO_MAX 6

int lmp90xxx_gpio_set_output(const struct device *dev, uint8_t pin);

int lmp90xxx_gpio_set_input(const struct device *dev, uint8_t pin);

int lmp90xxx_gpio_set_pin_value(const struct device *dev, uint8_t pin,
                                bool value);

int lmp90xxx_gpio_get_pin_value(const struct device *dev, uint8_t pin,
                                bool *value);

int lmp90xxx_gpio_port_get_raw(const struct device *dev,
                               gpio_port_value_t *value);

int lmp90xxx_gpio_port_set_masked_raw(const struct device *dev,
                                      gpio_port_pins_t mask,
                                      gpio_port_value_t value);

int lmp90xxx_gpio_port_set_bits_raw(const struct device *dev,
                                    gpio_port_pins_t pins);

int lmp90xxx_gpio_port_clear_bits_raw(const struct device *dev,
                                      gpio_port_pins_t pins);

int lmp90xxx_gpio_port_toggle_bits(const struct device *dev,
                                   gpio_port_pins_t pins);


#endif /* ZEPHYR_INCLUDE_DRIVERS_ADC_LMP90XXX_H_ */
```

## 74.2\_注释与阅读说明

该源码浏览页展示引脚编号上限和九个函数声明，没有函数实现或额外的计算注释。完整保留输入输出指针、端口值类型和引脚集合类型；函数用途及对应详细接口见前一章。

---

[上一章：LMP90xxx扩展头文件参考](P073_LMP90xxx扩展头文件参考.md) · [下一章：Infineon自主模拟SAR驱动头文件参考](P075_Infineon自主模拟SAR驱动头文件参考.md) · [返回大纲](大纲.md)
