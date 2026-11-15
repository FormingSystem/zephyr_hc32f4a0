---
id: learning.zephyr-docs.api-file-flash-test-reference.page-1
title: zephyr__drivers__auxdisplay.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_auxdisplay.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

辅助显示器（Auxiliary Display，文本式/非图形式）驱动API的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/auxdisplay.h>
```

查看此文件的源码。

辅助显示器（Auxiliary Display，文本式/非图形式）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_auxdisplay_5Flight"></a>

```c
struct auxdisplay_light
```

相关声明：[auxdisplay_light](../driver_model_reference/P023_辅助显示器亮度.md)。

亮度和／或背光的光照等级（Light Levels）。

<a id="r_auxdisplay_5Fcapabilities"></a>

```c
struct auxdisplay_capabilities
```

相关声明：[auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)。

保存显示器能力（Display Capabilities）的结构体。

<a id="r_auxdisplay_5Fcustom_5Fdata"></a>

```c
struct auxdisplay_custom_data
```

相关声明：[auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)。

自定义命令（Custom Command）结构体。

<a id="r_auxdisplay_5Fcharacter"></a>

```c
struct auxdisplay_character
```

相关声明：[auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)。

自定义字符（Custom Character）结构体。

<a id="r_auxdisplay_5Fdriver_5Fapi"></a>

```c
struct auxdisplay_driver_api
```

相关声明：[auxdisplay_driver_api](../driver_model_reference/P022_辅助显示器驱动接口.md)。

驱动操作（Driver Operations）：辅助显示器（Auxiliary Display）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga0bd1d97b360f3138887a5e3e4729e01b"></a>

```c
#define AUXDISPLAY_LIGHT_NOT_SUPPORTED 0
```

相关声明：[AUXDISPLAY_LIGHT_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga0bd1d97b360f3138887a5e3e4729e01b)。

不支持亮度／背光（Brightness/Backlight）时，用作其最小值和最大值。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga78861a5414ac95e9ca77436c0b82acc2"></a>

```c
typedef uint32_t auxdisplay_mode_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[auxdisplay_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga78861a5414ac95e9ca77436c0b82acc2)。

用于描述辅助文本显示器（Auxiliary Text Display）的模式。

<a id="r_gab1af1819efa902c0cf448a8fda8dd3dc"></a>

```c
typedef int(* auxdisplay_display_on_t) (const struct device *dev)
```

相关声明：[auxdisplay_display_on_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gab1af1819efa902c0cf448a8fda8dd3dc)、[device](../device_reference/P002_设备对象结构.md)。

开启显示器的回调 API（Callback API）。

<a id="r_ga3afc243389b001683f4ee5466678100d"></a>

```c
typedef int(* auxdisplay_display_off_t) (const struct device *dev)
```

相关声明：[auxdisplay_display_off_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga3afc243389b001683f4ee5466678100d)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示器的回调 API（Callback API）。

<a id="r_ga266a31661ae5370e11b5f2eccb9d0a55"></a>

```c
typedef int(* auxdisplay_cursor_set_enabled_t) (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_cursor_set_enabled_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga266a31661ae5370e11b5f2eccb9d0a55)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置显示光标可见性（Cursor Visibility）开启或关闭的回调 API。

<a id="r_ga44a9dac2fea0b3eef65dd140e4f81105"></a>

```c
typedef int(* auxdisplay_position_blinking_set_enabled_t) (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_position_blinking_set_enabled_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga44a9dac2fea0b3eef65dd140e4f81105)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置当前位置闪烁（Position Blinking）开启或关闭的回调 API。

<a id="r_ga4c76fd207dcaf659481725416ec4de66"></a>

```c
typedef int(* auxdisplay_cursor_shift_set_t) (const struct device *dev, uint8_t direction, bool display_shift)
```

相关声明：[auxdisplay_cursor_shift_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga4c76fd207dcaf659481725416ec4de66)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置写入字符后光标移动方式（Cursor Shift）的回调 API。

<a id="r_gac3679902422c05974d1262ab3e002169"></a>

```c
typedef int(* auxdisplay_cursor_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_cursor_position_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gac3679902422c05974d1262ab3e002169)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置光标位置（Cursor Position）的回调 API。

<a id="r_ga585ea33c13736d0500766c75c7145b48"></a>

```c
typedef int(* auxdisplay_cursor_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_cursor_position_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga585ea33c13736d0500766c75c7145b48)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取光标位置（Cursor Position）的回调 API。

