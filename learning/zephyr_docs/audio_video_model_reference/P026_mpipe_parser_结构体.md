---
id: learning.zephyr-docs.audio-video-model-reference.page-26
title: mpipe_parser_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__parser.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_mpipe\_parser\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__parser.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基础解析器元素（Base Parser Element）的结构。

```c
#include <zephyr/mpipe/mpipe_parser.h>
```

<a id="details"></a>

解析器元素（parser element）的基础结构体。在元素（Elements）的基础上增加接收和源连接点、能力协商以及缓冲池钩子，供帧重组（frame reassembly）元素使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a0dde2f144cbea55f3fa9ef14b611c001"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#a0dde2f144cbea55f3fa9ef14b611c001)。

基础元素（Base element）。

<a id="r_a7025e3f02be6cfa673c7eba74bac229b"></a>

```c
struct mpipe_pad sink_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[sink_pad](#a7025e3f02be6cfa673c7eba74bac229b)。

用于接收数据的接收连接点（sink pad）。

<a id="r_a9e10d2e1d154e588e8d5d3843a0c96ad"></a>

```c
struct mpipe_pad src_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[src_pad](#a9e10d2e1d154e588e8d5d3843a0c96ad)。

用于发送数据的源连接点（source pad）。

<a id="r_a8c2d33e51a8d8930e7d5c44060f6f4eb"></a>

```c
struct mpipe_buffer_pool * out_pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[out_pool](#a8c2d33e51a8d8930e7d5c44060f6f4eb)。

指向输出缓冲池的指针。

<a id="r_a8cd14c8caf8cf2b277d751f89cb95668"></a>

```c
int(* set_caps )(struct mpipe_parser *self, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

相关声明：[set_caps](#a8cd14c8caf8cf2b277d751f89cb95668)、[mpipe_parser](P026_mpipe_parser_结构体.md)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

将协商得到的能力应用到此元素的一个连接点。

<a id="r_a4ad16cf2eef4e0e5d34a08d27685b901"></a>

```c
int(* propose_buffer_pool )(struct mpipe_parser *self, struct mpipe_dispatch *query)
```

相关声明：[propose_buffer_pool](#a4ad16cf2eef4e0e5d34a08d27685b901)、[mpipe_parser](P026_mpipe_parser_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

向上游提出一个缓冲池。

<a id="r_a5488ff3b2857d463f2a16a346ad2a5a2"></a>

```c
int(* decide_buffer_pool )(struct mpipe_parser *self, struct mpipe_dispatch *query)
```

相关声明：[decide_buffer_pool](#a5488ff3b2857d463f2a16a346ad2a5a2)、[mpipe_parser](P026_mpipe_parser_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

为下游确定缓冲池。

## 26.2\_详细说明（Detailed Documentation）

<a id="a5488ff3b2857d463f2a16a346ad2a5a2"></a>

### `decide_buffer_pool`

```c
int(* mpipe_parser::decide_buffer_pool) (struct mpipe_parser *self, struct mpipe_dispatch *query)
```

为下游确定缓冲池。

只能通过 `mpipe_buffer_pool_set_config` 将需求提交给提出的缓冲池，而缓冲池可能拒绝，因此需要保留后备方案。如果元素为自身的缓冲池作决策，则在每次协商时都在此处重建配置基线。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向解析器元素的指针。 |
| `query` | 缓冲池查询，参见分派（Dispatches）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a0dde2f144cbea55f3fa9ef14b611c001"></a>

### `element`

```c
struct mpipe_element mpipe_parser::element
```

基础元素（Base element）。

<a id="a8c2d33e51a8d8930e7d5c44060f6f4eb"></a>

### `out_pool`

```c
struct mpipe_buffer_pool* mpipe_parser::out_pool
```

指向输出缓冲池的指针。

<a id="a4ad16cf2eef4e0e5d34a08d27685b901"></a>

### `propose_buffer_pool`

```c
int(* mpipe_parser::propose_buffer_pool) (struct mpipe_parser *self, struct mpipe_dispatch *query)
```

向上游提出一个缓冲池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向解析器元素的指针。 |
| `query` | 缓冲池查询，参见分派（Dispatches）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a8cd14c8caf8cf2b277d751f89cb95668"></a>

### `set_caps`

```c
int(* mpipe_parser::set_caps) (struct mpipe_parser *self, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

将协商得到的能力应用到此元素的一个连接点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向解析器元素的指针。 |
| `direction` | 连接点方向，参见 `mpipe_pad_direction`。 |
| `caps` | 指向待应用能力的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a7025e3f02be6cfa673c7eba74bac229b"></a>

### `sink_pad`

```c
struct mpipe_pad mpipe_parser::sink_pad
```

用于接收数据的接收连接点（sink pad）。

<a id="a9e10d2e1d154e588e8d5d3843a0c96ad"></a>

### `src_pad`

```c
struct mpipe_pad mpipe_parser::src_pad
```

用于发送数据的源连接点（source pad）。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_parser.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_parser.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [mpipe_parser](P026_mpipe_parser_结构体.md)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)
- [Elements](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)
- [Dispatches](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_mpipe_pad_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_mpipe_player_结构体.md)
