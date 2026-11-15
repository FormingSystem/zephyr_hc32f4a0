---
id: learning.zephyr-docs.gpio-driver-reference.page-1
title: GPIO驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_GPIO驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2gpio_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入GPIO公共头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

GPIO（通用输入输出，General-purpose Input/Output）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/slist.h>
#include <zephyr/tracing/tracing.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/gpio/gpio.h>
#include <zephyr/syscalls/gpio.h>
```

查看此文件的源码。

GPIO（通用输入输出，General-purpose Input/Output）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_gpio_5Fdt_5Fspec"></a>

```c
struct gpio_dt_spec
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

保存设备树（Devicetree）中指定的GPIO引脚信息的容器。

<a id="r_gpio_5Fdriver_5Fconfig"></a>

```c
struct gpio_driver_config
```

相关声明：[gpio_driver_config](../hardware/P268_GPIO公共驱动配置.md)。

所有GPIO驱动共用此结构；它应当是device结构的config字段所指向对象的第一个成员。

<a id="r_gpio_5Fdriver_5Fdata"></a>

```c
struct gpio_driver_data
```

相关声明：[gpio_driver_data](../hardware/P269_GPIO公共驱动数据.md)。

所有GPIO驱动共用此结构；它应当是驱动的struct driver_data声明中的第一个成员。

<a id="r_gpio_5Fcallback"></a>

```c
struct gpio_callback
```

相关声明：[gpio_callback](../hardware/P270_GPIO回调结构.md)。

GPIO回调结构（Callback Structure）。

<a id="r_gpio_5Fdriver_5Fapi"></a>

```c
struct gpio_driver_api
```

相关声明：[gpio_driver_api](../hardware/P272_GPIO驱动函数表.md)。

驱动操作（Driver Operations）：GPIO驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gacb1077b77aecf8f1a9c7636ea583c4cf"></a>

```c
#define GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)
```

