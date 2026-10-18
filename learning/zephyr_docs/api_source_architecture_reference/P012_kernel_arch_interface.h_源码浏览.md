---
id: learning.zephyr-docs.api-source-architecture-reference.page-12
title: kernel_arch_interface.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_kernel\_arch\_interface.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h.html)。

## 12.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00049"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00278"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00296"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="foldopen00447"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00592"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00639"></a>
<a id="l00645"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00745"></a>
<a id="l00751"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="aarch__interface_8h_html"></a>
<a id="aarch__interface_8h_html_a3707e886593b0a8b4995309e4230b717"></a>
<a id="aarch__interface_8h_html_a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>
<a id="agroup__arch-coredump_html_ga1d9b0c011a03434272ff9bec120f273d"></a>
<a id="agroup__arch-coredump_html_ga31bcb446604666c8f4d05ccfcbc00441"></a>
<a id="agroup__arch-coredump_html_ga54e37d442ec14ee803a70bad2b3fe9a1"></a>
<a id="agroup__arch-coredump_html_ga62d5f5996b36634ce38bf0544ca50bc2"></a>
<a id="agroup__arch-coredump_html_ga65105f6fdebaa751338c0eb218efe541"></a>
<a id="agroup__arch-coredump_html_gad53d55d1e9bf8c15137e204bc05d2732"></a>
<a id="agroup__arch-coredump_html_gae997cb3dc249bec6d5166145f37d9292"></a>
<a id="agroup__arch-irq_html_ga1dda03646da3989f08a3bad1b258c691"></a>
<a id="agroup__arch-misc_html_ga62cc65268b396d2683e47c09c9b62af5"></a>
<a id="agroup__arch-misc_html_ga6860efc93b8ba35911cfb0afbe372623"></a>
<a id="agroup__arch-misc_html_gabb087b9e158824121212d65646ae4154"></a>
<a id="agroup__arch-mmu_html_ga229fa5699ad47951235af494f3d2a06a"></a>
<a id="agroup__arch-mmu_html_ga3c446aea862e37d479a809582322b3ae"></a>
<a id="agroup__arch-mmu_html_ga4c13ffab5b5a5f8c93971c4d3b51bd8f"></a>
<a id="agroup__arch-mmu_html_ga65e10c80055d7e695add000f2ccfbb0b"></a>
<a id="agroup__arch-mmu_html_ga74b3ce1173b91a8f82c25ef89f9fbbc0"></a>
<a id="agroup__arch-mmu_html_gab32a4bb6b3d44c126d63a473caf28b70"></a>
<a id="agroup__arch-mmu_html_gab716b971ebbc382e397b6a464d534e69"></a>
<a id="agroup__arch-mmu_html_gad78289a6d8810c30c7fa3052bcac9c23"></a>
<a id="agroup__arch-mmu_html_gae4e82c3100b08bdfdcd9361d316735a1"></a>
<a id="agroup__arch-mmu_html_gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9"></a>
<a id="agroup__arch-mmu_html_gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a"></a>
<a id="agroup__arch-mmu_html_gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db"></a>
<a id="agroup__arch-pm_html_gada83bf3beb5004a39a1f9c8c7ce35348"></a>
<a id="agroup__arch-threads_html_ga05c03d97386bc973a403102f4c048444"></a>
<a id="agroup__arch-threads_html_ga3ddd51635018a2e0235d5599401f5269"></a>
<a id="agroup__arch-threads_html_ga61b6981d7dd768fa01922c6c6ab9780f"></a>
<a id="agroup__arch-threads_html_ga7c2f0ee0bee6f9de0bd23a0aa321a46d"></a>
<a id="agroup__arch-threads_html_ga84a679d2699d0abf2dec31134857c47a"></a>
<a id="agroup__arch-threads_html_gab411d82ce5b60f062171f5a19e33e025"></a>
<a id="agroup__arch-threads_html_gacd40e26783f3dbd8a658fc1af512fb18"></a>
<a id="agroup__arch-threads_html_gad27c008111ce88ed1b2064a26a45ba80"></a>
<a id="agroup__arch-threads_html_gade449838e445fa8201266e38215c616c"></a>
<a id="agroup__arch-timing_html_gaffc9f3013d53e72c25243ce4f972549f"></a>
<a id="agroup__arch-tls_html_ga7f159caca46063b04cf03a54b39255fc"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__thread_html"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_KERNEL_INCLUDE_KERNEL_ARCH_INTERFACE_H_
#define ZEPHYR_KERNEL_INCLUDE_KERNEL_ARCH_INTERFACE_H_

