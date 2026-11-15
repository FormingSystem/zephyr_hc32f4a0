---
id: learning.zephyr-docs.api-source-reference.page-547
title: mpipe_caps_filter.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第547章\_mpipe\_caps\_filter.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h.html)。

## 547.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="agroup__mpipe__caps__filter_html_gaabd0709b12a0b2528c41da650414d88f"></a>
<a id="agroup__mpipe__caps__filter_html_gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597"></a>
<a id="agroup__mpipe__transform_html_gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__transform_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__caps__filter_html"></a>
<a id="astructmpipe__caps__filter_html_a8f1606d154922e56a82126bf7d44fd87"></a>
<a id="astructmpipe__caps__filter_html_a92cf8181e4e4e646be334f4b99dd2b86"></a>
<a id="astructmpipe__caps__filter_html_abe1e0857c10b4805507a60a35b33d517"></a>
<a id="astructmpipe__caps__filter_html_ad4aa2bb005e8f905a4faf5b17a528893"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructmpipe__transform_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_CAPS_FILTER_H_
#define ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_CAPS_FILTER_H_


#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_transform.h>

enum {
        MPIPE_PROP_BASE_CAPS_FILTER_CAPS = MPIPE_PROP_TRANSFORM_LAST,
};

struct mpipe_caps_filter {
        struct mpipe_transform transform;
        struct mpipe_pad *saved_sink_peer;
        struct mpipe_pad *saved_src_peer;
        struct mpipe_structure filter_caps;
};

int mpipe_caps_filter_init(struct mpipe_caps_filter *caps_filter, uint8_t id);


#endif /* ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_CAPS_FILTER_H_ */
```

## 547.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_CAPS_FILTER_H_`。

## 547.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__caps__filter_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [MPIPE_PROP_BASE_CAPS_FILTER_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gga7ba4b02da65b2fdc12c901779577e2c1a4a40eb12f04c9830c1a727a0587b0597)
- [MPIPE_PROP_TRANSFORM_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)
- [mpipe_caps_filter](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [transform](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#a92cf8181e4e4e646be334f4b99dd2b86)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [saved_sink_peer](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#a8f1606d154922e56a82126bf7d44fd87)
- [saved_src_peer](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#ad4aa2bb005e8f905a4faf5b17a528893)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [filter_caps](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#abe1e0857c10b4805507a60a35b33d517)
- [mpipe_caps_filter_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html#gaabd0709b12a0b2528c41da650414d88f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [mpipe_caps_filter::saved_sink_peer](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#a8f1606d154922e56a82126bf7d44fd87)
- [mpipe_caps_filter::transform](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#a92cf8181e4e4e646be334f4b99dd2b86)
- [mpipe_caps_filter::filter_caps](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#abe1e0857c10b4805507a60a35b33d517)
- [mpipe_caps_filter::saved_src_peer](../audio_video_model_reference/P019_mpipe_caps_filter_结构体.md#ad4aa2bb005e8f905a4faf5b17a528893)

---

[上一章](P546_mpipe_buffer.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P548_mpipe_dispatch.h_源码浏览.md)
