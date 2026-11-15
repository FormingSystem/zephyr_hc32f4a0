---
id: learning.zephyr-docs.api-source-reference.page-560
title: mpipe_structure.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第560章\_mpipe\_structure.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)。

## 560.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00064"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00118"></a>
<a id="l00124"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="aclock_8h_html"></a>
<a id="agroup__mpipe__structure_html_ga0165db3d65894c7832dc455e8014deb5"></a>
<a id="agroup__mpipe__structure_html_ga20cd6955b0e18fedccc784705a52a34e"></a>
<a id="agroup__mpipe__structure_html_ga2b80afbbed288b46f8586f8ddc37cfde"></a>
<a id="agroup__mpipe__structure_html_ga2d00586a6073ec63775e6f690c1738dc"></a>
<a id="agroup__mpipe__structure_html_ga39287529dd4f6a3ad41d379cc99758fc"></a>
<a id="agroup__mpipe__structure_html_ga3c5ec431967b07d00bf2ad85dfbd22b4"></a>
<a id="agroup__mpipe__structure_html_ga4c3f662227ccbf343d69e2db0597cb0b"></a>
<a id="agroup__mpipe__structure_html_ga4e2bcc7f5152bfde2579bd92618b7b1c"></a>
<a id="agroup__mpipe__structure_html_ga50d3ad084dceffbff34dbd427fe65580"></a>
<a id="agroup__mpipe__structure_html_ga51192c54b880d8a20c8d3d74c83482bd"></a>
<a id="agroup__mpipe__structure_html_ga7876dc8e926adb6bd229882ead04ac54"></a>
<a id="agroup__mpipe__structure_html_ga7c612e79af6a7c600af5a32b9ee36a7b"></a>
<a id="agroup__mpipe__structure_html_ga80b32dcb5bfd7de40323302c950a76d7"></a>
<a id="agroup__mpipe__structure_html_ga9e4df6b974dab5d79fb84eff549eb2c1"></a>
<a id="agroup__mpipe__structure_html_gad0e14518c25e189a2f52383af6d56f66"></a>
<a id="agroup__mpipe__structure_html_gaf2a980631b57b9199d7f85cb2499a4e1"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618"></a>
<a id="agroup__mpipe__structure_html_gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129"></a>
<a id="agroup__mpipe__structure_html_gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535"></a>
<a id="agroup__mpipe__structure_html_gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238"></a>
<a id="agroup__mpipe__structure_html_gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229"></a>
<a id="ampipe__value_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__structure_html"></a>
<a id="astructmpipe__structure_html_a369725cad51f522a1ad631c97ad66e0b"></a>
<a id="astructmpipe__structure_html_a70a820ab037028c1cdcd3471ec262f8f"></a>
<a id="astructmpipe__structure_html_a77c9646be70c5276be0475017bfc0b0e"></a>
<a id="astructmpipe__structure_html_ad7a264c02f28023249e59b25bd5b21fd"></a>
<a id="astructmpipe__structure_html_aec4c4cdf74b7aeaeb49fc76ffabb55c8"></a>
<a id="astructmpipe__value_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_STRUCTURE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_STRUCTURE_H_

#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>

#include <zephyr/mpipe/mpipe_value.h>


enum mpipe_media_type {
        MPIPE_MEDIA_UNKNOWN = 0,
        MPIPE_MEDIA_AUDIO_PCM,
        MPIPE_MEDIA_VIDEO,
        MPIPE_MEDIA_END,
};

enum mpipe_caps_field {
        MPIPE_CAPS_PIXEL_FORMAT = 0,
        MPIPE_CAPS_IMAGE_WIDTH,
        MPIPE_CAPS_IMAGE_HEIGHT,
        MPIPE_CAPS_SAMPLE_RATE,
        MPIPE_CAPS_BIT_WIDTH,
        MPIPE_CAPS_NUM_CHANNELS,
        MPIPE_CAPS_INTERLEAVED,
        MPIPE_CAPS_FRAME_INTERVAL,
        MPIPE_CAPS_END,
};

#define MPIPE_STRUCTURE_FLAG_ANY BIT(0)

#define MPIPE_FRAME_INTERVAL_FROM_FPS(fps) DIV_ROUND_CLOSEST(USEC_PER_SEC, (fps))

struct mpipe_structure {
        uint8_t media_type_id;
        uint8_t flags;
        uint8_t num_fields;
        uint8_t ids[CONFIG_MPIPE_STRUCTURE_MAX_FIELDS];
        struct mpipe_value values[CONFIG_MPIPE_STRUCTURE_MAX_FIELDS];
};

#define MPIPE_STRUCTURE_FIELD_COUNT(field_id, value) 1 +
#define MPIPE_STRUCTURE_FIELD_ID(field_id, value)    (field_id),
#define MPIPE_STRUCTURE_FIELD_VALUE(field_id, value) value,

