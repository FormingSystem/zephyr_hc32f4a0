---
id: learning.zephyr-docs.api-file-service-interface-reference.page-31
title: ____w__zephyr__zephyr__kernel__include__kernel_arch_interface.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_kernel\_\_include\_\_kernel\_arch\_interface.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kernel__arch__interface_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

在架构层实现的内部内核API（Internal Kernel APIs）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/arch/arch_interface.h>
#include <kernel_arch_func.h>
```

查看此文件的源码。

在体系结构层（Architecture Layer）实现的内部内核 API。此处并未包含所有体系结构专用定义；供公共函数和宏使用的 API 定义在 `include/zephyr/arch/arch_interface.h` 中。此处声明原型的所有内联函数（Inline Functions），预期由 `arch/ARCH/include/kernel_arch_func.h` 提供实现。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="r_ga38cfc7602d259972cdd0b557ab26c2b4"></a>

```c
#define ARCH_DATA_PAGE_ACCESSED
```

相关声明：[ARCH_DATA_PAGE_ACCESSED](../arch_core_reference/P003_架构内存映射接口.md#ga38cfc7602d259972cdd0b557ab26c2b4)。

表示自上次清除此值以来，数据页曾被访问的位（Accessed Bit）。

<a id="r_ga4a60b63f47f88db455d67c33ef7bb85d"></a>

```c
#define ARCH_DATA_PAGE_DIRTY
```

相关声明：[ARCH_DATA_PAGE_DIRTY](../arch_core_reference/P003_架构内存映射接口.md#ga4a60b63f47f88db455d67c33ef7bb85d)。

表示数据页若被逐出，则需要换出的位。

<a id="r_gae76ce742aca8b4ac12907a2bfce98b0e"></a>

```c
#define ARCH_DATA_PAGE_LOADED
```

相关声明：[ARCH_DATA_PAGE_LOADED](../arch_core_reference/P003_架构内存映射接口.md#gae76ce742aca8b4ac12907a2bfce98b0e)。

表示数据页已装入物理页框（Physical Page Frame）的位。

<a id="r_ga843c53394b00d80b1649a6224557a56a"></a>

```c
#define ARCH_DATA_PAGE_NOT_MAPPED
```

相关声明：[ARCH_DATA_PAGE_NOT_MAPPED](../arch_core_reference/P003_架构内存映射接口.md#ga843c53394b00d80b1649a6224557a56a)。

当 `ARCH_DATA_PAGE_LOADED` 未置位时，此位表示该页完全没有映射。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.2\_枚举（Enumerations）

<a id="r_ga65e10c80055d7e695add000f2ccfbb0b"></a>

```c
enum arch_page_location { ARCH_PAGE_LOCATION_PAGED_OUT , ARCH_PAGE_LOCATION_PAGED_IN , ARCH_PAGE_LOCATION_BAD }
```

相关声明：[arch_page_location](../arch_core_reference/P003_架构内存映射接口.md#ga65e10c80055d7e695add000f2ccfbb0b)、[ARCH_PAGE_LOCATION_PAGED_OUT](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a)、[ARCH_PAGE_LOCATION_PAGED_IN](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db)、[ARCH_PAGE_LOCATION_BAD](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)。

某个页面位置的状态（Page Location Status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 31.3\_函数（Functions）

<a id="r_gaffc9f3013d53e72c25243ce4f972549f"></a>

```c
void arch_busy_wait (uint32_t usec_to_wait)
```

相关声明：[arch_busy_wait](../timing_reference/P009_架构计数周期接口.md#gaffc9f3013d53e72c25243ce4f972549f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

架构专有的忙等待（Busy-waiting）实现。

<a id="r_gade449838e445fa8201266e38215c616c"></a>

```c
void arch_new_thread (struct k_thread *thread, k_thread_stack_t *stack, char *stack_ptr, k_thread_entry_t entry, void *p1, void *p2, void *p3)
```

相关声明：[arch_new_thread](../thread_stack_reference/P004_架构线程接口.md#gade449838e445fa8201266e38215c616c)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)。

处理建立新线程时架构专有的逻辑。

<a id="r_gab411d82ce5b60f062171f5a19e33e025"></a>

```c
static void arch_switch (void *switch_to, void **switched_from)
```

相关声明：[arch_switch](../thread_stack_reference/P004_架构线程接口.md#gab411d82ce5b60f062171f5a19e33e025)。

协作式上下文切换原语（Cooperative Context Switch Primitive）。

<a id="r_ga05c03d97386bc973a403102f4c048444"></a>

```c
int arch_swap (unsigned int key)
```

相关声明：[arch_swap](../thread_stack_reference/P004_架构线程接口.md#ga05c03d97386bc973a403102f4c048444)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

以协作方式切换上下文。

<a id="r_ga61b6981d7dd768fa01922c6c6ab9780f"></a>

```c
static ALWAYS_INLINE void arch_thread_return_value_set (struct k_thread *thread, unsigned int value)
```

相关声明：[arch_thread_return_value_set](../thread_stack_reference/P004_架构线程接口.md#ga61b6981d7dd768fa01922c6c6ab9780f)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置指定线程的返回值。

<a id="r_ga3ddd51635018a2e0235d5599401f5269"></a>

```c
void arch_switch_to_main_thread (struct k_thread *main_thread, char *stack_ptr, k_thread_entry_t _main)
```

相关声明：[arch_switch_to_main_thread](../thread_stack_reference/P004_架构线程接口.md#ga3ddd51635018a2e0235d5599401f5269)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)。

在早期启动阶段进入主线程上下文的自定义逻辑。

<a id="r_ga84a679d2699d0abf2dec31134857c47a"></a>

```c
void arch_ipi_lazy_coprocessors_save (void)
```

相关声明：[arch_ipi_lazy_coprocessors_save](../thread_stack_reference/P004_架构线程接口.md#ga84a679d2699d0abf2dec31134857c47a)。

在处理器间中断（Inter-processor Interrupt，IPI）中保存协处理器状态。

<a id="r_ga7c2f0ee0bee6f9de0bd23a0aa321a46d"></a>

```c
int arch_float_disable (struct k_thread *thread)
```

相关声明：[arch_float_disable](../thread_stack_reference/P004_架构线程接口.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

禁用浮点上下文保存（Floating-point Context Preservation）。

<a id="r_gacd40e26783f3dbd8a658fc1af512fb18"></a>

```c
int arch_float_enable (struct k_thread *thread, unsigned int options)
```

相关声明：[arch_float_enable](../thread_stack_reference/P004_架构线程接口.md#gacd40e26783f3dbd8a658fc1af512fb18)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用浮点上下文保存。

<a id="r_gad27c008111ce88ed1b2064a26a45ba80"></a>

```c
int arch_coprocessors_disable (struct k_thread *thread)
```

相关声明：[arch_coprocessors_disable](../thread_stack_reference/P004_架构线程接口.md#gad27c008111ce88ed1b2064a26a45ba80)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

禁用协处理器上下文保存（Coprocessor Context Preservation）。

<a id="r_gada83bf3beb5004a39a1f9c8c7ce35348"></a>

```c
FUNC_NORETURN void arch_system_halt (unsigned int reason)
```

相关声明：[arch_system_halt](../arch_core_reference/P006_架构电源管理接口.md#gada83bf3beb5004a39a1f9c8c7ce35348)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

停止系统（Halt），可选择传递原因代码。

<a id="r_ga1dda03646da3989f08a3bad1b258c691"></a>

```c
static bool arch_is_in_isr (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_is_in_isr](../fatal_irq_reference/P008_架构中断接口.md#ga1dda03646da3989f08a3bad1b258c691)。

判断当前上下文是否为中断上下文（Interrupt Context）。

<a id="r_gab716b971ebbc382e397b6a464d534e69"></a>

```c
int arch_mem_map (void *virt, uintptr_t phys, size_t size, uint32_t flags)
```

相关声明：[arch_mem_map](../arch_core_reference/P003_架构内存映射接口.md#gab716b971ebbc382e397b6a464d534e69)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将物理内存映射到虚拟地址空间（Virtual Address Space）。

<a id="r_gad78289a6d8810c30c7fa3052bcac9c23"></a>

```c
int arch_mem_unmap (void *addr, size_t size)
```

相关声明：[arch_mem_unmap](../arch_core_reference/P003_架构内存映射接口.md#gad78289a6d8810c30c7fa3052bcac9c23)。

移除指定虚拟地址范围的映射。

<a id="r_ga229fa5699ad47951235af494f3d2a06a"></a>

```c
void arch_reserved_pages_update (void)
```

相关声明：[arch_reserved_pages_update](../arch_core_reference/P003_架构内存映射接口.md#ga229fa5699ad47951235af494f3d2a06a)。

使用保留页信息更新页框数据库（Page Frame Database）。

<a id="r_ga4c13ffab5b5a5f8c93971c4d3b51bd8f"></a>

```c
void arch_mem_page_out (void *addr, uintptr_t location)
```

相关声明：[arch_mem_page_out](../arch_core_reference/P003_架构内存映射接口.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为换出的数据页更新所有页表（Page Tables）。

<a id="r_ga3c446aea862e37d479a809582322b3ae"></a>

```c
void arch_mem_page_in (void *addr, uintptr_t phys)
```

相关声明：[arch_mem_page_in](../arch_core_reference/P003_架构内存映射接口.md#ga3c446aea862e37d479a809582322b3ae)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为换入的数据页更新所有页表。

<a id="r_gae4e82c3100b08bdfdcd9361d316735a1"></a>

```c
void arch_mem_scratch (uintptr_t phys)
```

相关声明：[arch_mem_scratch](../arch_core_reference/P003_架构内存映射接口.md#gae4e82c3100b08bdfdcd9361d316735a1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为临时映射更新当前页表。

<a id="r_ga74b3ce1173b91a8f82c25ef89f9fbbc0"></a>

```c
enum arch_page_location arch_page_location_get (void *addr, uintptr_t *location)
```

相关声明：[arch_page_location](../arch_core_reference/P003_架构内存映射接口.md#ga65e10c80055d7e695add000f2ccfbb0b)、[arch_page_location_get](../arch_core_reference/P003_架构内存映射接口.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

取得指定地址处页面的位置信息。

<a id="r_gab32a4bb6b3d44c126d63a473caf28b70"></a>

```c
uintptr_t arch_page_info_get (void *addr, uintptr_t *location, bool clear_accessed)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_page_info_get](../arch_core_reference/P003_架构内存映射接口.md#gab32a4bb6b3d44c126d63a473caf28b70)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从页表取得页面特征。

<a id="r_ga6860efc93b8ba35911cfb0afbe372623"></a>

```c
int arch_printk_char_out (int c)
```

相关声明：[arch_printk_char_out](../arch_core_reference/P008_架构杂项接口.md#ga6860efc93b8ba35911cfb0afbe372623)。

早期启动控制台输出钩子（Early Boot Console Output Hook）。

<a id="r_ga62cc65268b396d2683e47c09c9b62af5"></a>

```c
static void arch_kernel_init (void)
```

相关声明：[arch_kernel_init](../arch_core_reference/P008_架构杂项接口.md#ga62cc65268b396d2683e47c09c9b62af5)。

架构专有内核初始化钩子。

<a id="r_gabb087b9e158824121212d65646ae4154"></a>

```c
static void arch_nop (void)
```

相关声明：[arch_nop](../arch_core_reference/P008_架构杂项接口.md#gabb087b9e158824121212d65646ae4154)。

不做任何操作并返回。

<a id="r_gae997cb3dc249bec6d5166145f37d9292"></a>

```c
void arch_coredump_info_dump (const struct arch_esf *esf)
```

相关声明：[arch_coredump_info_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#gae997cb3dc249bec6d5166145f37d9292)。

核心转储（Coredump）期间的体系结构专用处理。

<a id="r_ga1d9b0c011a03434272ff9bec120f273d"></a>

```c
uint16_t arch_coredump_tgt_code_get (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[arch_coredump_tgt_code_get](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga1d9b0c011a03434272ff9bec120f273d)。

获取体系结构指定的目标代码（Target Code）。

<a id="r_gad53d55d1e9bf8c15137e204bc05d2732"></a>

```c
uintptr_t arch_coredump_stack_ptr_get (const struct k_thread *thread)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_coredump_stack_ptr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#gad53d55d1e9bf8c15137e204bc05d2732)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

获取线程的栈指针（Stack Pointer）。

<a id="r_ga54e37d442ec14ee803a70bad2b3fe9a1"></a>

```c
void arch_coredump_freeze_other_cpus (void)
```

相关声明：[arch_coredump_freeze_other_cpus](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga54e37d442ec14ee803a70bad2b3fe9a1)。

冻结其他所有在线 CPU，并捕获其即时寄存器状态（Live Register State）。

<a id="r_ga62d5f5996b36634ce38bf0544ca50bc2"></a>

```c
void arch_coredump_thaw_other_cpus (void)
```

相关声明：[arch_coredump_thaw_other_cpus](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga62d5f5996b36634ce38bf0544ca50bc2)。

释放被 `arch_coredump_freeze_other_cpus()` 冻结的每个 CPU。

<a id="r_ga65105f6fdebaa751338c0eb218efe541"></a>

```c
void arch_coredump_cpu_snapshot_dump (unsigned int cpu)
```

相关声明：[arch_coredump_cpu_snapshot_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga65105f6fdebaa751338c0eb218efe541)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

输出为指定 CPU 索引捕获的即时寄存器快照（Live Register Snapshot）。

<a id="r_ga31bcb446604666c8f4d05ccfcbc00441"></a>

```c
void arch_coredump_priv_stack_dump (struct k_thread *thread)
```

相关声明：[arch_coredump_priv_stack_dump](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-coredump.html#ga31bcb446604666c8f4d05ccfcbc00441)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

转储特权栈（Privileged Stack）时的体系结构专用处理。

<a id="r_ga7f159caca46063b04cf03a54b39255fc"></a>

```c
size_t arch_tls_stack_setup (struct k_thread *new_thread, char *stack_ptr)
```

相关声明：[arch_tls_stack_setup](../arch_core_reference/P007_架构线程局部存储接口.md#ga7f159caca46063b04cf03a54b39255fc)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

在线程栈中建立架构专有的线程局部存储（Thread-local Storage，TLS）区域。


## 31.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/arch/arch_interface.h](../api_source_supplement_reference/P015_arch_interface.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P012_kernel_arch_interface.h_源码浏览.md)
- [ARCH_DATA_PAGE_ACCESSED](../arch_core_reference/P003_架构内存映射接口.md#ga38cfc7602d259972cdd0b557ab26c2b4)
- [ARCH_DATA_PAGE_DIRTY](../arch_core_reference/P003_架构内存映射接口.md#ga4a60b63f47f88db455d67c33ef7bb85d)
- [ARCH_DATA_PAGE_LOADED](../arch_core_reference/P003_架构内存映射接口.md#gae76ce742aca8b4ac12907a2bfce98b0e)
- [ARCH_DATA_PAGE_NOT_MAPPED](../arch_core_reference/P003_架构内存映射接口.md#ga843c53394b00d80b1649a6224557a56a)
- [arch_page_location](../arch_core_reference/P003_架构内存映射接口.md#ga65e10c80055d7e695add000f2ccfbb0b)
- [ARCH_PAGE_LOCATION_PAGED_OUT](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a)
- [ARCH_PAGE_LOCATION_PAGED_IN](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db)
- [ARCH_PAGE_LOCATION_BAD](../arch_core_reference/P003_架构内存映射接口.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)
- [arch_busy_wait](../timing_reference/P009_架构计数周期接口.md#gaffc9f3013d53e72c25243ce4f972549f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [arch_new_thread](../thread_stack_reference/P004_架构线程接口.md#gade449838e445fa8201266e38215c616c)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [arch_switch](../thread_stack_reference/P004_架构线程接口.md#gab411d82ce5b60f062171f5a19e33e025)
- [arch_swap](../thread_stack_reference/P004_架构线程接口.md#ga05c03d97386bc973a403102f4c048444)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [arch_thread_return_value_set](../thread_stack_reference/P004_架构线程接口.md#ga61b6981d7dd768fa01922c6c6ab9780f)
- [arch_switch_to_main_thread](../thread_stack_reference/P004_架构线程接口.md#ga3ddd51635018a2e0235d5599401f5269)
- [arch_ipi_lazy_coprocessors_save](../thread_stack_reference/P004_架构线程接口.md#ga84a679d2699d0abf2dec31134857c47a)
- [arch_float_disable](../thread_stack_reference/P004_架构线程接口.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)
- [arch_float_enable](../thread_stack_reference/P004_架构线程接口.md#gacd40e26783f3dbd8a658fc1af512fb18)
- [arch_coprocessors_disable](../thread_stack_reference/P004_架构线程接口.md#gad27c008111ce88ed1b2064a26a45ba80)
- [arch_system_halt](../arch_core_reference/P006_架构电源管理接口.md#gada83bf3beb5004a39a1f9c8c7ce35348)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [arch_is_in_isr](../fatal_irq_reference/P008_架构中断接口.md#ga1dda03646da3989f08a3bad1b258c691)
- [arch_mem_map](../arch_core_reference/P003_架构内存映射接口.md#gab716b971ebbc382e397b6a464d534e69)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [arch_mem_unmap](../arch_core_reference/P003_架构内存映射接口.md#gad78289a6d8810c30c7fa3052bcac9c23)
- [arch_reserved_pages_update](../arch_core_reference/P003_架构内存映射接口.md#ga229fa5699ad47951235af494f3d2a06a)
- [arch_mem_page_out](../arch_core_reference/P003_架构内存映射接口.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)
- [arch_mem_page_in](../arch_core_reference/P003_架构内存映射接口.md#ga3c446aea862e37d479a809582322b3ae)
- [arch_mem_scratch](../arch_core_reference/P003_架构内存映射接口.md#gae4e82c3100b08bdfdcd9361d316735a1)
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
- [include/zephyr/arch/arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)

<a id="header-details"></a>

---

[上一章](P030_zephyr__dt-bindings__sensor__ism6hg256x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__dt-bindings__sensor__lis2de12.h_文件参考.md)
