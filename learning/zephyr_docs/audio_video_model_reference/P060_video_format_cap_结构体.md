---
id: learning.zephyr-docs.audio-video-model-reference.page-60
title: video_format_cap_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format__cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_video\_format\_cap\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format__cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频格式能力（Video Format Capability）。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频格式能力（Video format capability），用于描述视频端点的一种格式能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_af5beb952295592dc9dc235a4151b2f59"></a>

```c
uint32_t pixelformat
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pixelformat](#af5beb952295592dc9dc235a4151b2f59)。

四字符代码（FourCC）像素格式值，参见视频格式（Video Formats）。

<a id="r_a539b75ac7b1eadc8c9ee9395b5b2fba9"></a>

```c
uint32_t width_min
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[width_min](#a539b75ac7b1eadc8c9ee9395b5b2fba9)。

支持的最小帧宽度，单位为像素。

<a id="r_ab45cdeb28d93d670f06caca449fccd66"></a>

```c
uint32_t width_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[width_max](#ab45cdeb28d93d670f06caca449fccd66)。

支持的最大帧宽度，单位为像素。

<a id="r_ae6f82b60ad822a37a3c97a71892d8d35"></a>

```c
uint32_t height_min
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[height_min](#ae6f82b60ad822a37a3c97a71892d8d35)。

支持的最小帧高度，单位为像素。

<a id="r_ae5f4de43c4fdaa6bc7085042ec67cd5f"></a>

```c
uint32_t height_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[height_max](#ae5f4de43c4fdaa6bc7085042ec67cd5f)。

支持的最大帧高度，单位为像素。

<a id="r_ab86710dfc4da3b5d0f9dd5017f971aad"></a>

```c
uint16_t width_step
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[width_step](#ab86710dfc4da3b5d0f9dd5017f971aad)。

宽度步长，单位为像素。

<a id="r_a512907acd398e053d48d26aab611772e"></a>

```c
uint16_t height_step
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[height_step](#a512907acd398e053d48d26aab611772e)。

高度步长，单位为像素。

## 60.2\_详细说明（Detailed Documentation）

<a id="ae5f4de43c4fdaa6bc7085042ec67cd5f"></a>

### `height_max`

```c
uint32_t video_format_cap::height_max
```

支持的最大帧高度，单位为像素。

<a id="ae6f82b60ad822a37a3c97a71892d8d35"></a>

### `height_min`

```c
uint32_t video_format_cap::height_min
```

支持的最小帧高度，单位为像素。

<a id="a512907acd398e053d48d26aab611772e"></a>

### `height_step`

```c
uint16_t video_format_cap::height_step
```

高度步长，单位为像素。

<a id="af5beb952295592dc9dc235a4151b2f59"></a>

### `pixelformat`

```c
uint32_t video_format_cap::pixelformat
```

四字符代码（FourCC）像素格式值，参见视频格式（Video Formats）。

<a id="ab45cdeb28d93d670f06caca449fccd66"></a>

### `width_max`

```c
uint32_t video_format_cap::width_max
```

支持的最大帧宽度，单位为像素。

<a id="a539b75ac7b1eadc8c9ee9395b5b2fba9"></a>

### `width_min`

```c
uint32_t video_format_cap::width_min
```

支持的最小帧宽度，单位为像素。

<a id="ab86710dfc4da3b5d0f9dd5017f971aad"></a>

### `width_step`

```c
uint16_t video_format_cap::width_step
```

宽度步长，单位为像素。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [视频格式（Video Formats）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_video_format_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_video_frmival_结构体.md)
