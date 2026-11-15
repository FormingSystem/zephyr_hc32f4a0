---
id: learning.zephyr-docs.api-source-reference.page-543
title: mpipe_app_sink.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第543章\_mpipe\_app\_sink.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h.html)。

## 543.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="agroup__mpipe__app__sink_html_ga2f62c9d0d779686aeb62ee6a393ed36b"></a>
<a id="agroup__mpipe__app__sink_html_ga6ab7e49f03e81d49a32988f996760af1"></a>
<a id="agroup__mpipe__app__sink_html_ga8bd213256bc8867364864eff4e9b0d55"></a>
<a id="agroup__mpipe__app__sink_html_ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7"></a>
<a id="agroup__mpipe__app__sink_html_ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b"></a>
<a id="agroup__mpipe__sink_html_gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__sink_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmpipe__app__sink__cb_html"></a>
<a id="astructmpipe__app__sink__cb_html_a51c6b2ef1d60e8d7d7cb644467865365"></a>
<a id="astructmpipe__app__sink__cb_html_a90c7a21725790e1e4790d78dac9b207e"></a>
<a id="astructmpipe__app__sink_html"></a>
<a id="astructmpipe__app__sink_html_a0130d318174f6d1cbc9970a163886763"></a>
<a id="astructmpipe__app__sink_html_a194a07370e0f213e08862808b2a5878f"></a>
<a id="astructmpipe__app__sink_html_a4fdd22f37571f00d27a311e39d408d34"></a>
<a id="astructmpipe__app__sink_html_a75db864f047d15bc7ea2bb9e0c67c3e7"></a>
<a id="astructmpipe__app__sink_html_a91df7398dfd2b8af883871fdaf1e5947"></a>
<a id="astructmpipe__sink_html"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ade8055f804d5a1fea13e55d71d92a5e7"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SINK_H_
#define ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SINK_H_


#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>

#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_sink.h>
#include <zephyr/mpipe/mpipe_structure.h>

enum {
        MPIPE_PROP_BASE_APP_SINK_CAPS = MPIPE_PROP_SINK_LAST,
        MPIPE_PROP_BASE_APP_SINK_CB,
};

typedef void (*mpipe_app_sink_cb_t)(const struct net_buf *buf, void *user_data);

struct mpipe_app_sink_cb {
        mpipe_app_sink_cb_t fn;
        void *user_data;
};

struct mpipe_app_sink {
        struct mpipe_sink sink;
        struct mpipe_structure caps;
        struct mpipe_app_sink_cb cb;
        struct k_msgq msgq;
        char msgq_buffer[CONFIG_MPIPE_BASE_APP_SINK_QUEUE_DEPTH * sizeof(void *)];
};

int mpipe_app_sink_init(struct mpipe_app_sink *app_sink, uint8_t id);

int mpipe_app_sink_pull(struct mpipe_app_sink *app_sink, struct net_buf **buf, k_timeout_t timeout);


#endif /* ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SINK_H_ */
```

## 543.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 126 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_APP_SINK_H_`。

## 543.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [MPIPE_PROP_BASE_APP_SINK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b)
- [MPIPE_PROP_SINK_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b)
- [MPIPE_PROP_BASE_APP_SINK_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7)
- [mpipe_app_sink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga8bd213256bc8867364864eff4e9b0d55)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [mpipe_app_sink_cb](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md)
- [fn](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md#a90c7a21725790e1e4790d78dac9b207e)
- [user_data](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md#a51c6b2ef1d60e8d7d7cb644467865365)
- [mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)
- [mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)
- [sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a0130d318174f6d1cbc9970a163886763)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [caps](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a75db864f047d15bc7ea2bb9e0c67c3e7)
- [cb](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a4fdd22f37571f00d27a311e39d408d34)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [msgq](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a194a07370e0f213e08862808b2a5878f)
- [msgq_buffer](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a91df7398dfd2b8af883871fdaf1e5947)
- [mpipe_app_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga6ab7e49f03e81d49a32988f996760af1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_app_sink_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga2f62c9d0d779686aeb62ee6a393ed36b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [mpipe_app_sink_cb::user_data](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md#a51c6b2ef1d60e8d7d7cb644467865365)
- [mpipe_app_sink_cb::fn](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md#a90c7a21725790e1e4790d78dac9b207e)
- [mpipe_app_sink::sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a0130d318174f6d1cbc9970a163886763)
- [mpipe_app_sink::msgq](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a194a07370e0f213e08862808b2a5878f)
- [mpipe_app_sink::cb](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a4fdd22f37571f00d27a311e39d408d34)
- [mpipe_app_sink::caps](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a75db864f047d15bc7ea2bb9e0c67c3e7)
- [mpipe_app_sink::msgq_buffer](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md#a91df7398dfd2b8af883871fdaf1e5947)
- [net_buf::user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)

---

[上一章](P542_mpipe.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P544_mpipe_app_src.h_源码浏览.md)
