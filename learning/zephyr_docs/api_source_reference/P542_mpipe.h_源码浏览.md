---
id: learning.zephyr-docs.api-source-reference.page-542
title: mpipe.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第542章\_mpipe.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe_8h.html)。

## 542.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00026"></a>
<a id="l00066"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="ampipe__bin_8h_html"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__dispatch_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__message_8h_html"></a>
<a id="ampipe__object_8h_html"></a>
<a id="ampipe__pad_8h_html"></a>
<a id="ampipe__parser_8h_html"></a>
<a id="ampipe__pipeline_8h_html"></a>
<a id="ampipe__sink_8h_html"></a>
<a id="ampipe__src_8h_html"></a>
<a id="ampipe__structure_8h_html"></a>
<a id="ampipe__transform_8h_html"></a>
<a id="ampipe__transform__client_8h_html"></a>
<a id="ampipe__value_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_H_




#include <zephyr/mpipe/mpipe_bin.h>
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_dispatch.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_message.h>
#include <zephyr/mpipe/mpipe_object.h>
#include <zephyr/mpipe/mpipe_pad.h>
#include <zephyr/mpipe/mpipe_parser.h>
#include <zephyr/mpipe/mpipe_pipeline.h>
#include <zephyr/mpipe/mpipe_sink.h>
#include <zephyr/mpipe/mpipe_src.h>
#include <zephyr/mpipe/mpipe_structure.h>
#include <zephyr/mpipe/mpipe_transform.h>
#include <zephyr/mpipe/mpipe_value.h>
#if defined(CONFIG_MPIPE_RPC)
#include <zephyr/mpipe/mpipe_transform_client.h>
#endif

#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_H_ */
```

## 542.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 96 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_H_`。

## 542.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe_8h.html)
- [zephyr/mpipe/mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_dispatch.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [zephyr/mpipe/mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [zephyr/mpipe/mpipe_parser.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html)
- [zephyr/mpipe/mpipe_pipeline.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)
- [zephyr/mpipe/mpipe_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)
- [zephyr/mpipe/mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [zephyr/mpipe/mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [zephyr/mpipe/mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)
- [zephyr/mpipe/mpipe_transform_client.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html)
- [mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_dispatch.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)
- [mpipe_parser.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__parser_8h.html)
- [mpipe_pipeline.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pipeline_8h.html)
- [mpipe_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__sink_8h.html)
- [mpipe_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)
- [mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)
- [mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [mpipe_transform_client.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html)
- [mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)

---

[上一章](P541_openthread.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P543_mpipe_app_sink.h_源码浏览.md)
