---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-1
title: 辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现辅助显示驱动（Auxiliary Display Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_auxdisplay_5Fdriver_5Fapi"></a>

```c
struct auxdisplay_driver_api
```

相关声明：[auxdisplay_driver_api](../driver_model_reference/P022_辅助显示器驱动接口.md)。

驱动操作（Driver Operations）：辅助显示器（Auxiliary Display）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_gab1af1819efa902c0cf448a8fda8dd3dc"></a>

```c
typedef int(* auxdisplay_display_on_t) (const struct device *dev)
```

相关声明：[auxdisplay_display_on_t](#gab1af1819efa902c0cf448a8fda8dd3dc)、[device](../device_reference/P002_设备对象结构.md)。

开启显示器的回调 API（Callback API）。

<a id="r_ga3afc243389b001683f4ee5466678100d"></a>

```c
typedef int(* auxdisplay_display_off_t) (const struct device *dev)
```

相关声明：[auxdisplay_display_off_t](#ga3afc243389b001683f4ee5466678100d)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示器的回调 API（Callback API）。

<a id="r_ga266a31661ae5370e11b5f2eccb9d0a55"></a>

```c
typedef int(* auxdisplay_cursor_set_enabled_t) (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_cursor_set_enabled_t](#ga266a31661ae5370e11b5f2eccb9d0a55)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置显示光标可见性（Cursor Visibility）开启或关闭的回调 API。

<a id="r_ga44a9dac2fea0b3eef65dd140e4f81105"></a>

```c
typedef int(* auxdisplay_position_blinking_set_enabled_t) (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_position_blinking_set_enabled_t](#ga44a9dac2fea0b3eef65dd140e4f81105)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置当前位置闪烁（Position Blinking）开启或关闭的回调 API。

<a id="r_ga4c76fd207dcaf659481725416ec4de66"></a>

```c
typedef int(* auxdisplay_cursor_shift_set_t) (const struct device *dev, uint8_t direction, bool display_shift)
```

相关声明：[auxdisplay_cursor_shift_set_t](#ga4c76fd207dcaf659481725416ec4de66)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置写入字符后光标移动方式（Cursor Shift）的回调 API。

<a id="r_gac3679902422c05974d1262ab3e002169"></a>

```c
typedef int(* auxdisplay_cursor_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_cursor_position_set_t](#gac3679902422c05974d1262ab3e002169)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置光标位置（Cursor Position）的回调 API。

<a id="r_ga585ea33c13736d0500766c75c7145b48"></a>

```c
typedef int(* auxdisplay_cursor_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_cursor_position_get_t](#ga585ea33c13736d0500766c75c7145b48)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取光标位置（Cursor Position）的回调 API。

<a id="r_ga15ddaa101a8399febff08e065d2b8878"></a>

```c
typedef int(* auxdisplay_display_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_display_position_set_t](#ga15ddaa101a8399febff08e065d2b8878)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置显示器当前位置（Display Position）的回调 API。

<a id="r_gab9caf3b35dd3a22f6f5bbae6568a3e8d"></a>

```c
typedef int(* auxdisplay_display_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_display_position_get_t](#gab9caf3b35dd3a22f6f5bbae6568a3e8d)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取显示器当前位置（Display Position）的回调 API。

<a id="r_gafe80906adf675409f28cf95306dc7b0a"></a>

```c
typedef int(* auxdisplay_capabilities_get_t) (const struct device *dev, struct auxdisplay_capabilities *capabilities)
```

相关声明：[auxdisplay_capabilities_get_t](#gafe80906adf675409f28cf95306dc7b0a)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)。

获取显示能力（Display Capabilities）的回调 API。

<a id="r_ga6d95cc2416de90adf2613e33106e5405"></a>

```c
typedef int(* auxdisplay_clear_t) (const struct device *dev)
```

相关声明：[auxdisplay_clear_t](#ga6d95cc2416de90adf2613e33106e5405)、[device](../device_reference/P002_设备对象结构.md)。

清空显示器内容（Clear Contents）的回调 API。

<a id="r_ga095f0b08e482727a05973f4263d30093"></a>

```c
typedef int(* auxdisplay_brightness_get_t) (const struct device *dev, uint8_t *brightness)
```

相关声明：[auxdisplay_brightness_get_t](#ga095f0b08e482727a05973f4263d30093)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前及支持的亮度设置（Brightness Settings）的回调 API。

<a id="r_ga7ad06a27ebff673599d1e92e7714bd20"></a>

```c
typedef int(* auxdisplay_brightness_set_t) (const struct device *dev, uint8_t brightness)
```

相关声明：[auxdisplay_brightness_set_t](#ga7ad06a27ebff673599d1e92e7714bd20)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器亮度（Brightness）的回调 API。

<a id="r_ga7caf2a44b902627aec02bdcb2491b4a5"></a>

```c
typedef int(* auxdisplay_backlight_get_t) (const struct device *dev, uint8_t *backlight)
```

相关声明：[auxdisplay_backlight_get_t](#ga7caf2a44b902627aec02bdcb2491b4a5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前及支持的背光设置（Backlight Settings）的回调 API。

<a id="r_gadf5064c065e5c9cd417152ee2210dafb"></a>

```c
typedef int(* auxdisplay_backlight_set_t) (const struct device *dev, uint8_t backlight)
```

相关声明：[auxdisplay_backlight_set_t](#gadf5064c065e5c9cd417152ee2210dafb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置背光级别（Backlight Level）的回调 API。

<a id="r_gaa0d87c8648d244816df62c29a6fb07e0"></a>

```c
typedef int(* auxdisplay_is_busy_t) (const struct device *dev)
```

相关声明：[auxdisplay_is_busy_t](#gaa0d87c8648d244816df62c29a6fb07e0)、[device](../device_reference/P002_设备对象结构.md)。

检查显示器是否正忙于某项操作（Busy with an Operation）的回调 API。

<a id="r_ga25df80bc845a83f0bcdd2bc9083e595a"></a>

```c
typedef int(* auxdisplay_custom_character_set_t) (const struct device *dev, struct auxdisplay_character *character)
```

相关声明：[auxdisplay_custom_character_set_t](#ga25df80bc845a83f0bcdd2bc9083e595a)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)。

在显示器上设置自定义字符（Custom Character）的回调 API。

<a id="r_ga6971aee119d3806e161c2b6c5c0158d4"></a>

```c
typedef int(* auxdisplay_write_t) (const struct device *dev, const uint8_t *data, uint16_t len)
```

相关声明：[auxdisplay_write_t](#ga6971aee119d3806e161c2b6c5c0158d4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向显示器写入文本（Text）的回调 API。

<a id="r_ga1d30d7d50f3052f31d73367034a78ac3"></a>

```c
typedef int(* auxdisplay_custom_command_t) (const struct device *dev, struct auxdisplay_custom_data *command)
```

相关声明：[auxdisplay_custom_command_t](#ga1d30d7d50f3052f31d73367034a78ac3)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)。

向显示器发送自定义命令（Custom Command）的回调 API。

<a id="r_ga59ee336b7cbbc56a8f02331caad74ba8"></a>

```c
typedef int(* auxdisplay_custom_indicator_set_t) (const struct device *dev, uint8_t index, bool enable)
```

相关声明：[auxdisplay_custom_indicator_set_t](#ga59ee336b7cbbc56a8f02331caad74ba8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭自定义指示器（Custom Indicator）的回调 API。参数说明参见 auxdisplay_custom_indicator_set()。

## 1.3\_详细说明（Detailed Documentation）

<a id="ga7caf2a44b902627aec02bdcb2491b4a5"></a>

### `auxdisplay_backlight_get_t`

```c
typedef int(* auxdisplay_backlight_get_t) (const struct device *dev, uint8_t *backlight)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取当前及支持的背光设置（Backlight Settings）的回调 API。

参数说明（Argument Description）参见 auxdisplay_backlight_get()。

<a id="gadf5064c065e5c9cd417152ee2210dafb"></a>

### `auxdisplay_backlight_set_t`

```c
typedef int(* auxdisplay_backlight_set_t) (const struct device *dev, uint8_t backlight)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置背光级别（Backlight Level）的回调 API。

参数说明（Argument Description）参见 auxdisplay_backlight_set()。

<a id="ga095f0b08e482727a05973f4263d30093"></a>

### `auxdisplay_brightness_get_t`

```c
typedef int(* auxdisplay_brightness_get_t) (const struct device *dev, uint8_t *brightness)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取当前及支持的亮度设置（Brightness Settings）的回调 API。

参数说明（Argument Description）参见 auxdisplay_brightness_get()。

<a id="ga7ad06a27ebff673599d1e92e7714bd20"></a>

### `auxdisplay_brightness_set_t`

```c
typedef int(* auxdisplay_brightness_set_t) (const struct device *dev, uint8_t brightness)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置显示器亮度（Brightness）的回调 API。

参数说明（Argument Description）参见 auxdisplay_brightness_set()。

<a id="gafe80906adf675409f28cf95306dc7b0a"></a>

### `auxdisplay_capabilities_get_t`

```c
typedef int(* auxdisplay_capabilities_get_t) (const struct device *dev, struct auxdisplay_capabilities *capabilities)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取显示能力（Display Capabilities）的回调 API。

参数说明（Argument Description）参见 auxdisplay_capabilities_get()。

<a id="ga6d95cc2416de90adf2613e33106e5405"></a>

### `auxdisplay_clear_t`

```c
typedef int(* auxdisplay_clear_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

清空显示器内容（Clear Contents）的回调 API。

参数说明（Argument Description）参见 auxdisplay_clear()。

<a id="ga585ea33c13736d0500766c75c7145b48"></a>

### `auxdisplay_cursor_position_get_t`

```c
typedef int(* auxdisplay_cursor_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取光标位置（Cursor Position）的回调 API。

参数说明（Argument Description）参见 auxdisplay_cursor_position_get()。

<a id="gac3679902422c05974d1262ab3e002169"></a>

### `auxdisplay_cursor_position_set_t`

```c
typedef int(* auxdisplay_cursor_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置光标位置（Cursor Position）的回调 API。

参数说明（Argument Description）参见 auxdisplay_cursor_position_set()。

<a id="ga266a31661ae5370e11b5f2eccb9d0a55"></a>

### `auxdisplay_cursor_set_enabled_t`

```c
typedef int(* auxdisplay_cursor_set_enabled_t) (const struct device *dev, bool enabled)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置显示光标可见性（Cursor Visibility）开启或关闭的回调 API。

参数说明（Argument Description）参见 auxdisplay_cursor_set_enabled()。

<a id="ga4c76fd207dcaf659481725416ec4de66"></a>

### `auxdisplay_cursor_shift_set_t`

```c
typedef int(* auxdisplay_cursor_shift_set_t) (const struct device *dev, uint8_t direction, bool display_shift)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置写入字符后光标移动方式（Cursor Shift）的回调 API。

参数说明（Argument Description）参见 auxdisplay_cursor_shift_set()。

<a id="ga25df80bc845a83f0bcdd2bc9083e595a"></a>

### `auxdisplay_custom_character_set_t`

```c
typedef int(* auxdisplay_custom_character_set_t) (const struct device *dev, struct auxdisplay_character *character)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

在显示器上设置自定义字符（Custom Character）的回调 API。

参数说明（Argument Description）参见 auxdisplay_custom_character_set()。

<a id="ga1d30d7d50f3052f31d73367034a78ac3"></a>

### `auxdisplay_custom_command_t`

```c
typedef int(* auxdisplay_custom_command_t) (const struct device *dev, struct auxdisplay_custom_data *command)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

向显示器发送自定义命令（Custom Command）的回调 API。

参数说明（Argument Description）参见 auxdisplay_custom_command()。

<a id="ga59ee336b7cbbc56a8f02331caad74ba8"></a>

### `auxdisplay_custom_indicator_set_t`

```c
typedef int(* auxdisplay_custom_indicator_set_t) (const struct device *dev, uint8_t index, bool enable)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

开启或关闭自定义指示器（Custom Indicator）的回调 API。参数说明参见 auxdisplay_custom_indicator_set()。

<a id="ga3afc243389b001683f4ee5466678100d"></a>

### `auxdisplay_display_off_t`

```c
typedef int(* auxdisplay_display_off_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

关闭显示器的回调 API（Callback API）。

参数说明（Argument Description）参见 auxdisplay_display_off()。

<a id="gab1af1819efa902c0cf448a8fda8dd3dc"></a>

### `auxdisplay_display_on_t`

```c
typedef int(* auxdisplay_display_on_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

开启显示器的回调 API（Callback API）。

参数说明（Argument Description）参见 auxdisplay_display_on()。

<a id="gab9caf3b35dd3a22f6f5bbae6568a3e8d"></a>

### `auxdisplay_display_position_get_t`

```c
typedef int(* auxdisplay_display_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取显示器当前位置（Display Position）的回调 API。

参数说明（Argument Description）参见 auxdisplay_display_position_get()。

<a id="ga15ddaa101a8399febff08e065d2b8878"></a>

### `auxdisplay_display_position_set_t`

```c
typedef int(* auxdisplay_display_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置显示器当前位置（Display Position）的回调 API。

参数说明（Argument Description）参见 auxdisplay_display_position_set()。

<a id="gaa0d87c8648d244816df62c29a6fb07e0"></a>

### `auxdisplay_is_busy_t`

```c
typedef int(* auxdisplay_is_busy_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

检查显示器是否正忙于某项操作（Busy with an Operation）的回调 API。

参数说明（Argument Description）参见 auxdisplay_is_busy()。

<a id="ga44a9dac2fea0b3eef65dd140e4f81105"></a>

### `auxdisplay_position_blinking_set_enabled_t`

```c
typedef int(* auxdisplay_position_blinking_set_enabled_t) (const struct device *dev, bool enabled)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置当前位置闪烁（Position Blinking）开启或关闭的回调 API。

参数说明（Argument Description）参见 auxdisplay_position_blinking_set_enabled()。

<a id="ga6971aee119d3806e161c2b6c5c0158d4"></a>

### `auxdisplay_write_t`

```c
typedef int(* auxdisplay_write_t) (const struct device *dev, const uint8_t *data, uint16_t len)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

向显示器写入文本（Text）的回调 API。

参数说明（Argument Description）参见 auxdisplay_write()。


## 1.4\_原页交叉引用（Cross References）

- [auxdisplay_driver_api](../driver_model_reference/P022_辅助显示器驱动接口.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)
- [auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)
- [auxdisplay_custom_indicator_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7930b8287b2cefa08af90a755fd5651c)
- [zephyr/drivers/auxdisplay.h](https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h.html)
- [auxdisplay_backlight_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf10ebdbe821894ccbeccb35bfa985fea)
- [auxdisplay_backlight_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga28aef24928543329c706513cc7e5b814)
- [auxdisplay_brightness_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f5be6fefc759607d2859a648a1fb3b8)
- [auxdisplay_brightness_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga34b31b70fdc57e33fc46f1048cc25e1a)
- [auxdisplay_capabilities_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga4dd5cba56d4b90b77ae8ad02122ef81c)
- [auxdisplay_clear()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaa5a643603353319946c823cc959b74b3)
- [auxdisplay_cursor_position_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga37bd5403c876ff294be5ea72292de4b4)
- [auxdisplay_cursor_position_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga9c6302789d9cc9e481dd7c54ef370988)
- [auxdisplay_cursor_set_enabled()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7191475b362f728cc92eb07cb1f2ed00)
- [auxdisplay_cursor_shift_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gafb18729b4897cea83dbfc1c7241f5b2d)
- [auxdisplay_custom_character_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf03a1068b0aed1f27ee9e2e61066da08)
- [auxdisplay_custom_command()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga87064057ae857f81431e6e9f139a6aaa)
- [auxdisplay_display_off()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga625f399720417715090793c7f6d63f7e)
- [auxdisplay_display_on()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaffb3c1c41d810355fe2da3558ebba0c2)
- [auxdisplay_display_position_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f9e363765d715edb899901a14c54674)
- [auxdisplay_display_position_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga02e8e930203cfb1410752a0ffee9a34e)
- [auxdisplay_is_busy()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga2af115a23f370e0770b3c998ecf0b96b)
- [auxdisplay_position_blinking_set_enabled()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7102ec9941f8b3131a18e4ff7b640241)
- [auxdisplay_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga231dd862cda34ea4c0c8870675556f8d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙网状网络（Bluetooth Mesh）.md)
