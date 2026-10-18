---
id: learning.zephyr-docs.kconfig-reference.page-29
title: "`arch/arm`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第29章\_`arch/arm`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `arch/arm` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AARCH32_ARMV8_A"></a>

## 29.1 `CONFIG_AARCH32_ARMV8_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用在 AArch32 执行状态（Execution State）下运行的 ARMv8-A 处理器。根据 [Arm A-profile 架构说明](https://developer.arm.com/products/architecture/cpu-architecture/a-profile)，Armv8-A 面向应用处理器体系（Applications Profile），在 32 位 AArch32 状态之外引入 64 位执行状态 AArch64。在 AArch32 状态下，它提供基于内存管理单元（MMU）的虚拟内存系统架构（Virtual Memory System Architecture，VMSA），支持 A32 和 T32 指令集。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARM_A_PROFILE_AARCH32
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ISA_ARM
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_ARCH_HAS_DIRECTED_IPIS
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A32
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM_A_PROFILE_AARCH32`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_A_PROFILE_AARCH32)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ISA_ARM`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_ARM)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_CPU_CORTEX_A32`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_A32)。

<a id="CONFIG_AARCH32_ARMV8_A_MONITOR_INIT"></a>

## 29.2 `CONFIG_AARCH32_ARMV8_A_MONITOR_INIT`

**提示（Prompt）**：复位时执行监控模式初始化（Monitor Mode Initialization）

**说明（Help）**

在复位时启用早期监控模式（Monitor Mode，即 EL3 AArch32）初始化，类似 arm64 移植中的 EL3 初始化 `z_arm64_el3_init`。ARMv8-A AArch32 平台裸机启动且不使用 Trusted Firmware-A 时，内核复位进入安全 SVC 模式（Secure SVC Mode）。某些系统寄存器只能从监控模式访问，例如用于启用 GICv3 CPU 接口系统寄存器访问的 `ICC_MSRE`。此选项在复位时短暂切换到监控模式，配置这些寄存器后返回 SVC。该代码块在每个 CPU 复位时、SMP 投票（SMP Voting）之前执行。

在 AArch32 安全状态下裸机启动，且 EL3 以 AArch32 实现、监控模式可用时启用。当 EL3 仅支持 AArch64、Trusted Firmware-A 已完成此初始化，或从非安全状态启动时，应保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AARCH32_ARMV8_A && CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_AARCH32_ARMV8_A`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_A)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_AARCH32_ARMV8_R"></a>

## 29.3 `CONFIG_AARCH32_ARMV8_R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv8-R AArch32 处理器实现。根据 [Arm R-profile 架构说明](https://developer.arm.com/products/architecture/cpu-architecture/r-profile)，Armv8-R 面向实时处理器体系（Real-time Profile），在最高安全级别引入虚拟化（Virtualization），同时保留基于内存保护单元（MPU）的受保护内存系统架构（Protected Memory System Architecture，PMSA），支持 A32 和 T32 指令集。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_ARCH_HAS_DIRECTED_IPIS
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R52
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L252)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_CPU_CORTEX_R52`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52)。

<a id="CONFIG_ARCH_HAS_STACKWALK"></a>

## 29.4 `CONFIG_ARCH_HAS_STACKWALK`

原库同名定义共 5 条；本项为数据库第 499 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，表示已实现 `arch_stack_walk()` API，且可以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_EXTRA_EXCEPTION_INFO && CONFIG_CPU_CORTEX_M
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L259)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_EXTRA_EXCEPTION_INFO`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_EXTRA_EXCEPTION_INFO)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)。

<a id="CONFIG_ARMV5"></a>

## 29.5 `CONFIG_ARMV5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv5 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV5T
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV5T`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5T)。

<a id="CONFIG_ARMV5T"></a>

## 29.6 `CONFIG_ARMV5T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv5T CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV5
```

**被选择（Selected by）**

```text
CONFIG_ARMV5TE
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5)、[`CONFIG_ARMV5TE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5TE)。

<a id="CONFIG_ARMV5TE"></a>

## 29.7 `CONFIG_ARMV5TE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv5TE CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV5T
```

**被选择（Selected by）**

```text
CONFIG_ARMV5TEJ
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV5T`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5T)、[`CONFIG_ARMV5TEJ`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5TEJ)。

<a id="CONFIG_ARMV5TEJ"></a>

## 29.8 `CONFIG_ARMV5TEJ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv5TEJ CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV5TE
```

**被选择（Selected by）**

```text
CONFIG_CPU_ARM926EJ_S
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV5TE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5TE)、[`CONFIG_CPU_ARM926EJ_S`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_ARM926EJ_S)。

<a id="CONFIG_ARMV5_EXCEPTION_STACK_SIZE"></a>

## 29.9 `CONFIG_ARMV5_EXCEPTION_STACK_SIZE`

**提示（Prompt）**：未定义指令与中止异常栈大小（Undefined Instruction and Abort Stack Size，字节）

**说明（Help）**

此选项指定未定义指令（Undefined Instruction）和数据中止（Data Abort）异常处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV5 && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV5_FIQ_STACK_SIZE"></a>

## 29.10 `CONFIG_ARMV5_FIQ_STACK_SIZE`

**提示（Prompt）**：快速中断栈大小（FIQ Stack Size，字节）

**说明（Help）**

此选项指定快速中断（FIQ）处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV5 && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV5_SVC_STACK_SIZE"></a>

## 29.11 `CONFIG_ARMV5_SVC_STACK_SIZE`

**提示（Prompt）**：监管者模式栈大小（SVC Stack Size，字节）

**说明（Help）**

此选项指定 SVC 处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV5 && CONFIG_ARM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV5_SYS_STACK_SIZE"></a>

## 29.12 `CONFIG_ARMV5_SYS_STACK_SIZE`

**提示（Prompt）**：系统模式栈大小（SYS Stack Size，字节）

**说明（Help）**

此选项指定系统模式（System Mode）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV5 && CONFIG_ARM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV6_M_ARMV8_M_BASELINE"></a>

## 29.13 `CONFIG_ARMV6_M_ARMV8_M_BASELINE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv6-M 处理器实现，或支持基线实现（Baseline Implementation）的 ARMv8-M 处理器。

注意：不包含主扩展（Main Extension）的处理单元（Processing Element，PE）也称为基线实现，其指令、寄存器和功能均为主线实现（Mainline Implementation）的子集。所有 ARMv8-M 实现均提供 ARMv6-M 兼容性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN if CONFIG_ARMV8_M_BASELINE
CONFIG_ATOMIC_OPERATIONS_C if !CONFIG_ARMV8_M_BASELINE
CONFIG_ISA_THUMB2
CONFIG_ARCH_HAS_LLEXT_VENEERS
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M0
CONFIG_CPU_CORTEX_M0PLUS
CONFIG_CPU_CORTEX_M1
CONFIG_ARMV8_M_BASELINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_ATOMIC_OPERATIONS_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_ISA_THUMB2`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_THUMB2)、[`CONFIG_ARCH_HAS_LLEXT_VENEERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_LLEXT_VENEERS)、[`CONFIG_CPU_CORTEX_M0`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0)、[`CONFIG_CPU_CORTEX_M0PLUS`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0PLUS)、[`CONFIG_CPU_CORTEX_M1`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_LLEXT_VENEERS`。

<a id="CONFIG_ARMV7_A_NS"></a>

## 29.14 `CONFIG_ARMV7_A_NS`

**提示（Prompt）**：ARMv7-A 非安全状态（Non-Secure State，即 TrustZone 非安全世界）

**说明（Help）**

Zephyr 在 ARMv7-A 内核的 ARM TrustZone 非安全状态（Non-Secure State）下运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_A && CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`。

<a id="CONFIG_ARMV7_EXCEPTION_STACK_SIZE"></a>

## 29.15 `CONFIG_ARMV7_EXCEPTION_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 624 条记录，各定义分别保留。

**提示（Prompt）**：未定义指令与中止异常栈大小（Undefined Instruction and Abort Stack Size，字节）

**说明（Help）**

此选项指定未定义指令（Undefined Instruction）和数据中止（Data Abort）异常处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_EXCEPTION_STACK_SIZE--record-625"></a>

## 29.16 `CONFIG_ARMV7_EXCEPTION_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 625 条记录，各定义分别保留。

**提示（Prompt）**：未定义指令与中止异常栈大小（Undefined Instruction and Abort Stack Size，字节）

**说明（Help）**

此选项指定未定义指令（Undefined Instruction）和数据中止（Data Abort）异常处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_FIQ_STACK_SIZE"></a>

## 29.17 `CONFIG_ARMV7_FIQ_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 626 条记录，各定义分别保留。

**提示（Prompt）**：快速中断栈大小（FIQ Stack Size，字节）

**说明（Help）**

此选项指定快速中断（FIQ）处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_FIQ_STACK_SIZE--record-627"></a>

## 29.18 `CONFIG_ARMV7_FIQ_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 627 条记录，各定义分别保留。

**提示（Prompt）**：快速中断栈大小（FIQ Stack Size，字节）

**说明（Help）**

此选项指定快速中断（FIQ）处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L274)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_M_ARMV8_M_FP"></a>

