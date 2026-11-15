---
id: learning.zephyr-docs.api-source-reference.page-550
title: mpipe_element.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第550章\_mpipe\_element.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)。

## 550.1\_原始可见代码（Source Code）

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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__mpipe__element_html_ga4b7bea3b1e0995ceaaebc3f8ec4e0530"></a>
<a id="agroup__mpipe__element_html_ga5b478364e7baec25fef972ab3fee0807"></a>
<a id="agroup__mpipe__element_html_ga7ead9fea0963f40d4db49c8008cb3366"></a>
<a id="agroup__mpipe__element_html_ga89e9dc38e2cff13b63e70177732773e9"></a>
<a id="agroup__mpipe__element_html_gaa571f5b8e78dafb71e2175f0df3c496a"></a>
<a id="agroup__mpipe__element_html_gaaadee8e87da20d947d8fc90e4533ef8b"></a>
<a id="agroup__mpipe__element_html_gad20f56bd84d7767a2e5f854be7d34116"></a>
<a id="agroup__mpipe__element_html_gadd1c172f5ce2f4eb6fffeb40ecc931b6"></a>
<a id="agroup__mpipe__element_html_gafb59f995c7a2bd799316d187ec252632"></a>
<a id="agroup__mpipe__element_html_gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1"></a>
<a id="agroup__mpipe__element_html_gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92"></a>
<a id="agroup__mpipe__element_html_gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129"></a>
<a id="agroup__mpipe__element_html_gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492"></a>
<a id="agroup__mpipe__element_html_gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922"></a>
<a id="agroup__mpipe__element_html_gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544"></a>
<a id="agroup__mpipe__element_html_gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24"></a>
<a id="ampipe__object_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__element_html_a08f3bb36f9d4e3c397a91bb7a97317a8"></a>
<a id="astructmpipe__element_html_a2a414eb61a9d44a07ea38fecc7db8f07"></a>
<a id="astructmpipe__element_html_a4330512249b2c98893cdb59333794d3b"></a>
<a id="astructmpipe__element_html_a7f9ce9f14e2a46228ca02f0866904cf2"></a>
<a id="astructmpipe__element_html_a9c819d9a520a157f4211e2e80468808a"></a>
<a id="astructmpipe__element_html_aae5c0e9104f4c480e0bfafbec6619f3b"></a>
<a id="astructmpipe__element_html_adbdc3105f51b539961e2120ae13e0635"></a>
<a id="astructmpipe__object_html"></a>
<a id="astructmpipe__pad_html"></a>
<a id="astructzbus__channel_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_ELEMENT_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_ELEMENT_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util.h>

#include <zephyr/mpipe/mpipe_object.h>

struct mpipe_dispatch;
struct zbus_channel;

#if defined(CONFIG_MPIPE_ELEMENT_NAME)
#define MPIPE_ELEMENT_SET_NAME(e, n) ((e)->name = (n))
#else
#define MPIPE_ELEMENT_SET_NAME(e, n) ((void)0)
#endif

#define MPIPE_STATE_GET_NEXT(cur, target)                                                          \
        ((enum mpipe_state)((int)cur + SYS_SIGN((int)target - (int)cur)))

#define MPIPE_STATE_TRANSITION(cur, next) (((cur) << 2) | (next))

#define MPIPE_STATE_TRANSITION_CURRENT(trans) ((enum mpipe_state)((trans) >> 2))

#define MPIPE_STATE_TRANSITION_NEXT(trans) ((enum mpipe_state)((trans) & 0x3))

enum mpipe_state {
        MPIPE_STATE_READY = 0,
        MPIPE_STATE_PAUSED = 1,
        MPIPE_STATE_PLAYING = 2,
};

enum mpipe_state_change {
        MPIPE_STATE_CHANGE_READY_TO_PAUSED =
                MPIPE_STATE_TRANSITION(MPIPE_STATE_READY, MPIPE_STATE_PAUSED),
        MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING =
                MPIPE_STATE_TRANSITION(MPIPE_STATE_PAUSED, MPIPE_STATE_PLAYING),
        MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED =
                MPIPE_STATE_TRANSITION(MPIPE_STATE_PLAYING, MPIPE_STATE_PAUSED),
        MPIPE_STATE_CHANGE_PAUSED_TO_READY =
                MPIPE_STATE_TRANSITION(MPIPE_STATE_PAUSED, MPIPE_STATE_READY),
};

