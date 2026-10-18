---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-9
title: 向量缩放（Vector Scale）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_向量缩放（Vector Scale）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将向量乘以一个标量值。

<a id="details"></a>

将向量乘以标量（Scalar）。浮点数据的算法见下方第一个原始公式。在定点 Q7、Q15 和 Q31 函数中，缩放系数（Scale）由小数乘数 `scale_fract` 和算术移位量 `shift` 共同表示；移位允许缩放运算的增益超过 1.0。定点算法见下方第二个原始公式。作用于定点数据的总缩放系数为 `scale = scale_fract * 2^shift`。函数支持原位计算（In-place Computation），允许源指针和目标指针引用同一内存缓冲区。

```c

    dst[n] = src[n] * scale,   0 <= n < block_size.
```

```c

    dst[n] = (src[n] * scale_fract) << shift,   0 <= n < block_size.
```

```c

    scale = scale_fract * 2^shift.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_ga3a07935285b763bb9e9106db42292466"></a>

```c
void zdsp_scale_f32 (const float32_t *src, float32_t scale, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_f32](#ga3a07935285b763bb9e9106db42292466)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

<a id="r_ga2158a3f20bd5af0516f5b3af824c32e1"></a>

```c
void zdsp_scale_q7 (const q7_t *src, q7_t scale_fract, int8_t shift, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q7](#ga2158a3f20bd5af0516f5b3af824c32e1)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q7 向量乘以标量（Scalar）。

<a id="r_ga95e03e993542ff1710c771a9dc0eb01b"></a>

```c
void zdsp_scale_q15 (const q15_t *src, q15_t scale_fract, int8_t shift, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q15](#ga95e03e993542ff1710c771a9dc0eb01b)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q15 向量乘以标量（Scalar）。

<a id="r_ga63eaab2b1ef431e4bceb90b0a701c879"></a>

```c
void zdsp_scale_q31 (const q31_t *src, q31_t scale_fract, int8_t shift, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_q31](#ga63eaab2b1ef431e4bceb90b0a701c879)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q31 向量乘以标量（Scalar）。

<a id="r_gaf25f08e866acb513c69797e4097dd1f5"></a>

```c
void zdsp_scale_f16 (const float16_t *src, float16_t scale, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_scale_f16](#gaf25f08e866acb513c69797e4097dd1f5)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

## 9.2\_详细说明（Detailed Documentation）

<a id="gaf25f08e866acb513c69797e4097dd1f5"></a>

### `zdsp_scale_f16()`

```c
void zdsp_scale_f16 ( const float16_t * src, float16_t scale, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] scale` | 要应用的缩放系数（Scale Factor）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="ga3a07935285b763bb9e9106db42292466"></a>

### `zdsp_scale_f32()`

```c
void zdsp_scale_f32 ( const float32_t * src, float32_t scale, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将浮点向量（Floating-point Vector）乘以标量（Scalar）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] scale` | 要应用的缩放系数（Scale Factor）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="ga95e03e993542ff1710c771a9dc0eb01b"></a>

### `zdsp_scale_q15()`

```c
void zdsp_scale_q15 ( const q15_t * src, q15_t scale_fract, int8_t shift, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q15 向量乘以标量（Scalar）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] scale_fract` | 缩放值的小数部分（Fractional Portion）。 |
| `[in] shift` | 结果需要移位的位数。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**输入数据 `*src` 和 `scale_fract` 为 `1.15` 格式；相乘得到 `2.30` 格式的中间结果，再通过带饱和处理的移位转换为 `1.15` 格式。

<a id="ga63eaab2b1ef431e4bceb90b0a701c879"></a>

### `zdsp_scale_q31()`

```c
void zdsp_scale_q31 ( const q31_t * src, q31_t scale_fract, int8_t shift, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q31 向量乘以标量（Scalar）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] scale_fract` | 缩放值的小数部分（Fractional Portion）。 |
| `[in] shift` | 结果需要移位的位数。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**输入数据 `*src` 和 `scale_fract` 为 `1.31` 格式；相乘得到 `2.62` 格式的中间结果，再通过带饱和处理的移位转换为 `1.31` 格式。

<a id="ga2158a3f20bd5af0516f5b3af824c32e1"></a>

### `zdsp_scale_q7()`

```c
void zdsp_scale_q7 ( const q7_t * src, q7_t scale_fract, int8_t shift, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q7 向量乘以标量（Scalar）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] scale_fract` | 缩放值的小数部分（Fractional Portion）。 |
| `[in] shift` | 结果需要移位的位数。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**输入数据 `*src` 和 `scale_fract` 为 `1.7` 格式；相乘得到 `2.14` 格式的中间结果，再通过带饱和处理的移位转换为 `1.7` 格式。


## 9.3\_原页交叉引用（Cross References）

- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](../api_file_service_interface_reference/P008_zephyr__dsp__basicmath_f16.h_文件参考.md)
- [zephyr/dsp/basicmath.h](../api_file_service_interface_reference/P007_zephyr__dsp__basicmath.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_向量偏移（Vector Offset）.md) · [返回大纲](大纲.md) · [下一章](P010_映像管理回调（Image Management Callbacks）.md)
