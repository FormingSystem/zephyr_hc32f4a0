---
id: learning.zephyr-docs.audio-video-model-reference.page-62
title: video_frmival_enum_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival__enum.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_video\_frmival\_enum\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__frmival__enum.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频帧间隔枚举（Video Frame Interval Enumeration）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频帧间隔枚举（Video frame interval enumeration）结构体，用于描述给定视频格式支持的帧间隔。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a7654ce36fd942885b193da57579d88ed"></a>

```c
uint32_t index
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[index](#a7654ce36fd942885b193da57579d88ed)。

枚举时的帧间隔索引。

<a id="r_a8c103777cd5db24a2197ef994b8d008d"></a>

```c
const struct video_format * format
```

相关声明：[video_format](P059_video_format_结构体.md)、[format](#a8c103777cd5db24a2197ef994b8d008d)。

本次查询对应的视频格式。

<a id="r_aec62b54ed1152d6b3ea80c24ce7624f7"></a>

```c
enum video_frmival_type type
```

相关声明：[video_frmival_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga6abf1fc9c35cf1d1648cde7616e7cad1)、[type](#aec62b54ed1152d6b3ea80c24ce7624f7)。

设备支持的帧间隔类型。

```c
union {
```

<a id="r_aca90de6c24776a0e314a13ff05f974eb"></a>

```c
struct video_frmival discrete
```

相关声明：[video_frmival](P061_video_frmival_结构体.md)、[discrete](#af22ef303cdc75fd48b698ff72b57354c)。

<a id="r_a6b8164d3db389f69c2469e406993eddf"></a>

```c
struct video_frmival_stepwise stepwise
```

相关声明：[video_frmival_stepwise](P063_video_frmival_stepwise_结构体.md)、[stepwise](#aa3fda4e99646bff1d902198437982124)。

<a id="r_a86aa1babb7d817acba8dc47679883b65"></a>

```c
};
```

实际帧间隔。

## 62.2\_详细说明（Detailed Documentation）

<a id="a86aa1babb7d817acba8dc47679883b65"></a>

### `[union]`

```c
union { ... } video_frmival_enum
```

实际帧间隔。

<a id="af22ef303cdc75fd48b698ff72b57354c"></a>

### `discrete`

```c
struct video_frmival video_frmival_enum::discrete
```

<a id="a8c103777cd5db24a2197ef994b8d008d"></a>

### `format`

```c
const struct video_format* video_frmival_enum::format
```

本次查询对应的视频格式。

<a id="a7654ce36fd942885b193da57579d88ed"></a>

### `index`

```c
uint32_t video_frmival_enum::index
```

枚举时的帧间隔索引。

<a id="aa3fda4e99646bff1d902198437982124"></a>

### `stepwise`

```c
struct video_frmival_stepwise video_frmival_enum::stepwise
```

<a id="aec62b54ed1152d6b3ea80c24ce7624f7"></a>

### `type`

```c
enum video_frmival_type video_frmival_enum::type
```

设备支持的帧间隔类型。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [video_format](P059_video_format_结构体.md)
- [video_frmival_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga6abf1fc9c35cf1d1648cde7616e7cad1)
- [video_frmival](P061_video_frmival_结构体.md)
- [video_frmival_stepwise](P063_video_frmival_stepwise_结构体.md)
- [video_frmival_enum](P062_video_frmival_enum_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_video_frmival_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_video_frmival_stepwise_结构体.md)
