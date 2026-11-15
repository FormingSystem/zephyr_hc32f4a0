---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-16
title: zephyr__kernel__mm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_kernel\_\_mm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
#include <zephyr/kernel/internal/mm.h>
#include <stdint.h>
#include <stddef.h>
#include <inttypes.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 缓存模式定义（Caching Mode Definitions）

这些选项互斥（Mutually Exclusive）。

<a id="r_gaae7605452be94d1bd6e0364e9db113c6"></a>

```c
#define K_MEM_CACHE_NONE 2
```

相关声明：[K_MEM_CACHE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaae7605452be94d1bd6e0364e9db113c6)。

不使用缓存（No Caching）。

<a id="r_ga1c8d5fee98c68b08cc6acf781eb35320"></a>

```c
#define K_MEM_CACHE_WT 1
```

相关声明：[K_MEM_CACHE_WT](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1c8d5fee98c68b08cc6acf781eb35320)。

直写缓存（Write-through Caching）。

<a id="r_ga802a69d7a53cafcf357861ab50258c99"></a>

```c
#define K_MEM_CACHE_WB 0
```

相关声明：[K_MEM_CACHE_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga802a69d7a53cafcf357861ab50258c99)。

完整回写缓存（Full Write-back Caching）。

<a id="r_gaae828c97c7bae5d235b863ff3b6b913e"></a>

```c
#define K_MEM_CACHE_MASK (BIT(3) - 1)
```