struct mpipe_element;

struct mpipe_element {
        struct mpipe_object object;

#if defined(CONFIG_MPIPE_ELEMENT_NAME) || defined(__DOXYGEN__)
        const char *name;
#endif

        sys_dlist_t src_pads;
        sys_dlist_t sink_pads;

        enum mpipe_state current_state;

        int (*set_state)(struct mpipe_element *element, enum mpipe_state state);
        int (*change_state)(struct mpipe_element *element, enum mpipe_state_change transition);
};

int mpipe_element_init(struct mpipe_element *self, uint8_t id);

static inline void mpipe_element_set_name(struct mpipe_element *self, const char *name)
{
        ARG_UNUSED(self);
        ARG_UNUSED(name);

        MPIPE_ELEMENT_SET_NAME(self, name);
}

struct mpipe_pad;

void mpipe_element_reset_pad_caps(struct mpipe_element *element);

void mpipe_element_add_pad(struct mpipe_element *element, struct mpipe_pad *pad);

int mpipe_element_link(struct mpipe_element *element_1, struct mpipe_element *element_2, ...);

int mpipe_element_set_state(struct mpipe_element *element, enum mpipe_state state);

struct zbus_channel *mpipe_element_get_bus_chan(struct mpipe_element *element);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_ELEMENT_H_ */
```

## 550.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 308 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_ELEMENT_H_`。

## 550.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/mpipe/mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [zbus_channel](../intercore_reference/P206_zbus通道结构.md)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [MPIPE_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24)
- [MPIPE_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544)
- [MPIPE_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [MPIPE_STATE_CHANGE_READY_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129)
- [MPIPE_STATE_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gad20f56bd84d7767a2e5f854be7d34116)
- [MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492)
- [MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92)
- [MPIPE_STATE_CHANGE_PAUSED_TO_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [object](../audio_video_model_reference/P021_mpipe_element_结构体.md#a2a414eb61a9d44a07ea38fecc7db8f07)
- [name](../audio_video_model_reference/P021_mpipe_element_结构体.md#a4330512249b2c98893cdb59333794d3b)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [src_pads](../audio_video_model_reference/P021_mpipe_element_结构体.md#adbdc3105f51b539961e2120ae13e0635)
- [sink_pads](../audio_video_model_reference/P021_mpipe_element_结构体.md#a7f9ce9f14e2a46228ca02f0866904cf2)
- [current_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#a9c819d9a520a157f4211e2e80468808a)
- [set_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#a08f3bb36f9d4e3c397a91bb7a97317a8)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [change_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#aae5c0e9104f4c480e0bfafbec6619f3b)
- [mpipe_element_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaa571f5b8e78dafb71e2175f0df3c496a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga89e9dc38e2cff13b63e70177732773e9)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [mpipe_element_reset_pad_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga4b7bea3b1e0995ceaaebc3f8ec4e0530)
- [mpipe_element_add_pad](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaaadee8e87da20d947d8fc90e4533ef8b)
- [mpipe_element_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga5b478364e7baec25fef972ab3fee0807)
- [mpipe_element_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gafb59f995c7a2bd799316d187ec252632)
- [mpipe_element_get_bus_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gadd1c172f5ce2f4eb6fffeb40ecc931b6)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [mpipe_element::set_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#a08f3bb36f9d4e3c397a91bb7a97317a8)
- [mpipe_element::object](../audio_video_model_reference/P021_mpipe_element_结构体.md#a2a414eb61a9d44a07ea38fecc7db8f07)
- [mpipe_element::name](../audio_video_model_reference/P021_mpipe_element_结构体.md#a4330512249b2c98893cdb59333794d3b)
- [mpipe_element::sink_pads](../audio_video_model_reference/P021_mpipe_element_结构体.md#a7f9ce9f14e2a46228ca02f0866904cf2)
- [mpipe_element::current_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#a9c819d9a520a157f4211e2e80468808a)
- [mpipe_element::change_state](../audio_video_model_reference/P021_mpipe_element_结构体.md#aae5c0e9104f4c480e0bfafbec6619f3b)
- [mpipe_element::src_pads](../audio_video_model_reference/P021_mpipe_element_结构体.md#adbdc3105f51b539961e2120ae13e0635)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P549_mpipe_dump.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P551_mpipe_fake_src.h_源码浏览.md)
