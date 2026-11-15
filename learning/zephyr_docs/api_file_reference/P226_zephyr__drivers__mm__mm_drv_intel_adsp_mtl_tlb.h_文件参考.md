---
id: learning.zephyr-docs.api-file-reference.page-226
title: zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第226章\_zephyr\_\_drivers\_\_mm\_\_mm\_drv\_intel\_adsp\_mtl\_tlb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 226.1\_数据结构（Data Structures）

<a id="r_intel_5Fadsp_5Ftlb_5Fapi"></a>

```c
struct intel_adsp_tlb_api
```

相关声明：[intel_adsp_tlb_api](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 226.2\_类型定义（Typedefs）

<a id="r_aec3b78e74d53f6a9fe6ca029c7d776a5"></a>

```c
typedef void(* mm_save_context) (void *storage_buffer)
```

相关声明：[mm_save_context](#aec3b78e74d53f6a9fe6ca029c7d776a5)。

<a id="r_a19135d221cf896eb1795c2f22f6679bc"></a>

```c
typedef uint32_t(* mm_get_storage_size) (void)
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mm_get_storage_size](#a19135d221cf896eb1795c2f22f6679bc)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 226.3\_函数（Functions）

<a id="r_aa98be3168d56e8fb7e183563eb64cbdb"></a>

```c
void adsp_mm_restore_context (void *storage_buffer)
```

相关声明：[adsp_mm_restore_context](#aa98be3168d56e8fb7e183563eb64cbdb)。

<a id="r_a9c9ca0a75fdbb3806d5ca6e37f51ad11"></a>

```c
uintptr_t adsp_mm_get_unused_l2_start_aligned (void)
```

相关声明：[uintptr_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[adsp_mm_get_unused_l2_start_aligned](#a9c9ca0a75fdbb3806d5ca6e37f51ad11)。

## 226.4\_详细说明（Detailed Documentation）

<a id="a19135d221cf896eb1795c2f22f6679bc"></a>

### `mm_get_storage_size`

```c
typedef uint32_t(* mm_get_storage_size) (void)
```

<a id="aec3b78e74d53f6a9fe6ca029c7d776a5"></a>

### `mm_save_context`

```c
typedef void(* mm_save_context) (void *storage_buffer)
```

<a id="a9c9ca0a75fdbb3806d5ca6e37f51ad11"></a>

### `adsp_mm_get_unused_l2_start_aligned()`

```c
uintptr_t adsp_mm_get_unused_l2_start_aligned ( void )
```

<a id="aa98be3168d56e8fb7e183563eb64cbdb"></a>

### `adsp_mm_restore_context()`

```c
void adsp_mm_restore_context ( void * storage_buffer)
```


## 226.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html)
- [intel_adsp_tlb_api](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uintptr_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P225_zephyr__drivers__mipi_dsi__mipi_dsi_mcux_2l.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P227_zephyr__posix__sys__mman.h_文件参考.md)
