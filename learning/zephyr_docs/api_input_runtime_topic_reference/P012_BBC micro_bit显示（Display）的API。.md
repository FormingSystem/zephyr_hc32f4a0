---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-12
title: BBC micro_bit显示（Display）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_BBC micro\_bit显示（Display）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BBC micro:bit显示（Display）的API。

<a id="details"></a>

BBC micro:bit显示（Display）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_mb_5Fimage"></a>

```c
struct mb_image
```

相关声明：[mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)。

BBC micro:bit显示图像（Display Image）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_ga529a5650acaf699b23b4b4234127cf2c"></a>

```c
#define MB_IMAGE(_rows...)
```

相关声明：[MB_IMAGE](#ga529a5650acaf699b23b4b4234127cf2c)。

根据给定数组的行／列生成图像对象（image object）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_ga750a177cffbb90ab38392d9ebad9a8eb"></a>

```c
enum mb_display_mode { MB_DISPLAY_MODE_DEFAULT , MB_DISPLAY_MODE_SINGLE , MB_DISPLAY_MODE_SCROLL , MB_DISPLAY_FLAG_LOOP = BIT(16) }
```

相关声明：[mb_display_mode](#ga750a177cffbb90ab38392d9ebad9a8eb)、[MB_DISPLAY_MODE_DEFAULT](#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5)、[MB_DISPLAY_MODE_SINGLE](#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a)、[MB_DISPLAY_MODE_SCROLL](#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69)、[MB_DISPLAY_FLAG_LOOP](#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc)。

显示模式（display mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ga94e3eadd1cf386b8d9494ccfa8afaa40"></a>

```c
struct mb_display * mb_display_get (void)
```

相关声明：[mb_display_get](#ga94e3eadd1cf386b8d9494ccfa8afaa40)。

获取指向 BBC micro:bit 显示对象的指针。

<a id="r_ga2a6e20d57d0d65033281dd7c3ea19126"></a>

```c
void mb_display_image (struct mb_display *disp, uint32_t mode, int32_t duration, const struct mb_image *img, uint8_t img_count)
```

相关声明：[mb_display_image](#ga2a6e20d57d0d65033281dd7c3ea19126)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在 BBC micro:bit LED 显示屏上显示一个或多个图像。

<a id="r_ga993a6a0225206f53170d25d9177c1225"></a>

```c
void mb_display_print (struct mb_display *disp, uint32_t mode, int32_t duration, const char *fmt,...)
```

相关声明：[mb_display_print](#ga993a6a0225206f53170d25d9177c1225)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

在 BBC micro:bit LED 显示屏上打印字符串。

<a id="r_gad15b3635993007d8aad9364cbe29311b"></a>

```c
void mb_display_stop (struct mb_display *disp)
```

相关声明：[mb_display_stop](#gad15b3635993007d8aad9364cbe29311b)。

停止当前进行中的图像显示。

## 12.5\_详细说明（Detailed Documentation）

<a id="ga529a5650acaf699b23b4b4234127cf2c"></a>

### `MB_IMAGE`

```c
#define MB_IMAGE ( _rows...)
```

```c
#include <zephyr/display/mb_display.h>
```

展开值（Value）：

```c
{ .r = { _rows } }
```

根据给定数组的行／列生成图像对象（image object）。

此辅助接口接受一个包含 5 行的数组，每行由 5 个 `0`／`1` 值组成，对应该行各列。`0` 表示关闭像素（Pixel Disabled），`1` 表示点亮像素（Pixel Enabled）。

像素从左到右、从上到下排列：左上角是第一行的第一个值，右上角是第一行的最后一个值，右下角是最后一行（第 5 行）的最后一个值。例如，下方代码创建笑脸图像（Smiley Face Image）：

原始示例（Example）：

```c

static const struct mb_image smiley = MB_IMAGE({ 0, 1, 0, 1, 0 },
                                          { 0, 1, 0, 1, 0 },
                                          { 0, 0, 0, 0, 0 },
                                          { 1, 0, 0, 0, 1 },
                                          { 0, 1, 1, 1, 0 });
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_rows` | 5 行中的每一行，表示为包含 5 个列值的数组（Column Array）。 |

**返回（Returns）**：**返回值（Returns）：**图像位图（Image Bitmap），可传给 `mb_display_image()` 等函数。

<a id="ga750a177cffbb90ab38392d9ebad9a8eb"></a>

### `mb_display_mode`

```c
enum mb_display_mode
```

```c
#include <zephyr/display/mb_display.h>
```

显示模式（display mode）。

前 16 位保留给模式（Modes），后 16 位用于标志（Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MB_DISPLAY_MODE_DEFAULT` | 默认模式（Default Mode）：图像使用“单张”（Single），文本使用“滚动”（Scroll）。 |
| `MB_DISPLAY_MODE_SINGLE` | 依次显示图像（Images），一次一张。 |
| `MB_DISPLAY_MODE_SCROLL` | 以滚动（Scrolling）方式显示图像。 |
| `MB_DISPLAY_FLAG_LOOP` | 到达最后一张图像时循环回到开头（Loop Back）。 |

<a id="ga94e3eadd1cf386b8d9494ccfa8afaa40"></a>

### `mb_display_get()`

```c
struct mb_display * mb_display_get ( void )
```

```c
#include <zephyr/display/mb_display.h>
```

获取指向 BBC micro:bit 显示对象的指针。

**返回（Returns）**：**返回值（Returns）：**显示对象（Display Object）指针。

<a id="ga2a6e20d57d0d65033281dd7c3ea19126"></a>

### `mb_display_image()`

```c
void mb_display_image ( struct mb_display * disp, uint32_t mode, int32_t duration, const struct mb_image * img, uint8_t img_count )
```

```c
#include <zephyr/display/mb_display.h>
```

在 BBC micro:bit LED 显示屏上显示一个或多个图像。

本函数接受含一张或多张图像的数组，并在 micro:bit 显示器上依次渲染。调用为异步（Asynchronous），显示处理在后台进行。若有另一张图像正在显示，则取消它，由新图像接替。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `disp` | 显示对象（Display Object）。 |
| `mode` | `MB_DISPLAY_MODE_*` 选项之一。 |
| `duration` | 每张图像的显示时长（Duration），单位为毫秒；也可为 `SYS_FOREVER_MS`。 |
| `img` | 图像位图数组（Image Bitmaps），元素为 `struct mb_image` 对象。 |
| `img_count` | `img` 数组中的图像数量。 |

<a id="ga993a6a0225206f53170d25d9177c1225"></a>

### `mb_display_print()`

```c
void mb_display_print ( struct mb_display * disp, uint32_t mode, int32_t duration, const char * fmt, ... )
```

```c
#include <zephyr/display/mb_display.h>
```

在 BBC micro:bit LED 显示屏上打印字符串。

本函数接受 `printf` 风格的格式字符串（Format String），并以滚动方式输出到显示器。

调用为异步（Asynchronous），显示处理在后台进行。若另有图像或字符串正在显示，则取消它，由新内容接替。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `disp` | 显示对象（Display Object）。 |
| `mode` | `MB_DISPLAY_MODE_*` 选项之一。 |
| `duration` | 每个字符的显示时长（Duration），单位为毫秒；也可为 `SYS_FOREVER_MS`。 |
| `fmt` | `printf` 风格的格式字符串（Format String）。 |
| `...` | 可选格式参数列表（Format Arguments）。 |

<a id="gad15b3635993007d8aad9364cbe29311b"></a>

### `mb_display_stop()`

```c
void mb_display_stop ( struct mb_display * disp)
```

```c
#include <zephyr/display/mb_display.h>
```

停止当前进行中的图像显示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `disp` | 显示对象（Display Object）。 |


## 12.6\_原页交叉引用（Cross References）

- [mb_image](../device_power_control_model_reference/P026_mb_image_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/display/mb_display.h](../api_file_management_reference/P028_zephyr__display__mb_display.h_文件参考.md)
- [SYS_FOREVER_MS](../timeutil_reference/P007_时间单位辅助接口.md#ga9f9c4c41f62c7578a30209475201efed)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5"></a>
<a id="gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a"></a>
<a id="gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69"></a>
<a id="gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_LSM6DSO API主题.md) · [返回大纲](大纲.md) · [下一章](P013_映像管理客户端（Image Management Client）.md)
