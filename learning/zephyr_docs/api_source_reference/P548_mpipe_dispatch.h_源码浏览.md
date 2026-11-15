---
id: learning.zephyr-docs.api-source-reference.page-548
title: mpipe_dispatch.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第548章\_mpipe\_dispatch.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html)。

## 548.1\_原始可见代码（Source Code）

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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="agroup__mpipe__dispatch_html_gae32e15ab045bc017100a7e713c3999b1"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_aeb4e270a084ee26fe73e799861bd0252"></a>
<a id="astructmpipe__buffer__pool__config_html"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__dispatch_html_a876f87006d975f9e292e96fd020adf74"></a>
<a id="astructmpipe__dispatch_html_aaa9ac3ab2e85a0df7bab82af11d4d045"></a>
<a id="astructmpipe__dispatch_html_ad0f5202097b4ea9819acd8545f749f2c"></a>
<a id="astructmpipe__dispatch_html_ae341e350aa4cef450267c9828ffa1cdd"></a>
<a id="astructmpipe__structure_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_DISPATCH_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_DISPATCH_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>

enum mpipe_dispatch_type {
        MPIPE_DISPATCH_UNKNOWN = 0,
        MPIPE_DISPATCH_EOS,
        MPIPE_DISPATCH_CAPS,
        MPIPE_DISPATCH_BUFFER_POOL,
        MPIPE_DISPATCH_END = UINT8_MAX,
};

struct mpipe_dispatch {
        uint8_t type;
        struct mpipe_structure *caps;
        struct mpipe_buffer_pool *pool;
        struct mpipe_buffer_pool_config pool_cfg;
};


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_DISPATCH_H_ */
```

## 548.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 110 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_DISPATCH_H_`。

## 548.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_dispatch_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#gae32e15ab045bc017100a7e713c3999b1)
- [MPIPE_DISPATCH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d)
- [MPIPE_DISPATCH_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed)
- [MPIPE_DISPATCH_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d)
- [MPIPE_DISPATCH_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3)
- [MPIPE_DISPATCH_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a)
- [UINT8_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#aeb4e270a084ee26fe73e799861bd0252)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [type](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#aaa9ac3ab2e85a0df7bab82af11d4d045)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [caps](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ad0f5202097b4ea9819acd8545f749f2c)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [pool](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#a876f87006d975f9e292e96fd020adf74)
- [mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)
- [pool_cfg](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ae341e350aa4cef450267c9828ffa1cdd)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_dispatch::pool](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#a876f87006d975f9e292e96fd020adf74)
- [mpipe_dispatch::type](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#aaa9ac3ab2e85a0df7bab82af11d4d045)
- [mpipe_dispatch::caps](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ad0f5202097b4ea9819acd8545f749f2c)
- [mpipe_dispatch::pool_cfg](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ae341e350aa4cef450267c9828ffa1cdd)

---

[上一章](P547_mpipe_caps_filter.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P549_mpipe_dump.h_源码浏览.md)
