---
id: learning.zephyr-docs.api-source-reference.page-427
title: stats.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel_2stats_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第427章\_stats.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2stats_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2stats_8h.html)。

## 427.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00017"></a>
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructk__cycle__stats_html"></a>
<a id="astructk__cycle__stats_html_a161c8d21c7d4a3d21c7cce87237c8334"></a>
<a id="astructk__cycle__stats_html_a1d49158db605872cd8d31225c0ae8ab5"></a>
<a id="astructk__cycle__stats_html_a8a955f987ddc88ff587edab8cb71dd6f"></a>
<a id="astructk__cycle__stats_html_a9c12b140936bcc4a8630c68680a245b4"></a>
<a id="astructk__cycle__stats_html_acdb6a6b005384535607aaf1bc5dd3feb"></a>

```c
/*
 * Copyright (c) 2021,2023, Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_KERNEL_STATS_H_
#define ZEPHYR_INCLUDE_KERNEL_STATS_H_

#include <stdint.h>
#include <stdbool.h>


struct k_cycle_stats {
        uint64_t  total;
#if defined(CONFIG_SCHED_THREAD_USAGE_ANALYSIS) || defined(__DOXYGEN__)
        uint64_t  current;
        uint64_t  longest;
        uint32_t  num_windows;
#endif /* CONFIG_SCHED_THREAD_USAGE_ANALYSIS */
        bool      track_usage;
};

#endif /* ZEPHYR_INCLUDE_KERNEL_STATS_H_ */
```

## 427.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021,2023, Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

条件编译配置（Configuration）标记：`CONFIG_SCHED_THREAD_USAGE_ANALYSIS`。

### 注释 3：原第 33 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KERNEL_STATS_H_`。

## 427.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2stats_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [k_cycle_stats](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [total](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a1d49158db605872cd8d31225c0ae8ab5)
- [current](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a9c12b140936bcc4a8630c68680a245b4)
- [longest](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a161c8d21c7d4a3d21c7cce87237c8334)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [num_windows](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#acdb6a6b005384535607aaf1bc5dd3feb)
- [track_usage](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a8a955f987ddc88ff587edab8cb71dd6f)
- [k_cycle_stats::longest](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a161c8d21c7d4a3d21c7cce87237c8334)
- [k_cycle_stats::total](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a1d49158db605872cd8d31225c0ae8ab5)
- [k_cycle_stats::track_usage](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a8a955f987ddc88ff587edab8cb71dd6f)
- [k_cycle_stats::current](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#a9c12b140936bcc4a8630c68680a245b4)
- [k_cycle_stats::num_windows](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md#acdb6a6b005384535607aaf1bc5dd3feb)

---

[上一章](P426_smp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P428_kernel_includes.h_源码浏览.md)
