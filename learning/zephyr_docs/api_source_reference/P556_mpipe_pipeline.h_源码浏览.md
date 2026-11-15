---
id: learning.zephyr-docs.api-source-reference.page-556
title: mpipe_pipeline.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第556章\_mpipe\_pipeline.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)。

## 556.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mpipe__pipeline_html_ga07a22fd0fa0ac67b938fd4a93b16f88d"></a>
<a id="agroup__mpipe__pipeline_html_ga4d4ef57dabea505630b4503ee25ec40a"></a>
<a id="agroup__mpipe__pipeline_html_ga86fe870690248ee26e9c7894773cc928"></a>
<a id="agroup__mpipe__pipeline_html_gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606"></a>
<a id="ampipe__bin_8h_html"></a>
<a id="ampipe__message_8h_html"></a>
<a id="ampipe__thread_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__bin_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__thread_html"></a>
<a id="astructmpipe_html"></a>
<a id="astructmpipe_html_a63c71ecb90a059a4f0c5ccfcd47ab8fc"></a>
<a id="astructmpipe_html_a67db803b50cb4100c1fd0abfcf485b43"></a>
<a id="astructmpipe_html_a8729f974974932476bee46600bb48ba2"></a>
<a id="astructmpipe_html_ada098be30c4f285e5066b36a56359724"></a>
<a id="astructnet__buf_html"></a>
<a id="azbus_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_PIPELINE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_PIPELINE_H_


#include <stdint.h>

#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/zbus/zbus.h>

#include <zephyr/mpipe/mpipe_bin.h>
#include <zephyr/mpipe/mpipe_message.h>
#include <zephyr/mpipe/mpipe_thread.h>

enum mpipe_prop_pipeline {
        MPIPE_PROP_PIPELINE_THREAD_PRIORITY,
};

struct mpipe {
        struct mpipe_bin bin;
        struct mpipe_thread thread;
        uint32_t num_sinks;
        atomic_t eos_count;
};

int mpipe_pipeline_init(struct mpipe *pipe, uint8_t id);

int mpipe_push_buffer(struct mpipe_pad *src_pad, struct net_buf *buffer);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_PIPELINE_H_ */
```

## 556.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 109 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_PIPELINE_H_`。

## 556.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/zbus/zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)
- [zephyr/mpipe/mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [zephyr/mpipe/mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [zephyr/mpipe/mpipe_thread.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)
- [mpipe_prop_pipeline](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga07a22fd0fa0ac67b938fd4a93b16f88d)
- [MPIPE_PROP_PIPELINE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [bin](../audio_video_model_reference/P011_mpipe_结构体.md#a8729f974974932476bee46600bb48ba2)
- [mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)
- [thread](../audio_video_model_reference/P011_mpipe_结构体.md#a63c71ecb90a059a4f0c5ccfcd47ab8fc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [num_sinks](../audio_video_model_reference/P011_mpipe_结构体.md#ada098be30c4f285e5066b36a56359724)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [eos_count](../audio_video_model_reference/P011_mpipe_结构体.md#a67db803b50cb4100c1fd0abfcf485b43)
- [mpipe_pipeline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga86fe870690248ee26e9c7894773cc928)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_push_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html#ga4d4ef57dabea505630b4503ee25ec40a)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [mpipe_thread.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [mpipe::thread](../audio_video_model_reference/P011_mpipe_结构体.md#a63c71ecb90a059a4f0c5ccfcd47ab8fc)
- [mpipe::eos_count](../audio_video_model_reference/P011_mpipe_结构体.md#a67db803b50cb4100c1fd0abfcf485b43)
- [mpipe::bin](../audio_video_model_reference/P011_mpipe_结构体.md#a8729f974974932476bee46600bb48ba2)
- [mpipe::num_sinks](../audio_video_model_reference/P011_mpipe_结构体.md#ada098be30c4f285e5066b36a56359724)
- [zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)

---

[上一章](P555_mpipe_parser.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P557_mpipe_queue.h_源码浏览.md)
