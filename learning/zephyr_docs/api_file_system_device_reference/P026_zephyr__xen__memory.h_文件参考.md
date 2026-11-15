---
id: learning.zephyr-docs.api-file-system-device-reference.page-26
title: zephyr__xen__memory.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memory_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_xen\_\_memory.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/memory_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen内存管理（Memory Management）的操作。

<a id="details"></a>

```c
#include <xen/public/xen.h>
#include <xen/public/memory.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

Xen内存管理（Memory Management）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.1\_函数（Functions）

<a id="r_gab548b9bcc4479f33f3d8b8467dc6855f"></a>

```c
int xendom_add_to_physmap (int domid, unsigned long idx, unsigned int space, xen_pfn_t gpfn)
```

相关声明：[xendom_add_to_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gab548b9bcc4479f33f3d8b8467dc6855f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

向域（domain）的物理映射（physmap）添加单个映射。

<a id="r_gad3a6f591da88d9781fd08c197a7f933b"></a>

```c
int xendom_add_to_physmap_batch (int domid, int foreign_domid, unsigned int space, unsigned int size, xen_ulong_t *idxs, xen_pfn_t *gpfns, int *errs)
```

相关声明：[xendom_add_to_physmap_batch](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gad3a6f591da88d9781fd08c197a7f933b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

向域的物理映射添加多个映射。

<a id="r_gae4c9930819726c7ce77725649c03dedf"></a>

```c
int xendom_remove_from_physmap (int domid, xen_pfn_t gpfn)
```

相关声明：[xendom_remove_from_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gae4c9930819726c7ce77725649c03dedf)。

从域的物理映射移除映射。

<a id="r_ga7c538490f4f15e71d79ee9de4d3160cb"></a>

```c
int xendom_increase_reservation (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_increase_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7c538490f4f15e71d79ee9de4d3160cb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

增加域的内存预留（memory reservation）。

<a id="r_ga68b8323ed437eb4f501276e8678aa6b7"></a>

```c
int xendom_decrease_reservation (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_decrease_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga68b8323ed437eb4f501276e8678aa6b7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

减少域的内存预留。

<a id="r_ga7fe2ce11ffa483afa33d95b7cf61520b"></a>

```c
int xendom_populate_physmap (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_populate_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7fe2ce11ffa483afa33d95b7cf61520b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

为客户机页帧（guest frames）填充内存。

<a id="r_ga1890a7a1b7137b009e8488049ab36bf4"></a>

```c
int xendom_acquire_resource (domid_t domid, uint16_t type, uint32_t id, uint64_t frame, uint32_t *nr_frames, xen_pfn_t *frame_list)
```

相关声明：[xendom_acquire_resource](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga1890a7a1b7137b009e8488049ab36bf4)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为域获取由 Xen 管理的资源映射（resource mapping）。


## 26.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P513_memory.h_源码浏览.md)
- [xendom_add_to_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gab548b9bcc4479f33f3d8b8467dc6855f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [xendom_add_to_physmap_batch](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gad3a6f591da88d9781fd08c197a7f933b)
- [xendom_remove_from_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#gae4c9930819726c7ce77725649c03dedf)
- [xendom_increase_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7c538490f4f15e71d79ee9de4d3160cb)
- [xendom_decrease_reservation](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga68b8323ed437eb4f501276e8678aa6b7)
- [xendom_populate_physmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga7fe2ce11ffa483afa33d95b7cf61520b)
- [xendom_acquire_resource](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html#ga1890a7a1b7137b009e8488049ab36bf4)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>

---

[上一章](P025_zephyr__pmci__mctp__mctp_memory.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__modem__ppp.h_文件参考.md)