<a id="r_ga15ddaa101a8399febff08e065d2b8878"></a>

```c
typedef int(* auxdisplay_display_position_set_t) (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_display_position_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga15ddaa101a8399febff08e065d2b8878)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置显示器当前位置（Display Position）的回调 API。

<a id="r_gab9caf3b35dd3a22f6f5bbae6568a3e8d"></a>

```c
typedef int(* auxdisplay_display_position_get_t) (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_display_position_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gab9caf3b35dd3a22f6f5bbae6568a3e8d)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取显示器当前位置（Display Position）的回调 API。

<a id="r_gafe80906adf675409f28cf95306dc7b0a"></a>

```c
typedef int(* auxdisplay_capabilities_get_t) (const struct device *dev, struct auxdisplay_capabilities *capabilities)
```

相关声明：[auxdisplay_capabilities_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gafe80906adf675409f28cf95306dc7b0a)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)。

获取显示能力（Display Capabilities）的回调 API。

<a id="r_ga6d95cc2416de90adf2613e33106e5405"></a>

```c
typedef int(* auxdisplay_clear_t) (const struct device *dev)
```

相关声明：[auxdisplay_clear_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga6d95cc2416de90adf2613e33106e5405)、[device](../device_reference/P002_设备对象结构.md)。

清空显示器内容（Clear Contents）的回调 API。

<a id="r_ga095f0b08e482727a05973f4263d30093"></a>

```c
typedef int(* auxdisplay_brightness_get_t) (const struct device *dev, uint8_t *brightness)
```

相关声明：[auxdisplay_brightness_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga095f0b08e482727a05973f4263d30093)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前及支持的亮度设置（Brightness Settings）的回调 API。

<a id="r_ga7ad06a27ebff673599d1e92e7714bd20"></a>

```c
typedef int(* auxdisplay_brightness_set_t) (const struct device *dev, uint8_t brightness)
```

相关声明：[auxdisplay_brightness_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga7ad06a27ebff673599d1e92e7714bd20)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器亮度（Brightness）的回调 API。

<a id="r_ga7caf2a44b902627aec02bdcb2491b4a5"></a>

```c
typedef int(* auxdisplay_backlight_get_t) (const struct device *dev, uint8_t *backlight)
```