## 29.19 `CONFIG_ARMV7_M_ARMV8_M_FP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv7-M 处理器实现，或支持浮点扩展（Floating-Point Extension）的 ARMv8-M 处理器实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE && !CONFIG_CPU_CORTEX_M3 && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M4
CONFIG_CPU_CORTEX_M33
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
CONFIG_CPU_CORTEX_M7
```

**弱选择（Implies）**

```text
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M3`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M3)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M4`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M4)、[`CONFIG_CPU_CORTEX_M33`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M33)、[`CONFIG_CPU_CORTEX_M52`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

<a id="CONFIG_ARMV7_M_ARMV8_M_MAINLINE"></a>

## 29.20 `CONFIG_ARMV7_M_ARMV8_M_MAINLINE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv7-M 处理器实现，或支持主扩展（Main Extension）、具备向后兼容性的 ARMv8-M 处理器实现。

注意：具有主扩展的处理单元（Processing Element，PE）也称为主线实现（Mainline Implementation）；ARMv7-M 兼容性要求具有主扩展。根据 [Arm M-profile 架构说明](https://developer.arm.com/products/architecture/m-profile)，主扩展提供与 ARMv7-M 的向后兼容性。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ISA_THUMB2
CONFIG_CPU_CORTEX_M_HAS_BASEPRI
CONFIG_CPU_CORTEX_M_HAS_VTOR
CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS
CONFIG_CPU_CORTEX_M_HAS_SYSTICK
CONFIG_USE_SWITCH_SUPPORTED if !CONFIG_TRUSTED_EXECUTION_NONSECURE
CONFIG_ARCH_HAS_LLEXT_VENEERS
CONFIG_ARCH_HAS_BIT_REV
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M3
CONFIG_CPU_CORTEX_M4
CONFIG_CPU_CORTEX_M7
CONFIG_ARMV8_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ISA_THUMB2`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_THUMB2)、[`CONFIG_CPU_CORTEX_M_HAS_BASEPRI`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_BASEPRI)、[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS)、[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_ARCH_HAS_LLEXT_VENEERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_LLEXT_VENEERS)、[`CONFIG_ARCH_HAS_BIT_REV`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_BIT_REV)、[`CONFIG_CPU_CORTEX_M3`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M3)、[`CONFIG_CPU_CORTEX_M4`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M4)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_LLEXT_VENEERS`。

<a id="CONFIG_ARMV7_R"></a>

## 29.21 `CONFIG_ARMV7_R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv7-R 处理器实现。根据 [Arm R-profile 架构说明](https://developer.arm.com/products/architecture/cpu-architecture/r-profile)，Armv7-R 实现具有多种模式的传统 Arm 架构，支持基于内存保护单元（MPU）的受保护内存系统架构（Protected Memory System Architecture，PMSA），以及 Arm（32）和 Thumb（T32）指令集。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ISA_ARM
CONFIG_ISA_THUMB2
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R4
CONFIG_CPU_CORTEX_R5
CONFIG_CPU_CORTEX_R7
CONFIG_CPU_CORTEX_R8
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ISA_ARM`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_ARM)、[`CONFIG_ISA_THUMB2`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_THUMB2)、[`CONFIG_CPU_CORTEX_R4`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R4)、[`CONFIG_CPU_CORTEX_R5`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R5)、[`CONFIG_CPU_CORTEX_R7`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R7)、[`CONFIG_CPU_CORTEX_R8`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R8)。

<a id="CONFIG_ARMV7_R_FP"></a>

## 29.22 `CONFIG_ARMV7_R_FP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持浮点扩展（Floating-Point Extension）的 ARMv7-R 处理器实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_R && CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R4
CONFIG_CPU_CORTEX_R5
CONFIG_CPU_CORTEX_R7
CONFIG_CPU_CORTEX_R8
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_R`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_R)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_R4`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R4)、[`CONFIG_CPU_CORTEX_R5`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R5)、[`CONFIG_CPU_CORTEX_R7`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R7)、[`CONFIG_CPU_CORTEX_R8`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R8)。

<a id="CONFIG_ARMV7_SVC_STACK_SIZE"></a>

## 29.23 `CONFIG_ARMV7_SVC_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 632 条记录，各定义分别保留。

**提示（Prompt）**：监管者模式栈大小（SVC Stack Size，字节）

**说明（Help）**

此选项指定 SVC 处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_SVC_STACK_SIZE--record-633"></a>

## 29.24 `CONFIG_ARMV7_SVC_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 633 条记录，各定义分别保留。

**提示（Prompt）**：监管者模式栈大小（SVC Stack Size，字节）

**说明（Help）**

此选项指定 SVC 处理程序使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_SYS_STACK_SIZE"></a>

## 29.25 `CONFIG_ARMV7_SYS_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 634 条记录，各定义分别保留。

**提示（Prompt）**：系统模式栈大小（SYS Stack Size，字节）

**说明（Help）**

此选项指定系统模式（System Mode）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV7_SYS_STACK_SIZE--record-635"></a>

## 29.26 `CONFIG_ARMV7_SYS_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 635 条记录，各定义分别保留。

**提示（Prompt）**：系统模式栈大小（SYS Stack Size，字节）

**说明（Help）**

此选项指定系统模式（System Mode）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_R && CONFIG_ARM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV8_1_M_MAINLINE"></a>

## 29.27 `CONFIG_ARMV8_1_M_MAINLINE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持主扩展（Main Extension）的 ARMv8.1-M 处理器实现。ARMv8.1-M 主扩展包含 ARMv8-M 架构中没有的附加功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV8_M_MAINLINE
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L261)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M52`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)。

<a id="CONFIG_ARMV8_1_M_MVEF"></a>

## 29.28 `CONFIG_ARMV8_1_M_MVEF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持 M-profile 向量扩展（M-Profile Vector Extension，MVE）浮点指令集的 ARMv8.1-M 处理器实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_1_M_MVEI && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_R7KA8P1KFLCAC_CM85
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_PSE84_M55
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_MVEI`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MVEI)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_PSE84_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M55)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`、`CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_SERIES_PSE84_M55`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_ARMV8_1_M_MVEI"></a>

## 29.29 `CONFIG_ARMV8_1_M_MVEI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持 M-profile 向量扩展（M-Profile Vector Extension，MVE）整数指令集的 ARMv8.1-M 处理器实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_1_M_MAINLINE && CONFIG_ARMV8_M_DSP && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_R7KA8P1KFLCAC_CM85
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_PSE84_M55
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L296)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARMV8_M_DSP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_DSP)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_PSE84_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M55)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`、`CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_SERIES_PSE84_M55`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_ARMV8_1_M_PMU"></a>

## 29.30 `CONFIG_ARMV8_1_M_PMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 实现 ARMv8-M 性能监测单元（Performance Monitoring Unit，PMU）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L312)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_ARMV8_M_BASELINE"></a>

## 29.31 `CONFIG_ARMV8_M_BASELINE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv8-M 处理器实现。ARMv8-M 基线实现（Baseline）包含 ARMv6-M 架构中没有的附加功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV6_M_ARMV8_M_BASELINE
CONFIG_CPU_CORTEX_M_HAS_CMSE
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M23
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L212)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_CPU_CORTEX_M_HAS_CMSE`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_CMSE)、[`CONFIG_CPU_CORTEX_M23`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M23)。

<a id="CONFIG_ARMV8_M_DSP"></a>

## 29.32 `CONFIG_ARMV8_M_DSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持 DSP 扩展（DSP Extension）的 ARMv8-M 处理器实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_M_MAINLINE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_AM13E23019
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S26
CONFIG_SOC_LPC55S28
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_SR100
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
CONFIG_SOC_SERIES_MCXA1X6
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_MCXW2XX
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L05_CPUAPP
CONFIG_SOC_NRF54L10_CPUAPP
CONFIG_SOC_NRF54L15_CPUAPP
CONFIG_SOC_NRF54LM20A_CPUAPP
CONFIG_SOC_NRF54LM20B_CPUAPP
CONFIG_SOC_NRF54LV10A_CPUAPP
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_AN521_CPU1
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
CONFIG_SOC_MUSCA_S1
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:289`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L289)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S26)、[`CONFIG_SOC_LPC55S28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S28)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_MCXA1X6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X6)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L05_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_AN521_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521_CPU1)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S26`、`CONFIG_SOC_LPC55S28`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_MCXA1X6`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_MCXW2XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_ARMV8_M_MAINLINE"></a>

## 29.33 `CONFIG_ARMV8_M_MAINLINE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持主扩展（Main Extension）的 ARMv8-M 处理器实现。ARMv8-M 主扩展包含 ARMv7-M 架构中没有的附加功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_CPU_CORTEX_M_HAS_SPLIM
CONFIG_CPU_CORTEX_M_HAS_CMSE
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M33
CONFIG_ARMV8_1_M_MAINLINE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L249)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M_HAS_SPLIM`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SPLIM)、[`CONFIG_CPU_CORTEX_M_HAS_CMSE`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_CMSE)、[`CONFIG_CPU_CORTEX_M33`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M33)、[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)。

<a id="CONFIG_ARMV8_M_PMU_EVENTCNT"></a>

## 29.34 `CONFIG_ARMV8_M_PMU_EVENTCNT`

**提示（Prompt）**：性能监测单元中的事件计数器数量（Number of Event Counters）

**说明（Help）**

已实现的事件计数器（Event Counter）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_1_M_PMU && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_PMU`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_PMU)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARMV8_M_SE"></a>

## 29.35 `CONFIG_ARMV8_M_SE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用支持安全扩展（Security Extensions）的 ARMv8-M 处理器实现，可以是基线（Baseline）或主线（Mainline）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV8_M_BASELINE || CONFIG_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M_HAS_SPLIM if !CONFIG_ARM_NONSECURE_FIRMWARE
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M23
CONFIG_CPU_CORTEX_M33
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L271)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M_HAS_SPLIM`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SPLIM)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_CPU_CORTEX_M23`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M23)、[`CONFIG_CPU_CORTEX_M33`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M33)、[`CONFIG_CPU_CORTEX_M52`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)。

<a id="CONFIG_ARM_AARCH32_MMU"></a>

## 29.36 `CONFIG_ARM_AARCH32_MMU`

**提示（Prompt）**：ARM 内存管理单元（MMU）支持

**说明（Help）**

当前 CPU 具有 ARMv5 或 ARMv7 内存管理单元（Memory Management Unit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MMU && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_MMU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_THREAD_STACK_INFO
CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CYCLONEV
CONFIG_ARM_AARCH32_MMU_VMSA_V5
CONFIG_ARM_AARCH32_MMU_VMSA_V7
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)、[`CONFIG_ARM_AARCH32_MMU_VMSA_V5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_VMSA_V5)、[`CONFIG_ARM_AARCH32_MMU_VMSA_V7`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_VMSA_V7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`。

<a id="CONFIG_ARM_AARCH32_MMU_TYPE"></a>

## 29.37 `CONFIG_ARM_AARCH32_MMU_TYPE`

**提示（Prompt）**：内存管理单元类型（MMU Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MMU && CONFIG_ARM
```

**默认值（Defaults）**

```text
CONFIG_ARM_AARCH32_MMU_VMSA_V5 if CONFIG_CPU_AARCH32_ARM9
CONFIG_ARM_AARCH32_MMU_VMSA_V7 if CONFIG_CPU_AARCH32_CORTEX_A
```

**可选项（Choices）**

```text
CONFIG_ARM_AARCH32_MMU_VMSA_V5
CONFIG_ARM_AARCH32_MMU_VMSA_V7
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM_AARCH32_MMU_VMSA_V5`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_VMSA_V5)、[`CONFIG_CPU_AARCH32_ARM9`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_ARM9)、[`CONFIG_ARM_AARCH32_MMU_VMSA_V7`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_VMSA_V7)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)。

<a id="CONFIG_ARM_AARCH32_MMU_VMSA_V5"></a>

## 29.38 `CONFIG_ARM_AARCH32_MMU_VMSA_V5`

**提示（Prompt）**：ARMv5 内存管理单元（MMU）支持

**说明（Help）**

当前 CPU 具有 ARMv5 内存管理单元（Memory Management Unit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_AARCH32_MMU_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_ARM_AARCH32_MMU
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 内存管理单元类型（MMU Type）

**配置项引用（Symbol References）**：[`CONFIG_ARM_AARCH32_MMU_TYPE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_TYPE)、[`CONFIG_ARM_AARCH32_MMU`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU)。

