---
id: learning.zephyr-docs.audio-video-model-reference.page-3
title: dai_properties_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdai__properties.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_dai\_properties\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdai__properties.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（DAI）的属性。

```c
#include <zephyr/drivers/dai.h>
```

<a id="details"></a>

DAI 属性（properties）。此结构体配合 API 的 `get_properties` 函数使用，用于查询 DAI 属性，例如 FIFO 地址和 DMA 握手信息。例如，在驱动代码之外配置 DMA 时，就需要这些信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a98053c85634b80b144bda05d83f2eb7e"></a>

```c
uint32_t fifo_address
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fifo_address](#a98053c85634b80b144bda05d83f2eb7e)。

FIFO 硬件地址，例如用于下文所述的连接场景。

<a id="r_a9b056f0ff59b473d3040851642d1601c"></a>

```c
uint32_t fifo_depth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fifo_depth](#a9b056f0ff59b473d3040851642d1601c)。

FIFO 深度。

<a id="r_a7203f5c97aaf8f48f9eb51d88424afce"></a>

```c
uint32_t dma_hs_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_hs_id](#a7203f5c97aaf8f48f9eb51d88424afce)。

DMA 握手 ID（handshake ID）。

<a id="r_a8fc2d359fe889b3a46ecc8918a82f680"></a>

```c
uint32_t reg_init_delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reg_init_delay](#a8fc2d359fe889b3a46ecc8918a82f680)。

初始化寄存器所需的延迟。

<a id="r_adab0f1199c7169a521329adc98c2f0ac"></a>

```c
int stream_id
```

相关声明：[stream_id](#adab0f1199c7169a521329adc98c2f0ac)。

流 ID（Stream ID）。

## 3.2\_详细说明（Detailed Documentation）

<a id="a7203f5c97aaf8f48f9eb51d88424afce"></a>

### `dma_hs_id`

```c
uint32_t dai_properties::dma_hs_id
```

DMA 握手 ID（handshake ID）。

<a id="a98053c85634b80b144bda05d83f2eb7e"></a>

### `fifo_address`

```c
uint32_t dai_properties::fifo_address
```

FIFO 硬件地址，例如用于下文所述的连接场景。

连接到 DMA 时使用。

<a id="a9b056f0ff59b473d3040851642d1601c"></a>

### `fifo_depth`

```c
uint32_t dai_properties::fifo_depth
```

FIFO 深度。

<a id="a8fc2d359fe889b3a46ecc8918a82f680"></a>

### `reg_init_delay`

```c
uint32_t dai_properties::reg_init_delay
```

初始化寄存器所需的延迟。

<a id="adab0f1199c7169a521329adc98c2f0ac"></a>

### `stream_id`

```c
int dai_properties::stream_id
```

流 ID（Stream ID）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dai.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dai.h](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_dai_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_dai_ts_cfg_结构体.md)
