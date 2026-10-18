---
id: learning.zephyr-docs.kconfig-reference.page-28
title: "`arch/arc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第28章\_`arch/arc`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/arc` 的 53 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARC_AGU_LARGE"></a>

## 28.1 `CONFIG_ARC_AGU_LARGE`

**提示（Prompt）**：ARC AGU 大规模寄存器组（Large-size Registers）

**说明（Help）**

保存并恢复大规模地址生成单元（AGU）寄存器组，包括 12 个地址指针寄存器、8 个地址偏移寄存器和 24 个修饰寄存器（Modifier Register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_AGU_SHARING && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_ARC_AGU_MEDIUM
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options） → ARC 地址生成单元寄存器（Address Generation Unit Registers） → ARC 地址生成单元寄存器共享（AGU Register Sharing）

**配置项引用（Symbol References）**：[`CONFIG_ARC_AGU_SHARING`](P028_arch_arc_配置项参考.md#CONFIG_ARC_AGU_SHARING)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_AGU_MEDIUM`](P028_arch_arc_配置项参考.md#CONFIG_ARC_AGU_MEDIUM)。

<a id="CONFIG_ARC_AGU_MEDIUM"></a>

## 28.2 `CONFIG_ARC_AGU_MEDIUM`

**提示（Prompt）**：ARC AGU 中等规模寄存器组（Medium-size Registers）

**说明（Help）**

保存并恢复中等规模地址生成单元（AGU）寄存器组，包括 8 个地址指针寄存器、4 个地址偏移寄存器和 12 个修饰寄存器（Modifier Register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_AGU_SHARING && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**被选择（Selected by）**

```text
CONFIG_ARC_AGU_LARGE
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options） → ARC 地址生成单元寄存器（Address Generation Unit Registers） → ARC 地址生成单元寄存器共享（AGU Register Sharing）

**配置项引用（Symbol References）**：[`CONFIG_ARC_AGU_SHARING`](P028_arch_arc_配置项参考.md#CONFIG_ARC_AGU_SHARING)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_AGU_LARGE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_AGU_LARGE)。

<a id="CONFIG_ARC_AGU_SHARING"></a>

## 28.3 `CONFIG_ARC_AGU_SHARING`

**提示（Prompt）**：ARC 地址生成单元寄存器共享（AGU Register Sharing）

**说明（Help）**

此选项启用在上下文切换（Context Switch）期间保存硬件地址生成单元（AGU）寄存器，允许多个线程并发操作 XY 存储器（XY Memory）。默认保存并恢复小规模 AGU 寄存器组，包括 4 个地址指针寄存器、2 个地址偏移寄存器和 4 个修饰寄存器（Modifier Register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_XY_ENABLE && CONFIG_MULTITHREADING && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_DSP_SHARING
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options） → ARC 地址生成单元寄存器（Address Generation Unit Registers）

**配置项引用（Symbol References）**：[`CONFIG_ARC_XY_ENABLE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_XY_ENABLE)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_DSP_SHARING`](P028_arch_arc_配置项参考.md#CONFIG_DSP_SHARING)。

<a id="CONFIG_ARC_CONNECT"></a>

## 28.4 `CONFIG_ARC_CONNECT`

**提示（Prompt）**：ARC 具有 ARC CONNECT

**说明（Help）**

ARC 配置了 ARC CONNECT，它是用于连接多个内核的硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
```

