---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-16
title: 内核内存管理内部 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_内核内存管理内部 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="r_gae9f618604758a034b52509c0377d1bdb"></a>

```c
#define K_MEM_VIRT_OFFSET
```

相关声明：[K_MEM_VIRT_OFFSET](#gae9f618604758a034b52509c0377d1bdb)。

从物理地址到永久虚拟映射（permanent virtual mapping）的地址偏移量。

<a id="r_gaeda081ed25c90237b2ca88bc5ae0f254"></a>

```c
#define IS_SRAM_ADDRESS_LOWER(ADDR)
```

相关声明：[IS_SRAM_ADDRESS_LOWER](#gaeda081ed25c90237b2ca88bc5ae0f254)。

<a id="r_ga38152dff07d0cc76efc4b9eed96e8037"></a>

```c
#define IS_SRAM_ADDRESS_UPPER(ADDR)
```

相关声明：[IS_SRAM_ADDRESS_UPPER](#ga38152dff07d0cc76efc4b9eed96e8037)。

<a id="r_gae0d6fc45cca5dc25d77294b4efb14c80"></a>

```c
#define IS_SRAM_ADDRESS(ADDR)
```

相关声明：[IS_SRAM_ADDRESS](#gae0d6fc45cca5dc25d77294b4efb14c80)。

<a id="r_ga49b13f5f43530952220fb223c3d56d3c"></a>

```c
#define K_MEM_PHYS_ADDR(virt)
```

相关声明：[K_MEM_PHYS_ADDR](#ga49b13f5f43530952220fb223c3d56d3c)。

根据虚拟地址获取物理地址。

<a id="r_ga850451db4842595d8d96e85a087e8964"></a>

```c
#define K_MEM_VIRT_ADDR(phys)
```

相关声明：[K_MEM_VIRT_ADDR](#ga850451db4842595d8d96e85a087e8964)。

根据物理地址获取虚拟地址。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_gadc2d4d6258059524eaba2ff139c2f9ff"></a>

```c
static uintptr_t k_mem_phys_addr (void *virt)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[k_mem_phys_addr](#gadc2d4d6258059524eaba2ff139c2f9ff)。

根据虚拟地址获取物理地址。

<a id="r_gaed8dccb2a3c15daff9d2e5b4d49f782a"></a>

```c
static void * k_mem_virt_addr (uintptr_t phys)
```

相关声明：[k_mem_virt_addr](#gaed8dccb2a3c15daff9d2e5b4d49f782a)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据物理地址获取虚拟地址。

<a id="r_gaa2c52222198f4c7362c183e1397a4e5c"></a>

```c
void k_mem_map_phys_bare (uint8_t **virt_ptr, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[k_mem_map_phys_bare](#gaa2c52222198f4c7362c183e1397a4e5c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将物理内存区域映射到内核虚拟地址空间（virtual address space）。

<a id="r_gae713c4eb253302d06f758f87503cf5dd"></a>

```c
void k_mem_unmap_phys_bare (uint8_t *virt, size_t size)
```

相关声明：[k_mem_unmap_phys_bare](#gae713c4eb253302d06f758f87503cf5dd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从内核虚拟地址空间解除虚拟内存区域的映射。

<a id="r_ga2aeab99cba24ac3fd9479dbd421f6c5c"></a>

```c
void * k_mem_map_phys_guard (uintptr_t phys, size_t size, uint32_t flags, bool is_anon)
```

相关声明：[k_mem_map_phys_guard](#ga2aeab99cba24ac3fd9479dbd421f6c5c)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将内存映射到虚拟地址空间，并设置保护页（guard pages）。

<a id="r_gaca476fbacb86815edd4898b13ecf5120"></a>

```c
void k_mem_unmap_phys_guard (void *addr, size_t size, bool is_anon)
```

相关声明：[k_mem_unmap_phys_guard](#gaca476fbacb86815edd4898b13ecf5120)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

解除通过 `k_mem_map_phys_guard()` 建立的内存映射。

## 16.3\_详细说明（Detailed Documentation）

<a id="gae0d6fc45cca5dc25d77294b4efb14c80"></a>

### `IS_SRAM_ADDRESS`

```c
#define IS_SRAM_ADDRESS ( ADDR)
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
(IS_SRAM_ADDRESS_LOWER(ADDR) &&  \
 IS_SRAM_ADDRESS_UPPER(ADDR))
```

<a id="gaeda081ed25c90237b2ca88bc5ae0f254"></a>

### `IS_SRAM_ADDRESS_LOWER`

```c
#define IS_SRAM_ADDRESS_LOWER ( ADDR)
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
true
```

<a id="ga38152dff07d0cc76efc4b9eed96e8037"></a>

### `IS_SRAM_ADDRESS_UPPER`

```c
#define IS_SRAM_ADDRESS_UPPER ( ADDR)
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
false
```

<a id="ga49b13f5f43530952220fb223c3d56d3c"></a>

### `K_MEM_PHYS_ADDR`

```c
#define K_MEM_PHYS_ADDR ( virt)
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
((virt) - K_MEM_VIRT_OFFSET)
```

根据虚拟地址获取物理地址。

仅适用于内核的永久 RAM 映射（Permanent Mapping of RAM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 虚拟地址（Virtual Address） |

**返回（Returns）**：返回值（Returns）：物理地址（Physical Address）。

<a id="ga850451db4842595d8d96e85a087e8964"></a>

### `K_MEM_VIRT_ADDR`

```c
#define K_MEM_VIRT_ADDR ( phys)
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
((phys) + K_MEM_VIRT_OFFSET)
```

根据物理地址获取虚拟地址。

仅适用于内核的永久 RAM 映射（Permanent Mapping of RAM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phys` | 物理地址（Physical Address） |

**返回（Returns）**：返回值（Returns）：虚拟地址（Virtual Address）。

<a id="gae9f618604758a034b52509c0377d1bdb"></a>

### `K_MEM_VIRT_OFFSET`

```c
#define K_MEM_VIRT_OFFSET
```

```c
#include <zephyr/kernel/internal/mm.h>
```

展开值（Value）：

```c
((CONFIG_KERNEL_VM_BASE + CONFIG_KERNEL_VM_OFFSET) - \
(DT_CHOSEN_SRAM_ADDR + CONFIG_SRAM_OFFSET))
```

从物理地址到永久虚拟映射（permanent virtual mapping）的地址偏移量。

对于内核永久 RAM 映射中的虚拟地址，减去此偏移量（Offset）即可得到物理地址。

原始示例（Example）：

```c
virt_addr = phys_addr + K_MEM_VIRT_OFFSET
```

仅适用于区间 [CONFIG_KERNEL_VM_BASE, CONFIG_KERNEL_VM_BASE + DT_CHOSEN_SRAM_ADDR) 内的虚拟地址。

这些宏供汇编、链接器代码及静态初始化器（Static Initializers）使用，须谨慎。

启用按需分页（Demand Paging）时，仅适用于在启动时固定到其虚拟映射的页框（Pinned Page Frames）。

待办（TODO）：可能需要移至架构 API（Arch API），或定义额外约束。

<a id="gaa2c52222198f4c7362c183e1397a4e5c"></a>

### `k_mem_map_phys_bare()`

```c
void k_mem_map_phys_bare ( uint8_t ** virt_ptr, uintptr_t phys, size_t size, uint32_t flags )
```

```c
#include <zephyr/kernel/internal/mm.h>
```

将物理内存区域映射到内核虚拟地址空间（virtual address space）。

将内存映射 I/O 区域（Memory-mapped I/O Regions）映射到虚拟地址空间。给定物理地址与大小，返回线性地址（Linear Address），表示该物理区域在 Zephyr 内核虚拟地址空间中的映射基址。

通过此函数映射的内存，必须使用 k_mem_unmap_phys_bare() 解除映射。

修改为内核预留区域中的活动页表（Active Page Tables），由函数选择并返回虚拟地址。

可移植代码（Portable Code）绝不能假定 phys_addr 与 linear_addr 相等。

缓存与访问属性（Caching and Access Properties）由 flags 参数控制，其中未使用位保留供未来扩展。必须选择缓存模式。默认区域只读，禁止用户访问与代码执行；通过向 flags 传入 K_MEM_CACHE_* 和 K_MEM_PERM_* 宏改变策略。

映射所需虚拟地址空间不足时，触发内核致命故障（Kernel Panic）。

仅启用 CONFIG_MMU 时提供此 API。

强烈不建议用此函数映射系统 RAM 页框，可能与匿名内存映射（Anonymous Memory Mappings）及按需分页（Demand Paging）冲突并产生未定义行为。除非完全了解影响，否则不要用于 RAM。需要一块内存时，使用 k_mem_map()；需要物理连续缓冲区时，静态声明并在构建时固定（Pin），系统启动时会完成映射。

此 API 属于仍在开发中的基础设施，可能发生变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] virt_ptr` | 输出虚拟地址的存储位置 |
| `[in] phys` | 内存区域的物理基地址（Physical Address Base） |
| `[in] size` | 内存区域（Memory Region）的大小。 |
| `[in] flags` | 缓存模式及访问标志（Caching Mode and Access Flags），参见 K_MAP_* 宏。 |

<a id="ga2aeab99cba24ac3fd9479dbd421f6c5c"></a>

### `k_mem_map_phys_guard()`

```c
void * k_mem_map_phys_guard ( uintptr_t phys, size_t size, uint32_t flags, bool is_anon )
```

```c
#include <zephyr/kernel/internal/mm.h>
```

将内存映射到虚拟地址空间，并设置保护页（guard pages）。

将内存映射到虚拟地址空间，并在前后各设置一个保护页（Guard Page）。通过此函数映射的内存必须用 k_mem_unmap_phys_guard() 解除映射。

将连续物理内存区域映射到内核虚拟地址空间，并在前后各设置一个保护页（Guard Page）。给定物理地址与大小，返回线性地址（Linear Address），表示该物理区域在 Zephyr 内核虚拟地址空间中的映射基址。

修改为内核预留区域中的活动页表（Active Page Tables），由函数选择并返回虚拟地址。

若需要以任何方式管理用户线程访问控制，请勿在此启用 K_MEM_PERM_USER；应在映射建立后通过内存域 API（Memory Domain APIs）管理区域权限。此处设置 K_MEM_PERM_USER 将允许所有用户线程访问，通常不符合需求。

除非使用 K_MEM_MAP_UNINIT，否则返回的内存会被清零。

返回的虚拟内存指针按页对齐（Page-aligned）。size 参数以及用于重新映射的任何基地址也必须按页对齐。

分配包含紧邻所请求区域前后的两个保护页（Guard Pages）。总分配大小为请求大小加上这两个保护页的大小。

多个 K_MEM_MAP_* 标志可改变此函数行为，详情见各标志的文档。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phys` | 未请求匿名内存（Anonymous Memory）时，内存区域的物理基地址，必须按页对齐。 |
| `size` | 内存映射大小（Memory Mapping Size），必须按页对齐。 |
| `flags` | K_MEM_PERM_*、K_MEM_MAP_* 控制标志（Control Flags）。 |
| `is_anon` | 请求匿名内存映射（Anonymous Memory Mapping）时为 True。 |

**参阅（See Also）**：若经由 k_mem_map() 调用，另请参阅该函数以获取更多信息。

**返回（Returns）**：返回值（Returns）：映射的内存位置；虚拟地址空间不足、用于建立映射的物理内存不足，或分页结构所需内存不足时返回 NULL。

<a id="gadc2d4d6258059524eaba2ff139c2f9ff"></a>

### `k_mem_phys_addr()`

```c
uintptr_t k_mem_phys_addr ( void * virt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel/internal/mm.h>
```

根据虚拟地址获取物理地址。

仅适用于内核的永久 RAM 映射（Permanent Mapping of RAM）。

与 K_MEM_PHYS_ADDR() 相同，但带有类型安全（Type Safety）与断言（Assertions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 虚拟地址（Virtual Address） |

**返回（Returns）**：返回值（Returns）：物理地址（Physical Address）。

<a id="gae713c4eb253302d06f758f87503cf5dd"></a>

### `k_mem_unmap_phys_bare()`

```c
void k_mem_unmap_phys_bare ( uint8_t * virt, size_t size )
```

```c
#include <zephyr/kernel/internal/mm.h>
```

从内核虚拟地址空间解除虚拟内存区域的映射。

供需要建立临时内存映射（Temporary Memory Mappings）的驱动和早期启动例程使用，使这些映射在不再需要时可被丢弃。

修改为内核预留区域中的活动页表（Active Page Tables）。

将输入参数对齐到页边界，因此可以使用 k_mem_map_phys_bare() 返回的虚拟地址。

仅启用 CONFIG_MMU 时提供此 API。

强烈不建议用此函数解除内存映射，可能与匿名内存映射（Anonymous Memory Mappings）及按需分页（Demand Paging）冲突并产生未定义行为。除非完全了解影响，否则不要使用。

此 API 属于仍在开发中的基础设施，可能发生变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 待解除映射的虚拟地址区域起始地址。 |
| `size` | 虚拟地址区域大小（Virtual Address Region Size） |

<a id="gaca476fbacb86815edd4898b13ecf5120"></a>

### `k_mem_unmap_phys_guard()`

```c
void k_mem_unmap_phys_guard ( void * addr, size_t size, bool is_anon )
```

```c
#include <zephyr/kernel/internal/mm.h>
```

解除通过 `k_mem_map_phys_guard()` 建立的内存映射。

移除给定页对齐区域及其前后两个保护页（Guard Pages）的内存映射。

修改为内核预留区域中的活动页表（Active Page Tables）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 按页对齐的内存区域基虚拟地址（Base Virtual Address） |
| `size` | 按页对齐的内存区域大小（Region Size） |
| `is_anon` | 映射内存来自匿名内存（Anonymous Memory）时为 True。 |

**参阅（See Also）**：若经由 k_mem_unmap() 调用，另请参阅该函数以获取更多信息。

**说明（Note）**：注意（Note）：对最初并非由 k_mem_map_phys_guard() 映射的区域调用此函数，属于未定义行为（Undefined Behavior）。

<a id="gaed8dccb2a3c15daff9d2e5b4d49f782a"></a>

### `k_mem_virt_addr()`

```c
void * k_mem_virt_addr ( uintptr_t phys)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel/internal/mm.h>
```

根据物理地址获取虚拟地址。

仅适用于内核的永久 RAM 映射（Permanent Mapping of RAM）。

与 K_MEM_VIRT_ADDR() 相同，但带有类型安全（Type Safety）与断言（Assertions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phys` | 物理地址（Physical Address） |

**返回（Returns）**：返回值（Returns）：虚拟地址（Virtual Address）。


## 16.4\_原页交叉引用（Cross References）

- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/kernel/internal/mm.h](../api_file_system_device_reference/P020_zephyr__kernel__internal__mm.h_文件参考.md)
- [DT_CHOSEN_SRAM_ADDR](../dt_overview_reference/P005_选定SRAM区域宏.md#gad2693f2710d28709b0f129d5b791a29e)
- [k_mem_map()](P015_内核内存管理（Kernel Memory Management）.md#gacf5f9c43ac2c31c376fed4a19f607feb)
- [k_mem_unmap()](P015_内核内存管理（Kernel Memory Management）.md#ga1867ea13671daae6a5f38929ea9fd64a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__kernel__mm__internal__apis_html_gaeda081ed25c90237b2ca88bc5ae0f254"></a>
<a id="agroup__kernel__mm__internal__apis_html_gae9f618604758a034b52509c0377d1bdb"></a>
<a id="agroup__devicetree-chosen-sram_html_gad2693f2710d28709b0f129d5b791a29e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_内核内存管理（Kernel Memory Management）.md) · [返回大纲](大纲.md) · [下一章](P017_MAX30210 API主题.md)
