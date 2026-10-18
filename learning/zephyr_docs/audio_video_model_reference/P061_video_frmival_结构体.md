---
id: learning.zephyr-docs.audio-video-model-reference.page-61
title: video_frmival_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_video\_frmival\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频帧间隔（Video Frame Interval）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频帧间隔（Video frame interval）结构体，用于描述视频帧间隔。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a57ee282f01da0f1ef1db2558d777631c"></a>

```c
uint32_t numerator
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[numerator](#a57ee282f01da0f1ef1db2558d777631c)。

帧间隔的分子（numerator）。

<a id="r_aba4a6700ea733c3b07ee6445856c580a"></a>

```c
uint32_t denominator
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[denominator](#aba4a6700ea733c3b07ee6445856c580a)。

帧间隔的分母（denominator）。

## 61.2\_详细说明（Detailed Documentation）

<a id="aba4a6700ea733c3b07ee6445856c580a"></a>

### `denominator`

```c
uint32_t video_frmival::denominator
```

帧间隔的分母（denominator）。

<a id="a57ee282f01da0f1ef1db2558d777631c"></a>

### `numerator`

```c
uint32_t video_frmival::numerator
```

帧间隔的分子（numerator）。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_video_format_cap_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_video_frmival_enum_结构体.md)
