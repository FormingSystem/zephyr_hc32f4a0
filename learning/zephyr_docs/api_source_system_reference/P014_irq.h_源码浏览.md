---
id: learning.zephyr-docs.api-source-system-reference.page-14
title: irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P173_zephyr__irq.h_文件参考.md)。

## 14.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00032"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00066"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00091"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="foldopen00365"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00385"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="foldopen00395"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="foldopen00407"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="foldopen00443"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="foldopen00462"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="foldopen00478"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="foldopen00496"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="foldopen00521"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="aarch_2cpu_8h_html"></a>
<a id="agroup__arch-irq_html_ga41483a9fc1090d96d066e107a74ee38c"></a>
<a id="agroup__arch-irq_html_ga6f5e4f7795c23586b13c5f6eaecac54d"></a>
<a id="agroup__arch-irq_html_gaa45f7cc9823e3a3b5f760ffc02323516"></a>
<a id="agroup__arch-irq_html_gaa4d733913e12a12e104dc4781cca7308"></a>
<a id="agroup__arch-irq_html_gaad2c939389164d483a472d4f6d201ce0"></a>
<a id="agroup__arch-irq_html_gae2a76360ce4ddcd461c06602ef16ba32"></a>
<a id="agroup__isr__apis_html_ga19fdde73c3b02fcca6cf1d1e67631228"></a>
<a id="agroup__isr__apis_html_ga1afce7151e12971b53f7f522493b982c"></a>
<a id="agroup__isr__apis_html_ga2835209c4f3809b5d22fc84c1bdce935"></a>
<a id="agroup__isr__apis_html_ga432cfe25e5846d7a0a665043e623d3b6"></a>
<a id="agroup__isr__apis_html_ga4a5a523c81da5c75d25c58d7702b7144"></a>
<a id="agroup__isr__apis_html_ga4e9915b92b09df49b99bc449f0cc31a1"></a>
<a id="agroup__isr__apis_html_ga502c7221c97faad1399465e21880fef1"></a>
<a id="agroup__isr__apis_html_ga646045943b3b2a130738bcc48867bf57"></a>
<a id="agroup__isr__apis_html_ga71fef3867ba9818cf0a5baf8410a6354"></a>
<a id="agroup__isr__apis_html_ga7ea700ee31e4ff036c997a554dbedfeb"></a>
<a id="agroup__isr__apis_html_ga82c3a15d812f58e0f6525f358d031e6d"></a>
<a id="agroup__isr__apis_html_gaa322248445f4914ff2093e7cadff0891"></a>
<a id="agroup__isr__apis_html_gaa62fbe4efebb343ed5ae494c9fcd13cb"></a>
<a id="agroup__isr__apis_html_gaa9f2e3357809d1bb734d0841cb3a9653"></a>
<a id="agroup__isr__apis_html_gabba768c3c87a40641982e4b0654c0d26"></a>
<a id="agroup__isr__apis_html_gabdab7745edc1e15862e1772d8673fc00"></a>
<a id="agroup__isr__apis_html_gad4a27741fdbb40d4a7d1c7cea10eff03"></a>
<a id="agroup__isr__apis_html_gae2f1cb1c6babc98ff59d9e87daccb0c5"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alimits_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2015 Intel corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IRQ_H_
#define ZEPHYR_INCLUDE_IRQ_H_

/* Pull in the arch-specific implementations */
#include <zephyr/arch/cpu.h>

#ifndef _ASMLANGUAGE
#include <limits.h>
#include <stdbool.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif


#define IRQ_CONNECT(irq_p, priority_p, isr_p, isr_param_p, flags_p) \
        ARCH_IRQ_CONNECT(irq_p, priority_p, isr_p, isr_param_p, flags_p)

static inline int
irq_connect_dynamic(unsigned int irq, unsigned int priority,
                    void (*routine)(const void *parameter),
                    const void *parameter, uint32_t flags)
{
        return arch_irq_connect_dynamic(irq, priority, routine, parameter,
                                        flags);
}

static inline int
irq_disconnect_dynamic(unsigned int irq, unsigned int priority,
                       void (*routine)(const void *parameter),
                       const void *parameter, uint32_t flags)
{
        return arch_irq_disconnect_dynamic(irq, priority, routine,
                                           parameter, flags);
}

/*
 * Direct interrupts are optional; only architectures selecting
 * CONFIG_ARCH_HAS_DIRECT_INTERRUPTS define the ARCH_*_DIRECT_* hooks used
 * below. Without these fallbacks the undefined function-like macros survive
 * preprocessing and misparse as K&R function definitions, which reports a
 * missing return type rather than the missing feature.
 *
 * Only the two API entry points are stubbed: the HEADER/FOOTER/PM hooks are
 * reachable solely from inside a direct ISR body, so the assertion on
 * ARCH_ISR_DIRECT_DECLARE() already covers them, and RX defines the
 * HEADER/FOOTER hooks for its internal ISR accounting without supporting
 * direct interrupts, so stubbing those would collide.
 *
 * The guard cannot test the hooks themselves: the arch-level irq.h headers
 * include this file before defining them. Doxygen is kept out so that the
 * documented stubs in arch_interface.h remain the only visible definitions.
 */
