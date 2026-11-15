---
id: learning.zephyr-docs.api-source-supplement-reference.page-229
title: arch_inlines.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tricore_2arch__inlines_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第229章\_arch\_inlines.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2arch__inlines_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2arch__inlines_8h.html)。

## 229.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="acr_8h_html"></a>
<a id="agroup__arch-smp_html_ga078e9bf1a4a557d1321ddc4848092cbe"></a>
<a id="agroup__arch-smp_html_gad42138d41dff6a4aad8abf7d77fcd8b2"></a>
<a id="agroup__arch-smp_html_gad628c89816128546501e3c26eaaf9dea"></a>
<a id="akernel__structs_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_INLINES_H_
#define ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_INLINES_H_

#include <zephyr/arch/tricore/cr.h>

#ifndef _ASMLANGUAGE

#include <zephyr/kernel_structs.h>


static ALWAYS_INLINE uint32_t arch_proc_id(void)
{
        return 0;
}

static ALWAYS_INLINE _cpu_t *arch_curr_cpu(void)
{
#if defined(CONFIG_SMP)
        return &_kernel.cpus[arch_proc_id()];
#else
        return &_kernel.cpus[0];
#endif
}

static ALWAYS_INLINE unsigned int arch_num_cpus(void)
{
        return CONFIG_MP_MAX_NUM_CPUS;
}


#endif /* !_ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_INLINES_H_ */
```

## 229.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 3：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_TRICORE_ARCH_INLINES_H_`。

## 229.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2arch__inlines_8h.html)
- [zephyr/arch/tricore/cr.h](https://docs.zephyrproject.org/latest/doxygen/html/cr_8h.html)
- [zephyr/kernel_structs.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [arch_proc_id](../arch_core_reference/P005_架构多处理器接口.md#gad628c89816128546501e3c26eaaf9dea)
- [arch_curr_cpu](../arch_core_reference/P005_架构多处理器接口.md#gad42138d41dff6a4aad8abf7d77fcd8b2)
- [arch_num_cpus](../arch_core_reference/P005_架构多处理器接口.md#ga078e9bf1a4a557d1321ddc4848092cbe)
- [cr.h](https://docs.zephyrproject.org/latest/doxygen/html/cr_8h.html)
- [kernel_structs.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html)

---

[上一章](P228_transport_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P230_structs.h_源码浏览.md)
