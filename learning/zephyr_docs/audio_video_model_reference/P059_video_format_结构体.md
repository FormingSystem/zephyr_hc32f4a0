---
id: learning.zephyr-docs.audio-video-model-reference.page-59
title: video_format_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_video\_format\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频格式（Video Format）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频格式（Video format）结构体，用于配置帧格式。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a233841606bfe82626f94906bf47f5f87"></a>

```c
enum video_buf_type type
```

相关声明：[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)、[type](#a233841606bfe82626f94906bf47f5f87)。

缓冲区类型。

<a id="r_adb8bf2c8d59125c050cdfe160c30f5ef"></a>

```c
uint32_t pixelformat
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pixelformat](#adb8bf2c8d59125c050cdfe160c30f5ef)。

四字符代码（FourCC）像素格式值，参见视频格式（Video Formats）。

<a id="r_a7b0cc009ac03437e7e3e86b45545b693"></a>

```c
uint32_t width
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[width](#a7b0cc009ac03437e7e3e86b45545b693)。

帧宽度，单位为像素。

<a id="r_a0e71fa7a0abd7740d5245021ba1acbb0"></a>

```c
uint32_t height
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[height](#a0e71fa7a0abd7740d5245021ba1acbb0)。

帧高度，单位为像素。

<a id="r_aa4cd70933938ec6f52175232cf403ef6"></a>

```c
uint32_t pitch
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pitch](#aa4cd70933938ec6f52175232cf403ef6)。

行跨度（line stride）。

<a id="r_a42a2dfacc89f692c36c448b3ea297a90"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a42a2dfacc89f692c36c448b3ea297a90)。

缓冲区大小，单位为字节，需要由驱动设置。

## 59.2\_详细说明（Detailed Documentation）

<a id="a0e71fa7a0abd7740d5245021ba1acbb0"></a>

### `height`

```c
uint32_t video_format::height
```

帧高度，单位为像素。

<a id="aa4cd70933938ec6f52175232cf403ef6"></a>

### `pitch`

```c
uint32_t video_format::pitch
```

行跨度（line stride）。

从某行第一个像素的地址移动到下一行第一个像素的地址时，需要增加的字节数；此值大于或等于 `width`。

<a id="adb8bf2c8d59125c050cdfe160c30f5ef"></a>

### `pixelformat`

```c
uint32_t video_format::pixelformat
```

四字符代码（FourCC）像素格式值，参见视频格式（Video Formats）。

<a id="a42a2dfacc89f692c36c448b3ea297a90"></a>

### `size`

```c
uint32_t video_format::size
```

缓冲区大小，单位为字节，需要由驱动设置。

对于未压缩格式，这是原始数据缓冲区的字节大小；可以是整个原始图像，也可以在接收器或 DMA 支持时，仅包含原始图像的一部分。

对于压缩格式，这是容纳一帧完整压缩图像所需的最大字节数，按最坏情况估计。

<a id="a233841606bfe82626f94906bf47f5f87"></a>

### `type`

```c
enum video_buf_type video_format::type
```

缓冲区类型。

<a id="a7b0cc009ac03437e7e3e86b45545b693"></a>

### `width`

```c
uint32_t video_format::width
```

帧宽度，单位为像素。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [视频格式（Video Formats）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_video_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_video_format_cap_结构体.md)
