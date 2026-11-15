---
id: learning.zephyr-docs.api-source-system-reference.page-19
title: mm_drv_intel_adsp_mtl_tlb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_mm\_drv\_intel\_adsp\_mtl\_tlb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md)。

## 19.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="amm__drv__intel__adsp__mtl__tlb_8h_html_a19135d221cf896eb1795c2f22f6679bc"></a>
<a id="amm__drv__intel__adsp__mtl__tlb_8h_html_a9c9ca0a75fdbb3806d5ca6e37f51ad11"></a>
<a id="amm__drv__intel__adsp__mtl__tlb_8h_html_aa98be3168d56e8fb7e183563eb64cbdb"></a>
<a id="amm__drv__intel__adsp__mtl__tlb_8h_html_aec3b78e74d53f6a9fe6ca029c7d776a5"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructintel__adsp__tlb__api_html"></a>
<a id="astructintel__adsp__tlb__api_html_a49ce206e8ac75d0fad79af3bb5cd9447"></a>
<a id="astructintel__adsp__tlb__api_html_ad9788abb323e4c70c08178c9df98a62e"></a>

```c
/* SPDX-License-Identifier: Apache-2.0 */
/*
 * Copyright (c) 2022 Intel Corporation.
 *
 * Author: Marcin Szkudlinski <marcin.szkudlinski@linux.intel.com>
 *
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_INTEL_ADSP_MTL_TLB_H_
#define ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_INTEL_ADSP_MTL_TLB_H_


/*
 * This function will save contents of the physical memory banks into a provided storage buffer
 *
 * the system must be almost stopped. Operation is destructive - it will change physical to
 * virtual addresses mapping leaving the system not operational
 * Power states of memory banks will stay not touched
 * assuming
 *      - the dcache memory had been invalidated before
 *      - no remapping of addresses below unused_l2_sram_start_marker has been made
 *        (this is ensured by the driver itself - it rejects such remapping request)
 *
 * at this point the memory is still up&running so its safe to use libraries like memcpy
 * and the procedure can be called in a zephyr driver model way
 */
typedef void (*mm_save_context)(void *storage_buffer);

/*
 * This function will return a required size of storage buffer needed to perform context save
 *
 */
typedef uint32_t (*mm_get_storage_size)(void);

/*
 * This function will restore the contents and power state of the physical memory banks
 * and recreate physical to virtual mappings
 *
 * As the system memory is down at this point, the procedure
 *  - MUST be located in IMR memory region
 *  - MUST be called using a simple extern procedure call - API table is not yet loaded
 *  - MUST NOT use libraries, like memcpy, use instead a special version bmemcpy located in IMR
 *
 */
void adsp_mm_restore_context(void *storage_buffer);

/*
 * This procedure return a pointer to a first unused address in L2 virtual memory
 */
uintptr_t adsp_mm_get_unused_l2_start_aligned(void);

struct intel_adsp_tlb_api {
        mm_save_context save_context;
        mm_get_storage_size get_storage_size;
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_INTEL_ADSP_MTL_TLB_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 2 行

版权所有（Copyright）2022 Intel Corporation。

作者（Author）：Marcin Szkudlinski，邮箱：`marcin.szkudlinski@linux.intel.com`。

### 注释 3：原第 13 行

本函数将物理内存组（Physical Memory Banks）的内容保存到提供的存储缓冲区（Storage Buffer）中。

系统必须几乎完全停止。此操作具有破坏性（Destructive）：它会改变物理地址到虚拟地址的映射（Physical-to-Virtual Address Mapping），使系统暂时无法正常工作。内存组的电源状态（Power States）保持不变。操作假定：

- 数据缓存（Dcache）此前已经失效处理（Invalidated）。
- 未对 `unused_l2_sram_start_marker` 以下的地址进行重映射（Remapping）；驱动自身通过拒绝此类重映射请求保证这一点。

此时内存仍正常工作，因此可安全使用 `memcpy` 等库函数，并且可按 Zephyr 驱动模型（Driver Model）的方式调用该过程。

### 注释 4：原第 29 行

本函数返回执行上下文保存（Context Save）所需的存储缓冲区大小（Storage Buffer Size）。

### 注释 5：原第 35 行

本函数恢复物理内存组（Physical Memory Banks）的内容和电源状态（Power State），并重建物理地址到虚拟地址的映射（Physical-to-Virtual Mappings）。

由于此时系统内存不可用，该过程：

- 必须位于隔离内存区域（IMR Memory Region）。
- 必须通过普通 `extern` 过程调用进入，因为 API 表尚未加载。
- 不得使用 `memcpy` 等库函数，必须改用位于 IMR 中的专用版本 `bmemcpy`。

### 注释 6：原第 47 行

本过程返回指向 L2 虚拟内存（Virtual Memory）中第一个未使用地址的指针（Pointer）。

### 注释 7：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_INTEL_ADSP_MTL_TLB_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md)
- [mm_save_context](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md#aec3b78e74d53f6a9fe6ca029c7d776a5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mm_get_storage_size](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md#a19135d221cf896eb1795c2f22f6679bc)
- [adsp_mm_restore_context](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md#aa98be3168d56e8fb7e183563eb64cbdb)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [adsp_mm_get_unused_l2_start_aligned](../api_file_reference/P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md#a9c9ca0a75fdbb3806d5ca6e37f51ad11)
- [intel_adsp_tlb_api](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md)
- [save_context](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md#ad9788abb323e4c70c08178c9df98a62e)
- [get_storage_size](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md#a49ce206e8ac75d0fad79af3bb5cd9447)
- [intel_adsp_tlb_api::get_storage_size](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md#a49ce206e8ac75d0fad79af3bb5cd9447)
- [intel_adsp_tlb_api::save_context](../platform_security_model_reference/P014_intel_adsp_tlb_api_结构体.md#ad9788abb323e4c70c08178c9df98a62e)

---

[上一章](P018_smp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_mqtt.h_源码浏览.md)
