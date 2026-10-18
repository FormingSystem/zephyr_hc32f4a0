---
id: learning.zephyr-docs.kconfig-reference.page-1
title: "内核（Kernel）配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第1章\_内核（Kernel）配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `kernel` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APPLICATION_INIT_PRIORITY"></a>

## 1.1 `CONFIG_APPLICATION_INIT_PRIORITY`

**提示（Prompt）**：应用层驱动的默认初始化优先级（Default Initialization Priority）。

**说明（Help）**

此优先级用于传感器、显示等面向最终使用者、没有其他驱动依赖它们的驱动（End-user Drivers）。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`kernel/Kconfig.device:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 初始化优先级（Initialization Priorities）。

<a id="CONFIG_ARCH_HAS_THREAD_NAME_HOOK"></a>

## 1.2 `CONFIG_ARCH_HAS_THREAD_NAME_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构提供钩子（Hook）处理线程名称变化，所做工作不只是将名称存入内核结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`kernel/Kconfig:722`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L722)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ARCH_MEM_DOMAIN_DATA"></a>

## 1.3 `CONFIG_ARCH_MEM_DOMAIN_DATA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果每个内存域（Memory Domain）都需要架构专用数据，目标架构就选择此隐藏选项。此时，架构定义 `struct arch_mem_domain`，并将其嵌入每个 `struct k_mem_domain`。架构还必须定义 `arch_mem_domain_init()`，在创建内存域时完成初始化。典型用途是保存该内存域的一组页表（Page Tables）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_ARM_MMU
CONFIG_RISCV_PMP
CONFIG_X86
CONFIG_XTENSA
```

**定义位置（Location）**：[`kernel/userspace/Kconfig.mem_domain:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig.mem_domain#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内存域（Memory Domains）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_ARM_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MMU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)。

<a id="CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API"></a>

## 1.4 `CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果运行时修改内存域（Memory Domain）的分区，或改变其线程成员关系，需要同步调用架构层，则目标架构选择此隐藏选项。启用后，架构层必须实现以下 API：`arch_mem_domain_thread_add`、`arch_mem_domain_thread_remove`、`arch_mem_domain_partition_remove`、`arch_mem_domain_partition_add`。

注意，虽然特权线程（Supervisor Thread）可以属于内存域，但这种成员关系不会影响特权线程的内存访问。内存域 API 只能从特权模式（Supervisor Mode）调用。因此，在单处理器系统中，除非通过页表等独立软件结构管理内存访问策略，否则无需实现这些 API，因为上下文切换时本就会重新编程底层内存管理硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_ARM_MMU
CONFIG_RISCV_PMP
CONFIG_XTENSA_MMU
CONFIG_XTENSA_MPU
CONFIG_X86
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`kernel/userspace/Kconfig.mem_domain:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig.mem_domain#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内存域（Memory Domains）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_ARM_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MMU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_XTENSA_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_BARRIER_OPERATIONS_ARCH"></a>

## 1.5 `CONFIG_BARRIER_OPERATIONS_ARCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在不支持编译器内建函数（Compiler Built-ins），但已在 `arch/` 中编写优化汇编实现这些操作时使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_ARCHS
CONFIG_ARM
CONFIG_ARM64
```

**定义位置（Location）**：[`kernel/Kconfig:572`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L572)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 屏障操作（Barrier Operations）。

**配置项引用（Symbol References）**：[`CONFIG_CPU_ARCHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_ARCHS)、[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)。

<a id="CONFIG_BARRIER_OPERATIONS_BUILTIN"></a>

## 1.6 `CONFIG_BARRIER_OPERATIONS_BUILTIN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用编译器内建函数（Compiler Built-in Functions）执行屏障操作，这是首选方式。不过，GCC 尚未完整支持所有架构。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_ARCHS
CONFIG_RISCV
CONFIG_TRICORE
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`kernel/Kconfig:565`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L565)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 屏障操作（Barrier Operations）。

**配置项引用（Symbol References）**：[`CONFIG_CPU_ARCHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_ARCHS)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_TRICORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRICORE)、[`CONFIG_ARCH_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_POSIX)。

<a id="CONFIG_BOARD_EARLY_INIT_HOOK"></a>

## 1.7 `CONFIG_BOARD_EARLY_INIT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

运行早期开发板初始化钩子（Early Board Initialization Hook）。在内核和设备初始化之前执行自定义开发板钩子 `board_early_init_hook()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig.init:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

<a id="CONFIG_BOARD_LATE_INIT_HOOK"></a>

## 1.8 `CONFIG_BOARD_LATE_INIT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

运行后期开发板初始化钩子（Late Board Initialization Hook）。在内核和设备初始化之后执行自定义开发板钩子 `board_late_init_hook()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig.init:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

<a id="CONFIG_BOUNDS_CHECK_BYPASS_MITIGATION"></a>

## 1.9 `CONFIG_BOUNDS_CHECK_BYPASS_MITIGATION`

**提示（Prompt）**：推测执行的边界检查绕过缓解措施（Bounds Check Bypass Mitigations）。

**说明（Help）**

推测执行（Speculative Execution）期间，系统调用可能使用来自用户模式的不可信参数索引数组，这也称为 Spectre V1 漏洞。启用后，`misc/speculation.h` 定义的多个宏，会在对不可信来源（用户模式线程）传入的数组索引参数进行边界检查后，插入屏障指令（Fence Instruction）或其他适当缓解措施。禁用时，这些宏不执行任何操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_X86_BOUNDS_CHECK_BYPASS_MITIGATION
```

**定义位置（Location）**：[`kernel/userspace/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_X86_BOUNDS_CHECK_BYPASS_MITIGATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_BOUNDS_CHECK_BYPASS_MITIGATION)。

<a id="CONFIG_BUSYWAIT_CPU_LOOPS_PER_USEC"></a>

## 1.10 `CONFIG_BUSYWAIT_CPU_LOOPS_PER_USEC`

**提示（Prompt）**：粗略忙循环每微秒的 CPU 循环次数。

**说明（Help）**

用于校准基于 CPU 的粗略忙循环（Busy Loop）时长。默认值假设 CPU 频率为 1 GHz，每次循环消耗 2 个周期。实际情况肯定偏差更大，但这里仅需要一个粗略估计，以满足通过配置移除系统定时器支持的需求。如果精度非常重要，应考虑实现 `arch_busy_wait()`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_SYS_CLOCK_EXISTS && !CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`kernel/Kconfig:911`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L911)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT)。

<a id="CONFIG_CURRENT_THREAD_USE_NO_TLS"></a>

## 1.11 `CONFIG_CURRENT_THREAD_USE_NO_TLS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，表示不使用线程局部存储（Thread Local Storage，TLS）保存当前线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC_CURRENT_THREAD_USE_NO_TLS
CONFIG_XTENSA_MMU
CONFIG_XTENSA_MPU
```

**定义位置（Location）**：[`kernel/Kconfig:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核相关选项（Misc Kernel-related Options）。

**配置项引用（Symbol References）**：[`CONFIG_ARC_CURRENT_THREAD_USE_NO_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_CURRENT_THREAD_USE_NO_TLS)、[`CONFIG_XTENSA_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)。

<a id="CONFIG_CURRENT_THREAD_USE_TLS"></a>

## 1.12 `CONFIG_CURRENT_THREAD_USE_TLS`

**提示（Prompt）**：在线程局部存储（Thread Local Storage，TLS）中保存当前线程。

**说明（Help）**

使用线程局部存储（TLS）保存当前线程。启用用户空间（Userspace）时，这可避免一次系统调用（Syscall）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_LOCAL_STORAGE && !CONFIG_CURRENT_THREAD_USE_NO_TLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核相关选项（Misc Kernel-related Options）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)、[`CONFIG_CURRENT_THREAD_USE_NO_TLS`](P001_kernel_配置项参考_1.md#CONFIG_CURRENT_THREAD_USE_NO_TLS)。

<a id="CONFIG_DEMAND_MAPPING"></a>

## 1.13 `CONFIG_DEMAND_MAPPING`

**提示（Prompt）**：允许按需内存映射（On-demand Memory Mappings）。

**说明（Help）**

启用后，基于 RAM 的内存映射在 `mem_map` 时不会实际分配内存，而是利用按需分页（Demand Paging）机制，在访问时才填充映射。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_DEMAND_MAPPING && CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.vm:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_DEMAND_MAPPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_DEMAND_MAPPING)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING"></a>

## 1.14 `CONFIG_DEMAND_PAGING`

