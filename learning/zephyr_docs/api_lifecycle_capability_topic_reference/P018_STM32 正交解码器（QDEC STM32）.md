---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-18
title: STM32 正交解码器（QDEC STM32）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__stm32__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_STM32 正交解码器（QDEC STM32）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__stm32__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于 STM32 定时器的正交解码器（Quadrature decoder，QDEC）。

<a id="details"></a>

基于 STM32 定时器的正交解码器（Quadrature decoder，QDEC）。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_qdec_5Fstm32_2Eh"></a>

```c
file qdec_stm32.h
```

相关声明：[qdec_stm32.h](https://docs.zephyrproject.org/latest/doxygen/html/qdec__stm32_8h.html)。

the STM32 quadrature decoder的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.2\_输入滤波器选项（Input Filter Options）

应用于定时器编码器输入（Timer Encoder Inputs）的数字输入滤波器（Digital Input Filter）。

`FDIVx` 选择采样时钟相对于定时器时钟（`fDTS`）的分频比，`Ny` 为确认一次跳变（Transition）所需的连续一致样本（Consecutive Matching Samples）数量。

<a id="r_gaf6083715947fcaa2b78e670d6faeadf3"></a>

```c
#define NO_FILTER 0
```

相关声明：[NO_FILTER](#gaf6083715947fcaa2b78e670d6faeadf3)。

无滤波（No Filter），按 `fDTS` 采样。

<a id="r_gad415ae4093644929aa6d21234b58dd58"></a>

```c
#define FDIV1_N2 1
```

相关声明：[FDIV1_N2](#gad415ae4093644929aa6d21234b58dd58)。

采样频率（Sampling Frequency）为 `fDTS`，2 个样本（Samples）。

<a id="r_gade82dcbdaf332fa244a2cf72e1d7613a"></a>

```c
#define FDIV1_N4 2
```

相关声明：[FDIV1_N4](#gade82dcbdaf332fa244a2cf72e1d7613a)。

采样频率（Sampling Frequency）为 `fDTS`，4 个样本（Samples）。

<a id="r_gae0cef7c8bcd2c97648e6a40c99b44cad"></a>

```c
#define FDIV1_N8 3
```

相关声明：[FDIV1_N8](#gae0cef7c8bcd2c97648e6a40c99b44cad)。

采样频率（Sampling Frequency）为 `fDTS`，8 个样本（Samples）。

<a id="r_ga9cc705fdf1ebbf856b9360d2f38f8eeb"></a>

```c
#define FDIV2_N6 4
```

相关声明：[FDIV2_N6](#ga9cc705fdf1ebbf856b9360d2f38f8eeb)。

采样频率（Sampling Frequency）为 `fDTS / 2`，6 个样本（Samples）。

<a id="r_ga801abb0c889c2d2fdf5607fb264485ee"></a>

```c
#define FDIV2_N8 5
```

相关声明：[FDIV2_N8](#ga801abb0c889c2d2fdf5607fb264485ee)。

采样频率（Sampling Frequency）为 `fDTS / 2`，8 个样本（Samples）。

<a id="r_ga60b2068f901aeabcdc0fc00751d753f5"></a>

```c
#define FDIV4_N6 6
```

相关声明：[FDIV4_N6](#ga60b2068f901aeabcdc0fc00751d753f5)。

采样频率（Sampling Frequency）为 `fDTS / 4`，6 个样本（Samples）。

<a id="r_ga4f2fdb174f0a11c317e2edd513ea8585"></a>

```c
#define FDIV4_N8 7
```

相关声明：[FDIV4_N8](#ga4f2fdb174f0a11c317e2edd513ea8585)。

采样频率（Sampling Frequency）为 `fDTS / 4`，8 个样本（Samples）。

<a id="r_gac5f1cb7032cf39b914b0a31d0f4453df"></a>

```c
#define FDIV8_N6 8
```

相关声明：[FDIV8_N6](#gac5f1cb7032cf39b914b0a31d0f4453df)。

采样频率（Sampling Frequency）为 `fDTS / 8`，6 个样本（Samples）。

<a id="r_gac5a1ac7fe41d29d4435b0bfb0e9e3a43"></a>

```c
#define FDIV8_N8 9
```

相关声明：[FDIV8_N8](#gac5a1ac7fe41d29d4435b0bfb0e9e3a43)。

采样频率（Sampling Frequency）为 `fDTS / 8`，8 个样本（Samples）。

<a id="r_gae692108c36f07899b4511bdeffe9a6fc"></a>

```c
#define FDIV16_N5 10
```

相关声明：[FDIV16_N5](#gae692108c36f07899b4511bdeffe9a6fc)。

采样频率（Sampling Frequency）为 `fDTS / 16`，5 个样本（Samples）。

<a id="r_ga69d57c44e56b45868555d1045cbde98f"></a>

```c
#define FDIV16_N6 11
```

相关声明：[FDIV16_N6](#ga69d57c44e56b45868555d1045cbde98f)。

采样频率（Sampling Frequency）为 `fDTS / 16`，6 个样本（Samples）。

<a id="r_gad3c3cabc17767c6490606f2958c5e705"></a>

```c
#define FDIV16_N8 12
```

相关声明：[FDIV16_N8](#gad3c3cabc17767c6490606f2958c5e705)。

采样频率（Sampling Frequency）为 `fDTS / 16`，8 个样本（Samples）。

<a id="r_gafcc8a34afdf1a09e7ba1b3a263021ad2"></a>

```c
#define FDIV32_N5 13
```

相关声明：[FDIV32_N5](#gafcc8a34afdf1a09e7ba1b3a263021ad2)。

采样频率（Sampling Frequency）为 `fDTS / 32`，5 个样本（Samples）。

<a id="r_ga8d7c2661594400f40d8ebfaf1ef062ca"></a>

```c
#define FDIV32_N6 14
```

相关声明：[FDIV32_N6](#ga8d7c2661594400f40d8ebfaf1ef062ca)。

采样频率（Sampling Frequency）为 `fDTS / 32`，6 个样本（Samples）。

<a id="r_ga58b5f5b2b03ec61a40b3e97c137611d3"></a>

```c
#define FDIV32_N8 15
```

相关声明：[FDIV32_N8](#ga58b5f5b2b03ec61a40b3e97c137611d3)。

采样频率（Sampling Frequency）为 `fDTS / 32`，8 个样本（Samples）。

## 18.3\_详细说明（Detailed Documentation）

<a id="gae692108c36f07899b4511bdeffe9a6fc"></a>

### `FDIV16_N5`

```c
#define FDIV16_N5 10
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 16`，5 个样本（Samples）。

<a id="ga69d57c44e56b45868555d1045cbde98f"></a>

### `FDIV16_N6`

```c
#define FDIV16_N6 11
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 16`，6 个样本（Samples）。

<a id="gad3c3cabc17767c6490606f2958c5e705"></a>

### `FDIV16_N8`

```c
#define FDIV16_N8 12
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 16`，8 个样本（Samples）。

<a id="gad415ae4093644929aa6d21234b58dd58"></a>

### `FDIV1_N2`

```c
#define FDIV1_N2 1
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS`，2 个样本（Samples）。

<a id="gade82dcbdaf332fa244a2cf72e1d7613a"></a>

### `FDIV1_N4`

```c
#define FDIV1_N4 2
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS`，4 个样本（Samples）。

<a id="gae0cef7c8bcd2c97648e6a40c99b44cad"></a>

### `FDIV1_N8`

```c
#define FDIV1_N8 3
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS`，8 个样本（Samples）。

<a id="ga9cc705fdf1ebbf856b9360d2f38f8eeb"></a>

### `FDIV2_N6`

```c
#define FDIV2_N6 4
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 2`，6 个样本（Samples）。

<a id="ga801abb0c889c2d2fdf5607fb264485ee"></a>

### `FDIV2_N8`

```c
#define FDIV2_N8 5
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 2`，8 个样本（Samples）。

<a id="gafcc8a34afdf1a09e7ba1b3a263021ad2"></a>

### `FDIV32_N5`

```c
#define FDIV32_N5 13
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 32`，5 个样本（Samples）。

<a id="ga8d7c2661594400f40d8ebfaf1ef062ca"></a>

### `FDIV32_N6`

```c
#define FDIV32_N6 14
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 32`，6 个样本（Samples）。

<a id="ga58b5f5b2b03ec61a40b3e97c137611d3"></a>

### `FDIV32_N8`

```c
#define FDIV32_N8 15
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 32`，8 个样本（Samples）。

<a id="ga60b2068f901aeabcdc0fc00751d753f5"></a>

### `FDIV4_N6`

```c
#define FDIV4_N6 6
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 4`，6 个样本（Samples）。

<a id="ga4f2fdb174f0a11c317e2edd513ea8585"></a>

### `FDIV4_N8`

```c
#define FDIV4_N8 7
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 4`，8 个样本（Samples）。

<a id="gac5f1cb7032cf39b914b0a31d0f4453df"></a>

### `FDIV8_N6`

```c
#define FDIV8_N6 8
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 8`，6 个样本（Samples）。

<a id="gac5a1ac7fe41d29d4435b0bfb0e9e3a43"></a>

### `FDIV8_N8`

```c
#define FDIV8_N8 9
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

采样频率（Sampling Frequency）为 `fDTS / 8`，8 个样本（Samples）。

<a id="gaf6083715947fcaa2b78e670d6faeadf3"></a>

### `NO_FILTER`

```c
#define NO_FILTER 0
```

```c
#include <zephyr/dt-bindings/sensor/qdec_stm32.h>
```

无滤波（No Filter），按 `fDTS` 采样。


## 18.4\_原页交叉引用（Cross References）

- [qdec_stm32.h](https://docs.zephyrproject.org/latest/doxygen/html/qdec__stm32_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_Raspberry Pi Pico 可编程 I_O（PIO）.md) · [返回大纲](大纲.md) · [下一章](P019_Iclegend S3KM1110 API主题.md)
