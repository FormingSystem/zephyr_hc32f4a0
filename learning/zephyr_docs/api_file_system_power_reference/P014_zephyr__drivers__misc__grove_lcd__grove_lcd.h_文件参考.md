---
id: learning.zephyr-docs.api-file-system-power-reference.page-14
title: zephyr__drivers__misc__grove_lcd__grove_lcd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_misc\_\_grove\_lcd\_\_grove\_lcd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_ga4fe4ad1bc603fa658247ea2f7dbf7f31"></a>

```c
#define GLCD_DS_DISPLAY_ON (1 << 2)
```

相关声明：[GLCD_DS_DISPLAY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga4fe4ad1bc603fa658247ea2f7dbf7f31)。

<a id="r_ga66bc1e76fcda544f619d02ecbdcb368f"></a>

```c
#define GLCD_DS_DISPLAY_OFF (0 << 2)
```

相关声明：[GLCD_DS_DISPLAY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga66bc1e76fcda544f619d02ecbdcb368f)。

<a id="r_gaa40ba9872b397a1daa26f68f17d7e28d"></a>

```c
#define GLCD_DS_CURSOR_ON (1 << 1)
```

相关声明：[GLCD_DS_CURSOR_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaa40ba9872b397a1daa26f68f17d7e28d)。

<a id="r_gaac73ba0ea95d570493485212ce704691"></a>

```c
#define GLCD_DS_CURSOR_OFF (0 << 1)
```

相关声明：[GLCD_DS_CURSOR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaac73ba0ea95d570493485212ce704691)。

<a id="r_ga62f05f0aa279c530bb96153efd2a36da"></a>

```c
#define GLCD_DS_BLINK_ON (1 << 0)
```

相关声明：[GLCD_DS_BLINK_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga62f05f0aa279c530bb96153efd2a36da)。

<a id="r_gaca5ebc6bff0db636ff8767f7c225143f"></a>

```c
#define GLCD_DS_BLINK_OFF (0 << 0)
```

相关声明：[GLCD_DS_BLINK_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaca5ebc6bff0db636ff8767f7c225143f)。

<a id="r_ga460a887aaa11dbe4461226a55bcae951"></a>

```c
#define GLCD_IS_SHIFT_INCREMENT (1 << 1)
```

相关声明：[GLCD_IS_SHIFT_INCREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga460a887aaa11dbe4461226a55bcae951)。

<a id="r_ga2258570aac3ed680739324a2daf5f626"></a>

```c
#define GLCD_IS_SHIFT_DECREMENT (0 << 1)
```

相关声明：[GLCD_IS_SHIFT_DECREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga2258570aac3ed680739324a2daf5f626)。

<a id="r_ga5e136501ffbde18b34163bc1a7948c9a"></a>

```c
#define GLCD_IS_ENTRY_LEFT (1 << 0)
```

相关声明：[GLCD_IS_ENTRY_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga5e136501ffbde18b34163bc1a7948c9a)。

<a id="r_ga6c9cee5b9f86efcc2073f60dc204fc2a"></a>

```c
#define GLCD_IS_ENTRY_RIGHT (0 << 0)
```

相关声明：[GLCD_IS_ENTRY_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga6c9cee5b9f86efcc2073f60dc204fc2a)。

<a id="r_ga726ae92e51500c82a202164edb706cd4"></a>

```c
#define GLCD_FS_8BIT_MODE (1 << 4)
```

相关声明：[GLCD_FS_8BIT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga726ae92e51500c82a202164edb706cd4)。

<a id="r_ga7007ac8d919421d34e4dff4e97503cb6"></a>

```c
#define GLCD_FS_ROWS_2 (1 << 3)
```

相关声明：[GLCD_FS_ROWS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga7007ac8d919421d34e4dff4e97503cb6)。

<a id="r_ga2ebedc80c40c35ea57ebcb3968bc1052"></a>

```c
#define GLCD_FS_ROWS_1 (0 << 3)
```

相关声明：[GLCD_FS_ROWS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga2ebedc80c40c35ea57ebcb3968bc1052)。

