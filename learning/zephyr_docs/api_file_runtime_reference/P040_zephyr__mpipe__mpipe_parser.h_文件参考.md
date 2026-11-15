---
id: learning.zephyr-docs.api-file-runtime-reference.page-40
title: zephyr__mpipe__mpipe_parser.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_mpipe\_\_mpipe\_parser.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流解析器基础元素（Stream Parser Base Element）。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
```

查看此文件的源码。

流解析器基础元素（Stream Parser Base Element）。提供一个基类（Base Class），供将传入数据积累为完整帧（Complete Frames）、再向下游推送（Push Downstream）的元素使用。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 40.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fparser"></a>

```c
struct mpipe_parser
```

相关声明：[mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)。

基础解析器元素（Base Parser Element）的结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.2\_函数（Functions）

<a id="r_ga17fc0c53e8166bdde12176ee2ac7bdb1"></a>

```c
int mpipe_parser_init (struct mpipe_parser *parser, uint8_t id)
```

相关声明：[mpipe_parser_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga17fc0c53e8166bdde12176ee2ac7bdb1)、[mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化解析器元素（Parser Element）。

<a id="r_ga433bfb9df636fa51e737acc3ecc0b69f"></a>

```c
int mpipe_parser_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_parser_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga433bfb9df636fa51e737acc3ecc0b69f)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础解析器元素（Base Parser Element）的状态切换函数（Change State Function）。


## 40.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pad.h](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P555_mpipe_parser.h_源码浏览.md)
- [mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)
- [mpipe_parser_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga17fc0c53e8166bdde12176ee2ac7bdb1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_parser_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html#ga433bfb9df636fa51e737acc3ecc0b69f)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)

<a id="header-details"></a>

---

[上一章](P039_zephyr__mpipe__base__mpipe_caps_filter.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__mpipe__mpipe_pipeline.h_文件参考.md)
