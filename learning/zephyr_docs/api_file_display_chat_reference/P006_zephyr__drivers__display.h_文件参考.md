---
id: learning.zephyr-docs.api-file-display-chat-reference.page-6
title: zephyr__drivers__display.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_display.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

显示（Display）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <errno.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/dt-bindings/display/panel.h>
```

查看此文件的源码。

显示（Display）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_display_5Fpalette_5Fcolor"></a>

```c
struct display_palette_color
```

相关声明：[display_palette_color](../hardware/P218_显示调色板颜色.md)。

表示ARGB8888格式调色板条目（Color Palette Entry）的结构。

<a id="r_display_5Fcapabilities"></a>

```c
struct display_capabilities
```

相关声明：[display_capabilities](../hardware/P216_显示能力结构.md)。

保存显示器能力（Display Capabilities）的结构体。

<a id="r_display_5Fbuffer_5Fdescriptor"></a>

```c
struct display_buffer_descriptor
```

相关声明：[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

描述显示数据缓冲区布局（Display Data Buffer Layout）的结构。

<a id="r_display_5Fevent_5Fdata"></a>

```c
struct display_event_data
```

相关声明：[display_event_data](../hardware/P217_显示事件数据.md)。

显示事件（Display Event）的载荷。

<a id="r_display_5Fdriver_5Fapi"></a>

```c
struct display_driver_api
```

相关声明：[display_driver_api](../hardware/P220_显示驱动函数表.md)。

驱动操作（Driver Operations）：显示（Display）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga3b305be04da5921ca4087498627dc061"></a>

```c
#define DISPLAY_BITS_PER_PIXEL(fmt)
```

相关声明：[DISPLAY_BITS_PER_PIXEL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3b305be04da5921ca4087498627dc061)。

显示格式（Display Format）每像素所需的位数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gadca2fe10ecb27b5e82309bbab5e886ee"></a>

```c
typedef enum display_event_result(* display_event_cb_t) (const struct device *dev, uint32_t evt, const struct display_event_data *data, void *user_data)
```

相关声明：[display_event_result](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga5c3bcf15b62c66c1677e51a10451efe5)、[display_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gadca2fe10ecb27b5e82309bbab5e886ee)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[display_event_data](../hardware/P217_显示事件数据.md)。

在中断服务例程上下文（ISR Context）中调用（注册时 in_isr=true，参见 display_register_event_cb），或在线程上下文（Thread Context）中调用（in_isr=false 时，驱动调度工作项来调用它）。

<a id="r_gacf66a054396ccd8e178591b8fc98ff4d"></a>

```c
typedef int(* display_blanking_on_api) (const struct device *dev)
```

相关声明：[display_blanking_on_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gacf66a054396ccd8e178591b8fc98ff4d)、[device](../device_reference/P002_设备对象结构.md)。

开启显示消隐（Display Blanking）的回调 API。

<a id="r_gab23bbd9305792d6e37d2e4ff91a2b175"></a>

```c
typedef int(* display_blanking_off_api) (const struct device *dev)
```

相关声明：[display_blanking_off_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gab23bbd9305792d6e37d2e4ff91a2b175)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示消隐（Display Blanking）的回调 API。

<a id="r_ga5cab904b24062fdea531f450a8e5c367"></a>

```c
typedef int(* display_write_api) (const struct device *dev, const uint16_t x, const uint16_t y, const struct display_buffer_descriptor *desc, const void *buf)
```

相关声明：[display_write_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga5cab904b24062fdea531f450a8e5c367)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

向显示器写入数据的回调 API（Callback API）。

<a id="r_ga9ed51d3f666f747d9fb7f1f7746611b3"></a>

```c
typedef int(* display_read_api) (const struct device *dev, const uint16_t x, const uint16_t y, const struct display_buffer_descriptor *desc, void *buf)
```

相关声明：[display_read_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga9ed51d3f666f747d9fb7f1f7746611b3)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

从显示器读取数据的回调 API（Callback API）。

<a id="r_gaf42820ae69452788bf51f37512ca8586"></a>

```c
typedef int(* display_clear_api) (const struct device *dev)
```

相关声明：[display_clear_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaf42820ae69452788bf51f37512ca8586)、[device](../device_reference/P002_设备对象结构.md)。

清空显示器屏幕（Clear Screen）的回调 API。

<a id="r_ga6dd281032ad400d3adc7f5f812c5fe12"></a>

```c
typedef void *(* display_get_framebuffer_api) (const struct device *dev)
```

相关声明：[display_get_framebuffer_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6dd281032ad400d3adc7f5f812c5fe12)、[device](../device_reference/P002_设备对象结构.md)。

获取帧缓冲区指针（Framebuffer Pointer）的回调 API。

<a id="r_ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a"></a>

```c
typedef int(* display_set_brightness_api) (const struct device *dev, const uint8_t brightness)
```

相关声明：[display_set_brightness_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示亮度（Display Brightness）的回调 API。

<a id="r_gadf115352908f94b0a0bf225dbdd8ee85"></a>

```c
typedef int(* display_set_contrast_api) (const struct device *dev, const uint8_t contrast)
```

相关声明：[display_set_contrast_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadf115352908f94b0a0bf225dbdd8ee85)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示对比度（Display Contrast）的回调 API。

<a id="r_ga474f85a33aef019dddb1c720ea23f3fb"></a>

```c
typedef void(* display_get_capabilities_api) (const struct device *dev, struct display_capabilities *capabilities)
```

相关声明：[display_get_capabilities_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga474f85a33aef019dddb1c720ea23f3fb)、[device](../device_reference/P002_设备对象结构.md)、[display_capabilities](../hardware/P216_显示能力结构.md)。

获取显示能力（Display Capabilities）的回调 API。

<a id="r_ga2637286cf3a97c2b532bb33f22263303"></a>

```c
typedef int(* display_set_pixel_format_api) (const struct device *dev, const enum display_pixel_format pixel_format)
```

相关声明：[display_set_pixel_format_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga2637286cf3a97c2b532bb33f22263303)、[device](../device_reference/P002_设备对象结构.md)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

设置显示器所用像素格式（Pixel Format）的回调 API。

<a id="r_gaff3b76a6601cf176782be940139ccb48"></a>

```c
typedef int(* display_set_orientation_api) (const struct device *dev, const enum display_orientation orientation)
```

相关声明：[display_set_orientation_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaff3b76a6601cf176782be940139ccb48)、[device](../device_reference/P002_设备对象结构.md)、[display_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac59b091a3ed39431ab97a5f19fdc4855)。

设置显示器所用方向（Orientation）的回调 API。

<a id="r_gac0a36d044e4663ab5ee61d1e11d645d0"></a>

```c
typedef int(* display_register_event_cb_api) (const struct device *dev, display_event_cb_t cb, void *user_data, uint32_t event_mask, bool in_isr, uint32_t *out_reg_handle)
```

相关声明：[display_register_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gac0a36d044e4663ab5ee61d1e11d645d0)、[device](../device_reference/P002_设备对象结构.md)、[display_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gadca2fe10ecb27b5e82309bbab5e886ee)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

注册显示事件回调（Display Event Callback）的回调 API。

<a id="r_gadd468c71193663072489f32885bc30e5"></a>

```c
typedef int(* display_unregister_event_cb_api) (const struct device *dev, uint32_t reg_handle)
```

相关声明：[display_unregister_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadd468c71193663072489f32885bc30e5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

注销显示事件回调（Display Event Callback）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_gac346bc56771052a8fe919c3ec23d7c9c"></a>

```c
enum display_pixel_format { PIXEL_FORMAT_RGB_888 = BIT(0) , PIXEL_FORMAT_MONO01 = BIT(1) , PIXEL_FORMAT_MONO10 = BIT(2) , PIXEL_FORMAT_ARGB_8888 = BIT(3) , PIXEL_FORMAT_RGB_565 = BIT(4) , PIXEL_FORMAT_RGB_565X = BIT(5) , PIXEL_FORMAT_L_8 = BIT(6) , PIXEL_FORMAT_AL_88 = BIT(7) , PIXEL_FORMAT_XRGB_8888 = BIT(8) , PIXEL_FORMAT_BGR_888 = BIT(9) , PIXEL_FORMAT_ABGR_8888 = BIT(10) , PIXEL_FORMAT_RGBA_8888 = BIT(11) , PIXEL_FORMAT_BGRA_8888 = BIT(12) , PIXEL_FORMAT_I_4 = BIT(13) , PIXEL_FORMAT_L_4 = BIT(14) , PIXEL_FORMAT_YUYV = BIT(15) }
```

相关声明：[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)、[PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)、[PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)、[PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)、[PIXEL_FORMAT_ARGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)、[PIXEL_FORMAT_RGB_565](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)、[PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)、[PIXEL_FORMAT_L_8](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df)、[PIXEL_FORMAT_AL_88](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca92f4901daf73e26c4290e656e7afeb2f)、[PIXEL_FORMAT_XRGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca20bb97558d4acdf225a157c40d9058ab)、[PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172)、[PIXEL_FORMAT_ABGR_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca049f2930dfd1efadfb17a113ba0d879d)、[PIXEL_FORMAT_RGBA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca9de42e120e50119c2df1c503ed2e7a28)、[PIXEL_FORMAT_BGRA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca142784152249100847b0e5c6d656191c)、[PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a)、[PIXEL_FORMAT_L_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca015155116919cac3eff289764e9574d8)、[PIXEL_FORMAT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca5c905dcfaca35e58c14513f2e3a61091)。

显示像素格式（Display Pixel Formats）。

<a id="r_ga23030b6c27446c4579103fe38e821341"></a>

```c
enum display_screen_info { SCREEN_INFO_MONO_VTILED = BIT(0) , SCREEN_INFO_MONO_MSB_FIRST = BIT(1) , SCREEN_INFO_EPD = BIT(2) , SCREEN_INFO_DOUBLE_BUFFER = BIT(3) , SCREEN_INFO_X_ALIGNMENT_WIDTH = BIT(4) }
```

相关声明：[display_screen_info](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga23030b6c27446c4579103fe38e821341)、[SCREEN_INFO_MONO_VTILED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804)、[SCREEN_INFO_MONO_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d)、[SCREEN_INFO_EPD](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85)、[SCREEN_INFO_DOUBLE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842)、[SCREEN_INFO_X_ALIGNMENT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1)。

显示屏幕信息（Display Screen Information）。

<a id="r_gac59b091a3ed39431ab97a5f19fdc4855"></a>

```c
enum display_orientation { DISPLAY_ORIENTATION_NORMAL , DISPLAY_ORIENTATION_ROTATED_90 , DISPLAY_ORIENTATION_ROTATED_180 , DISPLAY_ORIENTATION_ROTATED_270 }
```

相关声明：[display_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac59b091a3ed39431ab97a5f19fdc4855)、[DISPLAY_ORIENTATION_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2)、[DISPLAY_ORIENTATION_ROTATED_90](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc)、[DISPLAY_ORIENTATION_ROTATED_180](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29)、[DISPLAY_ORIENTATION_ROTATED_270](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4)。

列出可用显示方向（Display Orientation）的枚举。

<a id="r_ga0042f460c729a5b11ed59f4aac609212"></a>

```c
enum display_event { DISPLAY_EVENT_LINE_INT = BIT(0) , DISPLAY_EVENT_VSYNC = BIT(1) , DISPLAY_EVENT_FRAME_DONE = BIT(2) , DISPLAY_EVENT_FIFO_UNDERFLOW = BIT(3) }
```

相关声明：[display_event](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga0042f460c729a5b11ed59f4aac609212)、[DISPLAY_EVENT_LINE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a4aecf6d165ca2ec432297cc5664c24a6)、[DISPLAY_EVENT_VSYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212acb5772017ec3e4d6677fee78295a379c)、[DISPLAY_EVENT_FRAME_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212abd4e3c24f05c2484137855349d6cf794)、[DISPLAY_EVENT_FIFO_UNDERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a456bc992ffdf5604828b7280f94dd649)。

显示事件类型（Display Event Types）。

<a id="r_ga5c3bcf15b62c66c1677e51a10451efe5"></a>

```c
enum display_event_result { DISPLAY_EVENT_RESULT_CONTINUE = 0 , DISPLAY_EVENT_RESULT_HANDLED = 1 }
```

相关声明：[display_event_result](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga5c3bcf15b62c66c1677e51a10451efe5)、[DISPLAY_EVENT_RESULT_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5abc630229e82e4e5d7ef50ec4c8e6aff7)、[DISPLAY_EVENT_RESULT_HANDLED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5ad79be33d4e885b6745feebebc3636dfc)。

显示事件回调返回标志（Display Event Callback Return Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga3a5114b4537039fc4d3258678b82cd18"></a>

```c
static int display_write (const struct device *dev, const uint16_t x, const uint16_t y, const struct display_buffer_descriptor *desc, const void *buf)
```

相关声明：[display_write](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3a5114b4537039fc4d3258678b82cd18)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

向显示器（Display）写入数据。

<a id="r_ga3f497776520b0eac16b8aea80ccbbcfc"></a>

```c
static int display_read (const struct device *dev, const uint16_t x, const uint16_t y, const struct display_buffer_descriptor *desc, void *buf)
```

相关声明：[display_read](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3f497776520b0eac16b8aea80ccbbcfc)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

从显示器（Display）读取数据。

<a id="r_ga62a6cd9e338aa07f789de60e64d3b3c4"></a>

```c
static int display_clear (const struct device *dev)
```

相关声明：[display_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga62a6cd9e338aa07f789de60e64d3b3c4)、[device](../device_reference/P002_设备对象结构.md)。

清空显示设备的屏幕（Clear Screen）。

<a id="r_ga4b66d380e46909caaa7317857f84a9e8"></a>

```c
static void * display_get_framebuffer (const struct device *dev)
```

相关声明：[display_get_framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4b66d380e46909caaa7317857f84a9e8)、[device](../device_reference/P002_设备对象结构.md)。

获取帧缓冲区（Framebuffer）指针以供直接访问。

<a id="r_gac6ad1f33067165e4c3bf7c0c345bb4e4"></a>

```c
static int display_blanking_on (const struct device *dev)
```

相关声明：[display_blanking_on](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac6ad1f33067165e4c3bf7c0c345bb4e4)、[device](../device_reference/P002_设备对象结构.md)。

开启显示消隐（Display Blanking）。

<a id="r_ga4d9e288891a6bde679c3aa00b9913e1d"></a>

```c
static int display_blanking_off (const struct device *dev)
```

相关声明：[display_blanking_off](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4d9e288891a6bde679c3aa00b9913e1d)、[device](../device_reference/P002_设备对象结构.md)。

关闭显示消隐（Display Blanking）。

<a id="r_gad5cdeb245d17c8d680a5843b3cce1f8c"></a>

```c
static int display_set_brightness (const struct device *dev, uint8_t brightness)
```

相关声明：[display_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gad5cdeb245d17c8d680a5843b3cce1f8c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器亮度（Brightness）。

<a id="r_ga855c72f72238b25f23e95e50546e2f27"></a>

```c
static int display_set_contrast (const struct device *dev, uint8_t contrast)
```

相关声明：[display_set_contrast](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga855c72f72238b25f23e95e50546e2f27)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置显示器对比度（Contrast）。

<a id="r_ga6a13e42773be13b141ebd8f047f8db50"></a>

```c
static void display_get_capabilities (const struct device *dev, struct display_capabilities *capabilities)
```

相关声明：[display_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga6a13e42773be13b141ebd8f047f8db50)、[device](../device_reference/P002_设备对象结构.md)、[display_capabilities](../hardware/P216_显示能力结构.md)。

获取显示能力（Display Capabilities）。

<a id="r_ga7ede828663090760c2558a231d9f2150"></a>

```c
static int display_set_pixel_format (const struct device *dev, const enum display_pixel_format pixel_format)
```

相关声明：[display_set_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga7ede828663090760c2558a231d9f2150)、[device](../device_reference/P002_设备对象结构.md)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

设置显示器所用像素格式（Pixel Format）。

<a id="r_ga4e0a4dc2e434144874af014b8e7c4394"></a>

```c
static int display_set_orientation (const struct device *dev, const enum display_orientation orientation)
```

相关声明：[display_set_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4e0a4dc2e434144874af014b8e7c4394)、[device](../device_reference/P002_设备对象结构.md)、[display_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac59b091a3ed39431ab97a5f19fdc4855)。

设置显示方向（Display Orientation）。

<a id="r_ga99b7e7da6b85bee97398a8a9b161c777"></a>

```c
static int display_register_event_cb (const struct device *dev, display_event_cb_t cb, void *user_data, uint32_t event_mask, bool in_isr, uint32_t *out_reg_handle)
```

相关声明：[display_register_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga99b7e7da6b85bee97398a8a9b161c777)、[device](../device_reference/P002_设备对象结构.md)、[display_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gadca2fe10ecb27b5e82309bbab5e886ee)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为显示设备注册事件回调（Event Callback）。

<a id="r_gaa4e433439206bc426db363c64882a395"></a>

```c
static int display_unregister_event_cb (const struct device *dev, uint32_t reg_handle)
```

相关声明：[display_unregister_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gaa4e433439206bc426db363c64882a395)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

注销显示设备的事件回调（Event Callback）。


## 6.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/dt-bindings/display/panel.h](../api_source_reference/P642_panel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [display_palette_color](../hardware/P218_显示调色板颜色.md)
- [display_capabilities](../hardware/P216_显示能力结构.md)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [display_event_data](../hardware/P217_显示事件数据.md)
- [display_driver_api](../hardware/P220_显示驱动函数表.md)
- [DISPLAY_BITS_PER_PIXEL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3b305be04da5921ca4087498627dc061)
- [display_event_result](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga5c3bcf15b62c66c1677e51a10451efe5)
- [display_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gadca2fe10ecb27b5e82309bbab5e886ee)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [display_register_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga99b7e7da6b85bee97398a8a9b161c777)
- [display_blanking_on_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gacf66a054396ccd8e178591b8fc98ff4d)
- [display_blanking_off_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gab23bbd9305792d6e37d2e4ff91a2b175)
- [display_write_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga5cab904b24062fdea531f450a8e5c367)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [display_read_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga9ed51d3f666f747d9fb7f1f7746611b3)
- [display_clear_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaf42820ae69452788bf51f37512ca8586)
- [display_get_framebuffer_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6dd281032ad400d3adc7f5f812c5fe12)
- [display_set_brightness_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [display_set_contrast_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadf115352908f94b0a0bf225dbdd8ee85)
- [display_get_capabilities_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga474f85a33aef019dddb1c720ea23f3fb)
- [display_set_pixel_format_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga2637286cf3a97c2b532bb33f22263303)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [display_set_orientation_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaff3b76a6601cf176782be940139ccb48)
- [display_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac59b091a3ed39431ab97a5f19fdc4855)
- [display_register_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gac0a36d044e4663ab5ee61d1e11d645d0)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [display_unregister_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadd468c71193663072489f32885bc30e5)
- [PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)
- [PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)
- [PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)
- [PIXEL_FORMAT_ARGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)
- [PIXEL_FORMAT_RGB_565](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)
- [PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)
- [PIXEL_FORMAT_L_8](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df)
- [PIXEL_FORMAT_AL_88](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca92f4901daf73e26c4290e656e7afeb2f)
- [PIXEL_FORMAT_XRGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca20bb97558d4acdf225a157c40d9058ab)
- [PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172)
- [PIXEL_FORMAT_ABGR_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca049f2930dfd1efadfb17a113ba0d879d)
- [PIXEL_FORMAT_RGBA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca9de42e120e50119c2df1c503ed2e7a28)
- [PIXEL_FORMAT_BGRA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca142784152249100847b0e5c6d656191c)
- [PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a)
- [PIXEL_FORMAT_L_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca015155116919cac3eff289764e9574d8)
- [PIXEL_FORMAT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca5c905dcfaca35e58c14513f2e3a61091)
- [display_screen_info](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga23030b6c27446c4579103fe38e821341)
- [SCREEN_INFO_MONO_VTILED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804)
- [SCREEN_INFO_MONO_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d)
- [SCREEN_INFO_EPD](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85)
- [SCREEN_INFO_DOUBLE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842)
- [SCREEN_INFO_X_ALIGNMENT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1)
- [DISPLAY_ORIENTATION_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2)
- [DISPLAY_ORIENTATION_ROTATED_90](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc)
- [DISPLAY_ORIENTATION_ROTATED_180](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29)
- [DISPLAY_ORIENTATION_ROTATED_270](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4)
- [display_event](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga0042f460c729a5b11ed59f4aac609212)
- [DISPLAY_EVENT_LINE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a4aecf6d165ca2ec432297cc5664c24a6)
- [DISPLAY_EVENT_VSYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212acb5772017ec3e4d6677fee78295a379c)
- [DISPLAY_EVENT_FRAME_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212abd4e3c24f05c2484137855349d6cf794)
- [DISPLAY_EVENT_FIFO_UNDERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a456bc992ffdf5604828b7280f94dd649)
- [DISPLAY_EVENT_RESULT_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5abc630229e82e4e5d7ef50ec4c8e6aff7)
- [DISPLAY_EVENT_RESULT_HANDLED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5ad79be33d4e885b6745feebebc3636dfc)
- [display_write](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3a5114b4537039fc4d3258678b82cd18)
- [display_read](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3f497776520b0eac16b8aea80ccbbcfc)
- [display_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga62a6cd9e338aa07f789de60e64d3b3c4)
- [display_get_framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4b66d380e46909caaa7317857f84a9e8)
- [display_blanking_on](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac6ad1f33067165e4c3bf7c0c345bb4e4)
- [display_blanking_off](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4d9e288891a6bde679c3aa00b9913e1d)
- [display_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gad5cdeb245d17c8d680a5843b3cce1f8c)
- [display_set_contrast](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga855c72f72238b25f23e95e50546e2f27)
- [display_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga6a13e42773be13b141ebd8f047f8db50)
- [display_set_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga7ede828663090760c2558a231d9f2150)
- [display_set_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4e0a4dc2e434144874af014b8e7c4394)
- [display_unregister_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gaa4e433439206bc426db363c64882a395)

<a id="header-details"></a>

---

[上一章](P005_zephyr__bluetooth__audio__csip.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__sensor__max30009.h_文件参考.md)
