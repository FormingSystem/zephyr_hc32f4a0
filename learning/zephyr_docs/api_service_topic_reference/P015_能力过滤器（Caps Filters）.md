---
id: learning.zephyr-docs.api-service-topic-reference.page-15
title: 能力过滤器（Caps Filters）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_能力过滤器（Caps Filters）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对协商得到的能力施加约束的变换元素。

<a id="details"></a>

对协商得到的能力施加约束的变换元素。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_mpipe_5Fcaps_5Ffilter_2Eh"></a>

```c
file mpipe_caps_filter.h
```

相关声明：[mpipe_caps_filter.h](../api_file_runtime_reference/P039_zephyr__mpipe__base__mpipe_caps_filter.h_文件参考.md)。

能力过滤元素（Caps Filter Element）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fcaps_5Ffilter"></a>

```c
struct mpipe_caps_filter
```

相关声明：[mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)。

能力过滤元素（Caps Filter Element）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.3\_枚举（Enumerations）

<a id="r_ga7ba4b02da65b2fdc12c901779577e2c1"></a>

```c
enum { MPIPE_PROP_BASE_CAPS_FILTER_CAPS = MPIPE_PROP_TRANSFORM_LAST }
```

相关声明：[MPIPE_PROP_BASE_CAPS_FILTER_CAPS](#gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597)。

能力过滤器属性标识（Caps Filter Property Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.4\_函数（Functions）

<a id="r_gaabd0709b12a0b2528c41da650414d88f"></a>

```c
int mpipe_caps_filter_init (struct mpipe_caps_filter *caps_filter, uint8_t id)
```

相关声明：[mpipe_caps_filter_init](#gaabd0709b12a0b2528c41da650414d88f)、[mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化能力过滤元素（Caps Filter Element）。

## 15.5\_详细说明（Detailed Documentation）

<a id="ga7ba4b02da65b2fdc12c901779577e2c1"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/mpipe/base/mpipe_caps_filter.h>
```

能力过滤器属性标识（Caps Filter Property Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_BASE_CAPS_FILTER_CAPS` | 能力标识属性（Caps ID Property）。 |

<a id="gaabd0709b12a0b2528c41da650414d88f"></a>

### `mpipe_caps_filter_init()`

```c
int mpipe_caps_filter_init ( struct mpipe_caps_filter * caps_filter, uint8_t id )
```

```c
#include <zephyr/mpipe/base/mpipe_caps_filter.h>
```

初始化能力过滤元素（Caps Filter Element）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `caps_filter` | 指向待初始化元素（Element）的指针（Pointer）。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 15.6\_原页交叉引用（Cross References）

- [mpipe_caps_filter.h](../api_file_runtime_reference/P039_zephyr__mpipe__base__mpipe_caps_filter.h_文件参考.md)
- [mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_统计信息管理（Statistics Management）.md) · [返回大纲](大纲.md) · [下一章](P016_OTP 驱动后端 API.md)