#if !defined(CONFIG_ARCH_HAS_DIRECT_INTERRUPTS) && !defined(__DOXYGEN__)

#define Z_ISR_DIRECT_UNSUPPORTED \
        BUILD_ASSERT(0, "direct interrupts are not supported by this architecture")

#define ARCH_IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p) \
        Z_ISR_DIRECT_UNSUPPORTED
#define ARCH_ISR_DIRECT_DECLARE(name) \
        Z_ISR_DIRECT_UNSUPPORTED; \
        int name(void)

#endif /* !CONFIG_ARCH_HAS_DIRECT_INTERRUPTS && !__DOXYGEN__ */

#define IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p) \
        ARCH_IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p)

#define ISR_DIRECT_HEADER() ARCH_ISR_DIRECT_HEADER()

#define ISR_DIRECT_FOOTER(check_reschedule) \
        ARCH_ISR_DIRECT_FOOTER(check_reschedule)

#define ISR_DIRECT_PM() ARCH_ISR_DIRECT_PM()

#define ISR_DIRECT_DECLARE(name) ARCH_ISR_DIRECT_DECLARE(name)

#ifdef CONFIG_SMP
unsigned int z_smp_global_lock(void);
#define irq_lock() z_smp_global_lock()
#else
#define irq_lock() arch_irq_lock()
#endif

#ifdef CONFIG_SMP
void z_smp_global_unlock(unsigned int key);
#define irq_unlock(key) z_smp_global_unlock(key)
#else
#define irq_unlock(key) arch_irq_unlock(key)
#endif

#define irq_enable(irq) arch_irq_enable(irq)

#define irq_disable(irq) arch_irq_disable(irq)

#define irq_is_enabled(irq) arch_irq_is_enabled(irq)

/*
 * Namespaced equivalents of the interrupt APIs above. New code should
 * prefer these. The unprefixed names remain fully supported and must stay
 * function-like macros: vendor HAL headers declare functions with those
 * names, and a macro coexists with such a declaration where a function
 * definition would conflict.
 */

static ALWAYS_INLINE unsigned int k_irq_lock(void)
{
        return irq_lock();
}

static ALWAYS_INLINE void k_irq_unlock(unsigned int key)
{
        irq_unlock(key);
}

static ALWAYS_INLINE void k_irq_enable(unsigned int irq)
{
        irq_enable(irq);
}

static ALWAYS_INLINE void k_irq_disable(unsigned int irq)
{
        irq_disable(irq);
}

static ALWAYS_INLINE int k_irq_is_enabled(unsigned int irq)
{
        return irq_is_enabled(irq);
}

static ALWAYS_INLINE int k_irq_connect_dynamic(unsigned int irq, unsigned int priority,
                                               void (*routine)(const void *parameter),
                                               const void *parameter, uint32_t flags)
{
        return irq_connect_dynamic(irq, priority, routine, parameter, flags);
}

static ALWAYS_INLINE int k_irq_disconnect_dynamic(unsigned int irq, unsigned int priority,
                                                  void (*routine)(const void *parameter),
                                                  const void *parameter, uint32_t flags)
{
        return irq_disconnect_dynamic(irq, priority, routine, parameter, flags);
}

#if defined(CONFIG_ARCH_HAS_IRQ_PENDING_OPS) || defined(__DOXYGEN__)
static ALWAYS_INLINE void k_irq_clear_pending(unsigned int irq)
{
        arch_irq_clear_pending(irq);
}

static ALWAYS_INLINE void k_irq_set_pending(unsigned int irq)
{
        arch_irq_set_pending(irq);
}

static ALWAYS_INLINE bool k_irq_is_pending(unsigned int irq)
{
        return arch_irq_is_pending(irq);
}
#endif /* CONFIG_ARCH_HAS_IRQ_PENDING_OPS */

#if defined(CONFIG_ARCH_HAS_IRQ_GET_ACTIVE) || defined(__DOXYGEN__)
#define K_IRQ_ACTIVE_NONE UINT_MAX

static ALWAYS_INLINE unsigned int k_irq_get_active(void)
{
        return arch_irq_get_active();
}
#endif /* CONFIG_ARCH_HAS_IRQ_GET_ACTIVE */


#ifdef __cplusplus
}
#endif

#endif /* ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_IRQ_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2015 Intel corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

引入架构专用实现（Architecture-Specific Implementations）。

### 注释 3：原第 100 行

