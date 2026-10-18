---
id: learning.zephyr-docs.api-source-supplement-reference.page-13
title: arch.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_arch.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html)。

## 13.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
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
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="aarch_2common_2sys__io_8h_html"></a>
<a id="aarch_2tricore_2irq_8h_html"></a>
<a id="aarch_2tricore_2thread_8h_html"></a>
<a id="acr_8h_html"></a>
<a id="affs_8h_html"></a>
<a id="agroup__arch-irq_html_ga1b827afafc622d412962f568b78726dc"></a>
<a id="agroup__arch-irq_html_ga25bca3069cb999b6d4f924b87bf7de38"></a>
<a id="agroup__arch-irq_html_gaa2b2745d8e99b8730b44805f4d3bbf05"></a>
<a id="agroup__arch-irq_html_gab7c91d90ed8ccfce15c8bd040496f9ac"></a>
<a id="agroup__arch-misc_html_gabb087b9e158824121212d65646ae4154"></a>
<a id="agroup__arch-timing_html_ga9ee9f897ec750957de45bf8d43349d5e"></a>
<a id="agroup__arch-timing_html_gacc1ed8d949f694a1d39e389334caf971"></a>
<a id="agroup__clock__apis_html_ga25328a181bd0229ef5110c15e8452fc1"></a>
<a id="agroup__clock__apis_html_ga42dcd1878309a82246dbfa26510f868a"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ainclude_2zephyr_2arch_2tricore_2error_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="asys_2util_8h_html"></a>
<a id="asys__bitops_8h_html"></a>
<a id="atricore_2exception_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_H_
#define ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_H_

#include <zephyr/arch/tricore/thread.h>
#include <zephyr/arch/tricore/exception.h>
#include <zephyr/arch/tricore/error.h>
#include <zephyr/arch/tricore/irq.h>
#include <zephyr/arch/tricore/cr.h>

#include <zephyr/arch/common/sys_io.h>
#include <zephyr/arch/common/sys_bitops.h>
#include <zephyr/arch/common/ffs.h>

#define ARCH_STACK_PTR_ALIGN 8

#ifndef _ASMLANGUAGE
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif


static ALWAYS_INLINE unsigned int arch_irq_lock(void)
{
        unsigned int key = cr_read(TRICORE_ICR);

        __asm__ volatile("disable" ::: "memory");

        return key;
}

static ALWAYS_INLINE void arch_irq_unlock(unsigned int key)
{
        if (arch_irq_unlocked(key)) {
                __asm__ volatile("enable" ::: "memory");
        }
}

static ALWAYS_INLINE bool arch_irq_unlocked(unsigned int key)
{
        return !!(key & BIT(15));
}

static inline bool arch_cpu_irqs_are_enabled(void)
{
        return !!(cr_read(TRICORE_ICR) & BIT(15));
}

extern uint32_t sys_clock_cycle_get_32(void);

static inline uint32_t arch_k_cycle_get_32(void)
{
        return sys_clock_cycle_get_32();
}

extern uint64_t sys_clock_cycle_get_64(void);

static inline uint64_t arch_k_cycle_get_64(void)
{
        return sys_clock_cycle_get_64();
}

static ALWAYS_INLINE void arch_nop(void)
{
        __asm__ volatile("nop");
}


#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 95 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 3：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html)
- [zephyr/arch/tricore/thread.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2thread_8h.html)
- [zephyr/arch/tricore/exception.h](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)
- [zephyr/arch/tricore/error.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2arch_2tricore_2error_8h.html)
- [zephyr/arch/tricore/irq.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h.html)
- [zephyr/arch/tricore/cr.h](https://docs.zephyrproject.org/latest/doxygen/html/cr_8h.html)
- [zephyr/arch/common/sys_io.h](../device_reference/P023_通用架构IO头文件参考.md)
- [zephyr/arch/common/sys_bitops.h](../device_reference/P025_通用内存位操作头文件参考.md)
- [zephyr/arch/common/ffs.h](../numeric_reference/P006_置位扫描头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [arch_irq_lock](../fatal_irq_reference/P008_架构中断接口.md#ga25bca3069cb999b6d4f924b87bf7de38)
- [arch_irq_unlock](../fatal_irq_reference/P008_架构中断接口.md#gaa2b2745d8e99b8730b44805f4d3bbf05)
- [arch_irq_unlocked](../fatal_irq_reference/P008_架构中断接口.md#ga1b827afafc622d412962f568b78726dc)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [arch_cpu_irqs_are_enabled](../fatal_irq_reference/P008_架构中断接口.md#gab7c91d90ed8ccfce15c8bd040496f9ac)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_clock_cycle_get_32](../timer_reference/P086_系统时钟公共接口.md#ga42dcd1878309a82246dbfa26510f868a)
- [arch_k_cycle_get_32](../timing_reference/P009_架构计数周期接口.md#ga9ee9f897ec750957de45bf8d43349d5e)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [sys_clock_cycle_get_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga25328a181bd0229ef5110c15e8452fc1)
- [arch_k_cycle_get_64](../timing_reference/P009_架构计数周期接口.md#gacc1ed8d949f694a1d39e389334caf971)
- [arch_nop](../arch_core_reference/P008_架构杂项接口.md#gabb087b9e158824121212d65646ae4154)
- [sys_io.h](../device_reference/P023_通用架构IO头文件参考.md)
- [irq.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h.html)
- [thread.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2thread_8h.html)
- [cr.h](https://docs.zephyrproject.org/latest/doxygen/html/cr_8h.html)
- [ffs.h](../numeric_reference/P006_置位扫描头文件参考.md)
- [error.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2arch_2tricore_2error_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [sys_bitops.h](../device_reference/P025_通用内存位操作头文件参考.md)
- [exception.h](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)

---

[上一章](P012_thread.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_arch_inlines.h_源码浏览.md)
