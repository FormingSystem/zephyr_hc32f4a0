---
id: learning.zephyr-docs.api-source-architecture-reference.page-9
title: grove_lcd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_grove\_lcd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h.html)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__grove__display_html_ga103c6edb0b5ed37f34c12694338acc70"></a>
<a id="agroup__grove__display_html_ga10929139f1632247968ccdd4fdd79dcd"></a>
<a id="agroup__grove__display_html_ga3c590c83b2f1c8ea0fe301daa7a40198"></a>
<a id="agroup__grove__display_html_ga5e9fb362faf9c040eaa16addbfad2b6d"></a>
<a id="agroup__grove__display_html_ga8272c8c1ff41835306908a0f6932feae"></a>
<a id="agroup__grove__display_html_gabd119208e05f9f878b7f24a62da08db2"></a>
<a id="agroup__grove__display_html_gac3139bf68d1acbb27905a2346da13b17"></a>
<a id="agroup__grove__display_html_gad660824e481428b811c914d6bf4634f5"></a>
<a id="agroup__grove__display_html_gae73554047414529e5e7957a5d394e4a2"></a>
<a id="agroup__grove__display_html_gaecd7b73186d110fa4bd2c47bbb7d63a2"></a>
<a id="agroup__grove__display_html_gaf99aa37f71396baaf523348a3ea9cbbe"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/* grove_lcd.h - Public API for the Grove RGB LCD device */
/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_GROVE_LCD_GROVE_LCD_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_GROVE_LCD_GROVE_LCD_H_

#include <stdint.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


void glcd_print(const struct device *dev, char *data, uint32_t size);


void glcd_cursor_pos_set(const struct device *dev, uint8_t col, uint8_t row);

void glcd_clear(const struct device *dev);

/* Defines for the GLCD_CMD_DISPLAY_SWITCH options */
#define GLCD_DS_DISPLAY_ON              (1 << 2)
#define GLCD_DS_DISPLAY_OFF             (0 << 2)
#define GLCD_DS_CURSOR_ON               (1 << 1)
#define GLCD_DS_CURSOR_OFF              (0 << 1)
#define GLCD_DS_BLINK_ON                (1 << 0)
#define GLCD_DS_BLINK_OFF               (0 << 0)
void glcd_display_state_set(const struct device *dev, uint8_t opt);

uint8_t glcd_display_state_get(const struct device *dev);

/* Defines for the GLCD_CMD_INPUT_SET to change text direction */
#define GLCD_IS_SHIFT_INCREMENT (1 << 1)
#define GLCD_IS_SHIFT_DECREMENT (0 << 1)
#define GLCD_IS_ENTRY_LEFT      (1 << 0)
#define GLCD_IS_ENTRY_RIGHT     (0 << 0)
void glcd_input_state_set(const struct device *dev, uint8_t opt);

uint8_t glcd_input_state_get(const struct device *dev);

/* Defines for the LCD_FUNCTION_SET */
#define GLCD_FS_8BIT_MODE       (1 << 4)
#define GLCD_FS_ROWS_2          (1 << 3)
#define GLCD_FS_ROWS_1          (0 << 3)
#define GLCD_FS_DOT_SIZE_BIG    (1 << 2)
#define GLCD_FS_DOT_SIZE_LITTLE (0 << 2)
/* Bits 0, 1 are not defined for this register */

void glcd_function_set(const struct device *dev, uint8_t opt);

uint8_t glcd_function_get(const struct device *dev);


/* Available color selections */
#define GROVE_RGB_WHITE         0
#define GROVE_RGB_RED           1
#define GROVE_RGB_GREEN         2
#define GROVE_RGB_BLUE          3
void glcd_color_select(const struct device *dev, uint8_t color);


void glcd_color_set(const struct device *dev, uint8_t r, uint8_t g,
                    uint8_t b);



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_GROVE_LCD_GROVE_LCD_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`grove_lcd.h`：Grove RGB 液晶显示设备（LCD Device）的公共 API（Public API）。

### 注释 2：原第 2 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 51 行

`GLCD_CMD_DISPLAY_SWITCH` 选项（Options）的定义。

### 注释 4：原第 80 行

供 `GLCD_CMD_INPUT_SET` 更改文本方向（Text Direction）使用的定义。

### 注释 5：原第 106 行

`LCD_FUNCTION_SET` 的定义（Defines）。

### 注释 6：原第 112 行

本寄存器未定义位 0 和位 1（Bits 0 and 1）。

### 注释 7：原第 135 行

可用的颜色选项（Color Selections）。

### 注释 8：原第 168 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_GROVE_LCD_GROVE_LCD_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/grove__lcd_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
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
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P008_ft8xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_common.h_源码浏览.md)
