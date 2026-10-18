---
id: learning.zephyr-docs.api-source-reference.page-544
title: mpipe_app_src.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第544章\_mpipe\_app\_src.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h.html)。

## 544.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="agroup__mpipe__app__src_html_ga36d2f33b184a21b4bc81c3851da09231"></a>
<a id="agroup__mpipe__app__src_html_ga38b11181f864200dc78a742e1627367a"></a>
<a id="agroup__mpipe__app__src_html_ga3b30d456b8b1812f98a753012618906b"></a>
<a id="agroup__mpipe__app__src_html_ga6b367eef2ce6e91ca66ceb9040a71d1f"></a>
<a id="agroup__mpipe__app__src_html_ga7e0d167ba0017e1952b455c9e269ca37"></a>
<a id="agroup__mpipe__app__src_html_ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef"></a>
<a id="agroup__mpipe__src_html_ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__src_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmpipe__app__src_html"></a>
<a id="astructmpipe__app__src_html_a0face8d4e3aaa965ce39df4a32be67b5"></a>
<a id="astructmpipe__app__src_html_a4f578e934ae856ef6ae93f3e41949831"></a>
<a id="astructmpipe__app__src_html_ac13f9d17dac184228947e42f0ca71b5c"></a>
<a id="astructmpipe__app__src_html_adc96d20cf76b13694c00370c3d30ba73"></a>
<a id="astructmpipe__app__src_html_ae1027603257aecb656c175acc6f57fbe"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__src_html"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructnet__buf_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SRC_H_
#define ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SRC_H_


#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>

#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_src.h>
#include <zephyr/mpipe/mpipe_structure.h>

enum {
        MPIPE_PROP_BASE_APP_SRC_CAPS = MPIPE_PROP_SRC_LAST,
};

struct mpipe_app_src {
        struct mpipe_src src;
        struct mpipe_structure caps;
        struct mpipe_buffer_pool pool;
        struct k_msgq msgq;
        char msgq_buffer[(CONFIG_MPIPE_BASE_APP_SRC_QUEUE_DEPTH + 1) * sizeof(void *)];
};

int mpipe_app_src_init(struct mpipe_app_src *app_src, uint8_t id);

int mpipe_app_src_alloc(struct mpipe_app_src *app_src, uint32_t size, k_timeout_t timeout,
                        struct net_buf **buf);

int mpipe_app_src_push_buf(struct mpipe_app_src *app_src, struct net_buf *buf, uint32_t size,
                           k_timeout_t timeout);

int mpipe_app_src_push(struct mpipe_app_src *app_src, const void *data, uint32_t size,
                       k_timeout_t timeout);

int mpipe_app_src_eos(struct mpipe_app_src *app_src, k_timeout_t timeout);


#endif /* ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SRC_H_ */
```

## 544.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 160 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SRC_H_`。

## 544.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [MPIPE_PROP_BASE_APP_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef)
- [MPIPE_PROP_SRC_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e)
- [mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)
- [mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)
- [src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#ae1027603257aecb656c175acc6f57fbe)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [caps](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#adc96d20cf76b13694c00370c3d30ba73)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [pool](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#a4f578e934ae856ef6ae93f3e41949831)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [msgq](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#ac13f9d17dac184228947e42f0ca71b5c)
- [msgq_buffer](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#a0face8d4e3aaa965ce39df4a32be67b5)
- [mpipe_app_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga36d2f33b184a21b4bc81c3851da09231)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_app_src_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga38b11181f864200dc78a742e1627367a)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_app_src_push_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga6b367eef2ce6e91ca66ceb9040a71d1f)
- [mpipe_app_src_push](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga3b30d456b8b1812f98a753012618906b)
- [mpipe_app_src_eos](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga7e0d167ba0017e1952b455c9e269ca37)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [mpipe_app_src::msgq_buffer](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#a0face8d4e3aaa965ce39df4a32be67b5)
- [mpipe_app_src::pool](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#a4f578e934ae856ef6ae93f3e41949831)
- [mpipe_app_src::msgq](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#ac13f9d17dac184228947e42f0ca71b5c)
- [mpipe_app_src::caps](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#adc96d20cf76b13694c00370c3d30ba73)
- [mpipe_app_src::src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md#ae1027603257aecb656c175acc6f57fbe)

---

[上一章](P543_mpipe_app_sink.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P545_mpipe_base.h_源码浏览.md)
