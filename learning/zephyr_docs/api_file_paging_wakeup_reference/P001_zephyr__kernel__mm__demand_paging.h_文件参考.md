---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-1
title: zephyr__kernel__mm__demand_paging.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_kernel\_\_mm\_\_demand\_paging.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel/mm.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
#include <stdint.h>
#include <stddef.h>
#include <inttypes.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/syscalls/demand_paging.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_函数（Functions）

<a id="r_ga0b18037209b4d8b5964bd9a1d760f703"></a>

```c
int k_mem_page_out (void *addr, size_t size)
```

相关声明：[k_mem_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga0b18037209b4d8b5964bd9a1d760f703)。

将按页对齐的虚拟内存区域（Page-aligned Virtual Memory Region）换出到后备存储（Backing Store）。

<a id="r_gab36c36a4e230677d2090514f7a34b408"></a>

```c
void k_mem_page_in (void *addr, size_t size)
```

相关声明：[k_mem_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gab36c36a4e230677d2090514f7a34b408)。

将虚拟数据区域（Virtual Data Region）载入内存。

<a id="r_ga5f2d422edde7d366e81a870ce057589f"></a>

```c
void k_mem_pin (void *addr, size_t size)
```

相关声明：[k_mem_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga5f2d422edde7d366e81a870ce057589f)。

固定（Pin）对齐的虚拟数据区域，必要时将其调页载入（Page In）。

<a id="r_ga3278aae5e24733c722b7d83c4b17dab3"></a>

```c
void k_mem_unpin (void *addr, size_t size)
```

相关声明：[k_mem_unpin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga3278aae5e24733c722b7d83c4b17dab3)。

解除对齐虚拟数据区域的固定（Unpin）。

<a id="r_ga52ad88e0c0eed2aa27331bfd4707b7ec"></a>

```c
void k_mem_paging_stats_get (struct k_mem_paging_stats_t *stats)
```

相关声明：[k_mem_paging_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga52ad88e0c0eed2aa27331bfd4707b7ec)、[k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)。

获取系统启动以来的分页统计（Paging Statistics）。

<a id="r_gafad6b39cb2faf3bb416cd4d3faaa8d8c"></a>

```c
void k_mem_paging_thread_stats_get (struct k_thread *thread, struct k_mem_paging_stats_t *stats)
```

相关声明：[k_mem_paging_thread_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gafad6b39cb2faf3bb416cd4d3faaa8d8c)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)。

获取线程自系统启动以来的分页统计（Paging Statistics）。

<a id="r_gaec64d019d819b00c7bc3804aac269199"></a>

```c
void k_mem_paging_histogram_eviction_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_eviction_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gaec64d019d819b00c7bc3804aac269199)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取换出计时直方图（Eviction Timing Histogram）。

<a id="r_ga1da0a643e8f85f98e29288e441a37dfa"></a>

```c
void k_mem_paging_histogram_backing_store_page_in_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_backing_store_page_in_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga1da0a643e8f85f98e29288e441a37dfa)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取后备存储调入计时直方图（Backing Store Page-in Timing Histogram）。

<a id="r_gae4f80d14f88a46ddb9aeb7afba861864"></a>

```c
void k_mem_paging_histogram_backing_store_page_out_get (struct k_mem_paging_histogram_t *hist)
```

相关声明：[k_mem_paging_histogram_backing_store_page_out_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gae4f80d14f88a46ddb9aeb7afba861864)、[k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)。

获取后备存储调出计时直方图（Backing Store Page-out Timing Histogram）。

<a id="r_ga6bb19be3098cc839ae3f6e9528598867"></a>

```c
void k_mem_paging_eviction_add (struct k_mem_page_frame *pf)
```

相关声明：[k_mem_paging_eviction_add](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga6bb19be3098cc839ae3f6e9528598867)。

提交页框（Page Frame），使其被跟踪为换出候选（Eviction Candidate）。

<a id="r_ga16a4df904cc7a9641d06741ed589949d"></a>

```c
void k_mem_paging_eviction_remove (struct k_mem_page_frame *pf)
```

相关声明：[k_mem_paging_eviction_remove](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga16a4df904cc7a9641d06741ed589949d)。

从潜在换出候选（Eviction Candidates）中移除页框（Page Frame）。

<a id="r_ga228747c10bfd8816aec59fddf0e3a224"></a>

```c
void k_mem_paging_eviction_accessed (uintptr_t phys)
```

相关声明：[k_mem_paging_eviction_accessed](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga228747c10bfd8816aec59fddf0e3a224)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

按刚被访问过的页框（Newly Accessed Page Frame）进行处理。

<a id="r_gaadbb4eb56c239f800daf995e6673ae1d"></a>

```c
struct k_mem_page_frame * k_mem_paging_eviction_select (bool *dirty)
```

