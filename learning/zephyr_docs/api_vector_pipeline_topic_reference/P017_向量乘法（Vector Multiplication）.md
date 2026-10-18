---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-17
title: 向量乘法（Vector Multiplication）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_向量乘法（Vector Multiplication）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对两个向量逐元素相乘。

<a id="details"></a>

对两个向量逐元素执行乘法（Element-by-element Multiplication），算法如下。浮点（Floating-point）、Q7、Q15 和 Q31 数据类型各有独立函数。

```c

    dst[n] = src_a[n] * src_b[n],   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.1\_函数（Functions）

<a id="r_gae0792b036a40a19af1c25b3a6a23e988"></a>

```c
void zdsp_mult_q7 (const q7_t *src_a, const q7_t *src_b, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q7](#gae0792b036a40a19af1c25b3a6a23e988)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量乘法（Vector Multiplication）。

<a id="r_gaf8aa8d6e976c9ee5f4ac836506da3bc7"></a>

```c
void zdsp_mult_q15 (const q15_t *src_a, const q15_t *src_b, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q15](#gaf8aa8d6e976c9ee5f4ac836506da3bc7)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量乘法（Vector Multiplication）。

<a id="r_ga0e4e4ff5e33e792feecf811cb8e96d18"></a>

```c
void zdsp_mult_q31 (const q31_t *src_a, const q31_t *src_b, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q31](#ga0e4e4ff5e33e792feecf811cb8e96d18)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量乘法（Vector Multiplication）。

<a id="r_gac9513150fc602b6bab481faf36f81ca4"></a>

```c
void zdsp_mult_f32 (const float32_t *src_a, const float32_t *src_b, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_f32](#gac9513150fc602b6bab481faf36f81ca4)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量乘法（Floating-point Vector Multiplication）。

<a id="r_ga35c098db40d7973507bb17db7436c538"></a>

```c
void zdsp_mult_f16 (const float16_t *src_a, const float16_t *src_b, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_f16](#ga35c098db40d7973507bb17db7436c538)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量乘法（Floating-point Vector Multiplication）。

## 17.2\_详细说明（Detailed Documentation）

<a id="ga35c098db40d7973507bb17db7436c538"></a>

### `zdsp_mult_f16()`

```c
void zdsp_mult_f16 ( const float16_t * src_a, const float16_t * src_b, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

浮点向量乘法（Floating-point Vector Multiplication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gac9513150fc602b6bab481faf36f81ca4"></a>

### `zdsp_mult_f32()`

```c
void zdsp_mult_f32 ( const float32_t * src_a, const float32_t * src_b, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

浮点向量乘法（Floating-point Vector Multiplication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gaf8aa8d6e976c9ee5f4ac836506da3bc7"></a>

### `zdsp_mult_q15()`

```c
void zdsp_mult_q15 ( const q15_t * src_a, const q15_t * src_b, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q15 向量乘法（Vector Multiplication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q15 范围 `[0x8000 0x7FFF]` 的结果进行饱和处理。

<a id="ga0e4e4ff5e33e792feecf811cb8e96d18"></a>

### `zdsp_mult_q31()`

```c
void zdsp_mult_q31 ( const q31_t * src_a, const q31_t * src_b, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q31 向量乘法（Vector Multiplication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q31 范围 `[0x80000000 0x7FFFFFFF]` 的结果进行饱和处理。

<a id="gae0792b036a40a19af1c25b3a6a23e988"></a>

### `zdsp_mult_q7()`

```c
void zdsp_mult_q7 ( const q7_t * src_a, const q7_t * src_b, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q7 向量乘法（Vector Multiplication）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q7 范围 `[0x80 0x7F]` 的结果进行饱和处理。


## 17.3\_原页交叉引用（Cross References）

- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_向量点积（Vector Dot Product）.md) · [返回大纲](大纲.md) · [下一章](P018_向量取负（Vector Negate）.md)
