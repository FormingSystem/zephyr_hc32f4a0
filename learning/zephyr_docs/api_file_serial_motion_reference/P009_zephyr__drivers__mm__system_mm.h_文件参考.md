---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-9
title: zephyr__drivers__mm__system_mm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_mm\_\_system\_mm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存管理（Memory Management）的驱动API。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

内存管理驱动 API（Memory Management Driver APIs）。包含系统级内存管理驱动（System-wide Memory Management Driver）的 API。系统中仅允许存在一个实例。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_sys_5Fmm_5Fdrv_5Fregion"></a>

```c
struct sys_mm_drv_region
```

相关声明：[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)。

表示可用内存区域（Available Memory Region）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 缓存模式定义（Caching Mode Definitions）

这些选项互斥（Mutually Exclusive）。

<a id="r_gafe1b7f8b4075da1b461f2a74d3142e49"></a>

```c
#define SYS_MM_MEM_CACHE_NONE 2
```

相关声明：[SYS_MM_MEM_CACHE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gafe1b7f8b4075da1b461f2a74d3142e49)。

不使用缓存（No Caching）。

<a id="r_gaed12cd6841eb0fd0af1cefe1d7a6b5aa"></a>

```c
#define SYS_MM_MEM_CACHE_WT 1
```

相关声明：[SYS_MM_MEM_CACHE_WT](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)。

直写缓存（Write-through Caching）。

<a id="r_gad0859fb79c8da1d1af0f38ea63064b8c"></a>

```c
#define SYS_MM_MEM_CACHE_WB 0
```

相关声明：[SYS_MM_MEM_CACHE_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gad0859fb79c8da1d1af0f38ea63064b8c)。

完整回写缓存（Full Write-back Caching）。

<a id="r_ga43050af5740a0449da7998b48f540817"></a>

```c
#define SYS_MM_MEM_CACHE_MASK (BIT(3) - 1)
```

相关声明：[SYS_MM_MEM_CACHE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga43050af5740a0449da7998b48f540817)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

为缓存模式（Cache Modes）预留的位。

<a id="define-members-1"></a>

### 区域权限属性（Region Permission Attributes）

默认应为只读（Read-only），不允许用户模式访问，也不允许执行（No User, No Exec）。

<a id="r_ga8547ea32c40b038daa34ee76cbaee275"></a>

```c
#define SYS_MM_MEM_PERM_RW BIT(3)
```

相关声明：[SYS_MM_MEM_PERM_RW](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga8547ea32c40b038daa34ee76cbaee275)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="r_gac564b8d2148bd7c0ac07313f0fa9861c"></a>

```c
#define SYS_MM_MEM_PERM_EXEC BIT(4)
```

