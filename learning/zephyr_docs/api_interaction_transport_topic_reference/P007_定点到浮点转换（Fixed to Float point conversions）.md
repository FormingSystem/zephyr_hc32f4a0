---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-7
title: 定点到浮点转换（Fixed to Float point conversions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_定点到浮点转换（Fixed to Float point conversions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过移位将 Q7/Q15/Q31 数值转换为 Float 或 Double 表示。

<a id="details"></a>

通过移位（Shift）将 Q7/Q15/Q31 定点数转换为 Float 或 Double 浮点表示。浮点、Q7、Q15 和 Q31 数据类型各有独立函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.1\_函数（Functions）

<a id="r_ga1f3f2c495cc243c66d23431b97c0acdb"></a>

```c
static float32_t zdsp_q7_to_f32_shift (q7_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q7_to_f32_shift](#ga1f3f2c495cc243c66d23431b97c0acdb)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga5b48f9416c2f5305fb5bc17db6e51e37"></a>

```c
static float32_t zdsp_q15_to_f32_shift (q15_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q15_to_f32_shift](#ga5b48f9416c2f5305fb5bc17db6e51e37)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga7ecfaad745f108899d21d4e508e05cfd"></a>

```c
static float32_t zdsp_q31_to_f32_shift (q31_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q31_to_f32_shift](#ga7ecfaad745f108899d21d4e508e05cfd)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga27cf1582b219e1d5522d32081b1faedd"></a>

```c
static float64_t zdsp_q7_to_f64_shift (q7_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q7_to_f64_shift](#ga27cf1582b219e1d5522d32081b1faedd)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

<a id="r_gabdca080c25364e463c5ded433b27f9be"></a>

```c
static float64_t zdsp_q15_to_f64_shift (q15_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q15_to_f64_shift](#gabdca080c25364e463c5ded433b27f9be)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

<a id="r_gad764039dcc24a76dfc859df54620dd65"></a>

```c
static float64_t zdsp_q31_to_f64_shift (q31_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q31_to_f64_shift](#gad764039dcc24a76dfc859df54620dd65)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

## 7.2\_详细说明（Detailed Documentation）

<a id="ga5b48f9416c2f5305fb5bc17db6e51e37"></a>

### `zdsp_q15_to_f32_shift()`

```c
float32_t zdsp_q15_to_f32_shift ( q15_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q15 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–15。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float32_t`。

<a id="gabdca080c25364e463c5ded433b27f9be"></a>

### `zdsp_q15_to_f64_shift()`

```c
float64_t zdsp_q15_to_f64_shift ( q15_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q15 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–15。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float64_t`。

<a id="ga7ecfaad745f108899d21d4e508e05cfd"></a>

### `zdsp_q31_to_f32_shift()`

```c
float32_t zdsp_q31_to_f32_shift ( q31_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q31 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–31。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float32_t`。

<a id="gad764039dcc24a76dfc859df54620dd65"></a>

### `zdsp_q31_to_f64_shift()`

```c
float64_t zdsp_q31_to_f64_shift ( q31_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q31 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–31。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float64_t`。

<a id="ga1f3f2c495cc243c66d23431b97c0acdb"></a>

### `zdsp_q7_to_f32_shift()`

```c
float32_t zdsp_q7_to_f32_shift ( q7_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q7 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–7。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float32_t`。

<a id="ga27cf1582b219e1d5522d32081b1faedd"></a>

### `zdsp_q7_to_f64_shift()`

```c
float64_t zdsp_q7_to_f64_shift ( q7_t src, uint32_t m )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/dsp/utils.h>
```

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 输入的 Q7 定点值（Fixed-point Value）。 |
| `m` | 输入值左移（Left Shift）的位数，范围为 0–7。 |

**返回（Returns）**：**返回值（Returns）：**转换后的浮点值（Floating-point Value），类型为 `float64_t`。


## 7.3\_原页交叉引用（Cross References）

- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)
- [zephyr/dsp/utils.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_浮点到定点转换（Float to Fixed point conversions）.md) · [返回大纲](大纲.md) · [下一章](P008_Microchip NVMCTRL G1 API主题.md)
