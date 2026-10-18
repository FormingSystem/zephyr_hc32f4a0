---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-27
title: zephyr__dt-bindings__sensor__qdec_stm32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qdec__stm32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_dt-bindings\_\_sensor\_\_qdec\_stm32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/qdec__stm32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the STM32 quadrature decoder的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the STM32 quadrature decoder的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输入滤波器选项（Input Filter Options）

应用于定时器编码器输入（Timer Encoder Inputs）的数字输入滤波器（Digital Input Filter）。

`FDIVx` 选择采样时钟相对于定时器时钟（`fDTS`）的分频比，`Ny` 为确认一次跳变（Transition）所需的连续一致样本（Consecutive Matching Samples）数量。

<a id="r_gaf6083715947fcaa2b78e670d6faeadf3"></a>

```c
#define NO_FILTER 0
```

相关声明：[NO_FILTER](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gaf6083715947fcaa2b78e670d6faeadf3)。

无滤波（No Filter），按 `fDTS` 采样。

<a id="r_gad415ae4093644929aa6d21234b58dd58"></a>

```c
#define FDIV1_N2 1
```

相关声明：[FDIV1_N2](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gad415ae4093644929aa6d21234b58dd58)。

采样频率（Sampling Frequency）为 `fDTS`，2 个样本（Samples）。

<a id="r_gade82dcbdaf332fa244a2cf72e1d7613a"></a>

```c
#define FDIV1_N4 2
```

相关声明：[FDIV1_N4](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gade82dcbdaf332fa244a2cf72e1d7613a)。

采样频率（Sampling Frequency）为 `fDTS`，4 个样本（Samples）。

<a id="r_gae0cef7c8bcd2c97648e6a40c99b44cad"></a>

```c
#define FDIV1_N8 3
```

相关声明：[FDIV1_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gae0cef7c8bcd2c97648e6a40c99b44cad)。

采样频率（Sampling Frequency）为 `fDTS`，8 个样本（Samples）。

<a id="r_ga9cc705fdf1ebbf856b9360d2f38f8eeb"></a>

```c
#define FDIV2_N6 4
```

相关声明：[FDIV2_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga9cc705fdf1ebbf856b9360d2f38f8eeb)。

采样频率（Sampling Frequency）为 `fDTS / 2`，6 个样本（Samples）。

<a id="r_ga801abb0c889c2d2fdf5607fb264485ee"></a>

```c
#define FDIV2_N8 5
```

相关声明：[FDIV2_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga801abb0c889c2d2fdf5607fb264485ee)。

采样频率（Sampling Frequency）为 `fDTS / 2`，8 个样本（Samples）。

<a id="r_ga60b2068f901aeabcdc0fc00751d753f5"></a>

```c
#define FDIV4_N6 6
```

相关声明：[FDIV4_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga60b2068f901aeabcdc0fc00751d753f5)。

采样频率（Sampling Frequency）为 `fDTS / 4`，6 个样本（Samples）。

<a id="r_ga4f2fdb174f0a11c317e2edd513ea8585"></a>

```c
#define FDIV4_N8 7
```

相关声明：[FDIV4_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga4f2fdb174f0a11c317e2edd513ea8585)。

采样频率（Sampling Frequency）为 `fDTS / 4`，8 个样本（Samples）。

<a id="r_gac5f1cb7032cf39b914b0a31d0f4453df"></a>

```c
#define FDIV8_N6 8
```

相关声明：[FDIV8_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gac5f1cb7032cf39b914b0a31d0f4453df)。

采样频率（Sampling Frequency）为 `fDTS / 8`，6 个样本（Samples）。

<a id="r_gac5a1ac7fe41d29d4435b0bfb0e9e3a43"></a>

```c
#define FDIV8_N8 9
```

相关声明：[FDIV8_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gac5a1ac7fe41d29d4435b0bfb0e9e3a43)。

采样频率（Sampling Frequency）为 `fDTS / 8`，8 个样本（Samples）。

<a id="r_gae692108c36f07899b4511bdeffe9a6fc"></a>

```c
#define FDIV16_N5 10
```

相关声明：[FDIV16_N5](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gae692108c36f07899b4511bdeffe9a6fc)。

采样频率（Sampling Frequency）为 `fDTS / 16`，5 个样本（Samples）。

<a id="r_ga69d57c44e56b45868555d1045cbde98f"></a>

```c
#define FDIV16_N6 11
```

相关声明：[FDIV16_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga69d57c44e56b45868555d1045cbde98f)。

采样频率（Sampling Frequency）为 `fDTS / 16`，6 个样本（Samples）。

<a id="r_gad3c3cabc17767c6490606f2958c5e705"></a>

```c
#define FDIV16_N8 12
```

相关声明：[FDIV16_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gad3c3cabc17767c6490606f2958c5e705)。

采样频率（Sampling Frequency）为 `fDTS / 16`，8 个样本（Samples）。

<a id="r_gafcc8a34afdf1a09e7ba1b3a263021ad2"></a>

```c
#define FDIV32_N5 13
```

相关声明：[FDIV32_N5](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gafcc8a34afdf1a09e7ba1b3a263021ad2)。

采样频率（Sampling Frequency）为 `fDTS / 32`，5 个样本（Samples）。

<a id="r_ga8d7c2661594400f40d8ebfaf1ef062ca"></a>

```c
#define FDIV32_N6 14
```

相关声明：[FDIV32_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga8d7c2661594400f40d8ebfaf1ef062ca)。

采样频率（Sampling Frequency）为 `fDTS / 32`，6 个样本（Samples）。

<a id="r_ga58b5f5b2b03ec61a40b3e97c137611d3"></a>

```c
#define FDIV32_N8 15
```

相关声明：[FDIV32_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga58b5f5b2b03ec61a40b3e97c137611d3)。

采样频率（Sampling Frequency）为 `fDTS / 32`，8 个样本（Samples）。


## 27.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P690_qdec_stm32.h_源码浏览.md)
- [NO_FILTER](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gaf6083715947fcaa2b78e670d6faeadf3)
- [FDIV1_N2](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gad415ae4093644929aa6d21234b58dd58)
- [FDIV1_N4](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gade82dcbdaf332fa244a2cf72e1d7613a)
- [FDIV1_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gae0cef7c8bcd2c97648e6a40c99b44cad)
- [FDIV2_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga9cc705fdf1ebbf856b9360d2f38f8eeb)
- [FDIV2_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga801abb0c889c2d2fdf5607fb264485ee)
- [FDIV4_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga60b2068f901aeabcdc0fc00751d753f5)
- [FDIV4_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga4f2fdb174f0a11c317e2edd513ea8585)
- [FDIV8_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gac5f1cb7032cf39b914b0a31d0f4453df)
- [FDIV8_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gac5a1ac7fe41d29d4435b0bfb0e9e3a43)
- [FDIV16_N5](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gae692108c36f07899b4511bdeffe9a6fc)
- [FDIV16_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga69d57c44e56b45868555d1045cbde98f)
- [FDIV16_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gad3c3cabc17767c6490606f2958c5e705)
- [FDIV32_N5](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#gafcc8a34afdf1a09e7ba1b3a263021ad2)
- [FDIV32_N6](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga8d7c2661594400f40d8ebfaf1ef062ca)
- [FDIV32_N8](../api_lifecycle_capability_topic_reference/P018_STM32 正交解码器（QDEC STM32）.md#ga58b5f5b2b03ec61a40b3e97c137611d3)

<a id="header-details"></a>

---

[上一章](P026_zephyr__mpipe__mpipe_pad.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__dt-bindings__gpio__renesas-rztn-gpio.h_文件参考.md)
