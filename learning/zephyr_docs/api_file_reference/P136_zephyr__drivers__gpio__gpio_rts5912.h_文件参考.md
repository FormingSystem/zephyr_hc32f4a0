---
id: learning.zephyr-docs.api-file-reference.page-136
title: zephyr__drivers__gpio__gpio_rts5912.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_rts5912.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <reg/reg_gpio.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 136.1\_函数（Functions）

<a id="r_acfacb1e55d774da53cab6e9fda59c25b"></a>

```c
gpio_pin_t gpio_rts5912_get_intr_pin (volatile uint32_t *reg_base)
```

相关声明：[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_rts5912_get_intr_pin](#acfacb1e55d774da53cab6e9fda59c25b)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a8640c6a53deb21cee7bc6be80b1581df"></a>

```c
static ALWAYS_INLINE void gpio_rts5912_set_wakeup_pin (uint32_t pin_num)
```

相关声明：[gpio_rts5912_set_wakeup_pin](#a8640c6a53deb21cee7bc6be80b1581df)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a955c6e7b8922a236de987c66596d28b2"></a>

```c
int gpio_rts5912_get_pin_num (const struct gpio_dt_spec *gpio)
```

相关声明：[gpio_rts5912_get_pin_num](#a955c6e7b8922a236de987c66596d28b2)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

<a id="r_a62065211bcb72d822eeccccc6e51dc51"></a>

```c
uint32_t * gpio_rts5912_get_port_address (const struct gpio_dt_spec *gpio)
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[gpio_rts5912_get_port_address](#a62065211bcb72d822eeccccc6e51dc51)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

## 136.2\_详细说明（Detailed Documentation）

<a id="acfacb1e55d774da53cab6e9fda59c25b"></a>

### `gpio_rts5912_get_intr_pin()`

```c
gpio_pin_t gpio_rts5912_get_intr_pin ( volatile uint32_t * reg_base)
```

<a id="a955c6e7b8922a236de987c66596d28b2"></a>

### `gpio_rts5912_get_pin_num()`

```c
int gpio_rts5912_get_pin_num ( const struct gpio_dt_spec * gpio)
```

<a id="a62065211bcb72d822eeccccc6e51dc51"></a>

### `gpio_rts5912_get_port_address()`

```c
uint32_t * gpio_rts5912_get_port_address ( const struct gpio_dt_spec * gpio)
```

<a id="a8640c6a53deb21cee7bc6be80b1581df"></a>

### `gpio_rts5912_set_wakeup_pin()`

```c
ALWAYS_INLINE void gpio_rts5912_set_wakeup_pin ( uint32_t pin_num)
```

声明属性：`static`。


## 136.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P082_gpio_rts5912.h_源码浏览.md)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P135_zephyr__drivers__gpio__gpio_intel.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P137_zephyr__posix__grp.h_文件参考.md)