相关声明：[GPIO_DT_SPEC_GET_BY_IDX](../hardware/P266_GPIO公共接口.md#gacb1077b77aecf8f1a9c7636ea583c4cf)。

gpio_dt_spec的静态初始化器（Static Initializer）。

<a id="r_ga3db4fa464e191016287f4c4d7eb9a983"></a>

```c
#define GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, idx, default_value)
```

相关声明：[GPIO_DT_SPEC_GET_BY_IDX_OR](../hardware/P266_GPIO公共接口.md#ga3db4fa464e191016287f4c4d7eb9a983)。

与GPIO_DT_SPEC_GET_BY_IDX()类似，但提供缺省值作为回退。

<a id="r_ga2fa6bb5880f46984f9fc29c70f7d503e"></a>

```c
#define GPIO_DT_SPEC_GET(node_id, prop)
```

相关声明：[GPIO_DT_SPEC_GET](../hardware/P266_GPIO公共接口.md#ga2fa6bb5880f46984f9fc29c70f7d503e)。

等价于GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, 0)。

<a id="r_ga26b2205aa82819df1d80a22761352e71"></a>

```c
#define GPIO_DT_SPEC_GET_OR(node_id, prop, default_value)
```

相关声明：[GPIO_DT_SPEC_GET_OR](../hardware/P266_GPIO公共接口.md#ga26b2205aa82819df1d80a22761352e71)。

等价于GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, 0, default_value)。

<a id="r_gabbdbef450f14fd0af73667e2728ad084"></a>

```c
#define GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, idx)
```

相关声明：[GPIO_DT_SPEC_INST_GET_BY_IDX](../hardware/P266_GPIO公共接口.md#gabbdbef450f14fd0af73667e2728ad084)。

从DT_DRV_COMPAT实例的GPIO属性中指定索引的条目生成gpio_dt_spec静态初始化器。

<a id="r_gaf07edf6bc88af18e9976c76f6c3c3bf1"></a>

```c
#define GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, idx, default_value)
```

相关声明：[GPIO_DT_SPEC_INST_GET_BY_IDX_OR](../hardware/P266_GPIO公共接口.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)。

从DT_DRV_COMPAT实例的GPIO属性中指定索引的条目生成gpio_dt_spec静态初始化器，并提供回退值。

<a id="r_ga168f5c6e39a0111191f606a9a0826e89"></a>

```c
#define GPIO_DT_SPEC_INST_GET(inst, prop)
```

相关声明：[GPIO_DT_SPEC_INST_GET](../hardware/P266_GPIO公共接口.md#ga168f5c6e39a0111191f606a9a0826e89)。

等价于GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, 0)。

<a id="r_gae6b4a354c3cf0e042a390aac4bc37c69"></a>

```c
#define GPIO_DT_SPEC_INST_GET_OR(inst, prop, default_value)
```

相关声明：[GPIO_DT_SPEC_INST_GET_OR](../hardware/P266_GPIO公共接口.md#gae6b4a354c3cf0e042a390aac4bc37c69)。

等价于GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, 0, default_value)。

<a id="r_ga439c3d29aa585b00853aba6d6416028a"></a>

```c
#define GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, ngpios)
```

相关声明：[GPIO_DT_RESERVED_RANGES_NGPIOS](../hardware/P266_GPIO公共接口.md#ga439c3d29aa585b00853aba6d6416028a)。

根据设备树gpio-reserved-ranges属性和ngpios参数生成保留GPIO的位掩码（Bitmask）。

<a id="r_ga648fcc0633d57b52d3df683efda98440"></a>

```c
#define GPIO_DT_RESERVED_RANGES(node_id)
```

相关声明：[GPIO_DT_RESERVED_RANGES](../hardware/P266_GPIO公共接口.md#ga648fcc0633d57b52d3df683efda98440)。

根据设备树gpio-reserved-ranges与ngpios属性的值生成保留GPIO的位掩码。

<a id="r_gaebaea00f6f7649c61651e8d50c7cdf07"></a>

```c
#define GPIO_DT_INST_RESERVED_RANGES_NGPIOS(inst, ngpios)
```

相关声明：[GPIO_DT_INST_RESERVED_RANGES_NGPIOS](../hardware/P266_GPIO公共接口.md#gaebaea00f6f7649c61651e8d50c7cdf07)。

根据DT_DRV_COMPAT实例的gpio-reserved-ranges属性和ngpios参数生成保留GPIO的位掩码。

<a id="r_ga9136b467eaddcc734bc6a0a7d8b34e14"></a>

```c
#define GPIO_DT_INST_RESERVED_RANGES(inst)
```

相关声明：[GPIO_DT_INST_RESERVED_RANGES](../hardware/P266_GPIO公共接口.md#ga9136b467eaddcc734bc6a0a7d8b34e14)。

根据DT_DRV_COMPAT实例的GPIO gpio-reserved-ranges与ngpios属性生成保留GPIO的位掩码。

<a id="r_ga274e09d7082d97b2f90c6a7fd4b71d49"></a>

```c
#define GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(node_id, ngpios)
```

相关声明：[GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC](../hardware/P266_GPIO公共接口.md#ga274e09d7082d97b2f90c6a7fd4b71d49)。

根据设备树gpio-reserved-ranges属性和ngpios参数生成允许使用的GPIO的位掩码。

<a id="r_ga856fe8042e496a39ef3a4e19fff2c4ce"></a>

```c
#define GPIO_DT_INST_PORT_PIN_MASK_NGPIOS_EXC(inst, ngpios)
```

相关声明：[GPIO_DT_INST_PORT_PIN_MASK_NGPIOS_EXC](../hardware/P266_GPIO公共接口.md#ga856fe8042e496a39ef3a4e19fff2c4ce)。

根据DT_DRV_COMPAT实例的gpio-reserved-ranges属性和ngpios参数生成允许使用的GPIO的位掩码。

<a id="r_ga1449ba90eaec5e6144fe4faae21f2e3f"></a>

```c
#define GPIO_MAX_PINS_PER_PORT (sizeof(gpio_port_pins_t) * __CHAR_BIT__)
```

相关声明：[GPIO_MAX_PINS_PER_PORT](../hardware/P266_GPIO公共接口.md#ga1449ba90eaec5e6144fe4faae21f2e3f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

gpio_port_pins_t能够支持的最大引脚数量。

<a id="define-members-0"></a>

### GPIO输入／输出配置标志（Input/Output Configuration Flags）

<a id="r_ga7be6a0cc9aa65da1d4ee5751b4085853"></a>

```c
#define GPIO_INPUT BIT(16)
```

相关声明：[GPIO_INPUT](../hardware/P266_GPIO公共接口.md#ga7be6a0cc9aa65da1d4ee5751b4085853)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将引脚使能为输入（Input）。

<a id="r_ga0db9fe8a278e6ab7c5c6f14fe58e5eb1"></a>

```c
#define GPIO_OUTPUT BIT(17)
```

相关声明：[GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将引脚使能为输出（Output），不改变输出状态。

<a id="r_gaf82306c09450f6933366c4b821db21ed"></a>

```c
#define GPIO_DISCONNECTED 0
```

相关声明：[GPIO_DISCONNECTED](../hardware/P266_GPIO公共接口.md#gaf82306c09450f6933366c4b821db21ed)。

同时禁用引脚的输入和输出。

<a id="r_gaf85baf9f9c1ba554324b4cd7064487b0"></a>

```c
#define GPIO_OUTPUT_LOW (GPIO_OUTPUT | GPIO_OUTPUT_INIT_LOW)
```

相关声明：[GPIO_OUTPUT_LOW](../hardware/P266_GPIO公共接口.md#gaf85baf9f9c1ba554324b4cd7064487b0)、[GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)。

将GPIO引脚配置为输出，并初始化为低电平（Low）。

<a id="r_ga10d31f204c0e927017d571352422fb09"></a>

```c
#define GPIO_OUTPUT_HIGH (GPIO_OUTPUT | GPIO_OUTPUT_INIT_HIGH)
```

相关声明：[GPIO_OUTPUT_HIGH](../hardware/P266_GPIO公共接口.md#ga10d31f204c0e927017d571352422fb09)、[GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)。

将GPIO引脚配置为输出，并初始化为高电平（High）。

<a id="r_ga1e1d6be5f2f788f89468a0ce8b854634"></a>

```c
#define GPIO_OUTPUT_INACTIVE
```

相关声明：[GPIO_OUTPUT_INACTIVE](../hardware/P266_GPIO公共接口.md#ga1e1d6be5f2f788f89468a0ce8b854634)。

将GPIO引脚配置为输出，并初始化为逻辑0（Logic 0）。

<a id="r_ga0f5cc126d6a690eb3e303eb29aa718ce"></a>

```c
#define GPIO_OUTPUT_ACTIVE
```

相关声明：[GPIO_OUTPUT_ACTIVE](../hardware/P266_GPIO公共接口.md#ga0f5cc126d6a690eb3e303eb29aa718ce)。

将GPIO引脚配置为输出，并初始化为逻辑1（Logic 1）。

<a id="define-members-1"></a>

### GPIO中断配置标志（Interrupt Configuration Flags）

GPIO_INT_*标志用于指定输入GPIO引脚如何触发中断。

中断可以响应引脚的物理电平或逻辑电平。响应逻辑电平的中断会考虑GPIO_ACTIVE_LOW标志。如果引脚配置为低有效（Active Low），物理低电平视为逻辑1，即有效状态；物理高电平视为逻辑0，即无效状态。配置中断触发属性时，GPIO控制器应重置中断状态，例如清除待处理位。应用应使用GPIO_INT_MODE_ENABLE_ONLY与GPIO_INT_MODE_DISABLE_ONLY标志，在不改变任何GPIO设置的情况下使能或禁用该引脚中断。

<a id="r_ga91657faac28f9b213105dd61a419dd5a"></a>

```c
#define GPIO_INT_DISABLE BIT(21)
```

相关声明：[GPIO_INT_DISABLE](../hardware/P266_GPIO公共接口.md#ga91657faac28f9b213105dd61a419dd5a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用GPIO引脚中断（Interrupt）。

<a id="r_gaed642a4e482f73aa917477370d0e241b"></a>

```c
#define GPIO_INT_EDGE_RISING
```

相关声明：[GPIO_INT_EDGE_RISING](../hardware/P266_GPIO公共接口.md#gaed642a4e482f73aa917477370d0e241b)。

将GPIO中断配置为引脚上升沿（Rising Edge）触发，并使能中断。

<a id="r_ga73bed10383a27d4a03feb300e64af8e8"></a>

```c
#define GPIO_INT_EDGE_FALLING
```

相关声明：[GPIO_INT_EDGE_FALLING](../hardware/P266_GPIO公共接口.md#ga73bed10383a27d4a03feb300e64af8e8)。

将GPIO中断配置为引脚下降沿（Falling Edge）触发，并使能中断。

<a id="r_ga10fa307ab17d02819108165a09f8e08b"></a>

```c
#define GPIO_INT_EDGE_BOTH
```

相关声明：[GPIO_INT_EDGE_BOTH](../hardware/P266_GPIO公共接口.md#ga10fa307ab17d02819108165a09f8e08b)。

将GPIO中断配置为引脚上升沿或下降沿触发，并使能中断。

<a id="r_gaddbb5ad576875af9c2d73b73df55c893"></a>

```c
#define GPIO_INT_LEVEL_LOW
```

相关声明：[GPIO_INT_LEVEL_LOW](../hardware/P266_GPIO公共接口.md#gaddbb5ad576875af9c2d73b73df55c893)。

将GPIO中断配置为引脚物理低电平触发，并使能中断。

<a id="r_ga233690d9a6a64bc9f804e3caa6d4a88f"></a>

```c
#define GPIO_INT_LEVEL_HIGH
```

相关声明：[GPIO_INT_LEVEL_HIGH](../hardware/P266_GPIO公共接口.md#ga233690d9a6a64bc9f804e3caa6d4a88f)。

将GPIO中断配置为引脚物理高电平触发，并使能中断。

<a id="r_ga7b922529a3cb9396b0d82ca823e9d010"></a>

```c
#define GPIO_INT_EDGE_TO_INACTIVE
```

相关声明：[GPIO_INT_EDGE_TO_INACTIVE](../hardware/P266_GPIO公共接口.md#ga7b922529a3cb9396b0d82ca823e9d010)。

将GPIO中断配置为引脚状态变为逻辑0时触发，并使能中断。

<a id="r_ga35d2ff0e041236d82004a4bb2b5bf634"></a>

```c
#define GPIO_INT_EDGE_TO_ACTIVE
```

相关声明：[GPIO_INT_EDGE_TO_ACTIVE](../hardware/P266_GPIO公共接口.md#ga35d2ff0e041236d82004a4bb2b5bf634)。

将GPIO中断配置为引脚状态变为逻辑1时触发，并使能中断。

<a id="r_gacb9bb1b63f172af2da7eb193e234c4f2"></a>

```c
#define GPIO_INT_LEVEL_INACTIVE
```

相关声明：[GPIO_INT_LEVEL_INACTIVE](../hardware/P266_GPIO公共接口.md#gacb9bb1b63f172af2da7eb193e234c4f2)。

将GPIO中断配置为引脚逻辑0电平触发，并使能中断。

<a id="r_gae51c68ff83959994bb942bb253505ca1"></a>

```c
#define GPIO_INT_LEVEL_ACTIVE
```

相关声明：[GPIO_INT_LEVEL_ACTIVE](../hardware/P266_GPIO公共接口.md#gae51c68ff83959994bb942bb253505ca1)。

将GPIO中断配置为引脚逻辑1电平触发，并使能中断。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga7f40ed51f14fd8000e9b52ab347b273f"></a>

```c
typedef uint32_t gpio_port_pins_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

标识某个端口（Port）关联的一组引脚。

<a id="r_gabcebe24c93486896e1dfc2459ec25693"></a>

```c
typedef uint32_t gpio_port_value_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

提供某个端口关联的一组引脚的值。

<a id="r_ga38179eb7a46a743c12cfac28f347fb34"></a>

```c
typedef uint8_t gpio_pin_t
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

用于保存GPIO引脚索引（Pin Index）的类型。

<a id="r_gad435719dccdc37c05852960a7218fbd2"></a>

```c
typedef uint16_t gpio_dt_flags_t
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)。

用于保存GPIO设备树标志（Devicetree Flags）的类型。

<a id="r_ga5f5cb5e7dae6d58e072bb450af029d2e"></a>

```c
typedef uint32_t gpio_flags_t
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)。

用于保存GPIO配置标志（Configuration Flags）的类型。

<a id="r_gaf0aa40279d32b1b8332f2f23a39510af"></a>

```c
typedef void(* gpio_callback_handler_t) (const struct device *port, struct gpio_callback *cb, gpio_port_pins_t pins)
```

相关声明：[gpio_callback_handler_t](../hardware/P266_GPIO公共接口.md#gaf0aa40279d32b1b8332f2f23a39510af)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

定义应用回调处理函数（Callback Handler）的签名。

<a id="r_ga6e7f6f2052ba10b6482445faaef4245f"></a>

```c
typedef int(* gpio_api_pin_configure_t) (const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

相关声明：[gpio_api_pin_configure_t](../hardware/P271_GPIO驱动后端.md#ga6e7f6f2052ba10b6482445faaef4245f)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置单个引脚的回调API。

<a id="r_ga0b30055e6722031df85b712b6b151710"></a>

```c
typedef int(* gpio_api_pin_get_config_t) (const struct device *port, gpio_pin_t pin, gpio_flags_t *flags)
```

相关声明：[gpio_api_pin_get_config_t](../hardware/P271_GPIO驱动后端.md#ga0b30055e6722031df85b712b6b151710)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取单个引脚配置的回调API。

<a id="r_gad31b73d23fa7f6c96ec2f4a2523d61fb"></a>

```c
typedef int(* gpio_api_port_get_raw_t) (const struct device *port, gpio_port_value_t *value)
```

相关声明：[gpio_api_port_get_raw_t](../hardware/P271_GPIO驱动后端.md#gad31b73d23fa7f6c96ec2f4a2523d61fb)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

获取端口中全部输入引脚物理电平的回调API。

<a id="r_gab3d809d4ffbba78cfad45bcdb8f5ce5a"></a>

```c
typedef int(* gpio_api_port_set_masked_raw_t) (const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

相关声明：[gpio_api_port_set_masked_raw_t](../hardware/P271_GPIO驱动后端.md#gab3d809d4ffbba78cfad45bcdb8f5ce5a)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

设置端口中选定输出引脚物理电平的回调API。

<a id="r_gabca79087ebe1c21911ef9a80eaaee43e"></a>

```c
typedef int(* gpio_api_port_set_bits_raw_t) (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_api_port_set_bits_raw_t](../hardware/P271_GPIO驱动后端.md#gabca79087ebe1c21911ef9a80eaaee43e)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚物理电平置高的回调API。

<a id="r_ga43e339579ea19b4cc7d90a04c208e587"></a>

```c
typedef int(* gpio_api_port_clear_bits_raw_t) (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_api_port_clear_bits_raw_t](../hardware/P271_GPIO驱动后端.md#ga43e339579ea19b4cc7d90a04c208e587)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚物理电平置低的回调API。

<a id="r_ga8486f9d9925531757b49e745ca7fdab2"></a>

```c
typedef int(* gpio_api_port_toggle_bits_t) (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_api_port_toggle_bits_t](../hardware/P271_GPIO驱动后端.md#ga8486f9d9925531757b49e745ca7fdab2)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

翻转选定输出引脚电平的回调API。

<a id="r_gafa0e73e50f77890699cfe1a04ed9f155"></a>

```c
typedef int(* gpio_api_pin_interrupt_configure_t) (const struct device *port, gpio_pin_t pin, enum gpio_int_mode mode, enum gpio_int_trig trig)
```

相关声明：[gpio_api_pin_interrupt_configure_t](../hardware/P271_GPIO驱动后端.md#gafa0e73e50f77890699cfe1a04ed9f155)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)、[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)。

配置引脚中断的回调API。

<a id="r_ga2aaa71c0dd3728fdd2f8bd111245c456"></a>

```c
typedef int(* gpio_api_manage_callback_t) (const struct device *port, struct gpio_callback *cb, bool set)
```

相关声明：[gpio_api_manage_callback_t](../hardware/P271_GPIO驱动后端.md#ga2aaa71c0dd3728fdd2f8bd111245c456)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

添加或移除应用回调的回调API。

<a id="r_ga2a4ec98edb4dfb38cde49ab796fcbff3"></a>

```c
typedef uint32_t(* gpio_api_get_pending_int_t) (const struct device *dev)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gpio_api_get_pending_int_t](../hardware/P271_GPIO驱动后端.md#ga2a4ec98edb4dfb38cde49ab796fcbff3)、[device](../device_reference/P002_设备对象结构.md)。

获取待处理中断（Pending Interrupts）的回调API。

<a id="r_ga5d175c3355e88ee78b08539b61fc84fd"></a>

```c
typedef int(* gpio_api_port_get_direction_t) (const struct device *port, gpio_port_pins_t map, gpio_port_pins_t *inputs, gpio_port_pins_t *outputs)
```

相关声明：[gpio_api_port_get_direction_t](../hardware/P271_GPIO驱动后端.md#ga5d175c3355e88ee78b08539b61fc84fd)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

获取端口中选定引脚方向（Direction）的回调API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga82f0562c44cf0f76cc7e16d606a975db"></a>

```c
enum gpio_int_mode { GPIO_INT_MODE_DISABLED = BIT(21) , GPIO_INT_MODE_LEVEL = GPIO_INT_ENABLE , GPIO_INT_MODE_EDGE = GPIO_INT_ENABLE | GPIO_INT_EDGE , GPIO_INT_MODE_DISABLE_ONLY = BIT(21) | GPIO_INT_ENABLE_DISABLE_ONLY , GPIO_INT_MODE_ENABLE_ONLY = GPIO_INT_ENABLE | GPIO_INT_ENABLE_DISABLE_ONLY }
```

相关声明：[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)、[GPIO_INT_MODE_DISABLED](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3)、[GPIO_INT_MODE_LEVEL](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9)、[GPIO_INT_MODE_EDGE](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0)、[GPIO_INT_MODE_DISABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e)、[GPIO_INT_MODE_ENABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688)。

供pin_interrupt_configure驱动操作使用的中断模式（Interrupt Modes）。

<a id="r_ga4ea6fd78423e6e3004702b599bc7b12d"></a>

```c
enum gpio_int_trig { GPIO_INT_TRIG_LOW = GPIO_INT_LOW_0 , GPIO_INT_TRIG_HIGH = GPIO_INT_HIGH_1 , GPIO_INT_TRIG_BOTH = GPIO_INT_LOW_0 | GPIO_INT_HIGH_1 , GPIO_INT_TRIG_WAKE = GPIO_INT_WAKEUP , GPIO_INT_TRIG_WAKE_LOW = GPIO_INT_LOW_0 | GPIO_INT_WAKEUP , GPIO_INT_TRIG_WAKE_HIGH = GPIO_INT_HIGH_1 | GPIO_INT_WAKEUP , GPIO_INT_TRIG_WAKE_BOTH = GPIO_INT_LOW_0 | GPIO_INT_HIGH_1 | GPIO_INT_WAKEUP }
```

相关声明：[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)、[GPIO_INT_TRIG_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134)、[GPIO_INT_TRIG_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1)、[GPIO_INT_TRIG_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8)、[GPIO_INT_TRIG_WAKE](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223)、[GPIO_INT_TRIG_WAKE_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6)、[GPIO_INT_TRIG_WAKE_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4)、[GPIO_INT_TRIG_WAKE_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5)。

供pin_interrupt_configure驱动操作使用的中断触发条件（Interrupt Triggers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gab7465c5401aa9d47d68980455847be9f"></a>

```c
static bool gpio_port_pin_is_supported (gpio_port_pins_t port_pin_mask, gpio_pin_t pin)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gpio_port_pin_is_supported](../hardware/P266_GPIO公共接口.md#gab7465c5401aa9d47d68980455847be9f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

检查引脚是否在有效范围内，并且受GPIO控制器支持。

<a id="r_gaaec9ad17c08a0d527d66445fe82d8327"></a>

```c
static bool gpio_is_ready_dt (const struct gpio_dt_spec *spec)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

验证GPIO端口是否就绪（Ready）。

<a id="r_ga9618f254365381063439a0e9c5e787cb"></a>

```c
int gpio_pin_interrupt_configure (const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

相关声明：[gpio_pin_interrupt_configure](../hardware/P266_GPIO公共接口.md#ga9618f254365381063439a0e9c5e787cb)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置引脚中断。

<a id="r_ga24f0b4ad30e6a8c81f51a2813478c793"></a>

```c
static int gpio_pin_interrupt_configure_dt (const struct gpio_dt_spec *spec, gpio_flags_t flags)
```

相关声明：[gpio_pin_interrupt_configure_dt](../hardware/P266_GPIO公共接口.md#ga24f0b4ad30e6a8c81f51a2813478c793)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

根据gpio_dt_spec配置引脚中断。

<a id="r_gaed4a2051d76db7eead8ed1719ce2ba33"></a>

```c
int gpio_pin_configure (const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

相关声明：[gpio_pin_configure](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置单个引脚。

<a id="r_ga423db4f985098ddcaa504ec430e91913"></a>

```c
static int gpio_pin_configure_dt (const struct gpio_dt_spec *spec, gpio_flags_t extra_flags)
```

相关声明：[gpio_pin_configure_dt](../hardware/P266_GPIO公共接口.md#ga423db4f985098ddcaa504ec430e91913)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)。

根据gpio_dt_spec及附加标志配置单个引脚。

<a id="r_gad2b2945dbe6987ac425e000721a894c4"></a>

```c
int gpio_port_get_direction (const struct device *port, gpio_port_pins_t map, gpio_port_pins_t *inputs, gpio_port_pins_t *outputs)
```

相关声明：[gpio_port_get_direction](../hardware/P266_GPIO公共接口.md#gad2b2945dbe6987ac425e000721a894c4)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

获取端口中选定引脚的方向。

<a id="r_ga1454bc223fc2200aff3c4aab7d747da2"></a>

```c
static int gpio_pin_is_input (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_pin_is_input](../hardware/P266_GPIO公共接口.md#ga1454bc223fc2200aff3c4aab7d747da2)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

检查引脚是否配置为输入。

<a id="r_ga7aaec28a83cac63bd87fc94cc72664b1"></a>

```c
static int gpio_pin_is_input_dt (const struct gpio_dt_spec *spec)
```

相关声明：[gpio_pin_is_input_dt](../hardware/P266_GPIO公共接口.md#ga7aaec28a83cac63bd87fc94cc72664b1)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

检查gpio_dt_spec指定的单个引脚是否配置为输入。

<a id="r_ga3b854d759180e222299ea445b401acc1"></a>

```c
static int gpio_pin_is_output (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_pin_is_output](../hardware/P266_GPIO公共接口.md#ga3b854d759180e222299ea445b401acc1)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

检查引脚是否配置为输出。

<a id="r_ga2255c5681d17952ab89a4b6016d8e80d"></a>

```c
static int gpio_pin_is_output_dt (const struct gpio_dt_spec *spec)
```

相关声明：[gpio_pin_is_output_dt](../hardware/P266_GPIO公共接口.md#ga2255c5681d17952ab89a4b6016d8e80d)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

检查gpio_dt_spec指定的单个引脚是否配置为输出。

<a id="r_ga133284b60a13c6dc50b87c1d04259f5e"></a>

```c
int gpio_pin_get_config (const struct device *port, gpio_pin_t pin, gpio_flags_t *flags)
```

相关声明：[gpio_pin_get_config](../hardware/P266_GPIO公共接口.md#ga133284b60a13c6dc50b87c1d04259f5e)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取单个引脚的配置。

<a id="r_ga820448aa4be8b14839bc6a00c9f34bb4"></a>

```c
static int gpio_pin_get_config_dt (const struct gpio_dt_spec *spec, gpio_flags_t *flags)
```

相关声明：[gpio_pin_get_config_dt](../hardware/P266_GPIO公共接口.md#ga820448aa4be8b14839bc6a00c9f34bb4)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取gpio_dt_spec指定的单个引脚的配置。

<a id="r_gae2a49b36cae2e17fc665a3bd844f50b4"></a>

```c
int gpio_port_get_raw (const struct device *port, gpio_port_value_t *value)
```

相关声明：[gpio_port_get_raw](../hardware/P266_GPIO公共接口.md#gae2a49b36cae2e17fc665a3bd844f50b4)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

获取端口中全部输入引脚的物理电平（Physical Level）。

<a id="r_ga7c7a53371834c7646dc7f41ca0bb7921"></a>

```c
int gpio_port_get (const struct device *port, gpio_port_value_t *value)
```

相关声明：[gpio_port_get](../hardware/P266_GPIO公共接口.md#ga7c7a53371834c7646dc7f41ca0bb7921)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

获取端口中全部输入引脚的逻辑电平（Logical Level）。

<a id="r_ga9e7b50d720fda362941acc1e3b3b2922"></a>

```c
int gpio_port_set_masked_raw (const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

相关声明：[gpio_port_set_masked_raw](../hardware/P266_GPIO公共接口.md#ga9e7b50d720fda362941acc1e3b3b2922)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

设置端口中输出引脚的物理电平。

<a id="r_ga0c5ddbec7eb194ffed6cf12ae235ae04"></a>

```c
int gpio_port_set_masked (const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

相关声明：[gpio_port_set_masked](../hardware/P266_GPIO公共接口.md#ga0c5ddbec7eb194ffed6cf12ae235ae04)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

设置端口中输出引脚的逻辑电平。

<a id="r_ga18e6ca0df95566fecc0633efb04a075a"></a>

```c
int gpio_port_set_bits_raw (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_port_set_bits_raw](../hardware/P266_GPIO公共接口.md#ga18e6ca0df95566fecc0633efb04a075a)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚的物理电平置高。

<a id="r_gae450ff904686aa4b8fd81bc0dbbafdb5"></a>

```c
int gpio_port_set_bits (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_port_set_bits](../hardware/P266_GPIO公共接口.md#gae450ff904686aa4b8fd81bc0dbbafdb5)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚的逻辑电平置为有效（Active）。

<a id="r_ga9d2c9daeec7ce127fc786ead566ad27f"></a>

```c
int gpio_port_clear_bits_raw (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_port_clear_bits_raw](../hardware/P266_GPIO公共接口.md#ga9d2c9daeec7ce127fc786ead566ad27f)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚的物理电平置低。

<a id="r_ga9318c349663568f1fb9400b9458765dc"></a>

```c
int gpio_port_clear_bits (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_port_clear_bits](../hardware/P266_GPIO公共接口.md#ga9318c349663568f1fb9400b9458765dc)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

将选定输出引脚的逻辑电平置为无效（Inactive）。

<a id="r_ga82977d8706fb9f464db455bd0e9ac2e4"></a>

```c
int gpio_port_toggle_bits (const struct device *port, gpio_port_pins_t pins)
```

相关声明：[gpio_port_toggle_bits](../hardware/P266_GPIO公共接口.md#ga82977d8706fb9f464db455bd0e9ac2e4)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

翻转选定输出引脚的电平。

<a id="r_ga1a06f729e76d39937d0572b6c531e038"></a>

```c
int gpio_port_set_clr_bits_raw (const struct device *port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins)
```

相关声明：[gpio_port_set_clr_bits_raw](../hardware/P266_GPIO公共接口.md#ga1a06f729e76d39937d0572b6c531e038)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

设置选定输出引脚的物理电平。

<a id="r_ga45172f2b1bb09e8f3c89fa951cdefc14"></a>

```c
int gpio_port_set_clr_bits (const struct device *port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins)
```

相关声明：[gpio_port_set_clr_bits](../hardware/P266_GPIO公共接口.md#ga45172f2b1bb09e8f3c89fa951cdefc14)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

设置选定输出引脚的逻辑电平。

<a id="r_ga635975f1df6157c7e8a6c67bac55fbc0"></a>

```c
int gpio_pin_get_raw (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_pin_get_raw](../hardware/P266_GPIO公共接口.md#ga635975f1df6157c7e8a6c67bac55fbc0)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

获取输入引脚的物理电平。

<a id="r_ga496cd45fd6a2826c75d70c71f967234b"></a>

```c
int gpio_pin_get (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_pin_get](../hardware/P266_GPIO公共接口.md#ga496cd45fd6a2826c75d70c71f967234b)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

获取输入引脚的逻辑电平。

<a id="r_gaabeb2d0d98856c7ff78be36651d6bbc1"></a>

```c
static int gpio_pin_get_dt (const struct gpio_dt_spec *spec)
```

相关声明：[gpio_pin_get_dt](../hardware/P266_GPIO公共接口.md#gaabeb2d0d98856c7ff78be36651d6bbc1)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

获取gpio_dt_spec指定的输入引脚的逻辑电平。

<a id="r_ga08824e05ea87c4ad2e48edaa13aad30a"></a>

```c
int gpio_pin_set_raw (const struct device *port, gpio_pin_t pin, int value)
```

相关声明：[gpio_pin_set_raw](../hardware/P266_GPIO公共接口.md#ga08824e05ea87c4ad2e48edaa13aad30a)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

设置输出引脚的物理电平。

<a id="r_gadac09ef40fc1ba5d8bb40965efde0fda"></a>

```c
int gpio_pin_set (const struct device *port, gpio_pin_t pin, int value)
```

相关声明：[gpio_pin_set](../hardware/P266_GPIO公共接口.md#gadac09ef40fc1ba5d8bb40965efde0fda)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

设置输出引脚的逻辑电平。

<a id="r_ga541064fb9e575c0c559c101754466fa8"></a>

```c
static int gpio_pin_set_dt (const struct gpio_dt_spec *spec, int value)
```

相关声明：[gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

设置gpio_dt_spec指定的输出引脚的逻辑电平。

<a id="r_gaa761788e22a185db227dce7c24915154"></a>

```c
int gpio_pin_toggle (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_pin_toggle](../hardware/P266_GPIO公共接口.md#gaa761788e22a185db227dce7c24915154)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

翻转引脚电平。

<a id="r_ga3272e866489da6c2e12c48f803c59e81"></a>

```c
static int gpio_pin_toggle_dt (const struct gpio_dt_spec *spec)
```

相关声明：[gpio_pin_toggle_dt](../hardware/P266_GPIO公共接口.md#ga3272e866489da6c2e12c48f803c59e81)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

翻转gpio_dt_spec指定的引脚电平。

<a id="r_ga7a7dd7c1f3a2135a9f378e1c34b6232c"></a>

```c
static void gpio_init_callback (struct gpio_callback *callback, gpio_callback_handler_t handler, gpio_port_pins_t pin_mask)
```

相关声明：[gpio_init_callback](../hardware/P266_GPIO公共接口.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)、[gpio_callback](../hardware/P270_GPIO回调结构.md)、[gpio_callback_handler_t](../hardware/P266_GPIO公共接口.md#gaf0aa40279d32b1b8332f2f23a39510af)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

用于正确初始化struct gpio_callback的辅助函数。

<a id="r_ga05fd15af20386d69f9332354285b0cca"></a>

```c
static int gpio_add_callback (const struct device *port, struct gpio_callback *callback)
```

相关声明：[gpio_add_callback](../hardware/P266_GPIO公共接口.md#ga05fd15af20386d69f9332354285b0cca)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

添加应用回调。

<a id="r_ga54845eb95bc9636c3e6ff285300b6979"></a>

```c
static int gpio_add_callback_dt (const struct gpio_dt_spec *spec, struct gpio_callback *callback)
```

相关声明：[gpio_add_callback_dt](../hardware/P266_GPIO公共接口.md#ga54845eb95bc9636c3e6ff285300b6979)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

添加应用回调。

<a id="r_gac1e94ba8faac79f469447e9b5d2f8c06"></a>

```c
static int gpio_remove_callback (const struct device *port, struct gpio_callback *callback)
```

相关声明：[gpio_remove_callback](../hardware/P266_GPIO公共接口.md#gac1e94ba8faac79f469447e9b5d2f8c06)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

移除应用回调。

<a id="r_ga2c9f8fee2addfc0aeeeeb011d534f304"></a>

```c
static int gpio_remove_callback_dt (const struct gpio_dt_spec *spec, struct gpio_callback *callback)
```

相关声明：[gpio_remove_callback_dt](../hardware/P266_GPIO公共接口.md#ga2c9f8fee2addfc0aeeeeb011d534f304)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

移除应用回调。

<a id="r_ga3f9e45de172a27f49c31a072c0c241e1"></a>

```c
int gpio_get_pending_int (const struct device *dev)
```

相关声明：[gpio_get_pending_int](../hardware/P266_GPIO公共接口.md#ga3f9e45de172a27f49c31a072c0c241e1)、[device](../device_reference/P002_设备对象结构.md)。

获取待处理中断的函数。

## 1.6\_源码定位与版本边界

相对源码定位：[GPIO公共头文件](../../../include/zephyr/drivers/gpio.h)、[GPIO工具辅助函数](../../../include/zephyr/drivers/gpio/gpio_utils.h)、[设备树标志](../../../include/zephyr/dt-bindings/gpio/gpio.h)、[系统调用处理](../../../drivers/gpio/gpio_handlers.c)、[配置选项](../../../drivers/gpio/Kconfig)和[控制器绑定](../../../dts/bindings/gpio/gpio-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：设备树描述与运行配置：gpio_dt_spec保存端口设备指针、引脚编号及16位设备树标志；GPIO_DT_SPEC_GET_*展开为结构初始化器，不是动态申请的对象。带_OR的宏按属性索引是否存在选择回退值；gpio_is_ready_dt只检查端口设备就绪，不检查引脚范围、配置、电气连接或回退对象是否完整。gpio_pin_configure_dt才把dt_flags与extra_flags合并后执行配置。

> 译注——源码核对：物理与逻辑电平：raw接口使用物理电平，逻辑接口依据gpio_driver_data.invert转换。GPIO_OUTPUT_HIGH／LOW指定物理初始值，GPIO_OUTPUT_ACTIVE／INACTIVE指定逻辑初始值；低有效引脚的逻辑1对应物理低电平。读取失败时先处理负错误码，不能直接把任何非零返回都当高电平。gpio_pin_get_dt／set_dt只传端口与引脚，实际极性来自已经配置的驱动数据，而非每次直接读取spec->dt_flags。

> 译注——源码核对：配置失败的边界：gpio_pin_configure先转换逻辑初始值，并在调用驱动pin_configure之前修改invert掩码；当前包装在驱动失败后不恢复该掩码。因此错误返回不能证明硬件状态与软件极性都保持原状。配置、成功读回和引脚实际电平分别需要证据。

> 译注——源码核对：引脚索引与位掩码：gpio_port_pins_t和gpio_port_value_t是32位，gpio_pin_t是8位索引；BIT(pin)才是端口位掩码，二者不能互换。gpio_port_pin_is_supported先检查索引上限再检查port_pin_mask。配置、查询配置及中断配置保留运行期索引上限检查；许多其他内核包装仅通过断言检查支持范围，不能将所有入口都视为始终返回-EINVAL的参数校验器。用户态系统调用另有对象、支持范围与输出缓冲区访问检查。

> 译注——源码核对：保留引脚：gpio-reserved-ranges由起始偏移与长度成对组成，ngpios包含槽位范围内可能存在的空洞。GPIO_DT_RESERVED_RANGES_NGPIOS在不存在保留范围属性时返回0，不能单靠它表示所有允许引脚；GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC另外限制ngpios范围并排除保留位，ngpios为0时返回0。控制器掩码不能替代实际芯片封装和板级连接核对。

> 译注——源码核对：中断极性：GPIO_INT_EDGE_RISING／FALLING和GPIO_INT_LEVEL_HIGH／LOW使用物理电平，TO_ACTIVE／TO_INACTIVE及LEVEL_ACTIVE／INACTIVE使用已保存的低有效极性。中断_dt包装仅从dt_flags合入GPIO_INT_WAKEUP，没有重新应用GPIO_ACTIVE_LOW；应先正确配置引脚。GPIO_INT_EDGE_BOTH同时设置低／高触发位，但不设置GPIO_INT_LEVELS_LOGICAL，因此不会进入逻辑极性转换分支。普通配置中断可能清状态；保留配置的ENABLE_ONLY／DISABLE_ONLY另受CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT和驱动支持约束。

> 译注——源码核对：驱动能力与配置：CONFIG_GPIO_GET_CONFIG、CONFIG_GPIO_GET_DIRECTION以及仅使能／禁用中断的选项在本次Kconfig中标为实验性（Experimental）。启用选项不等于驱动实现对应操作。查询配置、查询方向、中断配置、回调管理与待处理中断查询的相关包装检查可选操作指针并可返回-ENOSYS；基础端口读写等包装直接调用操作，不能统一假定都有空指针回退。

> 译注——源码核对：回调不是中断开关：gpio_init_callback只写入handler和pin_mask，gpio_add_callback委托驱动管理回调，两者都不代替引脚中断配置。通用gpio_manage_callback移除再前插已有节点，删除不存在节点返回-EINVAL；gpio_fire_callbacks向处理函数传入触发引脚与关注掩码的交集。回调对象应在注册期间保持有效；辅助函数自身没有增加锁，安全遍历宏也不代表任意并发修改均安全。

> 译注——源码核对：端口批量操作：set／clear逻辑接口通过带掩码写入路径完成极性转换，set_clr要求两组掩码不重叠。toggle调用驱动翻转操作，物理与逻辑翻转方向一致；公共包装不执行读后再写。具体驱动如何实现、是否支持目标引脚以及实际电气结果，不能从公共函数签名单独推定。

> 译注——源码核对：版本边界：本批核对GPIO公共头文件、GPIO工具辅助头文件、设备树标志定义、系统调用处理、Kconfig及控制器绑定共六份官方源码并记录摘要。源码页的非注释代码与读取的官方头文件一致；latest、滚动main与仓库版本不自动相同。仓库定位使用相对链接，本次未构建固件、配置实板引脚或操作硬件。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.7\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/tracing/tracing.h](../tracing_headers_reference/P001_跟踪公共头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/dt-bindings/gpio/gpio.h](../dt_bus_binding_reference/P002_GPIO绑定常量头文件源码.md)
- [查看此文件的源码](P002_GPIO驱动头文件源码.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [gpio_driver_config](../hardware/P268_GPIO公共驱动配置.md)
- [gpio_driver_data](../hardware/P269_GPIO公共驱动数据.md)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [gpio_driver_api](../hardware/P272_GPIO驱动函数表.md)
- [GPIO_DT_SPEC_GET_BY_IDX](../hardware/P266_GPIO公共接口.md#gacb1077b77aecf8f1a9c7636ea583c4cf)
- [GPIO_DT_SPEC_GET_BY_IDX_OR](../hardware/P266_GPIO公共接口.md#ga3db4fa464e191016287f4c4d7eb9a983)
- [GPIO_DT_SPEC_GET](../hardware/P266_GPIO公共接口.md#ga2fa6bb5880f46984f9fc29c70f7d503e)
- [GPIO_DT_SPEC_GET_OR](../hardware/P266_GPIO公共接口.md#ga26b2205aa82819df1d80a22761352e71)
- [GPIO_DT_SPEC_INST_GET_BY_IDX](../hardware/P266_GPIO公共接口.md#gabbdbef450f14fd0af73667e2728ad084)
- [GPIO_DT_SPEC_INST_GET_BY_IDX_OR](../hardware/P266_GPIO公共接口.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)
- [GPIO_DT_SPEC_INST_GET](../hardware/P266_GPIO公共接口.md#ga168f5c6e39a0111191f606a9a0826e89)
- [GPIO_DT_SPEC_INST_GET_OR](../hardware/P266_GPIO公共接口.md#gae6b4a354c3cf0e042a390aac4bc37c69)
- [GPIO_DT_RESERVED_RANGES_NGPIOS](../hardware/P266_GPIO公共接口.md#ga439c3d29aa585b00853aba6d6416028a)
- [GPIO_DT_RESERVED_RANGES](../hardware/P266_GPIO公共接口.md#ga648fcc0633d57b52d3df683efda98440)
- [GPIO_DT_INST_RESERVED_RANGES_NGPIOS](../hardware/P266_GPIO公共接口.md#gaebaea00f6f7649c61651e8d50c7cdf07)
- [GPIO_DT_INST_RESERVED_RANGES](../hardware/P266_GPIO公共接口.md#ga9136b467eaddcc734bc6a0a7d8b34e14)
- [GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC](../hardware/P266_GPIO公共接口.md#ga274e09d7082d97b2f90c6a7fd4b71d49)
- [GPIO_DT_INST_PORT_PIN_MASK_NGPIOS_EXC](../hardware/P266_GPIO公共接口.md#ga856fe8042e496a39ef3a4e19fff2c4ce)
- [GPIO_MAX_PINS_PER_PORT](../hardware/P266_GPIO公共接口.md#ga1449ba90eaec5e6144fe4faae21f2e3f)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [GPIO_INPUT](../hardware/P266_GPIO公共接口.md#ga7be6a0cc9aa65da1d4ee5751b4085853)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)
- [GPIO_DISCONNECTED](../hardware/P266_GPIO公共接口.md#gaf82306c09450f6933366c4b821db21ed)
- [GPIO_OUTPUT_LOW](../hardware/P266_GPIO公共接口.md#gaf85baf9f9c1ba554324b4cd7064487b0)
- [GPIO_OUTPUT_HIGH](../hardware/P266_GPIO公共接口.md#ga10d31f204c0e927017d571352422fb09)
- [GPIO_OUTPUT_INACTIVE](../hardware/P266_GPIO公共接口.md#ga1e1d6be5f2f788f89468a0ce8b854634)
- [GPIO_OUTPUT_ACTIVE](../hardware/P266_GPIO公共接口.md#ga0f5cc126d6a690eb3e303eb29aa718ce)
- [GPIO_INT_MODE_ENABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688)
- [GPIO_INT_MODE_DISABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e)
- [GPIO_INT_DISABLE](../hardware/P266_GPIO公共接口.md#ga91657faac28f9b213105dd61a419dd5a)
- [GPIO_INT_EDGE_RISING](../hardware/P266_GPIO公共接口.md#gaed642a4e482f73aa917477370d0e241b)
- [GPIO_INT_EDGE_FALLING](../hardware/P266_GPIO公共接口.md#ga73bed10383a27d4a03feb300e64af8e8)
- [GPIO_INT_EDGE_BOTH](../hardware/P266_GPIO公共接口.md#ga10fa307ab17d02819108165a09f8e08b)
- [GPIO_INT_LEVEL_LOW](../hardware/P266_GPIO公共接口.md#gaddbb5ad576875af9c2d73b73df55c893)
- [GPIO_INT_LEVEL_HIGH](../hardware/P266_GPIO公共接口.md#ga233690d9a6a64bc9f804e3caa6d4a88f)
- [GPIO_INT_EDGE_TO_INACTIVE](../hardware/P266_GPIO公共接口.md#ga7b922529a3cb9396b0d82ca823e9d010)
- [GPIO_INT_EDGE_TO_ACTIVE](../hardware/P266_GPIO公共接口.md#ga35d2ff0e041236d82004a4bb2b5bf634)
- [GPIO_INT_LEVEL_INACTIVE](../hardware/P266_GPIO公共接口.md#gacb9bb1b63f172af2da7eb193e234c4f2)
- [GPIO_INT_LEVEL_ACTIVE](../hardware/P266_GPIO公共接口.md#gae51c68ff83959994bb942bb253505ca1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [gpio_callback_handler_t](../hardware/P266_GPIO公共接口.md#gaf0aa40279d32b1b8332f2f23a39510af)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_api_pin_configure_t](../hardware/P271_GPIO驱动后端.md#ga6e7f6f2052ba10b6482445faaef4245f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [gpio_api_pin_get_config_t](../hardware/P271_GPIO驱动后端.md#ga0b30055e6722031df85b712b6b151710)
- [gpio_api_port_get_raw_t](../hardware/P271_GPIO驱动后端.md#gad31b73d23fa7f6c96ec2f4a2523d61fb)
- [gpio_api_port_set_masked_raw_t](../hardware/P271_GPIO驱动后端.md#gab3d809d4ffbba78cfad45bcdb8f5ce5a)
- [gpio_api_port_set_bits_raw_t](../hardware/P271_GPIO驱动后端.md#gabca79087ebe1c21911ef9a80eaaee43e)
- [gpio_api_port_clear_bits_raw_t](../hardware/P271_GPIO驱动后端.md#ga43e339579ea19b4cc7d90a04c208e587)
- [gpio_api_port_toggle_bits_t](../hardware/P271_GPIO驱动后端.md#ga8486f9d9925531757b49e745ca7fdab2)
- [gpio_api_pin_interrupt_configure_t](../hardware/P271_GPIO驱动后端.md#gafa0e73e50f77890699cfe1a04ed9f155)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [gpio_api_manage_callback_t](../hardware/P271_GPIO驱动后端.md#ga2aaa71c0dd3728fdd2f8bd111245c456)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [gpio_api_get_pending_int_t](../hardware/P271_GPIO驱动后端.md#ga2a4ec98edb4dfb38cde49ab796fcbff3)
- [gpio_api_port_get_direction_t](../hardware/P271_GPIO驱动后端.md#ga5d175c3355e88ee78b08539b61fc84fd)
- [GPIO_INT_MODE_DISABLED](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3)
- [GPIO_INT_MODE_LEVEL](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9)
- [GPIO_INT_MODE_EDGE](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0)
- [GPIO_INT_TRIG_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134)
- [GPIO_INT_TRIG_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1)
- [GPIO_INT_TRIG_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8)
- [GPIO_INT_TRIG_WAKE](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223)
- [GPIO_INT_TRIG_WAKE_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6)
- [GPIO_INT_TRIG_WAKE_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4)
- [GPIO_INT_TRIG_WAKE_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5)
- [gpio_port_pin_is_supported](../hardware/P266_GPIO公共接口.md#gab7465c5401aa9d47d68980455847be9f)
- [gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)
- [gpio_pin_interrupt_configure](../hardware/P266_GPIO公共接口.md#ga9618f254365381063439a0e9c5e787cb)
- [gpio_pin_interrupt_configure_dt](../hardware/P266_GPIO公共接口.md#ga24f0b4ad30e6a8c81f51a2813478c793)
- [gpio_pin_configure](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)
- [gpio_pin_configure_dt](../hardware/P266_GPIO公共接口.md#ga423db4f985098ddcaa504ec430e91913)
- [gpio_port_get_direction](../hardware/P266_GPIO公共接口.md#gad2b2945dbe6987ac425e000721a894c4)
- [gpio_pin_is_input](../hardware/P266_GPIO公共接口.md#ga1454bc223fc2200aff3c4aab7d747da2)
- [gpio_pin_is_input_dt](../hardware/P266_GPIO公共接口.md#ga7aaec28a83cac63bd87fc94cc72664b1)
- [gpio_pin_is_output](../hardware/P266_GPIO公共接口.md#ga3b854d759180e222299ea445b401acc1)
- [gpio_pin_is_output_dt](../hardware/P266_GPIO公共接口.md#ga2255c5681d17952ab89a4b6016d8e80d)
- [gpio_pin_get_config](../hardware/P266_GPIO公共接口.md#ga133284b60a13c6dc50b87c1d04259f5e)
- [gpio_pin_get_config_dt](../hardware/P266_GPIO公共接口.md#ga820448aa4be8b14839bc6a00c9f34bb4)
- [gpio_port_get_raw](../hardware/P266_GPIO公共接口.md#gae2a49b36cae2e17fc665a3bd844f50b4)
- [gpio_port_get](../hardware/P266_GPIO公共接口.md#ga7c7a53371834c7646dc7f41ca0bb7921)
- [gpio_port_set_masked_raw](../hardware/P266_GPIO公共接口.md#ga9e7b50d720fda362941acc1e3b3b2922)
- [gpio_port_set_masked](../hardware/P266_GPIO公共接口.md#ga0c5ddbec7eb194ffed6cf12ae235ae04)
- [gpio_port_set_bits_raw](../hardware/P266_GPIO公共接口.md#ga18e6ca0df95566fecc0633efb04a075a)
- [gpio_port_set_bits](../hardware/P266_GPIO公共接口.md#gae450ff904686aa4b8fd81bc0dbbafdb5)
- [gpio_port_clear_bits_raw](../hardware/P266_GPIO公共接口.md#ga9d2c9daeec7ce127fc786ead566ad27f)
- [gpio_port_clear_bits](../hardware/P266_GPIO公共接口.md#ga9318c349663568f1fb9400b9458765dc)
- [gpio_port_toggle_bits](../hardware/P266_GPIO公共接口.md#ga82977d8706fb9f464db455bd0e9ac2e4)
- [gpio_port_set_clr_bits_raw](../hardware/P266_GPIO公共接口.md#ga1a06f729e76d39937d0572b6c531e038)
- [gpio_port_set_clr_bits](../hardware/P266_GPIO公共接口.md#ga45172f2b1bb09e8f3c89fa951cdefc14)
- [gpio_pin_get_raw](../hardware/P266_GPIO公共接口.md#ga635975f1df6157c7e8a6c67bac55fbc0)
- [gpio_pin_get](../hardware/P266_GPIO公共接口.md#ga496cd45fd6a2826c75d70c71f967234b)
- [gpio_pin_get_dt](../hardware/P266_GPIO公共接口.md#gaabeb2d0d98856c7ff78be36651d6bbc1)
- [gpio_pin_set_raw](../hardware/P266_GPIO公共接口.md#ga08824e05ea87c4ad2e48edaa13aad30a)
- [gpio_pin_set](../hardware/P266_GPIO公共接口.md#gadac09ef40fc1ba5d8bb40965efde0fda)
- [gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)
- [gpio_pin_toggle](../hardware/P266_GPIO公共接口.md#gaa761788e22a185db227dce7c24915154)
- [gpio_pin_toggle_dt](../hardware/P266_GPIO公共接口.md#ga3272e866489da6c2e12c48f803c59e81)
- [gpio_init_callback](../hardware/P266_GPIO公共接口.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)
- [gpio_add_callback](../hardware/P266_GPIO公共接口.md#ga05fd15af20386d69f9332354285b0cca)
- [gpio_add_callback_dt](../hardware/P266_GPIO公共接口.md#ga54845eb95bc9636c3e6ff285300b6979)
- [gpio_remove_callback](../hardware/P266_GPIO公共接口.md#gac1e94ba8faac79f469447e9b5d2f8c06)
- [gpio_remove_callback_dt](../hardware/P266_GPIO公共接口.md#ga2c9f8fee2addfc0aeeeeb011d534f304)
- [gpio_get_pending_int](../hardware/P266_GPIO公共接口.md#ga3f9e45de172a27f49c31a072c0c241e1)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_GPIO驱动头文件源码.md)
