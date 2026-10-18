---
id: learning.zephyr-docs.api-file-runtime-reference.page-42
title: zephyr__mpipe__mpipe_sink.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_mpipe\_\_mpipe\_sink.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收端（Sink）：消耗缓冲区的元素。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
```

查看此文件的源码。

接收端（Sink）：消耗缓冲区的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 42.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fsink"></a>

```c
struct mpipe_sink
```

相关声明：[mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)。

接收端元素（Sink Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 42.2\_枚举（Enumerations）

<a id="r_ga87a63291ab124bd59e51a57f64446d01"></a>

```c
enum mpipe_prop_sink { MPIPE_PROP_SINK_LAST }
```

相关声明：[mpipe_prop_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga87a63291ab124bd59e51a57f64446d01)、[MPIPE_PROP_SINK_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b)。

汇端元素属性（Sink Element Properties）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.3\_函数（Functions）

<a id="r_ga8c19ec865af49f6e320161582b2dd5ae"></a>

```c
int mpipe_sink_init (struct mpipe_sink *sink, uint8_t id)
```

相关声明：[mpipe_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga8c19ec865af49f6e320161582b2dd5ae)、[mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化汇端元素（Sink Element）。

<a id="r_ga6461b51403968217a6bc568cbb990250"></a>

```c
int mpipe_sink_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_sink_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga6461b51403968217a6bc568cbb990250)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础汇端元素（Base Sink Element）的状态切换函数（Change State Function）。


## 42.4\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pad.h](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P558_mpipe_sink.h_源码浏览.md)
- [mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)
- [mpipe_prop_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga87a63291ab124bd59e51a57f64446d01)
- [MPIPE_PROP_SINK_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b)
- [mpipe_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga8c19ec865af49f6e320161582b2dd5ae)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_sink_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html#ga6461b51403968217a6bc568cbb990250)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)

<a id="header-details"></a>

---

[上一章](P041_zephyr__mpipe__mpipe_pipeline.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__mpipe__base__mpipe_tee.h_文件参考.md)
