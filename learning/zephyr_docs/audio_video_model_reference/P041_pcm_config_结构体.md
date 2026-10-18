---
id: learning.zephyr-docs.audio-video-model-reference.page-41
title: pcm_config_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcm__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_pcm\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcm__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

脉冲编码调制（PCM）的配置选项。

```c
#include <zephyr/audio/codec.h>
```

<a id="details"></a>

脉冲编码调制（PCM）的配置选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a2e6b978dd1795d400076bd7ba0812f02"></a>

```c
audio_dai_dir_t dir
```

相关声明：[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)、[dir](#a2e6b978dd1795d400076bd7ba0812f02)。

脉冲编码调制（PCM）方向。

<a id="r_a9c9d58e429f9f9198d22a8437c8373e3"></a>

```c
audio_pcm_width_t pcm_width
```

相关声明：[audio_pcm_width_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga1898dae0fac2e2bf34596453037bff7e)、[pcm_width](#a9c9d58e429f9f9198d22a8437c8373e3)。

表示一个数据字的位数。

<a id="r_ad0ad9c1e8c8af0016415f98a7fa0d69e"></a>

```c
uint8_t channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channels](#ad0ad9c1e8c8af0016415f98a7fa0d69e)。

每帧的通道数量。

<a id="r_aacad2be27111d146ad046ad048672f72"></a>

```c
size_t block_size
```

相关声明：[block_size](#aacad2be27111d146ad046ad048672f72)。

单个 RX/TX 内存块或缓冲区的大小，单位为字节。为满足某些 DMA 限制，应为 4 的整数倍。

<a id="r_ab1f1dd56e25317c3caaeb6206f07a211"></a>

```c
audio_pcm_rate_t samplerate
```

相关声明：[audio_pcm_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga8fd2079e6128c8a6da59c2dee58101ca)、[samplerate](#ab1f1dd56e25317c3caaeb6206f07a211)。

PCM 采样率（sample rate）。

## 41.2\_详细说明（Detailed Documentation）

<a id="aacad2be27111d146ad046ad048672f72"></a>

### `block_size`

```c
size_t pcm_config::block_size
```

单个 RX/TX 内存块或缓冲区的大小，单位为字节。为满足某些 DMA 限制，应为 4 的整数倍。

<a id="ad0ad9c1e8c8af0016415f98a7fa0d69e"></a>

### `channels`

```c
uint8_t pcm_config::channels
```

每帧的通道数量。

<a id="a2e6b978dd1795d400076bd7ba0812f02"></a>

### `dir`

```c
audio_dai_dir_t pcm_config::dir
```

脉冲编码调制（PCM）方向。

<a id="a9c9d58e429f9f9198d22a8437c8373e3"></a>

### `pcm_width`

```c
audio_pcm_width_t pcm_config::pcm_width
```

表示一个数据字的位数。

<a id="ab1f1dd56e25317c3caaeb6206f07a211"></a>

### `samplerate`

```c
audio_pcm_rate_t pcm_config::samplerate
```

PCM 采样率（sample rate）。

本数据类型文档由以下文件生成：

- `zephyr/audio/codec.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/audio/codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h_source.html)
- [audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)
- [audio_pcm_width_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga1898dae0fac2e2bf34596453037bff7e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [audio_pcm_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga8fd2079e6128c8a6da59c2dee58101ca)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_mpl_search_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_pcm_stream_cfg_结构体.md)
