---
id: learning.zephyr-docs.audio-video-model-reference.page-42
title: pcm_stream_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcm__stream__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_pcm\_stream\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcm__stream__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由脉冲密度调制（PDM）硬件输出的PCM流配置。

```c
#include <zephyr/audio/dmic.h>
```

<a id="details"></a>

PDM 硬件输出的 PCM 流配置。注意：如果某个流的 `pcm_rate` 或 `pcm_width` 任一项设为 0，该流将被禁用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_ae6e3790576f910943b0383f4731a5545"></a>

```c
uint32_t pcm_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pcm_rate](#ae6e3790576f910943b0383f4731a5545)。

流的 PCM 采样率。

<a id="r_a7d9fd0039bc25de292f35f60c99c6615"></a>

```c
uint8_t pcm_width
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pcm_width](#a7d9fd0039bc25de292f35f60c99c6615)。

流的 PCM 采样位宽（sample width）。

<a id="r_a3c224ba6f6c6fa7a128a739b6f1c36bf"></a>

```c
uint16_t block_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[block_size](#a3c224ba6f6c6fa7a128a739b6f1c36bf)。

每次传输的 PCM 采样块大小。

<a id="r_a64a94db251a8ff9358040bc23cba6de5"></a>

```c
int8_t gain_db
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[gain_db](#a64a94db251a8ff9358040bc23cba6de5)。

应用到通道的增益（gain），单位为 dB。

<a id="r_ade324dcfe8604fcb94400544ddb4517e"></a>

```c
struct k_mem_slab * mem_slab
```

相关声明：[mem_slab](#ade324dcfe8604fcb94400544ddb4517e)。

供 DMIC 驱动为流分配缓冲区的内存片（SLAB）。

## 42.2\_详细说明（Detailed Documentation）

<a id="a3c224ba6f6c6fa7a128a739b6f1c36bf"></a>

### `block_size`

```c
uint16_t pcm_stream_cfg::block_size
```

每次传输的 PCM 采样块大小。

<a id="a64a94db251a8ff9358040bc23cba6de5"></a>

### `gain_db`

```c
int8_t pcm_stream_cfg::gain_db
```

应用到通道的增益（gain），单位为 dB。

<a id="ade324dcfe8604fcb94400544ddb4517e"></a>

### `mem_slab`

```c
struct k_mem_slab* pcm_stream_cfg::mem_slab
```

供 DMIC 驱动为流分配缓冲区的内存片（SLAB）。

<a id="ae6e3790576f910943b0383f4731a5545"></a>

### `pcm_rate`

```c
uint32_t pcm_stream_cfg::pcm_rate
```

流的 PCM 采样率。

<a id="a7d9fd0039bc25de292f35f60c99c6615"></a>

### `pcm_width`

```c
uint8_t pcm_stream_cfg::pcm_width
```

流的 PCM 采样位宽（sample width）。

本数据类型文档由以下文件生成：

- `zephyr/audio/dmic.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_pcm_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_pdm_chan_cfg_结构体.md)