**定义位置（Location）**：[`arch/arc/Kconfig:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L247)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)。

<a id="CONFIG_ARC_CORE_MPU"></a>

## 28.5 `CONFIG_ARC_CORE_MPU`

**提示（Prompt）**：ARC 内核 MPU 功能（Core MPU Functionalities）

**说明（Help）**

ARC 内核 MPU 功能（Core MPU Functionalities）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_ARC
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
```

**定义位置（Location）**：[`arch/arc/core/mpu/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/mpu/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC 内存保护单元选项（MPU Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU)。

<a id="CONFIG_ARC_CURRENT_THREAD_USE_NO_TLS"></a>

## 28.6 `CONFIG_ARC_CURRENT_THREAD_USE_NO_TLS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

禁用 ARC 当前的线程局部存储（Thread Local Storage，TLS）实现。对于 `RGF_NUM_BANKS` 大于 1 的内核，默认禁用此参数，因为寄存器组同步（Bank Synchronization）需要较多时间，会降低性能。ARCMWDT 处理 TLS 指针的方式与 GCC 不同；对 MetaWare 而言，通过 `_current` 符号优化访问 TLS 指针并没有明显优势。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_RGF_NUM_BANKS > 1 || "zephyr" = "arcmwdt"
```

**主动选择（Selects）**

```text
CONFIG_CURRENT_THREAD_USE_NO_TLS
```

**定义位置（Location）**：[`arch/arc/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_RGF_NUM_BANKS`](P028_arch_arc_配置项参考.md#CONFIG_RGF_NUM_BANKS)、[`CONFIG_CURRENT_THREAD_USE_NO_TLS`](P001_kernel_配置项参考_1.md#CONFIG_CURRENT_THREAD_USE_NO_TLS)。

<a id="CONFIG_ARC_DCACHE_REGION_OPERATIONS"></a>

## 28.7 `CONFIG_ARC_DCACHE_REGION_OPERATIONS`

**提示（Prompt）**：数据缓存区域操作（DCACHE Region Operations）

**说明（Help）**

按区域（Region）而不是在循环中逐行执行 L1 数据缓存管理操作，以提高缓存管理性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_ARC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/arc/Kconfig:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L402)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_DSP"></a>

## 28.8 `CONFIG_ARC_DSP`

**提示（Prompt）**：数字信号处理（Digital Signal Processing，DSP）

**说明（Help）**

此选项启用 DSP 及其指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_DSP_BFLY_SHARING"></a>

## 28.9 `CONFIG_ARC_DSP_BFLY_SHARING`

**提示（Prompt）**：ARC 复数 DSP 运算（Complex DSP Operation）

**说明（Help）**

此选项使 Zephyr 在上下文切换（Context Switch）期间保存并恢复 `DSP_BFLY0` 和 `FFT_CTRL` 寄存器。只有多个线程使用蝶形指令（Butterfly Instructions）时，才需要此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_DSP && CONFIG_CPU_ARCEM && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_DSP`](P028_arch_arc_配置项参考.md#CONFIG_ARC_DSP)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_DSP_TURNED_OFF"></a>

## 28.10 `CONFIG_ARC_DSP_TURNED_OFF`

**提示（Prompt）**：存在 DSP 时将其关闭（Turn Off DSP）

**说明（Help）**

此选项通过复位 `DSP_CRTL` 寄存器禁用 DSP 模块。

译注：寄存器名称 `DSP_CRTL` 按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARC_DSP && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_DSP`](P028_arch_arc_配置项参考.md#CONFIG_ARC_DSP)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_EARLY_SOC_INIT"></a>

## 28.11 `CONFIG_ARC_EARLY_SOC_INIT`

**提示（Prompt）**：执行早期 SoC 专用初始化（Early-stage SoC-specific Initialization）

**说明（Help）**

在早期初始化阶段，即 C 运行时（C Runtime）初始化之前，调用 SoC 的每内核设置代码。设置代码以汇编宏 `soc_early_asm_init_percpu` 的形式调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/Kconfig:436`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L436)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_EXCEPTION_STACK_SIZE"></a>

## 28.12 `CONFIG_ARC_EXCEPTION_STACK_SIZE`

**提示（Prompt）**：ARC 异常处理栈大小（Exception Handling Stack Size）

**说明（Help）**

异常处理栈（Exception Handling Stack）的大小，以字节为单位。由于异常不频繁，该栈位于中断栈顶部，以减少内存占用。为减小对中断处理，特别是嵌套中断（Nested Interrupt）的影响，此栈不能过大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
768 if !CONFIG_64BIT
2048 if CONFIG_64BIT
```

**定义位置（Location）**：[`arch/arc/Kconfig:424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L424)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_ARC_FIRQ"></a>

## 28.13 `CONFIG_ARC_FIRQ`

**提示（Prompt）**：启用快速中断（FIRQ）

**说明（Help）**

支持快速中断（Fast Interrupt，FIRQ）。启用后，对于最高优先级中断，`status32` 和 `pc` 保存到辅助寄存器（Auxiliary Registers），其他寄存器按寄存器组（Register Bank）数量采取相应保存方式；禁用后，最高优先级中断的处理方式与其他中断相同。

注意：不允许同时启用 FIRQ 且只有一个中断优先级的配置，即所有中断都是 FIRQ。软件不支持这种配置，从性能角度看也没有好处。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_NUM_IRQ_PRIO_LEVELS > 1 && !CONFIG_ARC_HAS_SECURE && CONFIG_ARC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arc/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_NUM_IRQ_PRIO_LEVELS`](P028_arch_arc_配置项参考.md#CONFIG_NUM_IRQ_PRIO_LEVELS)、[`CONFIG_ARC_HAS_SECURE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_SECURE)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_FIRQ_STACK"></a>

