---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-12
title: zephyr__dsp__utils.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_dsp\_\_utils.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字信号处理（DSP）的附加工具函数。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/minmax.h>
#include <zephyr/kernel.h>
#include <zephyr/dsp/types.h>
```

查看此文件的源码。

数字信号处理（DSP）的附加工具函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.1\_函数（Functions）

<a id="r_ga1f3f2c495cc243c66d23431b97c0acdb"></a>

```c
static float32_t zdsp_q7_to_f32_shift (q7_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q7_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga1f3f2c495cc243c66d23431b97c0acdb)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga5b48f9416c2f5305fb5bc17db6e51e37"></a>

```c
static float32_t zdsp_q15_to_f32_shift (q15_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q15_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga5b48f9416c2f5305fb5bc17db6e51e37)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga7ecfaad745f108899d21d4e508e05cfd"></a>

```c
static float32_t zdsp_q31_to_f32_shift (q31_t src, uint32_t m)
```

相关声明：[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[zdsp_q31_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga7ecfaad745f108899d21d4e508e05cfd)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float32_t`。

<a id="r_ga27cf1582b219e1d5522d32081b1faedd"></a>

```c
static float64_t zdsp_q7_to_f64_shift (q7_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q7_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga27cf1582b219e1d5522d32081b1faedd)、[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q7 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

<a id="r_gabdca080c25364e463c5ded433b27f9be"></a>

```c
static float64_t zdsp_q15_to_f64_shift (q15_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q15_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#gabdca080c25364e463c5ded433b27f9be)、[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q15 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

<a id="r_gad764039dcc24a76dfc859df54620dd65"></a>

```c
static float64_t zdsp_q31_to_f64_shift (q31_t src, uint32_t m)
```

相关声明：[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[zdsp_q31_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#gad764039dcc24a76dfc859df54620dd65)、[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过左移（Left Shift）将 Q31 定点值（Fixed-point Value）转换为浮点值 `float64_t`。

<a id="r_ga9c8d709286fe9be34bd5d156bb7ff54b"></a>

```c
static q7_t zdsp_f32_to_q7_shift (float32_t src, uint32_t m)
```

相关声明：[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[zdsp_f32_to_q7_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga9c8d709286fe9be34bd5d156bb7ff54b)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q7 定点值（Fixed-point Value）。

<a id="r_ga0f8cf55569dddb741d7e21bda192c618"></a>

```c
static q15_t zdsp_f32_to_q15_shift (float32_t src, uint32_t m)
```

相关声明：[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[zdsp_f32_to_q15_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga0f8cf55569dddb741d7e21bda192c618)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q15 定点值（Fixed-point Value）。

<a id="r_ga8970f2c9068f2efc3afb04998d0b0d9c"></a>

```c
static q31_t zdsp_f32_to_q31_shift (float32_t src, uint32_t m)
```

相关声明：[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[zdsp_f32_to_q31_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga8970f2c9068f2efc3afb04998d0b0d9c)、[float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float32_t` 转换为 Q31 定点值（Fixed-point Value）。

<a id="r_gaf683e782aab7cd7beea33d5322f6f4d7"></a>

```c
static q7_t zdsp_f64_to_q7_shift (float64_t src, uint32_t m)
```

相关声明：[q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)、[zdsp_f64_to_q7_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#gaf683e782aab7cd7beea33d5322f6f4d7)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q7 定点值（Fixed-point Value）。

<a id="r_gab2152a9a007d7bd7106567bef08bfee0"></a>

```c
static q15_t zdsp_f64_to_q15_shift (float64_t src, uint32_t m)
```

相关声明：[q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)、[zdsp_f64_to_q15_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#gab2152a9a007d7bd7106567bef08bfee0)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q15 定点值（Fixed-point Value）。

<a id="r_ga6e06a7f19486f15447cccfc7dcd932e7"></a>

```c
static q31_t zdsp_f64_to_q31_shift (float64_t src, uint32_t m)
```

相关声明：[q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)、[zdsp_f64_to_q31_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga6e06a7f19486f15447cccfc7dcd932e7)、[float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过右移（Right Shift）将浮点值 `float64_t` 转换为 Q31 定点值（Fixed-point Value）。


## 12.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/minmax.h](../numeric_reference/P002_最小最大值与限幅宏源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P186_utils.h_源码浏览.md)
- [float32_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#ga4611b605e45ab401f02cab15c5e38715)
- [zdsp_q7_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga1f3f2c495cc243c66d23431b97c0acdb)
- [q7_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_q15_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga5b48f9416c2f5305fb5bc17db6e51e37)
- [q15_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gab5a8fb21a5b3b983d5f54f31614052ea)
- [zdsp_q31_to_f32_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga7ecfaad745f108899d21d4e508e05cfd)
- [q31_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gadc89a3547f5324b7b3b95adec3806bc0)
- [float64_t](../api_auxiliary_topic_reference/P009_数字信号处理（Digital Signal Processing，DSP）.md#gac55f3ae81b5bc9053760baacf57e47f4)
- [zdsp_q7_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#ga27cf1582b219e1d5522d32081b1faedd)
- [zdsp_q15_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#gabdca080c25364e463c5ded433b27f9be)
- [zdsp_q31_to_f64_shift](../api_interaction_transport_topic_reference/P007_定点到浮点转换（Fixed to Float point conversions）.md#gad764039dcc24a76dfc859df54620dd65)
- [zdsp_f32_to_q7_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga9c8d709286fe9be34bd5d156bb7ff54b)
- [zdsp_f32_to_q15_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga0f8cf55569dddb741d7e21bda192c618)
- [zdsp_f32_to_q31_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga8970f2c9068f2efc3afb04998d0b0d9c)
- [zdsp_f64_to_q7_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#gaf683e782aab7cd7beea33d5322f6f4d7)
- [zdsp_f64_to_q15_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#gab2152a9a007d7bd7106567bef08bfee0)
- [zdsp_f64_to_q31_shift](../api_interaction_transport_topic_reference/P006_浮点到定点转换（Float to Fixed point conversions）.md#ga6e06a7f19486f15447cccfc7dcd932e7)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__mfd__ds3231.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__net__ethernet_bridge.h_文件参考.md)
