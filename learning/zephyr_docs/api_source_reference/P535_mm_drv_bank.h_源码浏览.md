---
id: learning.zephyr-docs.api-source-reference.page-535
title: mm_drv_bank.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第535章\_mm\_drv\_bank.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h.html)。

## 535.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00038"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="agroup__mm__drv__bank__apis_html_ga24f5119ac69d07bdba20fbfb2427939f"></a>
<a id="agroup__mm__drv__bank__apis_html_ga55404378ab66ef3393e652a57eacc881"></a>
<a id="agroup__mm__drv__bank__apis_html_gaa0ae8be368233f6dfd88a54ae7ae1db0"></a>
<a id="agroup__mm__drv__bank__apis_html_gac1afd8ab934ce15f77de9d3f113cfa43"></a>
<a id="agroup__mm__drv__bank__apis_html_gad8f2956ec2346812977abf91506911fb"></a>
<a id="akernel_8h_html"></a>
<a id="amem__stats_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructsys__memory__stats_html"></a>
<a id="astructsys__mm__drv__bank_html"></a>
<a id="astructsys__mm__drv__bank_html_a2e84b41e42b801825aa694e569e8ad6c"></a>
<a id="astructsys__mm__drv__bank_html_a69f4b9f6a7fed6403e7271a4ecbe5ad1"></a>
<a id="astructsys__mm__drv__bank_html_a8fd91db4f69c273b2d26bb770292cd83"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_BANK_H_
#define ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_BANK_H_

#include <zephyr/kernel.h>
#include <zephyr/sys/mem_stats.h>
#include <stdint.h>


struct sys_mm_drv_bank {
        uint32_t  unmapped_pages;

        uint32_t  mapped_pages;

        uint32_t  max_mapped_pages;
};

void sys_mm_drv_bank_init(struct sys_mm_drv_bank *bank, uint32_t bank_pages);

uint32_t sys_mm_drv_bank_page_mapped(struct sys_mm_drv_bank *bank);

uint32_t sys_mm_drv_bank_page_unmapped(struct sys_mm_drv_bank *bank);

void sys_mm_drv_bank_stats_reset_max(struct sys_mm_drv_bank *bank);

void sys_mm_drv_bank_stats_get(struct sys_mm_drv_bank *bank,
                               struct sys_memory_stats *stats);


#endif /* ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_BANK_H_ */
```

## 535.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 117 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MM_MM_DRV_BANK_H_`。

## 535.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/mem_stats.h](../lowheap_reference/P019_内存统计头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [unmapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a8fd91db4f69c273b2d26bb770292cd83)
- [mapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a2e84b41e42b801825aa694e569e8ad6c)
- [max_mapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a69f4b9f6a7fed6403e7271a4ecbe5ad1)
- [sys_mm_drv_bank_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gad8f2956ec2346812977abf91506911fb)
- [sys_mm_drv_bank_page_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga24f5119ac69d07bdba20fbfb2427939f)
- [sys_mm_drv_bank_page_unmapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gac1afd8ab934ce15f77de9d3f113cfa43)
- [sys_mm_drv_bank_stats_reset_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga55404378ab66ef3393e652a57eacc881)
- [sys_mm_drv_bank_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gaa0ae8be368233f6dfd88a54ae7ae1db0)
- [sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mem_stats.h](../lowheap_reference/P019_内存统计头文件参考.md)
- [sys_mm_drv_bank::mapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a2e84b41e42b801825aa694e569e8ad6c)
- [sys_mm_drv_bank::max_mapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a69f4b9f6a7fed6403e7271a4ecbe5ad1)
- [sys_mm_drv_bank::unmapped_pages](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md#a8fd91db4f69c273b2d26bb770292cd83)

---

[上一章](P534_mlx90394.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P536_mmc56x3.h_源码浏览.md)
