---
id: learning.zephyr-docs.api-device-topic-reference.page-17
title: 内存管理（Memory Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_内存管理（Memory Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存管理（Memory Management）

<a id="details"></a>

内存管理（Memory Management）

<a id="header-groups"></a>
<a id="groups"></a>

## 17.1\_主题（Topics）

<a id="r_mm_5Fdrv_5Fbank_5Fapis"></a>

相关声明：[内存组（Memory Banks）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html)。

内存组（Memory Banks）的驱动API。

<a id="r_mem_5Fblocks_5Fapis"></a>

相关声明：[内存块 API（Memory Blocks APIs）](../memblocks_reference/P001_内存块分配公共接口.md)。

<a id="r_mm_5Fdrv_5Fapis"></a>

相关声明：[内存管理（Memory Management）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html)。

内存管理（Memory Management）的驱动API。

<a id="r_word_5Fgranular_5Faccess"></a>

相关声明：[按字粒度访问内存 API（Word Granular Access Memory APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html)。

<a id="header-files"></a>
<a id="files"></a>

## 17.2\_文件（Files）

<a id="r_mem_5Fmanage_2Eh"></a>

```c
file mem_manage.h
```

相关声明：[mem_manage.h](../api_file_configuration_reference/P051_zephyr__sys__mem_manage.h_文件参考.md)。

内存管理辅助接口（Memory Management Helpers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_gaef71defc60c1d898d5ece56c6826a2e1"></a>

```c
bool sys_mm_is_phys_addr_in_range (uintptr_t phys)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sys_mm_is_phys_addr_in_range](#gaef71defc60c1d898d5ece56c6826a2e1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

检查物理地址（Physical Address）是否位于物理内存（Physical Memory）的范围内。

<a id="r_ga1a4b707eae142c8f871a198b865e3d16"></a>

```c
bool sys_mm_is_virt_addr_in_range (void *virt)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sys_mm_is_virt_addr_in_range](#ga1a4b707eae142c8f871a198b865e3d16)。

检查虚拟地址（Virtual Address）是否位于虚拟内存（Virtual Memory）的范围内。

## 17.4\_详细说明（Detailed Documentation）

<a id="gaef71defc60c1d898d5ece56c6826a2e1"></a>

### `sys_mm_is_phys_addr_in_range()`

```c
bool sys_mm_is_phys_addr_in_range ( uintptr_t phys)
```

```c
#include <zephyr/sys/mem_manage.h>
```

检查物理地址（Physical Address）是否位于物理内存（Physical Memory）的范围内。

检查物理地址（physical address）`phys` 是否位于允许范围内，例如 `DT_CHOSEN_SRAM_ADDR` 与 `DT_CHOSEN_SRAM_ADDR + DT_CHOSEN_SRAM_SIZE` 之间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phys` | 待检查的物理地址。 |

**说明（Note）**：注意：仅在启用 `CONFIG_KERNEL_VM_USE_CUSTOM_MEM_RANGE_CHECK` 时使用。

**返回（Returns）**：返回值：物理地址位于范围内时为 true，否则为 false。

<a id="ga1a4b707eae142c8f871a198b865e3d16"></a>

### `sys_mm_is_virt_addr_in_range()`

```c
bool sys_mm_is_virt_addr_in_range ( void * virt)
```

```c
#include <zephyr/sys/mem_manage.h>
```

检查虚拟地址（Virtual Address）是否位于虚拟内存（Virtual Memory）的范围内。

检查虚拟地址（virtual address）`virt` 是否位于允许范围内，例如 `CONFIG_KERNEL_VM_BASE` 与 `CONFIG_KERNEL_VM_BASE + CONFIG_KERNEL_VM_SIZE` 之间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt` | 待检查的虚拟地址。 |

**说明（Note）**：注意：仅在启用 `CONFIG_KERNEL_VM_USE_CUSTOM_MEM_RANGE_CHECK` 时使用。

**返回（Returns）**：返回值：虚拟地址位于范围内时为 true，否则为 false。


## 17.5\_原页交叉引用（Cross References）

- [内存组（Memory Banks）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html)
- [内存块 API（Memory Blocks APIs）](../memblocks_reference/P001_内存块分配公共接口.md)
- [内存管理（Memory Management）的驱动API。](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html)
- [按字粒度访问内存 API（Word Granular Access Memory APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html)
- [mem_manage.h](../api_file_configuration_reference/P051_zephyr__sys__mem_manage.h_文件参考.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [DT_CHOSEN_SRAM_ADDR](../dt_overview_reference/P005_选定SRAM区域宏.md#gad2693f2710d28709b0f129d5b791a29e)
- [DT_CHOSEN_SRAM_SIZE](../dt_overview_reference/P005_选定SRAM区域宏.md#ga0a148f7de43111280b85a3ce4afaddea)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_MFD MAX22017 接口.md) · [返回大纲](大纲.md) · [下一章](P018_队列（Queues）.md)