**提示（Prompt）**：按需分页（Demand Paging）［实验性］。

**说明（Help）**

启用按需分页（Demand Paging）。这要求架构在内核链接方式上提供支持，并实现页面淘汰算法（Eviction Algorithm）及保存被淘汰页面的后备存储（Backing Store）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_DEMAND_PAGING && CONFIG_MMU
```

**被弱选择（Implied by）**

```text
CONFIG_POSIX_MEMLOCK_RANGE
```

**定义位置（Location）**：[`kernel/Kconfig.vm:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_DEMAND_PAGING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_POSIX_MEMLOCK_RANGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMLOCK_RANGE)。

<a id="CONFIG_DEMAND_PAGING_ALLOW_IRQ"></a>

## 1.15 `CONFIG_DEMAND_PAGING_ALLOW_IRQ`

**提示（Prompt）**：页面换入／换出时允许中断（Interrupts during Page-in/Page-out）。

**说明（Help）**

允许在淘汰页面或从后备存储（Backing Store）取回页面时处理中断。这有利于降低系统延迟，但中断上下文中运行的任何代码若发生缺页（Page Fault），都会导致内核致命错误（Kernel Panic），因此这些代码必须仅使用已固定驻留（Pinned）的代码页和数据页。此操作期间调度器仍被禁用。若禁用本选项，整个缺页处理过程均在中断关闭状态下运行，但中断服务程序（ISR）也可以发生缺页。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**定义位置（Location）**：[`kernel/Kconfig.vm:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING_PAGE_FRAMES_RESERVE"></a>

## 1.16 `CONFIG_DEMAND_PAGING_PAGE_FRAMES_RESERVE`

**提示（Prompt）**：为分页保留的页框（Page Frame）数量。

**说明（Help）**

设置为分页保留且不计入空闲内存的页框数量，确保分页代码和数据有可用页框。否则，匿名内存映射（Anonymous Memory Mapping）可能耗尽所有页框。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`kernel/Kconfig.vm:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING_STATS"></a>

## 1.17 `CONFIG_DEMAND_PAGING_STATS`

**提示（Prompt）**：收集按需分页统计信息（Demand Paging Statistics）。

**说明（Help）**

启用按需分页相关统计信息的收集，例如缺页次数。这有助于调优页面淘汰算法和优化后备存储（Backing Store）。此功能会带来开销，生产系统应选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**定义位置（Location）**：[`kernel/Kconfig.vm:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING_STATS_USING_TIMING_FUNCTIONS"></a>

## 1.18 `CONFIG_DEMAND_PAGING_STATS_USING_TIMING_FUNCTIONS`

**提示（Prompt）**：使用计时函数收集按需分页统计信息（Demand Paging Statistics）。

**说明（Help）**

使用计时函数（Timing Functions）收集各种按需分页统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT
```

**定义位置（Location）**：[`kernel/Kconfig.vm:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT)。

<a id="CONFIG_DEMAND_PAGING_THREAD_STATS"></a>

## 1.19 `CONFIG_DEMAND_PAGING_THREAD_STATS`

**提示（Prompt）**：按线程收集按需分页统计信息（Per-thread Demand Paging Statistics）。

**说明（Help）**

启用按线程收集按需分页统计信息。此功能会带来开销，生产系统应选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING_STATS && CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**定义位置（Location）**：[`kernel/Kconfig.vm:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING_STATS`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING_STATS)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM"></a>

## 1.20 `CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM`

**提示（Prompt）**：收集按需分页执行时间直方图（Execution Timing Histogram）。

**说明（Help）**

收集页面淘汰选择，以及后备存储页面换入、换出的执行时间直方图（Histogram）。此功能会带来开销，生产系统应选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING_STATS && CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**定义位置（Location）**：[`kernel/Kconfig.vm:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING_STATS`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING_STATS)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS"></a>

## 1.21 `CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS`

**提示（Prompt）**：按需分页时间直方图中的分箱（Bin／Bucket）数量。

**说明（Help）**

定义按需分页执行时间信息直方图使用的分箱（Bin／Bucket）数量。需要由 `k_mem_paging_eviction_histogram_bounds[]` 和 `k_mem_paging_backing_store_histogram_bounds[]` 定义每个分箱的上界。详情参见 `kernel/statistics.c`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM && CONFIG_DEMAND_PAGING && CONFIG_MMU
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`kernel/Kconfig.vm:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。 → 按需分页（Demand Paging）［实验性］。 → 收集按需分页执行时间直方图（Execution Timing Histogram）。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_DEVICE_API_ASSERT"></a>

## 1.22 `CONFIG_DEVICE_API_ASSERT`

**提示（Prompt）**：在 `DEVICE_API_GET` 中执行断言（Assert）。

**说明（Help）**

启用 `DEVICE_API_GET` 的断言，以检查 `NULL` 指针和设备 API 类型；禁用可节省部分闪存空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASSERT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig:1153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1153)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)。

<a id="CONFIG_DEVICE_DEINIT_SUPPORT"></a>

## 1.23 `CONFIG_DEVICE_DEINIT_SUPPORT`

**提示（Prompt）**：支持设备反初始化（Device De-initialization）。

**说明（Help）**

某些非常特殊的情况下，可能需要在运行时对设备进行反初始化。可通过提供执行此操作的函数来实现。注意，这会使每个 `struct device` 增加一个函数指针的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig.device:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备选项（Device Options）。

<a id="CONFIG_DEVICE_DEPS"></a>

## 1.24 `CONFIG_DEVICE_DEPS`

**提示（Prompt）**：保存设备依赖关系（Device Dependencies）。

**说明（Help）**

启用后，保存设备依赖关系以便在运行时查询。设备依赖关系通常从设备树（Devicetree）推导。启用本选项会增加 ROM 用量；启用动态设备依赖关系时，则增加 RAM 用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DMA_INTEL_LPSS
CONFIG_POWER_DOMAIN_GPIO
CONFIG_POWER_DOMAIN_INTEL_ADSP
CONFIG_POWER_DOMAIN_GPIO_MONITOR
CONFIG_POWER_DOMAIN_SOC_PM_STATE
CONFIG_POWER_DOMAIN_ARM_SCMI
CONFIG_POWER_DOMAIN_SILABS_SIWX91X
```

**定义位置（Location）**：[`kernel/Kconfig.device:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备选项（Device Options）。

**配置项引用（Symbol References）**：[`CONFIG_DMA_INTEL_LPSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_INTEL_LPSS)、[`CONFIG_POWER_DOMAIN_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_GPIO)、[`CONFIG_POWER_DOMAIN_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_INTEL_ADSP)、[`CONFIG_POWER_DOMAIN_GPIO_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_GPIO_MONITOR)、[`CONFIG_POWER_DOMAIN_SOC_PM_STATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_SOC_PM_STATE)、[`CONFIG_POWER_DOMAIN_ARM_SCMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_ARM_SCMI)、[`CONFIG_POWER_DOMAIN_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_SILABS_SIWX91X)。

<a id="CONFIG_DEVICE_DEPS_DYNAMIC"></a>

## 1.25 `CONFIG_DEVICE_DEPS_DYNAMIC`

**提示（Prompt）**：动态设备依赖关系（Dynamic Device Dependencies）。

**说明（Help）**

允许在运行时操作设备依赖关系（Device Dependencies）的选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEVICE_DEPS
```

**定义位置（Location）**：[`kernel/Kconfig.device:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备选项（Device Options）。 → 保存设备依赖关系（Device Dependencies）。

**配置项引用（Symbol References）**：[`CONFIG_DEVICE_DEPS`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DEPS)。

<a id="CONFIG_DEVICE_DT_METADATA"></a>

## 1.26 `CONFIG_DEVICE_DT_METADATA`

**提示（Prompt）**：为每个设备保存附加的设备树元数据（Devicetree Metadata）。

**说明（Help）**

启用后，为每个设备保存来自设备树的附加数据，从而可以使用 `device_get_by_dt_nodelabel()`、`device_get_dt_metadata()` 等接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**被弱选择（Implied by）**

```text
CONFIG_SHELL_DEVICE_HELPERS
```

**定义位置（Location）**：[`kernel/Kconfig.device:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备选项（Device Options）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_DEVICE_HELPERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_DEVICE_HELPERS)。

<a id="CONFIG_DEVICE_MUTABLE"></a>

## 1.27 `CONFIG_DEVICE_MUTABLE`

**提示（Prompt）**：可变设备（Mutable Devices）［实验性］。

**说明（Help）**

支持可变设备（Mutable Devices）。这些设备在 SRAM 中实例化，而非闪存中，并且可在内核模式下于运行时修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig.device:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备选项（Device Options）。

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_DYNAMIC_THREAD"></a>

## 1.28 `CONFIG_DYNAMIC_THREAD`

**提示（Prompt）**：动态线程支持（Dynamic Threads）［实验性］。

**说明（Help）**

启用动态线程（Dynamic Threads）及动态栈支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_STACK_INFO
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_DYNAMIC_OBJECTS if CONFIG_USERSPACE
CONFIG_THREAD_MONITOR
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_SOC_SERIES_CC23X0
CONFIG_WIFI_ESP32
```

**定义位置（Location）**：[`kernel/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)、[`CONFIG_DYNAMIC_OBJECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_OBJECTS)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)。

<a id="CONFIG_DYNAMIC_THREAD_ALLOC"></a>

## 1.29 `CONFIG_DYNAMIC_THREAD_ALLOC`

**提示（Prompt）**：支持从堆分配线程对象和线程栈（Heap-allocated Thread Objects and Stacks）。

**说明（Help）**

选择本选项，以启用从系统堆（System Heap）分配线程对象和线程栈。仅应在允许使用 `malloc` 的场景中使用这种分配方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CC23X0
CONFIG_WIFI_ESP32
```

**定义位置（Location）**：[`kernel/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)。

<a id="CONFIG_DYNAMIC_THREAD_POOL_SIZE"></a>

## 1.30 `CONFIG_DYNAMIC_THREAD_POOL_SIZE`

**提示（Prompt）**：静态预分配的线程数量（Statically Pre-allocated Threads）。

**说明（Help）**

在构建时预先分配固定数量的线程对象和线程栈。这种“动态”栈通常适用于不允许使用 `malloc` 的场景。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 8192]
```

**定义位置（Location）**：[`kernel/Kconfig:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)。

<a id="CONFIG_DYNAMIC_THREAD_PREFER"></a>

## 1.31 `CONFIG_DYNAMIC_THREAD_PREFER`

**提示（Prompt）**：首选动态线程分配器（Preferred Dynamic Thread Allocator）。

**说明（Help）**

同时满足 `CONFIG_DYNAMIC_THREAD_ALLOC=y` 和 `CONFIG_DYNAMIC_THREAD_POOL_SIZE > 0` 时，用户可指定尝试分配的顺序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD
```

**默认值（Defaults）**

```text
CONFIG_DYNAMIC_THREAD_PREFER_POOL
```

**可选项（Choices）**

```text
CONFIG_DYNAMIC_THREAD_PREFER_ALLOC
CONFIG_DYNAMIC_THREAD_PREFER_POOL
```

**定义位置（Location）**：[`kernel/Kconfig:246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L246)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_DYNAMIC_THREAD_PREFER_POOL`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_PREFER_POOL)、[`CONFIG_DYNAMIC_THREAD_PREFER_ALLOC`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_PREFER_ALLOC)。

<a id="CONFIG_DYNAMIC_THREAD_PREFER_ALLOC"></a>

## 1.32 `CONFIG_DYNAMIC_THREAD_PREFER_ALLOC`

**提示（Prompt）**：优先从堆分配（Heap-based Allocation）。

**说明（Help）**

选择本选项，先尝试从堆分配，再尝试从池分配（Pool-based Allocation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD_ALLOC && <choice CONFIG_DYNAMIC_THREAD_PREFER>
```

**定义位置（Location）**：[`kernel/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。 → 首选动态线程分配器（Preferred Dynamic Thread Allocator）。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD_ALLOC`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_ALLOC)、[`CONFIG_DYNAMIC_THREAD_PREFER`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_PREFER)。

<a id="CONFIG_DYNAMIC_THREAD_PREFER_POOL"></a>

## 1.33 `CONFIG_DYNAMIC_THREAD_PREFER_POOL`

**提示（Prompt）**：优先从池分配（Pool-based Allocation）。

**说明（Help）**

选择本选项，先尝试从池分配，再尝试从堆分配（Heap-based Allocation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DYNAMIC_THREAD_PREFER>
```

**定义位置（Location）**：[`kernel/Kconfig:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。 → 首选动态线程分配器（Preferred Dynamic Thread Allocator）。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD_PREFER`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_PREFER)。

<a id="CONFIG_DYNAMIC_THREAD_STACK_SIZE"></a>

## 1.34 `CONFIG_DYNAMIC_THREAD_STACK_SIZE`

**提示（Prompt）**：每个预分配线程栈的大小。

**说明（Help）**

动态线程的默认栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD
```

**默认值（Defaults）**

```text
4096 if CONFIG_X86 || CONFIG_COVERAGE_GCOV
1024 if !CONFIG_X86 && !CONFIG_64BIT
2048 if !CONFIG_X86 && CONFIG_64BIT
```

**定义位置（Location）**：[`kernel/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 动态线程支持（Dynamic Threads）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_64BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_64BIT)。

<a id="CONFIG_EVENTS"></a>

## 1.35 `CONFIG_EVENTS`

**提示（Prompt）**：事件对象（Event Objects）。

**说明（Help）**

本选项启用事件对象（Event Objects）。线程可在事件对象上等待特定事件，而线程和中断服务程序（ISR）都可向事件对象投递事件。注意，设置本选项会略微增加线程结构的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING
```

**被选择（Selected by）**

```text
CONFIG_USE_INFINEON_ABSTRACTION_RTOS
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_NXP_RF_IMU
CONFIG_USE_INFINEON_ABSTRACTION_RTOS
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_NXP_RF_IMU
CONFIG_SOC_SERIES_CC23X0
CONFIG_SCHED_IPI_SUPPORTED
CONFIG_BT_AIROC
CONFIG_ETH_STM32_HAL2_API
CONFIG_HDLC_RCP_IF
CONFIG_I2C_CADENCE
CONFIG_I2C_XILINX_AXI
CONFIG_INTEL_EMMC_HOST
CONFIG_SDHC_LITEX_LITESDCARD
CONFIG_SDHC_TI_AM654
CONFIG_XLNX_SDHC
CONFIG_SPI_XLNX_AXI_QUADSPI
CONFIG_SPI_XLNX_ZYNQMP_GQSPI
CONFIG_UDC_DWC2
CONFIG_UDC_NRF
CONFIG_UDC_KINETIS
CONFIG_UDC_IT51XXX
CONFIG_UDC_MCHP_UDPHS_G1
CONFIG_UDC_NXP_EHCI
CONFIG_UDC_NXP_IP3511
CONFIG_UDC_NUMAKER
CONFIG_UDC_RPI_PICO
CONFIG_UDC_SAM0
CONFIG_UDC_SAM_UDP
CONFIG_UDC_SAM_USBC
CONFIG_UDC_SAM_USBHS
CONFIG_UDC_BFLB_V1
CONFIG_UHC_DWC2
CONFIG_UHC_NXP_EHCI
CONFIG_UHC_NXP_KHCI
CONFIG_UHC_NXP_IP3516HS
CONFIG_UHC_NXP_OHCI
CONFIG_NRF_USBHS_WRAPPER
CONFIG_WIFI_BFLB_WIFI4
CONFIG_WIFI_ESP32
CONFIG_WIFI_NXP
CONFIG_WIFI_SILABS_SIWX91X
CONFIG_WIFI_ST67W611M1
CONFIG_CONSOLE_GETCHAR
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE
CONFIG_IPC_SERVICE_ICMSG_ME
CONFIG_HAWKBIT_AUTOHANDLER
CONFIG_MODEM_CMUX
CONFIG_MODEM_PIPE
CONFIG_ZPERF_SESSION_PER_THREAD
CONFIG_PM_DEVICE_RUNTIME_ASYNC
CONFIG_CMSIS_RTOS_V2
CONFIG_SHELL_LOCAL
CONFIG_USBIP
```

**定义位置（Location）**：[`kernel/Kconfig:660`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L660)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_USE_INFINEON_ABSTRACTION_RTOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_ABSTRACTION_RTOS)、[`CONFIG_IRONSIDE_SE_CALL_ZEPHYR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IRONSIDE_SE_CALL_ZEPHYR)、[`CONFIG_NXP_RF_IMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_RF_IMU)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_BT_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AIROC)、[`CONFIG_ETH_STM32_HAL2_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_STM32_HAL2_API)、[`CONFIG_HDLC_RCP_IF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HDLC_RCP_IF)、[`CONFIG_I2C_CADENCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_CADENCE)、[`CONFIG_I2C_XILINX_AXI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_XILINX_AXI)、[`CONFIG_INTEL_EMMC_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC_LITEX_LITESDCARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_LITEX_LITESDCARD)、[`CONFIG_SDHC_TI_AM654`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_TI_AM654)、[`CONFIG_XLNX_SDHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XLNX_SDHC)、[`CONFIG_SPI_XLNX_AXI_QUADSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_XLNX_AXI_QUADSPI)、[`CONFIG_SPI_XLNX_ZYNQMP_GQSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_XLNX_ZYNQMP_GQSPI)、[`CONFIG_UDC_DWC2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DWC2)、[`CONFIG_UDC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NRF)、[`CONFIG_UDC_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_KINETIS)、[`CONFIG_UDC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_IT51XXX)、[`CONFIG_UDC_MCHP_UDPHS_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NXP_EHCI)、[`CONFIG_UDC_NXP_IP3511`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NXP_IP3511)、[`CONFIG_UDC_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_RPI_PICO)、[`CONFIG_UDC_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_SAM0)、[`CONFIG_UDC_SAM_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_SAM_UDP)、[`CONFIG_UDC_SAM_USBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_SAM_USBC)、[`CONFIG_UDC_SAM_USBHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_SAM_USBHS)、[`CONFIG_UDC_BFLB_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_BFLB_V1)、[`CONFIG_UHC_DWC2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DWC2)、[`CONFIG_UHC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_EHCI)、[`CONFIG_UHC_NXP_KHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_KHCI)、[`CONFIG_UHC_NXP_IP3516HS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_IP3516HS)、[`CONFIG_UHC_NXP_OHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_OHCI)、[`CONFIG_NRF_USBHS_WRAPPER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_USBHS_WRAPPER)、[`CONFIG_WIFI_BFLB_WIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_BFLB_WIFI4)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_WIFI_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)、[`CONFIG_CONSOLE_GETCHAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CONSOLE_GETCHAR)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)、[`CONFIG_IPC_SERVICE_ICMSG_ME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_ICMSG_ME)、[`CONFIG_HAWKBIT_AUTOHANDLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_AUTOHANDLER)、[`CONFIG_MODEM_CMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_ZPERF_SESSION_PER_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZPERF_SESSION_PER_THREAD)、[`CONFIG_PM_DEVICE_RUNTIME_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_ASYNC)、[`CONFIG_CMSIS_RTOS_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_RTOS_V2)、[`CONFIG_SHELL_LOCAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_LOCAL)、[`CONFIG_USBIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBIP)。

<a id="CONFIG_EXECUTE_XOR_WRITE"></a>

## 1.36 `CONFIG_EXECUTE_XOR_WRITE`

**提示（Prompt）**：内存分区的写入与执行互斥（W^X）。

**说明（Help）**

启用后，强制可写分区不可执行，反之亦然。这并非在所有场景下都可接受，因此保留此选项，供愿意自行承担风险的使用者选择。若不确定，请选择 `Y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT && CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/userspace/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`。

<a id="CONFIG_FWARGS_HANDLER_HOOK"></a>

## 1.37 `CONFIG_FWARGS_HANDLER_HOOK`

**提示（Prompt）**：固件参数处理钩子（Firmware Argument Handler Hook）。

**说明（Help）**

启用 `fwargs_handler_hook()`，以处理架构保留的固件参数。启用本选项的代码必须提供 `fwargs_handler_hook()` 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK
```

**被选择（Selected by）**

```text
CONFIG_XEN_FDT
```

**定义位置（Location）**：[`kernel/Kconfig.init:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK)、[`CONFIG_XEN_FDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_FDT)。

<a id="CONFIG_HEAP_MEM_POOL_IGNORE_MIN"></a>

## 1.38 `CONFIG_HEAP_MEM_POOL_IGNORE_MIN`

**提示（Prompt）**：忽略堆内存池最低要求（Minimum Heap Memory Pool Requirement）。

**说明（Help）**

可设置本选项，强制使用比已启用子系统要求更小的堆内存池。当优化内存用量，并且已知特定应用更精确的最小堆大小时，这可能有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_MEM_POOL
```

**定义位置（Location）**：[`kernel/Kconfig:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。 → 使用内核内存池（Kernel Memory Pool）。

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_MEM_POOL`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_MEM_POOL)。

<a id="CONFIG_HEAP_MEM_POOL_SIZE"></a>

## 1.39 `CONFIG_HEAP_MEM_POOL_SIZE`

**提示（Prompt）**：堆内存池大小（Heap Memory Pool Size），单位为字节。

**说明（Help）**

本选项指定通过 `k_malloc()` 动态分配内存时使用的堆内存池大小。内存池的最大大小仅受可用内存限制。如果子系统指定了 `HEAP_MEM_POOL_ADD_SIZE_*` 选项，会将这些值求和，再与 `HEAP_MEM_POOL_SIZE` 比较。若总和更大，即使 `HEAP_MEM_POOL_SIZE` 为默认值 0，实际堆大小也会提高到各项要求之和，除非启用了 `HEAP_MEM_POOL_IGNORE_MIN`。同时考虑本选项和自定义要求之和后，如果最终值为零，则不提供系统堆（System Heap）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_MEM_POOL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`kernel/Kconfig:681`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L681)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。 → 使用内核内存池（Kernel Memory Pool）。

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_MEM_POOL`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_MEM_POOL)。

<a id="CONFIG_HW_SHADOW_STACK"></a>

## 1.40 `CONFIG_HW_SHADOW_STACK`

**提示（Prompt）**：使用硬件影子栈机制提供栈保护（Hardware Shadow Stack）［实验性］。

**说明（Help）**

本选项启用硬件影子栈（Hardware Shadow Stack），以提供栈保护。启用后，提供了影子栈的线程将用硬件影子栈保存函数调用的返回地址，从而帮助抵御面向返回编程（Return-oriented Programming，ROP）攻击。目前，内核创建的线程并非全部都有影子栈；线程需要手动附加影子栈才能使用此功能。详情参见相关文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_HW_SHADOW_STACK
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig:1031`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1031)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_HW_SHADOW_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_HW_SHADOW_STACK)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_HW_SHADOW_STACK`。

<a id="CONFIG_HW_SHADOW_STACK_ALLOW_REUSE"></a>

## 1.41 `CONFIG_HW_SHADOW_STACK_ALLOW_REUSE`

**提示（Prompt）**：允许复用影子栈（Shadow Stack Reuse）。

**说明（Help）**

本选项允许复用影子栈（Shadow Stack），用于适应同一线程被再次创建的线程复用情况，例如测试套件的做法。它并非用于在线程之间共享影子栈。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK
```

**默认值（Defaults）**

```text
y if CONFIG_ZTEST
```

**定义位置（Location）**：[`kernel/Kconfig:1071`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1071)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 使用硬件影子栈机制提供栈保护（Hardware Shadow Stack）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_HW_SHADOW_STACK_MIN_SIZE"></a>

## 1.42 `CONFIG_HW_SHADOW_STACK_MIN_SIZE`

**提示（Prompt）**：硬件影子栈的最小大小（Minimum Hardware Shadow Stack Size）。

**说明（Help）**

本选项指定硬件影子栈（Hardware Shadow Stack）的最小大小，单位为字节，使使用最小线程栈的线程仍能拥有合理大小的影子栈。默认值为 256 字节；即使按 `HW_SHADOW_STACK_PERCENTAGE_SIZE` 定义的比例计算出的大小更小，影子栈也至少为 256 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`kernel/Kconfig:1059`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1059)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 使用硬件影子栈机制提供栈保护（Hardware Shadow Stack）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)。

<a id="CONFIG_HW_SHADOW_STACK_PERCENTAGE_SIZE"></a>

## 1.43 `CONFIG_HW_SHADOW_STACK_PERCENTAGE_SIZE`

**提示（Prompt）**：用于计算影子栈大小的线程栈大小百分比。

**说明（Help）**

本选项指定影子栈（Shadow Stack）占线程栈总大小的百分比。默认值为 30%，表示在线程栈原有大小之外，额外分配相当于其 30% 的空间作为影子栈。注意，该大小还受 `HW_SHADOW_STACK_MIN_SIZE` 配置选项约束。译注：原文在该解释后重复出现片段“used for shadow stack.”，此处将重复片段并入同一句含义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`kernel/Kconfig:1046`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1046)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 使用硬件影子栈机制提供栈保护（Hardware Shadow Stack）［实验性］。

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)。

<a id="CONFIG_IDLE_STACK_SIZE"></a>

## 1.44 `CONFIG_IDLE_STACK_SIZE`

**提示（Prompt）**：空闲线程（Idle Thread）的栈大小。

**说明（Help）**

根据空闲任务所需完成的工作，空闲线程（Idle Thread）可能需要比默认值更大的栈。最常见原因是电源管理，也可能是系统事件日志等其他功能，例如记录系统进入睡眠的事件。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
1024 if CONFIG_XTENSA
512 if CONFIG_RISCV
384 if CONFIG_DYNAMIC_OBJECTS
320 if CONFIG_ARC || (CONFIG_ARM && CONFIG_CPU_HAS_FPU) || (CONFIG_X86 && CONFIG_MMU)
256
```

**定义位置（Location）**：[`kernel/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_DYNAMIC_OBJECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_OBJECTS)、[`CONFIG_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC)、[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_CPU_HAS_FPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_FPU)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_INIT_STACKS"></a>

## 1.45 `CONFIG_INIT_STACKS`

**提示（Prompt）**：初始化栈区域（Initialize Stack Areas）。

**说明（Help）**

本选项要求内核在线程栈和中断栈第一次使用之前，用已知值 `0xaa` 初始化其区域，以便确定栈使用高水位（High Water Mark）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_THREAD_ANALYZER
CONFIG_NET_DEBUG_MGMT_EVENT_STACK
CONFIG_PERCEPIO_TRACERECORDER
```

**被弱选择（Implied by）**

```text
CONFIG_KERNEL_SHELL
```

**定义位置（Location）**：[`kernel/Kconfig:396`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L396)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_THREAD_ANALYZER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_ANALYZER)、[`CONFIG_NET_DEBUG_MGMT_EVENT_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DEBUG_MGMT_EVENT_STACK)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)。

