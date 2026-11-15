---
id: learning.zephyr-docs.api-source-supplement-reference.page-221
title: system_mm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第221章\_system\_mm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h.html)。

## 221.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00036"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00072"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00101"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00276"></a>
<a id="l00284"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00357"></a>
<a id="l00365"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00414"></a>
<a id="l00422"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00480"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="agroup__mm__drv__apis_html_ga1186a31d55b24791d800e8f0aef311da"></a>
<a id="agroup__mm__drv__apis_html_ga15e6a5870378aeb6c7f285e23dd35f06"></a>
<a id="agroup__mm__drv__apis_html_ga188aebe0dcb10e8a4d620cf0bf9a0444"></a>
<a id="agroup__mm__drv__apis_html_ga3b2e4b2b359d4fcba104e43866d30d14"></a>
<a id="agroup__mm__drv__apis_html_ga40ae51932bc78bc30b72d16342ad6848"></a>
<a id="agroup__mm__drv__apis_html_ga60a9aa179216ed7ac5179c3a7eeb97d3"></a>
<a id="agroup__mm__drv__apis_html_ga7097d4d8880cb0c3d5db7623ffc11b26"></a>
<a id="agroup__mm__drv__apis_html_gaabbc2184a44f8c5c8cd98bf09a2cdc0f"></a>
<a id="agroup__mm__drv__apis_html_gab172793104608d2a5acae0eb40c50177"></a>
<a id="agroup__mm__drv__apis_html_gab36baa1ed134e5a69ea16451991b920e"></a>
<a id="agroup__mm__drv__apis_html_gab78668dd05ab1d4d17ca5bbe3182b0eb"></a>
<a id="agroup__mm__drv__apis_html_gab8d3585ffe98796a5c74d0bb9fc634d1"></a>
<a id="agroup__mm__drv__apis_html_gadc3ed78e29aef49b7578b9090dcaacbc"></a>
<a id="agroup__mm__drv__apis_html_gae46a4189560e314e96f8bee80b55b40b"></a>
<a id="agroup__mm__drv__apis_html_gaf2c06488bd4ff3ecd1285ce7d70321c9"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructsys__mm__drv__region_html"></a>
<a id="astructsys__mm__drv__region_html_a5b48a908a5393fec377edcd3760c18ad"></a>
<a id="astructsys__mm__drv__region_html_a6838fe4bd4daab440152c4d666a4597d"></a>
<a id="astructsys__mm__drv__region_html_a8dfa465f83cf5f6115094b6b5727f418"></a>

```c
/*
 * Copyright (c) 2021 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MM_SYSTEM_MM_H_
#define ZEPHYR_INCLUDE_DRIVERS_MM_SYSTEM_MM_H_

#include <zephyr/types.h>

#ifndef _ASMLANGUAGE

#ifdef __cplusplus
extern "C" {
#endif



#define SYS_MM_MEM_CACHE_NONE           2

#define SYS_MM_MEM_CACHE_WT             1

#define SYS_MM_MEM_CACHE_WB             0

#define SYS_MM_MEM_CACHE_MASK           (BIT(3) - 1)

struct sys_mm_drv_region {
        void *addr;
        size_t size;
        uint32_t attr;
};



#define SYS_MM_MEM_PERM_RW              BIT(3)

#define SYS_MM_MEM_PERM_EXEC            BIT(4)

#define SYS_MM_MEM_PERM_USER            BIT(5)



int sys_mm_drv_map_page(void *virt, uintptr_t phys, uint32_t flags);

int sys_mm_drv_map_page_safe(const struct sys_mm_drv_region *virtual_region,
                             void *virt, uintptr_t phys, uint32_t flags);

int sys_mm_drv_map_region(void *virt, uintptr_t phys,
                          size_t size, uint32_t flags);

int sys_mm_drv_map_region_safe(const struct sys_mm_drv_region *virtual_region,
                               void *virt, uintptr_t phys, size_t size,
                               uint32_t flags);

int sys_mm_drv_map_array(void *virt, uintptr_t *phys,
                         size_t cnt, uint32_t flags);

int sys_mm_drv_unmap_page(void *virt);

int sys_mm_drv_unmap_region(void *virt, size_t size);

int sys_mm_drv_remap_region(void *virt_old, size_t size, void *virt_new);



int sys_mm_drv_move_region(void *virt_old, size_t size, void *virt_new,
                           uintptr_t phys_new);

int sys_mm_drv_move_array(void *virt_old, size_t size, void *virt_new,
                          uintptr_t *phys_new, size_t phys_cnt);




int sys_mm_drv_update_page_flags(void *virt, uint32_t flags);


int sys_mm_drv_update_region_flags(void *virt, size_t size, uint32_t flags);



int sys_mm_drv_page_phys_get(void *virt, uintptr_t *phys);

/* TODO is it safe to assume no valid region has size == 0? */
#define SYS_MM_DRV_MEMORY_REGION_FOREACH(regions, iter) \
        for (iter = regions; iter->size; iter++)

const struct sys_mm_drv_region *sys_mm_drv_query_memory_regions(void);

void sys_mm_drv_query_memory_regions_free(const struct sys_mm_drv_region *regions);



#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_DRIVERS_MM_SYSTEM_MM_H_ */
```

## 221.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 442 行

待办（TODO）：能否安全地假定有效区域的大小都不为零（`size == 0`）？

### 注释 3：原第 489 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 4：原第 491 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MM_SYSTEM_MM_H_`。

## 221.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys_mm_drv_region](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md)
- [addr](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a8dfa465f83cf5f6115094b6b5727f418)
- [size](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a5b48a908a5393fec377edcd3760c18ad)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [attr](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a6838fe4bd4daab440152c4d666a4597d)
- [sys_mm_drv_map_page](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#ga7097d4d8880cb0c3d5db7623ffc11b26)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
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
- [sys_mm_drv_page_phys_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)
- [sys_mm_drv_query_memory_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaf2c06488bd4ff3ecd1285ce7d70321c9)
- [sys_mm_drv_query_memory_regions_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gab8d3585ffe98796a5c74d0bb9fc634d1)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys_mm_drv_region::size](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a5b48a908a5393fec377edcd3760c18ad)
- [sys_mm_drv_region::attr](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a6838fe4bd4daab440152c4d666a4597d)
- [sys_mm_drv_region::addr](../kernel_runtime_model_reference/P018_sys_mm_drv_region_结构体.md#a8dfa465f83cf5f6115094b6b5727f418)

---

[上一章](P220_sysapic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P222_test_asm_inline_other.h_源码浏览.md)
