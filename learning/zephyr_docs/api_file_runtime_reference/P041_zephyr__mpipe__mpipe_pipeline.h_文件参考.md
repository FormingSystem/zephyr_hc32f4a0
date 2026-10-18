---
id: learning.zephyr-docs.api-file-runtime-reference.page-41
title: zephyr__mpipe__mpipe_pipeline.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_mpipe\_\_mpipe\_pipeline.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流水线（Pipeline）：运行处理图的顶层容器（Bin）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/zbus/zbus.h>
#include <zephyr/mpipe/mpipe_bin.h>
#include <zephyr/mpipe/mpipe_message.h>
#include <zephyr/mpipe/mpipe_thread.h>
```

查看此文件的源码。

流水线（Pipeline）：运行处理图的顶层容器（Bin）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 41.1\_数据结构（Data Structures）

<a id="r_mpipe"></a>

```c
struct mpipe
```

相关声明：[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)。

流水线（Pipeline）：运行处理图（Graph）的顶层容器（Bin）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 41.2\_枚举（Enumerations）

<a id="r_ga07a22fd0fa0ac67b938fd4a93b16f88d"></a>

```c
enum mpipe_prop_pipeline { MPIPE_PROP_PIPELINE_THREAD_PRIORITY }
```

相关声明：[mpipe_prop_pipeline](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga07a22fd0fa0ac67b938fd4a93b16f88d)、[MPIPE_PROP_PIPELINE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606)。

流水线属性（Pipeline Properties）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 41.3\_函数（Functions）

<a id="r_ga86fe870690248ee26e9c7894773cc928"></a>

```c
int mpipe_pipeline_init (struct mpipe *pipe, uint8_t id)
```

相关声明：[mpipe_pipeline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga86fe870690248ee26e9c7894773cc928)、[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化流水线（Pipeline）。

<a id="r_ga4d4ef57dabea505630b4503ee25ec40a"></a>

```c
int mpipe_push_buffer (struct mpipe_pad *src_pad, struct net_buf *buffer)
```

相关声明：[mpipe_push_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga4d4ef57dabea505630b4503ee25ec40a)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从给定的源端垫端（Source Pad）开始，向下游推送缓冲区（Buffer）。


## 41.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/zbus/zbus.h](../intercore_reference/P212_zbus核心完整头文件.md)
- [zephyr/mpipe/mpipe_bin.h](../api_source_configuration_reference/P058_mpipe_bin.h_源码浏览.md)
- [zephyr/mpipe/mpipe_message.h](../api_source_reference/P552_mpipe_message.h_源码浏览.md)
- [zephyr/mpipe/mpipe_thread.h](../api_source_runtime_reference/P044_mpipe_thread.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P556_mpipe_pipeline.h_源码浏览.md)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [mpipe_prop_pipeline](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga07a22fd0fa0ac67b938fd4a93b16f88d)
- [MPIPE_PROP_PIPELINE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606)
- [mpipe_pipeline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga86fe870690248ee26e9c7894773cc928)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_push_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga4d4ef57dabea505630b4503ee25ec40a)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>

---

[上一章](P040_zephyr__mpipe__mpipe_parser.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__mpipe__mpipe_sink.h_文件参考.md)
