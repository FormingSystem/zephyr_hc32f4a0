---
id: learning.zephyr-docs.audio-video-model-reference.page-1
title: dai_config_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdai__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_dai\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdai__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字音频接口（DAI）的主配置结构。

```c
#include <zephyr/drivers/dai.h>
```

<a id="details"></a>

主要数字音频接口（DAI）配置结构体，提供通用 DAI 接口配置选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_acfb621417b789c71608ad50d0b54c1f6"></a>

```c
enum dai_type type
```

相关声明：[dai_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac95242d83a2c2b477fcb9eb3da420797)、[type](#acfb621417b789c71608ad50d0b54c1f6)。

数字音频接口（DAI）的类型。

<a id="r_aecb9fe475d71d55d8b19eb3faa697606"></a>

```c
uint32_t dai_index
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dai_index](#aecb9fe475d71d55d8b19eb3faa697606)。

DAI 的索引。

<a id="r_ac3f39c351ad9659356ad5ad4306585b8"></a>

```c
uint8_t channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channels](#ac3f39c351ad9659356ad5ad4306585b8)。

音频通道数，即每帧的字数。

<a id="r_a2d46087a3c94845d52b44386dd20cfc0"></a>

```c
uint32_t rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rate](#a2d46087a3c94845d52b44386dd20cfc0)。

帧时钟（WS）频率，即采样率（sampling rate）。

<a id="r_ac2c2c4a39bfe917d5a784d8bc596eb10"></a>

```c
uint16_t format
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[format](#ac2c2c4a39bfe917d5a784d8bc596eb10)。

DAI 专用的数据流格式。

<a id="r_ac8b2936e194421f95d03e1c595017306"></a>

```c
uint8_t options
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[options](#ac8b2936e194421f95d03e1c595017306)。

DAI 专用的配置选项。

<a id="r_afe7ab1b6c1163ca1bf4141bc6f2439ba"></a>

```c
uint8_t word_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[word_size](#afe7ab1b6c1163ca1bf4141bc6f2439ba)。

表示一个数据字的位数。

<a id="r_af3c768d9597298cea94bbdd6e5b5c4f3"></a>

```c
size_t block_size
```

相关声明：[block_size](#af3c768d9597298cea94bbdd6e5b5c4f3)。

单个接收/发送（RX/TX）内存块或缓冲区的大小，单位为字节。

<a id="r_afd3bcee428b5359b7151a269973049a1"></a>

```c
uint16_t link_config
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[link_config](#afd3bcee428b5359b7151a269973049a1)。

DAI 专用的链路配置。

<a id="r_a32830675c7bf7125c5006579d33e5e96"></a>

```c
uint32_t tdm_slot_group
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tdm_slot_group](#a32830675c7bf7125c5006579d33e5e96)。

时分复用（TDM）时隙组编号。

## 1.2\_详细说明（Detailed Documentation）

<a id="af3c768d9597298cea94bbdd6e5b5c4f3"></a>

### `block_size`

```c
size_t dai_config::block_size
```

单个接收/发送（RX/TX）内存块或缓冲区的大小，单位为字节。

<a id="ac3f39c351ad9659356ad5ad4306585b8"></a>

### `channels`

```c
uint8_t dai_config::channels
```

音频通道数，即每帧的字数。

<a id="aecb9fe475d71d55d8b19eb3faa697606"></a>

### `dai_index`

```c
uint32_t dai_config::dai_index
```

DAI 的索引。

<a id="ac2c2c4a39bfe917d5a784d8bc596eb10"></a>

### `format`

```c
uint16_t dai_config::format
```

DAI 专用的数据流格式。

<a id="afd3bcee428b5359b7151a269973049a1"></a>

### `link_config`

```c
uint16_t dai_config::link_config
```

DAI 专用的链路配置。

<a id="ac8b2936e194421f95d03e1c595017306"></a>

### `options`

```c
uint8_t dai_config::options
```

DAI 专用的配置选项。

<a id="a2d46087a3c94845d52b44386dd20cfc0"></a>

### `rate`

```c
uint32_t dai_config::rate
```

帧时钟（WS）频率，即采样率（sampling rate）。

<a id="a32830675c7bf7125c5006579d33e5e96"></a>

### `tdm_slot_group`

```c
uint32_t dai_config::tdm_slot_group
```

时分复用（TDM）时隙组编号。

<a id="acfb621417b789c71608ad50d0b54c1f6"></a>

### `type`

```c
enum dai_type dai_config::type
```

数字音频接口（DAI）的类型。

<a id="afe7ab1b6c1163ca1bf4141bc6f2439ba"></a>

### `word_size`

```c
uint8_t dai_config::word_size
```

表示一个数据字的位数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dai.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dai.h](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)
- [dai_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac95242d83a2c2b477fcb9eb3da420797)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_dai_driver_api_结构体.md)
