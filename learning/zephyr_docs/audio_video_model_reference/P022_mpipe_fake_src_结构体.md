---
id: learning.zephyr-docs.audio-video-model-reference.page-22
title: mpipe_fake_src_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__fake__src.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_mpipe\_fake\_src\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__fake__src.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟源元素（Fake Source Element）的结构。

```c
#include <zephyr/mpipe/mpipe_fake_src.h>
```

<a id="details"></a>

模拟源元素（Fake Source Element）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a6e92423906560a787979923b93af0ce6"></a>

```c
struct mpipe_src src
```

相关声明：[mpipe_src](P030_mpipe_src_结构体.md)、[src](#a6e92423906560a787979923b93af0ce6)。

基础源元素（base source element），必须是第一个成员。

<a id="r_a83bb72d761efa7ba80a8a9598b0c620d"></a>

```c
struct mpipe_buffer_pool pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[pool](#a83bb72d761efa7ba80a8a9598b0c620d)。

用于管理输出缓冲区的缓冲池。

## 22.2\_详细说明（Detailed Documentation）

<a id="a83bb72d761efa7ba80a8a9598b0c620d"></a>

### `pool`

```c
struct mpipe_buffer_pool mpipe_fake_src::pool
```

用于管理输出缓冲区的缓冲池。

<a id="a6e92423906560a787979923b93af0ce6"></a>

### `src`

```c
struct mpipe_src mpipe_fake_src::src
```

基础源元素（base source element），必须是第一个成员。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_fake_src.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_fake_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h_source.html)
- [mpipe_src](P030_mpipe_src_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_mpipe_element_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_mpipe_message_结构体.md)
