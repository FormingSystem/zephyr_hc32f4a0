---
id: learning.zephyr-docs.api-file-service-reference.page-24
title: zephyr__mpipe__utils__mpipe_dump.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_mpipe\_\_utils\_\_mpipe\_dump.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dump_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

绘制流水线拓扑（Pipeline Topology），供调试使用。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_bin.h>
#include <zephyr/mpipe/mpipe_structure.h>
```

查看此文件的源码。

绘制流水线拓扑（Pipeline Topology），供调试使用。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.1\_类型定义（Typedefs）

<a id="r_ga0215d4a9be34e7a5e58f8e11334ff507"></a>

```c
typedef void(* mpipe_dump_print_t) (void *ctx, const char *str)
```

相关声明：[mpipe_dump_print_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#ga0215d4a9be34e7a5e58f8e11334ff507)。

转储（Dump）的输出回调（Output Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.2\_函数（Functions）

<a id="r_gaa128307bee2a9cdba726f4a59313a8b2"></a>

```c
int mpipe_dump_bin (struct mpipe_bin *bin, mpipe_dump_print_t print, void *ctx)
```

相关声明：[mpipe_dump_bin](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gaa128307bee2a9cdba726f4a59313a8b2)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[mpipe_dump_print_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#ga0215d4a9be34e7a5e58f8e11334ff507)。

呈现元素容器（Bin）的拓扑（Topology）及其每个端口（Pad）的能力（Capability）。

<a id="r_gae215db838d4883132d79c08d0cec3eda"></a>

```c
int mpipe_dump_caps (const struct mpipe_structure *caps, mpipe_dump_print_t print, void *ctx)
```

相关声明：[mpipe_dump_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gae215db838d4883132d79c08d0cec3eda)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_dump_print_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#ga0215d4a9be34e7a5e58f8e11334ff507)。

在单行上呈现一个能力（Capability）。

<a id="r_gab3a73a3713a5b6fbcc961474c66f4bed"></a>

```c
const char * mpipe_dump_state_str (enum mpipe_state state)
```

相关声明：[mpipe_dump_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gab3a73a3713a5b6fbcc961474c66f4bed)、[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回元素状态（Element State）的名称。


## 24.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_bin.h](../api_source_configuration_reference/P058_mpipe_bin.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P549_mpipe_dump.h_源码浏览.md)
- [mpipe_dump_print_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#ga0215d4a9be34e7a5e58f8e11334ff507)
- [mpipe_dump_bin](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gaa128307bee2a9cdba726f4a59313a8b2)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [mpipe_dump_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gae215db838d4883132d79c08d0cec3eda)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_dump_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html#gab3a73a3713a5b6fbcc961474c66f4bed)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="header-details"></a>

---

[上一章](P023_zephyr__mpipe__mpipe_bin.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__mpipe__mpipe_message.h_文件参考.md)
