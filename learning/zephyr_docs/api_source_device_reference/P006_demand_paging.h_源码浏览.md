---
id: learning.zephyr-docs.api-source-device-reference.page-6
title: demand_paging.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_demand\_paging.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00321"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga1192487fdc8d63c025de42162fb204cd"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga25debe925b369765ecd5bd7777ce32d0"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga51f663e0a8c31367082e78097359af6d"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga6ad421ad5671d9df3d96e03361f672e8"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga7ff441f23619b2678bfb72559d5bd592"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga8d4bd3ea311fd873413d0477e8deb464"></a>
<a id="agroup__mem-demand-paging-backing-store_html_ga9becb4908cc7840ece93a2360692962d"></a>
<a id="agroup__mem-demand-paging-eviction_html_ga16a4df904cc7a9641d06741ed589949d"></a>
<a id="agroup__mem-demand-paging-eviction_html_ga228747c10bfd8816aec59fddf0e3a224"></a>
<a id="agroup__mem-demand-paging-eviction_html_ga68dcfc0e5374de2c8ad7b9fe4e65c4f4"></a>
<a id="agroup__mem-demand-paging-eviction_html_ga6bb19be3098cc839ae3f6e9528598867"></a>
<a id="agroup__mem-demand-paging-eviction_html_gaadbb4eb56c239f800daf995e6673ae1d"></a>
<a id="agroup__mem-demand-paging_html_ga0b18037209b4d8b5964bd9a1d760f703"></a>
<a id="agroup__mem-demand-paging_html_ga1da0a643e8f85f98e29288e441a37dfa"></a>
<a id="agroup__mem-demand-paging_html_ga3278aae5e24733c722b7d83c4b17dab3"></a>
<a id="agroup__mem-demand-paging_html_ga52ad88e0c0eed2aa27331bfd4707b7ec"></a>
<a id="agroup__mem-demand-paging_html_ga5f2d422edde7d366e81a870ce057589f"></a>
<a id="agroup__mem-demand-paging_html_gab36c36a4e230677d2090514f7a34b408"></a>
<a id="agroup__mem-demand-paging_html_gae4f80d14f88a46ddb9aeb7afba861864"></a>
<a id="agroup__mem-demand-paging_html_gaec64d019d819b00c7bc3804aac269199"></a>
<a id="agroup__mem-demand-paging_html_gafad6b39cb2faf3bb416cd4d3faaa8d8c"></a>
<a id="ainttypes_8h_html"></a>
<a id="amm_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructk__mem__paging__histogram__t_html"></a>
<a id="astructk__mem__paging__histogram__t_html_a4421676cbc9f6c63808ee914e2ff8c90"></a>
<a id="astructk__mem__paging__histogram__t_html_a893236502aeb56975263b27cf4f2755a"></a>
<a id="astructk__mem__paging__stats__t_html"></a>
<a id="astructk__mem__paging__stats__t_html_a210c83357c14a06fbd69b0cf2263fbb6"></a>
<a id="astructk__mem__paging__stats__t_html_a2c2183c1679ae158bdd232fa1fdeb250"></a>
<a id="astructk__mem__paging__stats__t_html_a3daad63e37d200f44d88c3d4e49f361a"></a>
<a id="astructk__mem__paging__stats__t_html_a4f8523c0e78c8de1e2443a194e875609"></a>
<a id="astructk__mem__paging__stats__t_html_a7b421897b3125d1a44284ca964ef1f66"></a>
<a id="astructk__mem__paging__stats__t_html_aa762731df50fc81d08beb3628f9dbd71"></a>
<a id="astructk__mem__paging__stats__t_html_aa8175953fd7fa0a5057069b73b930f3b"></a>
<a id="astructk__mem__paging__stats__t_html_af6331dae30074d48396151b33ac7a0a7"></a>
<a id="astructk__thread_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_KERNEL_MM_DEMAND_PAGING_H
#define ZEPHYR_INCLUDE_KERNEL_MM_DEMAND_PAGING_H

#include <zephyr/kernel/mm.h>

#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>



#ifndef _ASMLANGUAGE
#include <stdint.h>
#include <stddef.h>
#include <inttypes.h>
#include <zephyr/sys/__assert.h>

struct k_mem_page_frame;

struct k_mem_paging_stats_t {
#if defined(CONFIG_DEMAND_PAGING_STATS) || defined(__DOXYGEN__)
        struct {
                unsigned long                   cnt;

                unsigned long                   irq_locked;

