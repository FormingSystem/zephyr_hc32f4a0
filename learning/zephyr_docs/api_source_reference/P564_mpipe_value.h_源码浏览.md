---
id: learning.zephyr-docs.api-source-reference.page-564
title: mpipe_value.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第564章\_mpipe\_value.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)。

## 564.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
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
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00115"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="agroup__mpipe__value_html_ga13c68ab945becac3b8c05149abec8568"></a>
<a id="agroup__mpipe__value_html_ga1bfb3bbb99fb9cf85b8e31b4d96a8b99"></a>
<a id="agroup__mpipe__value_html_ga2acf7f0283f0f9770e8feeae9d409c43"></a>
<a id="agroup__mpipe__value_html_ga2ba5453982763aa205afd9fba8cb5a14"></a>
<a id="agroup__mpipe__value_html_ga35e81ced0e49dc6efc999a92d4b4b38b"></a>
<a id="agroup__mpipe__value_html_ga4a39e21b247f3adb27da9d6f0248d9f9"></a>
<a id="agroup__mpipe__value_html_ga73ac34a14a3a829b2c643652c209ec0a"></a>
<a id="agroup__mpipe__value_html_ga83b18949361ddd68ff58f6558b2f8ecb"></a>
<a id="agroup__mpipe__value_html_ga8b8b4952140ae9ef7e6e6f20aa99d8a2"></a>
<a id="agroup__mpipe__value_html_ga8fa023097fe09a526bd1304740010013"></a>
<a id="agroup__mpipe__value_html_gaa48c169a0b95ee16e2f3ed34f01de2f6"></a>
<a id="agroup__mpipe__value_html_gabbc6cee1cdd20b0b7405a2e109677670"></a>
<a id="agroup__mpipe__value_html_gad2db6ace74e12e07bf7cb01320a3feb0"></a>
<a id="agroup__mpipe__value_html_gae2bd5aa3194993312a5bbaa66c452ba1"></a>
<a id="agroup__mpipe__value_html_gaf0d9692302ff03a82cd93f7a2d0d3361"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astructmpipe__value_html"></a>
<a id="astructmpipe__value_html_a1988df0611b4ec27d349a7b3c000fa11"></a>
<a id="astructmpipe__value_html_a46023f18c7182424227b2499fe59673f"></a>
<a id="astructmpipe__value_html_a4b04c1933350af6ce38f32c0300fff0d"></a>
<a id="astructmpipe__value_html_a5e52fd9659e057fe6bbcba626fe4b581"></a>
<a id="astructmpipe__value_html_a6e8be639c2273a55e3ae42f2eac0cc66"></a>
<a id="astructmpipe__value_html_a7f43a41b3c31051462180182998e8b05"></a>
<a id="astructmpipe__value_html_ac5a154705771d149e834aa881441e373"></a>
<a id="astructmpipe__value_html_af070b57c281efe0ca839848063ea6522"></a>
<a id="aunionmpipe__value__bound_html"></a>
<a id="aunionmpipe__value__bound_html_a30a5b23650704fa72a62ea9f3558a7b8"></a>
<a id="aunionmpipe__value__bound_html_afe818d5dafd142fa89ca33aba7c5a671"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_VALUE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_VALUE_H_


#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>

enum mpipe_value_type {
        MPIPE_TYPE_NONE = 0,
        MPIPE_TYPE_BOOLEAN,
        MPIPE_TYPE_INT,
        MPIPE_TYPE_UINT,
        MPIPE_TYPE_INT_RANGE,
        MPIPE_TYPE_UINT_RANGE,
        MPIPE_TYPE_COUNT
};

union mpipe_value_bound {
        int32_t v_int;
        uint32_t v_uint;
};

struct mpipe_value {
        enum mpipe_value_type type;
        union {
                bool v_boolean;
                int32_t v_int;
                uint32_t v_uint;
                struct {
                        union mpipe_value_bound min;
                        union mpipe_value_bound max;
                        union mpipe_value_bound step;
                } range;
        };
};

#define MPIPE_VALUE_BOOLEAN(v)                {.type = MPIPE_TYPE_BOOLEAN, .v_boolean = (v)}
#define MPIPE_VALUE_INT(v)                    {.type = MPIPE_TYPE_INT, .v_int = (v)}
#define MPIPE_VALUE_UINT(v)                   {.type = MPIPE_TYPE_UINT, .v_uint = (v)}
#define MPIPE_VALUE_RANGE_INIT(m, lo, hi, st) {.min.m = (lo), .max.m = (hi), .step.m = (st)}
#define MPIPE_VALUE_INT_RANGE(lo, hi, st)                                                          \
        {.type = MPIPE_TYPE_INT_RANGE, .range = MPIPE_VALUE_RANGE_INIT(v_int, lo, hi, st)}

#define MPIPE_VALUE_UINT_RANGE(lo, hi, st)                                                         \
        {.type = MPIPE_TYPE_UINT_RANGE, .range = MPIPE_VALUE_RANGE_INIT(v_uint, lo, hi, st)}


int mpipe_value_set(struct mpipe_value *value, int type, ...);

int mpipe_value_set_va_list(struct mpipe_value *value, enum mpipe_value_type type, va_list *args);

bool mpipe_value_get_boolean(const struct mpipe_value *value);

int32_t mpipe_value_get_int(const struct mpipe_value *value);

uint32_t mpipe_value_get_uint(const struct mpipe_value *value);

