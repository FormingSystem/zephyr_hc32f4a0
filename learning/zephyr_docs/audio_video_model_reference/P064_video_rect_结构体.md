---
id: learning.zephyr-docs.audio-video-model-reference.page-64
title: video_rect_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__rect.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_video\_rect\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__rect.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

矩形区域（Rectangle Area）的描述。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

矩形区域（rectangle area）的描述，用于裁剪或合成（crop/compose），也可能供驱动内部使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_a94da5de0a4cc682556acd00fc05a8ea5"></a>

```c
uint32_t left
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[left](#a94da5de0a4cc682556acd00fc05a8ea5)。

选择矩形的左侧偏移量。

<a id="r_a769fd3843bcb11211eccdd766d09d83a"></a>

```c
uint32_t top
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[top](#a769fd3843bcb11211eccdd766d09d83a)。

选择矩形的顶部偏移量。

<a id="r_a26403179cc6d65ff6c07a4b31b1a5050"></a>

```c
uint32_t width
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[width](#a26403179cc6d65ff6c07a4b31b1a5050)。

选择矩形的宽度。

<a id="r_a57d79483c9fc9bd800437160bd30664d"></a>

```c
uint32_t height
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[height](#a57d79483c9fc9bd800437160bd30664d)。

选择矩形的高度。

## 64.2\_详细说明（Detailed Documentation）

<a id="a57d79483c9fc9bd800437160bd30664d"></a>

### `height`

```c
uint32_t video_rect::height
```

选择矩形的高度。

<a id="a94da5de0a4cc682556acd00fc05a8ea5"></a>

### `left`

```c
uint32_t video_rect::left
```

选择矩形的左侧偏移量。

<a id="a769fd3843bcb11211eccdd766d09d83a"></a>

### `top`

```c
uint32_t video_rect::top
```

选择矩形的顶部偏移量。

<a id="a26403179cc6d65ff6c07a4b31b1a5050"></a>

### `width`

```c
uint32_t video_rect::width
```

选择矩形的宽度。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_video_frmival_stepwise_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_video_selection_结构体.md)