                unsigned long                   irq_unlocked;

#if !defined(CONFIG_DEMAND_PAGING_ALLOW_IRQ) || defined(__DOXYGEN__)
                unsigned long                   in_isr;
#endif /* !CONFIG_DEMAND_PAGING_ALLOW_IRQ */
        } pagefaults;

        struct {
                unsigned long                   clean;

                unsigned long                   dirty;
        } eviction;
#endif /* CONFIG_DEMAND_PAGING_STATS */
};

struct k_mem_paging_histogram_t {
#if defined(CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM) || defined(__DOXYGEN__)
        /* Counts for each bin in timing histogram */
        unsigned long   counts[CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS];

        /* Bounds for the bins in timing histogram,
         * excluding the first and last (hence, NUM_SLOTS - 1).
         */
        unsigned long   bounds[CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS];
#endif /* CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM */
};

#ifdef __cplusplus
extern "C" {
#endif

int k_mem_page_out(void *addr, size_t size);

void k_mem_page_in(void *addr, size_t size);

void k_mem_pin(void *addr, size_t size);

void k_mem_unpin(void *addr, size_t size);

__syscall void k_mem_paging_stats_get(struct k_mem_paging_stats_t *stats);

struct k_thread;
__syscall
void k_mem_paging_thread_stats_get(struct k_thread *thread,
                                   struct k_mem_paging_stats_t *stats);

__syscall void k_mem_paging_histogram_eviction_get(
        struct k_mem_paging_histogram_t *hist);

__syscall void k_mem_paging_histogram_backing_store_page_in_get(
        struct k_mem_paging_histogram_t *hist);

__syscall void k_mem_paging_histogram_backing_store_page_out_get(
        struct k_mem_paging_histogram_t *hist);

#include <zephyr/syscalls/demand_paging.h>



#if defined(CONFIG_EVICTION_TRACKING) || defined(__DOXYGEN__)

void k_mem_paging_eviction_add(struct k_mem_page_frame *pf);

void k_mem_paging_eviction_remove(struct k_mem_page_frame *pf);

void k_mem_paging_eviction_accessed(uintptr_t phys);

#else /* CONFIG_EVICTION_TRACKING || __DOXYGEN__ */

static inline void k_mem_paging_eviction_add(struct k_mem_page_frame *pf)
{
        ARG_UNUSED(pf);
}

static inline void k_mem_paging_eviction_remove(struct k_mem_page_frame *pf)
{
        ARG_UNUSED(pf);
}

static inline void k_mem_paging_eviction_accessed(uintptr_t phys)
{
        ARG_UNUSED(phys);
}

#endif /* CONFIG_EVICTION_TRACKING || __DOXYGEN__ */

struct k_mem_page_frame *k_mem_paging_eviction_select(bool *dirty);

void k_mem_paging_eviction_init(void);



int k_mem_paging_backing_store_location_get(struct k_mem_page_frame *pf,
                                            uintptr_t *location,
                                            bool page_fault);

void k_mem_paging_backing_store_location_free(uintptr_t location);

int k_mem_paging_backing_store_location_query(void *addr, uintptr_t *location);

void k_mem_paging_backing_store_page_out(uintptr_t location);

void k_mem_paging_backing_store_page_in(uintptr_t location);

void k_mem_paging_backing_store_page_finalize(struct k_mem_page_frame *pf,
                                              uintptr_t location);

void k_mem_paging_backing_store_init(void);


#ifdef __cplusplus
}
#endif

#endif /* !_ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_KERNEL_MM_DEMAND_PAGING_H */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

条件编译（Conditional Compilation）：`!CONFIG_DEMAND_PAGING_ALLOW_IRQ`。

### 注释 3：原第 62 行

条件编译配置（Configuration）标记：`CONFIG_DEMAND_PAGING_STATS`。

### 注释 4：原第 70 行

时序直方图（Timing Histogram）各分箱（Bins）的计数（Counts）。

### 注释 5：原第 73 行

时序直方图（Timing Histogram）的分箱边界（Bin Bounds），不包括第一个和最后一个边界，因此数量为 `NUM_SLOTS - 1`。

### 注释 6：原第 77 行

条件编译配置（Configuration）标记：`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM`。

### 注释 7：原第 266 行

条件编译（Conditional Compilation）：`CONFIG_EVICTION_TRACKING || __DOXYGEN__`。

### 注释 8：原第 283 行

条件编译（Conditional Compilation）：`CONFIG_EVICTION_TRACKING || __DOXYGEN__`。

