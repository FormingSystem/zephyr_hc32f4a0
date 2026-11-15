---
id: learning.zephyr-docs.api-file-reference.page-196
title: ____w__zephyr__zephyr__lib__libc__minimal__include__math.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第196章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_math.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/math_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 196.1\_宏定义（Macros）

<a id="r_a5e9e29217f6ec61105a4520ec5942225"></a>

```c
#define MAXFLOAT 3.40282347e+38F
```

相关声明：[MAXFLOAT](#a5e9e29217f6ec61105a4520ec5942225)。

<a id="r_a9bf5d952c5c93c70f9e66c9794d406c9"></a>

```c
#define M_E 2.7182818284590452354
```

相关声明：[M_E](#a9bf5d952c5c93c70f9e66c9794d406c9)。

<a id="r_ac5c747ee5bcbe892875672a0b9d8171c"></a>

```c
#define M_LOG2E 1.4426950408889634074
```

相关声明：[M_LOG2E](#ac5c747ee5bcbe892875672a0b9d8171c)。

<a id="r_a9ed2b5582226f3896424ff6d2a3ebb14"></a>

```c
#define M_LOG10E 0.43429448190325182765
```

相关声明：[M_LOG10E](#a9ed2b5582226f3896424ff6d2a3ebb14)。

<a id="r_a92428112a5d24721208748774a4f23e6"></a>

```c
#define M_LN2 0.693147180559945309417
```

相关声明：[M_LN2](#a92428112a5d24721208748774a4f23e6)。

<a id="r_a0a53871497a155afe91424c28a8ec3c4"></a>

```c
#define M_LN10 2.30258509299404568402
```

相关声明：[M_LN10](#a0a53871497a155afe91424c28a8ec3c4)。

<a id="r_ae71449b1cc6e6250b91f539153a7a0d3"></a>

```c
#define M_PI 3.14159265358979323846
```

相关声明：[M_PI](#ae71449b1cc6e6250b91f539153a7a0d3)。

<a id="r_a958e4508ed28ee5cc04249144312c15f"></a>

```c
#define M_PI_2 1.57079632679489661923
```

相关声明：[M_PI_2](#a958e4508ed28ee5cc04249144312c15f)。

<a id="r_aeb24420b096a677f3a2dc5a72b36bf22"></a>

```c
#define M_PI_4 0.78539816339744830962
```

相关声明：[M_PI_4](#aeb24420b096a677f3a2dc5a72b36bf22)。

<a id="r_a08dfac3cca9601a02fc88356cc078e1d"></a>

```c
#define M_1_PI 0.31830988618379067154
```

相关声明：[M_1_PI](#a08dfac3cca9601a02fc88356cc078e1d)。

<a id="r_a97f6d6514d3d3dd50c3a2a6d622673db"></a>

```c
#define M_2_PI 0.63661977236758134308
```

相关声明：[M_2_PI](#a97f6d6514d3d3dd50c3a2a6d622673db)。

<a id="r_a631ff334c4a1a6db2e8a7ff4acbe48a5"></a>

```c
#define M_2_SQRTPI 1.12837916709551257390
```

相关声明：[M_2_SQRTPI](#a631ff334c4a1a6db2e8a7ff4acbe48a5)。

<a id="r_a66b3ab30f1332874326ed93969e496e0"></a>

```c
#define M_SQRT2 1.41421356237309504880
```

相关声明：[M_SQRT2](#a66b3ab30f1332874326ed93969e496e0)。

<a id="r_acdbb2c2f9429f08916f03c8786d2d2d7"></a>

```c
#define M_SQRT1_2 0.70710678118654752440
```

相关声明：[M_SQRT1_2](#acdbb2c2f9429f08916f03c8786d2d2d7)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 196.2\_类型定义（Typedefs）

<a id="r_a3ded656bbe9849ad9fa2b28530390f0a"></a>

```c
typedef float float_t
```

相关声明：[float_t](#a3ded656bbe9849ad9fa2b28530390f0a)。

<a id="r_ac340fde9f4743ef7a9398b79d7bea8bd"></a>

```c
typedef double double_t
```

相关声明：[double_t](#ac340fde9f4743ef7a9398b79d7bea8bd)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 196.3\_函数（Functions）

<a id="r_a769abd043ac3336a53318e327f2137c2"></a>

```c
float sqrtf (float square)
```

相关声明：[sqrtf](#a769abd043ac3336a53318e327f2137c2)。

<a id="r_ae0617f6dc83a7c2767e0766f5b3df203"></a>

```c
double sqrt (double square)
```

相关声明：[sqrt](#ae0617f6dc83a7c2767e0766f5b3df203)。

## 196.4\_详细说明（Detailed Documentation）

<a id="a08dfac3cca9601a02fc88356cc078e1d"></a>

### `M_1_PI`

```c
#define M_1_PI 0.31830988618379067154
```

<a id="a97f6d6514d3d3dd50c3a2a6d622673db"></a>

### `M_2_PI`

```c
#define M_2_PI 0.63661977236758134308
```

<a id="a631ff334c4a1a6db2e8a7ff4acbe48a5"></a>

### `M_2_SQRTPI`

```c
#define M_2_SQRTPI 1.12837916709551257390
```

<a id="a9bf5d952c5c93c70f9e66c9794d406c9"></a>

### `M_E`

```c
#define M_E 2.7182818284590452354
```

<a id="a0a53871497a155afe91424c28a8ec3c4"></a>

### `M_LN10`

```c
#define M_LN10 2.30258509299404568402
```

<a id="a92428112a5d24721208748774a4f23e6"></a>

### `M_LN2`

```c
#define M_LN2 0.693147180559945309417
```

<a id="a9ed2b5582226f3896424ff6d2a3ebb14"></a>

### `M_LOG10E`

```c
#define M_LOG10E 0.43429448190325182765
```

<a id="ac5c747ee5bcbe892875672a0b9d8171c"></a>

### `M_LOG2E`

```c
#define M_LOG2E 1.4426950408889634074
```

<a id="ae71449b1cc6e6250b91f539153a7a0d3"></a>

### `M_PI`

```c
#define M_PI 3.14159265358979323846
```

<a id="a958e4508ed28ee5cc04249144312c15f"></a>

### `M_PI_2`

```c
#define M_PI_2 1.57079632679489661923
```

<a id="aeb24420b096a677f3a2dc5a72b36bf22"></a>

### `M_PI_4`

```c
#define M_PI_4 0.78539816339744830962
```

<a id="acdbb2c2f9429f08916f03c8786d2d2d7"></a>

### `M_SQRT1_2`

```c
#define M_SQRT1_2 0.70710678118654752440
```

<a id="a66b3ab30f1332874326ed93969e496e0"></a>

### `M_SQRT2`

```c
#define M_SQRT2 1.41421356237309504880
```

<a id="a5e9e29217f6ec61105a4520ec5942225"></a>

### `MAXFLOAT`

```c
#define MAXFLOAT 3.40282347e+38F
```

<a id="ac340fde9f4743ef7a9398b79d7bea8bd"></a>

### `double_t`

```c
typedef double double_t
```

<a id="a3ded656bbe9849ad9fa2b28530390f0a"></a>

### `float_t`

```c
typedef float float_t
```

<a id="ae0617f6dc83a7c2767e0766f5b3df203"></a>

### `sqrt()`

```c
double sqrt ( double square)
```

<a id="a769abd043ac3336a53318e327f2137c2"></a>

### `sqrtf()`

```c
float sqrtf ( float square)
```


## 196.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P050_math.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P195_zephyr__dt-bindings__clock__lpc11u6x_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P197_zephyr__drivers__sensor__max31865.h_文件参考.md)
