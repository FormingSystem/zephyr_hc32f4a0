---
id: learning.zephyr-docs.api-source-reference.page-554
title: mpipe_pad.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第554章\_mpipe\_pad.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)。

## 554.1\_原始可见代码（Source Code）

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
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00159"></a>
<a id="l00168"></a>
<a id="l00177"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mpipe__pad_html_ga1249052f4192c3cc5c052c59fc120a82"></a>
<a id="agroup__mpipe__pad_html_ga1bc13e3d72c8daed41344d727766e830"></a>
<a id="agroup__mpipe__pad_html_ga28ede4a47055d4a98aac21a15973714b"></a>
<a id="agroup__mpipe__pad_html_ga35b334800669dbe25a46c71d75afd775"></a>
<a id="agroup__mpipe__pad_html_ga3a02138067490e72f3b36d3cfb3639bb"></a>
<a id="agroup__mpipe__pad_html_ga6103c9bbb48a5b03a3805a561c19b9f5"></a>
<a id="agroup__mpipe__pad_html_ga6b05aca1580f37d8b65d8534b5ab9fa3"></a>
<a id="agroup__mpipe__pad_html_ga6d217c7c0cf12e1f309839ccd3b30eb7"></a>
<a id="agroup__mpipe__pad_html_ga6daef8b8fb359e5a8edada810d5136bc"></a>
<a id="agroup__mpipe__pad_html_ga867dff16bf63d21cab505f2b1f282ebc"></a>
<a id="agroup__mpipe__pad_html_ga9de49691e139241133f231188671d4f2"></a>
<a id="agroup__mpipe__pad_html_gae260b9597d59469fdd89cc9604d33646"></a>
<a id="agroup__mpipe__pad_html_gaf1210118ce75177f5950074acb5bfd4f"></a>
<a id="agroup__mpipe__pad_html_gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24"></a>
<a id="agroup__mpipe__pad_html_gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b"></a>
<a id="agroup__mpipe__pad_html_gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe"></a>
<a id="agroup__mpipe__pad_html_gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1"></a>
<a id="agroup__mpipe__pad_html_gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4"></a>
<a id="agroup__mpipe__pad_html_gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485"></a>
<a id="agroup__mpipe__pad_html_ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1"></a>
<a id="agroup__mpipe__pad_html_ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3"></a>
<a id="agroup__mpipe__pad_html_ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__object_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__object_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructmpipe__pad_html_a03b9660c8380aef60aae41945979aa47"></a>
<a id="astructmpipe__pad_html_a0a6bc88b06ead152fbe6bf8f84836f00"></a>
<a id="astructmpipe__pad_html_a13c26a0fedaaae44870bdfd7699d88f4"></a>
<a id="astructmpipe__pad_html_a19b6d32fab3c7af1e3976c00ab0f757b"></a>
<a id="astructmpipe__pad_html_a220664610a98c5e24f15d05d3f7fbaf7"></a>
<a id="astructmpipe__pad_html_a2c4552341d8a39d6c4de66055ca3fa92"></a>
<a id="astructmpipe__pad_html_a500f2d13c64cd25557aa40e64ee6a550"></a>
<a id="astructmpipe__pad_html_a7868d142a953da55530271ec6619a57c"></a>
<a id="astructmpipe__pad_html_a8eb0fadf412d4c5307d0a0a0cf295eb7"></a>
<a id="astructmpipe__pad_html_add18ea9141b50fc74ead823bc34fdba6"></a>
<a id="astructmpipe__pad_html_af842f4ab962a4768da03661f5fb3decc"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructnet__buf_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_PAD_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_PAD_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>

#include <zephyr/kernel.h>

#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>
#include <zephyr/mpipe/mpipe_object.h>

struct mpipe_dispatch;

enum mpipe_pad_direction {
        MPIPE_PAD_UNKNOWN,
        MPIPE_PAD_SRC,
        MPIPE_PAD_SINK
};

enum mpipe_pad_mode {
        MPIPE_PAD_MODE_NONE,
        MPIPE_PAD_MODE_PUSH,
        MPIPE_PAD_MODE_PULL
};

enum mpipe_pad_presence {
        MPIPE_PAD_ALWAYS,
        MPIPE_PAD_SOMETIMES,
        MPIPE_PAD_REQUEST
};

struct mpipe_pad {
        struct mpipe_object object;
        enum mpipe_pad_direction direction;
        enum mpipe_pad_presence presence;
        enum mpipe_pad_mode mode;
        struct mpipe_pad *peer;
        struct mpipe_structure caps;
        atomic_t flushing;

        int (*process_fn)(struct mpipe_pad *pad, struct net_buf *in_buf, struct net_buf **out_buf);
        int (*query_fn)(struct mpipe_pad *pad, struct mpipe_dispatch *query);
        int (*event_fn)(struct mpipe_pad *pad, struct mpipe_dispatch *event);
        int (*enum_caps_fn)(struct mpipe_pad *pad, uint32_t index,
                            const struct mpipe_structure *filter, struct mpipe_structure *out);
};