## 28.14 `CONFIG_ARC_FIRQ_STACK`

**提示（Prompt）**：独立快速中断栈（Separate FIRQ Stack）

**说明（Help）**

使用独立栈处理快速中断（FIRQ）。当快速中断同时也是直接中断（Direct IRQ）时，可获得最小中断延迟（Interrupt Latency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_FIRQ && CONFIG_RGF_NUM_BANKS > 1 && CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/Kconfig:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L224)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → 启用快速中断（FIRQ）

**配置项引用（Symbol References）**：[`CONFIG_ARC_FIRQ`](P028_arch_arc_配置项参考.md#CONFIG_ARC_FIRQ)、[`CONFIG_RGF_NUM_BANKS`](P028_arch_arc_配置项参考.md#CONFIG_RGF_NUM_BANKS)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_FIRQ_STACK_SIZE"></a>

## 28.15 `CONFIG_ARC_FIRQ_STACK_SIZE`

**提示（Prompt）**：快速中断栈大小（FIRQ Stack Size）

**说明（Help）**

快速中断栈（FIRQ Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_FIRQ_STACK && CONFIG_ARC
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`arch/arc/Kconfig:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L231)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → 启用快速中断（FIRQ） → 独立快速中断栈（Separate FIRQ Stack）

**配置项引用（Symbol References）**：[`CONFIG_ARC_FIRQ_STACK`](P028_arch_arc_配置项参考.md#CONFIG_ARC_FIRQ_STACK)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_HAS_ACCL_REGS"></a>

## 28.16 `CONFIG_ARC_HAS_ACCL_REGS`

**提示（Prompt）**：寄存器对 ACCL:ACCH（FPU 和／或 MPY > 6 和／或 DSP）

**说明（Help）**

根据配置，CPU 可能包含累加器寄存器对（Accumulator Register Pair），也称为 `r58:r59`。GCC 也可能将它们用作通用寄存器（GPR），因此内核需要为每个进程保存／恢复。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_HS3X || CONFIG_CPU_HS4X || CONFIG_CPU_HS5X || CONFIG_CPU_HS6X
```

**被选择（Selected by）**

```text
CONFIG_DSP_SHARING
```

**定义位置（Location）**：[`arch/arc/Kconfig:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L314)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_HS3X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS6X)、[`CONFIG_DSP_SHARING`](P028_arch_arc_配置项参考.md#CONFIG_DSP_SHARING)。

<a id="CONFIG_ARC_HAS_SECURE"></a>

## 28.17 `CONFIG_ARC_HAS_SECURE`

**提示（Prompt）**：ARC 具有 SecureShield

**说明（Help）**

ARC 内核支持安全模式（Secure Mode）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_TEE
CONFIG_ARCH_HAS_TRUSTED_EXECUTION
```

**被选择（Selected by）**

```text
CONFIG_SOC_EMSDP_EM7D_ESP
CONFIG_SOC_SERIES_NSIM_SEM
```

**定义位置（Location）**：[`arch/arc/Kconfig:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L322)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TRUSTED_EXECUTION)、[`CONFIG_SOC_EMSDP_EM7D_ESP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM7D_ESP)、[`CONFIG_SOC_SERIES_NSIM_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_SEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`、`CONFIG_SOC_SERIES_NSIM_SEM`。

<a id="CONFIG_ARC_HAS_STACK_CHECKING"></a>

## 28.18 `CONFIG_ARC_HAS_STACK_CHECKING`

**提示（Prompt）**：ARC 具有栈检查（STACK_CHECKING）

**说明（Help）**

ARC 配置了 `STACK_CHECKING`，这是一种检查栈访问（Stack Access），并在检测到栈溢出或下溢（Overflow/Underflow）时引发异常的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arc/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_HAS_ZOL"></a>

## 28.19 `CONFIG_ARC_HAS_ZOL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARCv2 CPU 具有零开销循环（Zero-overhead Loop，ZOL）硬件机制，而 ARCv3 指令集架构（ISA）取消了该机制。ZOL 在架构层面提供 `LPcc` 指令、`LP_COUNT` 内核寄存器以及 `LP_START`、`LP_END` 辅助寄存器。禁用此选项会从代码中移除 ZOL 寄存器的使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arc/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_MPU"></a>

## 28.20 `CONFIG_ARC_MPU`

**提示（Prompt）**：ARC 内存保护单元（MPU）支持

**说明（Help）**

目标具有 ARC MPU

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_MPU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_ARC_CORE_MPU
CONFIG_THREAD_STACK_INFO
CONFIG_GEN_PRIV_STACKS if !(CONFIG_ARC_MPU_VER = 4 || CONFIG_ARC_MPU_VER = 8)
CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT if !(CONFIG_ARC_MPU_VER = 4 || CONFIG_ARC_MPU_VER = 8)
CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS if CONFIG_ARC_MPU_VER = 4 || CONFIG_ARC_MPU_VER = 8
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS
CONFIG_MEM_DOMAIN_ISOLATED_STACKS if CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_ARC_MPU_ENABLE
```

**定义位置（Location）**：[`arch/arc/core/mpu/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/mpu/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC 内存保护单元选项（MPU Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_ARC_CORE_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_CORE_MPU)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_GEN_PRIV_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_PRIV_STACKS)、[`CONFIG_ARC_MPU_VER`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU_VER)、[`CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_NON_OVERLAPPING_REGIONS)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS)、[`CONFIG_MEM_DOMAIN_ISOLATED_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_MEM_DOMAIN_ISOLATED_STACKS)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARC_MPU_ENABLE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU_ENABLE)。

