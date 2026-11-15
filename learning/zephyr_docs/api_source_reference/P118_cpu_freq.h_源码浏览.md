---
id: learning.zephyr-docs.api-source-reference.page-118
title: cpu_freq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_cpu\_freq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P027_CPU调频头文件.md)。

## 118.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="agroup__subsys__cpu__freq_html_ga05ad73b533df51a0f70e6883e6e0bdf3"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="apstate_8h_html"></a>
<a id="astructpstate_html"></a>

```c
/*
 * Copyright (c) 2025 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_CPU_FREQ_CPU_FREQ_H_
#define ZEPHYR_INCLUDE_CPU_FREQ_CPU_FREQ_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/types.h>
#include <zephyr/cpu_freq/pstate.h>


int cpu_freq_pstate_set(const struct pstate *state);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_CPU_FREQ_CPU_FREQ_H_ */
```

## 118.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_CPU_FREQ_CPU_FREQ_H_`。

## 118.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P027_CPU调频头文件.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/cpu_freq/pstate.h](../power/P029_性能状态头文件.md)
- [cpu_freq_pstate_set](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq.html#ga05ad73b533df51a0f70e6883e6e0bdf3)
- [pstate](../power/P026_性能状态结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [pstate.h](../power/P029_性能状态头文件.md)

---

[上一章](P117_controls.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P119_cst8xx-gesture-codes.h_源码浏览.md)
