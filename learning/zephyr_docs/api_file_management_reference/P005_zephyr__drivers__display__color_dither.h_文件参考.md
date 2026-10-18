---
id: learning.zephyr-docs.api-file-management-reference.page-5
title: zephyr__drivers__display__color_dither.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_display\_\_color\_dither.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/color__dither_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

显示驱动（Display Drivers）的颜色抖动辅助接口。

<a id="details"></a>

```c
#include <zephyr/drivers/display.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

显示驱动（Display Drivers）的颜色抖动辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_display_5Fcolor_5Fdither_5Fstate"></a>

```c
struct display_color_dither_state
```

相关声明：[display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)。

单个显示设备实例的颜色抖动辅助程序（Color Dithering Helper）所拥有的运行时状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_gaa5614d4a4e791b87d1a925964c3a862d"></a>

```c
#define DISPLAY_COLOR_DITHER_DEFINE(inst)
```

相关声明：[DISPLAY_COLOR_DITHER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gaa5614d4a4e791b87d1a925964c3a862d)。

为一个显示驱动实例定义颜色抖动（color dithering）所需的底层存储。

<a id="r_gab7a067eae6c3fde92740be190c11d62e"></a>

```c
#define DISPLAY_COLOR_DITHER_INIT(inst)
```

相关声明：[DISPLAY_COLOR_DITHER_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gab7a067eae6c3fde92740be190c11d62e)。

为一个显示驱动实例初始化驱动的 `display_color_dither_state` 成员。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_gab765e6926c9f1f1f693c5016bce04efc"></a>

```c
int display_color_dither_prepare (const struct device *dev, struct display_color_dither_state *state, const struct display_buffer_descriptor **desc, const void **buf, struct display_buffer_descriptor *scratch)
```

相关声明：[display_color_dither_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gab765e6926c9f1f1f693c5016bce04efc)、[device](../device_reference/P002_设备对象结构.md)、[display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

为原生 `PIXEL_FORMAT_I_4` 路径准备写缓冲区。

<a id="r_gaad0ed338c68320c61543c2986e3f7a0a"></a>

```c
void display_color_dither_patch_caps (struct display_color_dither_state *state, struct display_capabilities *caps)
```

相关声明：[display_color_dither_patch_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gaad0ed338c68320c61543c2986e3f7a0a)、[display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[display_capabilities](../hardware/P216_显示能力结构.md)。

将辅助模块管理的 RGB 格式添加到显示能力（display capabilities）中。

<a id="r_ga38578e4fd14280d9e623172b2bfabd15"></a>

```c
int display_color_dither_set_input_format (struct display_color_dither_state *state, enum display_pixel_format pf)
```

相关声明：[display_color_dither_set_input_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga38578e4fd14280d9e623172b2bfabd15)、[display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

选择辅助模块的输入像素格式（input pixel format）。

<a id="r_ga79ff5454e68af2c1bb5eedf25904dca2"></a>

```c
bool display_color_dither_is_active (const struct display_color_dither_state *state, enum display_pixel_format current_pixel_format)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[display_color_dither_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga79ff5454e68af2c1bb5eedf25904dca2)、[display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)。

报告辅助模块当前是否正在将输入转换为原生 I_4 格式。


## 5.4\_原页交叉引用（Cross References）

- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_device_reference/P005_color_dither.h_源码浏览.md)
- [display_color_dither_state](../hardware/P222_显示颜色抖动状态.md)
- [DISPLAY_COLOR_DITHER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gaa5614d4a4e791b87d1a925964c3a862d)
- [DISPLAY_COLOR_DITHER_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gab7a067eae6c3fde92740be190c11d62e)
- [display_color_dither_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gab765e6926c9f1f1f693c5016bce04efc)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a)
- [display_color_dither_patch_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#gaad0ed338c68320c61543c2986e3f7a0a)
- [display_capabilities](../hardware/P216_显示能力结构.md)
- [display_color_dither_set_input_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga38578e4fd14280d9e623172b2bfabd15)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [display_color_dither_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__display__color__dither.html#ga79ff5454e68af2c1bb5eedf25904dca2)

<a id="header-details"></a>

---

[上一章](P004_zephyr__net__prometheus__collector.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__net__conn_mgr_monitor.h_文件参考.md)
