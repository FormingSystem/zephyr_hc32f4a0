---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-11
title: 后备存储 API（Backing Store APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_后备存储 API（Backing Store APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

后备存储 API（Backing store APIs）

<a id="details"></a>

后备存储 API（Backing store APIs）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_ga1192487fdc8d63c025de42162fb204cd"></a>

```c
int k_mem_paging_backing_store_location_get (struct k_mem_page_frame *pf, uintptr_t *location, bool page_fault)
```

相关声明：[k_mem_paging_backing_store_location_get](#ga1192487fdc8d63c025de42162fb204cd)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为已载入页框（Page Frame）的数据页预留或获取存储位置（Storage Location）。

<a id="r_ga6ad421ad5671d9df3d96e03361f672e8"></a>

```c
void k_mem_paging_backing_store_location_free (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_location_free](#ga6ad421ad5671d9df3d96e03361f672e8)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

释放后备存储位置（Backing Store Location）。

<a id="r_ga25debe925b369765ecd5bd7777ce32d0"></a>

```c
int k_mem_paging_backing_store_location_query (void *addr, uintptr_t *location)
```

相关声明：[k_mem_paging_backing_store_location_query](#ga25debe925b369765ecd5bd7777ce32d0)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取按需内容（On-demand Content）的持久位置令牌（Persistent Location Token）。

<a id="r_ga51f663e0a8c31367082e78097359af6d"></a>

```c
void k_mem_paging_backing_store_page_out (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_out](#ga51f663e0a8c31367082e78097359af6d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将数据页从 `K_MEM_SCRATCH_PAGE` 复制到指定位置（Location）。

<a id="r_ga9becb4908cc7840ece93a2360692962d"></a>

```c
void k_mem_paging_backing_store_page_in (uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_in](#ga9becb4908cc7840ece93a2360692962d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将数据页从给定位置（Location）复制到 `K_MEM_SCRATCH_PAGE`。

<a id="r_ga8d4bd3ea311fd873413d0477e8deb464"></a>

```c
void k_mem_paging_backing_store_page_finalize (struct k_mem_page_frame *pf, uintptr_t location)
```

相关声明：[k_mem_paging_backing_store_page_finalize](#ga8d4bd3ea311fd873413d0477e8deb464)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

调页载入（Page-in）后更新内部记账信息（Internal Accounting）。

<a id="r_ga7ff441f23619b2678bfb72559d5bd592"></a>

```c
void k_mem_paging_backing_store_init (void)
```

相关声明：[k_mem_paging_backing_store_init](#ga7ff441f23619b2678bfb72559d5bd592)。

后备存储初始化函数（Backing Store Initialization Function）。

## 11.2\_详细说明（Detailed Documentation）

<a id="ga7ff441f23619b2678bfb72559d5bd592"></a>

### `k_mem_paging_backing_store_init()`

```c
void k_mem_paging_backing_store_init ( void )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

后备存储初始化函数（Backing Store Initialization Function）。

此函数返回后，实现可立即收到页面换入／换出（Page In/Out）调用，但在返回之前不会收到。此函数在 POST_KERNEL 阶段调用。

此函数应完成以下两件事：

- 初始化后备存储（Backing Store）所需的所有内部数据结构和管理记录。
- 若后备存储在启动时已包含全部或部分已加载的内核数据页，应为其关联页框适当设置 K_MEM_PAGE_FRAME_BACKED，并相应设置所有内部管理记录。

<a id="ga6ad421ad5671d9df3d96e03361f672e8"></a>

### `k_mem_paging_backing_store_location_free()`

```c
void k_mem_paging_backing_store_location_free ( uintptr_t location)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

释放后备存储位置（Backing Store Location）。

可以丢弃任何已存储数据，且与此地址关联的位置令牌（Location Token）可以重新用于其他数据页。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `location` | 待释放的位置令牌（Location Token） |

<a id="ga1192487fdc8d63c025de42162fb204cd"></a>

### `k_mem_paging_backing_store_location_get()`

```c
int k_mem_paging_backing_store_location_get ( struct k_mem_page_frame * pf, uintptr_t * location, bool page_fault )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

为已载入页框（Page Frame）的数据页预留或获取存储位置（Storage Location）。

返回的位置令牌（Location Token）必须唯一对应所映射的虚拟地址。此位置用于在后备存储（Backing Store）中保存换出的数据页内容，以便稍后取回。位置值必须按页对齐。

可能针对同一数据页多次调用此函数。如果其页框（Page Frame）已设置 K_MEM_PAGE_FRAME_BACKED 位，应返回该数据页先前的后备存储位置，其中缓存了干净副本（Clean Copy）。该副本可在换出时更新，也可用于直接丢弃干净页而无需写出其内容。

后备存储（Backing Store）已满时，可选择缓存某个已加载数据页的其他后备存储位置；此时须清除其关联页框中的 K_MEM_PAGE_FRAME_BACKED 位，因为该数据页已不再被缓存。

k_mem_page_frame_to_virt(pf) 表示该页当前映射到的虚拟地址。可容纳整个地址空间的大型稀疏后备存储（Sparse Backing Store）可以仅根据虚拟地址生成位置令牌，无需其他管理。

此函数区分调用是否由缺页（Page Fault）引起。必须始终预留一个空闲后备存储位置，确保缺页处理成功。如果未设置 page_fault 参数，即使仍有一个可用位置，此函数也应返回 -ENOMEM。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pf` | 要为其获取存储位置的虚拟地址（Virtual Address） |
| `[out] location` | 存储位置令牌（Storage Location Token） |
| ` page_fault` | 此次请求是否由缺页（Page Fault）引起 |

**返回（Returns）**：返回值（Returns）：0 表示成功；-ENOMEM 表示后备存储（Backing Store）已满。

<a id="ga25debe925b369765ecd5bd7777ce32d0"></a>

### `k_mem_paging_backing_store_location_query()`

```c
int k_mem_paging_backing_store_location_query ( void * addr, uintptr_t * location )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

获取按需内容（On-demand Content）的持久位置令牌（Persistent Location Token）。

与 k_mem_paging_backing_store_location_get() 不同，此函数不分配后备存储空间，而是返回对应某段固定存储内容的位置令牌（Location Token），供按需换入。预期与 CONFIG_LINKER_USE_ONDEMAND_SECTION 和 K_MEM_MAP_UNPAGED 标志配合，在启动时创建按需映射（Demand Mappings）；也可用于实现基于文件的 mmap() 等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` addr` | 要为其获取位置令牌（Location Token）的虚拟地址 |
| `[out] location` | 存储位置令牌（Storage Location Token） |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回负错误码。

<a id="ga8d4bd3ea311fd873413d0477e8deb464"></a>

### `k_mem_paging_backing_store_page_finalize()`

```c
void k_mem_paging_backing_store_page_finalize ( struct k_mem_page_frame * pf, uintptr_t location )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

调页载入（Page-in）后更新内部记账信息（Internal Accounting）。

在 k_mem_paging_backing_store_page_in() 之后且重新锁定中断后调用，因此可安全访问 k_mem_page_frame 数据。location 值与传给 k_mem_paging_backing_store_page_in() 的值相同。

主要用途是更新页框（Page Frame）中供后备存储使用的自定义字段，反映该页再次换出时应将数据逐出到何处。在某些实现中，此操作可以为空操作（No-op）。

若后备存储缓存已换入的数据页，此时适合设置 K_MEM_PAGE_FRAME_BACKED 位。内核仅在页表将数据页标为干净，且关联页框已设置 K_MEM_PAGE_FRAME_BACKED 位时，才跳过干净数据页的换出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pf` | 已加载数据的页框（Page Frame） |
| `location` | 已加载数据页的原始获取位置 |

<a id="ga9becb4908cc7840ece93a2360692962d"></a>

### `k_mem_paging_backing_store_page_in()`

```c
void k_mem_paging_backing_store_page_in ( uintptr_t location)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

将数据页从给定位置（Location）复制到 `K_MEM_SCRATCH_PAGE`。

紧接此调用之前，会将 K_MEM_SCRATCH_PAGE 以可读写方式映射到调用上下文的目标页框（Destination Page Frame）。

此函数与 k_mem_paging_backing_store_page_out() 的调用始终串行化（Serialized），但可能启用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `location` | 数据页的位置令牌（Location Token） |

<a id="ga51f663e0a8c31367082e78097359af6d"></a>

### `k_mem_paging_backing_store_page_out()`

```c
void k_mem_paging_backing_store_page_out ( uintptr_t location)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

将数据页从 `K_MEM_SCRATCH_PAGE` 复制到指定位置（Location）。

紧接此调用之前，会将 K_MEM_SCRATCH_PAGE 以可读写方式映射到调用上下文的源页框（Source Page Frame）。

此函数与 k_mem_paging_backing_store_page_in() 的调用始终串行化（Serialized），但可能启用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `location` | 数据页的位置令牌（Location Token），用于后续取回 |


## 11.3\_原页交叉引用（Cross References）

- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/kernel/mm/demand_paging.h](../api_file_paging_wakeup_reference/P001_zephyr__kernel__mm__demand_paging.h_文件参考.md)
- [mmap()](../api_file_reference/P227_zephyr__posix__sys__mman.h_文件参考.md#ac2e7d057b16f0c959ffb39d8719eb1ed)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_IPv6 套接字选项（Socket options）.md) · [返回大纲](大纲.md) · [下一章](P012_MFD ADP5360 接口.md)
