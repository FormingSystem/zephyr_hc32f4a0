---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-6
title: 浮点到定点转换（Float to Fixed point conversions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_浮点到定点转换（Float to Fixed point conversions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将 Float 或 Double 数值表示转换为 Q31/Q15/Q7 表示。

<a id="details"></a>

将 Float 或 Double 浮点表示转换为 Q31/Q15/Q7 定点表示（Fixed-point Representation）。浮点、Q7、Q15 和 Q31 数据类型各有独立函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.1\_函数（Functions）

<a id="r_ga9c8d709286fe9be34bd5d156bb7ff54b"></a>

```c
static q7_t zdsp_f32_to_q7_shift (float32_t src, uint32_t m)
```

相关声明：[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[zdsp_f32_to_q7_shift](#ga9c8d709286fe9be34bd5d156bb7ff54b)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q7 定点值（Fixed-point Value）。

<a id="r_ga0f8cf55569dddb741d7e21bda192c618"></a>

```c
static q15_t zdsp_f32_to_q15_shift (float32_t src, uint32_t m)
```

相关声明：[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[zdsp_f32_to_q15_shift](#ga0f8cf55569dddb741d7e21bda192c618)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q15 定点值（Fixed-point Value）。

<a id="r_ga8970f2c9068f2efc3afb04998d0b0d9c"></a>

```c
static q31_t zdsp_f32_to_q31_shift (float32_t src, uint32_t m)
```

相关声明：[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[zdsp_f32_to_q31_shift](#ga8970f2c9068f2efc3afb04998d0b0d9c)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q31 定点值（Fixed-point Value）。

<a id="r_gaf683e782aab7cd7beea33d5322f6f4d7"></a>

```c
static q7_t zdsp_f64_to_q7_shift (float64_t src, uint32_t m)
```

相关声明：[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[zdsp_f64_to_q7_shift](#gaf683e782aab7cd7beea33d5322f6f4d7)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q7 定点值（Fixed-point Value）。

<a id="r_gab2152a9a007d7bd7106567bef08bfee0"></a>

```c
static q15_t zdsp_f64_to_q15_shift (float64_t src, uint32_t m)
```

相关声明：[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[zdsp_f64_to_q15_shift](#gab2152a9a007d7bd7106567bef08bfee0)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q15 定点值（Fixed-point Value）。

<a id="r_ga6e06a7f19486f15447cccfc7dcd932e7"></a>

```c
static q31_t zdsp_f64_to_q31_shift (float64_t src, uint32_t m)
```

相关声明：[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[zdsp_f64_to_q31_shift](#ga6e06a7f19486f15447cccfc7dcd932e7)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q31 定点值（Fixed-point Value）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ga0f8cf55569dddb741d7e21bda192c618"></a>

### `zdsp_f32_to_q15_shift()`

```c
q15_t zdsp_f32_to_q15_shift ( float32_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q15 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float32_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–15。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q15 定点值（Fixed-point Value）。

<a id="ga8970f2c9068f2efc3afb04998d0b0d9c"></a>

### `zdsp_f32_to_q31_shift()`

```c
q31_t zdsp_f32_to_q31_shift ( float32_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q31 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float32_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–31。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q31 定点值（Fixed-point Value）。

<a id="ga9c8d709286fe9be34bd5d156bb7ff54b"></a>

### `zdsp_f32_to_q7_shift()`

```c
q7_t zdsp_f32_to_q7_shift ( float32_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q7 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float32_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–7。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q7 定点值（Fixed-point Value）。

<a id="gab2152a9a007d7bd7106567bef08bfee0"></a>

### `zdsp_f64_to_q15_shift()`

```c
q15_t zdsp_f64_to_q15_shift ( float64_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q15 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float64_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–15。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q15 定点值（Fixed-point Value）。

<a id="ga6e06a7f19486f15447cccfc7dcd932e7"></a>

### `zdsp_f64_to_q31_shift()`

```c
q31_t zdsp_f64_to_q31_shift ( float64_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q31 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float64_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–31。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q31 定点值（Fixed-point Value）。

<a id="gaf683e782aab7cd7beea33d5322f6f4d7"></a>

### `zdsp_f64_to_q7_shift()`

```c
q7_t zdsp_f64_to_q7_shift ( float64_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q7 定点值（Fixed-point Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入浮点值（Floating-point Value），类型为 `float64_t`。 |
| `m` | 输入值右移（Right Shift）的位数，范围为 0–7。 |

**返回（Returns）**：**返回值（Returns）：**转换后的 Q7 定点值（Fixed-point Value）。


## 6.3\_原页交叉引用（Cross References）

- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)
- [zephyr/dsp/utils.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_LVGL 键盘按键（Keypad keys）.md) · [返回大纲](大纲.md) · [下一章](P007_定点到浮点转换（Fixed to Float point conversions）.md)
