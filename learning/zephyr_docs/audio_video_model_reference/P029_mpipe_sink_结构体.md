---
id: learning.zephyr-docs.audio-video-model-reference.page-29
title: mpipe_sink_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_mpipe\_sink\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收端元素（Sink Element）的结构。

```c
#include <zephyr/mpipe/mpipe_sink.h>
```

<a id="details"></a>

接收端元素（Sink element）结构体。表示媒体管线中的接收端元素；它是终端元素，通过其接收连接点（sink pad）消费上游元素的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_aae87c7fbf8db3f8ab8b485f5c7105388"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#aae87c7fbf8db3f8ab8b485f5c7105388)。

基础元素（base element）结构体。

<a id="r_a5528d89ba5377e8dd4b928159e3e17a0"></a>

```c
struct mpipe_pad sink_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[sink_pad](#a5528d89ba5377e8dd4b928159e3e17a0)。

用于接收数据的输入连接点（input pad）。

<a id="r_a4c10b264a9081382277d6cf3301d7d01"></a>

```c
int(* set_caps )(struct mpipe_sink *self, const struct mpipe_structure *caps)
```

相关声明：[set_caps](#a4c10b264a9081382277d6cf3301d7d01)、[mpipe_sink](P029_mpipe_sink_结构体.md)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

应用协商得到的能力（capability）。

<a id="r_a85d4d68a6c00ffd5b52769e1e81c4987"></a>

```c
int(* propose_buffer_pool )(struct mpipe_sink *self, struct mpipe_dispatch *query)
```

相关声明：[propose_buffer_pool](#a85d4d68a6c00ffd5b52769e1e81c4987)、[mpipe_sink](P029_mpipe_sink_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

向上游对端提出一个缓冲池。

## 29.2\_详细说明（Detailed Documentation）

<a id="aae87c7fbf8db3f8ab8b485f5c7105388"></a>

### `element`

```c
struct mpipe_element mpipe_sink::element
```

基础元素（base element）结构体。

<a id="a85d4d68a6c00ffd5b52769e1e81c4987"></a>

### `propose_buffer_pool`

```c
int(* mpipe_sink::propose_buffer_pool) (struct mpipe_sink *self, struct mpipe_dispatch *query)
```

向上游对端提出一个缓冲池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向接收端元素的指针。 |
| `query` | 要响应的缓冲池查询。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a4c10b264a9081382277d6cf3301d7d01"></a>

### `set_caps`

```c
int(* mpipe_sink::set_caps) (struct mpipe_sink *self, const struct mpipe_structure *caps)
```

应用协商得到的能力（capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向接收端元素的指针。 |
| `caps` | 要应用的能力。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a5528d89ba5377e8dd4b928159e3e17a0"></a>

### `sink_pad`

```c
struct mpipe_pad mpipe_sink::sink_pad
```

用于接收数据的输入连接点（input pad）。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_sink.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_sink](P029_mpipe_sink_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_mpipe_queue_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_mpipe_src_结构体.md)