<a id="CONFIG_IPI_OPTIMIZE"></a>

## 1.46 `CONFIG_IPI_OPTIMIZE`

**提示（Prompt）**：优化处理器间中断投递（IPI Delivery）。

**说明（Help）**

选择后，当线程新近就绪可运行时，内核尝试确定需要接收处理器间中断（IPI）以触发重新调度的最小 CPU 集合。这使每次调度操作增加相对于 CPU 数量为 O(N) 的计算量，换取投递中断数量的减少；是否选择取决于应用行为。如果架构还支持向指定 CPU 定向发送 IPI，则随着 CPU 数量增加，有可能显著减少系统处理的 IPI 数量，进而减少中断服务程序（ISR）数量。如果架构不支持定向发送，唯一收益是：当新就绪线程的优先级低于其他 CPU 当前执行的所有线程时，不发送任何 IPI。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_IPI_SUPPORTED && CONFIG_MP_MAX_NUM_CPUS > 1 && CONFIG_SMP
```

**默认值（Defaults）**

```text
n
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`kernel/smp/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_IPI_OPTIMIZE_IDLE"></a>

## 1.47 `CONFIG_IPI_OPTIMIZE_IDLE`

**提示（Prompt）**：向一个空闲 CPU 发送调度处理器间中断（Scheduling IPI）。

**说明（Help）**

当线程就绪且可在一个或多个空闲 CPU 上执行时，仅向其中一个 CPU 定向发送调度处理器间中断（IPI），优先选择该线程上次运行的 CPU。如果目标 CPU 尚未调度时已有多个线程就绪，则为它们预留不同的空闲 CPU。此优化减少多个空闲 CPU 争抢新就绪线程时的惊群竞争（Thundering-herd Contention）。CPU 数量越多，收益越大；双 CPU 系统不会出现这种空闲 CPU 竞争，因此此选项对其无效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPI_OPTIMIZE && CONFIG_ARCH_HAS_DIRECTED_IPIS && CONFIG_MP_MAX_NUM_CPUS > 2 && CONFIG_SMP
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`kernel/smp/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。 → 优化处理器间中断投递（IPI Delivery）。

