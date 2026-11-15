---
id: learning.zephyr-docs.api-file-service-interface-reference.page-8
title: zephyr__dsp__basicmath_f16.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_dsp\_\_basicmath\_f16.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

16位浮点数字信号处理（DSP）基础数学运算（Basicmath）的公共API。

<a id="details"></a>

```c
#include <zephyr/dsp/dsp.h>
```

查看此文件的源码。

16位浮点数字信号处理（DSP）基础数学运算（Basicmath）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga35c098db40d7973507bb17db7436c538"></a>

```c
void zdsp_mult_f16 (const float16_t *src_a, const float16_t *src_b, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_mult_f16](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#ga35c098db40d7973507bb17db7436c538)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量乘法（Floating-point Vector Multiplication）。

<a id="r_gaebb4b61e2e77ace0f9cc0a5765d6661a"></a>

```c
void zdsp_add_f16 (const float16_t *src_a, const float16_t *src_b, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_add_f16](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gaebb4b61e2e77ace0f9cc0a5765d6661a)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量加法（Floating-point Vector Addition）。

<a id="r_gadfc2150ce943fe13853dedc5a6cb75bd"></a>

```c
void zdsp_sub_f16 (const float16_t *src_a, const float16_t *src_b, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_sub_f16](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gadfc2150ce943fe13853dedc5a6cb75bd)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量减法（Floating-point Vector Subtraction）。

<a id="r_gaf25f08e866acb513c69797e4097dd1f5"></a>

```c
void zdsp_scale_f16 (const float16_t *src, float16_t scale, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#gaf25f08e866acb513c69797e4097dd1f5)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

<a id="r_gae1a01c6ab370ebdb6beaf12c02ca5b8d"></a>

```c
void zdsp_abs_f16 (const float16_t *src, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_f16](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#gae1a01c6ab370ebdb6beaf12c02ca5b8d)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量绝对值（floating-point vector absolute value）。

<a id="r_ga0ad6b24c20716781e2beb4164059160c"></a>

```c
void zdsp_dot_prod_f16 (const float16_t *src_a, const float16_t *src_b, uint32_t block_size, float16_t *result)
```

相关声明：[zdsp_dot_prod_f16](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga0ad6b24c20716781e2beb4164059160c)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)。

浮点向量的点积（Dot Product）。

<a id="r_ga0bcfb3671a9257cabb525fe95794b286"></a>

```c
void zdsp_offset_f16 (const float16_t *src, float16_t offset, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga0bcfb3671a9257cabb525fe95794b286)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

<a id="r_ga662d3680b3a44d00c6b402e9072128dc"></a>

```c
void zdsp_negate_f16 (const float16_t *src, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_f16](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga662d3680b3a44d00c6b402e9072128dc)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对浮点向量的各元素取负（Negation）。

<a id="r_ga3d3bed1aab5379a67c86b2ffc2ac0c9c"></a>

```c
void zdsp_clip_f16 (const float16_t *src, float16_t *dst, float16_t low, float16_t high, uint32_t num_samples)
```

相关声明：[zdsp_clip_f16](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga3d3bed1aab5379a67c86b2ffc2ac0c9c)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点数逐元素限幅（elementwise floating-point clipping）。


## 8.2\_原页交叉引用（Cross References）

- [zephyr/dsp/dsp.h](../api_source_reference/P187_dsp.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P054_basicmath_f16.h_源码浏览.md)
- [zdsp_mult_f16](../api_vector_pipeline_topic_reference/P017_向量乘法（Vector Multiplication）.md#ga35c098db40d7973507bb17db7436c538)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_add_f16](../api_vector_pipeline_topic_reference/P015_向量加法（Vector Addition）.md#gaebb4b61e2e77ace0f9cc0a5765d6661a)
- [zdsp_sub_f16](../api_vector_pipeline_topic_reference/P020_向量减法（Vector Subtraction）.md#gadfc2150ce943fe13853dedc5a6cb75bd)
- [zdsp_scale_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#gaf25f08e866acb513c69797e4097dd1f5)
- [zdsp_abs_f16](../api_network_time_topic_reference/P020_向量绝对值（Vector Absolute Value）.md#gae1a01c6ab370ebdb6beaf12c02ca5b8d)
- [zdsp_dot_prod_f16](../api_vector_pipeline_topic_reference/P016_向量点积（Vector Dot Product）.md#ga0ad6b24c20716781e2beb4164059160c)
- [zdsp_offset_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga0bcfb3671a9257cabb525fe95794b286)
- [zdsp_negate_f16](../api_vector_pipeline_topic_reference/P018_向量取负（Vector Negate）.md#ga662d3680b3a44d00c6b402e9072128dc)
- [zdsp_clip_f16](../api_auxiliary_topic_reference/P010_向量限幅（Vector Clipping）.md#ga3d3bed1aab5379a67c86b2ffc2ac0c9c)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dsp__basicmath.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__bluetooth__mesh__brg_cfg_cli.h_文件参考.md)
