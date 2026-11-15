---
id: learning.zephyr-docs.api-source-reference.page-558
title: mpipe_sink.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第558章\_mpipe\_sink.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)。

## 558.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00071"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__mpipe__sink_html_ga6461b51403968217a6bc568cbb990250"></a>
<a id="agroup__mpipe__sink_html_ga87a63291ab124bd59e51a57f64446d01"></a>
<a id="agroup__mpipe__sink_html_ga8c19ec865af49f6e320161582b2dd5ae"></a>
<a id="agroup__mpipe__sink_html_gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__sink_html"></a>
<a id="astructmpipe__sink_html_a4c10b264a9081382277d6cf3301d7d01"></a>
<a id="astructmpipe__sink_html_a5528d89ba5377e8dd4b928159e3e17a0"></a>
<a id="astructmpipe__sink_html_a85d4d68a6c00ffd5b52769e1e81c4987"></a>
<a id="astructmpipe__sink_html_aae87c7fbf8db3f8ab8b485f5c7105388"></a>
<a id="astructmpipe__structure_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_SINK_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_SINK_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>

struct mpipe_dispatch;

enum mpipe_prop_sink {
        MPIPE_PROP_SINK_LAST,
};

struct mpipe_sink {
        struct mpipe_element element;
        struct mpipe_pad sink_pad;
        int (*set_caps)(struct mpipe_sink *self, const struct mpipe_structure *caps);
        int (*propose_buffer_pool)(struct mpipe_sink *self, struct mpipe_dispatch *query);
};

int mpipe_sink_init(struct mpipe_sink *sink, uint8_t id);

int mpipe_sink_change_state(struct mpipe_element *self, enum mpipe_state_change transition);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_SINK_H_ */
```

## 558.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 115 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_SINK_H_`。

## 558.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_prop_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga87a63291ab124bd59e51a57f64446d01)
- [MPIPE_PROP_SINK_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b)
- [mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P029_mpipe_sink_结构体.md#aae87c7fbf8db3f8ab8b485f5c7105388)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [sink_pad](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a5528d89ba5377e8dd4b928159e3e17a0)
- [set_caps](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a4c10b264a9081382277d6cf3301d7d01)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [propose_buffer_pool](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a85d4d68a6c00ffd5b52769e1e81c4987)
- [mpipe_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga8c19ec865af49f6e320161582b2dd5ae)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_sink_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga6461b51403968217a6bc568cbb990250)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_sink::set_caps](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a4c10b264a9081382277d6cf3301d7d01)
- [mpipe_sink::sink_pad](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a5528d89ba5377e8dd4b928159e3e17a0)
- [mpipe_sink::propose_buffer_pool](../audio_video_model_reference/P029_mpipe_sink_结构体.md#a85d4d68a6c00ffd5b52769e1e81c4987)
- [mpipe_sink::element](../audio_video_model_reference/P029_mpipe_sink_结构体.md#aae87c7fbf8db3f8ab8b485f5c7105388)

---

[上一章](P557_mpipe_queue.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P559_mpipe_src.h_源码浏览.md)
