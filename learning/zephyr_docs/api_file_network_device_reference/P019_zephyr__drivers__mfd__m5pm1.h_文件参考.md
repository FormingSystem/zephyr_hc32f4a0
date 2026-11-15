---
id: learning.zephyr-docs.api-file-network-device-reference.page-19
title: zephyr__drivers__mfd__m5pm1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/m5pm1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_mfd\_\_m5pm1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/m5pm1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

M5Stack M5PM1多功能设备（MFD）驱动的头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

M5Stack M5PM1多功能设备（MFD）驱动的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.1\_枚举（Enumerations）

<a id="r_ga6fd80cb688aac1023cd6450d83a73567"></a>

```c
enum m5pm1_pin_func { M5PM1_PIN_FUNC_GPIO = 0 , M5PM1_PIN_FUNC_IRQ , M5PM1_PIN_FUNC_ADC , M5PM1_PIN_FUNC_PWM , M5PM1_PIN_FUNC_NEOPIXEL }
```

相关声明：[m5pm1_pin_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga6fd80cb688aac1023cd6450d83a73567)、[M5PM1_PIN_FUNC_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a4f32a038ceb1e138261eb96c5a5beeb7)、[M5PM1_PIN_FUNC_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a77ee83c1164c2f4758024262a746839b)、[M5PM1_PIN_FUNC_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567acc8f1faa62f4652dcd6ec0d9a11740db)、[M5PM1_PIN_FUNC_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567ac1e5402b94c064949501a4b719fde33d)、[M5PM1_PIN_FUNC_NEOPIXEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a670d7b4c1f2a184c586a21ad493b7573)。

M5PM1 复用引脚（Multiplexed Pin）的语义功能（Semantic Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.2\_函数（Functions）

<a id="r_ga8ffcf8e07c86e9f92359ce7bd10582b2"></a>

```c
int mfd_m5pm1_read_reg (const struct device *dev, uint8_t reg, uint8_t *val)
```

相关声明：[mfd_m5pm1_read_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga8ffcf8e07c86e9f92359ce7bd10582b2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取一个 8 位 M5PM1 寄存器（Register）。

<a id="r_ga2d0904fa61bedeaf9701b0452569ddb2"></a>

```c
int mfd_m5pm1_write_reg (const struct device *dev, uint8_t reg, uint8_t val)
```

相关声明：[mfd_m5pm1_write_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga2d0904fa61bedeaf9701b0452569ddb2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入一个 8 位 M5PM1 寄存器（Register）。

<a id="r_ga23c99b53cbff717dc6f754bd007e1d7a"></a>

```c
int mfd_m5pm1_update_reg (const struct device *dev, uint8_t reg, uint8_t mask, uint8_t val)
```

相关声明：[mfd_m5pm1_update_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga23c99b53cbff717dc6f754bd007e1d7a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对 M5PM1 寄存器的选定位执行读－改－写（Read-modify-write）。

<a id="r_ga126cab6d565399da89293d7fb210354a"></a>

```c
int mfd_m5pm1_toggle_reg (const struct device *dev, uint8_t reg, uint8_t mask)
```

相关声明：[mfd_m5pm1_toggle_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga126cab6d565399da89293d7fb210354a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

翻转（Toggle）M5PM1 寄存器中的选定位。

<a id="r_gab26e112c7ea5e6349f92d2385e9a7076"></a>

```c
int mfd_m5pm1_burst_read (const struct device *dev, uint8_t reg, uint8_t *buf, size_t len)
```

相关声明：[mfd_m5pm1_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gab26e112c7ea5e6349f92d2385e9a7076)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在一次 I2C 事务（Transaction）中读取多个连续的 M5PM1 寄存器。

<a id="r_ga0d1db367f7e6a344ef017c0ddaa878ac"></a>

```c
int mfd_m5pm1_burst_write (const struct device *dev, uint8_t reg, const uint8_t *buf, size_t len)
```

相关声明：[mfd_m5pm1_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga0d1db367f7e6a344ef017c0ddaa878ac)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在一次 I2C 事务（Transaction）中写入多个连续的 M5PM1 寄存器。

<a id="r_gac38c4a90a406952ac7239ccd42fc4439"></a>

```c
int mfd_m5pm1_pin_request (const struct device *dev, const struct device *client, uint8_t pin, enum m5pm1_pin_func func)
```

相关声明：[mfd_m5pm1_pin_request](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gac38c4a90a406952ac7239ccd42fc4439)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[m5pm1_pin_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga6fd80cb688aac1023cd6450d83a73567)。

代表同级驱动（Sibling Driver）为指定功能申请占用引脚（Claim a Pin）。

<a id="r_gad00cc2f47ef55facd42040435bc22fc0"></a>

```c
int mfd_m5pm1_pin_release (const struct device *dev, const struct device *client, uint8_t pin)
```

相关声明：[mfd_m5pm1_pin_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gad00cc2f47ef55facd42040435bc22fc0)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

释放此前通过 `mfd_m5pm1_pin_request()` 申请的引脚。


## 19.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P470_m5pm1.h_源码浏览.md)
- [m5pm1_pin_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga6fd80cb688aac1023cd6450d83a73567)
- [M5PM1_PIN_FUNC_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a4f32a038ceb1e138261eb96c5a5beeb7)
- [M5PM1_PIN_FUNC_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a77ee83c1164c2f4758024262a746839b)
- [M5PM1_PIN_FUNC_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567acc8f1faa62f4652dcd6ec0d9a11740db)
- [M5PM1_PIN_FUNC_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567ac1e5402b94c064949501a4b719fde33d)
- [M5PM1_PIN_FUNC_NEOPIXEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gga6fd80cb688aac1023cd6450d83a73567a670d7b4c1f2a184c586a21ad493b7573)
- [mfd_m5pm1_read_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga8ffcf8e07c86e9f92359ce7bd10582b2)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_m5pm1_write_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga2d0904fa61bedeaf9701b0452569ddb2)
- [mfd_m5pm1_update_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga23c99b53cbff717dc6f754bd007e1d7a)
- [mfd_m5pm1_toggle_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga126cab6d565399da89293d7fb210354a)
- [mfd_m5pm1_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gab26e112c7ea5e6349f92d2385e9a7076)
- [mfd_m5pm1_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#ga0d1db367f7e6a344ef017c0ddaa878ac)
- [mfd_m5pm1_pin_request](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gac38c4a90a406952ac7239ccd42fc4439)
- [mfd_m5pm1_pin_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html#gad00cc2f47ef55facd42040435bc22fc0)

<a id="header-details"></a>

---

[上一章](P018_zephyr__dt-bindings__sensor__lis2du12.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__pinctrl__max32-pinctrl.h_文件参考.md)