int mpipe_pad_enum_caps(struct mpipe_pad *pad, uint32_t index, const struct mpipe_structure *filter,
                        struct mpipe_structure *out);

int mpipe_pad_enum_first(struct mpipe_pad *pad, const struct mpipe_structure *filter,
                         struct mpipe_structure *out);

int mpipe_pad_answer_caps_query(struct mpipe_pad *pad, struct mpipe_dispatch *query);

int mpipe_pad_enum_filter(const struct mpipe_structure *candidate,
                          const struct mpipe_structure *filter, struct mpipe_structure *out);

void mpipe_pad_init(struct mpipe_pad *pad, uint8_t id, enum mpipe_pad_direction direction,
                    enum mpipe_pad_presence presence);

int mpipe_pad_set_caps(struct mpipe_pad *pad, const struct mpipe_structure *caps);

void mpipe_pad_link(struct mpipe_pad *src_pad, struct mpipe_pad *sink_pad);

int mpipe_pad_send_event(struct mpipe_pad *pad, struct mpipe_dispatch *event);

int mpipe_pad_send_event_default(struct mpipe_pad *pad, struct mpipe_dispatch *event);

int mpipe_pad_query(struct mpipe_pad *pad, struct mpipe_dispatch *query);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_PAD_H_ */
```

## 554.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 366 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_PAD_H_`。

## 554.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [zephyr/mpipe/mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [MPIPE_PAD_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485)
- [MPIPE_PAD_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1)
- [MPIPE_PAD_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4)
- [mpipe_pad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6103c9bbb48a5b03a3805a561c19b9f5)
- [MPIPE_PAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe)
- [MPIPE_PAD_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24)
- [MPIPE_PAD_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b)
- [mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)
- [MPIPE_PAD_ALWAYS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1)
- [MPIPE_PAD_SOMETIMES](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3)
- [MPIPE_PAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [object](../audio_video_model_reference/P025_mpipe_pad_结构体.md#af842f4ab962a4768da03661f5fb3decc)
- [direction](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a220664610a98c5e24f15d05d3f7fbaf7)
- [presence](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a19b6d32fab3c7af1e3976c00ab0f757b)
- [mode](../audio_video_model_reference/P025_mpipe_pad_结构体.md#add18ea9141b50fc74ead823bc34fdba6)
- [peer](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a03b9660c8380aef60aae41945979aa47)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [caps](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a7868d142a953da55530271ec6619a57c)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flushing](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a8eb0fadf412d4c5307d0a0a0cf295eb7)
- [process_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a2c4552341d8a39d6c4de66055ca3fa92)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [query_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a13c26a0fedaaae44870bdfd7699d88f4)
- [event_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a500f2d13c64cd25557aa40e64ee6a550)
- [enum_caps_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a0a6bc88b06ead152fbe6bf8f84836f00)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_pad_enum_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6b05aca1580f37d8b65d8534b5ab9fa3)
- [mpipe_pad_enum_first](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6d217c7c0cf12e1f309839ccd3b30eb7)
- [mpipe_pad_answer_caps_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga28ede4a47055d4a98aac21a15973714b)
- [mpipe_pad_enum_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga3a02138067490e72f3b36d3cfb3639bb)
- [mpipe_pad_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6daef8b8fb359e5a8edada810d5136bc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_pad_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1249052f4192c3cc5c052c59fc120a82)
- [mpipe_pad_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gaf1210118ce75177f5950074acb5bfd4f)
- [mpipe_pad_send_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga867dff16bf63d21cab505f2b1f282ebc)
- [mpipe_pad_send_event_default](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1bc13e3d72c8daed41344d727766e830)
- [mpipe_pad_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga35b334800669dbe25a46c71d75afd775)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_pad::peer](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a03b9660c8380aef60aae41945979aa47)
- [mpipe_pad::enum_caps_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a0a6bc88b06ead152fbe6bf8f84836f00)
- [mpipe_pad::query_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a13c26a0fedaaae44870bdfd7699d88f4)
- [mpipe_pad::presence](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a19b6d32fab3c7af1e3976c00ab0f757b)
- [mpipe_pad::direction](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a220664610a98c5e24f15d05d3f7fbaf7)
- [mpipe_pad::process_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a2c4552341d8a39d6c4de66055ca3fa92)
- [mpipe_pad::event_fn](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a500f2d13c64cd25557aa40e64ee6a550)
- [mpipe_pad::caps](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a7868d142a953da55530271ec6619a57c)
- [mpipe_pad::flushing](../audio_video_model_reference/P025_mpipe_pad_结构体.md#a8eb0fadf412d4c5307d0a0a0cf295eb7)
- [mpipe_pad::mode](../audio_video_model_reference/P025_mpipe_pad_结构体.md#add18ea9141b50fc74ead823bc34fdba6)
- [mpipe_pad::object](../audio_video_model_reference/P025_mpipe_pad_结构体.md#af842f4ab962a4768da03661f5fb3decc)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P553_mpipe_object.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P555_mpipe_parser.h_源码浏览.md)
