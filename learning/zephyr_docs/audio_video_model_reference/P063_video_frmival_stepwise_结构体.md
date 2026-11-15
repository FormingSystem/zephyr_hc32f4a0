---
id: learning.zephyr-docs.audio-video-model-reference.page-63
title: video_frmival_stepwise_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival__stepwise.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_video\_frmival\_stepwise\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival__stepwise.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频帧间隔步进（Video Frame Interval Stepwise）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频帧间隔步进（Video frame interval stepwise）结构体，用于描述按步长变化的视频帧间隔类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_aec892104241a9d4204c87af51765ee2f"></a>

```c
struct video_frmival min
```

相关声明：[video_frmival](P061_video_frmival_结构体.md)、[min](#aec892104241a9d4204c87af51765ee2f)。

最小帧间隔，单位为秒。

<a id="r_af1c5a40da9fe7ad30185464eccf5b438"></a>

```c
struct video_frmival max
```

相关声明：[video_frmival](P061_video_frmival_结构体.md)、[max](#af1c5a40da9fe7ad30185464eccf5b438)。

最大帧间隔，单位为秒。

<a id="r_afc3c4e4fe3641952c4e6fc494fa85760"></a>

```c
struct video_frmival step
```

相关声明：[video_frmival](P061_video_frmival_结构体.md)、[step](#afc3c4e4fe3641952c4e6fc494fa85760)。

帧间隔步长，单位为秒。

## 63.2\_详细说明（Detailed Documentation）

<a id="af1c5a40da9fe7ad30185464eccf5b438"></a>

### `max`

```c
struct video_frmival video_frmival_stepwise::max
```

最大帧间隔，单位为秒。

<a id="aec892104241a9d4204c87af51765ee2f"></a>

### `min`

```c
struct video_frmival video_frmival_stepwise::min
```

最小帧间隔，单位为秒。

<a id="afc3c4e4fe3641952c4e6fc494fa85760"></a>

### `step`

```c
struct video_frmival video_frmival_stepwise::step
```

帧间隔步长，单位为秒。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [video_frmival](P061_video_frmival_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_video_frmival_enum_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_video_rect_结构体.md)