**配置项引用（Symbol References）**：[`CONFIG_IPI_OPTIMIZE`](P001_kernel_配置项参考_1.md#CONFIG_IPI_OPTIMIZE)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)。

<a id="CONFIG_ISR_STACK_SIZE"></a>

## 1.48 `CONFIG_ISR_STACK_SIZE`

**提示（Prompt）**：中断服务程序（ISR）及初始化栈大小，单位为字节。

**说明（Help）**

本选项指定中断服务程序（ISR）以及内核初始化期间使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`kernel/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_KERNEL_COHERENCE"></a>

## 1.49 `CONFIG_KERNEL_COHERENCE`

**提示（Prompt）**：将所有共享数据放入一致性内存（Coherent Memory）。

**说明（Help）**

在支持并选择本选项时，内核以如下模式构建：所有共享数据都放入多处理器一致性内存（Multiprocessor-coherent Memory），通常是不可缓存内存（Uncached Memory）。线程栈仍保持可缓存，使用 `__incoherent` 声明的应用内存也一样。此选项仅面向运行在缓存不一致架构上的 Zephyr 对称多处理（SMP）内核。

注意，选择本选项会隐式改变 API 约定：传给内核的任何内存都被假设具有缓存一致性。在不可缓存区域创建内核数据结构的代码可能出现异常失败。已有一些断言用于捕获这些错误，但无法检查所有情况。译注：此处“不可缓存区域”的表述按原文保留，不自行改写其条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_CAN_SAY_MEM_COHERENCE && CONFIG_SMP
```

**默认值（Defaults）**

```text
y if CONFIG_SMP && CONFIG_MP_MAX_NUM_CPUS > 1
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`kernel/smp/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_CACHE_CAN_SAY_MEM_COHERENCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_CAN_SAY_MEM_COHERENCE)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_KERNEL_DIRECT_MAP"></a>

