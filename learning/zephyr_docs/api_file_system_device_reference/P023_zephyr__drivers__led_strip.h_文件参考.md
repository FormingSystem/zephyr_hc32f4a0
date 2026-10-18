---
id: learning.zephyr-docs.api-file-system-device-reference.page-23
title: zephyr__drivers__led_strip.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_led\_strip.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/led__strip_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LED灯带（LED Strip）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
```

查看此文件的源码。

LED 灯带驱动 API（LED strip driver API）的主头文件。本库对可逐个寻址的 LED 灯带所用芯片组驱动进行抽象。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_led_5Frgb"></a>

```c
struct led_rgb
```

相关声明：[led_rgb](../hardware/P209_LED灯带颜色结构.md)。

单个RGB LED的颜色值（Color Value）。

<a id="r_led_5Fstrip_5Fdriver_5Fapi"></a>

```c
struct led_strip_driver_api
```

相关声明：[led_strip_driver_api](../hardware/P211_LED灯带驱动函数表.md)。

驱动操作（Driver Operations）：LED灯带（LED Strip）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.2\_类型定义（Typedefs）

<a id="r_gaa36be40a962173021a547192d0d39151"></a>

```c
typedef int(* led_api_update_rgb) (const struct device *dev, struct led_rgb *pixels, size_t num_pixels)
```

相关声明：[led_api_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gaa36be40a962173021a547192d0d39151)、[device](../device_reference/P002_设备对象结构.md)、[led_rgb](../hardware/P209_LED灯带颜色结构.md)。

用于更新 RGB LED 灯带的回调 API。

<a id="r_gab11579a7b5b7febfd48fa12560254501"></a>

```c
typedef int(* led_api_update_channels) (const struct device *dev, uint8_t *channels, size_t num_channels)
```

相关声明：[led_api_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gab11579a7b5b7febfd48fa12560254501)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于直接更新通道、不按 RGB 解释数据的回调 API。

<a id="r_ga3487e5d4a339898f88a225bb3678776b"></a>

```c
typedef size_t(* led_api_length) (const struct device *dev)
```

相关声明：[led_api_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#ga3487e5d4a339898f88a225bb3678776b)、[device](../device_reference/P002_设备对象结构.md)。

用于获取 LED 灯带长度的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.3\_函数（Functions）

<a id="r_ga6e63331a5be2430968ab8b60692f8d67"></a>

```c
static int led_strip_update_rgb (const struct device *dev, struct led_rgb *pixels, size_t num_pixels)
```

相关声明：[led_strip_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga6e63331a5be2430968ab8b60692f8d67)、[device](../device_reference/P002_设备对象结构.md)、[led_rgb](../hardware/P209_LED灯带颜色结构.md)。

使用给定 RGB 数组更新 LED 灯带。

<a id="r_ga846b1d37bc6f7ed2014bea9603788b34"></a>

```c
static int led_strip_update_channels (const struct device *dev, uint8_t *channels, size_t num_channels)
```

相关声明：[led_strip_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga846b1d37bc6f7ed2014bea9603788b34)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用给定通道数组更新 LED 灯带。

<a id="r_ga7f94eab0b357a81cccb5f0ea1575714a"></a>

```c
static size_t led_strip_length (const struct device *dev)
```

相关声明：[led_strip_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a)、[device](../device_reference/P002_设备对象结构.md)。

获取 LED 灯带设备的链长度（chain length），单位为像素。


## 23.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P037_led_strip.h_源码浏览.md)
- [led_rgb](../hardware/P209_LED灯带颜色结构.md)
- [led_strip_driver_api](../hardware/P211_LED灯带驱动函数表.md)
- [led_api_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gaa36be40a962173021a547192d0d39151)
- [device](../device_reference/P002_设备对象结构.md)
- [led_api_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gab11579a7b5b7febfd48fa12560254501)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [led_api_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#ga3487e5d4a339898f88a225bb3678776b)
- [led_strip_update_rgb](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga6e63331a5be2430968ab8b60692f8d67)
- [led_strip_update_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga846b1d37bc6f7ed2014bea9603788b34)
- [led_strip_length](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__led__led_fake.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__dt-bindings__sensor__lps22hh.h_文件参考.md)
