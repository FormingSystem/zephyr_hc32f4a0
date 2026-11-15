---
id: learning.zephyr-docs.audio-video-model-reference.page-55
title: video_ctrl_query_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__query.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_video\_ctrl\_query\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__query.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制查询（Video Control Query）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频控制查询（Video control query）结构体，用于查询控制项信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_aa534262295f6bf6816222d32f2b0986a"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#aa534262295f6bf6816222d32f2b0986a)。

要查询的设备；应用需要设置此字段。

<a id="r_a9444f2b8c981e61ec1b01a498b3d5506"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#a9444f2b8c981e61ec1b01a498b3d5506)。

控制项 ID；应用需要设置此字段。

<a id="r_a5a9cc00ce51abb9e3748100dc5d9403e"></a>

```c
uint32_t type
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#a5a9cc00ce51abb9e3748100dc5d9403e)。

控制项类型。

<a id="r_a0b2744becc777f7465fd9981c9e639f6"></a>

```c
const char * name
```

相关声明：[name](#a0b2744becc777f7465fd9981c9e639f6)。

控制项名称。

<a id="r_afc3e9b8a15e2d4eb04b17e0f7cd6a8cb"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb)。

控制项标志。

<a id="r_a37ac4deb89a9d5e4b30ff9293301feb5"></a>

```c
struct video_ctrl_range range
```

相关声明：[video_ctrl_range](P056_video_ctrl_range_结构体.md)、[range](#a37ac4deb89a9d5e4b30ff9293301feb5)。

控制项取值范围。

```c
union {
```

<a id="r_a0d3b58d3b600a63ea6cb9f83c76e8c6b"></a>

```c
const char *const * menu
```

相关声明：[menu](#a56323de13c279c678ffcddc2ea355eea)。

<a id="r_a8545470a0d01b5f5abf66b319abe0c42"></a>

```c
const int64_t * int_menu
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[int_menu](#ad0d74a650e83dece50ca2d46d9e5c750)。

<a id="r_a9699d22c111e21e67361e8a6f5a38b7e"></a>

```c
};
```

控制项为菜单类型时使用的菜单。

## 55.2\_详细说明（Detailed Documentation）

<a id="a9699d22c111e21e67361e8a6f5a38b7e"></a>

### `[union]`

```c
union { ... } video_ctrl_query
```

控制项为菜单类型时使用的菜单。

<a id="aa534262295f6bf6816222d32f2b0986a"></a>

### `dev`

```c
const struct device* video_ctrl_query::dev
```

要查询的设备；应用需要设置此字段。

<a id="afc3e9b8a15e2d4eb04b17e0f7cd6a8cb"></a>

### `flags`

```c
uint32_t video_ctrl_query::flags
```

控制项标志。

<a id="a9444f2b8c981e61ec1b01a498b3d5506"></a>

### `id`

```c
uint32_t video_ctrl_query::id
```

控制项 ID；应用需要设置此字段。

<a id="ad0d74a650e83dece50ca2d46d9e5c750"></a>

### `int_menu`

```c
const int64_t* video_ctrl_query::int_menu
```

<a id="a56323de13c279c678ffcddc2ea355eea"></a>

### `menu`

```c
const char* const* video_ctrl_query::menu
```

<a id="a0b2744becc777f7465fd9981c9e639f6"></a>

### `name`

```c
const char* video_ctrl_query::name
```

控制项名称。

<a id="a37ac4deb89a9d5e4b30ff9293301feb5"></a>

### `range`

```c
struct video_ctrl_range video_ctrl_query::range
```

控制项取值范围。

<a id="a5a9cc00ce51abb9e3748100dc5d9403e"></a>

### `type`

```c
uint32_t video_ctrl_query::type
```

控制项类型。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [video_ctrl_range](P056_video_ctrl_range_结构体.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [video_ctrl_query](P055_video_ctrl_query_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_video_ctrl_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_video_ctrl_range_结构体.md)