#define MPIPE_STRUCTURE_DEFINE(name, media, fields)                                                \
        BUILD_ASSERT((fields(MPIPE_STRUCTURE_FIELD_COUNT) 0) <= CONFIG_MPIPE_STRUCTURE_MAX_FIELDS, \
                     #name " has more fields than CONFIG_MPIPE_STRUCTURE_MAX_FIELDS");             \
        static const struct mpipe_structure name = {                                               \
                .media_type_id = (media),                                                          \
                .flags = 0,                                                                        \
                .num_fields = fields(MPIPE_STRUCTURE_FIELD_COUNT) 0,                               \
                .ids = {fields(MPIPE_STRUCTURE_FIELD_ID)},                                         \
                .values = {fields(MPIPE_STRUCTURE_FIELD_VALUE)},                                   \
        }

int mpipe_structure_init(struct mpipe_structure *structure, uint8_t media_type_id);

int mpipe_structure_init_fields(struct mpipe_structure *structure, uint8_t media_type_id, ...);

int mpipe_structure_init_any(struct mpipe_structure *structure);

bool mpipe_structure_is_any(const struct mpipe_structure *structure);

bool mpipe_structure_is_empty(const struct mpipe_structure *structure);

int mpipe_structure_append_value(struct mpipe_structure *structure, uint8_t field_id,
                                 const struct mpipe_value *value);

int mpipe_structure_copy_field(const struct mpipe_structure *src, struct mpipe_structure *dst,
                               uint8_t field_id);

int mpipe_structure_clear(struct mpipe_structure *structure);

bool mpipe_structure_is_fixed(const struct mpipe_structure *structure);

const struct mpipe_value *mpipe_structure_get_value(const struct mpipe_structure *structure,
                                                    uint8_t field_id);

int mpipe_structure_remove_field(struct mpipe_structure *structure, uint8_t field_id);

int mpipe_structure_intersect(const struct mpipe_structure *struct1,
                              const struct mpipe_structure *struct2, struct mpipe_structure *out);

int mpipe_structure_fixate(const struct mpipe_structure *src, struct mpipe_structure *out);

void mpipe_structure_print(const struct mpipe_structure *structure);


#endif /*ZEPHYR_INCLUDE_MPIPE_MPIPE_STRUCTURE_H_*/
```

## 560.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 436 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_STRUCTURE_H_`。

## 560.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/mpipe/mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)
- [mpipe_media_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4e2bcc7f5152bfde2579bd92618b7b1c)
- [MPIPE_MEDIA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535)
- [MPIPE_MEDIA_AUDIO_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238)
- [MPIPE_MEDIA_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229)
- [MPIPE_MEDIA_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129)
- [mpipe_caps_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga0165db3d65894c7832dc455e8014deb5)
- [MPIPE_CAPS_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618)
- [MPIPE_CAPS_IMAGE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972)
- [MPIPE_CAPS_IMAGE_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611)
- [MPIPE_CAPS_SAMPLE_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12)
- [MPIPE_CAPS_BIT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190)
- [MPIPE_CAPS_NUM_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982)
- [MPIPE_CAPS_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6)
- [MPIPE_CAPS_FRAME_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266)
- [MPIPE_CAPS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [media_type_id](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a369725cad51f522a1ad631c97ad66e0b)
- [flags](../audio_video_model_reference/P031_mpipe_structure_结构体.md#aec4c4cdf74b7aeaeb49fc76ffabb55c8)
- [num_fields](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a70a820ab037028c1cdcd3471ec262f8f)
- [ids](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a77c9646be70c5276be0475017bfc0b0e)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [values](../audio_video_model_reference/P031_mpipe_structure_结构体.md#ad7a264c02f28023249e59b25bd5b21fd)
- [mpipe_structure_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2b80afbbed288b46f8586f8ddc37cfde)
- [mpipe_structure_init_fields](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga80b32dcb5bfd7de40323302c950a76d7)
- [mpipe_structure_init_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga51192c54b880d8a20c8d3d74c83482bd)
- [mpipe_structure_is_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7c612e79af6a7c600af5a32b9ee36a7b)
- [mpipe_structure_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gad0e14518c25e189a2f52383af6d56f66)
- [mpipe_structure_append_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga50d3ad084dceffbff34dbd427fe65580)
- [mpipe_structure_copy_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2d00586a6073ec63775e6f690c1738dc)
- [mpipe_structure_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga39287529dd4f6a3ad41d379cc99758fc)
- [mpipe_structure_is_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4c3f662227ccbf343d69e2db0597cb0b)
- [mpipe_structure_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga20cd6955b0e18fedccc784705a52a34e)
- [mpipe_structure_remove_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga3c5ec431967b07d00bf2ad85dfbd22b4)
- [mpipe_structure_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga9e4df6b974dab5d79fb84eff549eb2c1)
- [mpipe_structure_fixate](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7876dc8e926adb6bd229882ead04ac54)
- [mpipe_structure_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaf2a980631b57b9199d7f85cb2499a4e1)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)
- [mpipe_structure::media_type_id](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a369725cad51f522a1ad631c97ad66e0b)
- [mpipe_structure::num_fields](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a70a820ab037028c1cdcd3471ec262f8f)
- [mpipe_structure::ids](../audio_video_model_reference/P031_mpipe_structure_结构体.md#a77c9646be70c5276be0475017bfc0b0e)
- [mpipe_structure::values](../audio_video_model_reference/P031_mpipe_structure_结构体.md#ad7a264c02f28023249e59b25bd5b21fd)
- [mpipe_structure::flags](../audio_video_model_reference/P031_mpipe_structure_结构体.md#aec4c4cdf74b7aeaeb49fc76ffabb55c8)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P559_mpipe_src.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P561_mpipe_tee.h_源码浏览.md)