## 1.50 `CONFIG_KERNEL_DIRECT_MAP`

**提示（Prompt）**：内存区域直接映射支持（Memory Region Direct-map Support）。

**说明（Help）**

启用直接映射（Direct Mapping）支持，即区域的虚拟地址与物理地址可以进行 1:1 映射。如果指定区域位于虚拟地址空间内，且不与已有映射重叠，则在虚拟地址空间中预留该区域并建立映射；否则失败。任何跨越虚拟地址空间边界的尝试也会失败。注意，此功能用于兼容性，可移植应用不应使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU && CONFIG_KERNEL_VM_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_CPU_CORTEX_A
CONFIG_RAM_CONSOLE_BUFFER_SECTION
CONFIG_COUNTER_MCUX_GPT
CONFIG_XEN_REGIONS
```

**定义位置（Location）**：[`kernel/Kconfig.vm:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_RAM_CONSOLE_BUFFER_SECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RAM_CONSOLE_BUFFER_SECTION)、[`CONFIG_COUNTER_MCUX_GPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_MCUX_GPT)、[`CONFIG_XEN_REGIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_REGIONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32MP13X`。

<a id="CONFIG_KERNEL_INIT_PRIORITY_DEFAULT"></a>

## 1.51 `CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`

**提示（Prompt）**：默认初始化优先级（Default Initialization Priority）。

**说明（Help）**

每个初始化级别的默认最低初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`kernel/Kconfig.device:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 初始化优先级（Initialization Priorities）。

<a id="CONFIG_KERNEL_INIT_PRIORITY_DEVICE"></a>

## 1.52 `CONFIG_KERNEL_INIT_PRIORITY_DEVICE`

**提示（Prompt）**：设备驱动的默认初始化优先级（Default Device Driver Initialization Priority）。

**说明（Help）**

依赖中断控制器等公共组件、但不依赖其他设备的设备驱动，使用此初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`kernel/Kconfig.device:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 初始化优先级（Initialization Priorities）。

<a id="CONFIG_KERNEL_INIT_PRIORITY_LIBC"></a>

## 1.53 `CONFIG_KERNEL_INIT_PRIORITY_LIBC`

**提示（Prompt）**：C 标准库初始化优先级（LIBC Initialization Priority）。

**说明（Help）**

C 标准库（LIBC）使用此优先级进行初始化。此优先级必须高于最低默认初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
35
```

**定义位置（Location）**：[`kernel/Kconfig.device:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 初始化优先级（Initialization Priorities）。

<a id="CONFIG_KERNEL_INIT_PRIORITY_OBJECTS"></a>

## 1.54 `CONFIG_KERNEL_INIT_PRIORITY_OBJECTS`

**提示（Prompt）**：内核对象初始化优先级（Kernel Object Initialization Priority）。

**说明（Help）**

内核对象使用此优先级进行初始化。此优先级必须高于最低默认初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`kernel/Kconfig.device:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.device#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 初始化优先级（Initialization Priorities）。

<a id="CONFIG_KERNEL_MEM_POOL"></a>

## 1.55 `CONFIG_KERNEL_MEM_POOL`

**提示（Prompt）**：使用内核内存池（Kernel Memory Pool）。

**说明（Help）**

启用内核内存池（Kernel Memory Pool）。若不确定，请选择 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_GIC_V3_ITS
```

**定义位置（Location）**：[`kernel/Kconfig:671`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L671)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3_ITS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC_V3_ITS)。

<a id="CONFIG_KERNEL_NO_LTO"></a>

## 1.56 `CONFIG_KERNEL_NO_LTO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些片上系统（SoC）要求将内核代码放在 RAM 中，因此这些文件不适合使用链接时优化（Link-time Optimization，LTO），需使用 `-fno-lto`。禁用 LTO 后，受影响的代码可以作为独立目标文件链接，并放入指定内存区域。从 RAM 执行内核代码可提高执行性能，尤其适用于时序关键例程或上下文切换路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LTO && CONFIG_XIP
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM
```

**定义位置（Location）**：[`kernel/Kconfig:1163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1163)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_LTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTO)、[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)、[`CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM)。

<a id="CONFIG_KERNEL_VM_BASE"></a>

## 1.57 `CONFIG_KERNEL_VM_BASE`

**提示（Prompt）**：虚拟地址空间基址（Virtual Address Space Base Address）。

**说明（Help）**

定义内核地址空间的基址。默认与 DTS 中 `DT_CHOSEN_Z_SRAM` 所表示的 SRAM 物理基址相同，此时 RAM 使用恒等映射（Identity Mapping）。某些架构可能要求这样映射 RAM；它们可能只有一个 RAM 区域，采用这种方式可大幅简化链接，因为至少在内核启动时，所有虚拟 RAM 地址都与其物理地址相同。运行时按需分页可能随后改变未固定驻留页框的映射。

如果 RAM 不采用恒等映射：

1. 架构负责在启动早期、进入内核的 `z_cstart()` 之前，将指令指针切换为虚拟地址。
2. 底层架构可能对内核地址空间边界施加约束，例如非恒等映射时不得与物理 RAM 区域重叠，或者虚拟与物理基址必须按同一数值对齐，以便通过分页结构的双重链接简化指令指针切换。

Zephyr 不实现拆分地址空间（Split Address Space）。如果使用多组页表，它们都具有相同的虚拟到物理地址映射，但权限可能不同。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_VM_SUPPORT
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`kernel/Kconfig.vm:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)。

