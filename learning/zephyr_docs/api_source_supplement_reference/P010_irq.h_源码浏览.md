---
id: learning.zephyr-docs.api-source-supplement-reference.page-10
title: irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h.html)。

## 10.1\_原始可见代码（Source Code）

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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="agroup__arch-irq_html_ga216d692e87bfba955a60f8e570e127df"></a>
<a id="agroup__arch-irq_html_ga3bd8e963a124421bb372dab4bdc6cd83"></a>
<a id="agroup__arch-irq_html_gaa278d630653b33cb339621d725ed295a"></a>
<a id="airq_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="asw__isr__table_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ARCH_TRICORE_IRQ_H_
#define ZEPHYR_INCLUDE_ARCH_TRICORE_IRQ_H_

#ifdef __cplusplus
extern "C" {
#endif
#include <zephyr/sys/util.h>


#define IRQ_USE_TOS BIT(1)
#define IRQ_TOS     GENMASK(31, 28)

#ifndef _ASMLANGUAGE
#include <zephyr/irq.h>
#include <zephyr/sw_isr_table.h>

extern void arch_irq_enable(unsigned int irq);
extern void arch_irq_disable(unsigned int irq);
extern int arch_irq_is_enabled(unsigned int irq);

extern void z_tricore_irq_config(unsigned int irq, unsigned int prio, unsigned int flags);

#define ARCH_IRQ_CONNECT(irq_p, priority_p, isr_p, isr_param_p, flags_p)                           \
        {                                                                                          \
                Z_ISR_DECLARE(irq_p, 0, isr_p, isr_param_p);                                       \
                z_tricore_irq_config(irq_p, priority_p, flags_p);                                  \
        }
#endif /* _ASMLANGUAGE */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_TRICORE_IRQ_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 3：原第 50 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_TRICORE_IRQ_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2irq_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)
- [zephyr/sw_isr_table.h](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html)
- [arch_irq_enable](../fatal_irq_reference/P008_架构中断接口.md#gaa278d630653b33cb339621d725ed295a)
- [arch_irq_disable](../fatal_irq_reference/P008_架构中断接口.md#ga216d692e87bfba955a60f8e570e127df)
- [arch_irq_is_enabled](../fatal_irq_reference/P008_架构中断接口.md#ga3bd8e963a124421bb372dab4bdc6cd83)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)
- [sw_isr_table.h](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P009_cpu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_syscall.h_源码浏览.md)
