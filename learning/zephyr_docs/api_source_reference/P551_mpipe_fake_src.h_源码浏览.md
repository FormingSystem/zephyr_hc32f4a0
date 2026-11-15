---
id: learning.zephyr-docs.api-source-reference.page-551
title: mpipe_fake_src.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第551章\_mpipe\_fake\_src.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h.html)。

## 551.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="agroup__mpipe__src_html_ga1eed36753b4c3d29b2e8c94e74ee832c"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__src_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__buffer__pool_html"></a>
<a id="astructmpipe__fake__src_html"></a>
<a id="astructmpipe__fake__src_html_a6e92423906560a787979923b93af0ce6"></a>
<a id="astructmpipe__fake__src_html_a83bb72d761efa7ba80a8a9598b0c620d"></a>
<a id="astructmpipe__src_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_FAKE_SRC_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_FAKE_SRC_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_src.h>

struct mpipe_fake_src {
        struct mpipe_src src;
        struct mpipe_buffer_pool pool;
};

int mpipe_fake_src_init(struct mpipe_fake_src *fsrc, uint8_t id);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_FAKE_SRC_H_ */
```

## 551.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_FAKE_SRC_H_`。

## 551.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)
- [mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)
- [src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md#a6e92423906560a787979923b93af0ce6)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [pool](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md#a83bb72d761efa7ba80a8a9598b0c620d)
- [mpipe_fake_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga1eed36753b4c3d29b2e8c94e74ee832c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [mpipe_fake_src::src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md#a6e92423906560a787979923b93af0ce6)
- [mpipe_fake_src::pool](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md#a83bb72d761efa7ba80a8a9598b0c620d)

---

[上一章](P550_mpipe_element.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P552_mpipe_message.h_源码浏览.md)
