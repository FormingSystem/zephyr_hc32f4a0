---
id: learning.zephyr-docs.audio-video-model-reference.page-67
title: audio_property_value_t_联合体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionaudio__property__value__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_audio\_property\_value\_t\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionaudio__property__value__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

编解码器属性值（Codec Property Values）。

```c
#include <zephyr/audio/codec.h>
```

<a id="details"></a>

编解码器属性值（Codec Property Values）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_aafcfb98016ab4306b4fd6cb54f0c22e0"></a>

```c
int vol
```

相关声明：[vol](#aafcfb98016ab4306b4fd6cb54f0c22e0)。

音量级别（volume level），具体含义取决于编解码器。

<a id="r_a23e0d9031006d64dfb31d87e4f061dc8"></a>

```c
bool mute
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[mute](#a23e0d9031006d64dfb31d87e4f061dc8)。

为 `true` 时静音，为 `false` 时取消静音。

<a id="r_a70b92e6c426f39e93b7db913e55cd49b"></a>

```c
struct audio_codec_eq_cfg eq
```

相关声明：[audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)、[eq](#a70b92e6c426f39e93b7db913e55cd49b)。

编解码器均衡器（Codec Equalizer）设置。

## 67.2\_详细说明（Detailed Documentation）

<a id="a70b92e6c426f39e93b7db913e55cd49b"></a>

### `eq`

```c
struct audio_codec_eq_cfg audio_property_value_t::eq
```

编解码器均衡器（Codec Equalizer）设置。

<a id="a23e0d9031006d64dfb31d87e4f061dc8"></a>

### `mute`

```c
bool audio_property_value_t::mute
```

为 `true` 时静音，为 `false` 时取消静音。

<a id="aafcfb98016ab4306b4fd6cb54f0c22e0"></a>

### `vol`

```c
int audio_property_value_t::vol
```

音量级别（volume level），具体含义取决于编解码器。

本数据类型文档由以下文件生成：

- `zephyr/audio/codec.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/audio/codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_audio_dai_cfg_t_联合体.md) · [返回大纲](大纲.md) · [下一章](P068_mic_privacy_mask_联合体.md)
