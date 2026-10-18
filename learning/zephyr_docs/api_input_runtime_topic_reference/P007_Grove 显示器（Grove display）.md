---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-7
title: Grove 显示器（Grove display）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Grove 显示器（Grove display）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Grove LCD RGB 显示器接口。

<a id="details"></a>

Grove LCD RGB 显示器接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga4fe4ad1bc603fa658247ea2f7dbf7f31"></a>

```c
#define GLCD_DS_DISPLAY_ON (1 << 2)
```

相关声明：[GLCD_DS_DISPLAY_ON](#ga4fe4ad1bc603fa658247ea2f7dbf7f31)。

<a id="r_ga66bc1e76fcda544f619d02ecbdcb368f"></a>

```c
#define GLCD_DS_DISPLAY_OFF (0 << 2)
```

相关声明：[GLCD_DS_DISPLAY_OFF](#ga66bc1e76fcda544f619d02ecbdcb368f)。

<a id="r_gaa40ba9872b397a1daa26f68f17d7e28d"></a>

```c
#define GLCD_DS_CURSOR_ON (1 << 1)
```

相关声明：[GLCD_DS_CURSOR_ON](#gaa40ba9872b397a1daa26f68f17d7e28d)。

<a id="r_gaac73ba0ea95d570493485212ce704691"></a>

```c
#define GLCD_DS_CURSOR_OFF (0 << 1)
```

相关声明：[GLCD_DS_CURSOR_OFF](#gaac73ba0ea95d570493485212ce704691)。

<a id="r_ga62f05f0aa279c530bb96153efd2a36da"></a>

```c
#define GLCD_DS_BLINK_ON (1 << 0)
```

相关声明：[GLCD_DS_BLINK_ON](#ga62f05f0aa279c530bb96153efd2a36da)。

<a id="r_gaca5ebc6bff0db636ff8767f7c225143f"></a>

```c
#define GLCD_DS_BLINK_OFF (0 << 0)
```

相关声明：[GLCD_DS_BLINK_OFF](#gaca5ebc6bff0db636ff8767f7c225143f)。

<a id="r_ga460a887aaa11dbe4461226a55bcae951"></a>

```c
#define GLCD_IS_SHIFT_INCREMENT (1 << 1)
```

相关声明：[GLCD_IS_SHIFT_INCREMENT](#ga460a887aaa11dbe4461226a55bcae951)。

<a id="r_ga2258570aac3ed680739324a2daf5f626"></a>

```c
#define GLCD_IS_SHIFT_DECREMENT (0 << 1)
```

相关声明：[GLCD_IS_SHIFT_DECREMENT](#ga2258570aac3ed680739324a2daf5f626)。

<a id="r_ga5e136501ffbde18b34163bc1a7948c9a"></a>

```c
#define GLCD_IS_ENTRY_LEFT (1 << 0)
```

相关声明：[GLCD_IS_ENTRY_LEFT](#ga5e136501ffbde18b34163bc1a7948c9a)。

<a id="r_ga6c9cee5b9f86efcc2073f60dc204fc2a"></a>

```c
#define GLCD_IS_ENTRY_RIGHT (0 << 0)
```

相关声明：[GLCD_IS_ENTRY_RIGHT](#ga6c9cee5b9f86efcc2073f60dc204fc2a)。

<a id="r_ga726ae92e51500c82a202164edb706cd4"></a>

```c
#define GLCD_FS_8BIT_MODE (1 << 4)
```

相关声明：[GLCD_FS_8BIT_MODE](#ga726ae92e51500c82a202164edb706cd4)。

<a id="r_ga7007ac8d919421d34e4dff4e97503cb6"></a>

```c
#define GLCD_FS_ROWS_2 (1 << 3)
```

相关声明：[GLCD_FS_ROWS_2](#ga7007ac8d919421d34e4dff4e97503cb6)。

<a id="r_ga2ebedc80c40c35ea57ebcb3968bc1052"></a>

```c
#define GLCD_FS_ROWS_1 (0 << 3)
```

相关声明：[GLCD_FS_ROWS_1](#ga2ebedc80c40c35ea57ebcb3968bc1052)。

<a id="r_gabcfa7abdd0834ee469a6693a0aa7f883"></a>

```c
#define GLCD_FS_DOT_SIZE_BIG (1 << 2)
```

相关声明：[GLCD_FS_DOT_SIZE_BIG](#gabcfa7abdd0834ee469a6693a0aa7f883)。

<a id="r_gae47fb073bb30f1fab7171a6bad55fc22"></a>

```c
#define GLCD_FS_DOT_SIZE_LITTLE (0 << 2)
```

相关声明：[GLCD_FS_DOT_SIZE_LITTLE](#gae47fb073bb30f1fab7171a6bad55fc22)。

<a id="r_gaca2204b331e88203b05d0382d80cc5de"></a>

```c
#define GROVE_RGB_WHITE 0
```

相关声明：[GROVE_RGB_WHITE](#gaca2204b331e88203b05d0382d80cc5de)。

<a id="r_gad391aa4262d4fd7e93052e7dafc5daa4"></a>

```c
#define GROVE_RGB_RED 1
```

相关声明：[GROVE_RGB_RED](#gad391aa4262d4fd7e93052e7dafc5daa4)。

<a id="r_ga6e9faff3c1a708d6c5d509a85e1dd1f4"></a>

```c
#define GROVE_RGB_GREEN 2
```

相关声明：[GROVE_RGB_GREEN](#ga6e9faff3c1a708d6c5d509a85e1dd1f4)。

<a id="r_gaf754fe5b8b20bca5ae9768833e045ef8"></a>

```c
#define GROVE_RGB_BLUE 3
```

相关声明：[GROVE_RGB_BLUE](#gaf754fe5b8b20bca5ae9768833e045ef8)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.2\_函数（Functions）

<a id="r_gaecd7b73186d110fa4bd2c47bbb7d63a2"></a>

```c
void glcd_print (const struct device *dev, char *data, uint32_t size)
```

相关声明：[glcd_print](#gaecd7b73186d110fa4bd2c47bbb7d63a2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向屏幕（Screen）发送文本。

<a id="r_ga8272c8c1ff41835306908a0f6932feae"></a>

```c
void glcd_cursor_pos_set (const struct device *dev, uint8_t col, uint8_t row)
```

相关声明：[glcd_cursor_pos_set](#ga8272c8c1ff41835306908a0f6932feae)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置后续添加文本使用的光标位置（Text Cursor Position）。

<a id="r_ga10929139f1632247968ccdd4fdd79dcd"></a>

```c
void glcd_clear (const struct device *dev)
```

相关声明：[glcd_clear](#ga10929139f1632247968ccdd4fdd79dcd)、[device](../device_reference/P002_设备对象结构.md)。

清除当前显示内容（Display）。

<a id="r_ga103c6edb0b5ed37f34c12694338acc70"></a>

```c
void glcd_display_state_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_display_state_set](#ga103c6edb0b5ed37f34c12694338acc70)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

改变显示状态（Display State）的函数。

<a id="r_gac3139bf68d1acbb27905a2346da13b17"></a>

```c
uint8_t glcd_display_state_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_display_state_get](#gac3139bf68d1acbb27905a2346da13b17)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的显示功能集（Display Feature Set）。

<a id="r_gae73554047414529e5e7957a5d394e4a2"></a>

```c
void glcd_input_state_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_input_state_set](#gae73554047414529e5e7957a5d394e4a2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

改变输入状态（Input State）的函数。

<a id="r_ga3c590c83b2f1c8ea0fe301daa7a40198"></a>

```c
uint8_t glcd_input_state_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_input_state_get](#ga3c590c83b2f1c8ea0fe301daa7a40198)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的输入设置（Input Set）。

<a id="r_ga5e9fb362faf9c040eaa16addbfad2b6d"></a>

```c
void glcd_function_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_function_set](#ga5e9fb362faf9c040eaa16addbfad2b6d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器功能状态（Functional State）的函数。

<a id="r_gad660824e481428b811c914d6bf4634f5"></a>

```c
uint8_t glcd_function_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_function_get](#gad660824e481428b811c914d6bf4634f5)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的功能设置（Function Set）。

<a id="r_gabd119208e05f9f878b7f24a62da08db2"></a>

```c
void glcd_color_select (const struct device *dev, uint8_t color)
```

相关声明：[glcd_color_select](#gabd119208e05f9f878b7f24a62da08db2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 LCD 背景（Background）设为预定义颜色（Predefined Color）。

<a id="r_gaf99aa37f71396baaf523348a3ea9cbbe"></a>

```c
void glcd_color_set (const struct device *dev, uint8_t r, uint8_t g, uint8_t b)
```

相关声明：[glcd_color_set](#gaf99aa37f71396baaf523348a3ea9cbbe)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 LCD 背景（Background）设为自定义 RGB 颜色值（Color Value）。

## 7.3\_详细说明（Detailed Documentation）

<a id="gaca5ebc6bff0db636ff8767f7c225143f"></a>

### `GLCD_DS_BLINK_OFF`

```c
#define GLCD_DS_BLINK_OFF (0 << 0)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga62f05f0aa279c530bb96153efd2a36da"></a>

### `GLCD_DS_BLINK_ON`

```c
#define GLCD_DS_BLINK_ON (1 << 0)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gaac73ba0ea95d570493485212ce704691"></a>

### `GLCD_DS_CURSOR_OFF`

```c
#define GLCD_DS_CURSOR_OFF (0 << 1)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gaa40ba9872b397a1daa26f68f17d7e28d"></a>

### `GLCD_DS_CURSOR_ON`

```c
#define GLCD_DS_CURSOR_ON (1 << 1)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga66bc1e76fcda544f619d02ecbdcb368f"></a>

### `GLCD_DS_DISPLAY_OFF`

```c
#define GLCD_DS_DISPLAY_OFF (0 << 2)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga4fe4ad1bc603fa658247ea2f7dbf7f31"></a>

### `GLCD_DS_DISPLAY_ON`

```c
#define GLCD_DS_DISPLAY_ON (1 << 2)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga726ae92e51500c82a202164edb706cd4"></a>

### `GLCD_FS_8BIT_MODE`

```c
#define GLCD_FS_8BIT_MODE (1 << 4)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gabcfa7abdd0834ee469a6693a0aa7f883"></a>

### `GLCD_FS_DOT_SIZE_BIG`

```c
#define GLCD_FS_DOT_SIZE_BIG (1 << 2)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gae47fb073bb30f1fab7171a6bad55fc22"></a>

### `GLCD_FS_DOT_SIZE_LITTLE`

```c
#define GLCD_FS_DOT_SIZE_LITTLE (0 << 2)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga2ebedc80c40c35ea57ebcb3968bc1052"></a>

### `GLCD_FS_ROWS_1`

```c
#define GLCD_FS_ROWS_1 (0 << 3)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga7007ac8d919421d34e4dff4e97503cb6"></a>

### `GLCD_FS_ROWS_2`

```c
#define GLCD_FS_ROWS_2 (1 << 3)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga5e136501ffbde18b34163bc1a7948c9a"></a>

### `GLCD_IS_ENTRY_LEFT`

```c
#define GLCD_IS_ENTRY_LEFT (1 << 0)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga6c9cee5b9f86efcc2073f60dc204fc2a"></a>

### `GLCD_IS_ENTRY_RIGHT`

```c
#define GLCD_IS_ENTRY_RIGHT (0 << 0)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga2258570aac3ed680739324a2daf5f626"></a>

### `GLCD_IS_SHIFT_DECREMENT`

```c
#define GLCD_IS_SHIFT_DECREMENT (0 << 1)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga460a887aaa11dbe4461226a55bcae951"></a>

### `GLCD_IS_SHIFT_INCREMENT`

```c
#define GLCD_IS_SHIFT_INCREMENT (1 << 1)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gaf754fe5b8b20bca5ae9768833e045ef8"></a>

### `GROVE_RGB_BLUE`

```c
#define GROVE_RGB_BLUE 3
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga6e9faff3c1a708d6c5d509a85e1dd1f4"></a>

### `GROVE_RGB_GREEN`

```c
#define GROVE_RGB_GREEN 2
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gad391aa4262d4fd7e93052e7dafc5daa4"></a>

### `GROVE_RGB_RED`

```c
#define GROVE_RGB_RED 1
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="gaca2204b331e88203b05d0382d80cc5de"></a>

### `GROVE_RGB_WHITE`

```c
#define GROVE_RGB_WHITE 0
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

<a id="ga10929139f1632247968ccdd4fdd79dcd"></a>

### `glcd_clear()`

```c
void glcd_clear ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

清除当前显示内容（Display）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |

<a id="gabd119208e05f9f878b7f24a62da08db2"></a>

### `glcd_color_select()`

```c
void glcd_color_select ( const struct device * dev, uint8_t color )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

将 LCD 背景（Background）设为预定义颜色（Predefined Color）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `color` | 预定义颜色选项（Predefined Color Options）之一。 |

<a id="gaf99aa37f71396baaf523348a3ea9cbbe"></a>

### `glcd_color_set()`

```c
void glcd_color_set ( const struct device * dev, uint8_t r, uint8_t g, uint8_t b )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

将 LCD 背景（Background）设为自定义 RGB 颜色值（Color Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `r` | 红色分量值（Red Color Value），最大为 `255`。 |
| `g` | 绿色分量值（Green Color Value），最大为 `255`。 |
| `b` | 蓝色分量值（Blue Color Value），最大为 `255`。 |

<a id="ga8272c8c1ff41835306908a0f6932feae"></a>

### `glcd_cursor_pos_set()`

```c
void glcd_cursor_pos_set ( const struct device * dev, uint8_t col, uint8_t row )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

设置后续添加文本使用的光标位置（Text Cursor Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `col` | 光标目标列（Cursor Column），范围 `0–15`。 |
| `row` | 光标目标行（Cursor Row），为 `0` 或 `1`。 |

<a id="gac3139bf68d1acbb27905a2346da13b17"></a>

### `glcd_display_state_get()`

```c
uint8_t glcd_display_state_get ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

返回设备关联的显示功能集（Display Feature Set）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要获取显示功能设置（Display Features Set）的 Grove LCD。 |

**返回（Returns）**：**返回值（Returns）：**设备关联的显示功能设置（Display Feature Set）。

<a id="ga103c6edb0b5ed37f34c12694338acc70"></a>

### `glcd_display_state_set()`

```c
void glcd_display_state_set ( const struct device * dev, uint8_t opt )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

改变显示状态（Display State）的函数。

本函数允许按需更改显示状态（Display State），例如开启／关闭屏幕、显示／隐藏光标，以及使光标闪烁。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `opt` | `GLCD_DS_*` 选项的 8 位掩码（Bitmask）。 |

<a id="gad660824e481428b811c914d6bf4634f5"></a>

### `glcd_function_get()`

```c
uint8_t glcd_function_get ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

返回设备关联的功能设置（Function Set）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要获取功能设置（Functions Set）的 Grove LCD。 |

**返回（Returns）**：**返回值（Returns）：**设备关联的功能特性设置（Function Features Set）。

<a id="ga5e9fb362faf9c040eaa16addbfad2b6d"></a>

### `glcd_function_set()`

```c
void glcd_function_set ( const struct device * dev, uint8_t opt )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

设置显示器功能状态（Functional State）的函数。

本函数允许按需更改显示状态（Display State），例如行数、点阵大小（Dot Size）和文本显示质量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `opt` | `GLCD_FS_*` 选项的位掩码（Bitmask）。 |

<a id="ga3c590c83b2f1c8ea0fe301daa7a40198"></a>

### `glcd_input_state_get()`

```c
uint8_t glcd_input_state_get ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

返回设备关联的输入设置（Input Set）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要获取输入特性设置（Input Features Set）的 Grove LCD。 |

**返回（Returns）**：**返回值（Returns）：**设备关联的输入设置（Input Set）。

<a id="gae73554047414529e5e7957a5d394e4a2"></a>

### `glcd_input_state_set()`

```c
void glcd_input_state_set ( const struct device * dev, uint8_t opt )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

改变输入状态（Input State）的函数。

本函数允许更改文本输入状态（Text Input State），例如从左侧或右侧输入文本，以及新文本输入时的递增距离。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `opt` | `GLCD_IS_*` 选项的位掩码（Bitmask）。 |

<a id="gaecd7b73186d110fa4bd2c47bbb7d63a2"></a>

### `glcd_print()`

```c
void glcd_print ( const struct device * dev, char * data, uint32_t size )
```

```c
#include <zephyr/drivers/misc/grove_lcd/grove_lcd.h>
```

向屏幕（Screen）发送文本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体（Device Structure）的指针。 |
| `data` | 要显示的 ASCII 文本（Text）。 |
| `size` | 文本长度（Text Length），单位为字节。 |


## 7.4\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/drivers/misc/grove_lcd/grove_lcd.h](../api_file_system_power_reference/P014_zephyr__drivers__misc__grove_lcd__grove_lcd.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_磁盘访问接口（Disk Access Interface）.md) · [返回大纲](大纲.md) · [下一章](P008_ICM45686 API主题.md)