相关声明：[SYS_MM_MEM_PERM_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gac564b8d2148bd7c0ac07313f0fa9861c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可执行（Executable）；通常禁止执行。

<a id="r_gad86f6d8cbb3102ad3e8375d10cb4551c"></a>

```c
#define SYS_MM_MEM_PERM_USER BIT(5)
```

相关声明：[SYS_MM_MEM_PERM_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gad86f6d8cbb3102ad3e8375d10cb4551c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="func-members-0"></a>

### 内存映射与解除映射（Memory Mapping and Unmapping）

用于内存映射与解除映射（Mapping and Unmapping）。

<a id="r_ga7097d4d8880cb0c3d5db7623ffc11b26"></a>

```c
int sys_mm_drv_map_page (void *virt, uintptr_t phys, uint32_t flags)
```

相关声明：[sys_mm_drv_map_page](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga7097d4d8880cb0c3d5db7623ffc11b26)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将一个物理页（Physical Page）映射到虚拟地址空间（Virtual Address Space）。

<a id="r_ga40ae51932bc78bc30b72d16342ad6848"></a>

```c
int sys_mm_drv_map_page_safe (const struct sys_mm_drv_region *virtual_region, void *virt, uintptr_t phys, uint32_t flags)
```

相关声明：[sys_mm_drv_map_page_safe](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga40ae51932bc78bc30b72d16342ad6848)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

进行区域检查（Region Check），将一个物理页映射到虚拟地址空间。

<a id="r_ga1186a31d55b24791d800e8f0aef311da"></a>

```c
int sys_mm_drv_map_region (void *virt, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_map_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga1186a31d55b24791d800e8f0aef311da)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将一段物理内存区域（Physical Memory Region）映射到虚拟地址空间。

<a id="r_ga15e6a5870378aeb6c7f285e23dd35f06"></a>

```c
int sys_mm_drv_map_region_safe (const struct sys_mm_drv_region *virtual_region, void *virt, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_map_region_safe](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga15e6a5870378aeb6c7f285e23dd35f06)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

进行区域检查（Region Check），将一段物理内存区域映射到虚拟地址空间。

<a id="r_gab36baa1ed134e5a69ea16451991b920e"></a>

```c
int sys_mm_drv_map_array (void *virt, uintptr_t *phys, size_t cnt, uint32_t flags)
```

相关声明：[sys_mm_drv_map_array](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab36baa1ed134e5a69ea16451991b920e)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将物理内存数组（Physical Memory Array）映射到虚拟地址空间。

<a id="r_gab78668dd05ab1d4d17ca5bbe3182b0eb"></a>

```c
int sys_mm_drv_unmap_page (void *virt)
```

相关声明：[sys_mm_drv_unmap_page](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab78668dd05ab1d4d17ca5bbe3182b0eb)。

移除所给虚拟地址对应的一个页的映射（Mapping）。

<a id="r_gadc3ed78e29aef49b7578b9090dcaacbc"></a>

```c
int sys_mm_drv_unmap_region (void *virt, size_t size)
```

相关声明：[sys_mm_drv_unmap_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gadc3ed78e29aef49b7578b9090dcaacbc)。

移除指定虚拟地址范围的映射。

<a id="r_gae46a4189560e314e96f8bee80b55b40b"></a>

```c
int sys_mm_drv_remap_region (void *virt_old, size_t size, void *virt_new)
```

相关声明：[sys_mm_drv_remap_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gae46a4189560e314e96f8bee80b55b40b)。

将虚拟页（Virtual Pages）重新映射到新地址。

<a id="func-members-1"></a>

### 内存移动（Memory Moving）

用于移动已映射内存（Moving Mapped Memory）。

<a id="r_ga3b2e4b2b359d4fcba104e43866d30d14"></a>

```c
int sys_mm_drv_move_region (void *virt_old, size_t size, void *virt_new, uintptr_t phys_new)
```

相关声明：[sys_mm_drv_move_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga3b2e4b2b359d4fcba104e43866d30d14)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

通过复制在物理层面移动内存（Physically Move Memory）。

<a id="r_gab172793104608d2a5acae0eb40c50177"></a>

```c
int sys_mm_drv_move_array (void *virt_old, size_t size, void *virt_new, uintptr_t *phys_new, size_t phys_cnt)
```

相关声明：[sys_mm_drv_move_array](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab172793104608d2a5acae0eb40c50177)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

通过复制在物理层面移动内存（Physically Move Memory）。

<a id="func-members-2"></a>

### 内存映射属性（Memory Mapping Attributes）

用于操作已映射内存的属性（Attributes）。

<a id="r_ga188aebe0dcb10e8a4d620cf0bf9a0444"></a>

```c
int sys_mm_drv_update_page_flags (void *virt, uint32_t flags)
```

相关声明：[sys_mm_drv_update_page_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga188aebe0dcb10e8a4d620cf0bf9a0444)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

更新内存页标志（Memory Page Flags）。

<a id="r_ga60a9aa179216ed7ac5179c3a7eeb97d3"></a>

```c
int sys_mm_drv_update_region_flags (void *virt, size_t size, uint32_t flags)
```

相关声明：[sys_mm_drv_update_region_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga60a9aa179216ed7ac5179c3a7eeb97d3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

更新内存区域标志（Memory Region Flags）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.4\_内存映射查询（Memory Mappings Query）

用于查询内存映射信息（Memory Mapping Information）。

<a id="r_gabd2c5de68d1976e4d0a8086523d66e7a"></a>

```c
#define SYS_MM_DRV_MEMORY_REGION_FOREACH(regions, iter)
```

相关声明：[SYS_MM_DRV_MEMORY_REGION_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gabd2c5de68d1976e4d0a8086523d66e7a)。

遍历 `sys_mm_drv_query_memory_regions` 返回的区域数组（Region Array）。

<a id="r_gaabbc2184a44f8c5c8cd98bf09a2cdc0f"></a>

```c
int sys_mm_drv_page_phys_get (void *virt, uintptr_t *phys)
```

相关声明：[sys_mm_drv_page_phys_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据虚拟地址获取已映射物理内存地址（Physical Memory Address）。

<a id="r_gaf2c06488bd4ff3ecd1285ce7d70321c9"></a>

```c
const struct sys_mm_drv_region * sys_mm_drv_query_memory_regions (void)
```

相关声明：[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)、[sys_mm_drv_query_memory_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaf2c06488bd4ff3ecd1285ce7d70321c9)。

查询可用内存区域（Available Memory Regions）。

<a id="r_gab8d3585ffe98796a5c74d0bb9fc634d1"></a>

```c
void sys_mm_drv_query_memory_regions_free (const struct sys_mm_drv_region *regions)
```

相关声明：[sys_mm_drv_query_memory_regions_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab8d3585ffe98796a5c74d0bb9fc634d1)、[sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)。

释放 `sys_mm_drv_query_memory_regions` 返回的内存数组（Memory Array）。


## 9.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P221_system_mm.h_源码浏览.md)
- [sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)
- [SYS_MM_MEM_CACHE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gafe1b7f8b4075da1b461f2a74d3142e49)
- [SYS_MM_MEM_CACHE_WT](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)
- [SYS_MM_MEM_CACHE_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gad0859fb79c8da1d1af0f38ea63064b8c)
- [SYS_MM_MEM_CACHE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga43050af5740a0449da7998b48f540817)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SYS_MM_MEM_PERM_RW](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga8547ea32c40b038daa34ee76cbaee275)
- [SYS_MM_MEM_PERM_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gac564b8d2148bd7c0ac07313f0fa9861c)
- [SYS_MM_MEM_PERM_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gad86f6d8cbb3102ad3e8375d10cb4551c)
- [sys_mm_drv_map_page](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga7097d4d8880cb0c3d5db7623ffc11b26)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [sys_mm_drv_map_page_safe](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga40ae51932bc78bc30b72d16342ad6848)
- [sys_mm_drv_map_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga1186a31d55b24791d800e8f0aef311da)
- [sys_mm_drv_map_region_safe](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga15e6a5870378aeb6c7f285e23dd35f06)
- [sys_mm_drv_map_array](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab36baa1ed134e5a69ea16451991b920e)
- [sys_mm_drv_unmap_page](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab78668dd05ab1d4d17ca5bbe3182b0eb)
- [sys_mm_drv_unmap_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gadc3ed78e29aef49b7578b9090dcaacbc)
- [sys_mm_drv_remap_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gae46a4189560e314e96f8bee80b55b40b)
- [sys_mm_drv_move_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga3b2e4b2b359d4fcba104e43866d30d14)
- [sys_mm_drv_move_array](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab172793104608d2a5acae0eb40c50177)
- [sys_mm_drv_update_page_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga188aebe0dcb10e8a4d620cf0bf9a0444)
- [sys_mm_drv_update_region_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga60a9aa179216ed7ac5179c3a7eeb97d3)
- [SYS_MM_DRV_MEMORY_REGION_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gabd2c5de68d1976e4d0a8086523d66e7a)
- [sys_mm_drv_query_memory_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaf2c06488bd4ff3ecd1285ce7d70321c9)
- [sys_mm_drv_page_phys_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)
- [sys_mm_drv_query_memory_regions_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab8d3585ffe98796a5c74d0bb9fc634d1)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__stepper__stepper_ctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__gpio__wisblock-io-slot.h_文件参考.md)
