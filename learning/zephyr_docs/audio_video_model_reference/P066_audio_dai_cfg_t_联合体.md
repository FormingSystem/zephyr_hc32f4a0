---
id: learning.zephyr-docs.audio-video-model-reference.page-66
title: audio_dai_cfg_t_联合体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionaudio__dai__cfg__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_audio\_dai\_cfg\_t\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionaudio__dai__cfg__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（Digital Audio Interface，DAI）配置。

```c
#include <zephyr/audio/codec.h>
```

<a id="details"></a>

数字音频接口配置（Digital Audio Interface Configuration）。具体配置取决于 DAI 类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a18514b2f3b9622ddb24a58d3701d090d"></a>

```c
struct i2s_config i2s
```

相关声明：[i2s_config](P008_i2s_config_结构体.md)、[i2s](#a18514b2f3b9622ddb24a58d3701d090d)。

I2S 配置。

<a id="r_a859ece50501a1c060e20e80f3dc05b95"></a>

```c
struct pcm_config pcm
```

相关声明：[pcm_config](P041_pcm_config_结构体.md)、[pcm](#a859ece50501a1c060e20e80f3dc05b95)。

PCM 配置。

## 66.2\_详细说明（Detailed Documentation）

<a id="a18514b2f3b9622ddb24a58d3701d090d"></a>

### `i2s`

```c
struct i2s_config audio_dai_cfg_t::i2s
```

I2S 配置。

<a id="a859ece50501a1c060e20e80f3dc05b95"></a>

### `pcm`

```c
struct pcm_config audio_dai_cfg_t::pcm
```

PCM 配置。

本数据类型文档由以下文件生成：

- `zephyr/audio/codec.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/audio/codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h_source.html)
- [i2s_config](P008_i2s_config_结构体.md)
- [pcm_config](P041_pcm_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_video_selection_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_audio_property_value_t_联合体.md)
