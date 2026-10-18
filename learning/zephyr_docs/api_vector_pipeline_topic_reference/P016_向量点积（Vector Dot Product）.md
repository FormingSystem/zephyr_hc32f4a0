---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-16
title: 向量点积（Vector Dot Product）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_向量点积（Vector Dot Product）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

计算两个向量的点积。

<a id="details"></a>

计算两个向量的点积（Dot Product）：先逐元素相乘，再将结果求和，算法如下。浮点（Floating-point）、Q7、Q15 和 Q31 数据类型各有独立函数。

```c

    sum = src_a[0]*src_b[0] + src_a[1]*src_b[1] + ... + src_a[block_size-1]*src_b[block_size-1]
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.1\_函数（Functions）

<a id="r_ga66932c50dc7e2b7207ad5c8218c110a6"></a>

```c
void zdsp_dot_prod_f32 (const float32_t *src_a, const float32_t *src_b, uint32_t block_size, float32_t *result)
```

相关声明：[zdsp_dot_prod_f32](#ga66932c50dc7e2b7207ad5c8218c110a6)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)。

浮点向量的点积（Dot Product）。

<a id="r_gaa6bdeed693734e5d1c7b93b58eaf9eeb"></a>

```c
void zdsp_dot_prod_q7 (const q7_t *src_a, const q7_t *src_b, uint32_t block_size, q31_t *result)
```

相关声明：[zdsp_dot_prod_q7](#gaa6bdeed693734e5d1c7b93b58eaf9eeb)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)。

Q7 向量的点积（Dot Product）。

<a id="r_ga5a76ac790b7d981b97143f7473587ccf"></a>

```c
void zdsp_dot_prod_q15 (const q15_t *src_a, const q15_t *src_b, uint32_t block_size, q63_t *result)
```

相关声明：[zdsp_dot_prod_q15](#ga5a76ac790b7d981b97143f7473587ccf)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)。

Q15 向量的点积（Dot Product）。

<a id="r_gaae752f1d9645d8c80fcdabc0f0b249f8"></a>

```c
void zdsp_dot_prod_q31 (const q31_t *src_a, const q31_t *src_b, uint32_t block_size, q63_t *result)
```

相关声明：[zdsp_dot_prod_q31](#gaae752f1d9645d8c80fcdabc0f0b249f8)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)。

Q31 向量的点积（Dot Product）。

<a id="r_ga0ad6b24c20716781e2beb4164059160c"></a>

```c
void zdsp_dot_prod_f16 (const float16_t *src_a, const float16_t *src_b, uint32_t block_size, float16_t *result)
```

相关声明：[zdsp_dot_prod_f16](#ga0ad6b24c20716781e2beb4164059160c)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)。

浮点向量的点积（Dot Product）。

## 16.2\_详细说明（Detailed Documentation）

<a id="ga0ad6b24c20716781e2beb4164059160c"></a>

### `zdsp_dot_prod_f16()`

```c
void zdsp_dot_prod_f16 ( const float16_t * src_a, const float16_t * src_b, uint32_t block_size, float16_t * result )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

浮点向量的点积（Dot Product）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |
| `[out] result` | 在此返回输出结果（Output Result）。 |

<a id="ga66932c50dc7e2b7207ad5c8218c110a6"></a>

### `zdsp_dot_prod_f32()`

```c
void zdsp_dot_prod_f32 ( const float32_t * src_a, const float32_t * src_b, uint32_t block_size, float32_t * result )
```

```c
#include <zephyr/dsp/basicmath.h>
```

浮点向量的点积（Dot Product）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |
| `[out] result` | 在此返回输出结果（Output Result）。 |

<a id="ga5a76ac790b7d981b97143f7473587ccf"></a>

### `zdsp_dot_prod_q15()`

```c
void zdsp_dot_prod_q15 ( const q15_t * src_a, const q15_t * src_b, uint32_t block_size, q63_t * result )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q15 向量的点积（Dot Product）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |
| `[out] result` | 在此返回输出结果（Output Result）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**中间乘法采用 `1.15 × 1.15 = 2.30` 格式，乘积累加到 `34.30` 格式的 64 位累加器（Accumulator）。加法不进行饱和处理；由于累加器有 33 个保护位（Guard Bits），不存在溢出风险。返回结果为 `34.30` 格式。

<a id="gaae752f1d9645d8c80fcdabc0f0b249f8"></a>

### `zdsp_dot_prod_q31()`

```c
void zdsp_dot_prod_q31 ( const q31_t * src_a, const q31_t * src_b, uint32_t block_size, q63_t * result )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q31 向量的点积（Dot Product）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |
| `[out] result` | 在此返回输出结果（Output Result）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**中间乘法采用 `1.31 × 1.31 = 2.62` 格式，然后丢弃低 14 位，截断为 `2.48` 格式。该结果以非饱和方式加到 `16.48` 格式的 64 位累加器（Accumulator）。累加器有 15 个保护位（Guard Bits），只要向量长度小于 `2^16` 个元素，就没有溢出风险。返回结果为 `16.48` 格式。

<a id="gaa6bdeed693734e5d1c7b93b58eaf9eeb"></a>

### `zdsp_dot_prod_q7()`

```c
void zdsp_dot_prod_q7 ( const q7_t * src_a, const q7_t * src_b, uint32_t block_size, q31_t * result )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q7 向量的点积（Dot Product）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向第一个输入向量（Input Vector）。 |
| `[in] src_b` | 指向第二个输入向量（Input Vector）。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |
| `[out] result` | 在此返回输出结果（Output Result）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**中间乘法采用 `1.7 × 1.7 = 2.14` 格式，乘积累加到 `18.14` 格式的累加器（Accumulator）。加法不进行饱和处理；只要向量长度小于 `2^18` 个元素，就没有回绕（Wrap Around）风险。返回结果为 `18.14` 格式。


## 16.3\_原页交叉引用（Cross References）

- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q63_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_向量加法（Vector Addition）.md) · [返回大纲](大纲.md) · [下一章](P017_向量乘法（Vector Multiplication）.md)
