---
id: learning.zephyr-docs.api-file-system-device-reference.page-22
title: zephyr__drivers__led__led_fake.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_led\_\_led\_fake.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟LED控制器（Fake LED Controller）驱动的API函数。

<a id="details"></a>

```c
#include <zephyr/drivers/led.h>
#include <zephyr/fff.h>
```

查看此文件的源码。

模拟LED控制器（Fake LED Controller）驱动的API函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_gab6d86a816ed9dcd8d393126a8dc3d2dd"></a>

```c
int fake_led_on (const struct device *, uint32_t)
```

相关声明：[fake_led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gab6d86a816ed9dcd8d393126a8dc3d2dd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

`led_driver_api::on` 驱动操作的替身实现（fake implementation）。

<a id="r_ga4475c7869fd8ab92c5b7fea4ec3c1a3d"></a>

```c
int fake_led_off (const struct device *, uint32_t)
```

相关声明：[fake_led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga4475c7869fd8ab92c5b7fea4ec3c1a3d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

`led_driver_api::off` 驱动操作的替身实现（fake implementation）。

<a id="r_ga68b14d1f205726941cb591f177ef89af"></a>

```c
int fake_led_set_brightness (const struct device *, uint32_t, uint8_t)
```

相关声明：[fake_led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga68b14d1f205726941cb591f177ef89af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`led_driver_api::set_brightness` 驱动操作的替身实现（fake implementation）。

<a id="r_ga276f41b4376784bf588d7785afdffd56"></a>

```c
int fake_led_blink (const struct device *, uint32_t, uint32_t, uint32_t)
```

相关声明：[fake_led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga276f41b4376784bf588d7785afdffd56)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

`led_driver_api::blink` 驱动操作的替身实现（fake implementation）。

<a id="r_gae4f88da2cfa43c93bc0f2d294b6f848e"></a>

```c
int fake_led_get_info (const struct device *, uint32_t, const struct led_info **)
```

相关声明：[fake_led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gae4f88da2cfa43c93bc0f2d294b6f848e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[led_info](../hardware/P204_LED信息结构.md)。

`led_driver_api::get_info` 驱动操作的替身实现（fake implementation）。

<a id="r_ga1860bf2d9d105ee8ecb7a092e2017b63"></a>

```c
int fake_led_set_color (const struct device *, uint32_t, uint8_t, const uint8_t *)
```

相关声明：[fake_led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga1860bf2d9d105ee8ecb7a092e2017b63)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`led_driver_api::set_color` 驱动操作的替身实现（fake implementation）。

<a id="r_gacf6109ac62eafca13ab6b56fb4676877"></a>

```c
int fake_led_write_channels (const struct device *, uint32_t, uint32_t, const uint8_t *)
```

相关声明：[fake_led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gacf6109ac62eafca13ab6b56fb4676877)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`led_driver_api::write_channels` 驱动操作的替身实现（fake implementation）。


## 22.2\_原页交叉引用（Cross References）

- [zephyr/drivers/led.h](../api_source_supplement_reference/P042_led.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P438_led_fake.h_源码浏览.md)
- [fake_led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gab6d86a816ed9dcd8d393126a8dc3d2dd)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [led_driver_api::on](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9ce7322282f8c525256d3c16a514ecc4)
- [fake_led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga4475c7869fd8ab92c5b7fea4ec3c1a3d)
- [led_driver_api::off](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a19ad736a130da2aff6bd5b299d8c33a7)
- [fake_led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga68b14d1f205726941cb591f177ef89af)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [led_driver_api::set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9c3e3c4d40c4b8219755df6df96b0058)
- [fake_led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga276f41b4376784bf588d7785afdffd56)
- [led_driver_api::blink](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#af1974c5cc20c818e0e387b34cd14ac3b)
- [fake_led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gae4f88da2cfa43c93bc0f2d294b6f848e)
- [led_info](../hardware/P204_LED信息结构.md)
- [led_driver_api::get_info](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a7c68219e44bcf6e766e64fd3967ecf7e)
- [fake_led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga1860bf2d9d105ee8ecb7a092e2017b63)
- [led_driver_api::set_color](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a336f30f2c1bd3d99213cae66911c142a)
- [fake_led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gacf6109ac62eafca13ab6b56fb4676877)
- [led_driver_api::write_channels](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#ada1dfb1830b48afb020c7e60dbd92337)

<a id="header-details"></a>

---

[上一章](P021_zephyr__drivers__led__is31fl3733.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__led_strip.h_文件参考.md)
