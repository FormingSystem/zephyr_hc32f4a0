---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-1
title: 辅助文本显示器（Auxiliary Text Display）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_辅助文本显示器（Auxiliary Text Display）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

辅助显示器接口，适用于文本显示和非图形显示（Textual/non-graphical displays）。

<a id="details"></a>

辅助显示器接口（Auxiliary Display Interfaces），用于文本／非图形显示。自 3.4 起提供（Since 3.4），版本（Version）0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_auxdisplay_5Finterface_5Fbackend"></a>

相关声明：[辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_auxdisplay_2Eh"></a>

```c
file auxdisplay.h
```

相关声明：[auxdisplay.h](../api_file_flash_test_reference/P001_zephyr__drivers__auxdisplay.h_文件参考.md)。

辅助显示器（Auxiliary Display，文本式/非图形式）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_ga0bd1d97b360f3138887a5e3e4729e01b"></a>

```c
#define AUXDISPLAY_LIGHT_NOT_SUPPORTED 0
```

相关声明：[AUXDISPLAY_LIGHT_NOT_SUPPORTED](#ga0bd1d97b360f3138887a5e3e4729e01b)。

不支持亮度／背光（Brightness/Backlight）时，用作其最小值和最大值。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_ga78861a5414ac95e9ca77436c0b82acc2"></a>

```c
typedef uint32_t auxdisplay_mode_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[auxdisplay_mode_t](#ga78861a5414ac95e9ca77436c0b82acc2)。

用于描述辅助文本显示器（Auxiliary Text Display）的模式。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_ga98b0be37fc76df0ae4dec0bef6c94504"></a>

```c
enum auxdisplay_position { AUXDISPLAY_POSITION_ABSOLUTE = 0 , AUXDISPLAY_POSITION_RELATIVE , AUXDISPLAY_POSITION_RELATIVE_DIRECTION , AUXDISPLAY_POSITION_COUNT }
```

相关声明：[auxdisplay_position](#ga98b0be37fc76df0ae4dec0bef6c94504)、[AUXDISPLAY_POSITION_ABSOLUTE](#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)、[AUXDISPLAY_POSITION_RELATIVE](#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)、[AUXDISPLAY_POSITION_RELATIVE_DIRECTION](#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)、[AUXDISPLAY_POSITION_COUNT](#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)。

用于移动光标或显示位置（Cursor or Display Position）。

<a id="r_ga5f95ac69e18091883e7121103014be10"></a>

```c
enum auxdisplay_direction { AUXDISPLAY_DIRECTION_RIGHT = 0 , AUXDISPLAY_DIRECTION_LEFT , AUXDISPLAY_DIRECTION_COUNT }
```

相关声明：[auxdisplay_direction](#ga5f95ac69e18091883e7121103014be10)、[AUXDISPLAY_DIRECTION_RIGHT](#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)、[AUXDISPLAY_DIRECTION_LEFT](#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352)、[AUXDISPLAY_DIRECTION_COUNT](#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)。

用于设置字符追加位置（Character Append Position）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_gaffb3c1c41d810355fe2da3558ebba0c2"></a>

```c
int auxdisplay_display_on (const struct device *dev)
```

相关声明：[auxdisplay_display_on](#gaffb3c1c41d810355fe2da3558ebba0c2)、[device](../device_reference/P002_设备对象结构.md)。

开启显示器（Display）。

<a id="r_ga625f399720417715090793c7f6d63f7e"></a>

```c
int auxdisplay_display_off (const struct device *dev)
```

相关声明：[auxdisplay_display_off](#ga625f399720417715090793c7f6d63f7e)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示器（Display）。

<a id="r_ga7191475b362f728cc92eb07cb1f2ed00"></a>

```c
int auxdisplay_cursor_set_enabled (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_cursor_set_enabled](#ga7191475b362f728cc92eb07cb1f2ed00)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置辅助显示器（Auxiliary Display）的光标启用状态（Cursor Enabled Status）。

<a id="r_ga7102ec9941f8b3131a18e4ff7b640241"></a>

```c
int auxdisplay_position_blinking_set_enabled (const struct device *dev, bool enabled)
```

相关声明：[auxdisplay_position_blinking_set_enabled](#ga7102ec9941f8b3131a18e4ff7b640241)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置辅助显示器（Auxiliary Display）的光标闪烁状态（Cursor Blinking Status）。

<a id="r_gafb18729b4897cea83dbfc1c7241f5b2d"></a>

```c
int auxdisplay_cursor_shift_set (const struct device *dev, uint8_t direction, bool display_shift)
```

相关声明：[auxdisplay_cursor_shift_set](#gafb18729b4897cea83dbfc1c7241f5b2d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置写入字符后的光标移动（Cursor Shift）及显示移动（Display Shift）。

<a id="r_ga9c6302789d9cc9e481dd7c54ef370988"></a>

```c
int auxdisplay_cursor_position_set (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_cursor_position_set](#ga9c6302789d9cc9e481dd7c54ef370988)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置辅助显示器的光标及写入位置（Cursor and Write Position）。

<a id="r_ga37bd5403c876ff294be5ea72292de4b4"></a>

```c
int auxdisplay_cursor_position_get (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_cursor_position_get](#ga37bd5403c876ff294be5ea72292de4b4)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取辅助显示器的当前光标（Current Cursor）。

<a id="r_ga02e8e930203cfb1410752a0ffee9a34e"></a>

```c
int auxdisplay_display_position_set (const struct device *dev, enum auxdisplay_position type, int16_t x, int16_t y)
```

相关声明：[auxdisplay_display_position_set](#ga02e8e930203cfb1410752a0ffee9a34e)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_position](#ga98b0be37fc76df0ae4dec0bef6c94504)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置辅助显示器的显示位置（Display Position）。

<a id="r_ga1f9e363765d715edb899901a14c54674"></a>

```c
int auxdisplay_display_position_get (const struct device *dev, int16_t *x, int16_t *y)
```

相关声明：[auxdisplay_display_position_get](#ga1f9e363765d715edb899901a14c54674)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取辅助显示器的当前显示位置（Display Position）。

<a id="r_ga4dd5cba56d4b90b77ae8ad02122ef81c"></a>

```c
int auxdisplay_capabilities_get (const struct device *dev, struct auxdisplay_capabilities *capabilities)
```

相关声明：[auxdisplay_capabilities_get](#ga4dd5cba56d4b90b77ae8ad02122ef81c)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)。

获取辅助显示器的能力及详细信息（Capabilities and Details）。

<a id="r_gaa5a643603353319946c823cc959b74b3"></a>

```c
int auxdisplay_clear (const struct device *dev)
```

相关声明：[auxdisplay_clear](#gaa5a643603353319946c823cc959b74b3)、[device](../device_reference/P002_设备对象结构.md)。

清空辅助显示器并返回起始位置（Home Position）。

<a id="r_ga1f5be6fefc759607d2859a648a1fb3b8"></a>

```c
int auxdisplay_brightness_get (const struct device *dev, uint8_t *brightness)
```

相关声明：[auxdisplay_brightness_get](#ga1f5be6fefc759607d2859a648a1fb3b8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取辅助显示器的当前亮度级别（Brightness Level）。

<a id="r_ga34b31b70fdc57e33fc46f1048cc25e1a"></a>

```c
int auxdisplay_brightness_set (const struct device *dev, uint8_t brightness)
```

相关声明：[auxdisplay_brightness_set](#ga34b31b70fdc57e33fc46f1048cc25e1a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新辅助显示器的亮度级别（Brightness Level）。

<a id="r_gaf10ebdbe821894ccbeccb35bfa985fea"></a>

```c
int auxdisplay_backlight_get (const struct device *dev, uint8_t *backlight)
```

相关声明：[auxdisplay_backlight_get](#gaf10ebdbe821894ccbeccb35bfa985fea)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取辅助显示器的背光级别详情（Backlight Level Details）。

<a id="r_ga28aef24928543329c706513cc7e5b814"></a>

```c
int auxdisplay_backlight_set (const struct device *dev, uint8_t backlight)
```

相关声明：[auxdisplay_backlight_set](#ga28aef24928543329c706513cc7e5b814)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新辅助显示器的背光级别（Backlight Level）。

<a id="r_ga2af115a23f370e0770b3c998ecf0b96b"></a>

```c
int auxdisplay_is_busy (const struct device *dev)
```

相关声明：[auxdisplay_is_busy](#ga2af115a23f370e0770b3c998ecf0b96b)、[device](../device_reference/P002_设备对象结构.md)。

检查辅助显示驱动（Auxiliary Display Driver）是否忙碌。

<a id="r_gaf03a1068b0aed1f27ee9e2e61066da08"></a>

```c
int auxdisplay_custom_character_set (const struct device *dev, struct auxdisplay_character *character)
```

相关声明：[auxdisplay_custom_character_set](#gaf03a1068b0aed1f27ee9e2e61066da08)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)。

在显示器中设置自定义字符（Custom Character）。

<a id="r_ga231dd862cda34ea4c0c8870675556f8d"></a>

```c
int auxdisplay_write (const struct device *dev, const uint8_t *data, uint16_t len)
```

相关声明：[auxdisplay_write](#ga231dd862cda34ea4c0c8870675556f8d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在当前位置向辅助显示器屏幕写入数据。

<a id="r_ga87064057ae857f81431e6e9f139a6aaa"></a>

```c
int auxdisplay_custom_command (const struct device *dev, struct auxdisplay_custom_data *data)
```

相关声明：[auxdisplay_custom_command](#ga87064057ae857f81431e6e9f139a6aaa)、[device](../device_reference/P002_设备对象结构.md)、[auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)。

向显示器发送自定义命令（Custom Command），需要驱动支持。

<a id="r_ga7930b8287b2cefa08af90a755fd5651c"></a>

```c
int auxdisplay_custom_indicator_set (const struct device *dev, uint8_t index, bool enable)
```

相关声明：[auxdisplay_custom_indicator_set](#ga7930b8287b2cefa08af90a755fd5651c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭显示器上的自定义指示器（Custom Indicator）。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga0bd1d97b360f3138887a5e3e4729e01b"></a>

### `AUXDISPLAY_LIGHT_NOT_SUPPORTED`

```c
#define AUXDISPLAY_LIGHT_NOT_SUPPORTED 0
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

不支持亮度／背光（Brightness/Backlight）时，用作其最小值和最大值。

<a id="ga78861a5414ac95e9ca77436c0b82acc2"></a>

### `auxdisplay_mode_t`

```c
typedef uint32_t auxdisplay_mode_t
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

用于描述辅助文本显示器（Auxiliary Text Display）的模式。

<a id="ga5f95ac69e18091883e7121103014be10"></a>

### `auxdisplay_direction`

```c
enum auxdisplay_direction
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

用于设置字符追加位置（Character Append Position）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUXDISPLAY_DIRECTION_RIGHT` | 每个字符放置在已有字符的右侧。 |
| `AUXDISPLAY_DIRECTION_LEFT` | 每个字符放置在已有字符的左侧。 |
| `AUXDISPLAY_DIRECTION_COUNT` |  |

<a id="ga98b0be37fc76df0ae4dec0bef6c94504"></a>

### `auxdisplay_position`

```c
enum auxdisplay_position
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

用于移动光标或显示位置（Cursor or Display Position）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUXDISPLAY_POSITION_ABSOLUTE` | 移动到指定的 X、Y 位置（Position）。 |
| `AUXDISPLAY_POSITION_RELATIVE` | 将当前位置按正／负 X、Y 偏移量移动，不考虑显示方向（Display Direction）。 |
| `AUXDISPLAY_POSITION_RELATIVE_DIRECTION` | 将当前位置按正／负 X、Y 偏移量移动，并考虑显示方向（Display Direction）。 |
| `AUXDISPLAY_POSITION_COUNT` |  |

<a id="gaf10ebdbe821894ccbeccb35bfa985fea"></a>

### `auxdisplay_backlight_get()`

```c
int auxdisplay_backlight_get ( const struct device * dev, uint8_t * backlight )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取辅助显示器的背光级别详情（Backlight Level Details）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `backlight` | 将更新为当前背光级别（Backlight Level）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga28aef24928543329c706513cc7e5b814"></a>

### `auxdisplay_backlight_set()`

```c
int auxdisplay_backlight_set ( const struct device * dev, uint8_t backlight )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

更新辅助显示器的背光级别（Backlight Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `backlight` | 要设置的背光级别（Backlight Level）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga1f5be6fefc759607d2859a648a1fb3b8"></a>

### `auxdisplay_brightness_get()`

```c
int auxdisplay_brightness_get ( const struct device * dev, uint8_t * brightness )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取辅助显示器的当前亮度级别（Brightness Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `brightness` | 将更新为当前亮度（Brightness）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga34b31b70fdc57e33fc46f1048cc25e1a"></a>

### `auxdisplay_brightness_set()`

```c
int auxdisplay_brightness_set ( const struct device * dev, uint8_t brightness )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

更新辅助显示器的亮度级别（Brightness Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `brightness` | 要设置的亮度级别（Brightness Level）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4dd5cba56d4b90b77ae8ad02122ef81c"></a>

### `auxdisplay_capabilities_get()`

```c
int auxdisplay_capabilities_get ( const struct device * dev, struct auxdisplay_capabilities * capabilities )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取辅助显示器的能力及详细信息（Capabilities and Details）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `capabilities` | 将更新为辅助显示器的详细信息（Auxiliary Display Details）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa5a643603353319946c823cc959b74b3"></a>

### `auxdisplay_clear()`

```c
int auxdisplay_clear ( const struct device * dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

清空辅助显示器并返回起始位置（Home Position）。

注意：这不会重置显示配置（Display Configuration），例如自定义字符（Custom Characters）和显示模式（Display Mode）会保留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga37bd5403c876ff294be5ea72292de4b4"></a>

### `auxdisplay_cursor_position_get()`

```c
int auxdisplay_cursor_position_get ( const struct device * dev, int16_t * x, int16_t * y )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取辅助显示器的当前光标（Current Cursor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `x` | 将更新为精确的 X 位置（X Position）。 |
| `y` | 将更新为精确的 Y 位置（Y Position）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga9c6302789d9cc9e481dd7c54ef370988"></a>

### `auxdisplay_cursor_position_set()`

```c
int auxdisplay_cursor_position_set ( const struct device * dev, enum auxdisplay_position type, int16_t x, int16_t y )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置辅助显示器的光标及写入位置（Cursor and Write Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `type` | 移动类型（Move Type），为绝对位置（Absolute）或偏移（Offset）。 |
| `x` | 精确的 X 位置或 X 偏移量（X Position/Offset）。 |
| `y` | 精确的 Y 位置或 Y 偏移量（Y Position/Offset）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7191475b362f728cc92eb07cb1f2ed00"></a>

### `auxdisplay_cursor_set_enabled()`

```c
int auxdisplay_cursor_set_enabled ( const struct device * dev, bool enabled )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置辅助显示器（Auxiliary Display）的光标启用状态（Cursor Enabled Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `enabled` | true 表示启用光标（Cursor），false 表示禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gafb18729b4897cea83dbfc1c7241f5b2d"></a>

### `auxdisplay_cursor_shift_set()`

```c
int auxdisplay_cursor_shift_set ( const struct device * dev, uint8_t direction, bool display_shift )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置写入字符后的光标移动（Cursor Shift）及显示移动（Display Shift）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `direction` | 设置写入字符时的显示方向（Display Direction）。 |
| `display_shift` | 为 true 时，在写入字符时移动显示内容（Shift Display），视觉上表现为显示内容移动，而非光标移动。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf03a1068b0aed1f27ee9e2e61066da08"></a>

### `auxdisplay_custom_character_set()`

```c
int auxdisplay_custom_character_set ( const struct device * dev, struct auxdisplay_character * character )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

在显示器中设置自定义字符（Custom Character）。

自定义字符结构体（Custom Character Struct）必须包含待添加字符的像素数据（Pixel Data）和有效的自定义字符索引。成功时，结构体中的 character_code 变量将设置为可用于 auxdisplay_write() 函数的字符编码（Character Code），以显示该字符。

字符必须对该显示器有效，并以大小为字符宽度乘字符高度的 uint8 数组表示。像素关闭时值为 0x00，像素开启时为 0xff；如果显示器支持灰度（Shades），则可使用 0x00 与 0xff 之间的值，具体取决于显示驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `character` | 指向自定义字符结构体（Custom Character Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga87064057ae857f81431e6e9f139a6aaa"></a>

### `auxdisplay_custom_command()`

```c
int auxdisplay_custom_command ( const struct device * dev, struct auxdisplay_custom_data * data )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

向显示器发送自定义命令（Custom Command），需要驱动支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `data` | 自定义命令结构体（Custom Command Structure），具体驱动可以扩展它。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7930b8287b2cefa08af90a755fd5651c"></a>

### `auxdisplay_custom_indicator_set()`

```c
int auxdisplay_custom_indicator_set ( const struct device * dev, uint8_t index, bool enable )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

开启或关闭显示器上的自定义指示器（Custom Indicator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `index` | 要控制的自定义指示器索引（Custom Indicator Index）。 |
| `enable` | true 表示开启指示器（Indicator），false 表示关闭。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga625f399720417715090793c7f6d63f7e"></a>

### `auxdisplay_display_off()`

```c
int auxdisplay_display_off ( const struct device * dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

关闭显示器（Display）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaffb3c1c41d810355fe2da3558ebba0c2"></a>

### `auxdisplay_display_on()`

```c
int auxdisplay_display_on ( const struct device * dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

开启显示器（Display）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga1f9e363765d715edb899901a14c54674"></a>

### `auxdisplay_display_position_get()`

```c
int auxdisplay_display_position_get ( const struct device * dev, int16_t * x, int16_t * y )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

获取辅助显示器的当前显示位置（Display Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `x` | 将更新为精确的 X 位置（X Position）。 |
| `y` | 将更新为精确的 Y 位置（Y Position）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga02e8e930203cfb1410752a0ffee9a34e"></a>

### `auxdisplay_display_position_set()`

```c
int auxdisplay_display_position_set ( const struct device * dev, enum auxdisplay_position type, int16_t x, int16_t y )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置辅助显示器的显示位置（Display Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `type` | 移动类型（Move Type），为绝对位置（Absolute）或偏移（Offset）。 |
| `x` | 精确的 X 位置或 X 偏移量（X Position/Offset）。 |
| `y` | 精确的 Y 位置或 Y 偏移量（Y Position/Offset）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga2af115a23f370e0770b3c998ecf0b96b"></a>

### `auxdisplay_is_busy()`

```c
int auxdisplay_is_busy ( const struct device * dev)
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

检查辅助显示驱动（Auxiliary Display Driver）是否忙碌。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 操作成功且显示器忙碌（Busy）时。 |
| `0` | 操作成功且显示器不忙碌（Not Busy）时。 |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

**返回（Returns）**：**返回值（Returns）：**失败时返回负 `errno`。

<a id="ga7102ec9941f8b3131a18e4ff7b640241"></a>

### `auxdisplay_position_blinking_set_enabled()`

```c
int auxdisplay_position_blinking_set_enabled ( const struct device * dev, bool enabled )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

设置辅助显示器（Auxiliary Display）的光标闪烁状态（Cursor Blinking Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `enabled` | 设置为 true 以启用位置闪烁（Blinking Position），false 以禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 不受支持／未实现（Not Supported/Implemented）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga231dd862cda34ea4c0c8870675556f8d"></a>

### `auxdisplay_write()`

```c
int auxdisplay_write ( const struct device * dev, const uint8_t * data, uint16_t len )
```

```c
#include <zephyr/drivers/auxdisplay.h>
```

在当前位置向辅助显示器屏幕写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 辅助显示设备实例（Auxiliary Display Device Instance）。 |
| `data` | 要写入的文本数据（Text Data）。 |
| `len` | 要写入的文本数据长度（Text Data Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 所提供参数无效（Invalid Argument）时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 1.9\_原页交叉引用（Cross References）

- [辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）](../api_coap_trusted_topic_reference/P001_辅助显示器驱动后端 API（Auxiliary Display Driver Backend API）.md)
- [auxdisplay.h](../api_file_flash_test_reference/P001_zephyr__drivers__auxdisplay.h_文件参考.md)
- [auxdisplay_light](../driver_model_reference/P023_辅助显示器亮度.md)
- [auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)
- [auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)
- [auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599"></a>
<a id="gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352"></a>
<a id="gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3"></a>
<a id="gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404"></a>
<a id="gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28"></a>
<a id="gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558"></a>
<a id="gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_音频流控制服务（Audio Stream Control Service，ASCS）.md)