相关声明：[k_mem_paging_eviction_select](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#gaadbb4eb56c239f800daf995e6673ae1d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

选择要换出的页框（Page Frame for Eviction）。

<a id="r_ga68dcfc0e5374de2c8ad7b9fe4e65c4f4"></a>

```c
void k_mem_paging_eviction_init (void)
```

相关声明：[k_mem_paging_eviction_init](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)。

初始化函数（Initialization Function）。

<a id="r_ga1192487fdc8d63c025de42162fb204cd"></a>

```c
int k_mem_paging_backing_store_location_get (struct k_mem_page_frame *pf, uintptr_t *location, bool page_fault)
```

相关声明：[k_mem_paging_backing_store_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga1192487fdc8d63c025de42162fb204cd)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为已载入页框（Page Frame）的数据页预留或获取存储位置（Storage Location）。

<a id="r_ga6ad421ad5671d9df3d96e03361f672e8"></a>

```c
void k_mem_paging_backing_store_location_free (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_location_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga6ad421ad5671d9df3d96e03361f672e8)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

释放后备存储位置（Backing Store Location）。

<a id="r_ga25debe925b369765ecd5bd7777ce32d0"></a>

```c
int k_mem_paging_backing_store_location_query (void *addr, uintptr_t *location)
```

相关声明：[k_mem_paging_backing_store_location_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga25debe925b369765ecd5bd7777ce32d0)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取按需内容（On-demand Content）的持久位置令牌（Persistent Location Token）。

<a id="r_ga51f663e0a8c31367082e78097359af6d"></a>

```c
void k_mem_paging_backing_store_page_out (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga51f663e0a8c31367082e78097359af6d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将数据页从 `K_MEM_SCRATCH_PAGE` 复制到指定位置（Location）。

<a id="r_ga9becb4908cc7840ece93a2360692962d"></a>

```c
void k_mem_paging_backing_store_page_in (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga9becb4908cc7840ece93a2360692962d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将数据页从给定位置（Location）复制到 `K_MEM_SCRATCH_PAGE`。

<a id="r_ga8d4bd3ea311fd873413d0477e8deb464"></a>

```c
void k_mem_paging_backing_store_page_finalize (struct k_mem_page_frame *pf, uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga8d4bd3ea311fd873413d0477e8deb464)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

调页载入（Page-in）后更新内部记账信息（Internal Accounting）。

<a id="r_ga7ff441f23619b2678bfb72559d5bd592"></a>

```c
void k_mem_paging_backing_store_init (void)
```

相关声明：[k_mem_paging_backing_store_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga7ff441f23619b2678bfb72559d5bd592)。

后备存储初始化函数（Backing Store Initialization Function）。


## 1.3\_原页交叉引用（Cross References）

- [zephyr/kernel/mm.h](../api_source_configuration_reference/P057_mm.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [inttypes.h](../api_source_http_wifi_reference/P005_inttypes.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P006_demand_paging.h_源码浏览.md)
- [k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)
- [k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)
- [k_mem_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga0b18037209b4d8b5964bd9a1d760f703)
- [k_mem_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gab36c36a4e230677d2090514f7a34b408)
- [k_mem_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga5f2d422edde7d366e81a870ce057589f)
- [k_mem_unpin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga3278aae5e24733c722b7d83c4b17dab3)
- [k_mem_paging_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga52ad88e0c0eed2aa27331bfd4707b7ec)
- [k_mem_paging_thread_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gafad6b39cb2faf3bb416cd4d3faaa8d8c)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_mem_paging_histogram_eviction_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gaec64d019d819b00c7bc3804aac269199)
- [k_mem_paging_histogram_backing_store_page_in_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga1da0a643e8f85f98e29288e441a37dfa)
- [k_mem_paging_histogram_backing_store_page_out_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gae4f80d14f88a46ddb9aeb7afba861864)
- [k_mem_paging_eviction_add](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga6bb19be3098cc839ae3f6e9528598867)
- [k_mem_paging_eviction_remove](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga16a4df904cc7a9641d06741ed589949d)
- [k_mem_paging_eviction_accessed](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga228747c10bfd8816aec59fddf0e3a224)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [k_mem_paging_eviction_select](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#gaadbb4eb56c239f800daf995e6673ae1d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_mem_paging_eviction_init](../api_lifecycle_capability_topic_reference/P010_页面淘汰算法 API（Eviction Algorithm APIs）.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)
- [k_mem_paging_backing_store_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga1192487fdc8d63c025de42162fb204cd)
- [k_mem_paging_backing_store_location_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga6ad421ad5671d9df3d96e03361f672e8)
- [k_mem_paging_backing_store_location_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga25debe925b369765ecd5bd7777ce32d0)
- [k_mem_paging_backing_store_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga51f663e0a8c31367082e78097359af6d)
- [k_mem_paging_backing_store_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga9becb4908cc7840ece93a2360692962d)
- [k_mem_paging_backing_store_page_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga8d4bd3ea311fd873413d0477e8deb464)
- [k_mem_paging_backing_store_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga7ff441f23619b2678bfb72559d5bd592)

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__firmware__scmi__protocol.h_文件参考.md)
