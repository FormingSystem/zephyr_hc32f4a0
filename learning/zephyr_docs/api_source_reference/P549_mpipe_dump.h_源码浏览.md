---
id: learning.zephyr-docs.api-source-reference.page-549
title: mpipe_dump.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第549章\_mpipe\_dump.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h.html)。

## 549.1\_原始可见代码（Source Code）

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
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="agroup__mpipe__dump_html_ga0215d4a9be34e7a5e58f8e11334ff507"></a>
<a id="agroup__mpipe__dump_html_gaa128307bee2a9cdba726f4a59313a8b2"></a>
<a id="agroup__mpipe__dump_html_gab3a73a3713a5b6fbcc961474c66f4bed"></a>
<a id="agroup__mpipe__dump_html_gae215db838d4883132d79c08d0cec3eda"></a>
<a id="agroup__mpipe__element_html_ga7ead9fea0963f40d4db49c8008cb3366"></a>
<a id="ampipe__bin_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astructmpipe__bin_html"></a>
<a id="astructmpipe__structure_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_DUMP_H_
#define ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_DUMP_H_


#include <zephyr/mpipe/mpipe_bin.h>
#include <zephyr/mpipe/mpipe_structure.h>

typedef void (*mpipe_dump_print_t)(void *ctx, const char *str);

int mpipe_dump_bin(struct mpipe_bin *bin, mpipe_dump_print_t print, void *ctx);

int mpipe_dump_caps(const struct mpipe_structure *caps, mpipe_dump_print_t print, void *ctx);

const char *mpipe_dump_state_str(enum mpipe_state state);


#endif /* ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_DUMP_H_ */
```

## 549.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_UTILS_MPIPE_DUMP_H_`。

## 549.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h.html)
- [zephyr/mpipe/mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_dump_print_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#ga0215d4a9be34e7a5e58f8e11334ff507)
- [mpipe_dump_bin](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gaa128307bee2a9cdba726f4a59313a8b2)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [mpipe_dump_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gae215db838d4883132d79c08d0cec3eda)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_dump_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gab3a73a3713a5b6fbcc961474c66f4bed)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)

---

[上一章](P548_mpipe_dispatch.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P550_mpipe_element.h_源码浏览.md)
