---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-6
title: 内存管理（Memory Management）的驱动API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_内存管理（Memory Management）的驱动API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存管理（Memory Management）的驱动API。

<a id="details"></a>

内存管理驱动 API（Memory Management Driver APIs）。包含系统级内存管理驱动（System-wide Memory Management Driver）的 API。系统中仅允许存在一个实例。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_sys_5Fmm_5Fdrv_5Fregion"></a>

```c
struct sys_mm_drv_region
```

相关声明：[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)。

表示可用内存区域（Available Memory Region）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.2\_内存映射与解除映射（Memory Mapping and Unmapping）

用于内存映射与解除映射（Mapping and Unmapping）。

<a id="r_ga7097d4d8880cb0c3d5db7623ffc11b26"></a>

```c
int sys_mm_drv_map_page (void *virt, uintptr_t phys, uint32_t flags)
```

相关声明：[sys_mm_drv_map_page](#ga7097d4d8880cb0c3d5db7623ffc11b26)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将一个物理页（Physical Page）映射到虚拟地址空间（Virtual Address Space）。

<a id="r_ga40ae51932bc78bc30b72d16342ad6848"></a>

```c
int sys_mm_drv_map_page_safe (const struct sys_mm_drv_region *virtual_region, void *virt, uintptr_t phys, uint32_t flags)
```

相关声明：[sys_mm_drv_map_page_safe](#ga40ae51932bc78bc30b72d16342ad6848)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

进行区域检查（Region Check），将一个物理页映射到虚拟地址空间。

<a id="r_ga1186a31d55b24791d800e8f0aef311da"></a>

```c
int sys_mm_drv_map_region (void *virt, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_map_region](#ga1186a31d55b24791d800e8f0aef311da)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将一段物理内存区域（Physical Memory Region）映射到虚拟地址空间。

<a id="r_ga15e6a5870378aeb6c7f285e23dd35f06"></a>

```c
int sys_mm_drv_map_region_safe (const struct sys_mm_drv_region *virtual_region, void *virt, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_map_region_safe](#ga15e6a5870378aeb6c7f285e23dd35f06)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

进行区域检查（Region Check），将一段物理内存区域映射到虚拟地址空间。

<a id="r_gab36baa1ed134e5a69ea16451991b920e"></a>

```c
int sys_mm_drv_map_array (void *virt, uintptr_t *phys, size_t cnt, uint32_t flags)
```

相关声明：[sys_mm_drv_map_array](#gab36baa1ed134e5a69ea16451991b920e)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将物理内存数组（Physical Memory Array）映射到虚拟地址空间。

<a id="r_gab78668dd05ab1d4d17ca5bbe3182b0eb"></a>

```c
int sys_mm_drv_unmap_page (void *virt)
```

相关声明：[sys_mm_drv_unmap_page](#gab78668dd05ab1d4d17ca5bbe3182b0eb)。

移除所给虚拟地址对应的一个页的映射（Mapping）。

<a id="r_gadc3ed78e29aef49b7578b9090dcaacbc"></a>

```c
int sys_mm_drv_unmap_region (void *virt, size_t size)
```

相关声明：[sys_mm_drv_unmap_region](#gadc3ed78e29aef49b7578b9090dcaacbc)。

移除指定虚拟地址范围的映射。

<a id="r_gae46a4189560e314e96f8bee80b55b40b"></a>

```c
int sys_mm_drv_remap_region (void *virt_old, size_t size, void *virt_new)
```

相关声明：[sys_mm_drv_remap_region](#gae46a4189560e314e96f8bee80b55b40b)。

将虚拟页（Virtual Pages）重新映射到新地址。

## 6.3\_内存移动（Memory Moving）

用于移动已映射内存（Moving Mapped Memory）。

<a id="r_ga3b2e4b2b359d4fcba104e43866d30d14"></a>

```c
int sys_mm_drv_move_region (void *virt_old, size_t size, void *virt_new, uintptr_t phys_new)
```

相关声明：[sys_mm_drv_move_region](#ga3b2e4b2b359d4fcba104e43866d30d14)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

通过复制在物理层面移动内存（Physically Move Memory）。

<a id="r_gab172793104608d2a5acae0eb40c50177"></a>

```c
int sys_mm_drv_move_array (void *virt_old, size_t size, void *virt_new, uintptr_t *phys_new, size_t phys_cnt)
```

相关声明：[sys_mm_drv_move_array](#gab172793104608d2a5acae0eb40c50177)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

通过复制在物理层面移动内存（Physically Move Memory）。

## 6.4\_内存映射属性（Memory Mapping Attributes）

用于操作已映射内存的属性（Attributes）。

<a id="r_ga188aebe0dcb10e8a4d620cf0bf9a0444"></a>

```c
int sys_mm_drv_update_page_flags (void *virt, uint32_t flags)
```

相关声明：[sys_mm_drv_update_page_flags](#ga188aebe0dcb10e8a4d620cf0bf9a0444)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

更新内存页标志（Memory Page Flags）。

<a id="r_ga60a9aa179216ed7ac5179c3a7eeb97d3"></a>

```c
int sys_mm_drv_update_region_flags (void *virt, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_update_region_flags](#ga60a9aa179216ed7ac5179c3a7eeb97d3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

更新内存区域标志（Memory Region Flags）。

## 6.5\_内存映射查询（Memory Mappings Query）

用于查询内存映射信息（Memory Mapping Information）。

<a id="r_gaabbc2184a44f8c5c8cd98bf09a2cdc0f"></a>

```c
int sys_mm_drv_page_phys_get (void *virt, uintptr_t *phys)
```

相关声明：[sys_mm_drv_page_phys_get](#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据虚拟地址获取已映射物理内存地址（Physical Memory Address）。

<a id="r_gaf2c06488bd4ff3ecd1285ce7d70321c9"></a>

```c
const struct sys_mm_drv_region * sys_mm_drv_query_memory_regions (void)
```

相关声明：[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[sys_mm_drv_query_memory_regions](#gaf2c06488bd4ff3ecd1285ce7d70321c9)。

查询可用内存区域（Available Memory Regions）。

<a id="r_gab8d3585ffe98796a5c74d0bb9fc634d1"></a>

```c
void sys_mm_drv_query_memory_regions_free (const struct sys_mm_drv_region *regions)
```

相关声明：[sys_mm_drv_query_memory_regions_free](#gab8d3585ffe98796a5c74d0bb9fc634d1)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)。

释放 `sys_mm_drv_query_memory_regions` 返回的内存数组（Memory Array）。

<a id="r_gabd2c5de68d1976e4d0a8086523d66e7a"></a>

```c
#define SYS_MM_DRV_MEMORY_REGION_FOREACH(regions, iter)
```

相关声明：[SYS_MM_DRV_MEMORY_REGION_FOREACH](#gabd2c5de68d1976e4d0a8086523d66e7a)。

遍历 `sys_mm_drv_query_memory_regions` 返回的区域数组（Region Array）。

## 6.6\_缓存模式定义（Caching Mode Definitions）

这些选项互斥（Mutually Exclusive）。

<a id="r_gafe1b7f8b4075da1b461f2a74d3142e49"></a>

```c
#define SYS_MM_MEM_CACHE_NONE 2
```

相关声明：[SYS_MM_MEM_CACHE_NONE](#gafe1b7f8b4075da1b461f2a74d3142e49)。

不使用缓存（No Caching）。

<a id="r_gaed12cd6841eb0fd0af1cefe1d7a6b5aa"></a>

```c
#define SYS_MM_MEM_CACHE_WT 1
```

相关声明：[SYS_MM_MEM_CACHE_WT](#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)。

直写缓存（Write-through Caching）。

<a id="r_gad0859fb79c8da1d1af0f38ea63064b8c"></a>

```c
#define SYS_MM_MEM_CACHE_WB 0
```

相关声明：[SYS_MM_MEM_CACHE_WB](#gad0859fb79c8da1d1af0f38ea63064b8c)。

完整回写缓存（Full Write-back Caching）。

<a id="r_ga43050af5740a0449da7998b48f540817"></a>

```c
#define SYS_MM_MEM_CACHE_MASK (BIT(3) - 1)
```

相关声明：[SYS_MM_MEM_CACHE_MASK](#ga43050af5740a0449da7998b48f540817)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

为缓存模式（Cache Modes）预留的位。

## 6.7\_区域权限属性（Region Permission Attributes）

默认应为只读（Read-only），不允许用户模式访问，也不允许执行（No User, No Exec）。

<a id="r_ga8547ea32c40b038daa34ee76cbaee275"></a>

```c
#define SYS_MM_MEM_PERM_RW BIT(3)
```

相关声明：[SYS_MM_MEM_PERM_RW](#ga8547ea32c40b038daa34ee76cbaee275)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="r_gac564b8d2148bd7c0ac07313f0fa9861c"></a>

```c
#define SYS_MM_MEM_PERM_EXEC BIT(4)
```

相关声明：[SYS_MM_MEM_PERM_EXEC](#gac564b8d2148bd7c0ac07313f0fa9861c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可执行（Executable）；通常禁止执行。

<a id="r_gad86f6d8cbb3102ad3e8375d10cb4551c"></a>

```c
#define SYS_MM_MEM_PERM_USER BIT(5)
```

相关声明：[SYS_MM_MEM_PERM_USER](#gad86f6d8cbb3102ad3e8375d10cb4551c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

## 6.8\_详细说明（Detailed Documentation）

<a id="gabd2c5de68d1976e4d0a8086523d66e7a"></a>

### `SYS_MM_DRV_MEMORY_REGION_FOREACH`

```c
#define SYS_MM_DRV_MEMORY_REGION_FOREACH ( regions, iter )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

展开值（Value）：

```c
for (iter = regions; iter->size; iter++)
```

遍历 `sys_mm_drv_query_memory_regions` 返回的区域数组（Region Array）。

注意：此宏要求数组中存在标记末尾的哨兵项（Sentinel Item）才能正常工作。

<a id="ga43050af5740a0449da7998b48f540817"></a>

### `SYS_MM_MEM_CACHE_MASK`

```c
#define SYS_MM_MEM_CACHE_MASK (BIT(3) - 1)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

为缓存模式（Cache Modes）预留的位。

<a id="gafe1b7f8b4075da1b461f2a74d3142e49"></a>

### `SYS_MM_MEM_CACHE_NONE`

```c
#define SYS_MM_MEM_CACHE_NONE 2
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

不使用缓存（No Caching）。

<a id="gad0859fb79c8da1d1af0f38ea63064b8c"></a>

### `SYS_MM_MEM_CACHE_WB`

```c
#define SYS_MM_MEM_CACHE_WB 0
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

完整回写缓存（Full Write-back Caching）。

<a id="gaed12cd6841eb0fd0af1cefe1d7a6b5aa"></a>

### `SYS_MM_MEM_CACHE_WT`

```c
#define SYS_MM_MEM_CACHE_WT 1
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

直写缓存（Write-through Caching）。

<a id="gac564b8d2148bd7c0ac07313f0fa9861c"></a>

### `SYS_MM_MEM_PERM_EXEC`

```c
#define SYS_MM_MEM_PERM_EXEC BIT(4)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

区域可执行（Executable）；通常禁止执行。

<a id="ga8547ea32c40b038daa34ee76cbaee275"></a>

### `SYS_MM_MEM_PERM_RW`

```c
#define SYS_MM_MEM_PERM_RW BIT(3)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="gad86f6d8cbb3102ad3e8375d10cb4551c"></a>

### `SYS_MM_MEM_PERM_USER`

```c
#define SYS_MM_MEM_PERM_USER BIT(5)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

<a id="gab36baa1ed134e5a69ea16451991b920e"></a>

### `sys_mm_drv_map_array()`

```c
int sys_mm_drv_map_array ( void * virt, uintptr_t * phys, size_t cnt, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

将物理内存数组（Physical Memory Array）映射到虚拟地址空间。

将一组物理页（Physical Pages）映射到连续虚拟地址空间（Continuous Virtual Address Space）。假定地址已按页对齐（Page-aligned）；传入未对齐地址时，行为未定义（Undefined Behavior）。

此操作不会访问物理内存页（Physical Memory Pages）本身。

此 API 必须能够在中断服务例程（ISRs）或异常处理程序（Exception Handlers）中安全调用，并假定对它的调用已经串行化（Serialized）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要映射到的、按页对齐的目标虚拟地址（Destination Virtual Address）。 |
| `phys` | 待映射的、按页对齐的源物理地址数组（Source Physical Address Array）。 |
| `cnt` | 物理页数组（Physical Page Array）的元素数量。 |
| `flags` | 缓存、访问与控制标志（Caching, Access and Control Flags），参见 `SYS_MM_MEM_*` 宏。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 任何虚拟地址（Virtual Addresses）已被映射时。 |

<a id="ga7097d4d8880cb0c3d5db7623ffc11b26"></a>

### `sys_mm_drv_map_page()`

```c
int sys_mm_drv_map_page ( void * virt, uintptr_t phys, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

将一个物理页（Physical Page）映射到虚拟地址空间（Virtual Address Space）。

将一个物理页（Physical Page）映射到虚拟地址空间（Virtual Address Space）。假定地址已按页对齐（Page-aligned）；传入未对齐地址时，行为未定义（Undefined Behavior）。

此操作不会访问内存区域本身。

此 API 必须能够在中断服务例程（ISRs）或异常处理程序（Exception Handlers）中安全调用，并假定对它的调用已经串行化（Serialized）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要映射到的、按页对齐的目标虚拟地址（Destination Virtual Address）。 |
| `phys` | 待映射的、按页对齐的源物理地址（Source Physical Address）。 |
| `flags` | 缓存、访问与控制标志（Caching, Access and Control Flags），参见 `SYS_MM_MEM_*` 宏。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址（Virtual Address）已被映射时。 |

<a id="ga40ae51932bc78bc30b72d16342ad6848"></a>

### `sys_mm_drv_map_page_safe()`

```c
int sys_mm_drv_map_page_safe ( const struct sys_mm_drv_region * virtual_region, void * virt, uintptr_t phys, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

进行区域检查（Region Check），将一个物理页映射到虚拟地址空间。

通过调用 sys_mm_drv_map_page，将一个物理页（Physical Page）映射到虚拟地址空间（Virtual Address Space）。相关说明参见 sys_mm_drv_map_page。

调用前执行安全检查（Safety Check），验证被映射的虚拟内存页是否完全位于给定虚拟区域内。

<a id="ga1186a31d55b24791d800e8f0aef311da"></a>

### `sys_mm_drv_map_region()`

```c
int sys_mm_drv_map_region ( void * virt, uintptr_t phys, size_t size, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

将一段物理内存区域（Physical Memory Region）映射到虚拟地址空间。

将一段物理内存区域（Physical Memory Region）映射到虚拟地址空间（Virtual Address Space）。假定地址和大小均按页对齐；传入未对齐的地址或大小时，行为未定义（Undefined Behavior）。

此操作不会访问内存区域本身。

此 API 必须能够在中断服务例程（ISRs）或异常处理程序（Exception Handlers）中安全调用，并假定对它的调用已经串行化（Serialized）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要映射到的、按页对齐的目标虚拟地址（Destination Virtual Address）。 |
| `phys` | 待映射的、按页对齐的源物理地址（Source Physical Address）。 |
| `size` | 映射内存区域的大小，单位为字节，须按页对齐。 |
| `flags` | 缓存、访问与控制标志（Caching, Access and Control Flags），参见 `SYS_MM_MEM_*` 宏。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 任何虚拟地址（Virtual Addresses）已被映射时。 |

<a id="ga15e6a5870378aeb6c7f285e23dd35f06"></a>

### `sys_mm_drv_map_region_safe()`

```c
int sys_mm_drv_map_region_safe ( const struct sys_mm_drv_region * virtual_region, void * virt, uintptr_t phys, size_t size, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

进行区域检查（Region Check），将一段物理内存区域映射到虚拟地址空间。

通过调用 sys_mm_drv_map_region，将一段物理内存区域（Physical Memory Region）映射到虚拟地址空间（Virtual Address Space）。相关说明参见 sys_mm_drv_map_region。

调用前执行安全检查（Safety Check），验证被映射的虚拟内存页是否全部位于给定虚拟区域内。

<a id="gab172793104608d2a5acae0eb40c50177"></a>

### `sys_mm_drv_move_array()`

```c
int sys_mm_drv_move_array ( void * virt_old, size_t size, void * virt_new, uintptr_t * phys_new, size_t phys_cnt )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

通过复制在物理层面移动内存（Physically Move Memory）。

将一段物理内存区域（Physical Memory Region）映射到新的虚拟地址空间 virt_new，并从旧虚拟地址空间 virt_old 复制大小为 size 的区域。新的虚拟内存区域由一组物理页（Physical Pages）映射而来。

假定地址和大小均按页对齐（Page-aligned）；传入未对齐的地址或大小时，行为未定义（Undefined Behavior）。

注意：此操作不处理内存域（Memory Domains），因此旧地址和新地址处的虚拟内存，在所有可运行 Zephyr 线程的内存域中都必须处于未映射状态（Unmapped）。

注意：为了简化实现，通常不支持旧、新虚拟内存区域重叠（Overlap）。是否允许重叠，请查阅实际驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt_old` | 现有内存按页对齐的虚拟基地址（Base Virtual Address）。 |
| `size` | 映射内存区域的大小，单位为字节，须按页对齐。 |
| `virt_new` | 用于映射新物理页的、按页对齐的虚拟基地址（Base Virtual Address）。 |
| `phys_new` | 用于容纳移动后内存内容的、按页对齐的物理地址数组（Physical Address Array）。 |
| `phys_cnt` | 物理页数组（Physical Page Array）的元素数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 旧虚拟地址并非全部已映射，或新虚拟地址并非全部未映射时。 |

<a id="ga3b2e4b2b359d4fcba104e43866d30d14"></a>

### `sys_mm_drv_move_region()`

```c
int sys_mm_drv_move_region ( void * virt_old, size_t size, void * virt_new, uintptr_t phys_new )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

通过复制在物理层面移动内存（Physically Move Memory）。

将一段物理内存区域（Physical Memory Region）映射到新的虚拟地址空间 virt_new，并从旧虚拟地址空间 virt_old 复制大小为 size 的区域。新的虚拟内存区域由起始地址为 phys_new、大小为 size 的物理内存映射而来。

假定地址和大小均按页对齐（Page-aligned）；传入未对齐的地址或大小时，行为未定义（Undefined Behavior）。

注意：此操作不处理内存域（Memory Domains），因此旧地址和新地址处的虚拟内存，在所有可运行 Zephyr 线程的内存域中都必须处于未映射状态（Unmapped）。

注意：为了简化实现，通常不支持旧、新虚拟内存区域重叠（Overlap）。是否允许重叠，请查阅实际驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt_old` | 现有内存按页对齐的虚拟基地址（Base Virtual Address）。 |
| `size` | 映射内存区域的大小，单位为字节，须按页对齐。 |
| `virt_new` | 用于映射新物理页的、按页对齐的虚拟基地址（Base Virtual Address）。 |
| `phys_new` | 用于容纳移动后内存内容的、按页对齐的物理基地址（Base Physical Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 旧虚拟地址并非全部已映射，或新虚拟地址并非全部未映射时。 |

<a id="gaabbc2184a44f8c5c8cd98bf09a2cdc0f"></a>

### `sys_mm_drv_page_phys_get()`

```c
int sys_mm_drv_page_phys_get ( void * virt, uintptr_t * phys )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

根据虚拟地址获取已映射物理内存地址（Physical Memory Address）。

此函数查询地址转换表（Translation Tables），查找已映射虚拟地址对应的物理内存地址（Physical Memory Address）。

假定地址已按页对齐（Page-aligned）；传入未对齐地址时，行为未定义（Undefined Behavior）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` virt` | 按页对齐的虚拟地址。 |
| `[out] phys` | 映射到的物理地址；若只检查虚拟地址是否已映射，可以为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 找到有效映射时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址未映射时。 |

<a id="gaf2c06488bd4ff3ecd1285ce7d70321c9"></a>

### `sys_mm_drv_query_memory_regions()`

```c
const struct sys_mm_drv_region * sys_mm_drv_query_memory_regions ( void )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

查询可用内存区域（Available Memory Regions）。

返回可用内存区域数组（Memory Regions Array），可使用 SYS_MM_DRV_MEMORY_REGION_FOREACH 遍历。数组最后一项是标记末尾的哨兵（Sentinel），通过其值为 0 的 size 属性识别。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `regions` | 可能为空的内存区域数组（Memory Regions Array），即仅包含末尾哨兵项（Sentinel）。 |

<a id="gab8d3585ffe98796a5c74d0bb9fc634d1"></a>

### `sys_mm_drv_query_memory_regions_free()`

```c
void sys_mm_drv_query_memory_regions_free ( const struct sys_mm_drv_region * regions)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

释放 `sys_mm_drv_query_memory_regions` 返回的内存数组（Memory Array）。

驱动可能动态分配了 sys_mm_drv_query_memory_regions 返回的区域数组所用内存。此方法使驱动有机会释放相关资源（Resources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `regions` | 先前由 sys_mm_drv_query_memory_regions 返回的区域数组（Regions Array）。 |

<a id="gae46a4189560e314e96f8bee80b55b40b"></a>

### `sys_mm_drv_remap_region()`

```c
int sys_mm_drv_remap_region ( void * virt_old, size_t size, void * virt_new )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

将虚拟页（Virtual Pages）重新映射到新地址。

将起始于 virt_old、大小为 size 的虚拟内存区域重新映射到起始于 virt_new 的新虚拟内存区域。换言之，将 virt_old 处对应的物理内存重新映射，使其出现在 virt_new。两个地址都必须按页对齐（Page-aligned）且有效。

注意：此操作不处理内存域（Memory Domains），因此旧地址和新地址处的虚拟内存，在所有可运行 Zephyr 线程的内存域中都必须处于未映射状态（Unmapped）。

注意：为了简化实现，通常不支持旧、新虚拟内存区域重叠（Overlap）。是否允许重叠，请查阅实际驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt_old` | 现有内存按页对齐的虚拟基地址（Base Virtual Address）。 |
| `size` | 映射内存区域的大小，单位为字节，须按页对齐。 |
| `virt_new` | 要将内存重新映射到的、按页对齐的虚拟基地址（Base Virtual Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 旧虚拟地址并非全部已映射，或新虚拟地址并非全部未映射时。 |

<a id="gab78668dd05ab1d4d17ca5bbe3182b0eb"></a>

### `sys_mm_drv_unmap_page()`

```c
int sys_mm_drv_unmap_page ( void * virt)
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

移除所给虚拟地址对应的一个页的映射（Mapping）。

从虚拟地址空间（Virtual Address Space）取消一个页的映射（Unmap）。

完成后，相关地址转换表项（Translation Table Entries）将更新为如同该内存页从未建立过映射，无需保留先前上下文。此函数必须更新所有活动地址转换表中的映射。

假定地址已按页对齐（Page-aligned）；传入未对齐地址时，行为未定义（Undefined Behavior）。

实现必须按需使地址转换缓存（Translation Caching）失效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要取消映射的、按页对齐的虚拟地址（Virtual Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址未映射时。 |

<a id="gadc3ed78e29aef49b7578b9090dcaacbc"></a>

### `sys_mm_drv_unmap_region()`

```c
int sys_mm_drv_unmap_region ( void * virt, size_t size )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

移除指定虚拟地址范围的映射。

取消所给虚拟地址范围（Virtual Address Range）中各页的映射。

完成后，相关地址转换表项（Translation Table Entries）将更新为如同该内存范围从未建立过映射，无需保留先前上下文。此函数必须更新所有活动地址转换表中的映射。

假定地址已按页对齐（Page-aligned）；传入未对齐地址时，行为未定义（Undefined Behavior）。

实现必须按需使地址转换缓存（Translation Caching）失效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 按页对齐、待解除映射的虚拟基址。 |
| `size` | 按页对齐的区域大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址未映射时。 |

<a id="ga188aebe0dcb10e8a4d620cf0bf9a0444"></a>

### `sys_mm_drv_update_page_flags()`

```c
int sys_mm_drv_update_page_flags ( void * virt, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

更新内存页标志（Memory Page Flags）。

更改已映射到虚拟地址的物理内存页的属性（Attributes）。特定内存区域的用途变化时，这很有用。例如，将库／模块代码复制到内存时，需要可读写属性（Read-write）；复制完成、准备执行代码时，则应改为只读／可执行（Read-only/Executable）。调用此 API 不得导致内存内容丢失。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要更新的、按页对齐的虚拟地址（Virtual Address）。 |
| `flags` | 缓存、访问与控制标志（Caching, Access and Control Flags），参见 `SYS_MM_MEM_*` 宏。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址未映射（Not Mapped）时。 |

<a id="ga60a9aa179216ed7ac5179c3a7eeb97d3"></a>

### `sys_mm_drv_update_region_flags()`

```c
int sys_mm_drv_update_region_flags ( void * virt, size_t size, uint32_t flags )
```

```c
#include <zephyr/drivers/mm/system_mm.h>
```

更新内存区域标志（Memory Region Flags）。

更改已映射到虚拟地址的物理内存的属性（Attributes）。特定内存区域的用途变化时，这很有用。例如，将库／模块代码复制到内存时，需要可读写属性（Read-write）；复制完成、准备执行代码时，则应改为只读／可执行（Read-only/Executable）。调用此 API 不得导致内存内容丢失。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 要更新的、按页对齐的虚拟地址（Virtual Address）。 |
| `size` | 映射内存区域的大小，单位为字节，须按页对齐。 |
| `flags` | 缓存、访问与控制标志（Caching, Access and Control Flags），参见 `SYS_MM_MEM_*` 宏。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 提供了无效参数（Invalid Arguments）时。 |
| `-EFAULT` | 虚拟地址未映射（Not Mapped）时。 |


## 6.9\_原页交叉引用（Cross References）

- [sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/drivers/mm/system_mm.h](../api_file_serial_motion_reference/P009_zephyr__drivers__mm__system_mm.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_MAX32664C API主题.md) · [返回大纲](大纲.md) · [下一章](P007_元素（Elements）.md)