相关声明：[K_MEM_CACHE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaae828c97c7bae5d235b863ff3b6b913e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`k_map()` 的 `flags` 参数中为缓存模式（Cache Modes）预留的位。

<a id="define-members-1"></a>

### 区域权限属性（Region Permission Attributes）

默认为只读（Read-only），不允许用户模式访问，也不允许执行（No User, No Exec）。

<a id="r_gab9ea94b7155e276f0b653bc1a081866e"></a>

```c
#define K_MEM_PERM_RW BIT(3)
```

相关声明：[K_MEM_PERM_RW](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gab9ea94b7155e276f0b653bc1a081866e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域具有读写访问权限（Read/Write Access），而非只读。

<a id="r_gaf1b0db3c1c5b28b1810f39cdac03f9de"></a>

```c
#define K_MEM_PERM_EXEC BIT(4)
```

相关声明：[K_MEM_PERM_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaf1b0db3c1c5b28b1810f39cdac03f9de)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可执行（Executable）；通常禁止执行。

<a id="r_gaa96222e46728d507ca229796a5724425"></a>

```c
#define K_MEM_PERM_USER BIT(5)
```

相关声明：[K_MEM_PERM_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaa96222e46728d507ca229796a5724425)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域可由用户模式（User Mode）访问；通常仅允许监督模式（Supervisor）访问。

<a id="define-members-2"></a>

### 区域映射行为属性（Region Mapping Behaviour Attributes）

<a id="r_ga36c4d2ede2f91490bc20ec399df663be"></a>

```c
#define K_MEM_DIRECT_MAP BIT(6)
```

相关声明：[K_MEM_DIRECT_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga36c4d2ede2f91490bc20ec399df663be)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域的虚拟地址与物理地址按 1:1 映射（Mapping）。

<a id="define-members-3"></a>

### k_mem_map() 控制标志（Control Flags）

<a id="r_ga0a3569731c9a9f8e94e913f840b4be61"></a>

```c
#define K_MEM_MAP_UNINIT BIT(16)
```

相关声明：[K_MEM_MAP_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga0a3569731c9a9f8e94e913f840b4be61)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不保证已映射区域被清零（Zeroed）。

<a id="r_ga7bed120eac76f03a55b1ab8a1f61ce8b"></a>

```c
#define K_MEM_MAP_LOCK BIT(17)
```

相关声明：[K_MEM_MAP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga7bed120eac76f03a55b1ab8a1f61ce8b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域固定（Pinned）在内存中，永不换页。

<a id="r_ga1275f42967e72f16c58bc3351656bced"></a>

```c
#define K_MEM_MAP_UNPAGED BIT(18)
```

相关声明：[K_MEM_MAP_UNPAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1275f42967e72f16c58bc3351656bced)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

区域采用非分页方式（Unpaged），即：

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_gabb315b4994193147e9f51b0c3268bfcd"></a>

```c
size_t k_mem_free_get (void)
```

相关声明：[k_mem_free_get](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gabb315b4994193147e9f51b0c3268bfcd)。

返回可用空闲内存量（Free Memory）。

<a id="r_gacf5f9c43ac2c31c376fed4a19f607feb"></a>

```c
static void * k_mem_map (size_t size, uint32_t flags)
```

相关声明：[k_mem_map](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gacf5f9c43ac2c31c376fed4a19f607feb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将匿名内存（Anonymous Memory）映射到 Zephyr 地址空间（Address Space）。

<a id="r_ga1867ea13671daae6a5f38929ea9fd64a"></a>

```c
static void k_mem_unmap (void *addr, size_t size)
```

相关声明：[k_mem_unmap](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1867ea13671daae6a5f38929ea9fd64a)。

解除已映射内存的映射（Un-map）。

<a id="r_gaf4740377cd87525fc81fa2ddafef084d"></a>

```c
int k_mem_update_flags (void *addr, size_t size, uint32_t flags)
```

相关声明：[k_mem_update_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaf4740377cd87525fc81fa2ddafef084d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

修改内存映射属性标志（Memory Mapping Attribute Flags）。

<a id="r_gad9a0110394e8026e27deb15687321ee9"></a>

```c
size_t k_mem_region_align (uintptr_t *aligned_addr, size_t *aligned_size, uintptr_t addr, size_t size, size_t align)
```

相关声明：[k_mem_region_align](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gad9a0110394e8026e27deb15687321ee9)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

对于任意给定区域，提供一个覆盖它的对齐区域（Aligned Region）。


## 16.3\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/kernel/internal/mm.h](../api_source_architecture_reference/P011_mm.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [inttypes.h](../api_source_http_wifi_reference/P005_inttypes.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P057_mm.h_源码浏览.md)
- [K_MEM_CACHE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaae7605452be94d1bd6e0364e9db113c6)
- [K_MEM_CACHE_WT](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1c8d5fee98c68b08cc6acf781eb35320)
- [K_MEM_CACHE_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga802a69d7a53cafcf357861ab50258c99)
- [K_MEM_CACHE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaae828c97c7bae5d235b863ff3b6b913e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [K_MEM_PERM_RW](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gab9ea94b7155e276f0b653bc1a081866e)
- [K_MEM_PERM_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaf1b0db3c1c5b28b1810f39cdac03f9de)
- [K_MEM_PERM_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaa96222e46728d507ca229796a5724425)
- [K_MEM_DIRECT_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga36c4d2ede2f91490bc20ec399df663be)
- [K_MEM_MAP_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga0a3569731c9a9f8e94e913f840b4be61)
- [K_MEM_MAP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga7bed120eac76f03a55b1ab8a1f61ce8b)
- [K_MEM_MAP_UNPAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1275f42967e72f16c58bc3351656bced)
- [k_mem_free_get](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gabb315b4994193147e9f51b0c3268bfcd)
- [k_mem_map](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gacf5f9c43ac2c31c376fed4a19f607feb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [k_mem_unmap](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga1867ea13671daae6a5f38929ea9fd64a)
- [k_mem_update_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gaf4740377cd87525fc81fa2ddafef084d)
- [k_mem_region_align](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gad9a0110394e8026e27deb15687321ee9)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

---

[上一章](P015_zephyr__dt-bindings__sensor__lsm6dso16is.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__bluetooth__mesh__msg.h_文件参考.md)