<a id="r_gabcfa7abdd0834ee469a6693a0aa7f883"></a>

```c
#define GLCD_FS_DOT_SIZE_BIG (1 << 2)
```

相关声明：[GLCD_FS_DOT_SIZE_BIG](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gabcfa7abdd0834ee469a6693a0aa7f883)。

<a id="r_gae47fb073bb30f1fab7171a6bad55fc22"></a>

```c
#define GLCD_FS_DOT_SIZE_LITTLE (0 << 2)
```

相关声明：[GLCD_FS_DOT_SIZE_LITTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gae47fb073bb30f1fab7171a6bad55fc22)。

<a id="r_gaca2204b331e88203b05d0382d80cc5de"></a>

```c
#define GROVE_RGB_WHITE 0
```

相关声明：[GROVE_RGB_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaca2204b331e88203b05d0382d80cc5de)。

<a id="r_gad391aa4262d4fd7e93052e7dafc5daa4"></a>

```c
#define GROVE_RGB_RED 1
```

相关声明：[GROVE_RGB_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gad391aa4262d4fd7e93052e7dafc5daa4)。

<a id="r_ga6e9faff3c1a708d6c5d509a85e1dd1f4"></a>

```c
#define GROVE_RGB_GREEN 2
```

相关声明：[GROVE_RGB_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga6e9faff3c1a708d6c5d509a85e1dd1f4)。

<a id="r_gaf754fe5b8b20bca5ae9768833e045ef8"></a>

```c
#define GROVE_RGB_BLUE 3
```

相关声明：[GROVE_RGB_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaf754fe5b8b20bca5ae9768833e045ef8)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.2\_函数（Functions）

<a id="r_gaecd7b73186d110fa4bd2c47bbb7d63a2"></a>

```c
void glcd_print (const struct device *dev, char *data, uint32_t size)
```

相关声明：[glcd_print](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaecd7b73186d110fa4bd2c47bbb7d63a2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向屏幕（Screen）发送文本。

<a id="r_ga8272c8c1ff41835306908a0f6932feae"></a>

```c
void glcd_cursor_pos_set (const struct device *dev, uint8_t col, uint8_t row)
```

相关声明：[glcd_cursor_pos_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga8272c8c1ff41835306908a0f6932feae)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置后续添加文本使用的光标位置（Text Cursor Position）。

<a id="r_ga10929139f1632247968ccdd4fdd79dcd"></a>

```c
void glcd_clear (const struct device *dev)
```

相关声明：[glcd_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga10929139f1632247968ccdd4fdd79dcd)、[device](../device_reference/P002_设备对象结构.md)。

清除当前显示内容（Display）。

<a id="r_ga103c6edb0b5ed37f34c12694338acc70"></a>

```c
void glcd_display_state_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_display_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga103c6edb0b5ed37f34c12694338acc70)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

改变显示状态（Display State）的函数。

<a id="r_gac3139bf68d1acbb27905a2346da13b17"></a>

```c
uint8_t glcd_display_state_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_display_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gac3139bf68d1acbb27905a2346da13b17)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的显示功能集（Display Feature Set）。

<a id="r_gae73554047414529e5e7957a5d394e4a2"></a>

```c
void glcd_input_state_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_input_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gae73554047414529e5e7957a5d394e4a2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

改变输入状态（Input State）的函数。

<a id="r_ga3c590c83b2f1c8ea0fe301daa7a40198"></a>

```c
uint8_t glcd_input_state_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_input_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga3c590c83b2f1c8ea0fe301daa7a40198)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的输入设置（Input Set）。

<a id="r_ga5e9fb362faf9c040eaa16addbfad2b6d"></a>

```c
void glcd_function_set (const struct device *dev, uint8_t opt)
```

