---
id: learning.zephyr-docs.audio-video-model-reference.page-6
title: dmic_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdmic__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_dmic\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdmic__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字麦克风（DMIC）配置API的输入配置结构。

```c
#include <zephyr/audio/dmic.h>
```

<a id="details"></a>

数字麦克风（DMIC）配置API的输入配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_abac7595e0a03cf976d8359a86259f54b"></a>

```c
struct pdm_io_cfg io
```

相关声明：[pdm_io_cfg](P044_pdm_io_cfg_结构体.md)、[io](#abac7595e0a03cf976d8359a86259f54b)。

脉冲密度调制（PDM）接口配置。

<a id="r_a90f08070236a8e2c07c30edc54c687a5"></a>

```c
struct pcm_stream_cfg * streams
```

相关声明：[pcm_stream_cfg](P042_pcm_stream_cfg_结构体.md)、[streams](#a90f08070236a8e2c07c30edc54c687a5)。

`pcm_stream_cfg` 数组，供应用为每个流提供配置。

<a id="r_aaef2d2b475ce65d18c48d60cd1d393c4"></a>

```c
struct pdm_chan_cfg channel
```

相关声明：[pdm_chan_cfg](P043_pdm_chan_cfg_结构体.md)、[channel](#aaef2d2b475ce65d18c48d60cd1d393c4)。

PDM 通道配置。

## 6.2\_详细说明（Detailed Documentation）

<a id="aaef2d2b475ce65d18c48d60cd1d393c4"></a>

### `channel`

```c
struct pdm_chan_cfg dmic_cfg::channel
```

PDM 通道配置。

<a id="abac7595e0a03cf976d8359a86259f54b"></a>

### `io`

```c
struct pdm_io_cfg dmic_cfg::io
```

脉冲密度调制（PDM）接口配置。

<a id="a90f08070236a8e2c07c30edc54c687a5"></a>

### `streams`

```c
struct pcm_stream_cfg* dmic_cfg::streams
```

`pcm_stream_cfg` 数组，供应用为每个流提供配置。

本数据类型文档由以下文件生成：

- `zephyr/audio/dmic.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)
- [pdm_io_cfg](P044_pdm_io_cfg_结构体.md)
- [pcm_stream_cfg](P042_pcm_stream_cfg_结构体.md)
- [pdm_chan_cfg](P043_pdm_chan_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_dai_ts_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_dmic_driver_api_结构体.md)
