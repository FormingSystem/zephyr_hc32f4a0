---
id: learning.zephyr-docs.api-source-reference.page-561
title: mpipe_tee.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第561章\_mpipe\_tee.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h.html)。

## 561.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="agroup__mpipe__tee_html_ga3b4228b75ae8c2b6274240979c3a1162"></a>
<a id="agroup__mpipe__tee_html_ga963f0d9cbcc79afcaea9de8fcd27e671"></a>
<a id="agroup__mpipe__tee_html_gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__tee_html"></a>
<a id="astructmpipe__tee_html_a601ed87f90ad3fdd37d82dabc4d03736"></a>
<a id="astructmpipe__tee_html_ace725880029f3b6a5508d4ddcc9345ea"></a>
<a id="astructmpipe__tee_html_ae36497b7921babc02064cb3fbcb887ae"></a>
<a id="astructmpipe__tee_html_ae80b0b54675a67dfb5c22fa44589a95e"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_TEE_H_
#define ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_TEE_H_


#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>

enum mpipe_prop_base_tee {
        MPIPE_PROP_BASE_TEE_SRC_PADS_NUM,
};

struct mpipe_tee {
        struct mpipe_element element;
        struct mpipe_pad sink_pad;
        struct mpipe_pad src_pads[CONFIG_MPIPE_BASE_TEE_MAX_SRC_PADS_NUM];
        uint8_t src_pads_num;
};

int mpipe_tee_init(struct mpipe_tee *tee, uint8_t id);


#endif /* ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_TEE_H_ */
```

## 561.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_TEE_H_`。

## 561.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_prop_base_tee](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga963f0d9cbcc79afcaea9de8fcd27e671)
- [MPIPE_PROP_BASE_TEE_SRC_PADS_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2)
- [mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ace725880029f3b6a5508d4ddcc9345ea)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [sink_pad](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ae36497b7921babc02064cb3fbcb887ae)
- [src_pads](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ae80b0b54675a67dfb5c22fa44589a95e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [src_pads_num](../audio_video_model_reference/P032_mpipe_tee_结构体.md#a601ed87f90ad3fdd37d82dabc4d03736)
- [mpipe_tee_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga3b4228b75ae8c2b6274240979c3a1162)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_tee::src_pads_num](../audio_video_model_reference/P032_mpipe_tee_结构体.md#a601ed87f90ad3fdd37d82dabc4d03736)
- [mpipe_tee::element](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ace725880029f3b6a5508d4ddcc9345ea)
- [mpipe_tee::sink_pad](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ae36497b7921babc02064cb3fbcb887ae)
- [mpipe_tee::src_pads](../audio_video_model_reference/P032_mpipe_tee_结构体.md#ae80b0b54675a67dfb5c22fa44589a95e)

---

[上一章](P560_mpipe_structure.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P562_mpipe_transform.h_源码浏览.md)
