---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-8
title: 向量偏移（Vector Offset）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_向量偏移（Vector Offset）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为向量的每个元素加上一个常量偏移值。

<a id="details"></a>

为向量各元素加上常量偏移（Constant Offset），算法如下。函数支持原位计算（In-place Computation），允许源指针和目标指针引用同一内存缓冲区。浮点（Floating-point）、Q7、Q15 和 Q31 数据类型各有独立函数。

```c

    dst[n] = src[n] + offset,   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga1f14e702ad5dc6482fcdb4758ad862c3"></a>

```c
void zdsp_offset_f32 (const float32_t *src, float32_t offset, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_f32](#ga1f14e702ad5dc6482fcdb4758ad862c3)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

<a id="r_ga701b8bbd1437e0f19807c38fd4d0e7e9"></a>

```c
void zdsp_offset_q7 (const q7_t *src, q7_t offset, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q7](#ga701b8bbd1437e0f19807c38fd4d0e7e9)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q7 向量加上常量偏移（Constant Offset）。

<a id="r_ga1740996532090e41ce20913bb201023c"></a>

```c
void zdsp_offset_q15 (const q15_t *src, q15_t offset, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q15](#ga1740996532090e41ce20913bb201023c)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q15 向量加上常量偏移（Constant Offset）。

<a id="r_ga2b5958ec0fc8bb26662c41136ec46b3e"></a>

```c
void zdsp_offset_q31 (const q31_t *src, q31_t offset, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_q31](#ga2b5958ec0fc8bb26662c41136ec46b3e)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 Q31 向量加上常量偏移（Constant Offset）。

<a id="r_ga0bcfb3671a9257cabb525fe95794b286"></a>

```c
void zdsp_offset_f16 (const float16_t *src, float16_t offset, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_offset_f16](#ga0bcfb3671a9257cabb525fe95794b286)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

## 8.2\_详细说明（Detailed Documentation）

<a id="ga0bcfb3671a9257cabb525fe95794b286"></a>

### `zdsp_offset_f16()`

```c
void zdsp_offset_f16 ( const float16_t * src, float16_t offset, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] offset` | 要加上的偏移量（Offset）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="ga1f14e702ad5dc6482fcdb4758ad862c3"></a>

### `zdsp_offset_f32()`

```c
void zdsp_offset_f32 ( const float32_t * src, float32_t offset, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

为浮点向量（Floating-point Vector）加上常量偏移（Constant Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] offset` | 要加上的偏移量（Offset）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

<a id="ga1740996532090e41ce20913bb201023c"></a>

### `zdsp_offset_q15()`

```c
void zdsp_offset_q15 ( const q15_t * src, q15_t offset, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

为 Q15 向量加上常量偏移（Constant Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] offset` | 要加上的偏移量（Offset）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q15 范围 `[0x8000 0x7FFF]` 的结果进行饱和处理。

<a id="ga2b5958ec0fc8bb26662c41136ec46b3e"></a>

### `zdsp_offset_q31()`

```c
void zdsp_offset_q31 ( const q31_t * src, q31_t offset, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

为 Q31 向量加上常量偏移（Constant Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] offset` | 要加上的偏移量（Offset）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q31 范围 `[0x80000000 0x7FFFFFFF]` 的结果进行饱和处理。

<a id="ga701b8bbd1437e0f19807c38fd4d0e7e9"></a>

### `zdsp_offset_q7()`

```c
void zdsp_offset_q7 ( const q7_t * src, q7_t offset, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

为 Q7 向量加上常量偏移（Constant Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] offset` | 要加上的偏移量（Offset）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q7 范围 `[0x80 0x7F]` 的结果进行饱和处理。


## 8.3\_原页交叉引用（Cross References）

- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)
- [zephyr/dsp/basicmath_f16.h](../api_file_service_interface_reference/P008_zephyr__dsp__basicmath_f16.h_文件参考.md)
- [zephyr/dsp/basicmath.h](../api_file_service_interface_reference/P007_zephyr__dsp__basicmath.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_LIS2DU12 API主题.md) · [返回大纲](大纲.md) · [下一章](P009_向量缩放（Vector Scale）.md)
