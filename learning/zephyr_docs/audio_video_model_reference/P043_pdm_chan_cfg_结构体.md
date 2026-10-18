---
id: learning.zephyr-docs.audio-video-model-reference.page-43
title: pdm_chan_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpdm__chan__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_pdm\_chan\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpdm__chan__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PDM通道到逻辑PCM输出通道的映射/排列（Mapping / Ordering）。

```c
#include <zephyr/audio/dmic.h>
```

<a id="details"></a>

PDM 通道到逻辑 PCM 输出通道的映射或排列。每个控制器可有 2 个音频通道（立体声），因此最多可有 `8 × 2 = 16` 个通道。实际通道数必须在 `act_num_chan` 中说明。如果启用 2 个流，两个流的通道顺序相同。每个通道用一个 4 位数表示，最低有效位指示选择该 PDM 控制器的左或右（LEFT/RIGHT）通道，最高的 3 位指示 PDM 控制器编号：位 0 至 3 对应通道 0，其中位 0 指示左或右；位 4 至 7 对应通道 1，其中位 4 指示左或右；依此类推。限制：每个 PDM 控制器的左、右通道必须彼此相邻。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_aa2518c6f577c3fd92ec009fa134a6185"></a>

```c
uint8_t req_num_chan
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[req_num_chan](#aa2518c6f577c3fd92ec009fa134a6185)。

请求的通道数量。

<a id="r_a3268169aaee14827cb15778fbc44ceb1"></a>

```c
uint8_t act_num_chan
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[act_num_chan](#a3268169aaee14827cb15778fbc44ceb1)。

驱动实际能够配置的通道数量。

<a id="r_ae1398759382606cc60cf8944a1b9e5f6"></a>

```c
uint8_t req_num_streams
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[req_num_streams](#ae1398759382606cc60cf8944a1b9e5f6)。

每个通道请求的流数量。

<a id="r_a7614fefd7976ba7b195afb4e81f7100e"></a>

```c
uint8_t act_num_streams
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[act_num_streams](#a7614fefd7976ba7b195afb4e81f7100e)。

驱动实际能够配置的流数量。

<a id="pub-attribs-0"></a>

### 请求的通道映射（Requested channel map）

<a id="r_a028c8cd3dfcf0bfce618ef8937a7b211"></a>

```c
uint32_t req_chan_map_lo
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[req_chan_map_lo](#a028c8cd3dfcf0bfce618ef8937a7b211)。

通道 0 至 7。

<a id="r_a11a258f6b21126e1d50c5a3f46b2cad7"></a>

```c
uint32_t req_chan_map_hi
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[req_chan_map_hi](#a11a258f6b21126e1d50c5a3f46b2cad7)。

通道 8 至 15。

<a id="pub-attribs-1"></a>

### 驱动实际能够配置的通道映射（Actual channel map that the driver could configure）

<a id="r_a34d2e2d03df48e26245835d4df88b60b"></a>

```c
uint32_t act_chan_map_lo
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[act_chan_map_lo](#a34d2e2d03df48e26245835d4df88b60b)。

通道 0 至 7。

<a id="r_a9a91e9341f4c033243effbebd5ffa194"></a>

```c
uint32_t act_chan_map_hi
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[act_chan_map_hi](#a9a91e9341f4c033243effbebd5ffa194)。

通道 8 至 15。

## 43.2\_详细说明（Detailed Documentation）

<a id="a9a91e9341f4c033243effbebd5ffa194"></a>

### `act_chan_map_hi`

```c
uint32_t pdm_chan_cfg::act_chan_map_hi
```

通道 8 至 15。

<a id="a34d2e2d03df48e26245835d4df88b60b"></a>

### `act_chan_map_lo`

```c
uint32_t pdm_chan_cfg::act_chan_map_lo
```

通道 0 至 7。

<a id="a3268169aaee14827cb15778fbc44ceb1"></a>

### `act_num_chan`

```c
uint8_t pdm_chan_cfg::act_num_chan
```

驱动实际能够配置的通道数量。

<a id="a7614fefd7976ba7b195afb4e81f7100e"></a>

### `act_num_streams`

```c
uint8_t pdm_chan_cfg::act_num_streams
```

驱动实际能够配置的流数量。

<a id="a11a258f6b21126e1d50c5a3f46b2cad7"></a>

### `req_chan_map_hi`

```c
uint32_t pdm_chan_cfg::req_chan_map_hi
```

通道 8 至 15。

<a id="a028c8cd3dfcf0bfce618ef8937a7b211"></a>

### `req_chan_map_lo`

```c
uint32_t pdm_chan_cfg::req_chan_map_lo
```

通道 0 至 7。

<a id="aa2518c6f577c3fd92ec009fa134a6185"></a>

### `req_num_chan`

```c
uint8_t pdm_chan_cfg::req_num_chan
```

请求的通道数量。

<a id="ae1398759382606cc60cf8944a1b9e5f6"></a>

### `req_num_streams`

```c
uint8_t pdm_chan_cfg::req_num_streams
```

每个通道请求的流数量。

本数据类型文档由以下文件生成：

- `zephyr/audio/dmic.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_pcm_stream_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_pdm_io_cfg_结构体.md)