<a id="CONFIG_ARC_MPU_ENABLE"></a>

## 28.21 `CONFIG_ARC_MPU_ENABLE`

**提示（Prompt）**：内存保护单元（Memory Protection Unit，MPU）

**说明（Help）**

启用内存保护单元（MPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_ARC_MPU
```

**定义位置（Location）**：[`arch/arc/Kconfig:389`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L389)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC 内存保护单元选项（MPU Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU)。

<a id="CONFIG_ARC_MPU_VER"></a>

## 28.22 `CONFIG_ARC_MPU_VER`

**提示（Prompt）**：ARC MPU 版本（Version）

**说明（Help）**

ARC MPU 有多个版本。MPU v2 的最小区域为 2048 字节，其他版本的最小区域为 32 字节；v4 具有安全功能，v6 最多支持 32 个区域。注意：不支持 MPU v5 和 v7。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_ARC
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`arch/arc/core/mpu/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/mpu/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC 内存保护单元选项（MPU Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND"></a>

## 28.23 `CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将原子操作与屏障 API（Atomic and Barrier APIs）路由至 `include/zephyr/arch/arc/` 中的 ARC 后端，而不使用编译器内建函数（Builtins）。MWDT 将每个 `__atomic_*` 操作转换为不含屏障的 `llock/scond` 库例程，丢弃内存序（Memory Order）参数，并将 `__sync_synchronize()` 实现为直接返回。因此，这些内建函数只提供原子性（Atomicity），不提供 Zephyr API 承诺的顺序保证。ARC GNU GCC 自行生成所需的 `dmb` 指令，不受此问题影响。

这是临时规避措施（Workaround）。一旦 MWDT 为原子内建函数实现了内存序支持，应一并撤销此符号和两个 ARC 后端头文件，使 ARC HS 恢复使用内建函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
y if "zephyr" = "arcmwdt"
```

**定义位置（Location）**：[`arch/arc/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_NORMAL_FIRMWARE"></a>

## 28.24 `CONFIG_ARC_NORMAL_FIRMWARE`

**提示（Prompt）**：生成普通固件（Normal Firmware）

**说明（Help）**

此选项表示构建的 Zephyr 镜像将在普通模式（Normal Mode）执行，其执行由安全模式（Secure Mode）下运行的安全固件触发。仅适用于实现 SecureShield 的 ARC 处理器。启用后，Zephyr 包含仅在普通模式执行的代码，并排除仅为安全模式设计的代码。普通模式代码无权访问 ARC 处理器的安全资源（Secure Resources），因此必须避免访问这些资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARC_SECURE_FIRMWARE && CONFIG_ARC_HAS_SECURE && CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`arch/arc/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_SECURE_FIRMWARE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_SECURE_FIRMWARE)、[`CONFIG_ARC_HAS_SECURE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_SECURE)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

<a id="CONFIG_ARC_SECURE_FIRMWARE"></a>

## 28.25 `CONFIG_ARC_SECURE_FIRMWARE`

**提示（Prompt）**：生成安全固件（Secure Firmware）

**说明（Help）**

