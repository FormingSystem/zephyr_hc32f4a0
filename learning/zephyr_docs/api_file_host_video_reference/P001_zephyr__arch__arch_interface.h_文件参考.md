---
id: learning.zephyr-docs.api-file-host-video-reference.page-1
title: zephyr__arch__arch_interface.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_arch\_\_arch\_interface.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/arch/cpu.h>
#include <zephyr/irq_offload.h>
#include <zephyr/arch/syscall.h>
#include <zephyr/timing/types.h>
#include <zephyr/arch/arch_inlines.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gace8831316d471ccfb06eeddb6d69d817"></a>

```c
#define ARCH_THREAD_STACK_RESERVED
```

相关声明：[ARCH_THREAD_STACK_RESERVED](../thread_stack_reference/P004_架构线程接口.md#gace8831316d471ccfb06eeddb6d69d817)。

每个线程栈对象起始处的保留空间。

<a id="r_gaf0f8ad93611d93cd0626914837e761d3"></a>

```c
#define ARCH_STACK_PTR_ALIGN
```

相关声明：[ARCH_STACK_PTR_ALIGN](../thread_stack_reference/P004_架构线程接口.md#gaf0f8ad93611d93cd0626914837e761d3)。

CPU 栈指针（Stack Pointer）所需的对齐。

<a id="r_gab6c1d96f5e018ed166ee401dc84b7ab7"></a>

```c
#define ARCH_THREAD_STACK_OBJ_ALIGN(size)
```

相关声明：[ARCH_THREAD_STACK_OBJ_ALIGN](../thread_stack_reference/P004_架构线程接口.md#gab6c1d96f5e018ed166ee401dc84b7ab7)。

栈对象最低地址所需的对齐。

<a id="r_gab76d60bd06e5c5a0f995c6b11bf97fd8"></a>

```c
#define ARCH_THREAD_STACK_SIZE_ADJUST(size)
```

相关声明：[ARCH_THREAD_STACK_SIZE_ADJUST](../thread_stack_reference/P004_架构线程接口.md#gab76d60bd06e5c5a0f995c6b11bf97fd8)。

将栈缓冲区大小向上取整，以满足对齐约束。

<a id="r_ga75b8e6cce01f5a34e9f3d649e561c3af"></a>

```c
#define ARCH_KERNEL_STACK_RESERVED
```

相关声明：[ARCH_KERNEL_STACK_RESERVED](../thread_stack_reference/P004_架构线程接口.md#ga75b8e6cce01f5a34e9f3d649e561c3af)。

仅内核栈（Kernel-only Stack）的 MPU 保护区大小。

<a id="r_ga6ba93b4006be7c5f912d148beee55851"></a>

```c
#define ARCH_KERNEL_STACK_OBJ_ALIGN(size)
```

相关声明：[ARCH_KERNEL_STACK_OBJ_ALIGN](../thread_stack_reference/P004_架构线程接口.md#ga6ba93b4006be7c5f912d148beee55851)。

仅内核栈最低地址所需的对齐。

<a id="r_gab3ab80b9bcef30a3109d6c7cecf941f6"></a>

```c
#define ARCH_IRQ_CONNECT(irq, pri, isr, arg, flags)
```

相关声明：[ARCH_IRQ_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#gab3ab80b9bcef30a3109d6c7cecf941f6)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

静态连接中断的架构专有钩子（Architecture-specific Hook）。

<a id="r_gaf6abdfe089e423aa209f7ad4b8934022"></a>

```c
#define ARCH_PCIE_IRQ_CONNECT(bdf, irq, pri, isr, arg, flags)
```

相关声明：[ARCH_PCIE_IRQ_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#gaf6abdfe089e423aa209f7ad4b8934022)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

连接 PCIe 端点中断的架构专有钩子。

<a id="r_ga875f2b1ca924721fe3854796bd96c2db"></a>

```c
#define ARCH_IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p)
```

相关声明：[ARCH_IRQ_DIRECT_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#ga875f2b1ca924721fe3854796bd96c2db)。

静态连接直接中断的架构专有钩子。

<a id="r_ga491cb79acec18c83b9a61b0b45dfab69"></a>

```c
#define ARCH_ISR_DIRECT_PM()
```

相关声明：[ARCH_ISR_DIRECT_PM](../fatal_irq_reference/P008_架构中断接口.md#ga491cb79acec18c83b9a61b0b45dfab69)。

在直接 ISR 中执行电源管理的架构专有钩子。

<a id="r_ga6c6d57983c066fe8ab21a78f86f7adb3"></a>

```c
#define ARCH_ISR_DIRECT_HEADER()
```

相关声明：[ARCH_ISR_DIRECT_HEADER](../fatal_irq_reference/P008_架构中断接口.md#ga6c6d57983c066fe8ab21a78f86f7adb3)。

进入直接中断时的架构专有状态维护。

<a id="r_gaa7c471213fa28b3685f153ea2a72cf9d"></a>

```c
#define ARCH_ISR_DIRECT_FOOTER(swap)
```

相关声明：[ARCH_ISR_DIRECT_FOOTER](../fatal_irq_reference/P008_架构中断接口.md#gaa7c471213fa28b3685f153ea2a72cf9d)。

退出直接中断时的架构专有状态维护。

<a id="r_ga5279598e93dd914614a2ae52557be1a5"></a>

```c
#define ARCH_ISR_DIRECT_DECLARE(name)
```

相关声明：[ARCH_ISR_DIRECT_DECLARE](../fatal_irq_reference/P008_架构中断接口.md#ga5279598e93dd914614a2ae52557be1a5)。

声明直接中断服务例程的架构专有钩子。

<a id="r_ga8d3604770d7735d229e7d2fef4ff590a"></a>

```c
#define ARCH_EXCEPT(reason_p)
```

相关声明：[ARCH_EXCEPT](../fatal_irq_reference/P008_架构中断接口.md#ga8d3604770d7735d229e7d2fef4ff590a)。

触发由软件引起的致命错误（Software-induced Fatal Error）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>

```c
typedef struct z_thread_stack_element k_thread_stack_t
```

相关声明：[k_thread_stack_t](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)。

`struct z_thread_stack_element` 的类型别名（Typedef）。

<a id="r_a3707e886593b0a8b4995309e4230b717"></a>

```c
typedef void(* k_thread_entry_t) (void *p1, void *p2, void *p3)
```

相关声明：[k_thread_entry_t](#a3707e886593b0a8b4995309e4230b717)。

线程入口函数类型（Thread Entry Point Function Type）。

<a id="r_ga4a9ac90ba7cc7c403472bfdaf3369ed2"></a>

```c
typedef void(* arch_cpustart_t) (void *data)
```

相关声明：[arch_cpustart_t](../arch_core_reference/P005_架构多处理器接口.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)。

每个 CPU 的入口函数（Per-CPU Entry Function）。

<a id="r_gaec9949df614728aa6d677f9f1fafd844"></a>

```c
typedef bool(* stack_trace_callback_fn) (void *cookie, unsigned long addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[stack_trace_callback_fn](../thread_stack_reference/P005_架构栈遍历接口.md#gaec9949df614728aa6d677f9f1fafd844)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

`stack_trace_callback_fn`：`arch_stack_walk` 的回调函数（Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga9ee9f897ec750957de45bf8d43349d5e"></a>

```c
static uint32_t arch_k_cycle_get_32 (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[arch_k_cycle_get_32](../timing_reference/P009_架构计数周期接口.md#ga9ee9f897ec750957de45bf8d43349d5e)。

取得当前周期计数，计数单位由 `CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC` 指定。

<a id="r_gacc1ed8d949f694a1d39e389334caf971"></a>

```c
static uint64_t arch_k_cycle_get_64 (void)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[arch_k_cycle_get_64](../timing_reference/P009_架构计数周期接口.md#gacc1ed8d949f694a1d39e389334caf971)。

与 `arch_k_cycle_get_32()` 相同，但返回值为 64 位。

<a id="r_ga6ce051203e6cc091d0fb42a15f662a48"></a>

```c
void arch_cpu_idle (void)
```

相关声明：[arch_cpu_idle](../arch_core_reference/P006_架构电源管理接口.md#ga6ce051203e6cc091d0fb42a15f662a48)。

节能空闲例程（Power-saving Idle Routine）。

<a id="r_ga4d0297717c23a3cc5df434549e26924d"></a>

```c
void arch_cpu_atomic_idle (unsigned int key)
```

相关声明：[arch_cpu_atomic_idle](../arch_core_reference/P006_架构电源管理接口.md#ga4d0297717c23a3cc5df434549e26924d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

原子地重新使能中断并进入低功耗模式（Low-power Mode）。

<a id="r_gab5e5f1690ef60723890b3d0b40b126d7"></a>

```c
unsigned int arch_pm_state_set_prepare (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arch_pm_state_set_prepare](../arch_core_reference/P006_架构电源管理接口.md#gab5e5f1690ef60723890b3d0b40b126d7)。

进入系统电源管理状态（PM State）前准备中断状态。

<a id="r_gadc25c1301f4fa3496361d0750c09cf4f"></a>

```c
void arch_pm_state_set_finish (unsigned int key)
```

相关声明：[arch_pm_state_set_finish](../arch_core_reference/P006_架构电源管理接口.md#gadc25c1301f4fa3496361d0750c09cf4f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

离开系统电源管理状态后恢复中断状态。

<a id="r_ga32b7e543ce51498200c368c39c900bc8"></a>

```c
void arch_cpu_start (int cpu_num, k_thread_stack_t *stack, int sz, arch_cpustart_t fn, void *arg)
```

相关声明：[arch_cpu_start](../arch_core_reference/P005_架构多处理器接口.md#ga32b7e543ce51498200c368c39c900bc8)、[k_thread_stack_t](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[arch_cpustart_t](../arch_core_reference/P005_架构多处理器接口.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)。

在具备多处理器能力（Multiprocessor，MP）的系统上启动指定编号的 CPU。

<a id="r_ga5a7f0198ee061551c300129bffe64717"></a>

```c
bool arch_cpu_active (int cpu_num)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_cpu_active](../arch_core_reference/P005_架构多处理器接口.md#ga5a7f0198ee061551c300129bffe64717)。

返回 CPU 电源状态（Power Status）。

<a id="r_ga25bca3069cb999b6d4f924b87bf7de38"></a>

```c
static unsigned int arch_irq_lock (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arch_irq_lock](../fatal_irq_reference/P008_架构中断接口.md#ga25bca3069cb999b6d4f924b87bf7de38)。

锁定当前 CPU 的中断。

<a id="r_gaa2b2745d8e99b8730b44805f4d3bbf05"></a>

```c
static void arch_irq_unlock (unsigned int key)
```

相关声明：[arch_irq_unlock](../fatal_irq_reference/P008_架构中断接口.md#gaa2b2745d8e99b8730b44805f4d3bbf05)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

解除当前 CPU 的中断锁定。

<a id="r_ga1b827afafc622d412962f568b78726dc"></a>

```c
static bool arch_irq_unlocked (unsigned int key)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_irq_unlocked](../fatal_irq_reference/P008_架构中断接口.md#ga1b827afafc622d412962f568b78726dc)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

判断以此键调用 `arch_irq_unlock()` 是否会解除中断锁定。

<a id="r_gab7c91d90ed8ccfce15c8bd040496f9ac"></a>

```c
static bool arch_cpu_irqs_are_enabled (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_cpu_irqs_are_enabled](../fatal_irq_reference/P008_架构中断接口.md#gab7c91d90ed8ccfce15c8bd040496f9ac)。

查询当前 CPU 中断控制器的整体锁定状态，不修改该状态。

<a id="r_ga216d692e87bfba955a60f8e570e127df"></a>

```c
void arch_irq_disable (unsigned int irq)
```

相关声明：[arch_irq_disable](../fatal_irq_reference/P008_架构中断接口.md#ga216d692e87bfba955a60f8e570e127df)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用指定中断线路。

<a id="r_gaa278d630653b33cb339621d725ed295a"></a>

```c
void arch_irq_enable (unsigned int irq)
```

相关声明：[arch_irq_enable](../fatal_irq_reference/P008_架构中断接口.md#gaa278d630653b33cb339621d725ed295a)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能指定中断线路。

<a id="r_ga3bd8e963a124421bb372dab4bdc6cd83"></a>

```c
int arch_irq_is_enabled (unsigned int irq)
```

相关声明：[arch_irq_is_enabled](../fatal_irq_reference/P008_架构中断接口.md#ga3bd8e963a124421bb372dab4bdc6cd83)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

判断指定中断线路是否已使能。

<a id="r_ga6f5e4f7795c23586b13c5f6eaecac54d"></a>

```c
void arch_irq_clear_pending (unsigned int irq)
```

相关声明：[arch_irq_clear_pending](../fatal_irq_reference/P008_架构中断接口.md#ga6f5e4f7795c23586b13c5f6eaecac54d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

清除指定中断线路的挂起状态。

<a id="r_gaad2c939389164d483a472d4f6d201ce0"></a>

```c
void arch_irq_set_pending (unsigned int irq)
```

相关声明：[arch_irq_set_pending](../fatal_irq_reference/P008_架构中断接口.md#gaad2c939389164d483a472d4f6d201ce0)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置指定中断线路的挂起状态。

<a id="r_gaa45f7cc9823e3a3b5f760ffc02323516"></a>

```c
bool arch_irq_is_pending (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_irq_is_pending](../fatal_irq_reference/P008_架构中断接口.md#gaa45f7cc9823e3a3b5f760ffc02323516)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

判断指定中断线路是否挂起。

<a id="r_gae2a76360ce4ddcd461c06602ef16ba32"></a>

```c
unsigned int arch_irq_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arch_irq_get_active](../fatal_irq_reference/P008_架构中断接口.md#gae2a76360ce4ddcd461c06602ef16ba32)。

报告当前 CPU 正在服务的中断线路。

<a id="r_gaa4d733913e12a12e104dc4781cca7308"></a>

```c
int arch_irq_connect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[arch_irq_connect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#gaa4d733913e12a12e104dc4781cca7308)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

安装动态中断的架构专有钩子。

<a id="r_ga41483a9fc1090d96d066e107a74ee38c"></a>

```c
int arch_irq_disconnect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[arch_irq_disconnect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#ga41483a9fc1090d96d066e107a74ee38c)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

动态卸载共享中断的架构专有钩子。

<a id="r_gaac8f60e7dfc5ce3222372798e96316ae"></a>

```c
unsigned int arch_irq_allocate (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arch_irq_allocate](../fatal_irq_reference/P008_架构中断接口.md#gaac8f60e7dfc5ce3222372798e96316ae)。

分配 IRQ 的架构专有钩子。

<a id="r_ga5f0942bd035c50c9d2d91ada472f37c4"></a>

```c
void arch_irq_set_used (unsigned int irq)
```

相关声明：[arch_irq_set_used](../fatal_irq_reference/P008_架构中断接口.md#ga5f0942bd035c50c9d2d91ada472f37c4)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

声明某 IRQ 已被使用的架构专有钩子。

<a id="r_ga5c85d7bf54a83190ed27587dc5a01de5"></a>

```c
bool arch_irq_is_used (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_irq_is_used](../fatal_irq_reference/P008_架构中断接口.md#ga5c85d7bf54a83190ed27587dc5a01de5)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

检查某 IRQ 是否已被使用的架构专有钩子。

<a id="r_gad42138d41dff6a4aad8abf7d77fcd8b2"></a>

```c
static struct _cpu * arch_curr_cpu (void)
```

相关声明：[arch_curr_cpu](../arch_core_reference/P005_架构多处理器接口.md#gad42138d41dff6a4aad8abf7d77fcd8b2)。

返回当前执行 CPU 对应的 CPU 结构。

<a id="r_gad628c89816128546501e3c26eaaf9dea"></a>

```c
static uint32_t arch_proc_id (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[arch_proc_id](../arch_core_reference/P005_架构多处理器接口.md#gad628c89816128546501e3c26eaaf9dea)。

处理器硬件 ID（Hardware ID）。

<a id="r_ga8fe90cec57c56993df14c0d545106ca3"></a>

```c
void arch_sched_broadcast_ipi (void)
```

相关声明：[arch_sched_broadcast_ipi](../arch_core_reference/P005_架构多处理器接口.md#ga8fe90cec57c56993df14c0d545106ca3)。

向所有 CPU 广播中断。

<a id="r_gadebac82c1ed0a8a08adb297738d2633e"></a>

```c
void arch_sched_directed_ipi (uint32_t cpu_bitmap)
```

相关声明：[arch_sched_directed_ipi](../arch_core_reference/P005_架构多处理器接口.md#gadebac82c1ed0a8a08adb297738d2633e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向指定 CPU 发送处理器间中断（Inter-processor Interrupt，IPI）。

<a id="r_ga6ffc01f86f4541d1092ee4b277a07ac6"></a>

```c
int arch_smp_init (void)
```

相关声明：[arch_smp_init](../arch_core_reference/P005_架构多处理器接口.md#ga6ffc01f86f4541d1092ee4b277a07ac6)。

<a id="r_ga078e9bf1a4a557d1321ddc4848092cbe"></a>

```c
static unsigned int arch_num_cpus (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arch_num_cpus](../arch_core_reference/P005_架构多处理器接口.md#ga078e9bf1a4a557d1321ddc4848092cbe)。

返回 CPU 数量。

<a id="r_gaa31a233dab4ad575a9a969de10965200"></a>

```c
int arch_page_phys_get (void *virt, uintptr_t *phys)
```

相关声明：[arch_page_phys_get](../arch_core_reference/P003_架构内存映射接口.md#gaa31a233dab4ad575a9a969de10965200)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

取得虚拟地址所映射的物理地址。

<a id="r_ga5e9ab24b9c980e327903fbe3f5bd97f3"></a>

```c
static uintptr_t arch_syscall_invoke0 (uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke0](../arch_core_reference/P004_架构用户空间接口.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起不带参数的系统调用。

<a id="r_ga4cfb3b2b38e5afca889e8b9765d6c3df"></a>

```c
static uintptr_t arch_syscall_invoke1 (uintptr_t arg1, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke1](../arch_core_reference/P004_架构用户空间接口.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 1 个参数的系统调用。

<a id="r_ga1e78f1022aaf10e88727b142b56d4ef0"></a>

```c
static uintptr_t arch_syscall_invoke2 (uintptr_t arg1, uintptr_t arg2, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke2](../arch_core_reference/P004_架构用户空间接口.md#ga1e78f1022aaf10e88727b142b56d4ef0)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 2 个参数的系统调用。

<a id="r_gaacb1c66a1b7bf2293fea269f6b5e1c7e"></a>

```c
static uintptr_t arch_syscall_invoke3 (uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke3](../arch_core_reference/P004_架构用户空间接口.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 3 个参数的系统调用。

<a id="r_ga0ba3ae2290827385b226ebdbf3de3b53"></a>

```c
static uintptr_t arch_syscall_invoke4 (uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke4](../arch_core_reference/P004_架构用户空间接口.md#ga0ba3ae2290827385b226ebdbf3de3b53)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 4 个参数的系统调用。

<a id="r_ga9971c78bc8f579a0dadf84225dc0c3ff"></a>

```c
static uintptr_t arch_syscall_invoke5 (uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t arg5, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke5](../arch_core_reference/P004_架构用户空间接口.md#ga9971c78bc8f579a0dadf84225dc0c3ff)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 5 个参数的系统调用。

<a id="r_gac6cae2197637993a86b6ec6803b5742b"></a>

```c
static uintptr_t arch_syscall_invoke6 (uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t arg5, uintptr_t arg6, uintptr_t call_id)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[arch_syscall_invoke6](../arch_core_reference/P004_架构用户空间接口.md#gac6cae2197637993a86b6ec6803b5742b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

发起带 6 个参数的系统调用。

<a id="r_ga89ab53a218add419e37f89c1f5fd955f"></a>

```c
static bool arch_is_user_context (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_is_user_context](../arch_core_reference/P004_架构用户空间接口.md#ga89ab53a218add419e37f89c1f5fd955f)。

指示当前是否运行在用户模式（User Mode）。

<a id="r_ga71542fcc679a94ad9ea60d7ac46da361"></a>

```c
int arch_mem_domain_max_partitions_get (void)
```

相关声明：[arch_mem_domain_max_partitions_get](../arch_core_reference/P004_架构用户空间接口.md#ga71542fcc679a94ad9ea60d7ac46da361)。

取得内存域（Memory Domain）可包含的最大分区数量。

<a id="r_gab5f05c76b315b6a8d1c3fd68abb8d594"></a>

```c
int arch_mem_domain_deinit (struct k_mem_domain *domain)
```

相关声明：[arch_mem_domain_deinit](../arch_core_reference/P004_架构用户空间接口.md#gab5f05c76b315b6a8d1c3fd68abb8d594)、[k_mem_domain](../memory_domain_reference/P004_内存域结构.md)。

用于反初始化内存域的架构专有钩子（Hook）。

<a id="r_ga13053a9233b86d5cd19dc3cea5804a16"></a>

```c
int arch_buffer_validate (const void *addr, size_t size, int write)
```

相关声明：[arch_buffer_validate](../arch_core_reference/P004_架构用户空间接口.md#ga13053a9233b86d5cd19dc3cea5804a16)。

检查内存区域权限。

<a id="r_ga48be2412ba65ec550ded63e2f1a0470f"></a>

```c
size_t arch_virt_region_align (uintptr_t phys, size_t size)
```

相关声明：[arch_virt_region_align](../arch_core_reference/P004_架构用户空间接口.md#ga48be2412ba65ec550ded63e2f1a0470f)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

取得可优化 MMU 页表布局的最佳虚拟区域对齐。

<a id="r_ga447daa0454a90a7a3a247de01e522567"></a>

```c
FUNC_NORETURN void arch_user_mode_enter (k_thread_entry_t user_entry, void *p1, void *p2, void *p3)
```

相关声明：[arch_user_mode_enter](../arch_core_reference/P004_架构用户空间接口.md#ga447daa0454a90a7a3a247de01e522567)、[k_thread_entry_t](#a3707e886593b0a8b4995309e4230b717)。

从监督模式（Supervisor Mode）单向切换到用户模式。

<a id="r_gad53908f229d7e2c333574b009493644b"></a>

```c
FUNC_NORETURN void arch_syscall_oops (void *ssf)
```

相关声明：[arch_syscall_oops](../arch_core_reference/P004_架构用户空间接口.md#gad53908f229d7e2c333574b009493644b)。

触发看起来来自指定位置的内核 oops（Kernel Oops）。

<a id="r_ga174c4f356fe315c523cefbf513858c9c"></a>

```c
size_t arch_user_string_nlen (const char *s, size_t maxsize, int *err)
```

相关声明：[arch_user_string_nlen](../arch_core_reference/P004_架构用户空间接口.md#ga174c4f356fe315c523cefbf513858c9c)。

安全取得可能无效的字符串长度。

<a id="r_ga306e9d0e5f8094cb75686f1c43d068a9"></a>

```c
static void arch_cohere_stacks (struct k_thread *old_thread, void *old_switch_handle, struct k_thread *new_thread)
```

相关声明：[arch_cohere_stacks](../arch_core_reference/P004_架构用户空间接口.md#ga306e9d0e5f8094cb75686f1c43d068a9)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

在上下文切换前确保缓存一致性（Cache Coherence）。

<a id="r_ga21c8a32d35c4d267b8306d595ff1d726"></a>

```c
void arch_gdb_init (void)
```

相关声明：[arch_gdb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga21c8a32d35c4d267b8306d595ff1d726)。

架构层调试启动（Architecture Layer Debug Start）。

<a id="r_ga9c130421feeee919651828511743b346"></a>

```c
void arch_gdb_continue (void)
```

相关声明：[arch_gdb_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga9c130421feeee919651828511743b346)。

继续运行程序（Continue）。

<a id="r_ga2aa577d5e55c8b739e2be6187336aaf0"></a>

```c
void arch_gdb_step (void)
```

相关声明：[arch_gdb_step](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga2aa577d5e55c8b739e2be6187336aaf0)。

单步继续执行（Single Step）。

<a id="r_ga5317106a8022bea2a0d42af0789cc016"></a>

```c
size_t arch_gdb_reg_readall (struct gdb_ctx *ctx, uint8_t *buf, size_t buflen)
```

相关声明：[arch_gdb_reg_readall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga5317106a8022bea2a0d42af0789cc016)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取全部寄存器，并以十六进制字符串（Hexadecimal String）输出。

<a id="r_ga0ef78d7e193e98549d9665632e53d5ca"></a>

```c
size_t arch_gdb_reg_writeall (struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen)
```

相关声明：[arch_gdb_reg_writeall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga0ef78d7e193e98549d9665632e53d5ca)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接收十六进制字符串（Hexadecimal String），并更新全部寄存器。

<a id="r_gaa3216e9f381f974c374a6399af5cdba5"></a>

```c
size_t arch_gdb_reg_readone (struct gdb_ctx *ctx, uint8_t *buf, size_t buflen, uint32_t regno)
```

相关声明：[arch_gdb_reg_readone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gaa3216e9f381f974c374a6399af5cdba5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取一个寄存器，并以十六进制字符串（Hexadecimal String）输出。

<a id="r_gad717b520d774294bbda78a56cddcaeff"></a>

```c
size_t arch_gdb_reg_writeone (struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen, uint32_t regno)
```

相关声明：[arch_gdb_reg_writeone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gad717b520d774294bbda78a56cddcaeff)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

接收十六进制字符串（Hexadecimal String），并更新一个寄存器。

<a id="r_gab6f42110cf2340132bf2b3916810c01d"></a>

```c
int arch_gdb_add_breakpoint (struct gdb_ctx *ctx, uint8_t type, uintptr_t addr, uint32_t kind)
```

相关声明：[arch_gdb_add_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab6f42110cf2340132bf2b3916810c01d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

添加断点或观察点（Breakpoint or Watchpoint）。

<a id="r_ga734041433f69030ad98439d10ef56ad6"></a>

```c
int arch_gdb_remove_breakpoint (struct gdb_ctx *ctx, uint8_t type, uintptr_t addr, uint32_t kind)
```

相关声明：[arch_gdb_remove_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga734041433f69030ad98439d10ef56ad6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

移除断点或观察点（Breakpoint or Watchpoint）。

<a id="r_gab1111c30383cbf30d5eb66711c326642"></a>

```c
void arch_gdb_post_memory_write (uintptr_t addr, size_t len, uint8_t align)
```

相关声明：[arch_gdb_post_memory_write](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab1111c30383cbf30d5eb66711c326642)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

内存写入后的处理（Post Processing）。

<a id="r_ga5d9923569b40437c28879ff4b3ff77c2"></a>

```c
void arch_timing_init (void)
```

相关声明：[arch_timing_init](../timing_reference/P002_架构计时接口.md#ga5d9923569b40437c28879ff4b3ff77c2)。

初始化计时子系统（Timing Subsystem）。

<a id="r_gaf8cd88e81c2104b5eb0fbe42967b7834"></a>

```c
void arch_timing_start (void)
```

相关声明：[arch_timing_start](../timing_reference/P002_架构计时接口.md#gaf8cd88e81c2104b5eb0fbe42967b7834)。

通知开始收集计时信息。

<a id="r_ga566483c64f5c5d2f0465e3f969303fd3"></a>

```c
void arch_timing_stop (void)
```

相关声明：[arch_timing_stop](../timing_reference/P002_架构计时接口.md#ga566483c64f5c5d2f0465e3f969303fd3)。

通知结束收集计时信息。

<a id="r_gad7a709477650c8596a96fe080f583fdd"></a>

```c
timing_t arch_timing_counter_get (void)
```

相关声明：[timing_t](../timing_reference/P007_计时类型头文件参考.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)、[arch_timing_counter_get](../timing_reference/P002_架构计时接口.md#gad7a709477650c8596a96fe080f583fdd)。

返回计时计数器（Timing Counter）的值。

<a id="r_ga44d3a7bd8b7008c9cd6c0524e97f128c"></a>

```c
uint64_t arch_timing_cycles_get (volatile timing_t *const start, volatile timing_t *const end)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[arch_timing_cycles_get](../timing_reference/P002_架构计时接口.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)、[timing_t](../timing_reference/P007_计时类型头文件参考.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)、[timing_t](../timing_reference/P007_计时类型头文件参考.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)。

获取 `start` 与 `end` 之间的周期数（Cycles）。

<a id="r_ga026409e1dc323ceddb82b2a6f1cc7ca2"></a>

```c
uint64_t arch_timing_freq_get (void)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[arch_timing_freq_get](../timing_reference/P002_架构计时接口.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)。

获取所用计数器的频率，以赫兹（Hertz，Hz）为单位。

<a id="r_ga8424bc96c05dcae34b7ffd445e2916fe"></a>

```c
uint64_t arch_timing_cycles_to_ns (uint64_t cycles)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[arch_timing_cycles_to_ns](../timing_reference/P002_架构计时接口.md#ga8424bc96c05dcae34b7ffd445e2916fe)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将周期数转换为纳秒。

<a id="r_ga925b4caff80f1dbac36531b479b24364"></a>

```c
uint64_t arch_timing_cycles_to_ns_avg (uint64_t cycles, uint32_t count)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[arch_timing_cycles_to_ns_avg](../timing_reference/P002_架构计时接口.md#ga925b4caff80f1dbac36531b479b24364)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将周期数转换为纳秒，并计算平均值。

<a id="r_ga1f7bfb9ce0588f3b423c2a63933d40eb"></a>

```c
uint32_t arch_timing_freq_get_mhz (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[arch_timing_freq_get_mhz](../timing_reference/P002_架构计时接口.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)。

获取所用计数器的频率，以兆赫兹（Megahertz，MHz）为单位。

<a id="r_a9932b29bc0c3b86e4f8cbd6708ef5d9c"></a>

```c
void arch_spin_relax (void)
```

相关声明：[arch_spin_relax](#a9932b29bc0c3b86e4f8cbd6708ef5d9c)。

在自旋循环（Spin Loops）内执行架构专用处理。

<a id="r_ga7129c254277cfa162cd9c5778a7662c2"></a>

```c
void arch_stack_walk (stack_trace_callback_fn callback_fn, void *cookie, const struct k_thread *thread, const struct arch_esf *esf)
```

相关声明：[arch_stack_walk](../thread_stack_reference/P005_架构栈遍历接口.md#ga7129c254277cfa162cd9c5778a7662c2)、[stack_trace_callback_fn](../thread_stack_reference/P005_架构栈遍历接口.md#gaec9949df614728aa6d677f9f1fafd844)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

遍历栈的架构专有函数。

## 1.4\_详细说明（Detailed Documentation）

<a id="a3707e886593b0a8b4995309e4230b717"></a>

### `k_thread_entry_t`

```c
typedef void(* k_thread_entry_t) (void *p1, void *p2, void *p3)
```

线程入口函数类型（Thread Entry Point Function Type）。

线程开始执行时调用其入口函数（Entry Point Function）。最多可以向此函数传递 3 个参数值。

若入口函数（Entry Point Function）返回，线程将永久终止执行。线程负责在返回前释放其拥有的全部共享资源（Shared Resources），例如互斥锁和动态分配的内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `p1` | 第一个参数（First Argument）。 |
| `p2` | 第二个参数（Second Argument）。 |
| `p3` | 第三个参数（Third Argument）。 |

<a id="a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>

### `k_thread_stack_t`

```c
typedef struct z_thread_stack_element k_thread_stack_t
```

`struct z_thread_stack_element` 的类型别名（Typedef）。

**参阅（See Also）**：另请参见：`z_thread_stack_element`。

<a id="a9932b29bc0c3b86e4f8cbd6708ef5d9c"></a>

### `arch_spin_relax()`

```c
void arch_spin_relax ( void )
```

在自旋循环（Spin Loops）内执行架构专用处理。

在禁用中断请求（IRQ）的忙循环（Busy Loops）中调用，例如存在争用的自旋锁循环。默认实现是调用 `arch_nop()` 的弱函数（Weak Function）。架构可按需实现此函数，执行额外检查或电源管理操作。


## 1.5\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/arch/cpu.h](../api_source_supplement_reference/P009_cpu.h_源码浏览.md)
- [zephyr/irq_offload.h](../fatal_irq_reference/P010_中断卸载头文件源码.md)
- [zephyr/arch/syscall.h](../syscall_boot_reference/P007_架构系统调用头文件源码.md)
- [zephyr/timing/types.h](../timing_reference/P008_计时类型头文件源码.md)
- [zephyr/arch/arch_inlines.h](../api_source_supplement_reference/P014_arch_inlines.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P015_arch_interface.h_源码浏览.md)
- [ARCH_THREAD_STACK_RESERVED](../thread_stack_reference/P004_架构线程接口.md#gace8831316d471ccfb06eeddb6d69d817)
- [ARCH_STACK_PTR_ALIGN](../thread_stack_reference/P004_架构线程接口.md#gaf0f8ad93611d93cd0626914837e761d3)
- [ARCH_THREAD_STACK_OBJ_ALIGN](../thread_stack_reference/P004_架构线程接口.md#gab6c1d96f5e018ed166ee401dc84b7ab7)
- [ARCH_THREAD_STACK_SIZE_ADJUST](../thread_stack_reference/P004_架构线程接口.md#gab76d60bd06e5c5a0f995c6b11bf97fd8)
- [ARCH_KERNEL_STACK_RESERVED](../thread_stack_reference/P004_架构线程接口.md#ga75b8e6cce01f5a34e9f3d649e561c3af)
- [ARCH_KERNEL_STACK_OBJ_ALIGN](../thread_stack_reference/P004_架构线程接口.md#ga6ba93b4006be7c5f912d148beee55851)
- [ARCH_IRQ_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#gab3ab80b9bcef30a3109d6c7cecf941f6)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [ARCH_PCIE_IRQ_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#gaf6abdfe089e423aa209f7ad4b8934022)
- [ARCH_IRQ_DIRECT_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#ga875f2b1ca924721fe3854796bd96c2db)
- [ARCH_ISR_DIRECT_PM](../fatal_irq_reference/P008_架构中断接口.md#ga491cb79acec18c83b9a61b0b45dfab69)
- [ARCH_ISR_DIRECT_HEADER](../fatal_irq_reference/P008_架构中断接口.md#ga6c6d57983c066fe8ab21a78f86f7adb3)
- [ARCH_ISR_DIRECT_FOOTER](../fatal_irq_reference/P008_架构中断接口.md#gaa7c471213fa28b3685f153ea2a72cf9d)
- [ARCH_ISR_DIRECT_DECLARE](../fatal_irq_reference/P008_架构中断接口.md#ga5279598e93dd914614a2ae52557be1a5)
- [ARCH_EXCEPT](../fatal_irq_reference/P008_架构中断接口.md#ga8d3604770d7735d229e7d2fef4ff590a)
- [arch_cpustart_t](../arch_core_reference/P005_架构多处理器接口.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [stack_trace_callback_fn](../thread_stack_reference/P005_架构栈遍历接口.md#gaec9949df614728aa6d677f9f1fafd844)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [arch_stack_walk](../thread_stack_reference/P005_架构栈遍历接口.md#ga7129c254277cfa162cd9c5778a7662c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [arch_k_cycle_get_32](../timing_reference/P009_架构计数周期接口.md#ga9ee9f897ec750957de45bf8d43349d5e)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [arch_k_cycle_get_64](../timing_reference/P009_架构计数周期接口.md#gacc1ed8d949f694a1d39e389334caf971)
- [arch_cpu_idle](../arch_core_reference/P006_架构电源管理接口.md#ga6ce051203e6cc091d0fb42a15f662a48)
- [arch_cpu_atomic_idle](../arch_core_reference/P006_架构电源管理接口.md#ga4d0297717c23a3cc5df434549e26924d)
- [arch_pm_state_set_prepare](../arch_core_reference/P006_架构电源管理接口.md#gab5e5f1690ef60723890b3d0b40b126d7)
- [arch_pm_state_set_finish](../arch_core_reference/P006_架构电源管理接口.md#gadc25c1301f4fa3496361d0750c09cf4f)
- [arch_cpu_start](../arch_core_reference/P005_架构多处理器接口.md#ga32b7e543ce51498200c368c39c900bc8)
- [arch_cpu_active](../arch_core_reference/P005_架构多处理器接口.md#ga5a7f0198ee061551c300129bffe64717)
- [arch_irq_lock](../fatal_irq_reference/P008_架构中断接口.md#ga25bca3069cb999b6d4f924b87bf7de38)
- [arch_irq_unlock](../fatal_irq_reference/P008_架构中断接口.md#gaa2b2745d8e99b8730b44805f4d3bbf05)
- [arch_irq_unlocked](../fatal_irq_reference/P008_架构中断接口.md#ga1b827afafc622d412962f568b78726dc)
- [arch_cpu_irqs_are_enabled](../fatal_irq_reference/P008_架构中断接口.md#gab7c91d90ed8ccfce15c8bd040496f9ac)
- [arch_irq_disable](../fatal_irq_reference/P008_架构中断接口.md#ga216d692e87bfba955a60f8e570e127df)
- [arch_irq_enable](../fatal_irq_reference/P008_架构中断接口.md#gaa278d630653b33cb339621d725ed295a)
- [arch_irq_is_enabled](../fatal_irq_reference/P008_架构中断接口.md#ga3bd8e963a124421bb372dab4bdc6cd83)
- [arch_irq_clear_pending](../fatal_irq_reference/P008_架构中断接口.md#ga6f5e4f7795c23586b13c5f6eaecac54d)
- [arch_irq_set_pending](../fatal_irq_reference/P008_架构中断接口.md#gaad2c939389164d483a472d4f6d201ce0)
- [arch_irq_is_pending](../fatal_irq_reference/P008_架构中断接口.md#gaa45f7cc9823e3a3b5f760ffc02323516)
- [arch_irq_get_active](../fatal_irq_reference/P008_架构中断接口.md#gae2a76360ce4ddcd461c06602ef16ba32)
- [arch_irq_connect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#gaa4d733913e12a12e104dc4781cca7308)
- [arch_irq_disconnect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#ga41483a9fc1090d96d066e107a74ee38c)
- [arch_irq_allocate](../fatal_irq_reference/P008_架构中断接口.md#gaac8f60e7dfc5ce3222372798e96316ae)
- [arch_irq_set_used](../fatal_irq_reference/P008_架构中断接口.md#ga5f0942bd035c50c9d2d91ada472f37c4)
- [arch_irq_is_used](../fatal_irq_reference/P008_架构中断接口.md#ga5c85d7bf54a83190ed27587dc5a01de5)
- [arch_curr_cpu](../arch_core_reference/P005_架构多处理器接口.md#gad42138d41dff6a4aad8abf7d77fcd8b2)
- [arch_proc_id](../arch_core_reference/P005_架构多处理器接口.md#gad628c89816128546501e3c26eaaf9dea)
- [arch_sched_broadcast_ipi](../arch_core_reference/P005_架构多处理器接口.md#ga8fe90cec57c56993df14c0d545106ca3)
- [arch_sched_directed_ipi](../arch_core_reference/P005_架构多处理器接口.md#gadebac82c1ed0a8a08adb297738d2633e)
- [arch_smp_init](../arch_core_reference/P005_架构多处理器接口.md#ga6ffc01f86f4541d1092ee4b277a07ac6)
- [arch_num_cpus](../arch_core_reference/P005_架构多处理器接口.md#ga078e9bf1a4a557d1321ddc4848092cbe)
- [arch_page_phys_get](../arch_core_reference/P003_架构内存映射接口.md#gaa31a233dab4ad575a9a969de10965200)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [arch_syscall_invoke0](../arch_core_reference/P004_架构用户空间接口.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)
- [arch_syscall_invoke1](../arch_core_reference/P004_架构用户空间接口.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)
- [arch_syscall_invoke2](../arch_core_reference/P004_架构用户空间接口.md#ga1e78f1022aaf10e88727b142b56d4ef0)
- [arch_syscall_invoke3](../arch_core_reference/P004_架构用户空间接口.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)
- [arch_syscall_invoke4](../arch_core_reference/P004_架构用户空间接口.md#ga0ba3ae2290827385b226ebdbf3de3b53)
- [arch_syscall_invoke5](../arch_core_reference/P004_架构用户空间接口.md#ga9971c78bc8f579a0dadf84225dc0c3ff)
- [arch_syscall_invoke6](../arch_core_reference/P004_架构用户空间接口.md#gac6cae2197637993a86b6ec6803b5742b)
- [arch_is_user_context](../arch_core_reference/P004_架构用户空间接口.md#ga89ab53a218add419e37f89c1f5fd955f)
- [arch_mem_domain_max_partitions_get](../arch_core_reference/P004_架构用户空间接口.md#ga71542fcc679a94ad9ea60d7ac46da361)
- [arch_mem_domain_deinit](../arch_core_reference/P004_架构用户空间接口.md#gab5f05c76b315b6a8d1c3fd68abb8d594)
- [k_mem_domain](../memory_domain_reference/P004_内存域结构.md)
- [arch_buffer_validate](../arch_core_reference/P004_架构用户空间接口.md#ga13053a9233b86d5cd19dc3cea5804a16)
- [arch_virt_region_align](../arch_core_reference/P004_架构用户空间接口.md#ga48be2412ba65ec550ded63e2f1a0470f)
- [arch_user_mode_enter](../arch_core_reference/P004_架构用户空间接口.md#ga447daa0454a90a7a3a247de01e522567)
- [arch_syscall_oops](../arch_core_reference/P004_架构用户空间接口.md#gad53908f229d7e2c333574b009493644b)
- [arch_user_string_nlen](../arch_core_reference/P004_架构用户空间接口.md#ga174c4f356fe315c523cefbf513858c9c)
- [arch_cohere_stacks](../arch_core_reference/P004_架构用户空间接口.md#ga306e9d0e5f8094cb75686f1c43d068a9)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [arch_gdb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga21c8a32d35c4d267b8306d595ff1d726)
- [arch_gdb_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga9c130421feeee919651828511743b346)
- [arch_gdb_step](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga2aa577d5e55c8b739e2be6187336aaf0)
- [arch_gdb_reg_readall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga5317106a8022bea2a0d42af0789cc016)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [arch_gdb_reg_writeall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga0ef78d7e193e98549d9665632e53d5ca)
- [arch_gdb_reg_readone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gaa3216e9f381f974c374a6399af5cdba5)
- [arch_gdb_reg_writeone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gad717b520d774294bbda78a56cddcaeff)
- [arch_gdb_add_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab6f42110cf2340132bf2b3916810c01d)
- [arch_gdb_remove_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga734041433f69030ad98439d10ef56ad6)
- [arch_gdb_post_memory_write](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab1111c30383cbf30d5eb66711c326642)
- [arch_timing_init](../timing_reference/P002_架构计时接口.md#ga5d9923569b40437c28879ff4b3ff77c2)
- [arch_timing_start](../timing_reference/P002_架构计时接口.md#gaf8cd88e81c2104b5eb0fbe42967b7834)
- [arch_timing_stop](../timing_reference/P002_架构计时接口.md#ga566483c64f5c5d2f0465e3f969303fd3)
- [timing_t](../timing_reference/P007_计时类型头文件参考.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)
- [arch_timing_counter_get](../timing_reference/P002_架构计时接口.md#gad7a709477650c8596a96fe080f583fdd)
- [arch_timing_cycles_get](../timing_reference/P002_架构计时接口.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)
- [arch_timing_freq_get](../timing_reference/P002_架构计时接口.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)
- [arch_timing_cycles_to_ns](../timing_reference/P002_架构计时接口.md#ga8424bc96c05dcae34b7ffd445e2916fe)
- [arch_timing_cycles_to_ns_avg](../timing_reference/P002_架构计时接口.md#ga925b4caff80f1dbac36531b479b24364)
- [arch_timing_freq_get_mhz](../timing_reference/P002_架构计时接口.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)
- [arch_nop()](../arch_core_reference/P008_架构杂项接口.md#gabb087b9e158824121212d65646ae4154)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__net__coap_service.h_文件参考.md)
