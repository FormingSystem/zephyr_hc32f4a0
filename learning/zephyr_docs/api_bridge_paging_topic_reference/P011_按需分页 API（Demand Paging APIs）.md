---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-11
title: 按需分页 API（Demand Paging APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_按需分页 API（Demand Paging APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_k_5Fmem_5Fpaging_5Fstats_5Ft"></a>

```c
struct k_mem_paging_stats_t
```

相关声明：[k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)。

分页统计信息（Paging Statistics）。

<a id="r_k_5Fmem_5Fpaging_5Fhistogram_5Ft"></a>

```c
struct k_mem_paging_histogram_t
```

相关声明：[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

分页统计直方图（Paging Statistics Histograms）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_ga0b18037209b4d8b5964bd9a1d760f703"></a>

```c
int k_mem_page_out (void *addr, size_t size)
```

相关声明：[k_mem_page_out](#ga0b18037209b4d8b5964bd9a1d760f703)。

将按页对齐的虚拟内存区域（Page-aligned Virtual Memory Region）换出到后备存储（Backing Store）。

<a id="r_gab36c36a4e230677d2090514f7a34b408"></a>

```c
void k_mem_page_in (void *addr, size_t size)
```

相关声明：[k_mem_page_in](#gab36c36a4e230677d2090514f7a34b408)。

将虚拟数据区域（Virtual Data Region）载入内存。

<a id="r_ga5f2d422edde7d366e81a870ce057589f"></a>

```c
void k_mem_pin (void *addr, size_t size)
```

相关声明：[k_mem_pin](#ga5f2d422edde7d366e81a870ce057589f)。

固定（Pin）对齐的虚拟数据区域，必要时将其调页载入（Page In）。

<a id="r_ga3278aae5e24733c722b7d83c4b17dab3"></a>

```c
void k_mem_unpin (void *addr, size_t size)
```

相关声明：[k_mem_unpin](#ga3278aae5e24733c722b7d83c4b17dab3)。

解除对齐虚拟数据区域的固定（Unpin）。

<a id="r_ga52ad88e0c0eed2aa27331bfd4707b7ec"></a>

```c
void k_mem_paging_stats_get (struct k_mem_paging_stats_t *stats)
```

相关声明：[k_mem_paging_stats_get](#ga52ad88e0c0eed2aa27331bfd4707b7ec)、[k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)。

获取系统启动以来的分页统计（Paging Statistics）。

<a id="r_gafad6b39cb2faf3bb416cd4d3faaa8d8c"></a>

```c
void k_mem_paging_thread_stats_get (struct k_thread *thread, struct k_mem_paging_stats_t *stats)
```

相关声明：[k_mem_paging_thread_stats_get](#gafad6b39cb2faf3bb416cd4d3faaa8d8c)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)。

获取线程自系统启动以来的分页统计（Paging Statistics）。

<a id="r_gaec64d019d819b00c7bc3804aac269199"></a>

```c
void k_mem_paging_histogram_eviction_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_eviction_get](#gaec64d019d819b00c7bc3804aac269199)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取换出计时直方图（Eviction Timing Histogram）。

<a id="r_ga1da0a643e8f85f98e29288e441a37dfa"></a>

```c
void k_mem_paging_histogram_backing_store_page_in_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_backing_store_page_in_get](#ga1da0a643e8f85f98e29288e441a37dfa)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取后备存储调入计时直方图（Backing Store Page-in Timing Histogram）。

<a id="r_gae4f80d14f88a46ddb9aeb7afba861864"></a>

```c
void k_mem_paging_histogram_backing_store_page_out_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_backing_store_page_out_get](#gae4f80d14f88a46ddb9aeb7afba861864)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取后备存储调出计时直方图（Backing Store Page-out Timing Histogram）。

## 11.3\_详细说明（Detailed Documentation）

<a id="gab36c36a4e230677d2090514f7a34b408"></a>

### `k_mem_page_in()`

```c
void k_mem_page_in ( void * addr, size_t size )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

将虚拟数据区域（Virtual Data Region）载入内存。

函数完成后，与此函数操作相关的所有页框（Page Frames）都会被调入，但不保证它们持续驻留。若已知即将使用该内存区域，此操作很有用。

若启用了 `CONFIG_DEMAND_PAGING_ALLOW_IRQ`，中断服务例程（ISR）不得调用此函数，因为后备存储（Backing Store）可能正在使用中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的虚拟基地址（Page-aligned Virtual Base Address）。 |
| `size` | 按页对齐的数据区域大小（Page-aligned Data Region Size）。 |

<a id="ga0b18037209b4d8b5964bd9a1d760f703"></a>

### `k_mem_page_out()`

```c
int k_mem_page_out ( void * addr, size_t size )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

将按页对齐的虚拟内存区域（Page-aligned Virtual Memory Region）换出到后备存储（Backing Store）。

若已知某个内存区域将在一段时间内不被使用，此操作很有用。指定区域中尚未换出的所有数据页都会被逐出到后备存储（Backing Store），相应页框（Page Frames）会被标记为可用于映射（Mappings）或调入（Page-ins）。

映射到所给区域的任何关联页框（Page Frames）都不应处于固定状态（Pinned）。

注意：无法保证这些页被逐出后能保持多久；它们可能立即发生缺页异常（Page Faults）。

若启用了 `CONFIG_DEMAND_PAGING_ALLOW_IRQ`，中断服务例程（ISR）不得调用此函数，因为后备存储（Backing Store）可能正在使用中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的虚拟基地址（Page-aligned Virtual Base Address）。 |
| `size` | 按页对齐的数据区域大小（Page-aligned Data Region Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 后备存储（Backing Store）空间不足以满足请求。该区域可能已部分换出（Paged Out）。 |

<a id="ga1da0a643e8f85f98e29288e441a37dfa"></a>

### `k_mem_paging_histogram_backing_store_page_in_get()`

```c
void k_mem_paging_histogram_backing_store_page_in_get ( struct k_mem_paging_histogram_t * hist)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取后备存储调入计时直方图（Backing Store Page-in Timing Histogram）。

填充作为参数传入的计时直方图结构体（Timing Histogram Struct）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] hist` | 要填充的计时直方图结构体（Timing Histogram Struct）。 |

<a id="gae4f80d14f88a46ddb9aeb7afba861864"></a>

### `k_mem_paging_histogram_backing_store_page_out_get()`

```c
void k_mem_paging_histogram_backing_store_page_out_get ( struct k_mem_paging_histogram_t * hist)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取后备存储调出计时直方图（Backing Store Page-out Timing Histogram）。

填充作为参数传入的计时直方图结构体（Timing Histogram Struct）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] hist` | 要填充的计时直方图结构体（Timing Histogram Struct）。 |

<a id="gaec64d019d819b00c7bc3804aac269199"></a>

### `k_mem_paging_histogram_eviction_get()`

```c
void k_mem_paging_histogram_eviction_get ( struct k_mem_paging_histogram_t * hist)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取换出计时直方图（Eviction Timing Histogram）。

填充作为参数传入的计时直方图结构体（Timing Histogram Struct）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] hist` | 要填充的计时直方图结构体（Timing Histogram Struct）。 |

<a id="ga52ad88e0c0eed2aa27331bfd4707b7ec"></a>

### `k_mem_paging_stats_get()`

```c
void k_mem_paging_stats_get ( struct k_mem_paging_stats_t * stats)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取系统启动以来的分页统计（Paging Statistics）。

填充作为参数传入的分页统计结构体（Paging Statistics Struct）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] stats` | 要填充的分页统计结构体（Paging Statistics Struct）。 |

<a id="gafad6b39cb2faf3bb416cd4d3faaa8d8c"></a>

### `k_mem_paging_thread_stats_get()`

```c
void k_mem_paging_thread_stats_get ( struct k_thread * thread, struct k_mem_paging_stats_t * stats )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取线程自系统启动以来的分页统计（Paging Statistics）。

将特定线程的分页统计（Paging Statistics）填入作为参数传入的结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] thread` | 线程（Thread） |
| `[in,out] stats` | 要填充的分页统计结构体（Paging Statistics Struct）。 |

<a id="ga5f2d422edde7d366e81a870ce057589f"></a>

### `k_mem_pin()`

```c
void k_mem_pin ( void * addr, size_t size )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

固定（Pin）对齐的虚拟数据区域，必要时将其调页载入（Page In）。

函数完成后，与此区域关联的所有页框（Page Frames）都会驻留在内存中，并被固定（Pinned），以确保它们保持驻留。这是比 `z_mem_page_in()` 更强的操作。

若启用了 `CONFIG_DEMAND_PAGING_ALLOW_IRQ`，中断服务例程（ISR）不得调用此函数，因为后备存储（Backing Store）可能正在使用中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的虚拟基地址（Page-aligned Virtual Base Address）。 |
| `size` | 按页对齐的数据区域大小（Page-aligned Data Region Size）。 |

<a id="ga3278aae5e24733c722b7d83c4b17dab3"></a>

### `k_mem_unpin()`

```c
void k_mem_unpin ( void * addr, size_t size )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

解除对齐虚拟数据区域的固定（Unpin）。

函数完成后，与此区域关联的所有页框（Page Frames）都会取消固定（Pinned）标记。此操作不会逐出该区域；若需要逐出，请随后调用 `z_mem_page_out()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的虚拟基地址（Page-aligned Virtual Base Address）。 |
| `size` | 按页对齐的数据区域大小（Page-aligned Data Region Size）。 |


## 11.4\_原页交叉引用（Cross References）

- [k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)
- [k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [zephyr/kernel/mm/demand_paging.h](../api_file_paging_wakeup_reference/P001_zephyr__kernel__mm__demand_paging.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_LSM6DSO16IS API主题.md) · [返回大纲](大纲.md) · [下一章](P012_应用源（Application sources）.md)