此选项表示构建的 Zephyr 镜像将在安全模式（Secure Mode）执行，仅适用于实现 SecureShield 的 ARC 处理器。启用后，Zephyr 包含安全模式代码，并排除仅为普通模式（Normal Mode）设计的代码。安全模式代码可以访问 ARC 处理器的安全资源和普通资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_HAS_SECURE && CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_SECURE
```

**定义位置（Location）**：[`arch/arc/Kconfig:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L339)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_HAS_SECURE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_SECURE)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_TRUSTED_EXECUTION_SECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_SECURE)。

<a id="CONFIG_ARC_SLC"></a>

## 28.26 `CONFIG_ARC_SLC`

**提示（Prompt）**：系统级缓存（System Level Cache）

**说明（Help）**

此选项启用系统级缓存（System Level Cache，SLC），并为数据缓存管理操作增加 SLC 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && (CONFIG_CPU_HS4X || CONFIG_CPU_HS3X) && CONFIG_ARC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/arc/Kconfig:410`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L410)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_CPU_HS4X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS3X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS3X)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_SLC_LINE_SIZE"></a>

## 28.27 `CONFIG_ARC_SLC_LINE_SIZE`

**提示（Prompt）**：系统级缓存行大小（SLC Line Size）

**说明（Help）**

CPU 系统级缓存行（System Level Cache Line）的大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_SLC && CONFIG_ARC
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`arch/arc/Kconfig:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L417)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → 系统级缓存（System Level Cache）

**配置项引用（Symbol References）**：[`CONFIG_ARC_SLC`](P028_arch_arc_配置项参考.md#CONFIG_ARC_SLC)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_STACK_CHECKING"></a>

## 28.28 `CONFIG_ARC_STACK_CHECKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 ARC 栈检查（STACK_CHECKING）进行栈保护

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_NO_UNUSED_STACK_INSPECTION
```

**被选择（Selected by）**

```text
CONFIG_ARC_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/arc/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_NO_UNUSED_STACK_INSPECTION`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NO_UNUSED_STACK_INSPECTION)、[`CONFIG_ARC_STACK_PROTECTION`](P028_arch_arc_配置项参考.md#CONFIG_ARC_STACK_PROTECTION)。

<a id="CONFIG_ARC_STACK_PROTECTION"></a>

## 28.29 `CONFIG_ARC_STACK_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用以下两种机制之一：ARC 栈检查（Stack Checking），或基于 MPU 的栈保护区（Stack Guard）。当前进程栈超出边界时，将触发系统致命错误（System Fatal Error）。两种栈保护选项互斥，优先选择 ARC 栈检查，而非基于 MPU 的栈保护区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_ARC_STACK_CHECKING if CONFIG_ARC_HAS_STACK_CHECKING
CONFIG_MPU_STACK_GUARD if !CONFIG_ARC_STACK_CHECKING && CONFIG_ARC_MPU && CONFIG_ARC_MPU_VER != 2
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/arc/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_ARC_STACK_CHECKING`](P028_arch_arc_配置项参考.md#CONFIG_ARC_STACK_CHECKING)、[`CONFIG_ARC_HAS_STACK_CHECKING`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_STACK_CHECKING)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_ARC_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU)、[`CONFIG_ARC_MPU_VER`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU_VER)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_ARC_USE_UNALIGNED_MEM_ACCESS"></a>

## 28.30 `CONFIG_ARC_USE_UNALIGNED_MEM_ACCESS`

**提示（Prompt）**：硬件非对齐访问（Unaligned Access in Hardware）

**说明（Help）**

不支持 SecureShield 2+2 模式的 ARC EM 内核，可能配置了非对齐内存访问（Unaligned Memory Access）能力，但默认禁用。此项在硬件中启用非对齐访问，并让软件使用该能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_CPU_ARCEM && !CONFIG_ARC_HAS_SECURE) || CONFIG_CPU_ARCHS) && CONFIG_ARC
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_ARCHS
```

**定义位置（Location）**：[`arch/arc/Kconfig:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L276)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)、[`CONFIG_ARC_HAS_SECURE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_SECURE)、[`CONFIG_CPU_ARCHS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCHS)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ARC_VPX_COOPERATIVE_SHARING"></a>

## 28.31 `CONFIG_ARC_VPX_COOPERATIVE_SHARING`

**提示（Prompt）**：协作共享 ARC VPX 向量寄存器（Cooperative Sharing of Vector Registers）

**说明（Help）**

此选项启用 ARC VPX 向量寄存器（Vector Registers）的协作共享。需要使用这些寄存器的线程，必须先成功调用 `arc_vpx_lock()`，使用完毕后调用 `arc_vpx_unlock()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_SCHED_CPU_MASK if CONFIG_MP_MAX_NUM_CPUS > 1
```

**定义位置（Location）**：[`arch/arc/Kconfig:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L375)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)。

