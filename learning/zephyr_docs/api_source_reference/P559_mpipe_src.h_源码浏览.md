---
id: learning.zephyr-docs.api-source-reference.page-559
title: mpipe_src.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第559章\_mpipe\_src.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)。

## 559.1\_原始可见代码（Source Code）

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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__mpipe__src_html_ga31c1f53bbb8ee29228766cf33f49f924"></a>
<a id="agroup__mpipe__src_html_ga53dfd90c1a3942949337f1d222317700"></a>
<a id="agroup__mpipe__src_html_ga867c427e847edb78082607cbe9d5a87b"></a>
<a id="agroup__mpipe__src_html_gab96ba2e8ce9cbe6bf2bb27587710bbf0"></a>
<a id="agroup__mpipe__src_html_gae7fdcd5a2bfe2bfb28fa5f430349355e"></a>
<a id="agroup__mpipe__src_html_ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b"></a>
<a id="agroup__mpipe__src_html_ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__object_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__src_html"></a>
<a id="astructmpipe__src_html_a22ab047639b1de3c3f351d85addb0025"></a>
<a id="astructmpipe__src_html_a47099f2fa1050e7aa51c61e82abdc62c"></a>
<a id="astructmpipe__src_html_aaf151bbd0cd641d7cdab96cd838ebaf4"></a>
<a id="astructmpipe__src_html_abcc3315a63cf07ea892a844041761dfa"></a>
<a id="astructmpipe__src_html_abe17e2ccce24b48a78400ec7556576f4"></a>
<a id="astructmpipe__src_html_ac5f6f1858c7ec49d7c328e98c3bf0c31"></a>
<a id="astructmpipe__structure_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_SRC_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_SRC_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>

enum mpipe_prop_src {
        MPIPE_PROP_SRC_NUM_BUFS,
        MPIPE_PROP_SRC_LAST,
};

struct mpipe_src {
        struct mpipe_element element;
        struct mpipe_pad src_pad;
        struct mpipe_buffer_pool *pool;
        uint32_t num_buffers;
        int (*set_caps)(struct mpipe_src *self, const struct mpipe_structure *caps);
        int (*decide_buffer_pool)(struct mpipe_src *self, struct mpipe_dispatch *query);
};

int mpipe_src_init(struct mpipe_src *src, uint8_t id);

int mpipe_src_change_state(struct mpipe_element *self, enum mpipe_state_change transition);

int mpipe_src_set_property(struct mpipe_object *obj, uint32_t key, const void *val);

int mpipe_src_get_property(struct mpipe_object *obj, uint32_t key, void *val);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_SRC_H_ */
```

## 559.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 138 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_SRC_H_`。

## 559.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_prop_src](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gae7fdcd5a2bfe2bfb28fa5f430349355e)
- [MPIPE_PROP_SRC_NUM_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b)
- [MPIPE_PROP_SRC_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e)
- [mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P030_mpipe_src_结构体.md#a22ab047639b1de3c3f351d85addb0025)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [src_pad](../audio_video_model_reference/P030_mpipe_src_结构体.md#aaf151bbd0cd641d7cdab96cd838ebaf4)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [pool](../audio_video_model_reference/P030_mpipe_src_结构体.md#abe17e2ccce24b48a78400ec7556576f4)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [num_buffers](../audio_video_model_reference/P030_mpipe_src_结构体.md#abcc3315a63cf07ea892a844041761dfa)
- [set_caps](../audio_video_model_reference/P030_mpipe_src_结构体.md#ac5f6f1858c7ec49d7c328e98c3bf0c31)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [decide_buffer_pool](../audio_video_model_reference/P030_mpipe_src_结构体.md#a47099f2fa1050e7aa51c61e82abdc62c)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gab96ba2e8ce9cbe6bf2bb27587710bbf0)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_src_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga53dfd90c1a3942949337f1d222317700)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_src_set_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga867c427e847edb78082607cbe9d5a87b)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [mpipe_src_get_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga31c1f53bbb8ee29228766cf33f49f924)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_src::element](../audio_video_model_reference/P030_mpipe_src_结构体.md#a22ab047639b1de3c3f351d85addb0025)
- [mpipe_src::decide_buffer_pool](../audio_video_model_reference/P030_mpipe_src_结构体.md#a47099f2fa1050e7aa51c61e82abdc62c)
- [mpipe_src::src_pad](../audio_video_model_reference/P030_mpipe_src_结构体.md#aaf151bbd0cd641d7cdab96cd838ebaf4)
- [mpipe_src::num_buffers](../audio_video_model_reference/P030_mpipe_src_结构体.md#abcc3315a63cf07ea892a844041761dfa)
- [mpipe_src::pool](../audio_video_model_reference/P030_mpipe_src_结构体.md#abe17e2ccce24b48a78400ec7556576f4)
- [mpipe_src::set_caps](../audio_video_model_reference/P030_mpipe_src_结构体.md#ac5f6f1858c7ec49d7c328e98c3bf0c31)

---

[上一章](P558_mpipe_sink.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P560_mpipe_structure.h_源码浏览.md)
