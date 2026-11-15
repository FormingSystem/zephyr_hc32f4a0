---
id: learning.zephyr-docs.audio-video-model-reference.page-65
title: video_selection_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__selection.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_video\_selection\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__selection.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频选择（裁剪/合成，Crop / Compose）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频选择区域（Video selection）结构体，用于裁剪或合成（crop/compose），描述对视频设备选择目标的查询与设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_aec9dd0ae07f995f490ebdd86d48c1a63"></a>

```c
enum video_buf_type type
```

相关声明：[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)、[type](#aec9dd0ae07f995f490ebdd86d48c1a63)。

缓冲区类型，允许为同时具有输入和输出的设备选择相应一侧。

<a id="r_afe358118a1d3c373888674f331dd05f1"></a>

```c
enum video_selection_target target
```

相关声明：[video_selection_target](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gae375c0586e3505632cc69348935c9b54)、[target](#afe358118a1d3c373888674f331dd05f1)。

选择目标（selection target）的枚举值。

<a id="r_a2e634792c0758a3dd576e4871c250bd2"></a>

```c
struct video_rect rect
```

相关声明：[video_rect](P064_video_rect_结构体.md)、[rect](#a2e634792c0758a3dd576e4871c250bd2)。

选择目标矩形。

## 65.2\_详细说明（Detailed Documentation）

<a id="a2e634792c0758a3dd576e4871c250bd2"></a>

### `rect`

```c
struct video_rect video_selection::rect
```

选择目标矩形。

<a id="afe358118a1d3c373888674f331dd05f1"></a>

### `target`

```c
enum video_selection_target video_selection::target
```

选择目标（selection target）的枚举值。

<a id="aec9dd0ae07f995f490ebdd86d48c1a63"></a>

### `type`

```c
enum video_buf_type video_selection::type
```

缓冲区类型，允许为同时具有输入和输出的设备选择相应一侧。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [video_selection_target](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gae375c0586e3505632cc69348935c9b54)
- [video_rect](P064_video_rect_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_video_rect_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_audio_dai_cfg_t_联合体.md)