<a id="CONFIG_ARC_XY_ENABLE"></a>

## 28.32 `CONFIG_ARC_XY_ENABLE`

**提示（Prompt）**：ARC 地址生成单元寄存器（Address Generation Unit Registers）

**说明（Help）**

具有 XY 存储器（XY Memory）和地址生成单元（AGU）寄存器的处理器，可配置此选项以加速 DSP 指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_CODE_DENSITY"></a>

## 28.33 `CONFIG_CODE_DENSITY`

**提示（Prompt）**：代码密度选项（Code Density Option）

**说明（Help）**

启用代码密度选项（Code Density Option），以获得更高代码密度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/Kconfig:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L309)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_CPU_ARCEM"></a>

## 28.34 `CONFIG_CPU_ARCEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARC EM CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_C
```

**被选择（Selected by）**

```text
CONFIG_CPU_EM4
CONFIG_CPU_EM4_DMIPS
CONFIG_CPU_EM4_FPUS
CONFIG_CPU_EM4_FPUDA
CONFIG_CPU_EM6
```

**定义位置（Location）**：[`arch/arc/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_CPU_EM4`](P028_arch_arc_配置项参考.md#CONFIG_CPU_EM4)、[`CONFIG_CPU_EM4_DMIPS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_EM4_DMIPS)、[`CONFIG_CPU_EM4_FPUS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_EM4_FPUS)、[`CONFIG_CPU_EM4_FPUDA`](P028_arch_arc_配置项参考.md#CONFIG_CPU_EM4_FPUDA)、[`CONFIG_CPU_EM6`](P028_arch_arc_配置项参考.md#CONFIG_CPU_EM6)。

<a id="CONFIG_CPU_ARCHS"></a>

## 28.35 `CONFIG_CPU_ARCHS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARC HS CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_ARCH if CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND
CONFIG_ATOMIC_OPERATIONS_BUILTIN if !CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND
CONFIG_BARRIER_OPERATIONS_ARCH if CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND
CONFIG_BARRIER_OPERATIONS_BUILTIN if !CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND
```

**被选择（Selected by）**

```text
CONFIG_CPU_HS3X
CONFIG_CPU_HS4X
CONFIG_CPU_HS5X
CONFIG_CPU_HS6X
```

**定义位置（Location）**：[`arch/arc/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ATOMIC_OPERATIONS_ARCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_ARCH)、[`CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MWDT_MEM_ORDERING_WORKAROUND)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_BARRIER_OPERATIONS_ARCH`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_ARCH)、[`CONFIG_BARRIER_OPERATIONS_BUILTIN`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_BUILTIN)、[`CONFIG_CPU_HS3X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](P028_arch_arc_配置项参考.md#CONFIG_CPU_HS6X)。

<a id="CONFIG_CPU_EM4"></a>

## 28.36 `CONFIG_CPU_EM4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC EM4 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCEM
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_ARC_EM
```

**定义位置（Location）**：[`arch/arc/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)、[`CONFIG_SOC_QEMU_ARC_EM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC_EM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_ARC_EM`。

<a id="CONFIG_CPU_EM4_DMIPS"></a>

## 28.37 `CONFIG_CPU_EM4_DMIPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC EM4 DMIPS CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCEM
```

**定义位置（Location）**：[`arch/arc/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)。

<a id="CONFIG_CPU_EM4_FPUDA"></a>

## 28.38 `CONFIG_CPU_EM4_FPUDA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用带单精度浮点（Single-precision Floating-point）和双精度辅助指令（Double Assist Instructions）的 ARC EM4 DMIPS CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCEM
```

**定义位置（Location）**：[`arch/arc/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)。

<a id="CONFIG_CPU_EM4_FPUS"></a>

## 28.39 `CONFIG_CPU_EM4_FPUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用带单精度浮点扩展（Single-precision Floating-point Extension）的 ARC EM4 DMIPS CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCEM
```

**定义位置（Location）**：[`arch/arc/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)。

<a id="CONFIG_CPU_EM6"></a>

## 28.40 `CONFIG_CPU_EM6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC EM6 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCEM
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**定义位置（Location）**：[`arch/arc/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCEM`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCEM)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)。

