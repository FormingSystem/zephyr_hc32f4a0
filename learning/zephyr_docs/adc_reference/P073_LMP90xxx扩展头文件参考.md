---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-73
title: LMP90xxx扩展头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lmp90xxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第73章\_LMP90xxx扩展头文件参考

原文：[lmp90xxx_8h](https://docs.zephyrproject.org/latest/doxygen/html/lmp90xxx_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc/lmp90xxx.h` 提供LMP90xxx模数转换器（Analog-to-Digital Converter，ADC）的扩展应用程序接口（Application Programming Interface，API），控制器件的通用输入输出（General-Purpose Input/Output，GPIO）。文件包含设备与GPIO声明：

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

## 73.1\_引脚编号上限

宏 `LMP90XXX_GPIO_MAX` 的值为 `6`，表示LMP90xxx支持的**最大引脚编号（Maximum Pin Number）**，不是引脚总数。

## 73.2\_单引脚方向与值

以下四个函数依次将引脚配置为输出、配置为输入、设置引脚值和读取引脚值。`pin` 是引脚编号；设置函数的 `value` 是布尔值，读取函数通过 `bool *value` 输出结果。

```c
int lmp90xxx_gpio_set_output(const struct device *dev, uint8_t pin);
int lmp90xxx_gpio_set_input(const struct device *dev, uint8_t pin);
int lmp90xxx_gpio_set_pin_value(const struct device *dev, uint8_t pin, bool value);
int lmp90xxx_gpio_get_pin_value(const struct device *dev, uint8_t pin, bool *value);
```

## 73.3\_端口访问

以下函数依次读取端口值、按掩码设置端口值、置位、清位和翻转指定的位。掩码（Mask）用于指定要操作的端口位；`gpio_port_value_t` 与 `gpio_port_pins_t` 分别保留原接口的值类型和引脚集合类型。

```c
int lmp90xxx_gpio_port_get_raw(const struct device *dev, gpio_port_value_t *value);
int lmp90xxx_gpio_port_set_masked_raw(const struct device *dev, gpio_port_pins_t mask, gpio_port_value_t value);
int lmp90xxx_gpio_port_set_bits_raw(const struct device *dev, gpio_port_pins_t pins);
int lmp90xxx_gpio_port_clear_bits_raw(const struct device *dev, gpio_port_pins_t pins);
int lmp90xxx_gpio_port_toggle_bits(const struct device *dev, gpio_port_pins_t pins);
```

每个函数的 `dev` 均指向设备实例。参数限制与返回值详见[LMP90xxx扩展接口](../hardware/P470_LMP90xxx扩展接口.md)，GPIO通用类型见[GPIO公共接口](../hardware/P266_GPIO公共接口.md)。完整声明及许可见[源码页](P074_LMP90xxx扩展头文件源码.md)。

---

[上一章：分压器扩展头文件源码](P072_分压器扩展头文件源码.md) · [下一章：LMP90xxx扩展头文件源码](P074_LMP90xxx扩展头文件源码.md) · [返回大纲](大纲.md)
