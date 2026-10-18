---
id: learning.zephyr-docs.device-power-control-model-reference.page-86
title: sf32lb_dma_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsf32lb__dma__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_sf32lb\_dma\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsf32lb__dma__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SF32LB直接内存访问的设备树规格（DMA DT Spec）。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

<a id="details"></a>

SF32LB直接内存访问的设备树规格（DMA DT Spec）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a4dd872374ab38aa659293c3f9c7a59ce"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a4dd872374ab38aa659293c3f9c7a59ce)。

DMA 控制器。

<a id="r_a801de8d8db3db6879f1c36a2d0bd0d3b"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a801de8d8db3db6879f1c36a2d0bd0d3b)。

DMA 通道。

<a id="r_adee69348348f08787130b786e48c91af"></a>

```c
uint8_t request
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[request](#adee69348348f08787130b786e48c91af)。

DMA 请求。

<a id="r_aa18d2b334d4ad18398a2d557ca3b421b"></a>

```c
uint8_t config
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config](#aa18d2b334d4ad18398a2d557ca3b421b)。

DMA 配置。

## 86.2\_详细说明（Detailed Documentation）

<a id="a801de8d8db3db6879f1c36a2d0bd0d3b"></a>

### `channel`

```c
uint8_t sf32lb_dma_dt_spec::channel
```

DMA 通道。

<a id="aa18d2b334d4ad18398a2d557ca3b421b"></a>

### `config`

```c
uint8_t sf32lb_dma_dt_spec::config
```

DMA 配置。

<a id="a4dd872374ab38aa659293c3f9c7a59ce"></a>

### `dev`

```c
const struct device* sf32lb_dma_dt_spec::dev
```

DMA 控制器。

<a id="adee69348348f08787130b786e48c91af"></a>

### `request`

```c
uint8_t sf32lb_dma_dt_spec::request
```

DMA 请求。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dma/sf32lb.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dma/sf32lb.h](https://docs.zephyrproject.org/latest/doxygen/html/dma_2sf32lb_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_sf32lb_clock_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_silabs_clock_control_cmu_config_结构体.md)
