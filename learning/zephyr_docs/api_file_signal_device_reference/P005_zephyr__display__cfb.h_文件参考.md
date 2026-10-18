---
id: learning.zephyr-docs.api-file-signal-device-reference.page-5
title: zephyr__display__cfb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_display\_\_cfb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cfb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单色字符帧缓冲区（Monochrome Character Framebuffer）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/display.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

单色字符帧缓冲区（Monochrome Character Framebuffer）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_cfb_5Ffont"></a>

```c
struct cfb_font
```

相关声明：[cfb_font](../hardware/P185_字符帧缓冲字体结构.md)。

<a id="r_cfb_5Fposition"></a>

```c
struct cfb_position
```

相关声明：[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga1fe25d7d6b057a40715ad44db7bc9249"></a>

```c
#define FONT_ENTRY_DEFINE(_name, _width, _height, _caps, _data, _fc, _lc)
```

相关声明：[FONT_ENTRY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga1fe25d7d6b057a40715ad44db7bc9249)。

创建字体条目（Font Entry）的宏。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_ga32e8edb517093dbc1b612a1bef24c7af"></a>

```c
enum cfb_display_param { CFB_DISPLAY_HEIGHT = 0 , CFB_DISPLAY_WIDTH , CFB_DISPLAY_PPT , CFB_DISPLAY_ROWS , CFB_DISPLAY_COLS }
```

相关声明：[cfb_display_param](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga32e8edb517093dbc1b612a1bef24c7af)、[CFB_DISPLAY_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afaf5bdbd92f8d454caa8d8e2ddf484aaba)、[CFB_DISPLAY_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a)、[CFB_DISPLAY_PPT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630)、[CFB_DISPLAY_ROWS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c)、[CFB_DISPLAY_COLS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)。

<a id="r_gae98337479a5339d4171797e96313fee5"></a>

```c
enum cfb_font_caps { CFB_FONT_MONO_VPACKED = BIT(0) , CFB_FONT_MONO_HPACKED = BIT(1) , CFB_FONT_MSB_FIRST = BIT(2) }
```

相关声明：[cfb_font_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae98337479a5339d4171797e96313fee5)、[CFB_FONT_MONO_VPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6)、[CFB_FONT_MONO_HPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c)、[CFB_FONT_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga029d0f320157e6b2936bb9f0794024d6"></a>

```c
int cfb_print (const struct device *dev, const char *const str, int16_t x, int16_t y)
```

相关声明：[cfb_print](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga029d0f320157e6b2936bb9f0794024d6)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将字符串打印到帧缓冲区（Framebuffer）。

<a id="r_ga496b3b161fa0bc2e42e3d5de83c4f544"></a>

```c
int cfb_draw_text (const struct device *dev, const char *const str, int16_t x, int16_t y)
```

相关声明：[cfb_draw_text](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga496b3b161fa0bc2e42e3d5de83c4f544)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将字符串打印到帧缓冲区（Framebuffer）。

<a id="r_gae1943e8d138f5e612f6508dd0f510134"></a>

```c
int cfb_draw_point (const struct device *dev, const struct cfb_position *pos)
```

相关声明：[cfb_draw_point](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae1943e8d138f5e612f6508dd0f510134)、[device](../device_reference/P002_设备对象结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)。

绘制点（Point）。

<a id="r_ga81af74d2831d5a4fc1338da693401958"></a>

```c
int cfb_draw_line (const struct device *dev, const struct cfb_position *start, const struct cfb_position *end)
```

相关声明：[cfb_draw_line](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga81af74d2831d5a4fc1338da693401958)、[device](../device_reference/P002_设备对象结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)。

绘制线（Line）。

<a id="r_ga0b26cd0d9e2de71f754f85849ccba001"></a>

```c
int cfb_draw_rect (const struct device *dev, const struct cfb_position *start, const struct cfb_position *end)
```

相关声明：[cfb_draw_rect](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga0b26cd0d9e2de71f754f85849ccba001)、[device](../device_reference/P002_设备对象结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)。

绘制矩形（Rectangle）。

<a id="r_ga2a87d5fd58bb7a56081668313f7038f6"></a>

```c
int cfb_draw_circle (const struct device *dev, const struct cfb_position *start, uint16_t radius)
```

相关声明：[cfb_draw_circle](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2a87d5fd58bb7a56081668313f7038f6)、[device](../device_reference/P002_设备对象结构.md)、[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制圆（Circle）。

<a id="r_gac9a957b5dd6e99377d9c070085df3252"></a>

```c
int cfb_framebuffer_clear (const struct device *dev, bool clear_display)
```

相关声明：[cfb_framebuffer_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac9a957b5dd6e99377d9c070085df3252)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

清除帧缓冲区（Framebuffer）。

<a id="r_ga8e86d48a0c6d951de34089f5d6cf5fb1"></a>

```c
int cfb_framebuffer_invert (const struct device *dev)
```

相关声明：[cfb_framebuffer_invert](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga8e86d48a0c6d951de34089f5d6cf5fb1)、[device](../device_reference/P002_设备对象结构.md)。

反转像素（Invert Pixels）。

<a id="r_ga02dbf9751af0ee01e20a293b94fcfb7a"></a>

```c
int cfb_invert_area (const struct device *dev, int16_t x, int16_t y, uint16_t width, uint16_t height)
```

相关声明：[cfb_invert_area](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga02dbf9751af0ee01e20a293b94fcfb7a)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

反转选定区域内的像素（Invert Pixels）。

<a id="r_ga9d0b3f63c2b52458ab040993b3c3b97d"></a>

```c
int cfb_framebuffer_finalize (const struct device *dev)
```

相关声明：[cfb_framebuffer_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga9d0b3f63c2b52458ab040993b3c3b97d)、[device](../device_reference/P002_设备对象结构.md)。

完成帧缓冲区（Framebuffer）处理并写入显示 RAM，必要时反转或重排像素。

<a id="r_gaeb46dfb72c31474c1acbc46d2f08803e"></a>

```c
int cfb_get_display_parameter (const struct device *dev, enum cfb_display_param)
```

相关声明：[cfb_get_display_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gaeb46dfb72c31474c1acbc46d2f08803e)、[device](../device_reference/P002_设备对象结构.md)、[cfb_display_param](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga32e8edb517093dbc1b612a1bef24c7af)。

获取显示参数（Display Parameter）。

<a id="r_ga29343c61a7a9e28c50cb384ba4f383cf"></a>

```c
int cfb_framebuffer_set_font (const struct device *dev, uint8_t idx)
```

相关声明：[cfb_framebuffer_set_font](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga29343c61a7a9e28c50cb384ba4f383cf)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置字体（Font）。

<a id="r_gac0918644cb24a39ef578e54acac46d64"></a>

```c
int cfb_set_kerning (const struct device *dev, int8_t kerning)
```

相关声明：[cfb_set_kerning](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac0918644cb24a39ef578e54acac46d64)、[device](../device_reference/P002_设备对象结构.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置字体字距（Font Kerning），即各字母之间的间距。

<a id="r_ga63ea5f559391ed735da8afa78745e458"></a>

```c
int cfb_get_font_size (const struct device *dev, uint8_t idx, uint8_t *width, uint8_t *height)
```

相关声明：[cfb_get_font_size](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga63ea5f559391ed735da8afa78745e458)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取字体大小（Font Size）。

<a id="r_ga5ef3b84b6169eaef398cf47b3583c827"></a>

```c
int cfb_get_numof_fonts (const struct device *dev)
```

相关声明：[cfb_get_numof_fonts](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga5ef3b84b6169eaef398cf47b3583c827)、[device](../device_reference/P002_设备对象结构.md)。

获取字体数量（Number of Fonts）。

<a id="r_ga2bbe913d7f0a10b4ba543d83ef6fac95"></a>

```c
int cfb_framebuffer_init (const struct device *dev)
```

相关声明：[cfb_framebuffer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2bbe913d7f0a10b4ba543d83ef6fac95)、[device](../device_reference/P002_设备对象结构.md)。

初始化字符帧缓冲区（Character Framebuffer）。

<a id="r_ga981f062bb314c107230e068f575f81ef"></a>

```c
void cfb_framebuffer_deinit (const struct device *dev)
```

相关声明：[cfb_framebuffer_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga981f062bb314c107230e068f575f81ef)、[device](../device_reference/P002_设备对象结构.md)。

反初始化字符帧缓冲区（Character Framebuffer）。


## 5.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P087_cfb.h_源码浏览.md)
- [cfb_font](../hardware/P185_字符帧缓冲字体结构.md)
- [cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)
- [FONT_ENTRY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga1fe25d7d6b057a40715ad44db7bc9249)
- [cfb_display_param](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga32e8edb517093dbc1b612a1bef24c7af)
- [CFB_DISPLAY_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afaf5bdbd92f8d454caa8d8e2ddf484aaba)
- [CFB_DISPLAY_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a)
- [CFB_DISPLAY_PPT](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630)
- [CFB_DISPLAY_ROWS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c)
- [CFB_DISPLAY_COLS](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)
- [cfb_font_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae98337479a5339d4171797e96313fee5)
- [CFB_FONT_MONO_VPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6)
- [CFB_FONT_MONO_HPACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c)
- [CFB_FONT_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b)
- [cfb_print](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga029d0f320157e6b2936bb9f0794024d6)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [cfb_draw_text](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga496b3b161fa0bc2e42e3d5de83c4f544)
- [cfb_draw_point](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gae1943e8d138f5e612f6508dd0f510134)
- [cfb_draw_line](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga81af74d2831d5a4fc1338da693401958)
- [cfb_draw_rect](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga0b26cd0d9e2de71f754f85849ccba001)
- [cfb_draw_circle](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2a87d5fd58bb7a56081668313f7038f6)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [cfb_framebuffer_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac9a957b5dd6e99377d9c070085df3252)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [cfb_framebuffer_invert](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga8e86d48a0c6d951de34089f5d6cf5fb1)
- [cfb_invert_area](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga02dbf9751af0ee01e20a293b94fcfb7a)
- [cfb_framebuffer_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga9d0b3f63c2b52458ab040993b3c3b97d)
- [cfb_get_display_parameter](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gaeb46dfb72c31474c1acbc46d2f08803e)
- [cfb_framebuffer_set_font](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga29343c61a7a9e28c50cb384ba4f383cf)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cfb_set_kerning](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#gac0918644cb24a39ef578e54acac46d64)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [cfb_get_font_size](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga63ea5f559391ed735da8afa78745e458)
- [cfb_get_numof_fonts](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga5ef3b84b6169eaef398cf47b3583c827)
- [cfb_framebuffer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2bbe913d7f0a10b4ba543d83ef6fac95)
- [cfb_framebuffer_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga981f062bb314c107230e068f575f81ef)

<a id="header-details"></a>

---

[上一章](P004_zephyr__drivers__cellular.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__i3c__devicetree.h_文件参考.md)