<a id="CONFIG_ARM_AARCH32_MMU_VMSA_V7"></a>

## 29.39 `CONFIG_ARM_AARCH32_MMU_VMSA_V7`

**提示（Prompt）**：ARMv7 Cortex-A 内存管理单元（MMU）支持

**说明（Help）**

当前 CPU 具有 ARMv7 内存管理单元（Memory Management Unit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_AARCH32_MMU_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_ARM_AARCH32_MMU
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 内存管理单元类型（MMU Type）

**配置项引用（Symbol References）**：[`CONFIG_ARM_AARCH32_MMU_TYPE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU_TYPE)、[`CONFIG_ARM_AARCH32_MMU`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU)。

<a id="CONFIG_ARM_A_PROFILE_AARCH32"></a>

## 29.40 `CONFIG_ARM_A_PROFILE_AARCH32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为所有运行于 AArch32 执行状态（Execution State）的 ARM A-profile 处理器，即 ARMv7-A 或 ARMv8-A AArch32，启用的能力标志（Capability Flag）。用户不能直接选择此项，由 A-profile AArch32 架构符号选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH32_CORTEX_A && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_ARMV7_A
CONFIG_AARCH32_ARMV8_A
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_AARCH32_ARMV8_A`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`。

<a id="CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER"></a>

## 29.41 `CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`

原库同名定义共 2 条；本项为数据库第 657 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 ARM CPU 连接到自定义中断控制器（Custom Interrupt Controller），即不是 GIC 或 NVIC。部分 Cortex-A 和 Cortex-R 内核，例如 Cortex-A5、Cortex-R4/5 等，允许连接自定义外部中断控制器；若连接的不是 ARM 通用中断控制器（GIC），也不是 Cortex-M 的 ARM 嵌套向量中断控制器（NVIC），就必须选择此项。选择后，架构中断控制函数映射到由 SoC 层实现的中断控制接口（Interrupt Control Interface）。

注意：所有 Cortex-M 内核都具有 NVIC，因此若选择此项，就假定自定义中断控制接口负责处理 NVIC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_SOC_BCM2710
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
```

**定义位置（Location）**：[`arch/arm/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_BCM2710`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2710)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BCM2710`。

<a id="CONFIG_ARM_ENTRY_VENEERS_LIB_NAME"></a>

## 29.42 `CONFIG_ARM_ENTRY_VENEERS_LIB_NAME`

**提示（Prompt）**：入口跳板符号文件（Entry Veneers Symbol File）

**说明（Help）**

用于查找入口跳板（Entry Veneer）符号表（Symbol Table）的库文件。通常来自包含安全入口函数（Secure Entry Functions）的安全固件构建，使非安全固件能够调用安全固件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS || CONFIG_ARM_FIRMWARE_USES_SECURE_ENTRY_FUNCS) && (CONFIG_ARM_SECURE_FIRMWARE || CONFIG_ARM_NONSECURE_FIRMWARE) && CONFIG_ARM_TRUSTZONE_M && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
"libentryveneers.a"
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM TrustZone-M 支持 → ARM TrustZone-M 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS)、[`CONFIG_ARM_FIRMWARE_USES_SECURE_ENTRY_FUNCS`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_FIRMWARE_USES_SECURE_ENTRY_FUNCS)、[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS"></a>

## 29.43 `CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS`

**提示（Prompt）**：安全固件具有安全入口函数（Secure Entry Functions）

**说明（Help）**

此选项表示 ARM 安全固件（Secure Firmware）包含可从非安全状态（Non-Secure State）调用的安全入口函数。这些函数必须位于非安全可调用内存区域（Non-Secure Callable Memory Regions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SECURE_FIRMWARE && (CONFIG_ARM_SECURE_FIRMWARE || CONFIG_ARM_NONSECURE_FIRMWARE) && CONFIG_ARM_TRUSTZONE_M && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM TrustZone-M 支持 → ARM TrustZone-M 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_FIRMWARE_USES_SECURE_ENTRY_FUNCS"></a>

## 29.44 `CONFIG_ARM_FIRMWARE_USES_SECURE_ENTRY_FUNCS`

**提示（Prompt）**：非安全固件使用安全入口函数（Secure Entry Functions）

**说明（Help）**

此选项表示 ARM 非安全固件（Non-Secure Firmware）使用安全固件提供的安全入口函数（Secure Entry Functions）。安全固件必须配置为提供这些函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_NONSECURE_FIRMWARE && (CONFIG_ARM_SECURE_FIRMWARE || CONFIG_ARM_NONSECURE_FIRMWARE) && CONFIG_ARM_TRUSTZONE_M && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM TrustZone-M 支持 → ARM TrustZone-M 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_FP_CLOBBER_WORKAROUND"></a>

## 29.45 `CONFIG_ARM_FP_CLOBBER_WORKAROUND`

**提示（Prompt）**：帧指针破坏规避措施（Frame Pointer Clobber Workaround）

**说明（Help）**

启用由两条指令组成的规避措施，解决 GNU 和 Clang 工具链中内联汇编（Inline Assembly）不能声明破坏帧指针（Frame Pointer Clobber）的限制。大多数代码不需要此项，但如果内核使用 `-fno-omit-frame-pointer` 编译，或使用要求 `sched.c` 动态分配栈空间的红黑树调度队列（Red-black Tree Scheduler Queue），则必须启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SWITCH && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_FRAME_POINTER
y if CONFIG_SCHED_SCALABLE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:526`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L526)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_FRAME_POINTER`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FRAME_POINTER)、[`CONFIG_SCHED_SCALABLE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_SCALABLE)。

<a id="CONFIG_ARM_MMU_NUM_L2_TABLES"></a>

## 29.46 `CONFIG_ARM_MMU_NUM_L2_TABLES`

**提示（Prompt）**：MMU 可用的二级转换表数量（Number of L2 Translation Tables）

**说明（Help）**

二级转换表（Level 2 Translation Table）的数量，每个表覆盖 1 MB 地址空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_AARCH32_MMU && CONFIG_CPU_HAS_MMU && CONFIG_ARM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_AARCH32_MMU`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_AARCH32_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_MMU_REGION_MIN_ALIGN_AND_SIZE"></a>

## 29.47 `CONFIG_ARM_MMU_REGION_MIN_ALIGN_AND_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM MMU 页面的最小大小及对齐（Minimum Size and Alignment）。不应修改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MMU && CONFIG_ARM
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/arm/core/mmu/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mmu/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_MPU_CM7_UNMAPPED_REGION"></a>

## 29.48 `CONFIG_ARM_MPU_CM7_UNMAPPED_REGION`

**提示（Prompt）**：为未映射地址设置兜底的禁止访问 MPU 区域（Catch-all No-access Region）

**说明（Help）**

将最低优先级 MPU 区域，即区域 `0`，配置为覆盖整个地址空间的 4 GB 强序（Strongly-ordered）、禁止访问（No-access）、禁止执行（Execute-Never）区域。显式配置的 MPU 区域使用更高编号，因此优先于该区域。Cortex-M7 可以推测访问（Speculative Access）任何未映射为禁止执行的地址，参见 Arm Cortex-M7 技术参考手册的“内存系统—推测访问（Memory System - Speculative Accesses）”；即便某地址的加载会导致故障，`PLD` 指令也可能对其执行缓存行填充（Cache Linefill），这是存在于所有 M7 修订版的勘误 1013783，编号 SDEN-1068427。此兜底区域通过消除 MPU 映射中的所有未映射空洞，实现推荐的规避措施。

警告：配置此区域后，`PRIVDEFENA` 背景映射将永不生效，因此开发板或 SoC 的静态 MPU 区域表必须显式覆盖固件访问的每个地址范围，包括代码、RAM 和外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M7 && CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_MPU_DISABLE_BACKGROUND_MAP
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_MPU_DISABLE_BACKGROUND_MAP`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_DISABLE_BACKGROUND_MAP)。

<a id="CONFIG_ARM_MPU_PXN"></a>

## 29.49 `CONFIG_ARM_MPU_PXN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Armv8.1-M MPU 的特权禁止执行（Privileged Execute Never，PXN）属性支持。标记 PXN 的 MPU 区域只能从非特权模式（Unprivileged Mode）执行；从特权模式执行该区域会引发内存管理故障（Memory Management Fault）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_1_M_MAINLINE && CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE"></a>

## 29.50 `CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE`

原库同名定义共 2 条；本项为数据库第 669 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM MPU 区域的最小大小及对齐（Minimum Size and Alignment）。使用此符号保证 MPU 区域满足最小大小和对齐要求。没有内存保护支持的 ARM 构建也强制采用至少 4 字节对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**默认值（Defaults）**

```text
256 if CONFIG_ARM_MPU && CONFIG_ARMV6_M_ARMV8_M_BASELINE && !CONFIG_ARMV8_M_BASELINE
128 if CONFIG_ARM_MPU && CONFIG_FPU_SHARING && CONFIG_MPU_STACK_GUARD
64 if CONFIG_ARM_MPU && CONFIG_AARCH32_ARMV8_R
32 if CONFIG_ARM_MPU
4
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_AARCH32_ARMV8_R`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_R)。

<a id="CONFIG_ARM_MPU_SKIP_ARCH_INIT"></a>

## 29.51 `CONFIG_ARM_MPU_SKIP_ARCH_INIT`

**提示（Prompt）**：跳过 MPU 初始化（Initialization）

**说明（Help）**

如果早期启动代码，例如驻留在紧耦合存储器（TCM）中的引导桩，已经在内核运行前启用并配置 MPU，请选择此项。`z_arm_mpu_init()` 会跳过重新编程，因为如果当前执行区域只有在 MPU 启用时才可访问，禁用 MPU 就会导致故障。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_VERSAL_RPU_OCM_BOOT
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_VERSAL_RPU_OCM_BOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU_OCM_BOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_VERSAL_RPU_OCM_BOOT`。

<a id="CONFIG_ARM_MPU_SRAM_WRITE_THROUGH"></a>

## 29.52 `CONFIG_ARM_MPU_SRAM_WRITE_THROUGH`

**提示（Prompt）**：为 SRAM 区域使用写穿透缓存策略（Write-Through Cache Policy）

**说明（Help）**

启用后，SRAM 区域使用写穿透（Write-Through）缓存策略，代替默认的写回（Write-Back）策略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/mpu/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/mpu/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_NONSECURE_FIRMWARE"></a>

## 29.53 `CONFIG_ARM_NONSECURE_FIRMWARE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示构建的 Zephyr 镜像将在非安全状态（Non-Secure State）执行，其执行由安全状态（Secure State）下运行的安全固件触发。仅适用于实现安全扩展（Security Extension）的 ARMv8-M MCU。启用后，Zephyr 包含仅在非安全状态执行的代码，并排除仅为安全状态设计的代码。非安全代码无权访问 Cortex-M MCU 的安全资源（Secure Resources），因此必须避免访问这些资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARM_SECURE_FIRMWARE && CONFIG_ARMV8_M_SE && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_NONSECURE
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L287)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)。

