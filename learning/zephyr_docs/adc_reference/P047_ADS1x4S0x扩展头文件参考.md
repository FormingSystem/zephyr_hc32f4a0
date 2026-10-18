---
id: learning.zephyr-docs.adc_reference.adcheaderti-47
title: ADS1x4S0x扩展头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第47章\_ADS1x4S0x扩展头文件参考

原文：[ads1x4s0x_8h](https://docs.zephyrproject.org/latest/doxygen/html/ads1x4s0x_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/ads1x4s0x.h` 是ADS1x4s0x模数转换器（Analog-to-Digital Converter，ADC）的扩展应用程序接口（Application Programming Interface，API）头文件，用于控制器件的通用输入输出（General-Purpose Input/Output，GPIO）。包含项如下：

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

所有函数的 `dev` 参数指向设备实例；`pin` 表示引脚编号，`uint8_t` 为8位无符号整数，`bool` 为布尔类型。`gpio_port_value_t` 是端口值类型，`gpio_port_pins_t` 是端口引脚位掩码类型，见[GPIO公共接口](../hardware/P266_GPIO公共接口.md)。以下按原头文件顺序列出全部8个函数。

## 47.1\_ads1x4s0x_gpio_set_output

```c
int ads1x4s0x_gpio_set_output(const struct device *dev, uint8_t pin, bool initial_value);
```

将ADS1x4s0x的GPIO引脚配置为输出（Output）。`initial_value` 为初始值。

## 47.2\_ads1x4s0x_gpio_set_input

```c
int ads1x4s0x_gpio_set_input(const struct device *dev, uint8_t pin);
```

将ADS1x4s0x的GPIO引脚配置为输入（Input）。

## 47.3\_ads1x4s0x_gpio_deconfigure

```c
int ads1x4s0x_gpio_deconfigure(const struct device *dev, uint8_t pin);
```

取消ADS1x4s0x引脚的GPIO配置（Deconfigure）。

## 47.4\_ads1x4s0x_gpio_set_pin_value

```c
int ads1x4s0x_gpio_set_pin_value(const struct device *dev, uint8_t pin,
                                bool value);
```

设置ADS1x4s0x的GPIO引脚值。`value` 为要写入的值。

## 47.5\_ads1x4s0x_gpio_get_pin_value

```c
int ads1x4s0x_gpio_get_pin_value(const struct device *dev, uint8_t pin,
                                bool *value);
```

读取ADS1x4s0x的GPIO引脚值。`value` 指向保存读取结果的位置。

## 47.6\_ads1x4s0x_gpio_port_get_raw

```c
int ads1x4s0x_gpio_port_get_raw(const struct device *dev,
                               gpio_port_value_t *value);
```

读取ADS1x4s0x的GPIO端口原始值（Raw Port Value）。`value` 指向保存端口值的位置。

## 47.7\_ads1x4s0x_gpio_port_set_masked_raw

```c
int ads1x4s0x_gpio_port_set_masked_raw(const struct device *dev,
                                      gpio_port_pins_t mask,
                                      gpio_port_value_t value);
```

按掩码（Mask）设置ADS1x4s0x的GPIO端口值。`mask` 选择要修改的引脚，`value` 为要写入的值。

## 47.8\_ads1x4s0x_gpio_port_toggle_bits

```c
int ads1x4s0x_gpio_port_toggle_bits(const struct device *dev,
                                   gpio_port_pins_t pins);
```

翻转（Toggle）ADS1x4s0x的GPIO端口中的指定比特；`pins` 为要翻转的引脚位掩码。

本文件参考页提供函数声明和简述；每个参数及成功／失败返回约定见[ADS1x4s0x扩展接口](../hardware/P468_ADS1x4s0x扩展接口.md)，全部可见源码见[下一章](P048_ADS1x4S0x扩展头文件源码.md)。

---

[上一章：ADS131M02扩展头文件源码](P046_ADS131M02扩展头文件源码.md) · [下一章：ADS1x4S0x扩展头文件源码](P048_ADS1x4S0x扩展头文件源码.md) · [返回大纲](大纲.md)
