---
id: learning.zephyr-docs.api-source-reference.page-670
title: print_format.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第670章\_print\_format.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)。

## 670.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="ainttypes_8h_html"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdlib_8h_html"></a>
<a id="astdlib_8h_html_a5613b9b7ce990f94ceaaf1f455cc98e6"></a>

```c
/* Copyright (c) 2023 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DSP_PRINT_FORMAT_H_
#define ZEPHYR_INCLUDE_DSP_PRINT_FORMAT_H_

#include <inttypes.h>
#include <stdlib.h>
#include <zephyr/dsp/types.h>


#define PRIq(precision) "s%" PRIu32 ".%0" STRINGIFY(precision) PRIu32

static inline int64_t ___PRIq_arg_shift(int64_t q, int shift)
{
        if (shift < 0) {
                return llabs(q) >> -shift;
        } else {
                return llabs(q) << shift;
        }
}

#define __EXP2(a, b) a ## b
#define __EXP(a, b) __EXP2(a ## e, b)
#define __CONSTPOW(C, x) __EXP(C, x)

#define __PRIq_arg_shift(q, shift)     ___PRIq_arg_shift(q, ((shift) + (8 * (4 - (int)sizeof(q)))))
#define __PRIq_arg_get(q, shift, h, l) FIELD_GET(GENMASK64(h, l), __PRIq_arg_shift(q, shift))
#define __PRIq_arg_get_int(q, shift)   __PRIq_arg_get(q, shift, 63, 31)
#define __PRIq_arg_get_frac(q, precision, shift)                                                   \
        ((__PRIq_arg_get(q, shift, 30, 0) * __CONSTPOW(1, precision)) / INT32_MAX)

#define PRIq_arg(q, precision, shift)                                                              \
        ((q) < 0 ? "-" : ""), (uint32_t)__PRIq_arg_get_int(q, shift),                              \
                (uint32_t)__PRIq_arg_get_frac(q, precision, shift)


#endif /* ZEPHYR_INCLUDE_DSP_PRINT_FORMAT_H_ */
```

## 670.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_PRINT_FORMAT_H_`。

## 670.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [stdlib.h](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [llabs](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a5613b9b7ce990f94ceaaf1f455cc98e6)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)

---

[上一章](P669_power.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P671_printk-hooks.h_源码浏览.md)