int32_t mpipe_value_get_int_range_min(const struct mpipe_value *range);

int32_t mpipe_value_get_int_range_max(const struct mpipe_value *range);

int32_t mpipe_value_get_int_range_step(const struct mpipe_value *range);

uint32_t mpipe_value_get_uint_range_min(const struct mpipe_value *range);

uint32_t mpipe_value_get_uint_range_max(const struct mpipe_value *range);

uint32_t mpipe_value_get_uint_range_step(const struct mpipe_value *range);

int mpipe_value_intersect(const struct mpipe_value *val1, const struct mpipe_value *val2,
                          struct mpipe_value *out);

bool mpipe_value_is_primitive(const struct mpipe_value *value);

void mpipe_value_print(const struct mpipe_value *value, bool new_line);


#endif /*ZEPHYR_INCLUDE_MPIPE_MPIPE_VALUE_H_*/
```

## 564.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 299 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_VALUE_H_`。

## 564.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)
- [MPIPE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483)
- [MPIPE_TYPE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b)
- [MPIPE_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5)
- [MPIPE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09)
- [MPIPE_TYPE_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583)
- [MPIPE_TYPE_UINT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5)
- [MPIPE_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817)
- [mpipe_value_bound](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [v_int](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md#afe818d5dafd142fa89ca33aba7c5a671)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [v_uint](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md#a30a5b23650704fa72a62ea9f3558a7b8)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [type](../audio_video_model_reference/P036_mpipe_value_结构体.md#a46023f18c7182424227b2499fe59673f)
- [v_boolean](../audio_video_model_reference/P036_mpipe_value_结构体.md#a1988df0611b4ec27d349a7b3c000fa11)
- [v_int](../audio_video_model_reference/P036_mpipe_value_结构体.md#af070b57c281efe0ca839848063ea6522)
- [v_uint](../audio_video_model_reference/P036_mpipe_value_结构体.md#a4b04c1933350af6ce38f32c0300fff0d)
- [min](../audio_video_model_reference/P036_mpipe_value_结构体.md#a6e8be639c2273a55e3ae42f2eac0cc66)
- [max](../audio_video_model_reference/P036_mpipe_value_结构体.md#ac5a154705771d149e834aa881441e373)
- [step](../audio_video_model_reference/P036_mpipe_value_结构体.md#a5e52fd9659e057fe6bbcba626fe4b581)
- [range](../audio_video_model_reference/P036_mpipe_value_结构体.md#a7f43a41b3c31051462180182998e8b05)
- [mpipe_value_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaf0d9692302ff03a82cd93f7a2d0d3361)
- [mpipe_value_set_va_list](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaa48c169a0b95ee16e2f3ed34f01de2f6)
- [mpipe_value_get_boolean](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga1bfb3bbb99fb9cf85b8e31b4d96a8b99)
- [mpipe_value_get_int](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga83b18949361ddd68ff58f6558b2f8ecb)
- [mpipe_value_get_uint](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2ba5453982763aa205afd9fba8cb5a14)
- [mpipe_value_get_int_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gae2bd5aa3194993312a5bbaa66c452ba1)
- [mpipe_value_get_int_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2acf7f0283f0f9770e8feeae9d409c43)
- [mpipe_value_get_int_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga73ac34a14a3a829b2c643652c209ec0a)
- [mpipe_value_get_uint_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8fa023097fe09a526bd1304740010013)
- [mpipe_value_get_uint_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga35e81ced0e49dc6efc999a92d4b4b38b)
- [mpipe_value_get_uint_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gabbc6cee1cdd20b0b7405a2e109677670)
- [mpipe_value_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gad2db6ace74e12e07bf7cb01320a3feb0)
- [mpipe_value_is_primitive](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga4a39e21b247f3adb27da9d6f0248d9f9)
- [mpipe_value_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga13c68ab945becac3b8c05149abec8568)
- [mpipe_value::v_boolean](../audio_video_model_reference/P036_mpipe_value_结构体.md#a1988df0611b4ec27d349a7b3c000fa11)
- [mpipe_value::type](../audio_video_model_reference/P036_mpipe_value_结构体.md#a46023f18c7182424227b2499fe59673f)
- [mpipe_value::v_uint](../audio_video_model_reference/P036_mpipe_value_结构体.md#a4b04c1933350af6ce38f32c0300fff0d)
- [mpipe_value::step](../audio_video_model_reference/P036_mpipe_value_结构体.md#a5e52fd9659e057fe6bbcba626fe4b581)
- [mpipe_value::min](../audio_video_model_reference/P036_mpipe_value_结构体.md#a6e8be639c2273a55e3ae42f2eac0cc66)
- [mpipe_value::range](../audio_video_model_reference/P036_mpipe_value_结构体.md#a7f43a41b3c31051462180182998e8b05)
- [mpipe_value::max](../audio_video_model_reference/P036_mpipe_value_结构体.md#ac5a154705771d149e834aa881441e373)
- [mpipe_value::v_int](../audio_video_model_reference/P036_mpipe_value_结构体.md#af070b57c281efe0ca839848063ea6522)
- [mpipe_value_bound::v_uint](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md#a30a5b23650704fa72a62ea9f3558a7b8)
- [mpipe_value_bound::v_int](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md#afe818d5dafd142fa89ca33aba7c5a671)

---

[上一章](P563_mpipe_transform_client.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P565_mpipe_workqueue.h_源码浏览.md)
