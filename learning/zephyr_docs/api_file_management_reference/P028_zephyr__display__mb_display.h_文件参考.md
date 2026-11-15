---
id: learning.zephyr-docs.api-file-management-reference.page-28
title: zephyr__display__mb_display.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_display\_\_mb\_display.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BBC micro:bit显示（Display）的API。

<a id="details"></a>

```c
#include <stdio.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

BBC micro:bit显示（Display）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

<a id="r_mb_5Fimage"></a>

```c
struct mb_image
```

相关声明：[mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)。

BBC micro:bit显示图像（Display Image）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.2\_宏定义（Macros）

<a id="r_ga529a5650acaf699b23b4b4234127cf2c"></a>

```c
#define MB_IMAGE(_rows...)
```

相关声明：[MB_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga529a5650acaf699b23b4b4234127cf2c)。

根据给定数组的行／列生成图像对象（image object）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 28.3\_枚举（Enumerations）

<a id="r_ga750a177cffbb90ab38392d9ebad9a8eb"></a>

```c
enum mb_display_mode { MB_DISPLAY_MODE_DEFAULT , MB_DISPLAY_MODE_SINGLE , MB_DISPLAY_MODE_SCROLL , MB_DISPLAY_FLAG_LOOP = BIT(16) }
```

相关声明：[mb_display_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga750a177cffbb90ab38392d9ebad9a8eb)、[MB_DISPLAY_MODE_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5)、[MB_DISPLAY_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a)、[MB_DISPLAY_MODE_SCROLL](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69)、[MB_DISPLAY_FLAG_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc)。

显示模式（display mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.4\_函数（Functions）

<a id="r_ga94e3eadd1cf386b8d9494ccfa8afaa40"></a>

```c
struct mb_display * mb_display_get (void)
```

相关声明：[mb_display_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga94e3eadd1cf386b8d9494ccfa8afaa40)。

获取指向 BBC micro:bit 显示对象的指针。

<a id="r_ga2a6e20d57d0d65033281dd7c3ea19126"></a>

```c
void mb_display_image (struct mb_display *disp, uint32_t mode, int32_t duration, const struct mb_image *img, uint8_t img_count)
```

相关声明：[mb_display_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga2a6e20d57d0d65033281dd7c3ea19126)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在 BBC micro:bit LED 显示屏上显示一个或多个图像。

<a id="r_ga993a6a0225206f53170d25d9177c1225"></a>

```c
void mb_display_print (struct mb_display *disp, uint32_t mode, int32_t duration, const char *fmt,...)
```

相关声明：[mb_display_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga993a6a0225206f53170d25d9177c1225)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

在 BBC micro:bit LED 显示屏上打印字符串。

<a id="r_gad15b3635993007d8aad9364cbe29311b"></a>

```c
void mb_display_stop (struct mb_display *disp)
```

相关声明：[mb_display_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gad15b3635993007d8aad9364cbe29311b)。

停止当前进行中的图像显示。


## 28.5\_原页交叉引用（Cross References）

- [stdio.h](../api_source_system_reference/P042_stdio.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P104_mb_display.h_源码浏览.md)
- [mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)
- [MB_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga529a5650acaf699b23b4b4234127cf2c)
- [mb_display_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga750a177cffbb90ab38392d9ebad9a8eb)
- [MB_DISPLAY_MODE_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5)
- [MB_DISPLAY_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a)
- [MB_DISPLAY_MODE_SCROLL](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69)
- [MB_DISPLAY_FLAG_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc)
- [mb_display_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga94e3eadd1cf386b8d9494ccfa8afaa40)
- [mb_display_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga2a6e20d57d0d65033281dd7c3ea19126)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mb_display_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga993a6a0225206f53170d25d9177c1225)
- [mb_display_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#gad15b3635993007d8aad9364cbe29311b)

<a id="header-details"></a>

---

[上一章](P027_zephyr__dt-bindings__pinctrl__lpc11u6x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__dt-bindings__interrupt-controller__mchp-xec-ecia.h_文件参考.md)
