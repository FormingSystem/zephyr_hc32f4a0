---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-19
title: 向量移位（Vector Shift）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_向量移位（Vector Shift）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将定点向量的各元素移位指定的位数。

<a id="details"></a>

将定点向量（Fixed-point Vector）的各元素移动指定的位数。Q7、Q15 和 Q31 数据类型各有独立函数。底层算法如下。`shift` 为正时左移，为负时右移。函数支持原位计算（In-place Computation），允许源指针与目标指针引用同一内存缓冲区。

```c

    dst[n] = src[n] << shift,   0 <= n < block_size.
```

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_ga8eb72ff139c173d3e1794a1d1c1c8fde"></a>

```c
void zdsp_shift_q7 (const q7_t *src, int8_t shift_bits, q7_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q7](#ga8eb72ff139c173d3e1794a1d1c1c8fde)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q7 向量的各元素移动指定的位数。

<a id="r_ga738fc0fe86b9c910a30fceff7dc4a789"></a>

```c
void zdsp_shift_q15 (const q15_t *src, int8_t shift_bits, q15_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q15](#ga738fc0fe86b9c910a30fceff7dc4a789)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q15 向量的各元素移动指定的位数。

<a id="r_gaf9af89a3c76ad385eec0225185b522c9"></a>

```c
void zdsp_shift_q31 (const q31_t *src, int8_t shift_bits, q31_t *dst, uint32_t block_size)
```

相关声明：[zdsp_shift_q31](#gaf9af89a3c76ad385eec0225185b522c9)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 Q31 向量的各元素移动指定的位数。

## 19.2\_详细说明（Detailed Documentation）

<a id="ga738fc0fe86b9c910a30fceff7dc4a789"></a>

### `zdsp_shift_q15()`

```c
void zdsp_shift_q15 ( const q15_t * src, int8_t shift_bits, q15_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q15 向量的各元素移动指定的位数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] shift_bits` | 移动的位数；正值左移（Shift Left），负值右移（Shift Right）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**前置条件（Precondition）／缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q15 范围 `[0x8000 0x7FFF]` 的结果进行饱和处理。

<a id="gaf9af89a3c76ad385eec0225185b522c9"></a>

### `zdsp_shift_q31()`

```c
void zdsp_shift_q31 ( const q31_t * src, int8_t shift_bits, q31_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q31 向量的各元素移动指定的位数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] shift_bits` | 移动的位数；正值左移（Shift Left），负值右移（Shift Right）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q31 范围 `[0x80000000 0x7FFFFFFF]` 的结果进行饱和处理。

<a id="ga8eb72ff139c173d3e1794a1d1c1c8fde"></a>

### `zdsp_shift_q7()`

```c
void zdsp_shift_q7 ( const q7_t * src, int8_t shift_bits, q7_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

将 Q7 向量的各元素移动指定的位数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量（Input Vector）。 |
| `[in] shift_bits` | 移动的位数；正值左移（Shift Left），负值右移（Shift Right）。 |
| `[out] dst` | 指向输出向量（Output Vector）。 |
| `[in] block_size` | 向量中的样本数（Number of Samples）。 |

**说明（Note）**：**缩放与溢出行为（Scaling and Overflow Behavior）：**函数使用饱和算术（Saturating Arithmetic），超出允许的 Q7 范围 `[0x80 0x7F]` 的结果进行饱和处理。


## 19.3\_原页交叉引用（Cross References）

- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_向量取负（Vector Negate）.md) · [返回大纲](大纲.md) · [下一章](P020_向量减法（Vector Subtraction）.md)
