---
id: learning.zephyr-docs.api-source-reference.page-546
title: mpipe_buffer.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第546章\_mpipe\_buffer.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)。

## 546.1\_原始可见代码（Source Code）

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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00082"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00149"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="agroup__mpipe__buffer_html_ga74d5d359f4880059485689e085887b74"></a>
<a id="agroup__mpipe__buffer_html_ga7ed6b0b1108097583138a61402c077ff"></a>
<a id="agroup__mpipe__buffer_html_ga8a80231824e6cbb7748e80df8d504e93"></a>
<a id="agroup__mpipe__buffer_html_gaa7c45d601a5891ad7a19d2b107086947"></a>
<a id="agroup__mpipe__buffer_html_gab718120f2a3c3f2a13107fd14d9385ec"></a>
<a id="agroup__mpipe__buffer_html_gabdb544b2a289a767976ecb9d97357eca"></a>
<a id="agroup__mpipe__buffer_html_gaca82ba8fed0f9b21281e9d89a8715378"></a>
<a id="agroup__mpipe__buffer_html_gad0509018241d2b69c8188b22a61530c1"></a>
<a id="agroup__net__buf_html_gaf2df457abe3e56d47107b76bdc004756"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmpipe__buffer__meta_html"></a>
<a id="astructmpipe__buffer__meta_html_a030b6e1f0c2b88c0e7bc5cdc86bb7740"></a>
<a id="astructmpipe__buffer__meta_html_a61f7a290475f471058ddd477a32206ea"></a>
<a id="astructmpipe__buffer__meta_html_a9c1c2114a0f15f52f4c134bd6bb0bf1b"></a>
<a id="astructmpipe__buffer__meta_html_aaac565e0d6f8a80a7d4a3b1e0e756198"></a>
<a id="astructmpipe__buffer__meta_html_af9725c46e3959c7c9821537851c2a17f"></a>
<a id="astructmpipe__buffer__pool__config_html"></a>
<a id="astructmpipe__buffer__pool__config_html_a94e5cd9b983b5ca8cea2cba02f8b1ec2"></a>
<a id="astructmpipe__buffer__pool__config_html_a99176426b6d20ec18eb099be1416be24"></a>
<a id="astructmpipe__buffer__pool__config_html_ab5717d6793f8f7788edc0d4874a39cd5"></a>
<a id="astructmpipe__buffer__pool__config_html_ab8412341dbd0fe3404bcbbcdd2536258"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__buffer__pool_html_a0393683ad4c617362d302e43697f7bbe"></a>
<a id="astructmpipe__buffer__pool_html_a2b300e70d25c4001552966a1a1861644"></a>
<a id="astructmpipe__buffer__pool_html_a2d3b29d91616908739e3d1e61628f8ec"></a>
<a id="astructmpipe__buffer__pool_html_a4e4dd42ddcf7b0a76fc8db650940ade3"></a>
<a id="astructmpipe__buffer__pool_html_a80a7f1817444a353765fd82634631812"></a>
<a id="astructmpipe__buffer__pool_html_a958bf985bcd2f6afcdefacc5c869a33b"></a>
<a id="astructmpipe__buffer__pool_html_a9f4030e94a053a1f4c8c3a019d8e4bd3"></a>
<a id="astructmpipe__buffer__pool_html_af31bdf5dd0aa881fd9d4394bb1020045"></a>
<a id="astructmpipe__buffer__pool_html_af542398f20b82e4f611fe31c8140ceaa"></a>
<a id="astructmpipe__buffer__pool_html_af8560f9a89aef97ff0a8fbce3f182c6b"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_BUFFER_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_BUFFER_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/net_buf.h>

struct mpipe_buffer_pool_config {
        uint32_t size;
        uint16_t align;
        uint8_t min_buffers;
        uint8_t max_buffers;
};

struct mpipe_structure;

struct mpipe_buffer_pool {
        struct mpipe_buffer_pool_config req_config;
        struct mpipe_buffer_pool_config config;
        struct net_buf_pool *nb_pool;

        int (*configure)(struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps);
        int (*set_config)(struct mpipe_buffer_pool *pool,
                          const struct mpipe_buffer_pool_config *cfg);
        int (*start)(struct mpipe_buffer_pool *pool);
        int (*stop)(struct mpipe_buffer_pool *pool);
        int (*acquire_buffer)(struct mpipe_buffer_pool *pool, struct net_buf **buf);
        int (*release_buffer)(struct mpipe_buffer_pool *pool, struct net_buf *buf);

        bool started;
};

struct mpipe_buffer_meta {
        struct mpipe_buffer_pool *pool;
        uint32_t bytes_used;
        uint32_t timestamp;
        void *driver_buf;
        void *priv;
};

static inline struct mpipe_buffer_meta *mpipe_buffer_get_meta(const struct net_buf *buf)
{
        return (struct mpipe_buffer_meta *)net_buf_user_data(buf);
}

void mpipe_buffer_destroy(struct net_buf *buf);

int mpipe_buffer_pool_configure(struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps);

