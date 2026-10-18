---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-9
title: 数字信号处理（Digital Signal Processing，DSP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_数字信号处理（Digital Signal Processing，DSP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字信号处理（DSP）数学函数和工具。

<a id="details"></a>

数字信号处理（Digital Signal Processing，DSP）数学函数和工具。自 Zephyr 3.3 起提供；API 版本为 0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 9.1\_主题（Topics）

<a id="r_math_5Fdsp_5Fbasic"></a>

相关声明：[基本数学函数（Basic Math Functions）](../api_topic_reference/P045_基本数学函数（Basic Math Functions）.md)。

用于 DSP 的基本逐元素数学运算。

<a id="r_math_5Fdsp_5Futils_5Fshifts"></a>

相关声明：[浮点/定点移位转换函数（Float/Fixed point shift conversion functions）](../api_topic_reference/P046_浮点_定点移位转换函数（Float_Fixed point shift conversion functions）.md)。

在 Float 或 Double 表示与 Q31/Q15/Q7 表示之间双向转换数值。

<a id="r_math_5Fprinting"></a>

相关声明：[用于打印 Q 格式数值的辅助宏。](../api_service_topic_reference/P012_用于打印 Q 格式数值的辅助宏。.md)。

扩展现有的 `inttypes` 头文件，以支持打印格式化。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_gae541b6f232c305361e9b416fc9eed263"></a>

```c
typedef int8_t q7_t
```

相关声明：[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q7_t](#gae541b6f232c305361e9b416fc9eed263)。

采用 1.7 格式的 8 位小数数据类型（fractional data type）。

<a id="r_gab5a8fb21a5b3b983d5f54f31614052ea"></a>

```c
typedef int16_t q15_t
```

相关声明：[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[q15_t](#gab5a8fb21a5b3b983d5f54f31614052ea)。

采用 1.15 格式的 16 位小数数据类型。

<a id="r_gadc89a3547f5324b7b3b95adec3806bc0"></a>

```c
typedef int32_t q31_t
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[q31_t](#gadc89a3547f5324b7b3b95adec3806bc0)。

采用 1.31 格式的 32 位小数数据类型。

<a id="r_ga5aea1cb12fc02d9d44c8abf217eaa5c6"></a>

```c
typedef int64_t q63_t
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[q63_t](#ga5aea1cb12fc02d9d44c8abf217eaa5c6)。

采用 1.63 格式的 64 位小数数据类型。

<a id="r_gaa94dc44bddb5718a22bb612890a7fe9f"></a>

```c
typedef __fp16 float16_t
```

相关声明：[float16_t](#gaa94dc44bddb5718a22bb612890a7fe9f)。

16 位浮点类型（floating-point type）定义。

<a id="r_ga4611b605e45ab401f02cab15c5e38715"></a>

```c
typedef float float32_t
```

相关声明：[float32_t](#ga4611b605e45ab401f02cab15c5e38715)。

32 位浮点类型定义。

<a id="r_gac55f3ae81b5bc9053760baacf57e47f4"></a>

```c
typedef double float64_t
```

相关声明：[float64_t](#gac55f3ae81b5bc9053760baacf57e47f4)。

64 位浮点类型定义。

## 9.3\_详细说明（Detailed Documentation）

<a id="gaa94dc44bddb5718a22bb612890a7fe9f"></a>

### `float16_t`

```c
typedef __fp16 float16_t
```

```c
#include <zephyr/dsp/types.h>
```

16 位浮点类型（floating-point type）定义。

<a id="ga4611b605e45ab401f02cab15c5e38715"></a>

### `float32_t`

```c
typedef float float32_t
```

```c
#include <zephyr/dsp/types.h>
```

32 位浮点类型定义。

<a id="gac55f3ae81b5bc9053760baacf57e47f4"></a>

### `float64_t`

```c
typedef double float64_t
```

```c
#include <zephyr/dsp/types.h>
```

64 位浮点类型定义。

<a id="gab5a8fb21a5b3b983d5f54f31614052ea"></a>

### `q15_t`

```c
typedef int16_t q15_t
```

```c
#include <zephyr/dsp/types.h>
```

采用 1.15 格式的 16 位小数数据类型。

<a id="gadc89a3547f5324b7b3b95adec3806bc0"></a>

### `q31_t`

```c
typedef int32_t q31_t
```

```c
#include <zephyr/dsp/types.h>
```

采用 1.31 格式的 32 位小数数据类型。

<a id="ga5aea1cb12fc02d9d44c8abf217eaa5c6"></a>

### `q63_t`

```c
typedef int64_t q63_t
```

```c
#include <zephyr/dsp/types.h>
```

采用 1.63 格式的 64 位小数数据类型。

<a id="gae541b6f232c305361e9b416fc9eed263"></a>

### `q7_t`

```c
typedef int8_t q7_t
```

```c
#include <zephyr/dsp/types.h>
```

采用 1.7 格式的 8 位小数数据类型（fractional data type）。


## 9.4\_原页交叉引用（Cross References）

- [基本数学函数（Basic Math Functions）](../api_topic_reference/P045_基本数学函数（Basic Math Functions）.md)
- [浮点/定点移位转换函数（Float/Fixed point shift conversion functions）](../api_topic_reference/P046_浮点_定点移位转换函数（Float_Fixed point shift conversion functions）.md)
- [用于打印 Q 格式数值的辅助宏。](../api_service_topic_reference/P012_用于打印 Q 格式数值的辅助宏。.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P008_AHB3RSTCR 复位控制（Reset Control）.md) · [返回大纲](大纲.md) · [下一章](P010_向量限幅（Vector Clipping）.md)
