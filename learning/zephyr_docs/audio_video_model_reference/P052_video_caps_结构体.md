---
id: learning.zephyr-docs.audio-video-model-reference.page-52
title: video_caps_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_video\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频格式能力（Video Format Capabilities）。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频格式能力（Video format capabilities），用于描述视频端点的能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a31520f03f621082bbf516efce23ef1f6"></a>

```c
enum video_buf_type type
```

相关声明：[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)、[type](#a31520f03f621082bbf516efce23ef1f6)。

缓冲区类型。

<a id="r_adb454a88504d9fd6e40510171a53b185"></a>

```c
const struct video_format_cap * format_caps
```

相关声明：[video_format_cap](P060_video_format_cap_结构体.md)、[format_caps](#adb454a88504d9fd6e40510171a53b185)。

视频格式能力列表，以零值终止。

<a id="r_a2b2604a36a2f7a5013d9383ab5ef198a"></a>

```c
uint8_t min_vbuf_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_vbuf_count](#a2b2604a36a2f7a5013d9383ab5ef198a)。

启动数据流之前必须入队的视频缓冲区最小数量。

<a id="r_ac82d9f03ecc316c6d9910beac021c5f8"></a>

```c
size_t buf_align
```

相关声明：[buf_align](#ac82d9f03ecc316c6d9910beac021c5f8)。

缓冲区对齐要求，单位为字节。

## 52.2\_详细说明（Detailed Documentation）

<a id="ac82d9f03ecc316c6d9910beac021c5f8"></a>

### `buf_align`

```c
size_t video_caps::buf_align
```

缓冲区对齐要求，单位为字节。

<a id="adb454a88504d9fd6e40510171a53b185"></a>

### `format_caps`

```c
const struct video_format_cap* video_caps::format_caps
```

视频格式能力列表，以零值终止。

<a id="a2b2604a36a2f7a5013d9383ab5ef198a"></a>

### `min_vbuf_count`

```c
uint8_t video_caps::min_vbuf_count
```

启动数据流之前必须入队的视频缓冲区最小数量。

<a id="a31520f03f621082bbf516efce23ef1f6"></a>

### `type`

```c
enum video_buf_type video_caps::type
```

缓冲区类型。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [video_format_cap](P060_video_format_cap_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_video_buffer_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_video_control_结构体.md)
