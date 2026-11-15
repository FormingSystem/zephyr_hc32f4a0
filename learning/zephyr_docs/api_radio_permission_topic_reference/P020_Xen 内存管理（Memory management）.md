---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-20
title: Xen 内存管理（Memory management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_Xen 内存管理（Memory management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理域的物理映射（Physmaps）和由 Xen 拥有的资源。

<a id="details"></a>

管理域的物理映射（Physmaps）和由 Xen 拥有的资源。

<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_memory_2Eh"></a>

```c
file memory.h
```

相关声明：[memory.h](../api_file_system_device_reference/P026_zephyr__xen__memory.h_文件参考.md)。

Xen内存管理（Memory Management）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.2\_函数（Functions）

<a id="r_gab548b9bcc4479f33f3d8b8467dc6855f"></a>

```c
int xendom_add_to_physmap (int domid, unsigned long idx, unsigned int space, xen_pfn_t gpfn)
```

相关声明：[xendom_add_to_physmap](#gab548b9bcc4479f33f3d8b8467dc6855f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

向域（domain）的物理映射（physmap）添加单个映射。

<a id="r_gad3a6f591da88d9781fd08c197a7f933b"></a>

```c
int xendom_add_to_physmap_batch (int domid, int foreign_domid, unsigned int space, unsigned int size, xen_ulong_t *idxs, xen_pfn_t *gpfns, int *errs)
```

相关声明：[xendom_add_to_physmap_batch](#gad3a6f591da88d9781fd08c197a7f933b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

向域的物理映射添加多个映射。

<a id="r_gae4c9930819726c7ce77725649c03dedf"></a>

```c
int xendom_remove_from_physmap (int domid, xen_pfn_t gpfn)
```

相关声明：[xendom_remove_from_physmap](#gae4c9930819726c7ce77725649c03dedf)。

从域的物理映射移除映射。

<a id="r_ga7c538490f4f15e71d79ee9de4d3160cb"></a>

```c
int xendom_increase_reservation (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_increase_reservation](#ga7c538490f4f15e71d79ee9de4d3160cb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

增加域的内存预留（memory reservation）。

<a id="r_ga68b8323ed437eb4f501276e8678aa6b7"></a>

```c
int xendom_decrease_reservation (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_decrease_reservation](#ga68b8323ed437eb4f501276e8678aa6b7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

减少域的内存预留。

<a id="r_ga7fe2ce11ffa483afa33d95b7cf61520b"></a>

```c
int xendom_populate_physmap (int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t *extent_start)
```

相关声明：[xendom_populate_physmap](#ga7fe2ce11ffa483afa33d95b7cf61520b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

为客户机页帧（guest frames）填充内存。

<a id="r_ga1890a7a1b7137b009e8488049ab36bf4"></a>

```c
int xendom_acquire_resource (domid_t domid, uint16_t type, uint32_t id, uint64_t frame, uint32_t *nr_frames, xen_pfn_t *frame_list)
```

相关声明：[xendom_acquire_resource](#ga1890a7a1b7137b009e8488049ab36bf4)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为域获取由 Xen 管理的资源映射（resource mapping）。

## 20.3\_详细说明（Detailed Documentation）

<a id="ga1890a7a1b7137b009e8488049ab36bf4"></a>

### `xendom_acquire_resource()`

```c
int xendom_acquire_resource ( domid_t domid, uint16_t type, uint32_t id, uint64_t frame, uint32_t * nr_frames, xen_pfn_t * frame_list )
```

```c
#include <zephyr/xen/memory.h>
```

为域获取由 Xen 管理的资源映射（resource mapping）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 目标域标识符（Target Domain Identifier）。 |
| ` type` | Xen 资源类型（Resource Type），例如 XENMEM_resource_ioreq_server。 |
| ` id` | 资源实例标识符（Resource Instance Identifier），其含义由 type 决定。 |
| ` frame` | Xen 资源中的起始页框（Starting Frame）；*nr_frames 为 0，即查询大小时忽略。 |
| `[in,out] nr_frames` | 输入时为要获取的页框数量；返回时为 Xen 针对此请求报告的页框数量。 |
| `[out] frame_list` | 客户机页框列表缓冲区（Guest Frame List Buffer）：对于 HVM 客户机，输入 GFN；对于 PV 客户机，输出 MFN。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gab548b9bcc4479f33f3d8b8467dc6855f"></a>

### `xendom_add_to_physmap()`

```c
int xendom_add_to_physmap ( int domid, unsigned long idx, unsigned int space, xen_pfn_t gpfn )
```

```c
#include <zephyr/xen/memory.h>
```

向域（domain）的物理映射（physmap）添加单个映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要更新其物理地址映射（Physmap）的域；非特权调用方必须使用 DOMID_SELF。 |
| `idx` | space 所标识的 Xen 映射空间（Mapping Space）中的索引。 |
| `space` | 映射空间选择器（Mapping Space Selector），通常为 XENMAPSPACE_* 常量之一。 |
| `gpfn` | 映射将出现于其上的客户机页框号（Guest Frame Number）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gad3a6f591da88d9781fd08c197a7f933b"></a>

### `xendom_add_to_physmap_batch()`

```c
int xendom_add_to_physmap_batch ( int domid, int foreign_domid, unsigned int space, unsigned int size, xen_ulong_t * idxs, xen_pfn_t * gpfns, int * errs )
```

```c
#include <zephyr/xen/memory.h>
```

向域的物理映射添加多个映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 要更新其物理地址映射（Physmap）的域；非特权调用方必须使用 DOMID_SELF。 |
| ` foreign_domid` | 与 XENMAPSPACE_gmfn_foreign 配合使用的外部域标识符（Foreign Domain Identifier）；其他映射空间传 0。 |
| ` space` | 映射空间选择器（Mapping Space Selector），通常为 XENMAPSPACE_* 常量之一。 |
| ` size` | 数组描述的映射数量（Number of Mappings）。 |
| ` idxs` | 映射空间索引数组（Mapping-space Indexes）。 |
| ` gpfns` | 接收映射的客户机页框号数组（Guest Frame Numbers）。 |
| `[out] errs` | 用于接收各条目 Xen 状态码（Status Code）的数组。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga68b8323ed437eb4f501276e8678aa6b7"></a>

### `xendom_decrease_reservation()`

```c
int xendom_decrease_reservation ( int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t * extent_start )
```

```c
#include <zephyr/xen/memory.h>
```

减少域的内存预留。

请求 Xen 从某个域的预留内存（Reservation）中释放客户机页框区段（Guest Frame Extents）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要减少其预留内存（Reservation）的域；非特权调用方必须使用 DOMID_SELF。 |
| `extent_order` | Xen 使用的区段阶数（Extent Order），每个区段覆盖 2^extent_order 页。 |
| `nr_extents` | 要释放的区段（Extents）数量。 |
| `mem_flags` | Xen 内存标志（Memory Flags），例如 XENMEMF_* 常量。 |
| `extent_start` | 待释放的客户机页框基址数组（Guest Frame Bases）。 |

**返回（Returns）**：返回值（Returns）：成功返回已释放区段（Extents）的数量，失败返回负 errno。

<a id="ga7c538490f4f15e71d79ee9de4d3160cb"></a>

### `xendom_increase_reservation()`

```c
int xendom_increase_reservation ( int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t * extent_start )
```

```c
#include <zephyr/xen/memory.h>
```

增加域的内存预留（memory reservation）。

请求 Xen 为域分配区段（Extents）。成功时，Xen 将已分配的机器页框基址（Machine Frame Bases）写入 extent_start。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 要增加其预留内存（Reservation）的域；非特权调用方必须使用 DOMID_SELF。 |
| ` extent_order` | Xen 使用的区段阶数（Extent Order），每个区段覆盖 2^extent_order 页。 |
| ` nr_extents` | 请求的区段（Extents）数量。 |
| ` mem_flags` | Xen 内存标志（Memory Flags），例如 XENMEMF_* 常量。 |
| `[out] extent_start` | 用于接收已分配机器页框基址（Machine Frame Bases）的数组。 |

**返回（Returns）**：返回值（Returns）：成功返回已分配区段（Extents）的数量，失败返回负 errno。

<a id="ga7fe2ce11ffa483afa33d95b7cf61520b"></a>

### `xendom_populate_physmap()`

```c
int xendom_populate_physmap ( int domid, unsigned int extent_order, unsigned int nr_extents, unsigned int mem_flags, xen_pfn_t * extent_start )
```

```c
#include <zephyr/xen/memory.h>
```

为客户机页帧（guest frames）填充内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要填充其物理地址映射（Physmap）的域；非特权调用方必须使用 DOMID_SELF。 |
| `extent_order` | Xen 使用的区段阶数（Extent Order），每个区段覆盖 2^extent_order 页。 |
| `nr_extents` | extent_start 中的条目数量。 |
| `mem_flags` | Xen 内存标志（Memory Flags），Arm 客户机目前传 0。 |
| `extent_start` | 用于接收填充区段的客户机页框号数组（Guest Frame Numbers）。 |

**返回（Returns）**：返回值（Returns）：成功返回已填充区段（Extents）的数量，失败返回负 errno。

<a id="gae4c9930819726c7ce77725649c03dedf"></a>

### `xendom_remove_from_physmap()`

```c
int xendom_remove_from_physmap ( int domid, xen_pfn_t gpfn )
```

```c
#include <zephyr/xen/memory.h>
```

从域的物理映射移除映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要更新其物理地址映射（Physmap）的域；非特权调用方必须使用 DOMID_SELF。 |
| `gpfn` | 要移除的客户机页框号（Guest Frame Number）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 20.4\_原页交叉引用（Cross References）

- [memory.h](../api_file_system_device_reference/P026_zephyr__xen__memory.h_文件参考.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_Xen 授权表（Grant tables）.md) · [返回大纲](大纲.md)
