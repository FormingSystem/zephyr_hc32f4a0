---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-15
title: 内核内存管理（Kernel Memory Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_内核内存管理（Kernel Memory Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内核内存管理（Kernel Memory Management）

<a id="details"></a>

内核内存管理（Kernel Memory Management）

<a id="header-groups"></a>
<a id="groups"></a>

## 15.1\_主题（Topics）

<a id="r_demand_5Fpaging"></a>

相关声明：[按需分页（Demand Paging）](../api_topic_reference/P029_按需分页（Demand Paging）.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_gabb315b4994193147e9f51b0c3268bfcd"></a>

```c
size_t k_mem_free_get (void)
```

相关声明：[k_mem_free_get](#gabb315b4994193147e9f51b0c3268bfcd)。

返回可用空闲内存量（Free Memory）。

<a id="r_gacf5f9c43ac2c31c376fed4a19f607feb"></a>

```c
static void * k_mem_map (size_t size, uint32_t flags)
```

相关声明：[k_mem_map](#gacf5f9c43ac2c31c376fed4a19f607feb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将匿名内存（Anonymous Memory）映射到 Zephyr 地址空间（Address Space）。

<a id="r_ga1867ea13671daae6a5f38929ea9fd64a"></a>

```c
static void k_mem_unmap (void *addr, size_t size)
```

相关声明：[k_mem_unmap](#ga1867ea13671daae6a5f38929ea9fd64a)。

解除已映射内存的映射（Un-map）。

<a id="r_gaf4740377cd87525fc81fa2ddafef084d"></a>

```c
int k_mem_update_flags (void *addr, size_t size, uint32_t flags)
```

相关声明：[k_mem_update_flags](#gaf4740377cd87525fc81fa2ddafef084d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

修改内存映射属性标志（Memory Mapping Attribute Flags）。

<a id="r_gad9a0110394e8026e27deb15687321ee9"></a>

```c
size_t k_mem_region_align (uintptr_t *aligned_addr, size_t *aligned_size, uintptr_t addr, size_t size, size_t align)
```

相关声明：[k_mem_region_align](#gad9a0110394e8026e27deb15687321ee9)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

对于任意给定区域，提供一个覆盖它的对齐区域（Aligned Region）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 15.3\_缓存模式定义（Caching Mode Definitions）

这些选项互斥（Mutually Exclusive）。

<a id="r_gaae7605452be94d1bd6e0364e9db113c6"></a>

```c
#define K_MEM_CACHE_NONE 2
```

相关声明：[K_MEM_CACHE_NONE](#gaae7605452be94d1bd6e0364e9db113c6)。

不使用缓存（No Caching）。

<a id="r_ga1c8d5fee98c68b08cc6acf781eb35320"></a>

```c
#define K_MEM_CACHE_WT 1
```

相关声明：[K_MEM_CACHE_WT](#ga1c8d5fee98c68b08cc6acf781eb35320)。

直写缓存（Write-through Caching）。

<a id="r_ga802a69d7a53cafcf357861ab50258c99"></a>

```c
#define K_MEM_CACHE_WB 0
```

相关声明：[K_MEM_CACHE_WB](#ga802a69d7a53cafcf357861ab50258c99)。

完整回写缓存（Full Write-back Caching）。

<a id="r_gaae828c97c7bae5d235b863ff3b6b913e"></a>

```c
#define K_MEM_CACHE_MASK (BIT(3) - 1)
```

相关声明：[K_MEM_CACHE_MASK](#gaae828c97c7bae5d235b863ff3b6b913e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`k_map()` 的 `flags` 参数中为缓存模式（Cache Modes）预留的位。

## 15.4\_区域权限属性（Region Permission Attributes）

默认为只读（Read-only），不允许用户模式访问，也不允许执行（No User, No Exec）。

<a id="r_gab9ea94b7155e276f0b653bc1a081866e"></a>

```c
#define K_MEM_PERM_RW BIT(3)
```

相关声明：[K_MEM_PERM_RW](#gab9ea94b7155e276f0b653bc1a081866e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="r_gaf1b0db3c1c5b28b1810f39cdac03f9de"></a>

```c
#define K_MEM_PERM_EXEC BIT(4)
```

相关声明：[K_MEM_PERM_EXEC](#gaf1b0db3c1c5b28b1810f39cdac03f9de)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可执行（Executable）；通常禁止执行。

<a id="r_gaa96222e46728d507ca229796a5724425"></a>

```c
#define K_MEM_PERM_USER BIT(5)
```

相关声明：[K_MEM_PERM_USER](#gaa96222e46728d507ca229796a5724425)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

## 15.5\_区域映射行为属性（Region Mapping Behaviour Attributes）

<a id="r_ga36c4d2ede2f91490bc20ec399df663be"></a>

```c
#define K_MEM_DIRECT_MAP BIT(6)
```

相关声明：[K_MEM_DIRECT_MAP](#ga36c4d2ede2f91490bc20ec399df663be)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域的虚拟地址与物理地址按 1:1 映射（Mapping）。

## 15.6\_k_mem_map() 控制标志（Control Flags）

<a id="r_ga0a3569731c9a9f8e94e913f840b4be61"></a>

```c
#define K_MEM_MAP_UNINIT BIT(16)
```

相关声明：[K_MEM_MAP_UNINIT](#ga0a3569731c9a9f8e94e913f840b4be61)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不保证已映射区域被清零（Zeroed）。

<a id="r_ga7bed120eac76f03a55b1ab8a1f61ce8b"></a>

```c
#define K_MEM_MAP_LOCK BIT(17)
```

相关声明：[K_MEM_MAP_LOCK](#ga7bed120eac76f03a55b1ab8a1f61ce8b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域固定（Pinned）在内存中，永不换页。

<a id="r_ga1275f42967e72f16c58bc3351656bced"></a>

```c
#define K_MEM_MAP_UNPAGED BIT(18)
```

相关声明：[K_MEM_MAP_UNPAGED](#ga1275f42967e72f16c58bc3351656bced)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域采用非分页方式（Unpaged），即：

## 15.7\_详细说明（Detailed Documentation）

<a id="gaae828c97c7bae5d235b863ff3b6b913e"></a>

### `K_MEM_CACHE_MASK`

```c
#define K_MEM_CACHE_MASK (BIT(3) - 1)
```

```c
#include <zephyr/kernel/mm.h>
```

`k_map()` 的 `flags` 参数中为缓存模式（Cache Modes）预留的位。

<a id="gaae7605452be94d1bd6e0364e9db113c6"></a>

### `K_MEM_CACHE_NONE`

```c
#define K_MEM_CACHE_NONE 2
```

```c
#include <zephyr/kernel/mm.h>
```

不使用缓存（No Caching）。

多数驱动需要此项。

<a id="ga802a69d7a53cafcf357861ab50258c99"></a>

### `K_MEM_CACHE_WB`

```c
#define K_MEM_CACHE_WB 0
```

```c
#include <zephyr/kernel/mm.h>
```

完整回写缓存（Full Write-back Caching）。

任何映射的 RAM 都需要此项。

<a id="ga1c8d5fee98c68b08cc6acf781eb35320"></a>

### `K_MEM_CACHE_WT`

```c
#define K_MEM_CACHE_WT 1
```

```c
#include <zephyr/kernel/mm.h>
```

直写缓存（Write-through Caching）。

由某些驱动使用。

<a id="ga36c4d2ede2f91490bc20ec399df663be"></a>

### `K_MEM_DIRECT_MAP`

```c
#define K_MEM_DIRECT_MAP BIT(6)
```

```c
#include <zephyr/kernel/mm.h>
```

区域的虚拟地址与物理地址按 1:1 映射（Mapping）。

<a id="ga7bed120eac76f03a55b1ab8a1f61ce8b"></a>

### `K_MEM_MAP_LOCK`

```c
#define K_MEM_MAP_LOCK BIT(17)
```

```c
#include <zephyr/kernel/mm.h>
```

区域固定（Pinned）在内存中，永不换页。

映射调用返回后，保证此内存不会因页面换出（Page-outs）或写时复制（Copy-on-write）产生缺页（Page Fault）。将按需预取并固定（Pin）物理页框。

<a id="ga0a3569731c9a9f8e94e913f840b4be61"></a>

### `K_MEM_MAP_UNINIT`

```c
#define K_MEM_MAP_UNINIT BIT(16)
```

```c
#include <zephyr/kernel/mm.h>
```

不保证已映射区域被清零（Zeroed）。

这可能改善性能。关联页框可能包含未确定的数据、零，甚至敏感信息。

不得与 K_MEM_PERM_USER 同用，因为不存在安全的使用情形。

<a id="ga1275f42967e72f16c58bc3351656bced"></a>

### `K_MEM_MAP_UNPAGED`

```c
#define K_MEM_MAP_UNPAGED BIT(18)
```

```c
#include <zephyr/kernel/mm.h>
```

区域采用非分页方式（Unpaged），即：

未映射到内存（Not Mapped）。

供内核代码（Kernel Code）使用，不供应用代码使用。

将对应地址范围设置为初始不分配任何实际内存；访问范围内地址时，通过按需分页（Demand Paging）分配。与 K_MEM_MAP_LOCK 不兼容。

指定此标志时，arch_mem_map() 的 phys 参数解释为后备存储位置值（Backing Store Location），而非物理地址，与 arch_mem_page_out() 很相似。定义了两个特殊位置值 ARCH_UNPAGED_ANON_ZERO 和 ARCH_UNPAGED_ANON_UNINIT，分别用于匿名内存映射（Anonymous Memory Mappings）的清零页面和未初始化页面。

<a id="gaf1b0db3c1c5b28b1810f39cdac03f9de"></a>

### `K_MEM_PERM_EXEC`

```c
#define K_MEM_PERM_EXEC BIT(4)
```

```c
#include <zephyr/kernel/mm.h>
```

区域可执行（Executable）；通常禁止执行。

<a id="gab9ea94b7155e276f0b653bc1a081866e"></a>

### `K_MEM_PERM_RW`

```c
#define K_MEM_PERM_RW BIT(3)
```

```c
#include <zephyr/kernel/mm.h>
```

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="gaa96222e46728d507ca229796a5724425"></a>

### `K_MEM_PERM_USER`

```c
#define K_MEM_PERM_USER BIT(5)
```

```c
#include <zephyr/kernel/mm.h>
```

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

<a id="gabb315b4994193147e9f51b0c3268bfcd"></a>

### `k_mem_free_get()`

```c
size_t k_mem_free_get ( void )
```

```c
#include <zephyr/kernel/mm.h>
```

返回可用空闲内存量（Free Memory）。

返回值反映当前空闲 RAM 页框（Page Frames）的数量。启用按需分页（Demand Paging）后，仍可能分配更多内存。

若并发发生内存映射或页面换入，此函数报告的信息可能立即过期。

**返回（Returns）**：返回值（Returns）：空闲物理 RAM，单位为字节。

<a id="gacf5f9c43ac2c31c376fed4a19f607feb"></a>

### `k_mem_map()`

```c
void * k_mem_map ( size_t size, uint32_t flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel/mm.h>
```

将匿名内存（Anonymous Memory）映射到 Zephyr 地址空间（Address Space）。

此函数实际扩大 Zephyr 可用的数据空间。内核选择并返回一个基虚拟地址（Base Virtual Address），按 flags 参数为所有上下文设置此内存的访问权限。

若需要以任何方式管理用户线程访问控制，请勿在此启用 K_MEM_PERM_USER；应在映射建立后通过内存域 API（Memory Domain APIs）管理区域权限。此处设置 K_MEM_PERM_USER 将允许所有用户线程访问，通常不符合需求。

除非使用 K_MEM_MAP_UNINIT，否则返回的内存会被清零。

不保证映射区域在物理内存中连续。物理连续缓冲区（Physically Contiguous Buffers）应静态分配，并在构建时固定（Pinned）。

这样映射的页面采用回写缓存（Write-back Cache）设置。

返回的虚拟内存指针按页对齐（Page-aligned）。size 参数以及用于重新映射的任何基地址也必须按页对齐。

分配包含紧邻所请求区域前后的两个保护页（Guard Pages）。总分配大小为请求大小加上这两个保护页的大小。

多个 K_MEM_MAP_* 标志可改变此函数行为，详情见各标志的文档。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `size` | 内存映射大小（Memory Mapping Size），必须按页对齐。 |
| `flags` | K_MEM_PERM_*、K_MEM_MAP_* 控制标志（Control Flags）。 |

**返回（Returns）**：返回值（Returns）：映射的内存位置；虚拟地址空间不足、用于建立映射的物理内存不足，或分页结构所需内存不足时返回 NULL。

<a id="gad9a0110394e8026e27deb15687321ee9"></a>

### `k_mem_region_align()`

```c
size_t k_mem_region_align ( uintptr_t * aligned_addr, size_t * aligned_size, uintptr_t addr, size_t size, size_t align )
```

```c
#include <zephyr/kernel/mm.h>
```

对于任意给定区域，提供一个覆盖它的对齐区域（Aligned Region）。

返回区域的基地址和大小都按给定对齐值（Alignment Value）对齐。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] aligned_addr` | 对齐后的地址（Aligned Address） |
| `[out] aligned_size` | 对齐后的区域大小（Aligned Region Size） |
| `[in] addr` | 区域基地址（Region Base Address） |
| `[in] size` | 区域大小。 |
| `[in] align` | 地址与大小所使用的对齐值（Alignment） |

**返回（Returns）**：返回值（Returns）：aligned_addr 与 addr 之间的偏移量。

<a id="ga1867ea13671daae6a5f38929ea9fd64a"></a>

### `k_mem_unmap()`

```c
void k_mem_unmap ( void * addr, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel/mm.h>
```

解除已映射内存的映射（Un-map）。

移除给定页对齐区域的内存映射。关联页框释放，内核可复用关联虚拟地址区域；已换出的数据页可以丢弃。

对原本未映射的区域调用此函数属于未定义行为（Undefined Behavior）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的内存区域基虚拟地址（Base Virtual Address） |
| `size` | 按页对齐的内存区域大小（Region Size） |

<a id="gaf4740377cd87525fc81fa2ddafef084d"></a>

### `k_mem_update_flags()`

```c
int k_mem_update_flags ( void * addr, size_t size, uint32_t flags )
```

```c
#include <zephyr/kernel/mm.h>
```

修改内存映射属性标志（Memory Mapping Attribute Flags）。

更新给定页对齐内存区域的缓存、访问和控制标志（Caching, Access and Control Flags）。

对原本未映射的区域调用此函数属于未定义行为（Undefined Behavior）；但支持启动时隐式映射的系统内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的内存区域基虚拟地址（Base Virtual Address） |
| `size` | 按页对齐的内存区域大小（Region Size） |
| `flags` | K_MEM_PERM_*、K_MEM_MAP_* 控制标志（Control Flags）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回负错误码。


## 15.8\_原页交叉引用（Cross References）

- [按需分页（Demand Paging）](../api_topic_reference/P029_按需分页（Demand Paging）.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/kernel/mm.h](../api_file_mesh_interrupt_reference/P016_zephyr__kernel__mm.h_文件参考.md)
- [arch_mem_map()](../arch_core_reference/P003_架构内存映射接口.md#gab716b971ebbc382e397b6a464d534e69)
- [arch_mem_page_out()](../arch_core_reference/P003_架构内存映射接口.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_INA237 API主题.md) · [返回大纲](大纲.md) · [下一章](P016_内核内存管理内部 API.md)
