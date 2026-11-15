---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-15
title: 向量加法（Vector Addition）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_向量加法（Vector Addition）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对两个向量逐元素相加。

<a id="details"></a>

对两个向量逐元素执行加法（Element-by-element Addition），算法如下。浮点（Floating-point）、Q7、Q15 和 Q31 数据类型各有独立函数。

```c

    dst[n] = src_a[n] + src_b[n],   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.1\_函数（Functions）

<a id="r_gae890add140205717dcb4b1c39650b797"></a>

```c
void zdsp_add_f32 (const float32_t *src_a, const float32_t *src_b, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_f32](#gae890add140205717dcb4b1c39650b797)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量加法（Floating-point Vector Addition）。

<a id="r_gae5d919e8595e80216302953797fcf987"></a>

```c
void zdsp_add_q7 (const q7_t *src_a, const q7_t *src_b, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q7](#gae5d919e8595e80216302953797fcf987)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量加法（Vector Addition）。

<a id="r_ga978af9251a9c8b8d62b47a921dcf9d38"></a>

```c
void zdsp_add_q15 (const q15_t *src_a, const q15_t *src_b, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q15](#ga978af9251a9c8b8d62b47a921dcf9d38)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量加法（Vector Addition）。

<a id="r_gad2bbabc990f868b3ecfe270458e22657"></a>

```c
void zdsp_add_q31 (const q31_t *src_a, const q31_t *src_b, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q31](#gad2bbabc990f868b3ecfe270458e22657)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量加法（Vector Addition）。

<a id="r_gaebb4b61e2e77ace0f9cc0a5765d6661a"></a>

```c
void zdsp_add_f16 (const float16_t *src_a, const float16_t *src_b, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_f16](#gaebb4b61e2e77ace0f9cc0a5765d6661a)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量加法（Floating-point Vector Addition）。

## 15.2\_详细说明（Detailed Documentation）

<a id="gaebb4b61e2e77ace0f9cc0a5765d6661a"></a>

### `zdsp_add_f16()`

```c
void zdsp_add_f16 ( const float16_t * src_a, const float16_t * src_b, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

浮点向量加法（Floating-point Vector Addition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gae890add140205717dcb4b1c39650b797"></a>

### `zdsp_add_f32()`

```c
void zdsp_add_f32 ( const float32_t * src_a, const float32_t * src_b, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

浮点向量加法（Floating-point Vector Addition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga978af9251a9c8b8d62b47a921dcf9d38"></a>

### `zdsp_add_q15()`

```c
void zdsp_add_q15 ( const q15_t * src_a, const q15_t * src_b, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q15 向量加法（Vector Addition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q15 范围 `[0x8000 0x7FFF]` 的结果进行饱和处理。

<a id="gad2bbabc990f868b3ecfe270458e22657"></a>

### `zdsp_add_q31()`

```c
void zdsp_add_q31 ( const q31_t * src_a, const q31_t * src_b, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q31 向量加法（Vector Addition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q31 范围 `[0x80000000 0x7FFFFFFF]` 的结果进行饱和处理。

<a id="gae5d919e8595e80216302953797fcf987"></a>

### `zdsp_add_q7()`

```c
void zdsp_add_q7 ( const q7_t * src_a, const q7_t * src_b, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q7 向量加法（Vector Addition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q7 范围 `[0x80 0x7F]` 的结果进行饱和处理。


## 15.3\_原页交叉引用（Cross References）

- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_LSM6DSV80X API主题.md) · [返回大纲](大纲.md) · [下一章](P016_向量点积（Vector Dot Product）.md)
