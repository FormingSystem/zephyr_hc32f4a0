---
id: learning.zephyr-docs.audio-video-model-reference.page-53
title: video_control_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_video\_control\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__control.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制（Video Control）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频控制（Video control）结构体，用于获取或设置视频控制项。另见驱动实现中使用的 `video_ctrl` 结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a9ff5d90ec4ccb2b23dbd84c0eacdad75"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#a9ff5d90ec4ccb2b23dbd84c0eacdad75)。

控制项 ID。

```c
union {
```

<a id="r_a011ad0b34c388868b5d09bc8e1cb3fe0"></a>

```c
int32_t val
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[val](#a9068d0a2e351688a9077e607042a4ed3)。

<a id="r_ad9781f16df1e2aed45a7784c4c6b54b1"></a>

```c
int64_t val64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[val64](#ab0504077a3dcc37f5781a54baeb1e65f)。

<a id="r_ad58d71b9608a7076e6edb27acb23775e"></a>

```c
};
```

控制项值。

## 53.2\_详细说明（Detailed Documentation）

<a id="ad58d71b9608a7076e6edb27acb23775e"></a>

### `[union]`

```c
union { ... } video_control
```

控制项值。

<a id="a9ff5d90ec4ccb2b23dbd84c0eacdad75"></a>

### `id`

```c
uint32_t video_control::id
```

控制项 ID。

<a id="a9068d0a2e351688a9077e607042a4ed3"></a>

### `val`

```c
int32_t video_control::val
```

<a id="ab0504077a3dcc37f5781a54baeb1e65f"></a>

### `val64`

```c
int64_t video_control::val64
```

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [video_ctrl](P054_video_ctrl_结构体.md)
- [video_control](P053_video_control_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_video_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_video_ctrl_结构体.md)