<a id="CONFIG_KERNEL_VM_OFFSET"></a>

## 1.58 `CONFIG_KERNEL_VM_OFFSET`

**提示（Prompt）**：内核在地址空间内的偏移（Kernel Offset within Address Space）。

**说明（Help）**

当内核镜像在其地址空间中的起始偏移不同于其相对 RAM 起点的偏移时，使用此项。选择该值时可能需要谨慎。在某些构建时情形下，或无法通过页表查找物理地址时，将使用以下公式，为启动时已映射的内存进行物理与虚拟地址转换：

```text
virt = phys + ((KERNEL_VM_BASE + KERNEL_VM_OFFSET) - (SRAM_BASE_ADDRESS + SRAM_OFFSET))
```

这种情况并不常见，只有虚拟内存和物理内存起点的对齐方式不同时才需要。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_VM_SUPPORT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`kernel/Kconfig.vm:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)。

<a id="CONFIG_KERNEL_VM_SIZE"></a>

## 1.59 `CONFIG_KERNEL_VM_SIZE`

**提示（Prompt）**：内核地址空间大小，单位为字节。

**说明（Help）**

内核地址空间的大小。限制它有助于控制页表所占总内存量。原文说明，`KERNEL_VM_BASE` 与 `KERNEL_VM_SIZE` 的差值表示运行时内存映射所用虚拟区域的大小。该区域用于映射驱动的内存映射 I/O（MMIO）区域，以及 VSDO 页面、内存映射线程栈、匿名内存映射等特殊 RAM 映射场景。启动时内核本身也映射到此区域。

拥有大量内存（例如 512M 或更多）的系统应使用 64 位 Zephyr 构建。目前没有计划在 Zephyr 中引入“高端内存”（High Memory）概念，来处理物理 RAM 大于所定义虚拟地址空间边界的情况。

译注：原文使用“difference between KERNEL_VM_BASE and KERNEL_VM_SIZE”及“VSDO”，此处保留其表述和拼写，不自行改写成其他计算公式或符号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_VM_SUPPORT
```

**默认值（Defaults）**

```text
0x800000
```

**定义位置（Location）**：[`kernel/Kconfig.vm:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)。

<a id="CONFIG_KERNEL_VM_SUPPORT"></a>

## 1.60 `CONFIG_KERNEL_VM_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于启用虚拟内存相关 Kconfig 选项的隐藏选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MMU
CONFIG_MM_DRV
```

**定义位置（Location）**：[`kernel/Kconfig.vm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_MM_DRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MM_DRV)。

<a id="CONFIG_KERNEL_VM_USE_CUSTOM_MEM_RANGE_CHECK"></a>

## 1.61 `CONFIG_KERNEL_VM_USE_CUSTOM_MEM_RANGE_CHECK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用自定义内存范围检查函数，替代 `k_mem_phys_addr()` 和 `k_mem_virt_addr()` 中的通用检查。必须实现 `sys_mm_is_phys_addr_in_range()` 和 `sys_mm_is_virt_addr_in_range()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE30
CONFIG_SOC_SERIES_INTEL_ADSP_ACE40
```

**定义位置（Location）**：[`kernel/Kconfig.vm:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE30)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`。

<a id="CONFIG_KERNEL_WHOLE_ARCHIVE"></a>

## 1.62 `CONFIG_KERNEL_WHOLE_ARCHIVE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

本选项强制纳入 `libkernel.a` 归档中的每个目标文件，而不是搜索归档并仅提取所需目标文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`kernel/Kconfig:1127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1127)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT)。

<a id="CONFIG_MAIN_STACK_SIZE"></a>

## 1.63 `CONFIG_MAIN_STACK_SIZE`

**提示（Prompt）**：初始化线程和主线程（Main Thread）的栈大小。

**说明（Help）**

初始化完成后，执行初始化的线程继续执行 `main()` 例程，以复用初始化所用的栈，否则这部分 RAM 会被浪费。也就是说，初始化完成后，该线程运行 `main()`。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
512 if CONFIG_ZTEST && !(CONFIG_RISCV || CONFIG_X86 || CONFIG_ARM || CONFIG_ARC || CONFIG_OPENRISC || CONFIG_HEXAGON)
1024
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/mchp_rnbd451_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mchp_rnbd451_bt/Kconfig.defconfig)。

```text
2048 if CONFIG_BT_HOST_CRYPTO
```

来源：[`boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig)。

```text
2560
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
2560
```

**定义位置（Location）**：[`kernel/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC)、[`CONFIG_OPENRISC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENRISC)、[`CONFIG_HEXAGON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEXAGON)、[`CONFIG_BT_HOST_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HOST_CRYPTO)。

<a id="CONFIG_MAIN_THREAD_PRIORITY"></a>

## 1.64 `CONFIG_MAIN_THREAD_PRIORITY`

**提示（Prompt）**：初始化／主线程优先级（Initialization/Main Thread Priority）。

**说明（Help）**

初始化线程运行时的优先级，也适用于刚进入 `main()` 时。之后，`main()` 可按需改变自身优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
-2 if !CONFIG_PREEMPT_ENABLED
0
```

**定义位置（Location）**：[`kernel/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_MAX_DOMAIN_PARTITIONS"></a>

## 1.65 `CONFIG_MAX_DOMAIN_PARTITIONS`

**提示（Prompt）**：每个内存域的最大分区数（Maximum Partitions per Memory Domain）。

**说明（Help）**

配置每个内存域（Memory Domain）的最大分区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`kernel/userspace/Kconfig.mem_domain:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig.mem_domain#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内存域（Memory Domains）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)。

<a id="CONFIG_MEM_DOMAIN_HAS_THREAD_LIST"></a>

## 1.66 `CONFIG_MEM_DOMAIN_HAS_THREAD_LIST`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，每个内存域结构中都有一个双向链表（Doubly Linked List），用于跟踪属于该内存域的线程。需要此功能才能工作的架构会选择本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_ARM64
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT
```

