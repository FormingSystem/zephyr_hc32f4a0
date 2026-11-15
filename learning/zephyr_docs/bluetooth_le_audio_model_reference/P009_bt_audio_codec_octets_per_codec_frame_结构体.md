---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-9
title: bt_audio_codec_octets_per_codec_frame_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__octets__per__codec__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_bt\_audio\_codec\_octets\_per\_codec\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__octets__per__codec__frame.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存所支持编解码器帧大小的最小值和最大值的结构体。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

<a id="details"></a>

保存所支持编解码器帧大小的最小值和最大值的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_aa8b234fa137273cd16230ebabc5f8ef4"></a>

```c
uint16_t min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min](#aa8b234fa137273cd16230ebabc5f8ef4)。

每个编解码器帧支持的最少八位字节（Octets）数。

<a id="r_ae09686799077b13e78b856b1e7e63b6a"></a>

```c
uint16_t max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max](#ae09686799077b13e78b856b1e7e63b6a)。

每个编解码器帧支持的最多八位字节数。

## 9.2\_详细说明（Detailed Documentation）

<a id="ae09686799077b13e78b856b1e7e63b6a"></a>

### `max`

```c
uint16_t bt_audio_codec_octets_per_codec_frame::max
```

每个编解码器帧支持的最多八位字节数。

<a id="aa8b234fa137273cd16230ebabc5f8ef4"></a>

### `min`

```c
uint16_t bt_audio_codec_octets_per_codec_frame::min
```

每个编解码器帧支持的最少八位字节（Octets）数。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/audio.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_bt_audio_codec_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_bt_bap_ascs_rsp_结构体.md)
