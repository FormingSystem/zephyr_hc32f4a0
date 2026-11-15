---
id: learning.zephyr-docs.hardware.gpiobackend-2
title: GPIO模拟接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第273章\_GPIO模拟接口

原文：[group__gpio__emul](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html)。读取日期：2026-10-13，`latest`。

## 273.1\_应用定义的模拟行为

本页提供模拟通用输入/输出（Emulated General Purpose Input/Output，Emulated GPIO）的后端接口，声明来自 `zephyr/drivers/gpio/gpio_emul.h`。模拟行为由应用定义，每个应用可以：

- 编写设备树覆盖文件（Devicetree Overlay），指定GPIO控制器数量及每个控制器的引脚数量。
- 用 [`gpio_add_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga05fd15af20386d69f9332354285b0cca) 向控制器注册回调（Callback），模拟“接线”（Wiring）。
- 异步调用 [`gpio_emul_input_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8) 和/或 [`gpio_emul_input_set_masked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa7eae6a0f85d0f0fb6a8aa41329f4709)，模拟GPIO事件。

官方覆盖文件示例位于 `tests/drivers/gpio/gpio_basic_api/boards/native_sim.overlay`。注册回调模拟接线及调用输入设置函数的示例位于 `tests/drivers/gpio/gpio_basic_api/src/main.c`。

下文 `port` 为模拟GPIO端口，`pin` 为对应引脚，`spec` 为设备树中的模拟GPIO描述。错误码 `-EINVAL` 表示参数无效；可用配置标志见[GPIO公共接口](P266_GPIO公共接口.md)。

## 273.2\_gpio_emul_flags_get

函数 [`gpio_emul_flags_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga86bd5ff4f557e4d520a4f760fb74cdd5) 声明为：

```c
int gpio_emul_flags_get(const struct device * port, gpio_pin_t pin, gpio_flags_t * flags);
```

取得指定模拟引脚的配置标志，保存在 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 指向的位置。成功返回 `0`，参数无效返回 `-EINVAL`。

## 273.3\_gpio_emul_flags_get_dt

函数 [`gpio_emul_flags_get_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga781faaeb7570b8cc1095ebe99c3efdf9) 声明为：

```c
static inline int gpio_emul_flags_get_dt(const struct gpio_dt_spec * spec, gpio_flags_t * flags);
```

从设备树描述取得模拟引脚配置标志，保存在 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 指向的位置。返回 [`gpio_emul_flags_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga86bd5ff4f557e4d520a4f760fb74cdd5) 的结果，等价调用为：

```c
gpio_emul_flags_get(spec->port, spec->pin, flags);
```

## 273.4\_gpio_emul_input_set

函数 [`gpio_emul_input_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8) 声明为：

```c
static inline int gpio_emul_input_set(const struct device * port, gpio_pin_t pin, int value);
```

修改一个模拟输入引脚的值，`value` 为要赋给引脚的新值。成功返回 `0`，参数无效返回 `-EINVAL`。

## 273.5\_gpio_emul_input_set_dt

函数 [`gpio_emul_input_set_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gab937159126e992126de136f6b1523191) 声明为：

```c
static inline int gpio_emul_input_set_dt(const struct gpio_dt_spec * spec, int value);
```

从设备树描述修改模拟输入引脚值，`value` 为新值。返回 [`gpio_emul_input_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga3962e337bc22e532f2c181724621fcf8) 的结果，等价调用为：

```c
gpio_emul_input_set(spec->port, spec->pin, value);
```

## 273.6\_gpio_emul_input_set_masked

函数 [`gpio_emul_input_set_masked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa7eae6a0f85d0f0fb6a8aa41329f4709) 声明为：

```c
int gpio_emul_input_set_masked(const struct device * port, gpio_port_pins_t pins, gpio_port_value_t values);
```

修改一个或多个模拟输入引脚的值。`pins` 为发生变化的引脚掩码（Pin Mask），`values` 为要赋给这些引脚的新值。成功返回 `0`，参数无效返回 `-EINVAL`。

## 273.7\_gpio_emul_output_get

函数 [`gpio_emul_output_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa62613aa6eb442d2c4e436893316124f) 声明为：

```c
static inline int gpio_emul_output_get(const struct device * port, gpio_pin_t pin);
```

读取一个模拟输出引脚的值。成功返回 `0` 或 `1`，参数无效返回 `-EINVAL`。

## 273.8\_gpio_emul_output_get_dt

函数 [`gpio_emul_output_get_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#ga5fdc3ebb295074bb5befeaaa75f05da0) 声明为：

```c
static inline int gpio_emul_output_get_dt(const struct gpio_dt_spec * spec);
```

从设备树描述读取一个模拟输出引脚的值，返回 [`gpio_emul_output_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa62613aa6eb442d2c4e436893316124f) 的结果，等价调用为：

```c
gpio_emul_output_get(spec->port, spec->pin);
```

## 273.9\_gpio_emul_output_get_masked

函数 [`gpio_emul_output_get_masked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html#gaa6e4c5c2c53d421e9635c0a977172205) 声明为：

```c
int gpio_emul_output_get_masked(const struct device * port, gpio_port_pins_t pins, gpio_port_value_t * values);
```

读取一个或多个模拟输出引脚的值。`pins` 为引脚掩码，原参数说明称其为“发生变化的引脚”；`values` 指向保存这些引脚值的位置。成功返回 `0`，参数无效返回 `-EINVAL`。


---

[上一章：GPIO驱动函数表](P272_GPIO驱动函数表.md) · [下一章：GPIO器件扩展目录](P274_GPIO器件扩展目录.md) · [返回大纲](大纲.md)