**定义位置（Location）**：[`kernel/userspace/Kconfig.mem_domain:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig.mem_domain#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内存域（Memory Domains）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT)。

<a id="CONFIG_MEM_DOMAIN_ISOLATED_STACKS"></a>

## 1.67 `CONFIG_MEM_DOMAIN_ISOLATED_STACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，同一内存域（Memory Domain）内的线程栈相互隔离，线程不能访问同域其他线程的栈。禁用后，同域线程可以访问彼此的栈。无论此设置如何，线程都不能访问域外线程的栈。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MMU || CONFIG_MPU) && CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS && CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_RISCV_PMP
```

**定义位置（Location）**：[`kernel/userspace/Kconfig.mem_domain:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig.mem_domain#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内存域（Memory Domains）。

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)。

<a id="CONFIG_MEM_SLAB_POINTER_VALIDATE"></a>

## 1.68 `CONFIG_MEM_SLAB_POINTER_VALIDATE`

**提示（Prompt）**：分配或释放时验证内存片（Memory Slab）指针。

**说明（Help）**

启用附加运行时检查，在分配或释放内存片（Memory Slab）时验证其指针。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_ASSERT
```

**定义位置（Location）**：[`kernel/Kconfig:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)。

<a id="CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION"></a>

## 1.69 `CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION`

**提示（Prompt）**：获取内存片最大使用量（Maximum Slab Utilization）。

**说明（Help）**

