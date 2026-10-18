---
id: learning.zephyr-docs.audio-video-model-reference.page-56
title: video_ctrl_range_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_video\_ctrl\_range\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制范围（Video Control Range）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频控制范围（Video control range）结构体，描述控制项的取值范围，包括最小值、最大值、步长及默认值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_aaf4364cc626167fd7f362cbf66cc86d8"></a>

```c
int32_t min
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[min](#a0814e901d0edfcfa8be5419eb5bf063e)。

<a id="r_ad4882fbabfefb001b7ffea7b0ee53f10"></a>

```c
int64_t min64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[min64](#a25e816ab3403881ea1b0db70fbe736f1)。

<a id="r_a02dae1961257dace8dda3450ab6eec8e"></a>

```c
};
```

控制项最小值，包含此边界。

```c
union {
```

<a id="r_a8976a8d0592b8d7e90e1320dfda2452b"></a>

```c
int32_t max
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[max](#a3c2108ece802872716abf1672ccde5fa)。

<a id="r_a6defc4d8d3b927ae2c1a435764b8b700"></a>

```c
int64_t max64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[max64](#a7acb36bff57836f7bffd3ccbb2e4691e)。

<a id="r_a6c8a9f82aacbaf43dc534c482292c05b"></a>

```c
};
```

控制项最大值，包含此边界。

```c
union {
```

<a id="r_a5209dabfe30f6fa1d145599b70bcb75b"></a>

```c
int32_t step
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[step](#ab1ca560d28446134189cd7d585bd146a)。

<a id="r_af32734ae2b7d8c695a3eb9c8feaa582e"></a>

```c
int64_t step64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[step64](#a9912a5060e6615388b5c8f013eaa3c51)。

<a id="r_abaa44d64c6e0b2ce4257463f4c25cc06"></a>

```c
};
```

控制项取值步长。

```c
union {
```

<a id="r_a22d4a90cbb83aa7e8d6614e11e7dfc98"></a>

```c
int32_t def
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[def](#ac41aad65e524036c1f01f164726dc209)。

<a id="r_a88e1b8151e18f75c47e79d47b23e123a"></a>

```c
int64_t def64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[def64](#a9f339e7fce8f61b939d68421169a7030)。

<a id="r_a0d9cb50d8976f73fad9ee09a5afbadd8"></a>

```c
};
```

控制项默认值，适用于 `VIDEO_CTRL_TYPE_INTEGER`、`VIDEO_CTRL_TYPE_BOOLEAN`、`VIDEO_CTRL_TYPE_MENU` 或 `VIDEO_CTRL_TYPE_INTEGER_MENU`，对其他类型无效。

## 56.2\_详细说明（Detailed Documentation）

<a id="a02dae1961257dace8dda3450ab6eec8e"></a>

### `[union]`

```c
union { ... } video_ctrl_range
```

控制项最小值，包含此边界。

<a id="abaa44d64c6e0b2ce4257463f4c25cc06"></a>

### `[union]`

```c
union { ... } video_ctrl_range
```

控制项取值步长。

<a id="a6c8a9f82aacbaf43dc534c482292c05b"></a>

### `[union]`

```c
union { ... } video_ctrl_range
```

控制项最大值，包含此边界。

<a id="a0d9cb50d8976f73fad9ee09a5afbadd8"></a>

### `[union]`

```c
union { ... } video_ctrl_range
```

控制项默认值，适用于 `VIDEO_CTRL_TYPE_INTEGER`、`VIDEO_CTRL_TYPE_BOOLEAN`、`VIDEO_CTRL_TYPE_MENU` 或 `VIDEO_CTRL_TYPE_INTEGER_MENU`，对其他类型无效。

<a id="ac41aad65e524036c1f01f164726dc209"></a>

### `def`

```c
int32_t video_ctrl_range::def
```

<a id="a9f339e7fce8f61b939d68421169a7030"></a>

### `def64`

```c
int64_t video_ctrl_range::def64
```

<a id="a3c2108ece802872716abf1672ccde5fa"></a>

### `max`

```c
int32_t video_ctrl_range::max
```

<a id="a7acb36bff57836f7bffd3ccbb2e4691e"></a>

### `max64`

```c
int64_t video_ctrl_range::max64
```

<a id="a0814e901d0edfcfa8be5419eb5bf063e"></a>

### `min`

```c
int32_t video_ctrl_range::min
```

<a id="a25e816ab3403881ea1b0db70fbe736f1"></a>

### `min64`

```c
int64_t video_ctrl_range::min64
```

<a id="ab1ca560d28446134189cd7d585bd146a"></a>

### `step`

```c
int32_t video_ctrl_range::step
```

<a id="a9912a5060e6615388b5c8f013eaa3c51"></a>

### `step64`

```c
int64_t video_ctrl_range::step64
```

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [video_ctrl_range](P056_video_ctrl_range_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_video_ctrl_query_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_video_device_结构体.md)
