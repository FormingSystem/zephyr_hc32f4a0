---
id: learning.zephyr-docs.api-source-reference.page-187
title: dsp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_dsp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)。

## 187.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
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
<a id="abasicmath_8h_html"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="aprint__format_8h_html"></a>

```c
/* Copyright (c) 2022 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DSP_DSP_H_
#define ZEPHYR_INCLUDE_DSP_DSP_H_

#ifdef CONFIG_DSP_BACKEND_HAS_STATIC
#define DSP_FUNC_SCOPE static
#else
#define DSP_FUNC_SCOPE
#endif

#ifdef CONFIG_DSP_BACKEND_HAS_AGU
#define DSP_DATA __agu
#else
#define DSP_DATA
#endif

#ifdef CONFIG_DSP_BACKEND_HAS_XDATA_SECTION
#define DSP_STATIC_DATA DSP_DATA __attribute__((section(".Xdata")))
#else
#define DSP_STATIC_DATA DSP_DATA
#endif


#include <zephyr/dsp/types.h>

#include <zephyr/dsp/basicmath.h>

#include <zephyr/dsp/print_format.h>

#include "zdsp_backend.h"

#endif /* ZEPHYR_INCLUDE_DSP_DSP_H_ */
```

## 187.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_DSP_H_`。

## 187.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)
- [zephyr/dsp/print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)

---

[上一章](P186_utils.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P188_acpi.h_源码浏览.md)