#include <zephyr/kernel.h>
#include <zephyr/arch/arch_interface.h>

#ifndef _ASMLANGUAGE

#ifdef __cplusplus
extern "C" {
#endif

#ifdef CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT
void arch_busy_wait(uint32_t usec_to_wait);
#endif /* CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT */



void arch_new_thread(struct k_thread *thread, k_thread_stack_t *stack,
                     char *stack_ptr, k_thread_entry_t entry,
                     void *p1, void *p2, void *p3);

#ifdef CONFIG_USE_SWITCH
static inline void arch_switch(void *switch_to, void **switched_from);
#endif /* CONFIG_USE_SWITCH */

#if !defined(CONFIG_USE_SWITCH) || defined(__DOXYGEN__)
#if defined(__DOXYGEN__)
int arch_swap(unsigned int key);
#endif /* __DOXYGEN__ */

static ALWAYS_INLINE void
arch_thread_return_value_set(struct k_thread *thread, unsigned int value);
#endif /* !CONFIG_USE_SWITCH || __DOXYGEN__ */

#ifdef CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN
void arch_switch_to_main_thread(struct k_thread *main_thread, char *stack_ptr,
                                k_thread_entry_t _main);
#endif /* CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN */

void arch_ipi_lazy_coprocessors_save(void);

#if defined(CONFIG_FPU) && defined(CONFIG_FPU_SHARING)
int arch_float_disable(struct k_thread *thread);

int arch_float_enable(struct k_thread *thread, unsigned int options);
#endif /* CONFIG_FPU && CONFIG_FPU_SHARING */

int arch_coprocessors_disable(struct k_thread *thread);

#if defined(CONFIG_USERSPACE) && defined(CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET)
int arch_thread_priv_stack_space_get(const struct k_thread *thread, size_t *stack_size,
                                     size_t *unused_ptr);
#endif /* CONFIG_USERSPACE && CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET */


FUNC_NORETURN void arch_system_halt(unsigned int reason);




static inline bool arch_is_in_isr(void);



int arch_mem_map(void *virt, uintptr_t phys, size_t size, uint32_t flags);

int arch_mem_unmap(void *addr, size_t size);

void arch_reserved_pages_update(void);

void arch_mem_page_out(void *addr, uintptr_t location);

void arch_mem_page_in(void *addr, uintptr_t phys);

void arch_mem_scratch(uintptr_t phys);

enum arch_page_location {
        ARCH_PAGE_LOCATION_PAGED_OUT,

        ARCH_PAGE_LOCATION_PAGED_IN,

        ARCH_PAGE_LOCATION_BAD
};

enum arch_page_location arch_page_location_get(void *addr, uintptr_t *location);

#ifdef __DOXYGEN__
#define ARCH_DATA_PAGE_ACCESSED
#endif

#ifdef __DOXYGEN__
#define ARCH_DATA_PAGE_DIRTY
#endif

#ifdef __DOXYGEN__
#define ARCH_DATA_PAGE_LOADED
#endif

#ifdef __DOXYGEN__
#define ARCH_DATA_PAGE_NOT_MAPPED
#endif

uintptr_t arch_page_info_get(void *addr, uintptr_t *location,
                             bool clear_accessed);



int arch_printk_char_out(int c);

#ifdef CONFIG_ARCH_HAS_THREAD_NAME_HOOK
int arch_thread_name_set(struct k_thread *thread, const char *str);
#endif /* CONFIG_ARCH_HAS_THREAD_NAME_HOOK */

static inline void arch_kernel_init(void);

static inline void arch_nop(void);



void arch_coredump_info_dump(const struct arch_esf *esf);

uint16_t arch_coredump_tgt_code_get(void);

uintptr_t arch_coredump_stack_ptr_get(const struct k_thread *thread);

#if defined(CONFIG_DEBUG_COREDUMP_SMP_FREEZE_CPUS) || defined(__DOXYGEN__)

void arch_coredump_freeze_other_cpus(void);

void arch_coredump_thaw_other_cpus(void);

void arch_coredump_cpu_snapshot_dump(unsigned int cpu);

#endif /* CONFIG_DEBUG_COREDUMP_SMP_FREEZE_CPUS */

#if defined(CONFIG_USERSPACE) || defined(__DOXYGEN__)

void arch_coredump_priv_stack_dump(struct k_thread *thread);

#endif /* CONFIG_USERSPACE || __DOXYGEN__ */

#ifdef CONFIG_DEBUG_COREDUMP_FATAL_UNLOCK_IRQS

void arch_coredump_fatal_irq_unlock(unsigned int key, void *cookie);

unsigned int arch_coredump_fatal_irq_lock(void *cookie);

#endif /* CONFIG_DEBUG_COREDUMP_FATAL_UNLOCK_IRQS */



size_t arch_tls_stack_setup(struct k_thread *new_thread, char *stack_ptr);


/* Include arch-specific inline function implementation */
#include <kernel_arch_func.h>

#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_KERNEL_INCLUDE_KERNEL_ARCH_INTERFACE_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`。

### 注释 3：原第 132 行

条件编译配置（Configuration）标记：`CONFIG_USE_SWITCH`。

### 注释 4：原第 149 行

文档生成条件标识（Documentation Generation Identifier）：`__DOXYGEN__`。

### 注释 5：原第 161 行

条件编译（Conditional Compilation）：`!CONFIG_USE_SWITCH || __DOXYGEN__`。

### 注释 6：原第 176 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN`。

### 注释 7：原第 222 行

条件编译（Conditional Compilation）：`CONFIG_FPU && CONFIG_FPU_SHARING`。

### 注释 8：原第 258 行

条件编译（Conditional Compilation）：`CONFIG_USERSPACE && CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`。

### 注释 9：原第 625 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_HAS_THREAD_NAME_HOOK`。

### 注释 10：原第 696 行

条件编译配置（Configuration）标记：`CONFIG_DEBUG_COREDUMP_SMP_FREEZE_CPUS`。

### 注释 11：原第 709 行

条件编译（Conditional Compilation）：`CONFIG_USERSPACE || __DOXYGEN__`。

### 注释 12：原第 742 行

条件编译配置（Configuration）标记：`CONFIG_DEBUG_COREDUMP_FATAL_UNLOCK_IRQS`。

### 注释 13：原第 766 行

包含架构专用内联函数实现（Architecture-Specific Inline Function Implementation）。

### 注释 14：原第 773 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 15：原第 775 行

头文件保护宏（Header guard）标记：`ZEPHYR_KERNEL_INCLUDE_KERNEL_ARCH_INTERFACE_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/arch/arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [arch_busy_wait](../timing_reference/P009_架构计数周期接口.md#gaffc9f3013d53e72c25243ce4f972549f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [arch_new_thread](../thread_stack_reference/P004_架构线程接口.md#gade449838e445fa8201266e38215c616c)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [arch_switch](../thread_stack_reference/P004_架构线程接口.md#gab411d82ce5b60f062171f5a19e33e025)
- [arch_swap](../thread_stack_reference/P004_架构线程接口.md#ga05c03d97386bc973a403102f4c048444)
- [arch_thread_return_value_set](../thread_stack_reference/P004_架构线程接口.md#ga61b6981d7dd768fa01922c6c6ab9780f)
- [arch_switch_to_main_thread](../thread_stack_reference/P004_架构线程接口.md#ga3ddd51635018a2e0235d5599401f5269)
- [arch_ipi_lazy_coprocessors_save](../thread_stack_reference/P004_架构线程接口.md#ga84a679d2699d0abf2dec31134857c47a)
- [arch_float_disable](../thread_stack_reference/P004_架构线程接口.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)
- [arch_float_enable](../thread_stack_reference/P004_架构线程接口.md#gacd40e26783f3dbd8a658fc1af512fb18)
- [arch_coprocessors_disable](../thread_stack_reference/P004_架构线程接口.md#gad27c008111ce88ed1b2064a26a45ba80)
- [arch_system_halt](../arch_core_reference/P006_架构电源管理接口.md#gada83bf3beb5004a39a1f9c8c7ce35348)
- [arch_is_in_isr](../fatal_irq_reference/P008_架构中断接口.md#ga1dda03646da3989f08a3bad1b258c691)
- [arch_mem_map](../arch_core_reference/P003_架构内存映射接口.md#gab716b971ebbc382e397b6a464d534e69)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [arch_mem_unmap](../arch_core_reference/P003_架构内存映射接口.md#gad78289a6d8810c30c7fa3052bcac9c23)
- [arch_reserved_pages_update](../arch_core_reference/P003_架构内存映射接口.md#ga229fa5699ad47951235af494f3d2a06a)
- [arch_mem_page_out](../arch_core_reference/P003_架构内存映射接口.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)
- [arch_mem_page_in](../arch_core_reference/P003_架构内存映射接口.md#ga3c446aea862e37d479a809582322b3ae)
- [arch_mem_scratch](../arch_core_reference/P003_架构内存映射接口.md#gae4e82c3100b08bdfdcd9361d316735a1)
- [arch_page_location](../arch_core_reference/P003_架构内存映射接口.md#ga65e10c80055d7e695add000f2ccfbb0b)
- [ARCH_PAGE_LOCATION_PAGED_OUT](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a)
- [ARCH_PAGE_LOCATION_PAGED_IN](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db)
- [ARCH_PAGE_LOCATION_BAD](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)
- [arch_page_location_get](../arch_core_reference/P003_架构内存映射接口.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)
- [arch_page_info_get](../arch_core_reference/P003_架构内存映射接口.md#gab32a4bb6b3d44c126d63a473caf28b70)
- [arch_printk_char_out](../arch_core_reference/P008_架构杂项接口.md#ga6860efc93b8ba35911cfb0afbe372623)
- [arch_kernel_init](../arch_core_reference/P008_架构杂项接口.md#ga62cc65268b396d2683e47c09c9b62af5)
- [arch_nop](../arch_core_reference/P008_架构杂项接口.md#gabb087b9e158824121212d65646ae4154)
- [arch_coredump_info_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#gae997cb3dc249bec6d5166145f37d9292)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [arch_coredump_tgt_code_get](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga1d9b0c011a03434272ff9bec120f273d)
- [arch_coredump_stack_ptr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#gad53d55d1e9bf8c15137e204bc05d2732)
- [arch_coredump_freeze_other_cpus](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga54e37d442ec14ee803a70bad2b3fe9a1)
- [arch_coredump_thaw_other_cpus](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga62d5f5996b36634ce38bf0544ca50bc2)
- [arch_coredump_cpu_snapshot_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga65105f6fdebaa751338c0eb218efe541)
- [arch_coredump_priv_stack_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga31bcb446604666c8f4d05ccfcbc00441)
- [arch_tls_stack_setup](../arch_core_reference/P007_架构线程局部存储接口.md#ga7f159caca46063b04cf03a54b39255fc)
- [arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P011_mm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_kinetis_pcc.h_源码浏览.md)
