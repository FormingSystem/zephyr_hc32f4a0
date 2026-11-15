---
id: learning.zephyr-docs.audio-video-model-reference.page-32
title: mpipe_tee_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__tee.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_mpipe\_tee\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__tee.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分流元素（Tee Element）的结构。

```c
#include <zephyr/mpipe/base/mpipe_tee.h>
```

<a id="details"></a>

分流元素（Tee element）结构体。分流元素在唯一的接收连接点接收缓冲区，并将其广播到所有源连接点。各分支共享上游分配的缓冲区。分流元素绝不会将下游缓冲池转发给上游，因为多个分支不能共享同一个下游池：只有各分支合并后的缓冲池配置会向上传递，无法使用这些缓冲区的分支会将数据复制到自己的缓冲池。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_ace725880029f3b6a5508d4ddcc9345ea"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#ace725880029f3b6a5508d4ddcc9345ea)。

基础元素（base element）结构体。

<a id="r_ae36497b7921babc02064cb3fbcb887ae"></a>

```c
struct mpipe_pad sink_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[sink_pad](#ae36497b7921babc02064cb3fbcb887ae)。

用于接收输入数据的接收连接点。

<a id="r_ae80b0b54675a67dfb5c22fa44589a95e"></a>

```c
struct mpipe_pad src_pads [CONFIG_MPIPE_BASE_TEE_MAX_SRC_PADS_NUM]
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[src_pads](#ae80b0b54675a67dfb5c22fa44589a95e)。

用于发送数据的源连接点数组。

<a id="r_a601ed87f90ad3fdd37d82dabc4d03736"></a>

```c
uint8_t src_pads_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_pads_num](#a601ed87f90ad3fdd37d82dabc4d03736)。

源连接点数量。

## 32.2\_详细说明（Detailed Documentation）

<a id="ace725880029f3b6a5508d4ddcc9345ea"></a>

### `element`

```c
struct mpipe_element mpipe_tee::element
```

基础元素（base element）结构体。

<a id="ae36497b7921babc02064cb3fbcb887ae"></a>

### `sink_pad`

```c
struct mpipe_pad mpipe_tee::sink_pad
```

用于接收输入数据的接收连接点。

<a id="ae80b0b54675a67dfb5c22fa44589a95e"></a>

### `src_pads`

```c
struct mpipe_pad mpipe_tee::src_pads[CONFIG_MPIPE_BASE_TEE_MAX_SRC_PADS_NUM]
```

用于发送数据的源连接点数组。

<a id="a601ed87f90ad3fdd37d82dabc4d03736"></a>

### `src_pads_num`

```c
uint8_t mpipe_tee::src_pads_num
```

源连接点数量。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_tee.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_tee.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_mpipe_structure_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_mpipe_thread_结构体.md)
