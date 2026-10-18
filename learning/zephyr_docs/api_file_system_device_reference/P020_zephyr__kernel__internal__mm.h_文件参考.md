---
id: learning.zephyr-docs.api-file-system-device-reference.page-20
title: zephyr__kernel__internal__mm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/internal_2mm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_kernel\_\_internal\_\_mm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/internal_2mm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
#include <zephyr/devicetree.h>
#include <stdint.h>
#include <stddef.h>
#include <inttypes.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/mem_manage.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_gae9f618604758a034b52509c0377d1bdb"></a>

```c
#define K_MEM_VIRT_OFFSET
```

相关声明：[K_MEM_VIRT_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae9f618604758a034b52509c0377d1bdb)。

从物理地址到永久虚拟映射（permanent virtual mapping）的地址偏移量。

<a id="r_gaeda081ed25c90237b2ca88bc5ae0f254"></a>

```c
#define IS_SRAM_ADDRESS_LOWER(ADDR)
```

相关声明：[IS_SRAM_ADDRESS_LOWER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaeda081ed25c90237b2ca88bc5ae0f254)。

<a id="r_ga38152dff07d0cc76efc4b9eed96e8037"></a>

```c
#define IS_SRAM_ADDRESS_UPPER(ADDR)
```

相关声明：[IS_SRAM_ADDRESS_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga38152dff07d0cc76efc4b9eed96e8037)。

<a id="r_gae0d6fc45cca5dc25d77294b4efb14c80"></a>

```c
#define IS_SRAM_ADDRESS(ADDR)
```

相关声明：[IS_SRAM_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae0d6fc45cca5dc25d77294b4efb14c80)。

<a id="r_ga49b13f5f43530952220fb223c3d56d3c"></a>

```c
#define K_MEM_PHYS_ADDR(virt)
```

相关声明：[K_MEM_PHYS_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga49b13f5f43530952220fb223c3d56d3c)。

根据虚拟地址获取物理地址。

<a id="r_ga850451db4842595d8d96e85a087e8964"></a>

```c
#define K_MEM_VIRT_ADDR(phys)
```

相关声明：[K_MEM_VIRT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga850451db4842595d8d96e85a087e8964)。

根据物理地址获取虚拟地址。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.2\_函数（Functions）

<a id="r_gadc2d4d6258059524eaba2ff139c2f9ff"></a>

```c
static uintptr_t k_mem_phys_addr (void *virt)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[k_mem_phys_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gadc2d4d6258059524eaba2ff139c2f9ff)。

根据虚拟地址获取物理地址。

<a id="r_gaed8dccb2a3c15daff9d2e5b4d49f782a"></a>

```c
static void * k_mem_virt_addr (uintptr_t phys)
```

相关声明：[k_mem_virt_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaed8dccb2a3c15daff9d2e5b4d49f782a)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据物理地址获取虚拟地址。

<a id="r_gaa2c52222198f4c7362c183e1397a4e5c"></a>

```c
void k_mem_map_phys_bare (uint8_t **virt_ptr, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[k_mem_map_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaa2c52222198f4c7362c183e1397a4e5c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将物理内存区域映射到内核虚拟地址空间（virtual address space）。

<a id="r_gae713c4eb253302d06f758f87503cf5dd"></a>

```c
void k_mem_unmap_phys_bare (uint8_t *virt, size_t size)
```

相关声明：[k_mem_unmap_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae713c4eb253302d06f758f87503cf5dd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从内核虚拟地址空间解除虚拟内存区域的映射。

<a id="r_ga2aeab99cba24ac3fd9479dbd421f6c5c"></a>

```c
void * k_mem_map_phys_guard (uintptr_t phys, size_t size, uint32_t flags, bool is_anon)
```

相关声明：[k_mem_map_phys_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga2aeab99cba24ac3fd9479dbd421f6c5c)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将内存映射到虚拟地址空间，并设置保护页（guard pages）。

<a id="r_gaca476fbacb86815edd4898b13ecf5120"></a>

```c
void k_mem_unmap_phys_guard (void *addr, size_t size, bool is_anon)
```

相关声明：[k_mem_unmap_phys_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaca476fbacb86815edd4898b13ecf5120)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

解除通过 `k_mem_map_phys_guard()` 建立的内存映射。


## 20.3\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [zephyr/sys/mem_manage.h](../api_source_supplement_reference/P110_mem_manage.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P011_mm.h_源码浏览.md)
- [K_MEM_VIRT_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae9f618604758a034b52509c0377d1bdb)
- [IS_SRAM_ADDRESS_LOWER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaeda081ed25c90237b2ca88bc5ae0f254)
- [IS_SRAM_ADDRESS_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga38152dff07d0cc76efc4b9eed96e8037)
- [IS_SRAM_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae0d6fc45cca5dc25d77294b4efb14c80)
- [K_MEM_PHYS_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga49b13f5f43530952220fb223c3d56d3c)
- [K_MEM_VIRT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga850451db4842595d8d96e85a087e8964)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [k_mem_phys_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gadc2d4d6258059524eaba2ff139c2f9ff)
- [k_mem_virt_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaed8dccb2a3c15daff9d2e5b4d49f782a)
- [k_mem_map_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaa2c52222198f4c7362c183e1397a4e5c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [k_mem_unmap_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae713c4eb253302d06f758f87503cf5dd)
- [k_mem_map_phys_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#ga2aeab99cba24ac3fd9479dbd421f6c5c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_mem_unmap_phys_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaca476fbacb86815edd4898b13ecf5120)

---

[上一章](P019_zephyr__drivers__interrupt_controller__intc_irqmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__led__is31fl3733.h_文件参考.md)