相关声明：[auxdisplay_backlight_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga7caf2a44b902627aec02bdcb2491b4a5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前及支持的背光设置（Backlight Settings）的回调 API。

<a id="r_gadf5064c065e5c9cd417152ee2210dafb"></a>

```c
typedef int(* auxdisplay_backlight_set_t) (const struct device *dev, uint8_t backlight)
```

相关声明：[auxdisplay_backlight_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gadf5064c065e5c9cd417152ee2210dafb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置背光级别（Backlight Level）的回调 API。

<a id="r_gaa0d87c8648d244816df62c29a6fb07e0"></a>

```c
typedef int(* auxdisplay_is_busy_t) (const struct device *dev)
```

相关声明：[auxdisplay_is_busy_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gaa0d87c8648d244816df62c29a6fb07e0)、[device](../device_reference/P002_设备对象结构.md)。

检查显示器是否正忙于某项操作（Busy with an Operation）的回调 API。

<a id="r_ga25df80bc845a83f0bcdd2bc9083e595a"></a>

```c
typedef int(* auxdisplay_custom_character_set_t) (const struct device *dev, struct auxdisplay_character *character)
```

相关声明：[auxdisplay_custom_character_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga25df80bc845a83f0bcdd2bc9083e595a)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)。

在显示器上设置自定义字符（Custom Character）的回调 API。

<a id="r_ga6971aee119d3806e161c2b6c5c0158d4"></a>

```c
typedef int(* auxdisplay_write_t) (const struct device *dev, const uint8_t *data, uint16_t len)
```

相关声明：[auxdisplay_write_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga6971aee119d3806e161c2b6c5c0158d4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向显示器写入文本（Text）的回调 API。

<a id="r_ga1d30d7d50f3052f31d73367034a78ac3"></a>

```c
typedef int(* auxdisplay_custom_command_t) (const struct device *dev, struct auxdisplay_custom_data *command)
```

相关声明：[auxdisplay_custom_command_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga1d30d7d50f3052f31d73367034a78ac3)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)。

向显示器发送自定义命令（Custom Command）的回调 API。

<a id="r_ga59ee336b7cbbc56a8f02331caad74ba8"></a>

```c
typedef int(* auxdisplay_custom_indicator_set_t) (const struct device *dev, uint8_t index, bool enable)
```

相关声明：[auxdisplay_custom_indicator_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga59ee336b7cbbc56a8f02331caad74ba8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭自定义指示器（Custom Indicator）的回调 API。参数说明参见 auxdisplay_custom_indicator_set()。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga98b0be37fc76df0ae4dec0bef6c94504"></a>

```c
enum auxdisplay_position { AUXDISPLAY_POSITION_ABSOLUTE = 0 , AUXDISPLAY_POSITION_RELATIVE , AUXDISPLAY_POSITION_RELATIVE_DIRECTION , AUXDISPLAY_POSITION_COUNT }
```

相关声明：[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[AUXDISPLAY_POSITION_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)、[AUXDISPLAY_POSITION_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)、[AUXDISPLAY_POSITION_RELATIVE_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)、[AUXDISPLAY_POSITION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)。

用于移动光标或显示位置（Cursor or Display Position）。

<a id="r_ga5f95ac69e18091883e7121103014be10"></a>

```c
enum auxdisplay_direction { AUXDISPLAY_DIRECTION_RIGHT = 0 , AUXDISPLAY_DIRECTION_LEFT , AUXDISPLAY_DIRECTION_COUNT }
```

相关声明：[auxdisplay_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga5f95ac69e18091883e7121103014be10)、[AUXDISPLAY_DIRECTION_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)、[AUXDISPLAY_DIRECTION_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352)、[AUXDISPLAY_DIRECTION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)。

用于设置字符追加位置（Character Append Position）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gaffb3c1c41d810355fe2da3558ebba0c2"></a>

```c
int auxdisplay_display_on (const struct device *dev)
```

相关声明：[auxdisplay_display_on](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaffb3c1c41d810355fe2da3558ebba0c2)、[device](../device_reference/P002_设备对象结构.md)。

开启显示器（Display）。

<a id="r_ga625f399720417715090793c7f6d63f7e"></a>

```c
int auxdisplay_display_off (const struct device *dev)
```

相关声明：[auxdisplay_display_off](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga625f399720417715090793c7f6d63f7e)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示器（Display）。

<a id="r_ga7191475b362f728cc92eb07cb1f2ed00"></a>

```c
int auxdisplay_cursor_set_enabled (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_cursor_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7191475b362f728cc92eb07cb1f2ed00)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置辅助显示器（Auxiliary Display）的光标启用状态（Cursor Enabled Status）。

<a id="r_ga7102ec9941f8b3131a18e4ff7b640241"></a>

```c
int auxdisplay_position_blinking_set_enabled (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_position_blinking_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7102ec9941f8b3131a18e4ff7b640241)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置辅助显示器（Auxiliary Display）的光标闪烁状态（Cursor Blinking Status）。

<a id="r_gafb18729b4897cea83dbfc1c7241f5b2d"></a>

```c
int auxdisplay_cursor_shift_set (const struct device *dev, uint8_t direction, bool display_shift)
```

相关声明：[auxdisplay_cursor_shift_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gafb18729b4897cea83dbfc1c7241f5b2d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置写入字符后的光标移动（Cursor Shift）及显示移动（Display Shift）。

<a id="r_ga9c6302789d9cc9e481dd7c54ef370988"></a>

```c
int auxdisplay_cursor_position_set (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_cursor_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga9c6302789d9cc9e481dd7c54ef370988)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置辅助显示器的光标及写入位置（Cursor and Write Position）。

<a id="r_ga37bd5403c876ff294be5ea72292de4b4"></a>

```c
int auxdisplay_cursor_position_get (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_cursor_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga37bd5403c876ff294be5ea72292de4b4)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取辅助显示器的当前光标（Current Cursor）。

<a id="r_ga02e8e930203cfb1410752a0ffee9a34e"></a>

```c
int auxdisplay_display_position_set (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_display_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga02e8e930203cfb1410752a0ffee9a34e)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置辅助显示器的显示位置（Display Position）。

<a id="r_ga1f9e363765d715edb899901a14c54674"></a>

```c
int auxdisplay_display_position_get (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_display_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f9e363765d715edb899901a14c54674)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取辅助显示器的当前显示位置（Display Position）。

<a id="r_ga4dd5cba56d4b90b77ae8ad02122ef81c"></a>

```c
int auxdisplay_capabilities_get (const struct device *dev, struct auxdisplay_capabilities *capabilities)
```

相关声明：[auxdisplay_capabilities_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga4dd5cba56d4b90b77ae8ad02122ef81c)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)。

获取辅助显示器的能力及详细信息（Capabilities and Details）。

<a id="r_gaa5a643603353319946c823cc959b74b3"></a>

```c
int auxdisplay_clear (const struct device *dev)
```

相关声明：[auxdisplay_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaa5a643603353319946c823cc959b74b3)、[device](../device_reference/P002_设备对象结构.md)。

清空辅助显示器并返回起始位置（Home Position）。

<a id="r_ga1f5be6fefc759607d2859a648a1fb3b8"></a>

```c
int auxdisplay_brightness_get (const struct device *dev, uint8_t *brightness)
```

相关声明：[auxdisplay_brightness_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f5be6fefc759607d2859a648a1fb3b8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取辅助显示器的当前亮度级别（Brightness Level）。

<a id="r_ga34b31b70fdc57e33fc46f1048cc25e1a"></a>

```c
int auxdisplay_brightness_set (const struct device *dev, uint8_t brightness)
```

相关声明：[auxdisplay_brightness_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga34b31b70fdc57e33fc46f1048cc25e1a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新辅助显示器的亮度级别（Brightness Level）。

<a id="r_gaf10ebdbe821894ccbeccb35bfa985fea"></a>

```c
int auxdisplay_backlight_get (const struct device *dev, uint8_t *backlight)
```

相关声明：[auxdisplay_backlight_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf10ebdbe821894ccbeccb35bfa985fea)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取辅助显示器的背光级别详情（Backlight Level Details）。

<a id="r_ga28aef24928543329c706513cc7e5b814"></a>

```c
int auxdisplay_backlight_set (const struct device *dev, uint8_t backlight)
```

相关声明：[auxdisplay_backlight_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga28aef24928543329c706513cc7e5b814)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新辅助显示器的背光级别（Backlight Level）。

<a id="r_ga2af115a23f370e0770b3c998ecf0b96b"></a>

```c
int auxdisplay_is_busy (const struct device *dev)
```

相关声明：[auxdisplay_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga2af115a23f370e0770b3c998ecf0b96b)、[device](../device_reference/P002_设备对象结构.md)。

检查辅助显示驱动（Auxiliary Display Driver）是否忙碌。

<a id="r_gaf03a1068b0aed1f27ee9e2e61066da08"></a>

```c
int auxdisplay_custom_character_set (const struct device *dev, struct auxdisplay_character *character)
```

相关声明：[auxdisplay_custom_character_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf03a1068b0aed1f27ee9e2e61066da08)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)。

在显示器中设置自定义字符（Custom Character）。

<a id="r_ga231dd862cda34ea4c0c8870675556f8d"></a>

```c
int auxdisplay_write (const struct device *dev, const uint8_t *data, uint16_t len)
```

相关声明：[auxdisplay_write](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga231dd862cda34ea4c0c8870675556f8d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在当前位置向辅助显示器屏幕写入数据。

<a id="r_ga87064057ae857f81431e6e9f139a6aaa"></a>

```c
int auxdisplay_custom_command (const struct device *dev, struct auxdisplay_custom_data *data)
```

相关声明：[auxdisplay_custom_command](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga87064057ae857f81431e6e9f139a6aaa)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)。

向显示器发送自定义命令（Custom Command），需要驱动支持。

<a id="r_ga7930b8287b2cefa08af90a755fd5651c"></a>

```c
int auxdisplay_custom_indicator_set (const struct device *dev, uint8_t index, bool enable)
```

相关声明：[auxdisplay_custom_indicator_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7930b8287b2cefa08af90a755fd5651c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭显示器上的自定义指示器（Custom Indicator）。


## 1.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P047_auxdisplay.h_源码浏览.md)
- [auxdisplay_light](../driver_model_reference/P023_辅助显示器亮度.md)
- [auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)
- [auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)
- [auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)
- [auxdisplay_driver_api](../driver_model_reference/P022_辅助显示器驱动接口.md)
- [AUXDISPLAY_LIGHT_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga0bd1d97b360f3138887a5e3e4729e01b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [auxdisplay_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga78861a5414ac95e9ca77436c0b82acc2)
- [auxdisplay_display_on_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gab1af1819efa902c0cf448a8fda8dd3dc)
- [device](../device_reference/P002_设备对象结构.md)
- [auxdisplay_display_off_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga3afc243389b001683f4ee5466678100d)
- [auxdisplay_cursor_set_enabled_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga266a31661ae5370e11b5f2eccb9d0a55)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [auxdisplay_position_blinking_set_enabled_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga44a9dac2fea0b3eef65dd140e4f81105)
- [auxdisplay_cursor_shift_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga4c76fd207dcaf659481725416ec4de66)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [auxdisplay_cursor_position_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gac3679902422c05974d1262ab3e002169)
- [auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [auxdisplay_cursor_position_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga585ea33c13736d0500766c75c7145b48)
- [auxdisplay_display_position_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga15ddaa101a8399febff08e065d2b8878)
- [auxdisplay_display_position_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gab9caf3b35dd3a22f6f5bbae6568a3e8d)
- [auxdisplay_capabilities_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gafe80906adf675409f28cf95306dc7b0a)
- [auxdisplay_clear_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga6d95cc2416de90adf2613e33106e5405)
- [auxdisplay_brightness_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga095f0b08e482727a05973f4263d30093)
- [auxdisplay_brightness_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga7ad06a27ebff673599d1e92e7714bd20)
- [auxdisplay_backlight_get_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga7caf2a44b902627aec02bdcb2491b4a5)
- [auxdisplay_backlight_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gadf5064c065e5c9cd417152ee2210dafb)
- [auxdisplay_is_busy_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#gaa0d87c8648d244816df62c29a6fb07e0)
- [auxdisplay_custom_character_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga25df80bc845a83f0bcdd2bc9083e595a)
- [auxdisplay_write_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga6971aee119d3806e161c2b6c5c0158d4)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [auxdisplay_custom_command_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga1d30d7d50f3052f31d73367034a78ac3)
- [auxdisplay_custom_indicator_set_t](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md#ga59ee336b7cbbc56a8f02331caad74ba8)
- [auxdisplay_custom_indicator_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7930b8287b2cefa08af90a755fd5651c)
- [AUXDISPLAY_POSITION_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)
- [AUXDISPLAY_POSITION_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)
- [AUXDISPLAY_POSITION_RELATIVE_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)
- [AUXDISPLAY_POSITION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)
- [auxdisplay_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga5f95ac69e18091883e7121103014be10)
- [AUXDISPLAY_DIRECTION_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)
- [AUXDISPLAY_DIRECTION_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352)
- [AUXDISPLAY_DIRECTION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)
- [auxdisplay_display_on](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaffb3c1c41d810355fe2da3558ebba0c2)
- [auxdisplay_display_off](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga625f399720417715090793c7f6d63f7e)
- [auxdisplay_cursor_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7191475b362f728cc92eb07cb1f2ed00)
- [auxdisplay_position_blinking_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7102ec9941f8b3131a18e4ff7b640241)
- [auxdisplay_cursor_shift_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gafb18729b4897cea83dbfc1c7241f5b2d)
- [auxdisplay_cursor_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga9c6302789d9cc9e481dd7c54ef370988)
- [auxdisplay_cursor_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga37bd5403c876ff294be5ea72292de4b4)
- [auxdisplay_display_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga02e8e930203cfb1410752a0ffee9a34e)
- [auxdisplay_display_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f9e363765d715edb899901a14c54674)
- [auxdisplay_capabilities_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga4dd5cba56d4b90b77ae8ad02122ef81c)
- [auxdisplay_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaa5a643603353319946c823cc959b74b3)
- [auxdisplay_brightness_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f5be6fefc759607d2859a648a1fb3b8)
- [auxdisplay_brightness_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga34b31b70fdc57e33fc46f1048cc25e1a)
- [auxdisplay_backlight_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf10ebdbe821894ccbeccb35bfa985fea)
- [auxdisplay_backlight_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga28aef24928543329c706513cc7e5b814)
- [auxdisplay_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga2af115a23f370e0770b3c998ecf0b96b)
- [auxdisplay_custom_character_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf03a1068b0aed1f27ee9e2e61066da08)
- [auxdisplay_write](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga231dd862cda34ea4c0c8870675556f8d)
- [auxdisplay_custom_command](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga87064057ae857f81431e6e9f139a6aaa)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__authentication__fido2__fido2_types.h_文件参考.md)