### 注释 9：原第 459 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 10：原第 460 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KERNEL_MM_DEMAND_PAGING_H`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h.html)
- [zephyr/kernel/mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [inttypes.h](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md)
- [k_mem_paging_stats_t](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md)
- [cnt](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a3daad63e37d200f44d88c3d4e49f361a)
- [irq_locked](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#aa762731df50fc81d08beb3628f9dbd71)
- [irq_unlocked](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a2c2183c1679ae158bdd232fa1fdeb250)
- [in_isr](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a210c83357c14a06fbd69b0cf2263fbb6)
- [pagefaults](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#af6331dae30074d48396151b33ac7a0a7)
- [clean](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a7b421897b3125d1a44284ca964ef1f66)
- [dirty](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a4f8523c0e78c8de1e2443a194e875609)
- [eviction](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#aa8175953fd7fa0a5057069b73b930f3b)
- [k_mem_paging_histogram_t](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md)
- [counts](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md#a4421676cbc9f6c63808ee914e2ff8c90)
- [bounds](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md#a893236502aeb56975263b27cf4f2755a)
- [k_mem_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga0b18037209b4d8b5964bd9a1d760f703)
- [k_mem_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gab36c36a4e230677d2090514f7a34b408)
- [k_mem_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga5f2d422edde7d366e81a870ce057589f)
- [k_mem_unpin](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga3278aae5e24733c722b7d83c4b17dab3)
- [k_mem_paging_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga52ad88e0c0eed2aa27331bfd4707b7ec)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_mem_paging_thread_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gafad6b39cb2faf3bb416cd4d3faaa8d8c)
- [k_mem_paging_histogram_eviction_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gaec64d019d819b00c7bc3804aac269199)
- [k_mem_paging_histogram_backing_store_page_in_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#ga1da0a643e8f85f98e29288e441a37dfa)
- [k_mem_paging_histogram_backing_store_page_out_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging.html#gae4f80d14f88a46ddb9aeb7afba861864)
- [k_mem_paging_eviction_add](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html#ga6bb19be3098cc839ae3f6e9528598867)
- [k_mem_paging_eviction_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html#ga16a4df904cc7a9641d06741ed589949d)
- [k_mem_paging_eviction_accessed](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html#ga228747c10bfd8816aec59fddf0e3a224)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [k_mem_paging_eviction_select](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html#gaadbb4eb56c239f800daf995e6673ae1d)
- [k_mem_paging_eviction_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-eviction.html#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)
- [k_mem_paging_backing_store_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga1192487fdc8d63c025de42162fb204cd)
- [k_mem_paging_backing_store_location_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga6ad421ad5671d9df3d96e03361f672e8)
- [k_mem_paging_backing_store_location_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga25debe925b369765ecd5bd7777ce32d0)
- [k_mem_paging_backing_store_page_out](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga51f663e0a8c31367082e78097359af6d)
- [k_mem_paging_backing_store_page_in](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga9becb4908cc7840ece93a2360692962d)
- [k_mem_paging_backing_store_page_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga8d4bd3ea311fd873413d0477e8deb464)
- [k_mem_paging_backing_store_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mem-demand-paging-backing-store.html#ga7ff441f23619b2678bfb72559d5bd592)
- [mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)
- [k_mem_paging_histogram_t::counts](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md#a4421676cbc9f6c63808ee914e2ff8c90)
- [k_mem_paging_histogram_t::bounds](../kernel_runtime_model_reference/P003_k_mem_paging_histogram_t_结构体.md#a893236502aeb56975263b27cf4f2755a)
- [k_mem_paging_stats_t::in_isr](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a210c83357c14a06fbd69b0cf2263fbb6)
- [k_mem_paging_stats_t::irq_unlocked](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a2c2183c1679ae158bdd232fa1fdeb250)
- [k_mem_paging_stats_t::cnt](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a3daad63e37d200f44d88c3d4e49f361a)
- [k_mem_paging_stats_t::dirty](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a4f8523c0e78c8de1e2443a194e875609)
- [k_mem_paging_stats_t::clean](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#a7b421897b3125d1a44284ca964ef1f66)
- [k_mem_paging_stats_t::irq_locked](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#aa762731df50fc81d08beb3628f9dbd71)
- [k_mem_paging_stats_t::eviction](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#aa8175953fd7fa0a5057069b73b930f3b)
- [k_mem_paging_stats_t::pagefaults](../kernel_runtime_model_reference/P004_k_mem_paging_stats_t_结构体.md#af6331dae30074d48396151b33ac7a0a7)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P005_color_dither.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_bluetooth.h_源码浏览.md)
