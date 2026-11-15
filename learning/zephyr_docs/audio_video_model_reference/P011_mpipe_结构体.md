---
id: learning.zephyr-docs.audio-video-model-reference.page-11
title: mpipe_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_mpipe\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流水线（Pipeline）：运行处理图（Graph）的顶层容器（Bin）。

```c
#include <zephyr/mpipe/mpipe_pipeline.h>
```

<a id="details"></a>

管线（pipeline）：运行处理图的顶层容器（bin）。在容器（Bins）的基础上，增加驱动源元素的线程以及流结束（end-of-stream）计数，使包含多个接收端的处理图恰好报告一次完成。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a8729f974974932476bee46600bb48ba2"></a>

```c
struct mpipe_bin bin
```

相关声明：[mpipe_bin](P015_mpipe_bin_结构体.md)、[bin](#a8729f974974932476bee46600bb48ba2)。

基础容器（base bin）。

<a id="r_a63c71ecb90a059a4f0c5ccfcd47ab8fc"></a>

```c
struct mpipe_thread thread
```

相关声明：[mpipe_thread](P033_mpipe_thread_结构体.md)、[thread](#a63c71ecb90a059a4f0c5ccfcd47ab8fc)。

与管线关联的线程。

<a id="r_ada098be30c4f285e5066b36a56359724"></a>

```c
uint32_t num_sinks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_sinks](#ada098be30c4f285e5066b36a56359724)。

管线中的接收端元素（sink elements）数量，在 `READY -> PAUSED` 状态转换时计算。

<a id="r_a67db803b50cb4100c1fd0abfcf485b43"></a>

```c
atomic_t eos_count
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[eos_count](#a67db803b50cb4100c1fd0abfcf485b43)。

当前运行期间已观察到的流结束（EOS）消息数量。

## 11.2\_详细说明（Detailed Documentation）

<a id="a8729f974974932476bee46600bb48ba2"></a>

### `bin`

```c
struct mpipe_bin mpipe::bin
```

基础容器（base bin）。

<a id="a67db803b50cb4100c1fd0abfcf485b43"></a>

### `eos_count`

```c
atomic_t mpipe::eos_count
```

当前运行期间已观察到的流结束（EOS）消息数量。

<a id="ada098be30c4f285e5066b36a56359724"></a>

### `num_sinks`

```c
uint32_t mpipe::num_sinks
```

管线中的接收端元素（sink elements）数量，在 `READY -> PAUSED` 状态转换时计算。

<a id="a63c71ecb90a059a4f0c5ccfcd47ab8fc"></a>

### `thread`

```c
struct mpipe_thread mpipe::thread
```

与管线关联的线程。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_pipeline.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_pipeline.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h_source.html)
- [mpipe_bin](P015_mpipe_bin_结构体.md)
- [mpipe_thread](P033_mpipe_thread_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [Bins](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_mic_privacy_api_funcs_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_mpipe_app_sink_结构体.md)