<a id="CONFIG_CPU_HS3X"></a>

## 28.41 `CONFIG_CPU_HS3X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC HS3x CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCHS
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_ARC_HS
```

**定义位置（Location）**：[`arch/arc/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCHS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCHS)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_SOC_QEMU_ARC_HS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC_HS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_ARC_HS`。

<a id="CONFIG_CPU_HS4X"></a>

## 28.42 `CONFIG_CPU_HS4X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 HS4X CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV2 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCHS
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**定义位置（Location）**：[`arch/arc/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV2`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV2)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCHS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCHS)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)。

<a id="CONFIG_CPU_HS5X"></a>

## 28.43 `CONFIG_CPU_HS5X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC HS6x CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV3 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCHS
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_ARC_HS5X
```

**定义位置（Location）**：[`arch/arc/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV3`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV3)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCHS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCHS)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_SOC_QEMU_ARC_HS5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC_HS5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_ARC_HS5X`。

<a id="CONFIG_CPU_HS6X"></a>

## 28.44 `CONFIG_CPU_HS6X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设为 `y` 时，SoC 使用 ARC HS6x CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_ARCV3 && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARCHS
CONFIG_64BIT
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_ARC_HS6X
```

**定义位置（Location）**：[`arch/arc/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARCV3`](P028_arch_arc_配置项参考.md#CONFIG_ISA_ARCV3)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_CPU_ARCHS`](P028_arch_arc_配置项参考.md#CONFIG_CPU_ARCHS)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_SOC_QEMU_ARC_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC_HS6X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_ARC_HS6X`。

<a id="CONFIG_DSP_SHARING"></a>

## 28.45 `CONFIG_DSP_SHARING`

原库同名定义共 2 条；本项为数据库第 5216 条记录，各定义分别保留。

**提示（Prompt）**：DSP 寄存器共享（Register Sharing）

**说明（Help）**

此选项启用在上下文切换（Context Switch）期间保存硬件 DSP 寄存器，以允许多个线程并发执行 DSP 运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_DSP && CONFIG_MULTITHREADING && CONFIG_CPU_HAS_DSP && CONFIG_ARC
```

**主动选择（Selects）**

```text
CONFIG_ARC_HAS_ACCL_REGS
```

**定义位置（Location）**：[`arch/arc/core/dsp/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/dsp/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_DSP`](P028_arch_arc_配置项参考.md#CONFIG_ARC_DSP)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_HAS_ACCL_REGS`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_ACCL_REGS)。

<a id="CONFIG_HARVARD"></a>

## 28.46 `CONFIG_HARVARD`

**提示（Prompt）**：哈佛架构（Harvard Architecture）

**说明（Help）**

