---
id: learning.zephyr-docs.api-file-service-interface-reference.page-7
title: zephyr__dsp__basicmath.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dsp\_\_basicmath.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字信号处理（DSP）基础数学运算（Basicmath）的公共API。

<a id="details"></a>

```c
#include <zephyr/dsp/dsp.h>
#include <zephyr/dsp/basicmath_f16.h>
```

查看此文件的源码。

数字信号处理（DSP）基础数学运算（Basicmath）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.1\_函数（Functions）

<a id="r_gae0792b036a40a19af1c25b3a6a23e988"></a>

```c
void zdsp_mult_q7 (const q7_t *src_a, const q7_t *src_b, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q7](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gae0792b036a40a19af1c25b3a6a23e988)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量乘法（Vector Multiplication）。

<a id="r_gaf8aa8d6e976c9ee5f4ac836506da3bc7"></a>

```c
void zdsp_mult_q15 (const q15_t *src_a, const q15_t *src_b, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q15](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量乘法（Vector Multiplication）。

<a id="r_ga0e4e4ff5e33e792feecf811cb8e96d18"></a>

```c
void zdsp_mult_q31 (const q31_t *src_a, const q31_t *src_b, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_q31](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#ga0e4e4ff5e33e792feecf811cb8e96d18)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量乘法（Vector Multiplication）。

<a id="r_gac9513150fc602b6bab481faf36f81ca4"></a>

```c
void zdsp_mult_f32 (const float32_t *src_a, const float32_t *src_b, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_f32](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gac9513150fc602b6bab481faf36f81ca4)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量乘法（Floating-point Vector Multiplication）。

<a id="r_gae890add140205717dcb4b1c39650b797"></a>

```c
void zdsp_add_f32 (const float32_t *src_a, const float32_t *src_b, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_f32](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gae890add140205717dcb4b1c39650b797)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量加法（Floating-point Vector Addition）。

<a id="r_gae5d919e8595e80216302953797fcf987"></a>

```c
void zdsp_add_q7 (const q7_t *src_a, const q7_t *src_b, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q7](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gae5d919e8595e80216302953797fcf987)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量加法（Vector Addition）。

<a id="r_ga978af9251a9c8b8d62b47a921dcf9d38"></a>

```c
void zdsp_add_q15 (const q15_t *src_a, const q15_t *src_b, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q15](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#ga978af9251a9c8b8d62b47a921dcf9d38)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量加法（Vector Addition）。

<a id="r_gad2bbabc990f868b3ecfe270458e22657"></a>

```c
void zdsp_add_q31 (const q31_t *src_a, const q31_t *src_b, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_q31](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gad2bbabc990f868b3ecfe270458e22657)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量加法（Vector Addition）。

<a id="r_gafc66edd5888b19174cb24c2ea858d24d"></a>

```c
void zdsp_sub_f32 (const float32_t *src_a, const float32_t *src_b, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_sub_f32](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gafc66edd5888b19174cb24c2ea858d24d)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量减法（Floating-point Vector Subtraction）。

<a id="r_ga4eb67772a48933a9f24a68f73228adbf"></a>

```c
void zdsp_sub_q7 (const q7_t *src_a, const q7_t *src_b, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_sub_q7](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#ga4eb67772a48933a9f24a68f73228adbf)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量减法（Vector Subtraction）。

<a id="r_gab9698353b69654eefbd76ff6f723a4f3"></a>

```c
void zdsp_sub_q15 (const q15_t *src_a, const q15_t *src_b, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_sub_q15](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gab9698353b69654eefbd76ff6f723a4f3)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量减法（Vector Subtraction）。

<a id="r_ga693b9677fdf54694e49e03a9b629b35d"></a>

```c
void zdsp_sub_q31 (const q31_t *src_a, const q31_t *src_b, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_sub_q31](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#ga693b9677fdf54694e49e03a9b629b35d)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量减法（Vector Subtraction）。

<a id="r_ga3a07935285b763bb9e9106db42292466"></a>

```c
void zdsp_scale_f32 (const float32_t *src, float32_t scale, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga3a07935285b763bb9e9106db42292466)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

<a id="r_ga2158a3f20bd5af0516f5b3af824c32e1"></a>

```c
void zdsp_scale_q7 (const q7_t *src, q7_t scale_fract, int8_t shift, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga2158a3f20bd5af0516f5b3af824c32e1)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q7 向量乘以标量（Scalar）。

<a id="r_ga95e03e993542ff1710c771a9dc0eb01b"></a>

```c
void zdsp_scale_q15 (const q15_t *src, q15_t scale_fract, int8_t shift, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga95e03e993542ff1710c771a9dc0eb01b)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q15 向量乘以标量（Scalar）。

<a id="r_ga63eaab2b1ef431e4bceb90b0a701c879"></a>

```c
void zdsp_scale_q31 (const q31_t *src, q31_t scale_fract, int8_t shift, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga63eaab2b1ef431e4bceb90b0a701c879)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q31 向量乘以标量（Scalar）。

<a id="r_ga5a5358fb90f726256f064757fbab1bcd"></a>

```c
void zdsp_abs_f32 (const float32_t *src, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_f32](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga5a5358fb90f726256f064757fbab1bcd)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量绝对值（floating-point vector absolute value）。

<a id="r_ga69c38809979de090a3458ec9b31f4cb4"></a>

```c
void zdsp_abs_q7 (const q7_t *src, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q7](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga69c38809979de090a3458ec9b31f4cb4)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量绝对值。

<a id="r_ga53ee6bbc05423703f6299fd60c8e1d44"></a>

```c
void zdsp_abs_q15 (const q15_t *src, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q15](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga53ee6bbc05423703f6299fd60c8e1d44)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量绝对值。

<a id="r_ga74ccbbaf60257ca482fc96e1d40edeca"></a>

```c
void zdsp_abs_q31 (const q31_t *src, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q31](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga74ccbbaf60257ca482fc96e1d40edeca)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量绝对值。

<a id="r_ga66932c50dc7e2b7207ad5c8218c110a6"></a>

```c
void zdsp_dot_prod_f32 (const float32_t *src_a, const float32_t *src_b, uint32_t block_size, float32_t *result)
```

相关声明：[zdsp_dot_prod_f32](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga66932c50dc7e2b7207ad5c8218c110a6)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)。

浮点向量的点积（Dot Product）。

<a id="r_gaa6bdeed693734e5d1c7b93b58eaf9eeb"></a>

```c
void zdsp_dot_prod_q7 (const q7_t *src_a, const q7_t *src_b, uint32_t block_size, q31_t *result)
```

相关声明：[zdsp_dot_prod_q7](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)。

Q7 向量的点积（Dot Product）。

<a id="r_ga5a76ac790b7d981b97143f7473587ccf"></a>

```c
void zdsp_dot_prod_q15 (const q15_t *src_a, const q15_t *src_b, uint32_t block_size, q63_t *result)
```

相关声明：[zdsp_dot_prod_q15](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga5a76ac790b7d981b97143f7473587ccf)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)。

Q15 向量的点积（Dot Product）。

<a id="r_gaae752f1d9645d8c80fcdabc0f0b249f8"></a>

```c
void zdsp_dot_prod_q31 (const q31_t *src_a, const q31_t *src_b, uint32_t block_size, q63_t *result)
```

相关声明：[zdsp_dot_prod_q31](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#gaae752f1d9645d8c80fcdabc0f0b249f8)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)。

Q31 向量的点积（Dot Product）。

<a id="r_ga8eb72ff139c173d3e1794a1d1c1c8fde"></a>

```c
void zdsp_shift_q7 (const q7_t *src, int8_t shift_bits, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q7](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#ga8eb72ff139c173d3e1794a1d1c1c8fde)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q7 向量的各元素移动指定的位数。

<a id="r_ga738fc0fe86b9c910a30fceff7dc4a789"></a>

```c
void zdsp_shift_q15 (const q15_t *src, int8_t shift_bits, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q15](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#ga738fc0fe86b9c910a30fceff7dc4a789)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q15 向量的各元素移动指定的位数。

<a id="r_gaf9af89a3c76ad385eec0225185b522c9"></a>

```c
void zdsp_shift_q31 (const q31_t *src, int8_t shift_bits, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q31](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#gaf9af89a3c76ad385eec0225185b522c9)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q31 向量的各元素移动指定的位数。

<a id="r_ga1f14e702ad5dc6482fcdb4758ad862c3"></a>

```c
void zdsp_offset_f32 (const float32_t *src, float32_t offset, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1f14e702ad5dc6482fcdb4758ad862c3)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

<a id="r_ga701b8bbd1437e0f19807c38fd4d0e7e9"></a>

```c
void zdsp_offset_q7 (const q7_t *src, q7_t offset, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga701b8bbd1437e0f19807c38fd4d0e7e9)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q7 向量加上常量偏移（Constant Offset）。

<a id="r_ga1740996532090e41ce20913bb201023c"></a>

```c
void zdsp_offset_q15 (const q15_t *src, q15_t offset, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1740996532090e41ce20913bb201023c)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q15 向量加上常量偏移（Constant Offset）。

<a id="r_ga2b5958ec0fc8bb26662c41136ec46b3e"></a>

```c
void zdsp_offset_q31 (const q31_t *src, q31_t offset, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga2b5958ec0fc8bb26662c41136ec46b3e)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q31 向量加上常量偏移（Constant Offset）。

<a id="r_gad8760ce77fcf2198f73813278fa15343"></a>

```c
void zdsp_negate_f32 (const float32_t *src, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_f32](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#gad8760ce77fcf2198f73813278fa15343)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对浮点向量的各元素取负（Negation）。

<a id="r_ga578a3cee7cff2d818e41ec974066d55a"></a>

```c
void zdsp_negate_q7 (const q7_t *src, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q7](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga578a3cee7cff2d818e41ec974066d55a)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q7 向量的各元素取负（Negation）。

<a id="r_ga41dc3e0d8a0bd3654f74cbbd9038153d"></a>

```c
void zdsp_negate_q15 (const q15_t *src, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q15](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga41dc3e0d8a0bd3654f74cbbd9038153d)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q15 向量的各元素取负（Negation）。

<a id="r_ga08591323e804b4d7932c7bade4331705"></a>

```c
void zdsp_negate_q31 (const q31_t *src, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q31](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga08591323e804b4d7932c7bade4331705)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q31 向量的各元素取负（Negation）。

<a id="r_ga22c8c022d4f8cd9e34f1e1e47433d121"></a>

```c
void zdsp_and_u8 (const uint8_t *src_a, const uint8_t *src_b, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u8](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga22c8c022d4f8cd9e34f1e1e47433d121)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

<a id="r_ga988879dc54666692130793f6ce26fd23"></a>

```c
void zdsp_and_u16 (const uint16_t *src_a, const uint16_t *src_b, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u16](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga988879dc54666692130793f6ce26fd23)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

<a id="r_ga99019932e69574ca8aef86b4ace9c3b6"></a>

```c
void zdsp_and_u32 (const uint32_t *src_a, const uint32_t *src_b, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u32](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga99019932e69574ca8aef86b4ace9c3b6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

<a id="r_gabf9687bce70f19c4192b2ddba7b0d2da"></a>

```c
void zdsp_or_u8 (const uint8_t *src_a, const uint8_t *src_b, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_or_u8](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#gabf9687bce70f19c4192b2ddba7b0d2da)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑或（bitwise OR）。

<a id="r_ga979e50ef34a5e5c8dc28f1cfc5ef708a"></a>

```c
void zdsp_or_u16 (const uint16_t *src_a, const uint16_t *src_b, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_or_u16](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑或（bitwise OR）。

<a id="r_gaa218930efe8ab83663eb00b4f6f170bc"></a>

```c
void zdsp_or_u32 (const uint32_t *src_a, const uint32_t *src_b, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_or_u32](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#gaa218930efe8ab83663eb00b4f6f170bc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑或（bitwise OR）。

<a id="r_gaafd38edd648a03d328d51b5ca9097b5d"></a>

```c
void zdsp_not_u8 (const uint8_t *src, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u8](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#gaafd38edd648a03d328d51b5ca9097b5d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

<a id="r_ga3bca20f3c626e1a64dd79d0e22a43bed"></a>

```c
void zdsp_not_u16 (const uint16_t *src, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u16](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#ga3bca20f3c626e1a64dd79d0e22a43bed)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

<a id="r_gafd6993acd6abeaa529dea84f3fd4d3a9"></a>

```c
void zdsp_not_u32 (const uint32_t *src, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u32](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#gafd6993acd6abeaa529dea84f3fd4d3a9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

<a id="r_ga4f5a442ce2ce79a6d09fde4648ceb100"></a>

```c
void zdsp_xor_u8 (const uint8_t *src_a, const uint8_t *src_b, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u8](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#ga4f5a442ce2ce79a6d09fde4648ceb100)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

<a id="r_gaa4d486a9a9022120e86e6e5d62940444"></a>

```c
void zdsp_xor_u16 (const uint16_t *src_a, const uint16_t *src_b, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u16](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#gaa4d486a9a9022120e86e6e5d62940444)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

<a id="r_gac4dd8fed6e7485a0e989fb37b3fe0c77"></a>

```c
void zdsp_xor_u32 (const uint32_t *src_a, const uint32_t *src_b, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u32](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#gac4dd8fed6e7485a0e989fb37b3fe0c77)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

<a id="r_gaa81f891d1946313161d1a2989aafe0e1"></a>

```c
void zdsp_clip_f32 (const float32_t *src, float32_t *dst, float32_t low, float32_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_f32](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#gaa81f891d1946313161d1a2989aafe0e1)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点数逐元素限幅（elementwise floating-point clipping）。

<a id="r_ga2a7483cb8150e3caee8fade382dc3ceb"></a>

```c
void zdsp_clip_q31 (const q31_t *src, q31_t *dst, q31_t low, q31_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q31](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga2a7483cb8150e3caee8fade382dc3ceb)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。

<a id="r_ga7c83f52241784bfdf81baf14581435b9"></a>

```c
void zdsp_clip_q15 (const q15_t *src, q15_t *dst, q15_t low, q15_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q15](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga7c83f52241784bfdf81baf14581435b9)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。

<a id="r_ga4e368fccf4ec5f46e82127816ecfc22e"></a>

```c
void zdsp_clip_q7 (const q7_t *src, q7_t *dst, q7_t low, q7_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_q7](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga4e368fccf4ec5f46e82127816ecfc22e)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定点数逐元素限幅（elementwise fixed-point clipping）。


## 7.2\_原页交叉引用（Cross References）

- [zephyr/dsp/dsp.h](../api_source_reference/P187_dsp.h_源码浏览.md)
- [zephyr/dsp/basicmath_f16.h](../api_source_reference/P054_basicmath_f16.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P053_basicmath.h_源码浏览.md)
- [zdsp_mult_q7](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gae0792b036a40a19af1c25b3a6a23e988)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_mult_q15](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [zdsp_mult_q31](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#ga0e4e4ff5e33e792feecf811cb8e96d18)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [zdsp_mult_f32](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#gac9513150fc602b6bab481faf36f81ca4)
- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [zdsp_add_f32](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gae890add140205717dcb4b1c39650b797)
- [zdsp_add_q7](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gae5d919e8595e80216302953797fcf987)
- [zdsp_add_q15](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#ga978af9251a9c8b8d62b47a921dcf9d38)
- [zdsp_add_q31](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gad2bbabc990f868b3ecfe270458e22657)
- [zdsp_sub_f32](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gafc66edd5888b19174cb24c2ea858d24d)
- [zdsp_sub_q7](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#ga4eb67772a48933a9f24a68f73228adbf)
- [zdsp_sub_q15](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gab9698353b69654eefbd76ff6f723a4f3)
- [zdsp_sub_q31](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#ga693b9677fdf54694e49e03a9b629b35d)
- [zdsp_scale_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga3a07935285b763bb9e9106db42292466)
- [zdsp_scale_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga2158a3f20bd5af0516f5b3af824c32e1)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [zdsp_scale_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga95e03e993542ff1710c771a9dc0eb01b)
- [zdsp_scale_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga63eaab2b1ef431e4bceb90b0a701c879)
- [zdsp_abs_f32](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga5a5358fb90f726256f064757fbab1bcd)
- [zdsp_abs_q7](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga69c38809979de090a3458ec9b31f4cb4)
- [zdsp_abs_q15](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga53ee6bbc05423703f6299fd60c8e1d44)
- [zdsp_abs_q31](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#ga74ccbbaf60257ca482fc96e1d40edeca)
- [zdsp_dot_prod_f32](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga66932c50dc7e2b7207ad5c8218c110a6)
- [zdsp_dot_prod_q7](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb)
- [zdsp_dot_prod_q15](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga5a76ac790b7d981b97143f7473587ccf)
- [q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)
- [zdsp_dot_prod_q31](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#gaae752f1d9645d8c80fcdabc0f0b249f8)
- [zdsp_shift_q7](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#ga8eb72ff139c173d3e1794a1d1c1c8fde)
- [zdsp_shift_q15](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#ga738fc0fe86b9c910a30fceff7dc4a789)
- [zdsp_shift_q31](../api_vector_pipeline_topic_reference/P019_向量移位（Vector Shift）.md#gaf9af89a3c76ad385eec0225185b522c9)
- [zdsp_offset_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1f14e702ad5dc6482fcdb4758ad862c3)
- [zdsp_offset_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga701b8bbd1437e0f19807c38fd4d0e7e9)
- [zdsp_offset_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1740996532090e41ce20913bb201023c)
- [zdsp_offset_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga2b5958ec0fc8bb26662c41136ec46b3e)
- [zdsp_negate_f32](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#gad8760ce77fcf2198f73813278fa15343)
- [zdsp_negate_q7](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga578a3cee7cff2d818e41ec974066d55a)
- [zdsp_negate_q15](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga41dc3e0d8a0bd3654f74cbbd9038153d)
- [zdsp_negate_q31](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga08591323e804b4d7932c7bade4331705)
- [zdsp_and_u8](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga22c8c022d4f8cd9e34f1e1e47433d121)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zdsp_and_u16](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga988879dc54666692130793f6ce26fd23)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zdsp_and_u32](../api_protocol_topic_reference/P024_向量按位与（Vector bitwise AND）.md#ga99019932e69574ca8aef86b4ace9c3b6)
- [zdsp_or_u8](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#gabf9687bce70f19c4192b2ddba7b0d2da)
- [zdsp_or_u16](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a)
- [zdsp_or_u32](../api_protocol_topic_reference/P026_向量按位或（Vector bitwise OR）.md#gaa218930efe8ab83663eb00b4f6f170bc)
- [zdsp_not_u8](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#gaafd38edd648a03d328d51b5ca9097b5d)
- [zdsp_not_u16](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#ga3bca20f3c626e1a64dd79d0e22a43bed)
- [zdsp_not_u32](../api_protocol_topic_reference/P025_向量按位非（Vector bitwise NOT）.md#gafd6993acd6abeaa529dea84f3fd4d3a9)
- [zdsp_xor_u8](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#ga4f5a442ce2ce79a6d09fde4648ceb100)
- [zdsp_xor_u16](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#gaa4d486a9a9022120e86e6e5d62940444)
- [zdsp_xor_u32](../api_protocol_topic_reference/P027_向量按位异或（Vector bitwise XOR）.md#gac4dd8fed6e7485a0e989fb37b3fe0c77)
- [zdsp_clip_f32](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#gaa81f891d1946313161d1a2989aafe0e1)
- [zdsp_clip_q31](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga2a7483cb8150e3caee8fade382dc3ceb)
- [zdsp_clip_q15](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga7c83f52241784bfdf81baf14581435b9)
- [zdsp_clip_q7](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga4e368fccf4ec5f46e82127816ecfc22e)

<a id="header-details"></a>

---

[上一章](P006_zephyr__mgmt__ec_host_cmd__backend.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dsp__basicmath_f16.h_文件参考.md)