<a id="CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS"></a>

## 29.54 `CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS`

**提示（Prompt）**：允许抢占安全函数调用（Secure Function Calls）

**说明（Help）**

启用后，表示正在执行安全函数调用（Secure Function Call）的可抢占 Zephyr 线程允许被抢占（Preempt）。禁用后，这些线程在执行安全函数调用期间不得被上下文切换出去。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_NONSECURE_FIRMWARE && CONFIG_ARM
```

**被弱选择（Implied by）**

```text
CONFIG_BUILD_WITH_TFM
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_ARM_NSC_REGION_BASE_ADDRESS"></a>

## 29.55 `CONFIG_ARM_NSC_REGION_BASE_ADDRESS`

**提示（Prompt）**：ARM 非安全可调用区域基地址（Non-Secure Callable Region Base Address）

**说明（Help）**

非安全可调用段（Non-Secure Callable Section）的起始地址。

注意：未显式配置此选项时，默认值指示链接脚本将该段自动放入 `.text` 区域。根据 SoC 可用的安全属性单元（SAU 或 IDAU），非安全可调用段的大小和起始地址对齐可能受到特定要求或限制。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS && (CONFIG_ARM_SECURE_FIRMWARE || CONFIG_ARM_NONSECURE_FIRMWARE) && CONFIG_ARM_TRUSTZONE_M && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM TrustZone-M 支持 → ARM TrustZone-M 选项（Options） → 安全固件具有安全入口函数（Secure Entry Functions）

**配置项引用（Symbol References）**：[`CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_FIRMWARE_HAS_SECURE_ENTRY_FUNCS)、[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK"></a>

## 29.56 `CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用钩子 `z_arm_on_enter_cpu_idle()`，在通过 `k_cpu_idle()` 或 `k_cpu_atomic_idle()` 使 CPU 空闲时调用。必要时，可通过该钩子跳过 `WFE/WFI` 指令，阻止 CPU 实际进入休眠（Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND
CONFIG_SOC_NRF53_RTC_PRETICK
```

**被弱选择（Implied by）**

```text
CONFIG_MAX32_ON_ENTER_CPU_IDLE_HOOK
CONFIG_RTS5912_ON_ENTER_CPU_IDLE_HOOK
CONFIG_LOG_FRONTEND_STMESP
```

**定义位置（Location）**：[`arch/arm/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND)、[`CONFIG_SOC_NRF53_RTC_PRETICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_RTC_PRETICK)、[`CONFIG_MAX32_ON_ENTER_CPU_IDLE_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX32_ON_ENTER_CPU_IDLE_HOOK)、[`CONFIG_RTS5912_ON_ENTER_CPU_IDLE_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTS5912_ON_ENTER_CPU_IDLE_HOOK)、[`CONFIG_LOG_FRONTEND_STMESP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF53_ANOMALY_160_WORKAROUND`。

<a id="CONFIG_ARM_ON_ENTER_CPU_IDLE_PREPARE_HOOK"></a>

## 29.57 `CONFIG_ARM_ON_ENTER_CPU_IDLE_PREPARE_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用钩子 `z_arm_on_enter_cpu_idle_prepare()`，在通过 `k_cpu_idle()` 或 `k_cpu_atomic_idle()` 使 CPU 空闲时调用。必要时，该钩子可为即将调用的 `z_arm_on_enter_cpu_idle()` 准备数据。两者区别是 `z_arm_on_enter_cpu_idle_prepare` 在禁用中断之前调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF53_RTC_PRETICK
```

**定义位置（Location）**：[`arch/arm/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_NRF53_RTC_PRETICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_RTC_PRETICK)。

<a id="CONFIG_ARM_ON_EXIT_CPU_IDLE"></a>

## 29.58 `CONFIG_ARM_ON_EXIT_CPU_IDLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

允许在 CPU 空闲实现中的 `WFI/WFE` 指令之后立即插入 SoC 专用代码。启用后，要求 SoC 提供 `soc_cpu_idle.h` 头文件，在 `_ASMLANGUAGE` 条件保护下定义 `SOC_ON_EXIT_CPU_IDLE` 宏。该宏紧接 `WFI/WFE` 指令展开，在任何内存访问发生之前执行，用于缓解某些 SoC 上 `WFI/WFE` 之后的内存访问引起的问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF5340_CPUNET
CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND
CONFIG_SOC_SERIES_AMEBAD
```

**定义位置（Location）**：[`arch/arm/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_ANOMALY_168_WORKAROUND)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUNET`、`CONFIG_SOC_SERIES_AMEBAD`。

<a id="CONFIG_ARM_SECURE_BUSFAULT_HARDFAULT_NMI"></a>

## 29.59 `CONFIG_ARM_SECURE_BUSFAULT_HARDFAULT_NMI`

**提示（Prompt）**：BusFault、HardFault 和 NMI 以安全状态（Secure State）为目标

**说明（Help）**

强制将 NMI、HardFault，以及 ARMv8-M 主线（Mainline）中的 BusFault，作为安全异常（Secure Exceptions）处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SECURE_FIRMWARE && (CONFIG_ARM_SECURE_FIRMWARE || CONFIG_ARM_NONSECURE_FIRMWARE) && CONFIG_ARM_TRUSTZONE_M && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_TEST_ARM_CORTEX_M
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM TrustZone-M 支持 → ARM TrustZone-M 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_TEST_ARM_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_ARM_CORTEX_M)。

<a id="CONFIG_ARM_SECURE_FIRMWARE"></a>

## 29.60 `CONFIG_ARM_SECURE_FIRMWARE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示构建的 Zephyr 镜像将在安全状态（Secure State）执行，仅适用于实现安全扩展（Security Extension）的 ARMv8-M MCU。启用后，Zephyr 包含安全状态代码，并排除仅为非安全状态（Non-Secure State）设计的代码。安全状态代码可以访问 Cortex-M MCU 的安全资源和非安全资源。非安全代码访问 MCU 安全资源时，可能触发安全故障（Secure Fault），只能由安全状态代码处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV8_M_SE && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_TRUSTED_EXECUTION_SECURE
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_TRUSTED_EXECUTION_SECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_SECURE)。

<a id="CONFIG_ARM_STACK_PROTECTION"></a>

## 29.61 `CONFIG_ARM_STACK_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用以下两种机制之一：内置栈指针边界检查（Stack Pointer Limit Checking），或基于 MPU 的栈保护区（Stack Guard）。当前进程栈超出边界时，将触发系统致命错误（System Fatal Error）。两种栈保护选项互斥，优先选择内置栈指针边界检查；开发者仍可根据需要手动选择基于 MPU 的栈保护区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_MPU_STACK_GUARD if !CONFIG_BUILTIN_STACK_GUARD && CONFIG_ARM_MPU
```

**弱选择（Implies）**

```text
CONFIG_BUILTIN_STACK_GUARD if CONFIG_CPU_CORTEX_M_HAS_SPLIM
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_BUILTIN_STACK_GUARD`](P029_arch_arm_配置项参考_1.md#CONFIG_BUILTIN_STACK_GUARD)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_CORTEX_M_HAS_SPLIM`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SPLIM)。

<a id="CONFIG_ARM_STORE_EXC_RETURN"></a>

## 29.62 `CONFIG_ARM_STORE_EXC_RETURN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

切换线程时保存 `EXC_RETURN` 值。当线程的 FPU 使用情况或安全域（Security Domain）不同时，需要此值进行切换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_CORTEX_M && (CONFIG_FPU_SHARING || CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS)
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS)。

<a id="CONFIG_ARM_TRACK_ACTIVE_IRQ"></a>

## 29.63 `CONFIG_ARM_TRACK_ACTIVE_IRQ`

**提示（Prompt）**：在 ISR 包装函数中跟踪活动 IRQ（Active IRQ）

**说明（Help）**

在 Cortex-A/R 上提供 `k_irq_get_active()`。GIC 没有寄存器能够在应答（Acknowledge）后报告正在处理的中断 ID（INTID），因此 ISR 包装函数按 CPU 记录该信息，代价是每次中断进入和退出时增加几条指令。兼容 GIC 和自定义中断控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CPU_AARCH32_CORTEX_A || CONFIG_CPU_AARCH32_CORTEX_R) && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_IRQ_GET_ACTIVE
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARCH_HAS_IRQ_GET_ACTIVE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_GET_ACTIVE)。

<a id="CONFIG_ARM_TRUSTZONE_M"></a>

## 29.64 `CONFIG_ARM_TRUSTZONE_M`

**提示（Prompt）**：ARM TrustZone-M 支持

**说明（Help）**

平台支持 ARM TrustZone-M。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_TEE && CONFIG_ARMV8_M_SE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_SERIES_PSE84_M33
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/tz/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/tz/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_SERIES_PSE84_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M33)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_SERIES_PSE84_M33`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_ARM_VECTOR_TABLE_DTCM"></a>

## 29.65 `CONFIG_ARM_VECTOR_TABLE_DTCM`

**提示（Prompt）**：将向量表放入设备树 chosen 指定的 DTCM，而非 Flash

**说明（Help）**

启用就地执行（XiP）时，此选项将中断向量表从设备树 `zephyr,flash` chosen 指定的内存，重定位到 `zephyr,dtcm` chosen 指定的内存。虽然异常进入时会以指令获取方式读取向量表，但仍为没有指令紧耦合存储器（ITCM）的系统提供数据紧耦合存储器（DTCM）选项。相较普通 RAM，DTCM 仍能提供低延迟、确定性访问，但并不是指令获取性能最优的位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`arch/arm/Kconfig:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L213)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 向量表内存位置（Vector Table Memory Location）

<a id="CONFIG_ARM_VECTOR_TABLE_ITCM"></a>

## 29.66 `CONFIG_ARM_VECTOR_TABLE_ITCM`

**提示（Prompt）**：将向量表放入设备树 chosen 指定的 ITCM，而非 Flash

**说明（Help）**

