---
id: learning.zephyr-docs.api-source-reference.page-513
title: memory.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memory_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第513章\_memory.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/memory_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/memory_8h.html)。

## 513.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="agroup__xen__memory__management_html_ga1890a7a1b7137b009e8488049ab36bf4"></a>
<a id="agroup__xen__memory__management_html_ga68b8323ed437eb4f501276e8678aa6b7"></a>
<a id="agroup__xen__memory__management_html_ga7c538490f4f15e71d79ee9de4d3160cb"></a>
<a id="agroup__xen__memory__management_html_ga7fe2ce11ffa483afa33d95b7cf61520b"></a>
<a id="agroup__xen__memory__management_html_gab548b9bcc4479f33f3d8b8467dc6855f"></a>
<a id="agroup__xen__memory__management_html_gad3a6f591da88d9781fd08c197a7f933b"></a>
<a id="agroup__xen__memory__management_html_gae4c9930819726c7ce77725649c03dedf"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
/* SPDX-License-Identifier: Apache-2.0 */
/*
 * Copyright (c) 2023 EPAM Systems
 */


#ifndef ZEPHYR_INCLUDE_XEN_MEMORY_H_
#define ZEPHYR_INCLUDE_XEN_MEMORY_H_

#include <xen/public/xen.h>
#include <xen/public/memory.h>

#include <zephyr/kernel.h>


int xendom_add_to_physmap(int domid, unsigned long idx, unsigned int space,
                          xen_pfn_t gpfn);

int xendom_add_to_physmap_batch(int domid, int foreign_domid,
                                unsigned int space, unsigned int size,
                                xen_ulong_t *idxs, xen_pfn_t *gpfns, int *errs);

int xendom_remove_from_physmap(int domid, xen_pfn_t gpfn);

int xendom_increase_reservation(int domid, unsigned int extent_order,
                                unsigned int nr_extents, unsigned int mem_flags,
                                xen_pfn_t *extent_start);

int xendom_decrease_reservation(int domid, unsigned int extent_order,
                                unsigned int nr_extents, unsigned int mem_flags,
                                xen_pfn_t *extent_start);

int xendom_populate_physmap(int domid, unsigned int extent_order,
                            unsigned int nr_extents, unsigned int mem_flags,
                            xen_pfn_t *extent_start);

int xendom_acquire_resource(domid_t domid, uint16_t type, uint32_t id, uint64_t frame,
                            uint32_t *nr_frames, xen_pfn_t *frame_list);


#endif /* ZEPHYR_INCLUDE_XEN_MEMORY_H_ */
```

## 513.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 2 行

版权（Copyright）：© 2023 EPAM Systems。

### 注释 3：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_MEMORY_H_`。

## 513.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/memory_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [xendom_add_to_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gab548b9bcc4479f33f3d8b8467dc6855f)
- [xendom_add_to_physmap_batch](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gad3a6f591da88d9781fd08c197a7f933b)
- [xendom_remove_from_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gae4c9930819726c7ce77725649c03dedf)
- [xendom_increase_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7c538490f4f15e71d79ee9de4d3160cb)
- [xendom_decrease_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga68b8323ed437eb4f501276e8678aa6b7)
- [xendom_populate_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7fe2ce11ffa483afa33d95b7cf61520b)
- [xendom_acquire_resource](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga1890a7a1b7137b009e8488049ab36bf4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P512_memc_stm32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P514_mesh.h_源码浏览.md)
