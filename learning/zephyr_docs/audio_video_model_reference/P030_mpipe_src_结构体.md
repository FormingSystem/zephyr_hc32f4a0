---
id: learning.zephyr-docs.audio-video-model-reference.page-30
title: mpipe_src_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__src.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_mpipe\_src\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__src.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基础源元素（Base Source Element）的结构。

```c
#include <zephyr/mpipe/mpipe_src.h>
```

<a id="details"></a>

源元素（Source element）的基础结构体。源元素负责生成数据并推送到下游，包含一个用于输出的源连接点（source pad）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a22ab047639b1de3c3f351d85addb0025"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#a22ab047639b1de3c3f351d85addb0025)。

基础元素（base element）结构体。

<a id="r_aaf151bbd0cd641d7cdab96cd838ebaf4"></a>

```c
struct mpipe_pad src_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[src_pad](#aaf151bbd0cd641d7cdab96cd838ebaf4)。

用于输出数据的源连接点。

<a id="r_abe17e2ccce24b48a78400ec7556576f4"></a>

```c
struct mpipe_buffer_pool * pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[pool](#abe17e2ccce24b48a78400ec7556576f4)。

用于管理输出缓冲区的缓冲池。

<a id="r_abcc3315a63cf07ea892a844041761dfa"></a>

```c
uint32_t num_buffers
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_buffers](#abcc3315a63cf07ea892a844041761dfa)。

源元素发送 EOS 前输出的缓冲区数量；0 表示无限运行。

<a id="r_ac5f6f1858c7ec49d7c328e98c3bf0c31"></a>

```c
int(* set_caps )(struct mpipe_src *self, const struct mpipe_structure *caps)
```

相关声明：[set_caps](#ac5f6f1858c7ec49d7c328e98c3bf0c31)、[mpipe_src](P030_mpipe_src_结构体.md)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

将协商得到的能力应用到源连接点。

<a id="r_a47099f2fa1050e7aa51c61e82abdc62c"></a>

```c
int(* decide_buffer_pool )(struct mpipe_src *self, struct mpipe_dispatch *query)
```

相关声明：[decide_buffer_pool](#a47099f2fa1050e7aa51c61e82abdc62c)、[mpipe_src](P030_mpipe_src_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

为下游对端确定缓冲池。

## 30.2\_详细说明（Detailed Documentation）

<a id="a47099f2fa1050e7aa51c61e82abdc62c"></a>

### `decide_buffer_pool`

```c
int(* mpipe_src::decide_buffer_pool) (struct mpipe_src *self, struct mpipe_dispatch *query)
```

为下游对端确定缓冲池。

只能通过 `mpipe_buffer_pool_set_config` 将需求提交给提出的缓冲池；如果元素为自身的缓冲池作决策，则在每次协商时都在此处重建配置基线。

<a id="a22ab047639b1de3c3f351d85addb0025"></a>

### `element`

```c
struct mpipe_element mpipe_src::element
```

基础元素（base element）结构体。

<a id="abcc3315a63cf07ea892a844041761dfa"></a>

### `num_buffers`

```c
uint32_t mpipe_src::num_buffers
```

源元素发送 EOS 前输出的缓冲区数量；0 表示无限运行。

<a id="abe17e2ccce24b48a78400ec7556576f4"></a>

### `pool`

```c
struct mpipe_buffer_pool* mpipe_src::pool
```

用于管理输出缓冲区的缓冲池。

<a id="ac5f6f1858c7ec49d7c328e98c3bf0c31"></a>

### `set_caps`

```c
int(* mpipe_src::set_caps) (struct mpipe_src *self, const struct mpipe_structure *caps)
```

将协商得到的能力应用到源连接点。

<a id="aaf151bbd0cd641d7cdab96cd838ebaf4"></a>

### `src_pad`

```c
struct mpipe_pad mpipe_src::src_pad
```

用于输出数据的源连接点。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_src.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_src](P030_mpipe_src_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)
- [mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_mpipe_sink_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_mpipe_structure_结构体.md)