启用就地执行（XiP）时，此选项将中断向量表从设备树 `zephyr,flash` chosen 指定的内存，重定位到 `zephyr,itcm` chosen 指定的内存。指令紧耦合存储器（ITCM）通过 CPU 指令总线提供单周期、确定性的指令获取，具有最低中断延迟，可用时应优先选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`arch/arm/Kconfig:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L225)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 向量表内存位置（Vector Table Memory Location）

<a id="CONFIG_ARM_VECTOR_TABLE_SRAM"></a>

## 29.67 `CONFIG_ARM_VECTOR_TABLE_SRAM`

**提示（Prompt）**：将向量表放入设备树 chosen 指定的 SRAM，而非 Flash

**说明（Help）**

启用就地执行（XiP）时，此选项将中断向量表从设备树 `zephyr,flash` chosen 指定的内存，重定位到 `zephyr,sram` chosen 指定的内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/arm/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → 向量表内存位置（Vector Table Memory Location）

<a id="CONFIG_ARM_ZIMAGE_HEADER"></a>

## 29.68 `CONFIG_ARM_ZIMAGE_HEADER`

**提示（Prompt）**：zImage 头部（Header）

**说明（Help）**

此选项添加 zImage 头部（Header）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CPU_AARCH32_CORTEX_R || CONFIG_CPU_AARCH32_CORTEX_A || CONFIG_CPU_CORTEX_M_HAS_VTOR) && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_ASSEMBLER_ISA_THUMB2"></a>

## 29.69 `CONFIG_ASSEMBLER_ISA_THUMB2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此辅助符号（Helper Symbol）指定汇编器的默认目标指令集（Instruction Set）。只支持 Thumb-2 ISA 时，例如 Cortex-M 内核，汇编器必须使用 Thumb-2。同时支持 Thumb-2 和 ARM ISA 时，例如 Cortex-A 和 Cortex-R 内核，由于架构汇编代码使用 ARM 指令，汇编器必须使用 ARM 指令集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ISA_ARM && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_ISA_THUMB2 && !CONFIG_ISA_ARM
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_ARM`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_ARM)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ISA_THUMB2`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_THUMB2)。

<a id="CONFIG_BUILTIN_STACK_GUARD"></a>

## 29.70 `CONFIG_BUILTIN_STACK_GUARD`

**提示（Prompt）**：基于内置 ARM 栈边界检查的线程栈保护区（Thread Stack Guards）

**说明（Help）**

通过内置栈指针边界检查（Stack Pointer Limit Checking）启用线程／中断栈保护区（Thread/Interrupt Stack Guards）。硬件必须支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_SPLIM && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**被弱选择（Implied by）**

```text
CONFIG_ARM_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_SPLIM`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SPLIM)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARM_STACK_PROTECTION`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_STACK_PROTECTION)。

<a id="CONFIG_CODE_DATA_RELOCATION_SRAM"></a>

## 29.71 `CONFIG_CODE_DATA_RELOCATION_SRAM`

**提示（Prompt）**：将代码／数据段重定位（Relocate）到 SRAM

**说明（Help）**

选择后，将指定文件的 `.text`、`data` 和 `.bss` 段重定位到 SRAM。文件应在 `CMakeList.txt` 中通过 CMake API `zephyr_code_relocate()` 指定。此配置用于为代码重定位使用的 SRAM 空间创建 MPU 条目。

译注：文件名 `CMakeList.txt` 按原文保留；常规 CMake 构建文件名为 `CMakeLists.txt`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CODE_DATA_RELOCATION
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_SLEEPTIMER
CONFIG_SILABS_SISDK_SLEEPTIMER
CONFIG_SILABS_SIWX91X_NWP
CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_FLASH_MCUX_C40
```

**定义位置（Location）**：[`arch/arm/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)、[`CONFIG_SILABS_SISDK_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLEEPTIMER)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION)、[`CONFIG_SOC_FLASH_MCUX_C40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_MCUX_C40)。

<a id="CONFIG_COMPILER_ISA_THUMB2"></a>

## 29.72 `CONFIG_COMPILER_ISA_THUMB2`

**提示（Prompt）**：使用 Thumb-2 指令集（Instruction Set）编译 C/C++ 函数

**说明（Help）**

此选项配置编译器使用 Thumb-2 指令集（Instruction Set）编译所有 C/C++ 函数。注意，此符号的作用范围不一定限于 C 和 C++，而是指所有形式的编译代码（Compiled Code）。将来增加其他原生编译语言支持时，此符号也应为该语言指定 Thumb-2 指令集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISA_THUMB2 && CONFIG_ARM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ISA_THUMB2`](P030_arch_arm_配置项参考_2.md#CONFIG_ISA_THUMB2)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK"></a>

## 29.73 `CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK`

**提示（Prompt）**：用于调试的调试监控中断（Debug Monitor Interrupt）

**说明（Help）**

启用此选项，将调试监控异常（Debug Monitor Exception）配置为低优先级，以供调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARMV6_M_ARMV8_M_BASELINE && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:394`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L394)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CORTEX_M_DWT"></a>

## 29.74 `CONFIG_CORTEX_M_DWT`

**提示（Prompt）**：数据观察点与跟踪（Data Watchpoint and Trace，DWT）

**说明（Help）**

启用并使用数据观察点与跟踪（Data Watchpoint and Trace，DWT）单元，为计时函数（Timing Functions）提供支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_DWT && (CONFIG_ARMV6_M_ARMV8_M_BASELINE || CONFIG_ARMV7_M_ARMV8_M_MAINLINE) && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_TIMING_FUNCTIONS
```

**被选择（Selected by）**

```text
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT
CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L386)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options） → ARM Cortex-M0/M0+/M1/M3/M4/M7/M23/M33/M55 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT)、[`CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION)。

<a id="CONFIG_CORTEX_M_ERRATUM_440977_WORKAROUND"></a>

## 29.75 `CONFIG_CORTEX_M_ERRATUM_440977_WORKAROUND`

**提示（Prompt）**：Cortex-M7 勘误（Erratum）440977 的规避措施

**说明（Help）**

在 Cortex-M7 r0p0/r0p1 上，写入 `BASEPRI/BASEPRI_MAX` 以提高优先级后，紧接的指令仍可能被抢占，这是 Arm 勘误 440977，旧编号 837070，已在 r0p2 修复。保留现有的指令同步屏障（ISB）作为该条指令，使临界区（Critical Region）在该窗口关闭后开始。中断仍可抢占 ISB，ISB 的流水线串行化成本也仍然存在。

与 Arm 的 `CPSID i/MSR/CPSIE i` 规避措施不同，此方式不会临时屏蔽包括零延迟中断（Zero-latency Interrupt）在内的更高优先级中断，也不会改变 `PRIMASK`。其他内核在提高优先级的写操作之后不需要屏障。Cortex-M7 r0p2 及更新版本也可以禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_CORTEX_M7
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:509`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L509)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)。

<a id="CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION"></a>

## 29.76 `CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用并使用空指针异常（Null Pointer Exception）选项。这是 Cortex-M 的调试功能，通过引发 CPU 故障检测空指针解引用（Null Pointer Dereferencing）。支持此功能会增加代码占用，增加量由 `CORTEX_M_NULL_POINTER_EXCEPTION_PAGE_SIZE` 决定。注意，此隐藏选项由基于 DWT 或基于 MPU 方案的选择符号选中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L482)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_DWT)、[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU)。

<a id="CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION_PAGE_SIZE"></a>

## 29.77 `CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION_PAGE_SIZE`

**提示（Prompt）**：为实现空指针检测而取消映射的页大小（Unmapped Page Size）

**说明（Help）**

为检测空指针解引用（Null Pointer Dereferencing）而保留的页面大小，必须为 2 的幂。较大值可增强检测能力，代价是浪费更大一片不能用于代码的 Flash 区域。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:498`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L498)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_NULL_POINTER_EXCEPTION)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_CPU_AARCH32_ARM9"></a>

## 29.78 `CONFIG_CPU_AARCH32_ARM9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARM9 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_ARM9
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_CPU_ARM926EJ_S
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_ARM9`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_ARM9)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_CPU_ARM926EJ_S`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_ARM926EJ_S)。

<a id="CONFIG_CPU_AARCH32_CORTEX_A"></a>

