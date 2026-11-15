---
id: learning.zephyr-docs.audio-video-model-reference.page-19
title: mpipe_caps_filter_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__caps__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_mpipe\_caps\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__caps__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

能力过滤元素（Caps Filter Element）。

```c
#include <zephyr/mpipe/base/mpipe_caps_filter.h>
```

<a id="details"></a>

能力过滤器（Caps filter）元素。这是一种变换元素（transform），将其链路协商得到的能力固定为应用配置的能力，而不修改数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a92cf8181e4e4e646be334f4b99dd2b86"></a>

```c
struct mpipe_transform transform
```

相关声明：[mpipe_transform](P034_mpipe_transform_结构体.md)、[transform](#a92cf8181e4e4e646be334f4b99dd2b86)。

基础变换元素（base transform element）。

<a id="r_a8f1606d154922e56a82126bf7d44fd87"></a>

```c
struct mpipe_pad * saved_sink_peer
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[saved_sink_peer](#a8f1606d154922e56a82126bf7d44fd87)。

接收连接点所连接的上游源连接点（source pad）。

<a id="r_ad4aa2bb005e8f905a4faf5b17a528893"></a>

```c
struct mpipe_pad * saved_src_peer
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[saved_src_peer](#ad4aa2bb005e8f905a4faf5b17a528893)。

源连接点所连接的下游接收连接点（sink pad）。

<a id="r_abe1e0857c10b4805507a60a35b33d517"></a>

```c
struct mpipe_structure filter_caps
```

相关声明：[mpipe_structure](P031_mpipe_structure_结构体.md)、[filter_caps](#abe1e0857c10b4805507a60a35b33d517)。

已配置的过滤器，在 `PAUSED -> READY` 时重新应用到连接点。

## 19.2\_详细说明（Detailed Documentation）

<a id="abe1e0857c10b4805507a60a35b33d517"></a>

### `filter_caps`

```c
struct mpipe_structure mpipe_caps_filter::filter_caps
```

已配置的过滤器，在 `PAUSED -> READY` 时重新应用到连接点。

<a id="a8f1606d154922e56a82126bf7d44fd87"></a>

### `saved_sink_peer`

```c
struct mpipe_pad* mpipe_caps_filter::saved_sink_peer
```

接收连接点所连接的上游源连接点（source pad）。

<a id="ad4aa2bb005e8f905a4faf5b17a528893"></a>

### `saved_src_peer`

```c
struct mpipe_pad* mpipe_caps_filter::saved_src_peer
```

源连接点所连接的下游接收连接点（sink pad）。

<a id="a92cf8181e4e4e646be334f4b99dd2b86"></a>

### `transform`

```c
struct mpipe_transform mpipe_caps_filter::transform
```

基础变换元素（base transform element）。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_caps_filter.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_caps_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h_source.html)
- [mpipe_transform](P034_mpipe_transform_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_mpipe_buffer_pool_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_mpipe_dispatch_结构体.md)
