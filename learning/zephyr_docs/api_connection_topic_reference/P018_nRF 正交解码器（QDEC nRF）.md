---
id: learning.zephyr-docs.api-connection-topic-reference.page-18
title: nRF 正交解码器（QDEC nRF）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nrf__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_nRF 正交解码器（QDEC nRF）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nrf__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nordic nRF 正交解码器（Quadrature decoder，QDEC）。

<a id="details"></a>

Nordic nRF 正交解码器（Quadrature decoder，QDEC）。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_qdec_5Fnrf_2Eh"></a>

```c
file qdec_nrf.h
```

相关声明：[qdec_nrf.h](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nrf_8h.html)。

the Nordic nRF quadrature decoder的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.2\_采样周期选项（Sample period options）

设备树 `nordic,period` 属性的取值。

<a id="r_ga6e734f54de8fd8a7765d2eff2aa71ad6"></a>

```c
#define SAMPLEPER_128US 0
```

相关声明：[SAMPLEPER_128US](#ga6e734f54de8fd8a7765d2eff2aa71ad6)。

时间：128 μs。

<a id="r_gaca2a137bd93652abb6afb9f39c647aa8"></a>

```c
#define SAMPLEPER_256US 1
```

相关声明：[SAMPLEPER_256US](#gaca2a137bd93652abb6afb9f39c647aa8)。

时间：256 μs。

<a id="r_gaf4865f5b4646e2c4f1f9bc81286315ef"></a>

```c
#define SAMPLEPER_512US 2
```

相关声明：[SAMPLEPER_512US](#gaf4865f5b4646e2c4f1f9bc81286315ef)。

时间：512 μs。

<a id="r_gadf0f49c0c0ca99384b7b86dfa735bcb7"></a>

```c
#define SAMPLEPER_1024US 3
```

相关声明：[SAMPLEPER_1024US](#gadf0f49c0c0ca99384b7b86dfa735bcb7)。

时间：1024 μs。

<a id="r_gacebae5cf70e180fea44206b9d1642035"></a>

```c
#define SAMPLEPER_2048US 4
```

相关声明：[SAMPLEPER_2048US](#gacebae5cf70e180fea44206b9d1642035)。

时间：2048 μs。

<a id="r_ga353332f83456b8ff0f26b018228282f0"></a>

```c
#define SAMPLEPER_4096US 5
```

相关声明：[SAMPLEPER_4096US](#ga353332f83456b8ff0f26b018228282f0)。

时间：4096 μs。

<a id="r_ga431971098fa5de1be19bcb284e6ffbd7"></a>

```c
#define SAMPLEPER_8192US 6
```

相关声明：[SAMPLEPER_8192US](#ga431971098fa5de1be19bcb284e6ffbd7)。

时间：8192 μs。

<a id="r_gad0a9d6e40f704e15ac5a3ef6bb4a40f5"></a>

```c
#define SAMPLEPER_16384US 7
```

相关声明：[SAMPLEPER_16384US](#gad0a9d6e40f704e15ac5a3ef6bb4a40f5)。

时间：16384 μs。

## 18.3\_详细说明（Detailed Documentation）

<a id="gadf0f49c0c0ca99384b7b86dfa735bcb7"></a>

### `SAMPLEPER_1024US`

```c
#define SAMPLEPER_1024US 3
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：1024 μs。

<a id="ga6e734f54de8fd8a7765d2eff2aa71ad6"></a>

### `SAMPLEPER_128US`

```c
#define SAMPLEPER_128US 0
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：128 μs。

<a id="gad0a9d6e40f704e15ac5a3ef6bb4a40f5"></a>

### `SAMPLEPER_16384US`

```c
#define SAMPLEPER_16384US 7
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：16384 μs。

<a id="gacebae5cf70e180fea44206b9d1642035"></a>

### `SAMPLEPER_2048US`

```c
#define SAMPLEPER_2048US 4
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：2048 μs。

<a id="gaca2a137bd93652abb6afb9f39c647aa8"></a>

### `SAMPLEPER_256US`

```c
#define SAMPLEPER_256US 1
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：256 μs。

<a id="ga353332f83456b8ff0f26b018228282f0"></a>

### `SAMPLEPER_4096US`

```c
#define SAMPLEPER_4096US 5
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：4096 μs。

<a id="gaf4865f5b4646e2c4f1f9bc81286315ef"></a>

### `SAMPLEPER_512US`

```c
#define SAMPLEPER_512US 2
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：512 μs。

<a id="ga431971098fa5de1be19bcb284e6ffbd7"></a>

### `SAMPLEPER_8192US`

```c
#define SAMPLEPER_8192US 6
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nrf.h>
```

时间：8192 μs。


## 18.4\_原页交叉引用（Cross References）

- [qdec_nrf.h](https://docs.zephyrproject.org/latest/doxygen/html/qdec__nrf_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_网络主机名库（Network Hostname Library）.md) · [返回大纲](大纲.md) · [下一章](P019_NXP 系统电源协议（NXP System Power Protocol）.md)