## 29.79 `CONFIG_CPU_AARCH32_CORTEX_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX
CONFIG_CPU_HAS_MMU
CONFIG_HAS_CMSIS_CORE
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_ARCH_HAS_BIT_REV
CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO if !CONFIG_USE_SWITCH
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_ARCH_HAS_IRQ_PENDING_OPS if !CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER && !CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_ARCH_HAS_GDBSTUB
CONFIG_EXTRA_EXCEPTION_INFO if CONFIG_GDBSTUB
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A5
CONFIG_CPU_CORTEX_A7
CONFIG_CPU_CORTEX_A9
CONFIG_CPU_CORTEX_A32
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_HAS_CMSIS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_ARCH_HAS_BIT_REV`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_BIT_REV)、[`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_ARCH_HAS_IRQ_PENDING_OPS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_PENDING_OPS)、[`CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_ARCH_HAS_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_GDBSTUB)、[`CONFIG_EXTRA_EXCEPTION_INFO`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_EXTRA_EXCEPTION_INFO)、[`CONFIG_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GDBSTUB)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_CPU_CORTEX_A5`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_A5)、[`CONFIG_CPU_CORTEX_A7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_A7)、[`CONFIG_CPU_CORTEX_A9`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_A9)、[`CONFIG_CPU_CORTEX_A32`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_A32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CMSIS_CORE`、`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`、`CONFIG_ARCH_HAS_GDBSTUB`。

<a id="CONFIG_CPU_AARCH32_CORTEX_R"></a>

## 29.80 `CONFIG_CPU_AARCH32_CORTEX_R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX
CONFIG_HAS_CMSIS_CORE
CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_ARCH_HAS_BIT_REV
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARM_MPU && !CONFIG_USE_SWITCH
CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO if !CONFIG_USE_SWITCH
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
CONFIG_ARCH_HAS_IRQ_PENDING_OPS if !CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER && !CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT if CONFIG_ARM_MPU && CONFIG_CPU_HAS_ARM_MPU && CONFIG_CPU_HAS_DCACHE
CONFIG_ARCH_SUPPORTS_ROM_START
CONFIG_USE_SWITCH_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R4
CONFIG_CPU_CORTEX_R5
CONFIG_CPU_CORTEX_R7
CONFIG_CPU_CORTEX_R8
CONFIG_CPU_CORTEX_R52
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX)、[`CONFIG_HAS_CMSIS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE)、[`CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_ARCH_HAS_BIT_REV`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_BIT_REV)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_ARCH_HAS_IRQ_PENDING_OPS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_PENDING_OPS)、[`CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_CPU_CORTEX_R4`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R4)、[`CONFIG_CPU_CORTEX_R5`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R5)、[`CONFIG_CPU_CORTEX_R7`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R7)、[`CONFIG_CPU_CORTEX_R8`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R8)、[`CONFIG_CPU_CORTEX_R52`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_R52)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CMSIS_CORE`、`CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`、`CONFIG_ARCH_SUPPORTS_ROM_START`。

<a id="CONFIG_CPU_ARM9"></a>

## 29.81 `CONFIG_CPU_ARM9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARM9 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_CPU_AARCH32_ARM9
```

**定义位置（Location）**：[`arch/arm/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_ARM9`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_ARM9)。

<a id="CONFIG_CPU_ARM926EJ_S"></a>

## 29.82 `CONFIG_CPU_ARM926EJ_S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARM926EJ-S CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_ARMV5TEJ
CONFIG_CPU_AARCH32_ARM9
CONFIG_CPU_HAS_MMU
```

**定义位置（Location）**：[`arch/arm/core/arm9/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/arm9/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARMV5TEJ`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV5TEJ)、[`CONFIG_CPU_AARCH32_ARM9`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_ARM9)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)。

<a id="CONFIG_CPU_CORTEX"></a>

## 29.83 `CONFIG_CPU_CORTEX`

原库同名定义共 2 条；本项为数据库第 4309 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
```

**定义位置（Location）**：[`arch/arm/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)。

<a id="CONFIG_CPU_CORTEX_A32"></a>

## 29.84 `CONFIG_CPU_CORTEX_A32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A32 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_AARCH32_ARMV8_A
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_ENSEMBLE_APSS
CONFIG_SOC_V8A_AARCH32
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_AARCH32_ARMV8_A`](P029_arch_arm_配置项参考_1.md#CONFIG_AARCH32_ARMV8_A)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_APSS)、[`CONFIG_SOC_V8A_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A_AARCH32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`、`CONFIG_SOC_V8A_AARCH32`。

<a id="CONFIG_CPU_CORTEX_A5"></a>

## 29.85 `CONFIG_CPU_CORTEX_A5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A5 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARMV7_A
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`。

<a id="CONFIG_CPU_CORTEX_A7"></a>

## 29.86 `CONFIG_CPU_CORTEX_A7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A7 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARMV7_A
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SUN8I_H3
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
CONFIG_SOC_RV1106
CONFIG_SOC_SERIES_STM32MP13X
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_SUN8I_H3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN8I_H3)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_RV1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RV1106)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`、`CONFIG_SOC_SUN8I_H3`、`CONFIG_SOC_RV1106`、`CONFIG_SOC_SERIES_STM32MP13X`。

<a id="CONFIG_CPU_CORTEX_A9"></a>

## 29.87 `CONFIG_CPU_CORTEX_A9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A9 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARMV7_A
CONFIG_CPU_HAS_ICACHE
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RZA2M
CONFIG_SOC_SERIES_XC7ZXXX
CONFIG_SOC_SERIES_XC7ZXXXS
CONFIG_SOC_SERIES_CYCLONEV
```

**定义位置（Location）**：[`arch/arm/core/cortex_a_r/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_a_r/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARMV7_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_A)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_SERIES_RZA2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA2M)、[`CONFIG_SOC_SERIES_XC7ZXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_SOC_SERIES_XC7ZXXXS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXXS)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARMV7_A`。

<a id="CONFIG_CPU_CORTEX_M"></a>

## 29.88 `CONFIG_CPU_CORTEX_M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX
CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN if !CONFIG_USE_SWITCH
CONFIG_HAS_CMSIS_CORE
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT
CONFIG_ARCH_HAS_THREAD_ABORT if !CONFIG_USE_SWITCH
CONFIG_ARCH_HAS_TRUSTED_EXECUTION if CONFIG_ARM_TRUSTZONE_M
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_ARM_MPU || CONFIG_CPU_CORTEX_M_HAS_SPLIM
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARM_MPU
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT if CONFIG_ARM_MPU && CONFIG_CPU_HAS_ARM_MPU && CONFIG_CPU_HAS_DCACHE
CONFIG_ARCH_HAS_RAMFUNC_SUPPORT
CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION if CONFIG_CPU_CORTEX_M_HAS_VTOR
CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION
CONFIG_ARCH_HAS_IRQ_PENDING_OPS if !CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER && !CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_SWAP_NONATOMIC
CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO
CONFIG_ARCH_HAS_TIMING_FUNCTIONS if CONFIG_CPU_CORTEX_M_HAS_DWT
CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT
CONFIG_ARCH_HAS_SUSPEND_TO_RAM
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
CONFIG_ARCH_SUPPORTS_ROM_START
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M0
CONFIG_CPU_CORTEX_M0PLUS
CONFIG_CPU_CORTEX_M1
CONFIG_CPU_CORTEX_M3
CONFIG_CPU_CORTEX_M4
CONFIG_CPU_CORTEX_M23
CONFIG_CPU_CORTEX_M33
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
CONFIG_CPU_CORTEX_M7
```

**弱选择（Implies）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`arch/arm/core/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX)、[`CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_HAS_CMSIS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT)、[`CONFIG_ARCH_HAS_THREAD_ABORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_ABORT)、[`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TRUSTED_EXECUTION)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_CPU_CORTEX_M_HAS_SPLIM`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SPLIM)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_RAMFUNC_SUPPORT)、[`CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION)、[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION)、[`CONFIG_ARCH_HAS_IRQ_PENDING_OPS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_PENDING_OPS)、[`CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_SWAP_NONATOMIC`](P002_kernel_配置项参考_2.md#CONFIG_SWAP_NONATOMIC)、[`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO)、[`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_TIMING_FUNCTIONS)、[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT)、[`CONFIG_ARCH_HAS_SUSPEND_TO_RAM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SUSPEND_TO_RAM)、[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_CPU_CORTEX_M0`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0)、[`CONFIG_CPU_CORTEX_M0PLUS`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0PLUS)、[`CONFIG_CPU_CORTEX_M1`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M1)、[`CONFIG_CPU_CORTEX_M3`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M3)、[`CONFIG_CPU_CORTEX_M4`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M4)、[`CONFIG_CPU_CORTEX_M23`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M23)、[`CONFIG_CPU_CORTEX_M33`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M33)、[`CONFIG_CPU_CORTEX_M52`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CMSIS_CORE`、`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`、`CONFIG_ARCH_HAS_THREAD_ABORT`、`CONFIG_ARCH_HAS_TRUSTED_EXECUTION`、`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`、`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`、`CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION`、`CONFIG_ARCH_HAS_NESTED_EXCEPTION_DETECTION`、`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`、`CONFIG_ARCH_HAS_TIMING_FUNCTIONS`、`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`、`CONFIG_ARCH_SUPPORTS_ROM_START`。

<a id="CONFIG_CPU_CORTEX_M0"></a>

## 29.89 `CONFIG_CPU_CORTEX_M0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M0 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV6_M_ARMV8_M_BASELINE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_M031X
CONFIG_SOC_SERIES_NRF51
CONFIG_SOC_SERIES_STM32F0X
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_SOC_SERIES_M031X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M031X)、[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F0X`。

<a id="CONFIG_CPU_CORTEX_M0PLUS"></a>

## 29.90 `CONFIG_CPU_CORTEX_M0PLUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M0+ CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV6_M_ARMV8_M_BASELINE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_SERIES_LPC11U6X
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_LPC54114_M0
CONFIG_SOC_SERIES_LPC84X
CONFIG_SOC_SERIES_SAMC20
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD20
CONFIG_SOC_SERIES_SAMD21
CONFIG_SOC_SERIES_SAML21
CONFIG_SOC_SERIES_SAMR21
CONFIG_SOC_SERIES_SAMR34
CONFIG_SOC_SERIES_SAMR35
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_MCXL255_CPU1
CONFIG_SOC_MCXL254_CPU1
CONFIG_SOC_MCXL253_CPU1
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_MKL25Z4
CONFIG_SOC_MKW40Z4
CONFIG_SOC_MKW41Z4
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_XMC7200D_E272K8384_M0PLUS
CONFIG_SOC_CYT4BF8CES_M0PLUS
CONFIG_SOC_CYT4BF8CEE_M0PLUS
CONFIG_SOC_CYT4BF8CDS_M0PLUS
CONFIG_SOC_CYT4BF8CDE_M0PLUS
CONFIG_SOC_CYT4BFBCJS_M0PLUS
CONFIG_SOC_CYT4BFBCJE_M0PLUS
CONFIG_SOC_CYT4BFBCHS_M0PLUS
CONFIG_SOC_CYT4BFBCHE_M0PLUS
CONFIG_SOC_CYT4BFCCJS_M0PLUS
CONFIG_SOC_CYT4BFCCJE_M0PLUS
CONFIG_SOC_CYT4BFCCHS_M0PLUS
CONFIG_SOC_CYT4BFCCHE_M0PLUS
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_AN383
CONFIG_SOC_S32K116
CONFIG_SOC_S32K118
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_SERIES_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC11U6X)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_LPC54114_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M0)、[`CONFIG_SOC_SERIES_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC84X)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAML21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_SERIES_SAMR34`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_MCXL255_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU1)、[`CONFIG_SOC_MCXL254_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU1)、[`CONFIG_SOC_MCXL253_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU1)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_MKL25Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKL25Z4)、[`CONFIG_SOC_MKW40Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW40Z4)、[`CONFIG_SOC_MKW41Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW41Z4)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_XMC7200D_E272K8384_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XMC7200D_E272K8384_M0PLUS)、[`CONFIG_SOC_CYT4BF8CES_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CES_M0PLUS)、[`CONFIG_SOC_CYT4BF8CEE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CEE_M0PLUS)、[`CONFIG_SOC_CYT4BF8CDS_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDS_M0PLUS)、[`CONFIG_SOC_CYT4BF8CDE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDE_M0PLUS)、[`CONFIG_SOC_CYT4BFBCJS_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJS_M0PLUS)、[`CONFIG_SOC_CYT4BFBCJE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJE_M0PLUS)、[`CONFIG_SOC_CYT4BFBCHS_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHS_M0PLUS)、[`CONFIG_SOC_CYT4BFBCHE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHE_M0PLUS)、[`CONFIG_SOC_CYT4BFCCJS_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJS_M0PLUS)、[`CONFIG_SOC_CYT4BFCCJE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJE_M0PLUS)、[`CONFIG_SOC_CYT4BFCCHS_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHS_M0PLUS)、[`CONFIG_SOC_CYT4BFCCHE_M0PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHE_M0PLUS)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_AN383`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN383)、[`CONFIG_SOC_S32K116`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K116)、[`CONFIG_SOC_S32K118`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K118)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC11U6X`、`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_LPC54114_M0`、`CONFIG_SOC_SERIES_LPC84X`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_MCXL255_CPU1`、`CONFIG_SOC_MCXL254_CPU1`、`CONFIG_SOC_MCXL253_CPU1`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_MKL25Z4`、`CONFIG_SOC_MKW40Z4`、`CONFIG_SOC_MKW41Z4`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M0`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_XMC7200D_E272K8384_M0PLUS`、`CONFIG_SOC_CYT4BF8CES_M0PLUS`、`CONFIG_SOC_CYT4BF8CEE_M0PLUS`、`CONFIG_SOC_CYT4BF8CDS_M0PLUS`、`CONFIG_SOC_CYT4BF8CDE_M0PLUS`、`CONFIG_SOC_CYT4BFBCJS_M0PLUS`、`CONFIG_SOC_CYT4BFBCJE_M0PLUS`、`CONFIG_SOC_CYT4BFBCHS_M0PLUS`、`CONFIG_SOC_CYT4BFBCHE_M0PLUS`、`CONFIG_SOC_CYT4BFCCJS_M0PLUS`、`CONFIG_SOC_CYT4BFCCJE_M0PLUS`、`CONFIG_SOC_CYT4BFCCHS_M0PLUS`、`CONFIG_SOC_CYT4BFCCHE_M0PLUS`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WL3X`、`CONFIG_SOC_S32K116`、`CONFIG_SOC_S32K118`。

<a id="CONFIG_CPU_CORTEX_M0_HAS_VECTOR_TABLE_REMAP"></a>

## 29.91 `CONFIG_CPU_CORTEX_M0_HAS_VECTOR_TABLE_REMAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 Cortex-M0 具有可将向量表（Vector Table）映射到 SRAM 的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV6_M_ARMV8_M_BASELINE && CONFIG_CPU_CORTEX_M && CONFIG_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32F0X
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F0X`。

<a id="CONFIG_CPU_CORTEX_M1"></a>

## 29.92 `CONFIG_CPU_CORTEX_M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M1 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV6_M_ARMV8_M_BASELINE
```

**被选择（Selected by）**

```text
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV6_M_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV6_M_ARMV8_M_BASELINE)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1)。

