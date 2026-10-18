---
id: learning.zephyr-docs.api-source-reference.page-562
title: mpipe_transform.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第562章\_mpipe\_transform.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)。

## 562.1\_原始可见代码（Source Code）

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
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00164"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__mpipe__pad_html_ga9de49691e139241133f231188671d4f2"></a>
<a id="agroup__mpipe__transform_html_ga1710f61119b47e057d957b56ab690dfe"></a>
<a id="agroup__mpipe__transform_html_ga24c1be1b0231360f5f192d142975efd9"></a>
<a id="agroup__mpipe__transform_html_ga4a80bc07f3cab770a42bf73a510e1aad"></a>
<a id="agroup__mpipe__transform_html_ga53de93e6bf6ca6cc2e4a7be14ff76652"></a>
<a id="agroup__mpipe__transform_html_gaecc6d5f2c8fb0d033977ecb1d5edeb5a"></a>
<a id="agroup__mpipe__transform_html_gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7"></a>
<a id="agroup__mpipe__transform_html_gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea"></a>
<a id="agroup__mpipe__transform_html_gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c"></a>
<a id="agroup__mpipe__transform_html_gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__dispatch_html_ad0f5202097b4ea9819acd8545f749f2c"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructmpipe__transform_html"></a>
<a id="astructmpipe__transform_html_a27659ad4ddd7c042b0eda9c8faa6280a"></a>
<a id="astructmpipe__transform_html_a5cfad87f6c19e5c898aa07c32ca5b93d"></a>
<a id="astructmpipe__transform_html_a69adb521d80da09249a53a35a218268c"></a>
<a id="astructmpipe__transform_html_a8cc54f1047f93abe7e805aa861a696c4"></a>
<a id="astructmpipe__transform_html_aacf7a73bb88bbea37727af5ab40347b8"></a>
<a id="astructmpipe__transform_html_aad7f8583f688e223a7d0df7cafe5bed9"></a>
<a id="astructmpipe__transform_html_abf312cbfe076c2d231c3408ffbd81575"></a>
<a id="astructmpipe__transform_html_ad10c3a231a6409f15f670784b54bd8be"></a>
<a id="astructmpipe__transform_html_ad171b584bb4b610365b1ea505da3dc06"></a>
<a id="astructmpipe__transform_html_af6dbe1b933a463e9d2c8aabba327c804"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_H_


#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
#include <zephyr/mpipe/mpipe_structure.h>

enum mpipe_prop_transform {
        MPIPE_PROP_TRANSFORM_LAST,
};

enum mpipe_transform_mode {
        MPIPE_TRANSFORM_MODE_PASSTHROUGH = 0,
        MPIPE_TRANSFORM_MODE_INPLACE = 1,
        MPIPE_TRANSFORM_MODE_NORMAL = 2,
};

struct mpipe_transform {
        struct mpipe_element element;
        struct mpipe_pad sink_pad;
        struct mpipe_pad src_pad;
        struct mpipe_buffer_pool *in_pool;
        struct mpipe_buffer_pool *out_pool;
        enum mpipe_transform_mode mode;

        int (*set_caps)(struct mpipe_transform *self, enum mpipe_pad_direction direction,
                        const struct mpipe_structure *caps);
        int (*transform_caps)(struct mpipe_transform *self, enum mpipe_pad_direction direction,
                              const struct mpipe_structure *in, uint32_t index,
                              struct mpipe_structure *out);

        int (*propose_buffer_pool)(struct mpipe_transform *self, struct mpipe_dispatch *query);
        int (*decide_buffer_pool)(struct mpipe_transform *self, struct mpipe_dispatch *query);
};

int mpipe_transform_init(struct mpipe_transform *transform, uint8_t id);

int mpipe_transform_set_caps(struct mpipe_transform *transform, enum mpipe_pad_direction direction,
                             const struct mpipe_structure *caps);

int mpipe_transform_change_state(struct mpipe_element *self, enum mpipe_state_change transition);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_H_ */
```

## 562.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 228 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_H_`。

## 562.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_prop_transform](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga1710f61119b47e057d957b56ab690dfe)
- [MPIPE_PROP_TRANSFORM_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)
- [mpipe_transform_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga53de93e6bf6ca6cc2e4a7be14ff76652)
- [MPIPE_TRANSFORM_MODE_PASSTHROUGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b)
- [MPIPE_TRANSFORM_MODE_INPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea)
- [MPIPE_TRANSFORM_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P034_mpipe_transform_结构体.md#ad10c3a231a6409f15f670784b54bd8be)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [sink_pad](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a27659ad4ddd7c042b0eda9c8faa6280a)
- [src_pad](../audio_video_model_reference/P034_mpipe_transform_结构体.md#ad171b584bb4b610365b1ea505da3dc06)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [in_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#aad7f8583f688e223a7d0df7cafe5bed9)
- [out_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a5cfad87f6c19e5c898aa07c32ca5b93d)
- [mode](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a69adb521d80da09249a53a35a218268c)
- [set_caps](../audio_video_model_reference/P034_mpipe_transform_结构体.md#af6dbe1b933a463e9d2c8aabba327c804)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [transform_caps](../audio_video_model_reference/P034_mpipe_transform_结构体.md#abf312cbfe076c2d231c3408ffbd81575)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [propose_buffer_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a8cc54f1047f93abe7e805aa861a696c4)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [decide_buffer_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#aacf7a73bb88bbea37727af5ab40347b8)
- [mpipe_transform_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gaecc6d5f2c8fb0d033977ecb1d5edeb5a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_transform_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga24c1be1b0231360f5f192d142975efd9)
- [caps](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ad0f5202097b4ea9819acd8545f749f2c)
- [mpipe_transform_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga4a80bc07f3cab770a42bf73a510e1aad)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_dispatch::caps](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ad0f5202097b4ea9819acd8545f749f2c)
- [mpipe_transform::sink_pad](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a27659ad4ddd7c042b0eda9c8faa6280a)
- [mpipe_transform::out_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a5cfad87f6c19e5c898aa07c32ca5b93d)
- [mpipe_transform::mode](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a69adb521d80da09249a53a35a218268c)
- [mpipe_transform::propose_buffer_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#a8cc54f1047f93abe7e805aa861a696c4)
- [mpipe_transform::decide_buffer_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#aacf7a73bb88bbea37727af5ab40347b8)
- [mpipe_transform::in_pool](../audio_video_model_reference/P034_mpipe_transform_结构体.md#aad7f8583f688e223a7d0df7cafe5bed9)
- [mpipe_transform::transform_caps](../audio_video_model_reference/P034_mpipe_transform_结构体.md#abf312cbfe076c2d231c3408ffbd81575)
- [mpipe_transform::element](../audio_video_model_reference/P034_mpipe_transform_结构体.md#ad10c3a231a6409f15f670784b54bd8be)
- [mpipe_transform::src_pad](../audio_video_model_reference/P034_mpipe_transform_结构体.md#ad171b584bb4b610365b1ea505da3dc06)
- [mpipe_transform::set_caps](../audio_video_model_reference/P034_mpipe_transform_结构体.md#af6dbe1b933a463e9d2c8aabba327c804)

---

[上一章](P561_mpipe_tee.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P563_mpipe_transform_client.h_源码浏览.md)
