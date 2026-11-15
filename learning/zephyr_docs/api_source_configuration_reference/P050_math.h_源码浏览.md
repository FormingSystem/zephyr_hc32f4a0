---
id: learning.zephyr-docs.api-source-configuration-reference.page-50
title: math.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/math_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_math.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/math_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html)。

## 50.1\_原始可见代码（Source Code）

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
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="amath_8h_html_a3ded656bbe9849ad9fa2b28530390f0a"></a>
<a id="amath_8h_html_a769abd043ac3336a53318e327f2137c2"></a>
<a id="amath_8h_html_ac340fde9f4743ef7a9398b79d7bea8bd"></a>
<a id="amath_8h_html_ae0617f6dc83a7c2767e0766f5b3df203"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_MATH_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_MATH_H_

#ifdef __cplusplus
extern "C" {
#endif

#if !defined(FLT_EVAL_METHOD) && defined(__FLT_EVAL_METHOD__)
#define FLT_EVAL_METHOD __FLT_EVAL_METHOD__
#endif

#if defined FLT_EVAL_METHOD
        #if FLT_EVAL_METHOD == 0
                typedef float  float_t;
                typedef double double_t;
        #elif FLT_EVAL_METHOD == 1
                typedef double float_t;
                typedef double double_t;
        #elif FLT_EVAL_METHOD == 2
                typedef long double float_t;
                typedef long double double_t;
        #else
                /* Implementation-defined.  Assume float_t and double_t have
                 * already been defined */
        #endif
#else
        typedef float  float_t;
        typedef double double_t;
#endif

/* Useful constants.  */
#define MAXFLOAT    3.40282347e+38F

#define M_E         2.7182818284590452354
#define M_LOG2E     1.4426950408889634074
#define M_LOG10E    0.43429448190325182765
#define M_LN2       0.693147180559945309417
#define M_LN10      2.30258509299404568402
#define M_PI        3.14159265358979323846
#define M_PI_2      1.57079632679489661923
#define M_PI_4      0.78539816339744830962
#define M_1_PI      0.31830988618379067154
#define M_2_PI      0.63661977236758134308
#define M_2_SQRTPI  1.12837916709551257390
#define M_SQRT2     1.41421356237309504880
#define M_SQRT1_2   0.70710678118654752440

float sqrtf(float square);
double sqrt(double square);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_MATH_H_ */
```

## 50.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

由实现定义（Implementation-defined）。假定 `float_t` 和 `double_t` 已经定义。

### 注释 3：原第 37 行

实用常量（Useful constants）。

### 注释 4：原第 61 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_MATH_H_`。

## 50.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html)
- [float_t](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html#a3ded656bbe9849ad9fa2b28530390f0a)
- [double_t](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html#ac340fde9f4743ef7a9398b79d7bea8bd)
- [sqrtf](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html#a769abd043ac3336a53318e327f2137c2)
- [sqrt](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html#ae0617f6dc83a7c2767e0766f5b3df203)

---

[上一章](P049_lwm2m_path.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P051_max32-pinctrl.h_源码浏览.md)