<a id="CONFIG_CPU_CORTEX_M23"></a>

## 29.93 `CONFIG_CPU_CORTEX_M23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M23 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV8_M_BASELINE
CONFIG_ARMV8_M_SE if CONFIG_CPU_HAS_TEE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_SERIES_M2L31X
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32L23X
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV8_M_BASELINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_BASELINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`。

<a id="CONFIG_CPU_CORTEX_M3"></a>

## 29.94 `CONFIG_CPU_CORTEX_M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M3 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_KB106X
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_SIM3U
CONFIG_SOC_TI_LM3S6965
CONFIG_SOC_SERIES_SAM3X
CONFIG_SOC_SERIES_SMARTFUSION2
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_BEETLE
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3
CONFIG_SOC_AN385
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_SOC_SERIES_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KB106X)、[`CONFIG_SOC_SERIES_EFM32TG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_SIM3U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIM3U)、[`CONFIG_SOC_TI_LM3S6965`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_TI_LM3S6965)、[`CONFIG_SOC_SERIES_SAM3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SMARTFUSION2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3)、[`CONFIG_SOC_AN385`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN385)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32L1X`。

<a id="CONFIG_CPU_CORTEX_M33"></a>

## 29.95 `CONFIG_CPU_CORTEX_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M33 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV8_M_MAINLINE
CONFIG_ARMV8_M_SE if CONFIG_CPU_HAS_TEE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_AM13E23019
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S26
CONFIG_SOC_LPC55S28
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_R7KA8D2KFLCAC_CM33
CONFIG_SOC_R7KA8M2JFLCAC_CM33
CONFIG_SOC_R7KA8P1KFLCAC_CM33
CONFIG_SOC_R7KA8T2LFLCAC_CM33
CONFIG_SOC_SERIES_MCXA1X3
CONFIG_SOC_SERIES_MCXA1X6
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN947_CPU1
CONFIG_SOC_MCXN547
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN547_CPU1
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_MIMXRT1189_CM33
CONFIG_SOC_MIMXRT1186_CM33
CONFIG_SOC_MIMXRT1185_CM33
CONFIG_SOC_MIMXRT118C_CM33
CONFIG_SOC_MIMXRT1187_CM33
CONFIG_SOC_MIMXRT1182
CONFIG_SOC_MIMXRT1181
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_SERIES_PSE84_M33
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZG2L
CONFIG_SOC_SERIES_RZG2UL
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_SERIES_RZG3S
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_SERIES_RZV2L
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_AN521
CONFIG_SOC_MUSCA_B1
CONFIG_SOC_MUSCA_S1
CONFIG_SOC_SERIES_RW6XX
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_MAINLINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S26)、[`CONFIG_SOC_LPC55S28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S28)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM33)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM33)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM33)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM33)、[`CONFIG_SOC_SERIES_MCXA1X3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X3)、[`CONFIG_SOC_SERIES_MCXA1X6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X6)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN947_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU1)、[`CONFIG_SOC_MCXN547`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN547_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU1)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_MIMXRT1189_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1189_CM33)、[`CONFIG_SOC_MIMXRT1186_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1186_CM33)、[`CONFIG_SOC_MIMXRT1185_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1185_CM33)、[`CONFIG_SOC_MIMXRT118C_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT118C_CM33)、[`CONFIG_SOC_MIMXRT1187_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1187_CM33)、[`CONFIG_SOC_MIMXRT1182`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1182)、[`CONFIG_SOC_MIMXRT1181`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1181)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_SERIES_PSE84_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M33)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521)、[`CONFIG_SOC_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_B1)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S26`、`CONFIG_SOC_LPC55S28`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69`、`CONFIG_SOC_R7KA8D2KFLCAC_CM33`、`CONFIG_SOC_R7KA8M2JFLCAC_CM33`、`CONFIG_SOC_R7KA8P1KFLCAC_CM33`、`CONFIG_SOC_R7KA8T2LFLCAC_CM33`、`CONFIG_SOC_SERIES_MCXA1X3`、`CONFIG_SOC_SERIES_MCXA1X6`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN947_CPU1`、`CONFIG_SOC_MCXN547`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN547_CPU1`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_MIMXRT1189_CM33`、`CONFIG_SOC_MIMXRT1186_CM33`、`CONFIG_SOC_MIMXRT1185_CM33`、`CONFIG_SOC_MIMXRT118C_CM33`、`CONFIG_SOC_MIMXRT1187_CM33`、`CONFIG_SOC_MIMXRT1182`、`CONFIG_SOC_MIMXRT1181`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_PSE84_M33`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_AN521`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_CPU_CORTEX_M4"></a>

## 29.96 `CONFIG_CPU_CORTEX_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M4 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_FT9001
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_LPC54628
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_EOS_S3
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_KB1200
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_MIMXRT1175_CM4
CONFIG_SOC_MIMXRT1176_CM4
CONFIG_SOC_MIMXRT1166_CM4
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_MKW22D5
CONFIG_SOC_MKW24D5
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8MQ6_M4
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC32XX
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_SERIES_NPCM4
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_EM32F967
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_SAM4L
CONFIG_SOC_SERIES_SAM4S
CONFIG_SOC_SERIES_XMC4XXX
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_STM32H745XX_M4
CONFIG_SOC_STM32H747XX_M4
CONFIG_SOC_STM32H755XX_M4
CONFIG_SOC_STM32H757XX_M4
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_AN386
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_S32K142
CONFIG_SOC_S32K142W
CONFIG_SOC_S32K144
CONFIG_SOC_S32K144W
CONFIG_SOC_S32K146
CONFIG_SOC_S32K148
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_LPC54628`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54628)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_MIMXRT1175_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1175_CM4)、[`CONFIG_SOC_MIMXRT1176_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1176_CM4)、[`CONFIG_SOC_MIMXRT1166_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1166_CM4)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_MKW22D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW22D5)、[`CONFIG_SOC_MKW24D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW24D5)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8MQ6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6_M4)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_STM32H745XX_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H745XX_M4)、[`CONFIG_SOC_STM32H747XX_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H747XX_M4)、[`CONFIG_SOC_STM32H755XX_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H755XX_M4)、[`CONFIG_SOC_STM32H757XX_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H757XX_M4)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_AN386`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN386)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_S32K142`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142)、[`CONFIG_SOC_S32K142W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142W)、[`CONFIG_SOC_S32K144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144)、[`CONFIG_SOC_S32K144W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144W)、[`CONFIG_SOC_S32K146`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K146)、[`CONFIG_SOC_S32K148`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K148)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_LPC54628`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_MIMXRT1175_CM4`、`CONFIG_SOC_MIMXRT1176_CM4`、`CONFIG_SOC_MIMXRT1166_CM4`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_MKW22D5`、`CONFIG_SOC_MKW24D5`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_STM32H745XX_M4`、`CONFIG_SOC_STM32H747XX_M4`、`CONFIG_SOC_STM32H755XX_M4`、`CONFIG_SOC_STM32H757XX_M4`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_S32K142`、`CONFIG_SOC_S32K142W`、`CONFIG_SOC_S32K144`、`CONFIG_SOC_S32K144W`、`CONFIG_SOC_S32K146`、`CONFIG_SOC_S32K148`。

<a id="CONFIG_CPU_CORTEX_M52"></a>

## 29.97 `CONFIG_CPU_CORTEX_M52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M52 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV8_1_M_MAINLINE
CONFIG_ARMV8_M_SE if CONFIG_CPU_HAS_TEE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)。

<a id="CONFIG_CPU_CORTEX_M55"></a>

## 29.98 `CONFIG_CPU_CORTEX_M55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M55 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV8_1_M_MAINLINE
CONFIG_ARMV8_M_SE if CONFIG_CPU_HAS_TEE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_SERIES_PSE84_M55
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_CORSTONE300
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_SERIES_PSE84_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M55)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_SERIES_PSE84_M55`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_CORSTONE300`。

<a id="CONFIG_CPU_CORTEX_M7"></a>

