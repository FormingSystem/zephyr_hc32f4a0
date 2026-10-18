---
id: learning.zephyr-docs.hardware.gpiobackend-0
title: GPIO驱动后端
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第271章\_GPIO驱动后端

原文：[group__gpio__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 271.1\_范围

本组包含实现 **通用输入/输出（General Purpose Input/Output，GPIO）**驱动所需的应用程序接口（Application Programming Interface，API）类型、回调（Callback）签名及辅助定义，声明来自 `zephyr/drivers/gpio.h`。这些操作由结构 [`gpio_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__driver__api.html) 组织，参见[GPIO驱动函数表](P272_GPIO驱动函数表.md)。

## 271.2\_中断模式

<a id="ga82f0562c44cf0f76cc7e16d606a975db"></a>

枚举 [`gpio_int_mode`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga82f0562c44cf0f76cc7e16d606a975db) 用于驱动操作 `pin_interrupt_configure`。枚举值由公共标志定义，便于将公共标志掩码提取后直接传递给驱动。

| 枚举项 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3"></a>[`GPIO_INT_MODE_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3) | `BIT(21)` | 禁用引脚中断 |
| <a id="gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9"></a>[`GPIO_INT_MODE_LEVEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9) | `GPIO_INT_ENABLE` | 启用电平触发（Level Trigger）的引脚中断 |
| <a id="gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0"></a>[`GPIO_INT_MODE_EDGE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0) | `GPIO_INT_ENABLE \| GPIO_INT_EDGE` | 启用边沿触发（Edge Trigger）的引脚中断 |
| <a id="gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e"></a>[`GPIO_INT_MODE_DISABLE_ONLY`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e) | `BIT(21) \| GPIO_INT_ENABLE_DISABLE_ONLY` | 禁用此前配置的引脚中断，保留其配置 |
| <a id="gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688"></a>[`GPIO_INT_MODE_ENABLE_ONLY`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688) | `GPIO_INT_ENABLE \| GPIO_INT_ENABLE_DISABLE_ONLY` | 重新启用此前已配置的引脚中断 |

最后两项只有启用配置系统 Kconfig 的 [`CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT) 时才可用。`BIT(21)` 表示第21位；其余组成标志分别表示中断启用、边沿触发，以及只改变使能状态。

## 271.3\_中断触发条件

<a id="ga4ea6fd78423e6e3004702b599bc7b12d"></a>

枚举 [`gpio_int_trig`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga4ea6fd78423e6e3004702b599bc7b12d) 同样用于 `pin_interrupt_configure`。下面的高低均为**物理电平（Physical Level）**；原文括注的低/高有效在此随对应边沿或电平条件理解。

| 枚举项 | 原定义 | 触发条件 |
| --- | --- | --- |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134"></a>[`GPIO_INT_TRIG_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134) | `GPIO_INT_LOW_0` | 输入为物理低或变为物理低，亦即下降沿或低有效 |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1"></a>[`GPIO_INT_TRIG_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1) | `GPIO_INT_HIGH_1` | 输入为物理高或变为物理高，亦即上升沿或高有效 |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8"></a>[`GPIO_INT_TRIG_BOTH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8) | `GPIO_INT_LOW_0 \| GPIO_INT_HIGH_1` | 引脚上升沿或下降沿 |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223"></a>[`GPIO_INT_TRIG_WAKE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223) | `GPIO_INT_WAKEUP` | 触发系统唤醒（Wakeup） |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6"></a>[`GPIO_INT_TRIG_WAKE_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6) | `GPIO_INT_LOW_0 \| GPIO_INT_WAKEUP` | 输入为或变为物理低时唤醒，亦即下降沿或低有效 |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4"></a>[`GPIO_INT_TRIG_WAKE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4) | `GPIO_INT_HIGH_1 \| GPIO_INT_WAKEUP` | 输入为或变为物理高时唤醒，亦即上升沿或高有效 |
| <a id="gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5"></a>[`GPIO_INT_TRIG_WAKE_BOTH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5) | `GPIO_INT_LOW_0 \| GPIO_INT_HIGH_1 \| GPIO_INT_WAKEUP` | 上升沿或下降沿唤醒 |

## 271.4\_回调类型

以下声明完整保留后端类型；各参数的公共接口语义见[GPIO公共接口](P266_GPIO公共接口.md)。

<a id="ga2a4ec98edb4dfb38cde49ab796fcbff3"></a>

回调类型 [`gpio_api_get_pending_int_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga2a4ec98edb4dfb38cde49ab796fcbff3) 用于取得挂起中断。参数说明参见 [`gpio_get_pending_int()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3f9e45de172a27f49c31a072c0c241e1)。

```c
typedef uint32_t(* gpio_api_get_pending_int_t) (const struct device *dev);
```

> 译注：该后端返回类型是 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)，公共函数返回类型为 `int`，此处保留各自声明。

<a id="ga2aaa71c0dd3728fdd2f8bd111245c456"></a>