直接中断（Direct Interrupts）是可选功能；只有选择 `CONFIG_ARCH_HAS_DIRECT_INTERRUPTS` 的架构，才会定义下文使用的 `ARCH_*_DIRECT_*` 钩子（Hooks）。缺少这些回退定义（Fallbacks）时，未定义的函数式宏（Function-Like Macros）会保留到预处理之后，并被错误地解析为 K&R 函数定义，从而报告缺少返回类型，而不是缺少该功能。

这里只为两个 API 入口点提供桩实现（Stubs）：`HEADER`／`FOOTER`／`PM` 钩子只能从直接中断服务程序（Direct ISR）的函数体内到达，因此 `ARCH_ISR_DIRECT_DECLARE()` 上的断言（Assertion）已经覆盖它们。此外，RX 为内部 ISR 记账定义了 `HEADER`／`FOOTER` 钩子，但不支持直接中断；再为这些钩子提供桩实现会产生冲突。

保护条件（Guard）不能测试钩子本身，因为架构层的 `irq.h` 头文件会先包含本文件，再定义这些钩子。此处排除 Doxygen，使 `arch_interface.h` 中带文档的桩实现成为唯一可见的定义。

### 注释 4：原第 128 行

条件编译（Conditional Compilation）：`!CONFIG_ARCH_HAS_DIRECT_INTERRUPTS && !__DOXYGEN__`。

### 注释 5：原第 352 行

上方中断 API 的带命名空间版本（Namespaced Equivalents）。新代码应优先使用这些名称。不带前缀的名称仍完全受支持，且必须保留为函数式宏（Function-Like Macros）：厂商硬件抽象层（HAL）头文件会声明同名函数，宏可以与这种声明共存，而函数定义会与其冲突。

### 注释 6：原第 500 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_HAS_IRQ_PENDING_OPS`。

### 注释 7：原第 525 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_HAS_IRQ_GET_ACTIVE`。

### 注释 8：原第 535 行

汇编语言条件标识（Assembly Language Conditional Identifier）：`ASMLANGUAGE`。

### 注释 9：原第 536 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_IRQ_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P173_zephyr__irq.h_文件参考.md)
- [zephyr/arch/cpu.h](../api_file_reference/P013_zephyr__arch__cpu.h_文件参考.md)
- [limits.h](../api_file_reference/P189_____w__zephyr__zephyr__lib__libc__minimal__include__limits.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga4e9915b92b09df49b99bc449f0cc31a1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [arch_irq_connect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#gaa4d733913e12a12e104dc4781cca7308)
- [irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gabdab7745edc1e15862e1772d8673fc00)
- [arch_irq_disconnect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#ga41483a9fc1090d96d066e107a74ee38c)
- [k_irq_lock](../fatal_irq_reference/P007_中断服务接口.md#gad4a27741fdbb40d4a7d1c7cea10eff03)
- [irq_lock](../fatal_irq_reference/P007_中断服务接口.md#ga19fdde73c3b02fcca6cf1d1e67631228)
- [k_irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga4a5a523c81da5c75d25c58d7702b7144)
- [irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga646045943b3b2a130738bcc48867bf57)
- [k_irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga502c7221c97faad1399465e21880fef1)
- [irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga7ea700ee31e4ff036c997a554dbedfeb)
- [k_irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga432cfe25e5846d7a0a665043e623d3b6)
- [irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga82c3a15d812f58e0f6525f358d031e6d)
- [k_irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#gabba768c3c87a40641982e4b0654c0d26)
- [irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#ga71fef3867ba9818cf0a5baf8410a6354)
- [k_irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga2835209c4f3809b5d22fc84c1bdce935)
- [k_irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gae2f1cb1c6babc98ff59d9e87daccb0c5)
- [k_irq_clear_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa322248445f4914ff2093e7cadff0891)
- [arch_irq_clear_pending](../fatal_irq_reference/P008_架构中断接口.md#ga6f5e4f7795c23586b13c5f6eaecac54d)
- [k_irq_set_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa9f2e3357809d1bb734d0841cb3a9653)
- [arch_irq_set_pending](../fatal_irq_reference/P008_架构中断接口.md#gaad2c939389164d483a472d4f6d201ce0)
- [k_irq_is_pending](../fatal_irq_reference/P007_中断服务接口.md#ga1afce7151e12971b53f7f522493b982c)
- [arch_irq_is_pending](../fatal_irq_reference/P008_架构中断接口.md#gaa45f7cc9823e3a3b5f760ffc02323516)
- [k_irq_get_active](../fatal_irq_reference/P007_中断服务接口.md#gaa62fbe4efebb343ed5ae494c9fcd13cb)
- [arch_irq_get_active](../fatal_irq_reference/P008_架构中断接口.md#gae2a76360ce4ddcd461c06602ef16ba32)
- [cpu.h](../api_file_reference/P013_zephyr__arch__cpu.h_文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P013_haptics.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_isotp.h_源码浏览.md)