在 `k_mem_slab` 结构中增加变量，保存内存片（Memory Slab）的最大使用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LWM2M_LOG_ENCODE_BUFFER_ALLOCATIONS
```

**定义位置（Location）**：[`kernel/Kconfig:643`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L643)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_ENCODE_BUFFER_ALLOCATIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_ENCODE_BUFFER_ALLOCATIONS)。

<a id="CONFIG_MMU"></a>

## 1.70 `CONFIG_MMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 CPU 的内存管理单元（MMU）已启用，且 `arch_mem_map()` API 可用时，启用本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MMU
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_VM_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
CONFIG_ARM_AARCH32_MMU
CONFIG_ARM_MMU
CONFIG_XTENSA_MMU
CONFIG_X86_MMU
```

**定义位置（Location）**：[`kernel/Kconfig.vm:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_MMU)、[`CONFIG_KERNEL_VM_SUPPORT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_SUPPORT)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)、[`CONFIG_ARM_AARCH32_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_AARCH32_MMU)、[`CONFIG_ARM_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MMU)、[`CONFIG_XTENSA_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU)、[`CONFIG_X86_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_MMU)。

<a id="CONFIG_MMU_PAGE_SIZE"></a>

## 1.71 `CONFIG_MMU_PAGE_SIZE`

**提示（Prompt）**：内存管理单元最小粒度页大小（Smallest MMU Page Size）。

**说明（Help）**

内存页大小。其值因内存管理单元（MMU）而异，常见值为 4K。对于支持多种页大小的 MMU，在这里填写最小值。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`kernel/Kconfig.vm:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.vm#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 虚拟内存支持（Virtual Memory Support）。 → 内存管理单元特性（MMU Features）。

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_MP_MAX_NUM_CPUS"></a>

## 1.72 `CONFIG_MP_MAX_NUM_CPUS`

**提示（Prompt）**：CPU／处理器核最大数量（Maximum CPUs/Cores）。

**说明（Help）**

多 CPU API 及对称多处理（SMP）功能可使用的、具备多处理能力的处理器核最大数量。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`kernel/smp/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

<a id="CONFIG_MULTITHREADING"></a>

## 1.73 `CONFIG_MULTITHREADING`

**提示（Prompt）**：多线程（Multi-threading）。

**说明（Help）**

禁用后，仅有主线程可用，因此必须提供 `main()` 函数，中断仍可用。内核对象很可能无法按预期工作，尤其是等待（Pending）行为，因为主线程是系统唯一线程，不能进入等待状态。许多驱动和子系统在本选项设为 `n` 时无法工作；只有非常清楚其后果时才应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_INPUT_XEC_KBD
```

**定义位置（Location）**：[`kernel/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT_XEC_KBD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_XEC_KBD)。

<a id="CONFIG_MUTEX_DEADLOCK_DETECT"></a>

## 1.74 `CONFIG_MUTEX_DEADLOCK_DETECT`

**提示（Prompt）**：互斥锁死锁检测（Mutex Deadlock Detection）。

**说明（Help）**

对 `K_FOREVER` 等待，在加锁时检测互斥锁死锁环（Deadlock Cycle）。如果一次 `K_FOREVER` 加锁尝试会在所有权链中形成环，且环内每个成员也都永久等待，则触发断言。若环中任一成员有有限超时时间，则不报告，因为这类情况可通过 `-EAGAIN` 自然恢复。此检测属于优先级继承（Priority Inheritance）的链式遍历；如果 `CONFIG_PRIORITY_CEILING` 设置为等于或低于空闲线程优先级，优先级继承及此检测都会被禁用，因此检测无效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASSERT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)。

<a id="CONFIG_NONZERO_SPINLOCK_SIZE"></a>

## 1.75 `CONFIG_NONZERO_SPINLOCK_SIZE`

**提示（Prompt）**：强制自旋锁大小非零（Non-zero Spinlock Size）。

**说明（Help）**

本选项表示自旋锁（Spinlock）结构必须具有非零大小，例如用于数组时。使用 C++ 时会自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPP
CONFIG_POSIX_SPIN_LOCKS
```

**定义位置（Location）**：[`kernel/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核相关选项（Misc Kernel-related Options）。

**配置项引用（Symbol References）**：[`CONFIG_CPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPP)、[`CONFIG_POSIX_SPIN_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SPIN_LOCKS)。

<a id="CONFIG_NUM_COOP_PRIORITIES"></a>

## 1.76 `CONFIG_NUM_COOP_PRIORITIES`

**提示（Prompt）**：协作式优先级数量（Cooperative Priorities）。

**说明（Help）**

系统配置的协作式优先级数量。可用优先级为 `K_PRIO_COOP(0)` 至 `K_PRIO_COOP(CONFIG_NUM_COOP_PRIORITIES - 1)`；换一种表示方式，即 `-CONFIG_NUM_COOP_PRIORITIES` 至 `-1`。设为零可禁用协作式调度（Cooperative Scheduling）。协作式线程总是能够抢占可抢占线程。优先级总数为 `NUM_COOP_PRIORITIES + NUM_PREEMPT_PRIORITIES + 1`，额外的一个用于空闲线程；空闲线程必须运行在最低优先级，并且是该优先级唯一的线程。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
1 if !CONFIG_MULTITHREADING
16
```

**取值范围（Ranges）**

```text
[0, 128]
```

**定义位置（Location）**：[`kernel/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 多线程（Multi-threading）。

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_NUM_MBOX_ASYNC_MSGS"></a>

## 1.77 `CONFIG_NUM_MBOX_ASYNC_MSGS`

**提示（Prompt）**：在途异步邮箱消息的最大数量（In-flight Asynchronous Mailbox Messages）。

**说明（Help）**

本选项指定整个系统所有邮箱中可同时存在的异步邮箱消息（Asynchronous Mailbox Messages）总数。设为 0 可禁用异步邮箱消息支持。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`kernel/Kconfig:649`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L649)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

<a id="CONFIG_NUM_METAIRQ_PRIORITIES"></a>

## 1.78 `CONFIG_NUM_METAIRQ_PRIORITIES`

**提示（Prompt）**：超高优先级抢占线程（Preemptor Threads）的数量。

**说明（Help）**

在优先级范围数值最小的一端，定义一组具有“元中断”（Meta-IRQ）行为的优先级。这些优先级上的可运行线程，总是先于较低优先级线程调度，即使后者是协作式线程和／或已锁定调度器。以任何方式使这类线程变为可运行，都会产生“中断”当前任务并同步运行元中断线程的效果，类似异常或系统调用。

其意图是实现“中断下半部”（Interrupt Bottom Half）或“小任务”（Tasklet）行为，让驱动子系统返回中断上下文，同时保证剩余工作完成之前，当前 CPU 不执行用户代码。由于这打破了现有 API 对协作式线程不可抢占的承诺，应用代码可能不应使用此机制。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`kernel/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_NUM_PREEMPT_PRIORITIES"></a>

## 1.79 `CONFIG_NUM_PREEMPT_PRIORITIES`

**提示（Prompt）**：可抢占优先级数量（Preemptible Priorities）。

**说明（Help）**

系统可用的可抢占优先级数量，范围为 0 至 `CONFIG_NUM_PREEMPT_PRIORITIES - 1`。设为 0 可禁用抢占式调度（Preemptible Scheduling）。优先级总数为 `NUM_COOP_PRIORITIES + NUM_PREEMPT_PRIORITIES + 1`，额外的一个用于空闲线程；空闲线程必须运行在最低优先级，并且是该优先级唯一的线程。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
0 if !CONFIG_MULTITHREADING
15
```

**取值范围（Ranges）**

```text
[0, 127]
```

**定义位置（Location）**：[`kernel/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 多线程（Multi-threading）。

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_OBJ_CORE"></a>

## 1.80 `CONFIG_OBJ_CORE`

**提示（Prompt）**：对象核心框架（Object Core Framework）。

**说明（Help）**

本选项启用对象核心框架（Object Core Framework），将参与其中的内核对象及各自类型关联起来，使它们既能集中保存公共信息，又能通过自动化方式轻松获取这些信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**被选择（Selected by）**

```text
CONFIG_TRACING_OBJECT_TRACKING
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_TRACING_OBJECT_TRACKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING_OBJECT_TRACKING)。

<a id="CONFIG_OBJ_CORE_CONDVAR"></a>

## 1.81 `CONFIG_OBJ_CORE_CONDVAR`

**提示（Prompt）**：将条件变量（Condition Variables）集成到对象核心框架。

**说明（Help）**

启用后，将条件变量（Condition Variables）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_EVENT"></a>

## 1.82 `CONFIG_OBJ_CORE_EVENT`

**提示（Prompt）**：将事件（Events）集成到对象核心框架。

**说明（Help）**

启用后，将内核事件（Kernel Events）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y if CONFIG_EVENTS
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_OBJ_CORE_EVICT_ON_FREE"></a>

## 1.83 `CONFIG_OBJ_CORE_EVICT_ON_FREE`

**提示（Prompt）**：注销已释放内存中的对象（Unregister Objects in Released Memory）。

**说明（Help）**

当内存归还给 `sys_heap`、内存片（Memory Slab）或内存块分配器（Memory Blocks Allocator）时，注销其中所有对象，使它们立即停止被报告。代价是每次释放都要扫描注册表（Registry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_HEAP_RELEASE_HOOK
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_SYS_HEAP_RELEASE_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_HEAP_RELEASE_HOOK)。

<a id="CONFIG_OBJ_CORE_FIFO"></a>

## 1.84 `CONFIG_OBJ_CORE_FIFO`

**提示（Prompt）**：将先进先出队列（FIFO）集成到对象核心框架。

**说明（Help）**

启用后，将先进先出队列（FIFO）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_LIFO"></a>

## 1.85 `CONFIG_OBJ_CORE_LIFO`

**提示（Prompt）**：将后进先出队列（LIFO）集成到对象核心框架。

**说明（Help）**

启用后，将后进先出队列（LIFO）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_MAILBOX"></a>

## 1.86 `CONFIG_OBJ_CORE_MAILBOX`

**提示（Prompt）**：将邮箱（Mailbox）集成到对象核心框架。

**说明（Help）**

启用后，将邮箱（Mailbox）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS"></a>

## 1.87 `CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS`

**提示（Prompt）**：已注册对象的最大数量（Maximum Registered Objects）。

**说明（Help）**

运行时初始化对象的注册表（Registry）大小，例如嵌入驱动数据中的内核对象。静态定义的对象，如 `K_SEM_DEFINE()` 及类似对象，直接就地枚举，不占注册表条目；位于线程栈或中断栈内的对象从不注册。注册表满时，不再跟踪后续对象，并递增该对象类型的丢弃计数（Dropped Count）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_MEM_SLAB"></a>

## 1.88 `CONFIG_OBJ_CORE_MEM_SLAB`

**提示（Prompt）**：将内存片（Memory Slab）集成到对象核心框架。

**说明（Help）**

启用后，将内存片（Memory Slab）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_MSGQ"></a>

## 1.89 `CONFIG_OBJ_CORE_MSGQ`

**提示（Prompt）**：将消息队列（Message Queue）集成到对象核心框架。

**说明（Help）**

启用后，将消息队列（Message Queue）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_MUTEX"></a>

## 1.90 `CONFIG_OBJ_CORE_MUTEX`

**提示（Prompt）**：将互斥锁（Mutex）集成到对象核心框架。

**说明（Help）**

启用后，将互斥锁（Mutex）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_PIPE"></a>

## 1.91 `CONFIG_OBJ_CORE_PIPE`

**提示（Prompt）**：将管道（Pipe）集成到对象核心框架。

**说明（Help）**

启用后，将管道（Pipe）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_QUEUE"></a>

## 1.92 `CONFIG_OBJ_CORE_QUEUE`

**提示（Prompt）**：将队列（Queue）集成到对象核心框架。

**说明（Help）**

启用后，将队列（Queue）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_SEM"></a>

## 1.93 `CONFIG_OBJ_CORE_SEM`

**提示（Prompt）**：将信号量（Semaphore）集成到对象核心框架。

**说明（Help）**

启用后，将信号量（Semaphore）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_STACK"></a>

## 1.94 `CONFIG_OBJ_CORE_STACK`

**提示（Prompt）**：将栈（Stack）集成到对象核心框架。

**说明（Help）**

启用后，将栈（Stack）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_STATS"></a>

## 1.95 `CONFIG_OBJ_CORE_STATS`

**提示（Prompt）**：对象核心统计（Object Core Statistics）。

**说明（Help）**

将统计信息收集功能集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_NET_SOCKETS_OBJ_CORE
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_NET_SOCKETS_OBJ_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_STATS_MEM_SLAB"></a>

## 1.96 `CONFIG_OBJ_CORE_STATS_MEM_SLAB`

**提示（Prompt）**：内存片对象核心统计（Memory Slab Object Core Statistics）。

**说明（Help）**

启用后，允许将内存片（Memory Slab）统计信息集成到内核对象中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE_STATS && CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y if CONFIG_OBJ_CORE_MEM_SLAB
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。 → 对象核心统计（Object Core Statistics）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE_STATS`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS)、[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_OBJ_CORE_MEM_SLAB`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_MEM_SLAB)。

<a id="CONFIG_OBJ_CORE_STATS_SYSTEM"></a>

## 1.97 `CONFIG_OBJ_CORE_STATS_SYSTEM`

**提示（Prompt）**：系统级对象的对象核心统计（System-level Object Core Statistics）。

**说明（Help）**

启用后，将 CPU 级和系统级线程运行时间统计，集成到对象核心统计框架（Object Core Statistics Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE_STATS && CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y if CONFIG_OBJ_CORE_SYSTEM
```

**主动选择（Selects）**

```text
CONFIG_SCHED_THREAD_USAGE_ALL
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。 → 对象核心统计（Object Core Statistics）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE_STATS`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS)、[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_OBJ_CORE_SYSTEM`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_SYSTEM)、[`CONFIG_SCHED_THREAD_USAGE_ALL`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE_ALL)。

<a id="CONFIG_OBJ_CORE_STATS_THREAD"></a>

## 1.98 `CONFIG_OBJ_CORE_STATS_THREAD`

**提示（Prompt）**：线程对象核心统计（Thread Object Core Statistics）。

**说明（Help）**

启用后，将线程运行时间统计集成到对象核心统计框架（Object Core Statistics Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE_STATS && CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y if CONFIG_OBJ_CORE_THREAD
```

**主动选择（Selects）**

```text
CONFIG_THREAD_RUNTIME_STATS
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。 → 对象核心统计（Object Core Statistics）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE_STATS`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS)、[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_OBJ_CORE_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_THREAD)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)。

<a id="CONFIG_OBJ_CORE_SYSTEM"></a>

## 1.99 `CONFIG_OBJ_CORE_SYSTEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，将内部 CPU 对象和内核系统对象集成到对象核心框架（Object Core Framework）。由于这些是内部结构，本选项默认隐藏，仅向高级用户提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_OBJ_CORE_THREAD"></a>

## 1.100 `CONFIG_OBJ_CORE_THREAD`

**提示（Prompt）**：将线程（Thread）集成到对象核心框架。

**说明（Help）**

启用后，将线程（Thread）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<!-- kconfig-navigation -->

[返回大纲](大纲.md) · [下一章](P002_kernel_配置项参考_2.md)
