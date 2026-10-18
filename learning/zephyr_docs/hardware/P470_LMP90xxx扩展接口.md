---
id: learning.zephyr-docs.hardware.adcdevice-3
title: LMP90xxx扩展接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lmp90xxx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第470章\_LMP90xxx扩展接口

原文：[group__lmp90xxx__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__lmp90xxx__interface.html)。读取日期：2026-10-13，`latest`。

## 470.1\_用途与公共约定

本页为 Texas Instruments（德州仪器）LMP90xxx 的扩展应用程序接口（Application Programming Interface，API），控制其**通用输入输出（General-Purpose Input/Output，GPIO）**引脚和端口。LMP90xxx 是模拟前端（Analog Front End，AFE），提供 ADC 扩展接口。

```c
#include <zephyr/drivers/adc/lmp90xxx.h>
```

所有函数的 `dev` 参数均指向驱动实例的设备结构。[`gpio_port_value_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gabcebe24c93486896e1dfc2459ec25693) 为端口值类型，[`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f) 为引脚位掩码类型。
宏 [`LMP90XXX_GPIO_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__lmp90xxx__interface.html#ga4d1a76d266a648aa9ea4f831a37b2f78) 定义为 `6`，表示最大引脚编号；器件支持 D0—D6。以下所有 `pin` 参数的有效范围均为 0—`LMP90XXX_GPIO_MAX`。

```c
#define LMP90XXX_GPIO_MAX 6
```

## 470.2\_lmp90xxx_gpio_get_pin_value

读取指定 GPIO 引脚的值。

```c
int lmp90xxx_gpio_get_pin_value( const struct device * dev, uint8_t pin, bool * value );
```

`dev` 为设备结构指针。`pin` 为引脚编号，范围 0—6。`value` 指向保存引脚读取值的位置。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.3\_lmp90xxx_gpio_port_clear_bits_raw

清除 GPIO 端口的指定比特。

```c
int lmp90xxx_gpio_port_clear_bits_raw( const struct device * dev, gpio_port_pins_t pins );
```

`dev` 为设备结构指针。`pins` 是要清除的引脚掩码。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.4\_lmp90xxx_gpio_port_get_raw

读取 GPIO 端口的值。

```c
int lmp90xxx_gpio_port_get_raw( const struct device * dev, gpio_port_value_t * value );
```

`dev` 为设备结构指针。`value` 指向保存端口读取值的位置。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.5\_lmp90xxx_gpio_port_set_bits_raw

置位 GPIO 端口的指定比特。

```c
int lmp90xxx_gpio_port_set_bits_raw( const struct device * dev, gpio_port_pins_t pins );
```

`dev` 为设备结构指针。`pins` 是要置位的引脚掩码。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.6\_lmp90xxx_gpio_port_set_masked_raw

按掩码设置 GPIO 端口的值。

```c
int lmp90xxx_gpio_port_set_masked_raw( const struct device * dev, gpio_port_pins_t mask, gpio_port_value_t value );
```

`dev` 为设备结构指针。`value` 为要写入的值。`mask` 是要修改的引脚掩码。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.7\_lmp90xxx_gpio_port_toggle_bits

翻转 GPIO 端口中的指定比特。

```c
int lmp90xxx_gpio_port_toggle_bits( const struct device * dev, gpio_port_pins_t pins );
```

`dev` 为设备结构指针。`pins` 是要翻转的引脚掩码。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.8\_lmp90xxx_gpio_set_input

把 GPIO 引脚配置为输入。

```c
int lmp90xxx_gpio_set_input( const struct device * dev, uint8_t pin );
```

`dev` 为设备结构指针。`pin` 为引脚编号，范围 0—6。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.9\_lmp90xxx_gpio_set_output

把 GPIO 引脚配置为输出。

```c
int lmp90xxx_gpio_set_output( const struct device * dev, uint8_t pin );
```

`dev` 为设备结构指针。`pin` 为引脚编号，范围 0—6。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


## 470.10\_lmp90xxx_gpio_set_pin_value

设置 GPIO 引脚的值。

```c
int lmp90xxx_gpio_set_pin_value( const struct device * dev, uint8_t pin, bool value );
```

`dev` 为设备结构指针。`pin` 为引脚编号，范围 0—6。`value` 为要写入的值。

成功返回 0；通信失败时返回 `-EIO`（输入输出错误，Input/Output Error）或其他负的 errno 错误码。


---

[上一章：Infineon自动模拟SAR扩展接口](P469_Infineon自动模拟SAR扩展接口.md) · [下一章：WisBlock_ADC通道](P471_WisBlock_ADC通道.md) · [返回大纲](大纲.md)
