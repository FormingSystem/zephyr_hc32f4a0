---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-10
title: 页面淘汰算法 API（Eviction Algorithm APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_页面淘汰算法 API（Eviction Algorithm APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

页面淘汰算法 API（Eviction algorithm APIs）

<a id="details"></a>

页面淘汰算法 API（Eviction algorithm APIs）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.1\_函数（Functions）

<a id="r_ga6bb19be3098cc839ae3f6e9528598867"></a>

```c
void k_mem_paging_eviction_add (struct k_mem_page_frame *pf)
```

相关声明：[k_mem_paging_eviction_add](#ga6bb19be3098cc839ae3f6e9528598867)。

提交页框（Page Frame），使其被跟踪为换出候选（Eviction Candidate）。

<a id="r_ga16a4df904cc7a9641d06741ed589949d"></a>

```c
void k_mem_paging_eviction_remove (struct k_mem_page_frame *pf)
```

相关声明：[k_mem_paging_eviction_remove](#ga16a4df904cc7a9641d06741ed589949d)。

从潜在换出候选（Eviction Candidates）中移除页框（Page Frame）。

<a id="r_ga228747c10bfd8816aec59fddf0e3a224"></a>

```c
void k_mem_paging_eviction_accessed (uintptr_t phys)
```

相关声明：[k_mem_paging_eviction_accessed](#ga228747c10bfd8816aec59fddf0e3a224)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

按刚被访问过的页框（Newly Accessed Page Frame）进行处理。

<a id="r_gaadbb4eb56c239f800daf995e6673ae1d"></a>

```c
struct k_mem_page_frame * k_mem_paging_eviction_select (bool *dirty)
```

相关声明：[k_mem_paging_eviction_select](#gaadbb4eb56c239f800daf995e6673ae1d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

选择要换出的页框（Page Frame for Eviction）。

<a id="r_ga68dcfc0e5374de2c8ad7b9fe4e65c4f4"></a>

```c
void k_mem_paging_eviction_init (void)
```

相关声明：[k_mem_paging_eviction_init](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)。

初始化函数（Initialization Function）。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga228747c10bfd8816aec59fddf0e3a224"></a>

### `k_mem_paging_eviction_accessed()`

```c
void k_mem_paging_eviction_accessed ( uintptr_t phys)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

按刚被访问过的页框（Newly Accessed Page Frame）进行处理。

架构专用内存故障处理程序（Architecture-specific Memory Fault Handler）调用此接口，通知换出算法（Eviction Algorithm）：给定物理地址属于正在访问的页框，因此该页框应降低成为下一换出候选的可能性。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] phys` | 正在访问的物理地址（Physical Address）。 |

<a id="ga6bb19be3098cc839ae3f6e9528598867"></a>

### `k_mem_paging_eviction_add()`

```c
void k_mem_paging_eviction_add ( struct k_mem_page_frame * pf)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

提交页框（Page Frame），使其被跟踪为换出候选（Eviction Candidate）。

内核调用此接口，通知换出算法（Eviction Algorithm）：可以将给定页框（Page Frame）列为潜在换出候选。

首次调用 `k_mem_paging_eviction_init()` 之前，绝不会调用本函数。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pf` | 要添加的页框（Page Frame）。 |

<a id="ga68dcfc0e5374de2c8ad7b9fe4e65c4f4"></a>

### `k_mem_paging_eviction_init()`

```c
void k_mem_paging_eviction_init ( void )
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

初始化函数（Initialization Function）。

在 `POST_KERNEL` 阶段调用，执行换出算法（Eviction Algorithm）所需的初始化任务。保证在本函数返回之前不会调用 `k_mem_paging_eviction_select()`，且本函数仅调用一次。

<a id="ga16a4df904cc7a9641d06741ed589949d"></a>

### `k_mem_paging_eviction_remove()`

```c
void k_mem_paging_eviction_remove ( struct k_mem_page_frame * pf)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

从潜在换出候选（Eviction Candidates）中移除页框（Page Frame）。

内核调用此接口，通知换出算法（Eviction Algorithm）：不应再将给定页框（Page Frame）列为潜在换出候选。

传入本函数的页框（Page Frames）必须已通过 `k_mem_paging_eviction_add()` 提交过。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pf` | 要移除的页框（Page Frame）。 |

<a id="gaadbb4eb56c239f800daf995e6673ae1d"></a>

### `k_mem_paging_eviction_select()`

```c
struct k_mem_page_frame * k_mem_paging_eviction_select ( bool * dirty)
```

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

选择要换出的页框（Page Frame for Eviction）。

没有空闲页框时，内核调用此接口选择要换出的页框（Page Frame to Evict）。不保证返回的页框一定被换出；如果实际换出，内核会以该页框调用 `k_mem_paging_eviction_remove()`。

首次调用 `k_mem_paging_eviction_init()` 之前，绝不会调用本函数。

本函数在中断已锁定（Interrupts Locked）的情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] dirty` | 要换出的页是否为脏页（Dirty）。 |

**返回（Returns）**：**返回值（Returns）：**要换出的页框（Page Frame）。


## 10.3\_原页交叉引用（Cross References）

- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/kernel/mm/demand_paging.h](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_虚拟传输（Dummy transport）.md) · [返回大纲](大纲.md) · [下一章](P011_蜂窝调制解调器驱动定义宏（Driver definition macros）.md)