## 29.99 `CONFIG_CPU_CORTEX_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M7 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_VALKYRIE
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_MIMXRT1189_CM7
CONFIG_SOC_MIMXRT1186_CM7
CONFIG_SOC_MIMXRT1185_CM7
CONFIG_SOC_MIMXRT118C_CM7
CONFIG_SOC_MIMXRT1187_CM7
CONFIG_SOC_MIMXRT1151
CONFIG_SOC_MIMXRT1152
CONFIG_SOC_MIMXRT1175_CM7
CONFIG_SOC_MIMXRT1176_CM7
CONFIG_SOC_MIMXRT1166_CM7
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_XMC7200D_E272K8384_M7_0
CONFIG_SOC_XMC7200D_E272K8384_M7_1
CONFIG_SOC_CYT4BF8CES_M7_0
CONFIG_SOC_CYT4BF8CES_M7_1
CONFIG_SOC_CYT4BF8CEE_M7_0
CONFIG_SOC_CYT4BF8CEE_M7_1
CONFIG_SOC_CYT4BF8CDS_M7_0
CONFIG_SOC_CYT4BF8CDS_M7_1
CONFIG_SOC_CYT4BF8CDE_M7_0
CONFIG_SOC_CYT4BF8CDE_M7_1
CONFIG_SOC_CYT4BFBCJS_M7_0
CONFIG_SOC_CYT4BFBCJS_M7_1
CONFIG_SOC_CYT4BFBCJE_M7_0
CONFIG_SOC_CYT4BFBCJE_M7_1
CONFIG_SOC_CYT4BFBCHS_M7_0
CONFIG_SOC_CYT4BFBCHS_M7_1
CONFIG_SOC_CYT4BFBCHE_M7_0
CONFIG_SOC_CYT4BFBCHE_M7_1
CONFIG_SOC_CYT4BFCCJS_M7_0
CONFIG_SOC_CYT4BFCCJS_M7_1
CONFIG_SOC_CYT4BFCCJE_M7_0
CONFIG_SOC_CYT4BFCCJE_M7_1
CONFIG_SOC_CYT4BFCCHS_M7_0
CONFIG_SOC_CYT4BFCCHS_M7_1
CONFIG_SOC_CYT4BFCCHE_M7_0
CONFIG_SOC_CYT4BFCCHE_M7_1
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_STM32H723XX
CONFIG_SOC_STM32H725XX
CONFIG_SOC_STM32H730XX
CONFIG_SOC_STM32H730XXQ
CONFIG_SOC_STM32H735XX
CONFIG_SOC_STM32H742XX
CONFIG_SOC_STM32H743XX
CONFIG_SOC_STM32H745XX_M7
CONFIG_SOC_STM32H747XX_M7
CONFIG_SOC_STM32H750XX
CONFIG_SOC_STM32H753XX
CONFIG_SOC_STM32H755XX_M7
CONFIG_SOC_STM32H757XX_M7
CONFIG_SOC_STM32H7A3XX
CONFIG_SOC_STM32H7A3XXQ
CONFIG_SOC_STM32H7B0XX
CONFIG_SOC_STM32H7B0XXQ
CONFIG_SOC_STM32H7B3XX
CONFIG_SOC_STM32H7B3XXQ
CONFIG_SOC_AN500
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_S32K566_M7
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_VALKYRIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_VALKYRIE)、[`CONFIG_SOC_BCM58402_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_MIMXRT1189_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1189_CM7)、[`CONFIG_SOC_MIMXRT1186_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1186_CM7)、[`CONFIG_SOC_MIMXRT1185_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1185_CM7)、[`CONFIG_SOC_MIMXRT118C_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT118C_CM7)、[`CONFIG_SOC_MIMXRT1187_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1187_CM7)、[`CONFIG_SOC_MIMXRT1151`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1151)、[`CONFIG_SOC_MIMXRT1152`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1152)、[`CONFIG_SOC_MIMXRT1175_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1175_CM7)、[`CONFIG_SOC_MIMXRT1176_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1176_CM7)、[`CONFIG_SOC_MIMXRT1166_CM7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1166_CM7)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_XMC7200D_E272K8384_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XMC7200D_E272K8384_M7_0)、[`CONFIG_SOC_XMC7200D_E272K8384_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XMC7200D_E272K8384_M7_1)、[`CONFIG_SOC_CYT4BF8CES_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CES_M7_0)、[`CONFIG_SOC_CYT4BF8CES_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CES_M7_1)、[`CONFIG_SOC_CYT4BF8CEE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CEE_M7_0)、[`CONFIG_SOC_CYT4BF8CEE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CEE_M7_1)、[`CONFIG_SOC_CYT4BF8CDS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDS_M7_0)、[`CONFIG_SOC_CYT4BF8CDS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDS_M7_1)、[`CONFIG_SOC_CYT4BF8CDE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDE_M7_0)、[`CONFIG_SOC_CYT4BF8CDE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BF8CDE_M7_1)、[`CONFIG_SOC_CYT4BFBCJS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJS_M7_0)、[`CONFIG_SOC_CYT4BFBCJS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJS_M7_1)、[`CONFIG_SOC_CYT4BFBCJE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJE_M7_0)、[`CONFIG_SOC_CYT4BFBCJE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCJE_M7_1)、[`CONFIG_SOC_CYT4BFBCHS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHS_M7_0)、[`CONFIG_SOC_CYT4BFBCHS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHS_M7_1)、[`CONFIG_SOC_CYT4BFBCHE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHE_M7_0)、[`CONFIG_SOC_CYT4BFBCHE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFBCHE_M7_1)、[`CONFIG_SOC_CYT4BFCCJS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJS_M7_0)、[`CONFIG_SOC_CYT4BFCCJS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJS_M7_1)、[`CONFIG_SOC_CYT4BFCCJE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJE_M7_0)、[`CONFIG_SOC_CYT4BFCCJE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCJE_M7_1)、[`CONFIG_SOC_CYT4BFCCHS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHS_M7_0)、[`CONFIG_SOC_CYT4BFCCHS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHS_M7_1)、[`CONFIG_SOC_CYT4BFCCHE_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHE_M7_0)、[`CONFIG_SOC_CYT4BFCCHE_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4BFCCHE_M7_1)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_STM32H723XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H723XX)、[`CONFIG_SOC_STM32H725XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H725XX)、[`CONFIG_SOC_STM32H730XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H730XX)、[`CONFIG_SOC_STM32H730XXQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H730XXQ)、[`CONFIG_SOC_STM32H735XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H735XX)、[`CONFIG_SOC_STM32H742XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H742XX)、[`CONFIG_SOC_STM32H743XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H743XX)、[`CONFIG_SOC_STM32H745XX_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H745XX_M7)、[`CONFIG_SOC_STM32H747XX_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H747XX_M7)、[`CONFIG_SOC_STM32H750XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H750XX)、[`CONFIG_SOC_STM32H753XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H753XX)、[`CONFIG_SOC_STM32H755XX_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H755XX_M7)、[`CONFIG_SOC_STM32H757XX_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H757XX_M7)、[`CONFIG_SOC_STM32H7A3XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7A3XX)、[`CONFIG_SOC_STM32H7A3XXQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7A3XXQ)、[`CONFIG_SOC_STM32H7B0XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7B0XX)、[`CONFIG_SOC_STM32H7B0XXQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7B0XXQ)、[`CONFIG_SOC_STM32H7B3XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7B3XX)、[`CONFIG_SOC_STM32H7B3XXQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32H7B3XXQ)、[`CONFIG_SOC_AN500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN500)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_S32K566_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_M7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_MIMXRT1189_CM7`、`CONFIG_SOC_MIMXRT1186_CM7`、`CONFIG_SOC_MIMXRT1185_CM7`、`CONFIG_SOC_MIMXRT118C_CM7`、`CONFIG_SOC_MIMXRT1187_CM7`、`CONFIG_SOC_MIMXRT1151`、`CONFIG_SOC_MIMXRT1152`、`CONFIG_SOC_MIMXRT1175_CM7`、`CONFIG_SOC_MIMXRT1176_CM7`、`CONFIG_SOC_MIMXRT1166_CM7`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_XMC7200D_E272K8384_M7_0`、`CONFIG_SOC_XMC7200D_E272K8384_M7_1`、`CONFIG_SOC_CYT4BF8CES_M7_0`、`CONFIG_SOC_CYT4BF8CES_M7_1`、`CONFIG_SOC_CYT4BF8CEE_M7_0`、`CONFIG_SOC_CYT4BF8CEE_M7_1`、`CONFIG_SOC_CYT4BF8CDS_M7_0`、`CONFIG_SOC_CYT4BF8CDS_M7_1`、`CONFIG_SOC_CYT4BF8CDE_M7_0`、`CONFIG_SOC_CYT4BF8CDE_M7_1`、`CONFIG_SOC_CYT4BFBCJS_M7_0`、`CONFIG_SOC_CYT4BFBCJS_M7_1`、`CONFIG_SOC_CYT4BFBCJE_M7_0`、`CONFIG_SOC_CYT4BFBCJE_M7_1`、`CONFIG_SOC_CYT4BFBCHS_M7_0`、`CONFIG_SOC_CYT4BFBCHS_M7_1`、`CONFIG_SOC_CYT4BFBCHE_M7_0`、`CONFIG_SOC_CYT4BFBCHE_M7_1`、`CONFIG_SOC_CYT4BFCCJS_M7_0`、`CONFIG_SOC_CYT4BFCCJS_M7_1`、`CONFIG_SOC_CYT4BFCCJE_M7_0`、`CONFIG_SOC_CYT4BFCCJE_M7_1`、`CONFIG_SOC_CYT4BFCCHS_M7_0`、`CONFIG_SOC_CYT4BFCCHS_M7_1`、`CONFIG_SOC_CYT4BFCCHE_M7_0`、`CONFIG_SOC_CYT4BFCCHE_M7_1`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_STM32H723XX`、`CONFIG_SOC_STM32H725XX`、`CONFIG_SOC_STM32H730XX`、`CONFIG_SOC_STM32H730XXQ`、`CONFIG_SOC_STM32H735XX`、`CONFIG_SOC_STM32H742XX`、`CONFIG_SOC_STM32H743XX`、`CONFIG_SOC_STM32H745XX_M7`、`CONFIG_SOC_STM32H747XX_M7`、`CONFIG_SOC_STM32H750XX`、`CONFIG_SOC_STM32H753XX`、`CONFIG_SOC_STM32H755XX_M7`、`CONFIG_SOC_STM32H757XX_M7`、`CONFIG_SOC_STM32H7A3XX`、`CONFIG_SOC_STM32H7A3XXQ`、`CONFIG_SOC_STM32H7B0XX`、`CONFIG_SOC_STM32H7B0XXQ`、`CONFIG_SOC_STM32H7B3XX`、`CONFIG_SOC_STM32H7B3XXQ`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_S32K566_M7`。

<a id="CONFIG_CPU_CORTEX_M85"></a>

## 29.100 `CONFIG_CPU_CORTEX_M85`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-M85 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARMV8_1_M_MAINLINE
CONFIG_ARMV8_M_SE if CONFIG_CPU_HAS_TEE
CONFIG_ARMV7_M_ARMV8_M_FP if CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_R7KA8D2KFLCAC_CM85
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_R7KA8M2JFLCAC_CM85
CONFIG_SOC_R7KA8P1KFLCAC_CM85
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_R7KA8T2LFLCAC_CM85
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`arch/arm/core/cortex_m/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → ARM 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARMV8_1_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MAINLINE)、[`CONFIG_ARMV8_M_SE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_SE)、[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM85)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM85)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM85)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R7KA8D2KFLCAC_CM85`、`CONFIG_SOC_R7KA8M2JFLCAC_CM85`、`CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`CONFIG_SOC_R7KA8T2LFLCAC_CM85`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<!-- kconfig-navigation -->

[上一章](P028_arch_arc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P030_arch_arm_配置项参考_2.md)
