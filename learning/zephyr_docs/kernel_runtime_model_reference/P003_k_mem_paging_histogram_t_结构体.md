---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-3
title: k_mem_paging_histogram_t_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__mem__paging__histogram__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_k\_mem\_paging\_histogram\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__mem__paging__histogram__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分页统计直方图（Paging Statistics Histograms）。

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

<a id="details"></a>

分页统计直方图（Paging Statistics Histograms）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a4421676cbc9f6c63808ee914e2ff8c90"></a>

```c
unsigned long counts [CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[counts](#a4421676cbc9f6c63808ee914e2ff8c90)。

<a id="r_a893236502aeb56975263b27cf4f2755a"></a>

```c
unsigned long bounds [CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[bounds](#a893236502aeb56975263b27cf4f2755a)。

## 3.2\_详细说明（Detailed Documentation）

<a id="a893236502aeb56975263b27cf4f2755a"></a>

### `bounds`

```c
unsigned long k_mem_paging_histogram_t::bounds[CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS]
```

<a id="a4421676cbc9f6c63808ee914e2ff8c90"></a>

### `counts`

```c
unsigned long k_mem_paging_histogram_t::counts[CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS]
```

本数据类型文档由以下文件生成：

- `zephyr/kernel/mm/demand_paging.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/kernel/mm/demand_paging.h](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_k_ipi_work_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_k_mem_paging_stats_t_结构体.md)