回调类型 [`gpio_api_manage_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga2aaa71c0dd3728fdd2f8bd111245c456) 用于添加或移除应用回调。参数说明参见 `gpio_add_callback() 和 gpio_remove_callback()`。

```c
typedef int(* gpio_api_manage_callback_t) (const struct device *port, struct gpio_callback *cb, bool set);
```

`cb` 指向回调结构，`set` 指示添加或移除。

<a id="ga6e7f6f2052ba10b6482445faaef4245f"></a>

回调类型 [`gpio_api_pin_configure_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga6e7f6f2052ba10b6482445faaef4245f) 用于配置单个引脚。参数说明参见 [`gpio_pin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaed4a2051d76db7eead8ed1719ce2ba33)。

```c
typedef int(* gpio_api_pin_configure_t) (const struct device *port, gpio_pin_t pin, gpio_flags_t flags);
```

<a id="ga0b30055e6722031df85b712b6b151710"></a>

回调类型 [`gpio_api_pin_get_config_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga0b30055e6722031df85b712b6b151710) 用于取得单个引脚配置。参数说明参见 [`gpio_pin_get_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga133284b60a13c6dc50b87c1d04259f5e)。

```c
typedef int(* gpio_api_pin_get_config_t) (const struct device *port, gpio_pin_t pin, gpio_flags_t *flags);
```

<a id="gafa0e73e50f77890699cfe1a04ed9f155"></a>

回调类型 [`gpio_api_pin_interrupt_configure_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gafa0e73e50f77890699cfe1a04ed9f155) 用于配置引脚中断。参数说明参见 [`gpio_pin_interrupt_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9618f254365381063439a0e9c5e787cb)。

```c
typedef int(* gpio_api_pin_interrupt_configure_t) (const struct device *port, gpio_pin_t pin, enum gpio_int_mode mode, enum gpio_int_trig trig);
```

公共 `GPIO_INT_*` 标志在传入驱动前会分解为模式参数 `mode` 与触发条件参数 `trig`。

<a id="ga43e339579ea19b4cc7d90a04c208e587"></a>

回调类型 [`gpio_api_port_clear_bits_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga43e339579ea19b4cc7d90a04c208e587) 用于将所选输出引脚设置为物理低电平。参数说明参见 [`gpio_port_clear_bits_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9d2c9daeec7ce127fc786ead566ad27f)。

```c
typedef int(* gpio_api_port_clear_bits_raw_t) (const struct device *port, gpio_port_pins_t pins);
```

<a id="ga5d175c3355e88ee78b08539b61fc84fd"></a>

回调类型 [`gpio_api_port_get_direction_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga5d175c3355e88ee78b08539b61fc84fd) 用于取得端口所选引脚方向。参数说明参见 [`gpio_port_get_direction()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad2b2945dbe6987ac425e000721a894c4)。

```c
typedef int(* gpio_api_port_get_direction_t) (const struct device *port, gpio_port_pins_t map, gpio_port_pins_t *inputs, gpio_port_pins_t *outputs);
```

<a id="gad31b73d23fa7f6c96ec2f4a2523d61fb"></a>

回调类型 [`gpio_api_port_get_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gad31b73d23fa7f6c96ec2f4a2523d61fb) 用于取得端口所有输入引脚的物理电平。参数说明参见 [`gpio_port_get_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gae2a49b36cae2e17fc665a3bd844f50b4)。

```c
typedef int(* gpio_api_port_get_raw_t) (const struct device *port, gpio_port_value_t *value);
```

<a id="gabca79087ebe1c21911ef9a80eaaee43e"></a>

回调类型 [`gpio_api_port_set_bits_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gabca79087ebe1c21911ef9a80eaaee43e) 用于将所选输出引脚设置为物理高电平。参数说明参见 [`gpio_port_set_bits_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga18e6ca0df95566fecc0633efb04a075a)。

```c
typedef int(* gpio_api_port_set_bits_raw_t) (const struct device *port, gpio_port_pins_t pins);
```

<a id="gab3d809d4ffbba78cfad45bcdb8f5ce5a"></a>

回调类型 [`gpio_api_port_set_masked_raw_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#gab3d809d4ffbba78cfad45bcdb8f5ce5a) 用于设置端口所选输出引脚的物理电平。参数说明参见 [`gpio_port_set_masked_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9e7b50d720fda362941acc1e3b3b2922)。

```c
typedef int(* gpio_api_port_set_masked_raw_t) (const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value);
```

<a id="ga8486f9d9925531757b49e745ca7fdab2"></a>

回调类型 [`gpio_api_port_toggle_bits_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__backend.html#ga8486f9d9925531757b49e745ca7fdab2) 用于翻转所选输出引脚的电平。参数说明参见 [`gpio_port_toggle_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga82977d8706fb9f464db455bd0e9ac2e4)。

```c
typedef int(* gpio_api_port_toggle_bits_t) (const struct device *port, gpio_port_pins_t pins);
```


---

[上一章：GPIO回调结构](P270_GPIO回调结构.md) · [下一章：GPIO驱动函数表](P272_GPIO驱动函数表.md) · [返回大纲](大纲.md)
