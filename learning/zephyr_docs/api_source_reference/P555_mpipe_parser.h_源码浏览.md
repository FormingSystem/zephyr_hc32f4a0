---
id: learning.zephyr-docs.api-source-reference.page-555
title: mpipe_parser.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第555章\_mpipe\_parser.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html)。

## 555.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00081"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__mpipe__pad_html_ga9de49691e139241133f231188671d4f2"></a>
<a id="agroup__mpipe__parser_html_ga17fc0c53e8166bdde12176ee2ac7bdb1"></a>
<a id="agroup__mpipe__parser_html_ga433bfb9df636fa51e737acc3ecc0b69f"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__parser_html"></a>
<a id="astructmpipe__parser_html_a0dde2f144cbea55f3fa9ef14b611c001"></a>
<a id="astructmpipe__parser_html_a4ad16cf2eef4e0e5d34a08d27685b901"></a>
<a id="astructmpipe__parser_html_a5488ff3b2857d463f2a16a346ad2a5a2"></a>
<a id="astructmpipe__parser_html_a7025e3f02be6cfa673c7eba74bac229b"></a>
<a id="astructmpipe__parser_html_a8c2d33e51a8d8930e7d5c44060f6f4eb"></a>
<a id="astructmpipe__parser_html_a8cd14c8caf8cf2b277d751f89cb95668"></a>
<a id="astructmpipe__parser_html_a9e10d2e1d154e588e8d5d3843a0c96ad"></a>
<a id="astructmpipe__structure_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_PARSER_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_PARSER_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>

struct mpipe_parser {
        struct mpipe_element element;
        struct mpipe_pad sink_pad;
        struct mpipe_pad src_pad;
        struct mpipe_buffer_pool *out_pool;

        int (*set_caps)(struct mpipe_parser *self, enum mpipe_pad_direction direction,
                        const struct mpipe_structure *caps);
        int (*propose_buffer_pool)(struct mpipe_parser *self, struct mpipe_dispatch *query);
        int (*decide_buffer_pool)(struct mpipe_parser *self, struct mpipe_dispatch *query);
};

int mpipe_parser_init(struct mpipe_parser *parser, uint8_t id);

int mpipe_parser_change_state(struct mpipe_element *self, enum mpipe_state_change transition);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_PARSER_H_ */
```

## 555.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_PARSER_H_`。

## 555.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a0dde2f144cbea55f3fa9ef14b611c001)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [sink_pad](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a7025e3f02be6cfa673c7eba74bac229b)
- [src_pad](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a9e10d2e1d154e588e8d5d3843a0c96ad)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [out_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a8c2d33e51a8d8930e7d5c44060f6f4eb)
- [set_caps](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a8cd14c8caf8cf2b277d751f89cb95668)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [propose_buffer_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a4ad16cf2eef4e0e5d34a08d27685b901)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [decide_buffer_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a5488ff3b2857d463f2a16a346ad2a5a2)
- [mpipe_parser_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga17fc0c53e8166bdde12176ee2ac7bdb1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_parser_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga433bfb9df636fa51e737acc3ecc0b69f)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_parser::element](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a0dde2f144cbea55f3fa9ef14b611c001)
- [mpipe_parser::propose_buffer_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a4ad16cf2eef4e0e5d34a08d27685b901)
- [mpipe_parser::decide_buffer_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a5488ff3b2857d463f2a16a346ad2a5a2)
- [mpipe_parser::sink_pad](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a7025e3f02be6cfa673c7eba74bac229b)
- [mpipe_parser::out_pool](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a8c2d33e51a8d8930e7d5c44060f6f4eb)
- [mpipe_parser::set_caps](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a8cd14c8caf8cf2b277d751f89cb95668)
- [mpipe_parser::src_pad](../audio_video_model_reference/P026_mpipe_parser_结构体.md#a9e10d2e1d154e588e8d5d3843a0c96ad)

---

[上一章](P554_mpipe_pad.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P556_mpipe_pipeline.h_源码浏览.md)