int mpipe_buffer_pool_set_req_config(struct mpipe_buffer_pool *pool,
                                     const struct mpipe_buffer_pool_config *cfg);

int mpipe_buffer_pool_set_config(struct mpipe_buffer_pool *pool,
                                 const struct mpipe_buffer_pool_config *cfg);

int mpipe_buffer_pool_start(struct mpipe_buffer_pool *pool);

int mpipe_buffer_pool_stop(struct mpipe_buffer_pool *pool);

void mpipe_buffer_pool_init(struct mpipe_buffer_pool *pool);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_BUFFER_H_ */
```

## 546.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 258 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_BUFFER_H_`。

## 546.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [size](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#a94e5cd9b983b5ca8cea2cba02f8b1ec2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [align](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#a99176426b6d20ec18eb099be1416be24)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [min_buffers](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#ab8412341dbd0fe3404bcbbcdd2536258)
- [max_buffers](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#ab5717d6793f8f7788edc0d4874a39cd5)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [req_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a4e4dd42ddcf7b0a76fc8db650940ade3)
- [config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a2d3b29d91616908739e3d1e61628f8ec)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [nb_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a2b300e70d25c4001552966a1a1861644)
- [configure](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a9f4030e94a053a1f4c8c3a019d8e4bd3)
- [set_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a0393683ad4c617362d302e43697f7bbe)
- [start](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af8560f9a89aef97ff0a8fbce3f182c6b)
- [stop](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a958bf985bcd2f6afcdefacc5c869a33b)
- [acquire_buffer](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af31bdf5dd0aa881fd9d4394bb1020045)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [release_buffer](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af542398f20b82e4f611fe31c8140ceaa)
- [started](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a80a7f1817444a353765fd82634631812)
- [mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)
- [pool](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a9c1c2114a0f15f52f4c134bd6bb0bf1b)
- [bytes_used](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#aaac565e0d6f8a80a7d4a3b1e0e756198)
- [timestamp](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a030b6e1f0c2b88c0e7bc5cdc86bb7740)
- [driver_buf](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#af9725c46e3959c7c9821537851c2a17f)
- [priv](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a61f7a290475f471058ddd477a32206ea)
- [mpipe_buffer_get_meta](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaa7c45d601a5891ad7a19d2b107086947)
- [net_buf_user_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf2df457abe3e56d47107b76bdc004756)
- [mpipe_buffer_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gad0509018241d2b69c8188b22a61530c1)
- [mpipe_buffer_pool_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaca82ba8fed0f9b21281e9d89a8715378)
- [mpipe_buffer_pool_set_req_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga8a80231824e6cbb7748e80df8d504e93)
- [mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)
- [mpipe_buffer_pool_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga74d5d359f4880059485689e085887b74)
- [mpipe_buffer_pool_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga7ed6b0b1108097583138a61402c077ff)
- [mpipe_buffer_pool_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gabdb544b2a289a767976ecb9d97357eca)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [mpipe_buffer_meta::timestamp](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a030b6e1f0c2b88c0e7bc5cdc86bb7740)
- [mpipe_buffer_meta::priv](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a61f7a290475f471058ddd477a32206ea)
- [mpipe_buffer_meta::pool](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#a9c1c2114a0f15f52f4c134bd6bb0bf1b)
- [mpipe_buffer_meta::bytes_used](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#aaac565e0d6f8a80a7d4a3b1e0e756198)
- [mpipe_buffer_meta::driver_buf](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md#af9725c46e3959c7c9821537851c2a17f)
- [mpipe_buffer_pool_config::size](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#a94e5cd9b983b5ca8cea2cba02f8b1ec2)
- [mpipe_buffer_pool_config::align](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#a99176426b6d20ec18eb099be1416be24)
- [mpipe_buffer_pool_config::max_buffers](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#ab5717d6793f8f7788edc0d4874a39cd5)
- [mpipe_buffer_pool_config::min_buffers](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md#ab8412341dbd0fe3404bcbbcdd2536258)
- [mpipe_buffer_pool::set_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a0393683ad4c617362d302e43697f7bbe)
- [mpipe_buffer_pool::nb_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a2b300e70d25c4001552966a1a1861644)
- [mpipe_buffer_pool::config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a2d3b29d91616908739e3d1e61628f8ec)
- [mpipe_buffer_pool::req_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a4e4dd42ddcf7b0a76fc8db650940ade3)
- [mpipe_buffer_pool::started](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a80a7f1817444a353765fd82634631812)
- [mpipe_buffer_pool::stop](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a958bf985bcd2f6afcdefacc5c869a33b)
- [mpipe_buffer_pool::configure](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a9f4030e94a053a1f4c8c3a019d8e4bd3)
- [mpipe_buffer_pool::acquire_buffer](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af31bdf5dd0aa881fd9d4394bb1020045)
- [mpipe_buffer_pool::release_buffer](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af542398f20b82e4f611fe31c8140ceaa)
- [mpipe_buffer_pool::start](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#af8560f9a89aef97ff0a8fbce3f182c6b)

---

[上一章](P545_mpipe_base.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P547_mpipe_caps_filter.h_源码浏览.md)
