---
id: learning.zephyr-docs.api-source-reference.page-426
title: smp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第426章\_smp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html)。

## 426.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="akernel_2smp_8h_html_a33eb24503679583d853db1c4dc7e3812"></a>
<a id="akernel_2smp_8h_html_a39b4f48857baef688ee646bac36c882d"></a>
<a id="akernel_2smp_8h_html_abc49de5bf9e70f48e39f41c413f7cc74"></a>
<a id="astdbool_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_KERNEL_SMP_H_
#define ZEPHYR_INCLUDE_KERNEL_SMP_H_

#include <stdbool.h>

typedef void (*smp_init_fn)(void *arg);

void k_smp_cpu_start(int id, smp_init_fn fn, void *arg);

void k_smp_cpu_resume(int id, smp_init_fn fn, void *arg,
                      bool reinit_timer, bool invoke_sched);

#endif /* ZEPHYR_INCLUDE_KERNEL_SMP_H_ */
```

## 426.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KERNEL_SMP_H_`。

## 426.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [smp_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html#abc49de5bf9e70f48e39f41c413f7cc74)
- [k_smp_cpu_start](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html#a33eb24503679583d853db1c4dc7e3812)
- [k_smp_cpu_resume](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html#a39b4f48857baef688ee646bac36c882d)

---

[上一章](P425_its_ids.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P427_stats.h_源码浏览.md)
