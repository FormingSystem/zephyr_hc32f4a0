---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-10
title: 向量限幅（Vector Clipping）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_向量限幅（Vector Clipping）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

逐元素对值进行限幅。

<a id="details"></a>

逐元素限幅（element-by-element clipping），将值限制在两个边界之间。分别为浮点、Q7、Q15 和 Q31 数据类型提供独立函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.1\_函数（Functions）

<a id="r_gaa81f891d1946313161d1a2989aafe0e1"></a>

```c
void zdsp_clip_f32 (const float32_t *src, float32_t *dst, float32_t low, float32_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_f32](#gaa81f891d1946313161d1a2989aafe0e1)、[float32_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点数逐元素限幅（elementwise floating-point clipping）。

<a id="r_ga2a7483cb8150e3caee8fade382dc3ceb"></a>

```c
void zdsp_clip_q31 (const q31_t *src, q31_t *dst, q31_t low, q31_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q31](#ga2a7483cb8150e3caee8fade382dc3ceb)、[q31_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。

<a id="r_ga7c83f52241784bfdf81baf14581435b9"></a>

```c
void zdsp_clip_q15 (const q15_t *src, q15_t *dst, q15_t low, q15_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q15](#ga7c83f52241784bfdf81baf14581435b9)、[q15_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。

<a id="r_ga4e368fccf4ec5f46e82127816ecfc22e"></a>

```c
void zdsp_clip_q7 (const q7_t *src, q7_t *dst, q7_t low, q7_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q7](#ga4e368fccf4ec5f46e82127816ecfc22e)、[q7_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。

<a id="r_ga3d3bed1aab5379a67c86b2ffc2ac0c9c"></a>

```c
void zdsp_clip_f16 (const float16_t *src, float16_t *dst, float16_t low, float16_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_f16](#ga3d3bed1aab5379a67c86b2ffc2ac0c9c)、[float16_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点数逐元素限幅（elementwise floating-point clipping）。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga3d3bed1aab5379a67c86b2ffc2ac0c9c"></a>

### `zdsp_clip_f16()`

```c
void zdsp_clip_f16 ( const float16_t * src, float16_t * dst, float16_t low, float16_t high, uint32_t num_samples )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

浮点数逐元素限幅（elementwise floating-point clipping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入值。 |
| `[out] dst` | 指向限幅后的输出值。 |
| `[in] low` | 下界（lower bound）。 |
| `[in] high` | 上界（higher bound）。 |
| `[in] num_samples` | 要限幅的样本数。 |

<a id="gaa81f891d1946313161d1a2989aafe0e1"></a>

### `zdsp_clip_f32()`

```c
void zdsp_clip_f32 ( const float32_t * src, float32_t * dst, float32_t low, float32_t high, uint32_t num_samples )
```

```c
#include <zephyr/dsp/basicmath.h>
```

浮点数逐元素限幅（elementwise floating-point clipping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入值。 |
| `[out] dst` | 指向限幅后的输出值。 |
| `[in] low` | 下界（lower bound）。 |
| `[in] high` | 上界（higher bound）。 |
| `[in] num_samples` | 要限幅的样本数。 |

<a id="ga7c83f52241784bfdf81baf14581435b9"></a>

### `zdsp_clip_q15()`

```c
void zdsp_clip_q15 ( const q15_t * src, q15_t * dst, q15_t low, q15_t high, uint32_t num_samples )
```

```c
#include <zephyr/dsp/basicmath.h>
```

定点数逐元素限幅（elementwise fixed-point clipping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入值。 |
| `[out] dst` | 指向限幅后的输出值。 |
| `[in] low` | 下界（lower bound）。 |
| `[in] high` | 上界（higher bound）。 |
| `[in] num_samples` | 要限幅的样本数。 |

<a id="ga2a7483cb8150e3caee8fade382dc3ceb"></a>

### `zdsp_clip_q31()`

```c
void zdsp_clip_q31 ( const q31_t * src, q31_t * dst, q31_t low, q31_t high, uint32_t num_samples )
```

```c
#include <zephyr/dsp/basicmath.h>
```

定点数逐元素限幅（elementwise fixed-point clipping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入值。 |
| `[out] dst` | 指向限幅后的输出值。 |
| `[in] low` | 下界（lower bound）。 |
| `[in] high` | 上界（higher bound）。 |
| `[in] num_samples` | 要限幅的样本数。 |

<a id="ga4e368fccf4ec5f46e82127816ecfc22e"></a>

### `zdsp_clip_q7()`

```c
void zdsp_clip_q7 ( const q7_t * src, q7_t * dst, q7_t low, q7_t high, uint32_t num_samples )
```

```c
#include <zephyr/dsp/basicmath.h>
```

定点数逐元素限幅（elementwise fixed-point clipping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入值。 |
| `[out] dst` | 指向限幅后的输出值。 |
| `[in] low` | 下界（lower bound）。 |
| `[in] high` | 上界（higher bound）。 |
| `[in] num_samples` | 要限幅的样本数。 |


## 10.3\_原页交叉引用（Cross References）

- [float32_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q31_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [q15_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q7_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [float16_t](P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_数字信号处理（Digital Signal Processing，DSP）.md) · [返回大纲](大纲.md) · [下一章](P011_设置管理回调（Settings Management Callbacks）.md)
