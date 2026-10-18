---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-18
title: 向量取负（Vector Negate）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_向量取负（Vector Negate）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对向量的各元素取负。

<a id="details"></a>

对向量各元素取负（Negation），算法如下。函数支持原位计算（In-place Computation），允许源指针与目标指针引用同一内存缓冲区。浮点（Floating-point）、Q7、Q15 和 Q31 数据类型各有独立函数。

```c

    dst[n] = -src[n],   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.1\_函数（Functions）

<a id="r_gad8760ce77fcf2198f73813278fa15343"></a>

```c
void zdsp_negate_f32 (const float32_t *src, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_f32](#gad8760ce77fcf2198f73813278fa15343)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对浮点向量的各元素取负（Negation）。

<a id="r_ga578a3cee7cff2d818e41ec974066d55a"></a>

```c
void zdsp_negate_q7 (const q7_t *src, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q7](#ga578a3cee7cff2d818e41ec974066d55a)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q7 向量的各元素取负（Negation）。

<a id="r_ga41dc3e0d8a0bd3654f74cbbd9038153d"></a>

```c
void zdsp_negate_q15 (const q15_t *src, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q15](#ga41dc3e0d8a0bd3654f74cbbd9038153d)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q15 向量的各元素取负（Negation）。

<a id="r_ga08591323e804b4d7932c7bade4331705"></a>

```c
void zdsp_negate_q31 (const q31_t *src, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_q31](#ga08591323e804b4d7932c7bade4331705)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对 Q31 向量的各元素取负（Negation）。

<a id="r_ga662d3680b3a44d00c6b402e9072128dc"></a>

```c
void zdsp_negate_f16 (const float16_t *src, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_negate_f16](#ga662d3680b3a44d00c6b402e9072128dc)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对浮点向量的各元素取负（Negation）。

## 18.2\_详细说明（Detailed Documentation）

<a id="ga662d3680b3a44d00c6b402e9072128dc"></a>

### `zdsp_negate_f16()`

```c
void zdsp_negate_f16 ( const float16_t * src, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

对浮点向量的各元素取负（Negation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="gad8760ce77fcf2198f73813278fa15343"></a>

### `zdsp_negate_f32()`

```c
void zdsp_negate_f32 ( const float32_t * src, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

对浮点向量的各元素取负（Negation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="ga41dc3e0d8a0bd3654f74cbbd9038153d"></a>

### `zdsp_negate_q15()`

```c
void zdsp_negate_q15 ( const q15_t * src, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

对 Q15 向量的各元素取负（Negation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），Q15 值 `-1`（`0x8000`）取负时饱和到允许的最大正值 `0x7FFF`。

<a id="ga08591323e804b4d7932c7bade4331705"></a>

### `zdsp_negate_q31()`

```c
void zdsp_negate_q31 ( const q31_t * src, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

对 Q31 向量的各元素取负（Negation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），Q31 值 `-1`（`0x80000000`）取负时饱和到允许的最大正值 `0x7FFFFFFF`。

<a id="ga578a3cee7cff2d818e41ec974066d55a"></a>

### `zdsp_negate_q7()`

```c
void zdsp_negate_q7 ( const q7_t * src, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

对 Q7 向量的各元素取负（Negation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），Q7 值 `-1`（`0x80`）取负时饱和到允许的最大正值 `0x7F`。


## 18.3\_原页交叉引用（Cross References）

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

[上一章](P017_向量乘法（Vector Multiplication）.md) · [返回大纲](大纲.md) · [下一章](P019_向量移位（Vector Shift）.md)