相关声明：[glcd_function_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga5e9fb362faf9c040eaa16addbfad2b6d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器功能状态（Functional State）的函数。

<a id="r_gad660824e481428b811c914d6bf4634f5"></a>

```c
uint8_t glcd_function_get (const struct device *dev)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[glcd_function_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gad660824e481428b811c914d6bf4634f5)、[device](../device_reference/P002_设备对象结构.md)。

返回设备关联的功能设置（Function Set）。

<a id="r_gabd119208e05f9f878b7f24a62da08db2"></a>

```c
void glcd_color_select (const struct device *dev, uint8_t color)
```

相关声明：[glcd_color_select](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gabd119208e05f9f878b7f24a62da08db2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 LCD 背景（Background）设为预定义颜色（Predefined Color）。

<a id="r_gaf99aa37f71396baaf523348a3ea9cbbe"></a>

```c
void glcd_color_set (const struct device *dev, uint8_t r, uint8_t g, uint8_t b)
```

相关声明：[glcd_color_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaf99aa37f71396baaf523348a3ea9cbbe)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 LCD 背景（Background）设为自定义 RGB 颜色值（Color Value）。


## 14.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_architecture_reference/P009_grove_lcd.h_源码浏览.md)
- [GLCD_DS_DISPLAY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga4fe4ad1bc603fa658247ea2f7dbf7f31)
- [GLCD_DS_DISPLAY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga66bc1e76fcda544f619d02ecbdcb368f)
- [GLCD_DS_CURSOR_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaa40ba9872b397a1daa26f68f17d7e28d)
- [GLCD_DS_CURSOR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaac73ba0ea95d570493485212ce704691)
- [GLCD_DS_BLINK_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga62f05f0aa279c530bb96153efd2a36da)
- [GLCD_DS_BLINK_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaca5ebc6bff0db636ff8767f7c225143f)
- [GLCD_IS_SHIFT_INCREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga460a887aaa11dbe4461226a55bcae951)
- [GLCD_IS_SHIFT_DECREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga2258570aac3ed680739324a2daf5f626)
- [GLCD_IS_ENTRY_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga5e136501ffbde18b34163bc1a7948c9a)
- [GLCD_IS_ENTRY_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga6c9cee5b9f86efcc2073f60dc204fc2a)
- [GLCD_FS_8BIT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga726ae92e51500c82a202164edb706cd4)
- [GLCD_FS_ROWS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga7007ac8d919421d34e4dff4e97503cb6)
- [GLCD_FS_ROWS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga2ebedc80c40c35ea57ebcb3968bc1052)
- [GLCD_FS_DOT_SIZE_BIG](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gabcfa7abdd0834ee469a6693a0aa7f883)
- [GLCD_FS_DOT_SIZE_LITTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gae47fb073bb30f1fab7171a6bad55fc22)
- [GROVE_RGB_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaca2204b331e88203b05d0382d80cc5de)
- [GROVE_RGB_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gad391aa4262d4fd7e93052e7dafc5daa4)
- [GROVE_RGB_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga6e9faff3c1a708d6c5d509a85e1dd1f4)
- [GROVE_RGB_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaf754fe5b8b20bca5ae9768833e045ef8)
- [glcd_print](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaecd7b73186d110fa4bd2c47bbb7d63a2)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [glcd_cursor_pos_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga8272c8c1ff41835306908a0f6932feae)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [glcd_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga10929139f1632247968ccdd4fdd79dcd)
- [glcd_display_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga103c6edb0b5ed37f34c12694338acc70)
- [glcd_display_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gac3139bf68d1acbb27905a2346da13b17)
- [glcd_input_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gae73554047414529e5e7957a5d394e4a2)
- [glcd_input_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga3c590c83b2f1c8ea0fe301daa7a40198)
- [glcd_function_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#ga5e9fb362faf9c040eaa16addbfad2b6d)
- [glcd_function_get](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gad660824e481428b811c914d6bf4634f5)
- [glcd_color_select](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gabd119208e05f9f878b7f24a62da08db2)
- [glcd_color_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html#gaf99aa37f71396baaf523348a3ea9cbbe)

---

[上一章](P013_zephyr__drivers__gnss__gnss_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__bluetooth__mesh__health_cli.h_文件参考.md)
