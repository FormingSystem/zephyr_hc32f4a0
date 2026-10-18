---
id: learning.zephyr-docs.api-file-runtime-reference.page-43
title: zephyr__mpipe__base__mpipe_tee.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_mpipe\_\_base\_\_mpipe\_tee.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__tee_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于流水线分支（Pipeline Branching）的分流元素（Tee）。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
```

查看此文件的源码。

用于流水线分支（Pipeline Branching）的分流元素（Tee Element）。它将单个输入分支（Input Branch）拆分为多个输出分支（Output Branches）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 43.1\_数据结构（Data Structures）

<a id="r_mpipe_5Ftee"></a>

```c
struct mpipe_tee
```

相关声明：[mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)。

分流元素（Tee Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 43.2\_枚举（Enumerations）

<a id="r_ga963f0d9cbcc79afcaea9de8fcd27e671"></a>

```c
enum mpipe_prop_base_tee { MPIPE_PROP_BASE_TEE_SRC_PADS_NUM }
```

相关声明：[mpipe_prop_base_tee](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga963f0d9cbcc79afcaea9de8fcd27e671)、[MPIPE_PROP_BASE_TEE_SRC_PADS_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2)。

分流元素属性标识（Tee Property Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.3\_函数（Functions）

<a id="r_ga3b4228b75ae8c2b6274240979c3a1162"></a>

```c
int mpipe_tee_init (struct mpipe_tee *tee, uint8_t id)
```

相关声明：[mpipe_tee_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga3b4228b75ae8c2b6274240979c3a1162)、[mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化分流元素（Tee Element）。


## 43.4\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pad.h](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P561_mpipe_tee.h_源码浏览.md)
- [mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)
- [mpipe_prop_base_tee](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga963f0d9cbcc79afcaea9de8fcd27e671)
- [MPIPE_PROP_BASE_TEE_SRC_PADS_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2)
- [mpipe_tee_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html#ga3b4228b75ae8c2b6274240979c3a1162)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P042_zephyr__mpipe__mpipe_sink.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__drivers__mspi_emul.h_文件参考.md)
