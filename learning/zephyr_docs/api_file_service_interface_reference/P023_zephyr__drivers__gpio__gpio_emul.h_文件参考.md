---
id: learning.zephyr-docs.api-file-service-interface-reference.page-23
title: zephyr__drivers__gpio__gpio_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

仿真GPIO（Emulated GPIO）的后端API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

仿真GPIO（Emulated GPIO）的后端API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_gaa7eae6a0f85d0f0fb6a8aa41329f4709"></a>

```c
int gpio_emul_input_set_masked (const struct device *port, gpio_port_pins_t pins, gpio_port_value_t values)
```

相关声明：[gpio_emul_input_set_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa7eae6a0f85d0f0fb6a8aa41329f4709)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

修改一个或多个仿真 GPIO 输入引脚的值。

<a id="r_ga3962e337bc22e532f2c181724621fcf8"></a>

```c
static int gpio_emul_input_set (const struct device *port, gpio_pin_t pin, int value)
```

相关声明：[gpio_emul_input_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

修改一个仿真 GPIO 输入引脚的值。

<a id="r_gab937159126e992126de136f6b1523191"></a>

```c
static int gpio_emul_input_set_dt (const struct gpio_dt_spec *spec, int value)
```

相关声明：[gpio_emul_input_set_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gab937159126e992126de136f6b1523191)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

根据 `gpio_dt_spec` 修改一个仿真 GPIO 输入引脚的值。

<a id="r_gaa6e4c5c2c53d421e9635c0a977172205"></a>

```c
int gpio_emul_output_get_masked (const struct device *port, gpio_port_pins_t pins, gpio_port_value_t *values)
```

相关声明：[gpio_emul_output_get_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa6e4c5c2c53d421e9635c0a977172205)、[device](../device_reference/P002_设备对象结构.md)、[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)、[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

读取一个或多个仿真 GPIO 输出引脚的值。

<a id="r_gaa62613aa6eb442d2c4e436893316124f"></a>

```c
static int gpio_emul_output_get (const struct device *port, gpio_pin_t pin)
```

相关声明：[gpio_emul_output_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa62613aa6eb442d2c4e436893316124f)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

读取一个仿真 GPIO 输出引脚的值。

<a id="r_ga5fdc3ebb295074bb5befeaaa75f05da0"></a>

```c
static int gpio_emul_output_get_dt (const struct gpio_dt_spec *spec)
```

相关声明：[gpio_emul_output_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga5fdc3ebb295074bb5befeaaa75f05da0)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

根据 `gpio_dt_spec` 读取一个仿真 GPIO 输出引脚的值。

<a id="r_ga86bd5ff4f557e4d520a4f760fb74cdd5"></a>

```c
int gpio_emul_flags_get (const struct device *port, gpio_pin_t pin, gpio_flags_t *flags)
```

相关声明：[gpio_emul_flags_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga86bd5ff4f557e4d520a4f760fb74cdd5)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取指定仿真 GPIO 引脚的标志（Flags）。

<a id="r_ga781faaeb7570b8cc1095ebe99c3efdf9"></a>

```c
static int gpio_emul_flags_get_dt (const struct gpio_dt_spec *spec, gpio_flags_t *flags)
```

相关声明：[gpio_emul_flags_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga781faaeb7570b8cc1095ebe99c3efdf9)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

根据 `gpio_dt_spec` 获取指定仿真 GPIO 引脚的标志（Flags）。


## 23.2\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P296_gpio_emul.h_源码浏览.md)
- [gpio_emul_input_set_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa7eae6a0f85d0f0fb6a8aa41329f4709)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)
- [gpio_emul_input_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [gpio_emul_input_set_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gab937159126e992126de136f6b1523191)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [gpio_emul_output_get_masked](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa6e4c5c2c53d421e9635c0a977172205)
- [gpio_emul_output_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa62613aa6eb442d2c4e436893316124f)
- [gpio_emul_output_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga5fdc3ebb295074bb5befeaaa75f05da0)
- [gpio_emul_flags_get](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga86bd5ff4f557e4d520a4f760fb74cdd5)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [gpio_emul_flags_get_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga781faaeb7570b8cc1095ebe99c3efdf9)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__gpio__gpio_bl61x_wo.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__mgmt__hawkbit__hawkbit.h_文件参考.md)
