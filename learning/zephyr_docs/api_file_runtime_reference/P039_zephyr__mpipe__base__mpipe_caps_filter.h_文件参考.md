---
id: learning.zephyr-docs.api-file-runtime-reference.page-39
title: zephyr__mpipe__base__mpipe_caps_filter.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_mpipe\_\_base\_\_mpipe\_caps\_filter.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

能力过滤元素（Caps Filter Element）。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_transform.h>
```

查看此文件的源码。

能力过滤元素（Caps Filter Element）。此元素不修改数据，而是约束在其链接（Link）上协商的格式（Negotiated Format）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 39.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fcaps_5Ffilter"></a>

```c
struct mpipe_caps_filter
```

相关声明：[mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)。

能力过滤元素（Caps Filter Element）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 39.2\_枚举（Enumerations）

<a id="r_ga7ba4b02da65b2fdc12c901779577e2c1"></a>

```c
enum { MPIPE_PROP_BASE_CAPS_FILTER_CAPS = MPIPE_PROP_TRANSFORM_LAST }
```

相关声明：[MPIPE_PROP_BASE_CAPS_FILTER_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597)。

能力过滤器属性标识（Caps Filter Property Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.3\_函数（Functions）

<a id="r_gaabd0709b12a0b2528c41da650414d88f"></a>

```c
int mpipe_caps_filter_init (struct mpipe_caps_filter *caps_filter, uint8_t id)
```

相关声明：[mpipe_caps_filter_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gaabd0709b12a0b2528c41da650414d88f)、[mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化能力过滤元素（Caps Filter Element）。


## 39.4\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_transform.h](../api_source_reference/P562_mpipe_transform.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P547_mpipe_caps_filter.h_源码浏览.md)
- [mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)
- [MPIPE_PROP_BASE_CAPS_FILTER_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597)
- [mpipe_caps_filter_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gaabd0709b12a0b2528c41da650414d88f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P038_zephyr__dt-bindings__gpio__microchip-xec-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__mpipe__mpipe_parser.h_文件参考.md)
