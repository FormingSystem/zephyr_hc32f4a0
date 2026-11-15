---
id: learning.zephyr-docs.hardware.adcdevice-1
title: ADS1x4s0x扩展接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ads1x4s0x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第468章\_ADS1x4s0x扩展接口

原文：[group__ads1x4s0x__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ads1x4s0x__interface.html)。读取日期：2026-10-13，`latest`。

## 468.1\_用途与公共约定

本页为 Texas Instruments（德州仪器）ADS1x4s0x 的扩展应用程序接口（Application Programming Interface，API），控制其**通用输入输出（General-Purpose Input/Output，GPIO）**引脚和端口。该器件属于模数转换器（Analog-to-Digital Converter，ADC）。

```c
#include <zephyr/drivers/adc/ads1x4s0x.h>
```

所有函数的 `dev` 参数均指向驱动实例的设备结构。[`gpio_port_value_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gabcebe24c93486896e1dfc2459ec25693) 为端口值类型，[`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f) 为引脚位掩码类型。

## 468.2\_ads1x4s0x_gpio_deconfigure

取消引脚的 GPIO 配置。

```c
int ads1x4s0x_gpio_deconfigure( const struct device * dev, uint8_t pin );
```

`dev` 为设备结构指针。`pin` 为引脚编号。

成功返回 0，失败返回负的 errno 错误码。


## 468.3\_ads1x4s0x_gpio_get_pin_value

读取指定 GPIO 引脚的值。

```c
int ads1x4s0x_gpio_get_pin_value( const struct device * dev, uint8_t pin, bool * value );
```

`dev` 为设备结构指针。`pin` 为引脚编号。`value` 指向保存引脚读取值的位置。

成功返回 0，失败返回负的 errno 错误码。


## 468.4\_ads1x4s0x_gpio_port_get_raw

读取 GPIO 端口的值。

```c
int ads1x4s0x_gpio_port_get_raw( const struct device * dev, gpio_port_value_t * value );
```

`dev` 为设备结构指针。`value` 指向保存端口读取值的位置。

成功返回 0，失败返回负的 errno 错误码。


## 468.5\_ads1x4s0x_gpio_port_set_masked_raw

按掩码设置 GPIO 端口的值。

```c
int ads1x4s0x_gpio_port_set_masked_raw( const struct device * dev, gpio_port_pins_t mask, gpio_port_value_t value );
```

`dev` 为设备结构指针。`value` 为要写入的值。`mask` 是要修改的引脚掩码。

成功返回 0，失败返回负的 errno 错误码。


## 468.6\_ads1x4s0x_gpio_port_toggle_bits

翻转 GPIO 端口中的指定比特。

```c
int ads1x4s0x_gpio_port_toggle_bits( const struct device * dev, gpio_port_pins_t pins );
```

`dev` 为设备结构指针。`pins` 是要翻转的引脚掩码。

成功返回 0，失败返回负的 errno 错误码。


## 468.7\_ads1x4s0x_gpio_set_input

把 GPIO 引脚配置为输入。

```c
int ads1x4s0x_gpio_set_input( const struct device * dev, uint8_t pin );
```

`dev` 为设备结构指针。`pin` 为引脚编号。

成功返回 0，失败返回负的 errno 错误码。


## 468.8\_ads1x4s0x_gpio_set_output

把 GPIO 引脚配置为输出。

```c
int ads1x4s0x_gpio_set_output( const struct device * dev, uint8_t pin, bool initial_value );
```

`dev` 为设备结构指针。`pin` 为引脚编号。`initial_value` 为引脚初始值。

成功返回 0，失败返回负的 errno 错误码。


## 468.9\_ads1x4s0x_gpio_set_pin_value

设置 GPIO 引脚的值。

```c
int ads1x4s0x_gpio_set_pin_value( const struct device * dev, uint8_t pin, bool value );
```

`dev` 为设备结构指针。`pin` 为引脚编号。`value` 为要写入的值。

成功返回 0，失败返回负的 errno 错误码。


---

[上一章：ADS131M02扩展接口](P467_ADS131M02扩展接口.md) · [下一章：Infineon自动模拟SAR扩展接口](P469_Infineon自动模拟SAR扩展接口.md) · [返回大纲](大纲.md)
