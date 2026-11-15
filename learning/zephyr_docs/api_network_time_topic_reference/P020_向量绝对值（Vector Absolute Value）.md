---
id: learning.zephyr-docs.api-network-time-topic-reference.page-20
title: 向量绝对值（Vector Absolute Value）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_向量绝对值（Vector Absolute Value）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

逐元素计算向量的绝对值。

<a id="details"></a>

逐元素计算向量的绝对值（absolute value）：`dst[n] = abs(src[n])`，其中 `0 <= n < block_size`。函数支持就地计算（in-place computation），允许源指针和目标指针指向同一内存缓冲区。分别为浮点、Q7、Q15 和 Q31 数据类型提供独立函数。

```c

    dst[n] = abs(src[n]),   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_ga5a5358fb90f726256f064757fbab1bcd"></a>

```c
void zdsp_abs_f32 (const float32_t *src, float32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_f32](#ga5a5358fb90f726256f064757fbab1bcd)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量绝对值（floating-point vector absolute value）。

<a id="r_ga69c38809979de090a3458ec9b31f4cb4"></a>

```c
void zdsp_abs_q7 (const q7_t *src, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q7](#ga69c38809979de090a3458ec9b31f4cb4)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q7 向量绝对值。

<a id="r_ga53ee6bbc05423703f6299fd60c8e1d44"></a>

```c
void zdsp_abs_q15 (const q15_t *src, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q15](#ga53ee6bbc05423703f6299fd60c8e1d44)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q15 向量绝对值。

<a id="r_ga74ccbbaf60257ca482fc96e1d40edeca"></a>

```c
void zdsp_abs_q31 (const q31_t *src, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_q31](#ga74ccbbaf60257ca482fc96e1d40edeca)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

Q31 向量绝对值。

<a id="r_gae1a01c6ab370ebdb6beaf12c02ca5b8d"></a>

```c
void zdsp_abs_f16 (const float16_t *src, float16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_abs_f16](#gae1a01c6ab370ebdb6beaf12c02ca5b8d)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[float16_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gaa94dc44bddb5718a22bb612890a7fe9f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

浮点向量绝对值（floating-point vector absolute value）。

## 20.2\_详细说明（Detailed Documentation）

<a id="gae1a01c6ab370ebdb6beaf12c02ca5b8d"></a>

### `zdsp_abs_f16()`

```c
void zdsp_abs_f16 ( const float16_t * src, float16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath_f16.h>
```

浮点向量绝对值（floating-point vector absolute value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入缓冲区。 |
| `[out] dst` | 指向输出缓冲区。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga5a5358fb90f726256f064757fbab1bcd"></a>

### `zdsp_abs_f32()`

```c
void zdsp_abs_f32 ( const float32_t * src, float32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

浮点向量绝对值（floating-point vector absolute value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入缓冲区。 |
| `[out] dst` | 指向输出缓冲区。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga53ee6bbc05423703f6299fd60c8e1d44"></a>

### `zdsp_abs_q15()`

```c
void zdsp_abs_q15 ( const q15_t * src, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q15 向量绝对值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入缓冲区。 |
| `[out] dst` | 指向输出缓冲区。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：缩放与溢出行为（Scaling and Overflow Behavior）：函数使用饱和算术（saturating arithmetic）。Q15 的 −1（`0x8000`）将饱和到允许的最大正值 `0x7FFF`。

<a id="ga74ccbbaf60257ca482fc96e1d40edeca"></a>

### `zdsp_abs_q31()`

```c
void zdsp_abs_q31 ( const q31_t * src, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q31 向量绝对值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入缓冲区。 |
| `[out] dst` | 指向输出缓冲区。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：缩放与溢出行为（Scaling and Overflow Behavior）：函数使用饱和算术（saturating arithmetic）。Q31 的 −1（`0x80000000`）将饱和到允许的最大正值 `0x7FFFFFFF`。

<a id="ga69c38809979de090a3458ec9b31f4cb4"></a>

### `zdsp_abs_q7()`

```c
void zdsp_abs_q7 ( const q7_t * src, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

Q7 向量绝对值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入缓冲区。 |
| `[out] dst` | 指向输出缓冲区。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

**说明（Note）**：缩放与溢出行为（Scaling and Overflow Behavior）：函数使用饱和算术（saturating arithmetic）。Q7 的 −1（`0x80`）将饱和到允许的最大正值 `0x7F`。


## 20.3\_原页交叉引用（Cross References）

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

[上一章](P019_LSM6DSV32X API主题.md) · [返回大纲](大纲.md) · [下一章](P021_蓝牙传输（Bluetooth transport）.md)