ARC CPU 可配置为具有两条总线：一条用于指令获取（Instruction Fetch），另一条用作数据总线（Data Bus）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**定义位置（Location）**：[`arch/arc/Kconfig:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L303)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_ISA_ARCV2"></a>

## 28.47 `CONFIG_ISA_ARCV2`

**提示（Prompt）**：ARC 指令集架构（ISA）v2

**说明（Help）**

用于 ARC-HS 和 ARC-EM 内核的 v2 指令集架构（ISA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_ARC_HAS_STACK_CHECKING || (CONFIG_ARC_MPU && CONFIG_ARC_MPU_VER != 2)
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARC_MPU
CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT if !CONFIG_SMP
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT if CONFIG_ARC_MPU && CONFIG_CPU_HAS_DCACHE && CONFIG_ARC_MPU_VER = 6
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
```

**定义位置（Location）**：[`arch/arc/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC 指令集（Instruction Set）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_ARC_HAS_STACK_CHECKING`](P028_arch_arc_配置项参考.md#CONFIG_ARC_HAS_STACK_CHECKING)、[`CONFIG_ARC_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU)、[`CONFIG_ARC_MPU_VER`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU_VER)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ISA_ARCV3"></a>

## 28.48 `CONFIG_ISA_ARCV3`

**提示（Prompt）**：ARC 指令集架构（ISA）v3

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT if !CONFIG_SMP
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
```

**定义位置（Location）**：[`arch/arc/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC 指令集（Instruction Set）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`。

<a id="CONFIG_MPU_STACK_GUARD"></a>

## 28.49 `CONFIG_MPU_STACK_GUARD`

原库同名定义共 2 条；本项为数据库第 12281 条记录，各定义分别保留。

**提示（Prompt）**：线程栈保护区（Thread Stack Guards）

**说明（Help）**

通过 MPU 启用线程栈保护区（Thread Stack Guard）。ARC 支持内置栈保护，如果内核具有该能力，应优先使用它，而非 MPU 栈保护区。对于 `ARC_MPU_VER == 2`，需要额外 2048 字节及严格的起始地址对齐，会造成大量内存浪费，因此不提供支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_CORE_MPU && CONFIG_ARC_MPU_VER != 2 && CONFIG_CPU_HAS_MPU && CONFIG_ARC
```

**被选择（Selected by）**

```text
CONFIG_ARC_STACK_PROTECTION
CONFIG_ARM_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/arc/core/mpu/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/mpu/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options） → ARC 内存保护单元选项（MPU Options） → ARC 内核 MPU 功能（Core MPU Functionalities）

**配置项引用（Symbol References）**：[`CONFIG_ARC_CORE_MPU`](P028_arch_arc_配置项参考.md#CONFIG_ARC_CORE_MPU)、[`CONFIG_ARC_MPU_VER`](P028_arch_arc_配置项参考.md#CONFIG_ARC_MPU_VER)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARC_STACK_PROTECTION`](P028_arch_arc_配置项参考.md#CONFIG_ARC_STACK_PROTECTION)、[`CONFIG_ARM_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_STACK_PROTECTION)。

<a id="CONFIG_NUM_IRQS"></a>

## 28.50 `CONFIG_NUM_IRQS`

**提示（Prompt）**：使用的中断编号／ID 上限（Upper Limit）

**说明（Help）**

可用中断编号为 `0` 到 `NUM_IRQS-1`。最小值为 `17`，因为向量表的前 16 个条目用于 CPU 异常（Exception）。板级支持包（BSP）必须提供有效默认值。此值决定向量表（Vector Table）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**取值范围（Ranges）**

```text
[17, 256]
```

**定义位置（Location）**：[`arch/arc/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_NUM_IRQ_PRIO_LEVELS"></a>

## 28.51 `CONFIG_NUM_IRQ_PRIO_LEVELS`

原库同名定义共 2 条；本项为数据库第 14035 条记录，各定义分别保留。

**提示（Prompt）**：支持的中断优先级数量（Number of Interrupt Priority Levels）

**说明（Help）**

可用中断优先级（Interrupt Priority）为 `0` 到 `NUM_IRQ_PRIO_LEVELS-1`，最小值为 `1`。板级支持包（BSP）必须提供有效默认值，以保证正常运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`arch/arc/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_RGF_NUM_BANKS"></a>

## 28.52 `CONFIG_RGF_NUM_BANKS`

**提示（Prompt）**：通用寄存器组数量（Number of General Purpose Register Banks）

**说明（Help）**

ARC CPU 可配置为具有多个寄存器组（Register Bank）。如果支持快速中断（FIRQ），第二个寄存器组将供 FIRQ 使用。如果支持 FIRQ 但只有一个寄存器组，快速中断处理程序必须保存并恢复通用寄存器（General Purpose Registers）。

注意：使用第二个寄存器组要求中断优先级多于一级，否则所有中断都会使用同一个寄存器组。软件不支持这种配置，从性能角度看也没有好处。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_FIRQ && CONFIG_NUM_IRQ_PRIO_LEVELS > 1 && CONFIG_ARC
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`arch/arc/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_FIRQ`](P028_arch_arc_配置项参考.md#CONFIG_ARC_FIRQ)、[`CONFIG_NUM_IRQ_PRIO_LEVELS`](P028_arch_arc_配置项参考.md#CONFIG_NUM_IRQ_PRIO_LEVELS)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<a id="CONFIG_SJLI_TABLE_SIZE"></a>

## 28.53 `CONFIG_SJLI_TABLE_SIZE`

**提示（Prompt）**：SJLI 表大小（Table Size）

**说明（Help）**

安全索引跳转并链接（Secure Jump and Link Indexed，SJLI）表的大小。普通模式（Normal Mode）的代码通过 `sjli` 指令调用安全模式（Secure Mode）中的安全服务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC_SECURE_FIRMWARE && CONFIG_ARC
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`arch/arc/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → ARC 选项（Options） → ARC CPU 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_SECURE_FIRMWARE`](P028_arch_arc_配置项参考.md#CONFIG_ARC_SECURE_FIRMWARE)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)。

<!-- kconfig-navigation -->

[上一章](P027_arch_Kconfig_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P029_arch_arm_配置项参考_1.md)
