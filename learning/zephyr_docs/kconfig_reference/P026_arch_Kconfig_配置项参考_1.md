---
id: learning.zephyr-docs.kconfig-reference.page-26
title: "`arch/Kconfig`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第26章\_`arch/Kconfig`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `arch/Kconfig` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_64BIT"></a>

## 26.1 `CONFIG_64BIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项告知构建系统，目标使用 64 位地址空间（Address Space），即指针和 `long` 类型宽度均为 64 位。由 `arch/$ARCH/Kconfig`、`soc/**/Kconfig` 或 `boards/**/Kconfig` 选择，用户通常应避免修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
CONFIG_CPU_HS6X
CONFIG_RISCV_ISA_RV64I
CONFIG_X86_64
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_CPU_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS6X)、[`CONFIG_RISCV_ISA_RV64I`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_RV64I)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`。

<a id="CONFIG_ARC"></a>

## 26.2 `CONFIG_ARC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARC 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_ARCH_SUPPORTS_ROM_START
CONFIG_ARCH_SUPPORTS_ROM_OFFSET
CONFIG_ARCH_HAS_DIRECTED_IPIS
CONFIG_ARCH_HAS_DIRECT_INTERRUPTS
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED if CONFIG_SMP
```

**被选择（Selected by）**

```text
CONFIG_SOC_ARC_HSDK
CONFIG_SOC_ARC_IOT
CONFIG_SOC_ARC_EMSDP
CONFIG_SOC_EMSK
CONFIG_SOC_ARC_HSDK4XD
CONFIG_SOC_SERIES_NSIM_EM
CONFIG_SOC_SERIES_NSIM_HS
CONFIG_SOC_SERIES_NSIM_SEM
CONFIG_SOC_SERIES_NSIM_VPX5
CONFIG_SOC_QEMU_ARC
```

**弱选择（Implies）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`arch/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_ARCH_SUPPORTS_ROM_OFFSET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_OFFSET)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECT_INTERRUPTS)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_SOC_ARC_HSDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_HSDK)、[`CONFIG_SOC_ARC_IOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_IOT)、[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_SOC_EMSK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK)、[`CONFIG_SOC_ARC_HSDK4XD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_HSDK4XD)、[`CONFIG_SOC_SERIES_NSIM_EM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_EM)、[`CONFIG_SOC_SERIES_NSIM_HS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_HS)、[`CONFIG_SOC_SERIES_NSIM_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_SEM)、[`CONFIG_SOC_SERIES_NSIM_VPX5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_VPX5)、[`CONFIG_SOC_QEMU_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_ARCH_SUPPORTS_ROM_START`、`CONFIG_SOC_ARC_HSDK`、`CONFIG_SOC_ARC_EMSDP`、`CONFIG_SOC_SERIES_NSIM_EM`、`CONFIG_SOC_SERIES_NSIM_HS`、`CONFIG_SOC_SERIES_NSIM_SEM`、`CONFIG_SOC_SERIES_NSIM_VPX5`、`CONFIG_SOC_QEMU_ARC`。

<a id="CONFIG_ARCH"></a>

## 26.3 `CONFIG_ARCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

系统架构字符串（System Architecture String）。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`arch/Kconfig:1508`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1508)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_ARCH_CACHE"></a>

## 26.4 `CONFIG_ARCH_CACHE`

**提示（Prompt）**：集成缓存控制器（Integrated Cache Controller）

**说明（Help）**

集成在内核上的缓存控制器（On-core Cache Controller）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:1476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1476)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options） → 缓存类型（Cache Type）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_TYPE)。

<a id="CONFIG_ARCH_DEVICE_STATE_ALIGN"></a>

## 26.5 `CONFIG_ARCH_DEVICE_STATE_ALIGN`

**提示（Prompt）**：设备状态对齐大小（Device State Alignment Size）

**说明（Help）**

此选项控制设备状态（Device State）的对齐大小。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`arch/Kconfig:673`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L673)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

<a id="CONFIG_ARCH_HAS_BIT_REV"></a>

## 26.6 `CONFIG_ARCH_HAS_BIT_REV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当目标架构提供 `arch_sys_bit_rev8()`、`arch_sys_bit_rev16()` 和 `arch_sys_bit_rev32()` 实现时，由该架构选择此隐藏选项。在工具链不提供等效的 `__builtin_bitreverse*()` 时，`sys_bit_rev*()` 辅助函数会使用这些实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_RISCV_ISA_EXT_ZBKB
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/Kconfig:868`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L868)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_RISCV_ISA_EXT_ZBKB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_ZBKB)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARCH_HAS_CODE_DATA_RELOCATION"></a>

## 26.7 `CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择后，表示架构／SoC 在其链接脚本（Linker Script）中实现了 `CODE_DATA_RELOCATION` 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_OPENRISC
CONFIG_RISCV
CONFIG_XTENSA
CONFIG_TRICORE
```

**定义位置（Location）**：[`arch/Kconfig:1080`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1080)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)。

<a id="CONFIG_ARCH_HAS_CPU_IDLE_HOOKS"></a>

## 26.8 `CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

能够告知 CPU 负载模块（CPU Load Module）CPU 何时进入和离开空闲状态的架构选择此选项，相关功能受 `CONFIG_SYS_IDLE_HOOKS` 控制。要求空闲路径（Idle Path）进入时调用 `sys_trace_idle()`，并通过以下任一种方式关闭空闲时间窗口（Idle Window）：

- 对于在中断锁定状态下等待的架构，例如 Arm、RISC-V，在等待后调用 `sys_trace_idle_exit()`。等待会在尚未处理中断时返回，因此退出钩子先于任何 ISR 执行。
- 对于在中断使能状态下等待的架构，例如 x86 的 `sti; hlt`、Xtensa 的 `waiti 0`，在 ISR 入口调用 `sys_trace_isr_enter()`。此时唤醒 ISR 先执行，并可能调度离开空闲线程，使退出钩子远晚于空闲结束才执行，因此改由 ISR 入口关闭时间窗口。

这是空闲钩子 CPU 负载后端（Idle-hook CPU Load Backend）`CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK` 的前提条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM
CONFIG_ARM64
CONFIG_X86
CONFIG_RISCV
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/Kconfig:956`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L956)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT"></a>

## 26.9 `CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构移植（Architecture Port）可能无法或不希望使用提供的 `k_busy_wait()`，而必须采用自定义实现。在这种情况下必须启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARCH_POSIX
CONFIG_HEXAGON
CONFIG_ARM_ARCH_TIMER
```

**定义位置（Location）**：[`arch/Kconfig:1538`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1538)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_HEXAGON`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HEXAGON)、[`CONFIG_ARM_ARCH_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARM_ARCH_TIMER)。

<a id="CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE"></a>

## 26.10 `CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项允许应用程序使用自定义实现覆盖默认的架构空闲实现（Architecture Idle Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_CH32V
CONFIG_ARC_IOT_CUSTOM_CPU_IDLE
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_SERIES_IT8XXX2
```

**定义位置（Location）**：[`arch/Kconfig:1525`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1525)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_ARC_IOT_CUSTOM_CPU_IDLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_IOT_CUSTOM_CPU_IDLE)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_SERIES_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`。

<a id="CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE"></a>

## 26.11 `CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项允许应用程序使用自定义实现覆盖默认的架构空闲实现（Architecture Idle Implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_CH32V
CONFIG_ARC_IOT_CUSTOM_CPU_IDLE
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_SERIES_IT8XXX2
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`arch/Kconfig:1519`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1519)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_ARC_IOT_CUSTOM_CPU_IDLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_IOT_CUSTOM_CPU_IDLE)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_SERIES_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`。

<a id="CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL"></a>

## 26.12 `CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构实现了 `arch_current_thread()` 和 `arch_current_thread_set()` 时选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_RISCV_CURRENT_VIA_GP
```

**定义位置（Location）**：[`arch/Kconfig:1545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1545)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_RISCV_CURRENT_VIA_GP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CURRENT_VIA_GP)。

<a id="CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN"></a>

## 26.13 `CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构移植（Architecture Port）可能无法使用 `z_swap_unlocked()` 切换到主线程（`bg_thread_main`），而必须采用自定义方式。在这种情况下必须启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`arch/Kconfig:1531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1531)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ARCH_HAS_DEMAND_MAPPING"></a>

## 26.14 `CONFIG_ARCH_HAS_DEMAND_MAPPING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构支持按需分页（Demand Paging），且 `arch_mem_map()` 支持 `K_MEM_MAP_UNPAGED`，则应由架构选择此隐藏配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM64
CONFIG_X86
```

**定义位置（Location）**：[`arch/Kconfig:1146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1146)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ARCH_HAS_DEMAND_PAGING"></a>

## 26.15 `CONFIG_ARCH_HAS_DEMAND_PAGING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构支持按需分页（Demand Paging），则应由架构选择此隐藏配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM64
CONFIG_X86
```

**定义位置（Location）**：[`arch/Kconfig:1140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1140)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ARCH_HAS_DIRECTED_IPIS"></a>

## 26.16 `CONFIG_ARCH_HAS_DIRECTED_IPIS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构实现了 `arch_sched_directed_ipi()`，允许将处理器间中断（IPI）定向发送到特定 CPU，则应由架构选择此隐藏配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_CAVSV25
CONFIG_AARCH32_ARMV8_A
CONFIG_AARCH32_ARMV8_R
CONFIG_X86_64
CONFIG_ARC
CONFIG_ARM64
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/Kconfig:1161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1161)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_CAVSV25`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CAVSV25)、[`CONFIG_AARCH32_ARMV8_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AARCH32_ARMV8_A)、[`CONFIG_AARCH32_ARMV8_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AARCH32_ARMV8_R)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_ARCH_HAS_DIRECT_INTERRUPTS"></a>

## 26.17 `CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

实现直接中断钩子（Direct Interrupt Hooks）的架构选择此选项，即实现 `ARCH_IRQ_DIRECT_CONNECT()` 和 `ARCH_ISR_DIRECT_DECLARE()`，以及它们展开后使用的 `ARCH_ISR_DIRECT_HEADER()`、`ARCH_ISR_DIRECT_FOOTER()`、`ARCH_ISR_DIRECT_PM()` 钩子。任何使用 `IRQ_DIRECT_CONNECT()` 或 `ISR_DIRECT_DECLARE()` 的代码都需要此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC
CONFIG_ARM
CONFIG_X86
CONFIG_RISCV
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`arch/Kconfig:932`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L932)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

<a id="CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK"></a>

## 26.18 `CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持在初始化期间调用固件参数处理钩子（Firmware Argument Handler Hook）的架构选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/Kconfig:977`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L977)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARCH_HAS_IRQ_GET_ACTIVE"></a>

## 26.19 `CONFIG_ARCH_HAS_IRQ_GET_ACTIVE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

能够通过 `arch_irq_get_active()`，进而通过 `k_irq_get_active()`，报告本地 CPU 当前正在处理的中断线（Interrupt Line）的架构选择此选项。某些中断控制器通过寄存器提供该信息，其他实现则在中断分派路径（Interrupt Dispatch Path）中记录。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM_TRACK_ACTIVE_IRQ
```

**定义位置（Location）**：[`arch/Kconfig:923`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L923)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM_TRACK_ACTIVE_IRQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_TRACK_ACTIVE_IRQ)。

<a id="CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED"></a>

## 26.20 `CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

若架构的 `irq_offload()` 实现允许从中断上下文（Interrupt Context）合法调用，从而在当前 CPU 上产生同步嵌套中断（Synchronous Nested Interrupt），则选择此选项。它控制 `CONFIG_IRQ_OFFLOAD_NESTED` 默认值的适用条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC
CONFIG_ARM
CONFIG_ARM64
CONFIG_X86
CONFIG_RISCV
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/Kconfig:907`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L907)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_ARCH_HAS_IRQ_PENDING_OPS"></a>

## 26.21 `CONFIG_ARCH_HAS_IRQ_PENDING_OPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

若架构的中断控制器能够设置、清除和查询单条中断线锁存的挂起状态（Latched Pending State），提供 `arch_irq_set_pending()`、`arch_irq_clear_pending()`、`arch_irq_is_pending()`，进而提供 `k_irq_*_pending()` API，则选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/Kconfig:915`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L915)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION"></a>

## 26.22 `CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持在本地声明由链接器放置的中断表（Interrupt Table）的架构选择此选项。这是 `CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED` 的前提条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM
CONFIG_ARM64
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/Kconfig:949`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L949)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_ARCH_HAS_PMU"></a>

## 26.23 `CONFIG_ARCH_HAS_PMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置后，预期 CPU 或 SoC 提供 Zephyr 性能监测单元（PMU）API，即 `<zephyr/arch/pmu.h>`，可使用的硬件性能计数器（Hardware Performance Counter）。对于 AArch64，Cortex-A 配置会选择此选项；启用 `CONFIG_ARM64_PMUV3` 可构建 ARMv8-A PMUv3 驱动后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A
```

**定义位置（Location）**：[`arch/Kconfig:1086`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1086)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)。

<a id="CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES"></a>

## 26.24 `CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果某些 RAM 页框（Page Frame）必须标记为保留，且永不用于内存映射（Memory Mapping），则应由架构选择此隐藏配置。架构需要实现 `arch_reserved_pages_update()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_ATOM
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_SERIES_CYCLONEV
CONFIG_X86_PC_COMPATIBLE
CONFIG_X86_MEMMAP
```

**被弱选择（Implied by）**

```text
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/Kconfig:1153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1153)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATOM)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)、[`CONFIG_X86_PC_COMPATIBLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_PC_COMPATIBLE)、[`CONFIG_X86_MEMMAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_MEMMAP)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ATOM`、`CONFIG_SOC_APOLLO_LAKE`。

<a id="CONFIG_ARCH_HAS_SEMIHOST"></a>

## 26.25 `CONFIG_ARCH_HAS_SEMIHOST`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

提供半主机（Semihosting）实现，即 `arch/*/core/semihost.c` 的架构选择此选项。这是 `CONFIG_SEMIHOST` 的前提条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM
CONFIG_ARM64
CONFIG_RISCV
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/Kconfig:942`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L942)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_ARCH_HAS_SUSPEND_TO_RAM"></a>

## 26.26 `CONFIG_ARCH_HAS_SUSPEND_TO_RAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择后，表示架构支持挂起到 RAM（Suspend-to-RAM，S2RAM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/Kconfig:1027`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1027)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET"></a>

## 26.27 `CONFIG_ARCH_HAS_THREAD_PRIV_STACK_SPACE_GET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构实现了 `arch_thread_priv_stack_space_get()` 时选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_X86
CONFIG_RISCV
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/Kconfig:1065`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1065)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_ARCH_IPI_LAZY_COPROCESSORS_SAVE"></a>

## 26.28 `CONFIG_ARCH_IPI_LAZY_COPROCESSORS_SAVE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构支持协处理器寄存器的多 CPU 延迟上下文切换（Lazy Context Switching）时选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_XTENSA_LAZY_HIFI_SHARING
```

**定义位置（Location）**：[`arch/Kconfig:1551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1551)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_LAZY_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_LAZY_HIFI_SHARING)。

<a id="CONFIG_ARCH_IRQ_VECTOR_TABLE_ALIGN"></a>

## 26.29 `CONFIG_ARCH_IRQ_VECTOR_TABLE_ALIGN`

**提示（Prompt）**：中断向量表对齐大小（Interrupt Vector Table Alignment Size）

**说明（Help）**

此选项控制生成的 `_irq_vector_table` 的对齐大小（Alignment Size）。某些架构要求 IRQ 向量表按架构特定大小对齐。默认值为 `0`，表示不进行对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_IRQ_VECTOR_TABLE
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`arch/Kconfig:663`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L663)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 使用生成的 IRQ 表（Generated IRQ Tables） → 生成中断向量表（Interrupt Vector Table）

**配置项引用（Symbol References）**：[`CONFIG_GEN_IRQ_VECTOR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_IRQ_VECTOR_TABLE)。

<a id="CONFIG_ARCH_IS_SET"></a>

## 26.30 `CONFIG_ARCH_IS_SET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

辅助符号（Helper Symbol），用于检测 SoC 是否忘记选择上述某个架构符号。参见顶层 `CMakeLists.txt`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC
CONFIG_ARM
CONFIG_ARM64
CONFIG_MIPS
CONFIG_OPENRISC
CONFIG_SPARC
CONFIG_X86
CONFIG_RISCV
CONFIG_XTENSA
CONFIG_TRICORE
CONFIG_ARCH_POSIX
CONFIG_HEXAGON
CONFIG_RX
```

**定义位置（Location）**：[`arch/Kconfig:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L252)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_MIPS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MIPS)、[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)、[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_HEXAGON`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HEXAGON)、[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)。

<a id="CONFIG_ARCH_MAPS_ALL_RAM"></a>

## 26.31 `CONFIG_ARCH_MAPS_ALL_RAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由架构选择此隐藏选项，告知内核在启动时映射了所有 RAM，而不只是 Zephyr 镜像（Image）范围。如果 RAM 从 `0x0` 开始，第一页必须保持未映射，以捕获 `NULL` 指针解引用。启用后，内核不会认为内核镜像之后的虚拟地址可用于新映射，而会考虑整个 RAM 映射。这通常由需要直接访问全部内存的架构设置。架构有责任在 `arch_reserved_pages_update()` 中将保留内存区域标记为保留。

内核不会通过将相关虚拟地址重新映射到其他位置来破坏该 RAM 映射，但此保证仅限于虚拟地址空间（Virtual Address Space）管理。内核的页框模型（Page Frame Ontology）完全不考虑此映射：非内核页面仍被视为空闲，除非标记为保留，而且不会设置 `K_MEM_PAGE_FRAME_MAPPED`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`arch/Kconfig:1185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1185)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT"></a>

## 26.32 `CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

目标架构支持反初始化（De-initialize）内存域（Memory Domain）时，选择此隐藏选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_MEM_DOMAIN_HAS_THREAD_LIST
```

**被选择（Selected by）**

```text
CONFIG_ARM_MMU
CONFIG_XTENSA_MMU
```

**定义位置（Location）**：[`arch/Kconfig:861`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L861)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_MEM_DOMAIN_HAS_THREAD_LIST`](P001_kernel_配置项参考_1.md#CONFIG_MEM_DOMAIN_HAS_THREAD_LIST)、[`CONFIG_ARM_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MMU)、[`CONFIG_XTENSA_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU)。

<a id="CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS"></a>

## 26.33 `CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

目标架构支持隔离同一内存域（Memory Domain）中各线程的栈（Thread Stack）时，选择此隐藏选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_RISCV_PMP
CONFIG_ARM_MPU
```

**定义位置（Location）**：[`arch/Kconfig:854`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L854)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)。

<a id="CONFIG_ARCH_POSIX"></a>

## 26.34 `CONFIG_ARCH_POSIX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

POSIX 原生架构（Native Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN
CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT
CONFIG_ARCH_HAS_THREAD_ABORT
CONFIG_ARCH_HAS_THREAD_NAME_HOOK
CONFIG_NATIVE_BUILD
CONFIG_HAS_COVERAGE_SUPPORT
CONFIG_BARRIER_OPERATIONS_BUILTIN
CONFIG_SKIP_BSS_CLEAR
CONFIG_ARCH_HAS_DIRECT_INTERRUPTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_POSIX
```

**定义位置（Location）**：[`arch/Kconfig:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L213)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN)、[`CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT)、[`CONFIG_ARCH_HAS_THREAD_ABORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_ABORT)、[`CONFIG_ARCH_HAS_THREAD_NAME_HOOK`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_HAS_THREAD_NAME_HOOK)、[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)、[`CONFIG_HAS_COVERAGE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_COVERAGE_SUPPORT)、[`CONFIG_BARRIER_OPERATIONS_BUILTIN`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_BUILTIN)、[`CONFIG_SKIP_BSS_CLEAR`](P002_kernel_配置项参考_2.md#CONFIG_SKIP_BSS_CLEAR)、[`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECT_INTERRUPTS)、[`CONFIG_SOC_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POSIX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_ABORT`。

<a id="CONFIG_ARCH_STACKWALK"></a>

## 26.35 `CONFIG_ARCH_STACKWALK`

**提示（Prompt）**：编译栈遍历函数（Stack Walking Function）

**说明（Help）**

选择 `Y` 可编译 `arch_stack_walk()` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_STACKWALK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:568`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L568)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_STACKWALK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACKWALK)。

<a id="CONFIG_ARCH_STACKWALK_MAX_FRAMES"></a>

## 26.36 `CONFIG_ARCH_STACKWALK_MAX_FRAMES`

**提示（Prompt）**：栈遍历函数最大深度（Max Depth for Stack Walk Function）

**说明（Help）**

根据具体实现，此选项可能对栈遍历函数（Stack Walk Function）可检查的栈深度施加硬性限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_STACKWALK
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`arch/Kconfig:575`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L575)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 编译栈遍历函数（Stack Walking Function）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_STACKWALK`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_STACKWALK)。

<a id="CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE"></a>

## 26.37 `CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构能够在核心转储（Coredump）期间冻结其他 CPU，并捕获其实时寄存器状态（Live Register State），而不只是每个线程最近一次换出时保存的被调用者保存上下文（Callee-saved Context）。这样可以准确回溯发生致命错误（Panic）时正在其他 CPU 上运行的线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A
```

**定义位置（Location）**：[`arch/Kconfig:989`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L989)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)。

<a id="CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING"></a>

## 26.38 `CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构代码在启用按需分页（Demand Paging）时，支持供页面逐出算法（Eviction Algorithm）使用的页面跟踪（Page Tracking）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARM64
CONFIG_X86
```

**定义位置（Location）**：[`arch/Kconfig:1012`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1012)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS"></a>

## 26.39 `CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

架构支持内存映射栈（Memory-mapped Stacks）时选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_X86
```

**定义位置（Location）**：[`arch/Kconfig:1060`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1060)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ARCH_SW_ISR_TABLE_ALIGN"></a>

## 26.40 `CONFIG_ARCH_SW_ISR_TABLE_ALIGN`

**提示（Prompt）**：软件 ISR 表对齐大小（Software ISR Table Alignment Size）

**说明（Help）**

此选项控制生成的 `_sw_isr_table` 的对齐大小（Alignment Size）。某些架构要求软件 ISR 表按架构特定大小对齐。默认大小为 `4`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_SW_ISR_TABLE
```

**默认值（Defaults）**

```text
64 if CONFIG_RISCV_HAS_CLIC
4
```

**定义位置（Location）**：[`arch/Kconfig:735`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L735)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 生成软件 ISR 表（Software ISR Table）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE)、[`CONFIG_RISCV_HAS_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_HAS_CLIC)。

<a id="CONFIG_ARM"></a>

## 26.41 `CONFIG_ARM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ARCH_SUPPORTS_COREDUMP if CONFIG_CPU_CORTEX_M
CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS if CONFIG_CPU_CORTEX_M
CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR if CONFIG_CPU_CORTEX_M
CONFIG_GEN_PRIV_STACKS
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE if CONFIG_CPU_AARCH32_CORTEX_R || CONFIG_CPU_CORTEX_M || CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_BARRIER_OPERATIONS_ARCH
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED if CONFIG_CPU_AARCH32_CORTEX_A || CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_ARCH_HAS_SEMIHOST
CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION
CONFIG_ARCH_SUPPORTS_ROM_OFFSET
CONFIG_ARCH_HAS_CPU_IDLE_HOOKS if CONFIG_CPU_CORTEX_M
CONFIG_ARCH_HAS_DIRECT_INTERRUPTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_SUN8I_H3
CONFIG_SOC_SERIES_KB106X
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_R8A77951_R7
CONFIG_SOC_R8A779F0_R52
CONFIG_SOC_R8A779G0_R52
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_AM13E23019
CONFIG_SOC_FT9001
CONFIG_SOC_FAMILY_LPC
CONFIG_SOC_SERIES_LPC11U6X
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_SERIES_LPC54XXX
CONFIG_SOC_SERIES_LPC84X
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_CORTEX_R8_VIRTUAL
CONFIG_SOC_EOS_S3
CONFIG_SOC_SERIES_SAMC20
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD20
CONFIG_SOC_SERIES_SAMD21
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_SERIES_SAML21
CONFIG_SOC_SERIES_SAMR21
CONFIG_SOC_SERIES_SAMR34
CONFIG_SOC_SERIES_SAMR35
CONFIG_SOC_SERIES_VALKYRIE
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_KB1200
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
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
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_FAMILY_MCXL
CONFIG_SOC_FAMILY_MCXN
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_SOC_SERIES_EFM32HG
CONFIG_SOC_SERIES_EFM32TG
CONFIG_SOC_SERIES_EFM32WG
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_SERIES_SIM3U
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_CM33_CPU1
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU1
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU1
CONFIG_SOC_SERIES_M031X
CONFIG_SOC_SERIES_M2L31X
CONFIG_SOC_SERIES_M333X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_SERIES_NRF51
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_TI_LM3S6965
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX8MQ6_M4
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_GD32L23X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_CC32XX
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_SERIES_NPCM4
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_FAMILY_ENSEMBLE_APSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZA2M
CONFIG_SOC_SERIES_RZG2L
CONFIG_SOC_SERIES_RZG2UL
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_SERIES_RZG3S
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_SERIES_RZV2L
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
CONFIG_SOC_SERIES_B1
CONFIG_SOC_EM32F967
CONFIG_SOC_SERIES_SAM3X
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_SAM4L
CONFIG_SOC_SERIES_SAM4S
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_SMARTFUSION2
CONFIG_SOC_RV1106
CONFIG_SOC_SERIES_XMC4XXX
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_XC7ZXXX
CONFIG_SOC_SERIES_XC7ZXXXS
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F0X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_BEETLE
CONFIG_SOC_SERIES_DESIGNSTART
CONFIG_SOC_V8A_AARCH32
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_SERIES_MPS2
CONFIG_SOC_SERIES_MPS3
CONFIG_SOC_SERIES_MPS4
CONFIG_SOC_SERIES_MUSCA
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_SERIES_CYCLONEV
CONFIG_SOC_SERIES_S32K1
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`arch/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ARCH_SUPPORTS_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR)、[`CONFIG_GEN_PRIV_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_PRIV_STACKS)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_BARRIER_OPERATIONS_ARCH`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_ARCH)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_ARCH_HAS_SEMIHOST`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SEMIHOST)、[`CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION)、[`CONFIG_ARCH_SUPPORTS_ROM_OFFSET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_OFFSET)、[`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS)、[`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECT_INTERRUPTS)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_SUN8I_H3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN8I_H3)、[`CONFIG_SOC_SERIES_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KB106X)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_R8A77951_R7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_R7)、[`CONFIG_SOC_R8A779F0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_R52)、[`CONFIG_SOC_R8A779G0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_R52)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)、[`CONFIG_SOC_SERIES_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC11U6X)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_SERIES_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC84X)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_CORTEX_R8_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORTEX_R8_VIRTUAL)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_SERIES_SAML21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_SERIES_SAMR34`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_VALKYRIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_VALKYRIE)、[`CONFIG_SOC_BCM58402_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXL)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_SERIES_EFM32HG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32HG)、[`CONFIG_SOC_SERIES_EFM32TG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32TG)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SERIES_SIM3U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIM3U)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M031X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M031X)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_TI_LM3S6965`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_TI_LM3S6965)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX8MQ6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6_M4)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_APSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZA2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA2M)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_EM32F967`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EM32F967)、[`CONFIG_SOC_SERIES_SAM3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_SMARTFUSION2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_SOC_RV1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RV1106)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_XC7ZXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_SOC_SERIES_XC7ZXXXS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXXS)、[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_SOC_SERIES_DESIGNSTART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DESIGNSTART)、[`CONFIG_SOC_V8A_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A_AARCH32)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_SERIES_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_SOC_SERIES_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS3)、[`CONFIG_SOC_SERIES_MPS4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MPS4)、[`CONFIG_SOC_SERIES_MUSCA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MUSCA)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP`、`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`、`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`、`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_SUN8I_H3`、`CONFIG_SOC_R8A779G0_R52`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_FAMILY_LPC`、`CONFIG_SOC_SERIES_LPC11U6X`、`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_SERIES_LPC84X`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_RA2L1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXL`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_RV1106`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F0X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WL3X`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_V8A_AARCH32`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_ARM64"></a>

## 26.42 `CONFIG_ARM64`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM64（AArch64）架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_64BIT
CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK
CONFIG_ARCH_SUPPORTS_COREDUMP
CONFIG_HAS_ARM_SMCCC
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_BARRIER_OPERATIONS_ARCH
CONFIG_ARCH_HAS_BIT_REV
CONFIG_ARCH_HAS_DIRECTED_IPIS
CONFIG_ARCH_HAS_DEMAND_PAGING
CONFIG_ARCH_HAS_DEMAND_MAPPING
CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING
CONFIG_EVICTION_TRACKING if CONFIG_DEMAND_PAGING
CONFIG_MEM_DOMAIN_HAS_THREAD_LIST if CONFIG_ARM_MPU && CONFIG_USERSPACE
CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED
CONFIG_ARCH_HAS_SEMIHOST
CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION
CONFIG_ARCH_SUPPORTS_ROM_OFFSET
CONFIG_ARCH_HAS_CPU_IDLE_HOOKS
CONFIG_ARCH_HAS_IRQ_PENDING_OPS if !CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A77951_A57
CONFIG_SOC_R8A77961
CONFIG_SOC_R8A779F0_A55
CONFIG_SOC_R8A779G0_A76
CONFIG_SOC_R8A78000_A720
CONFIG_SOC_SUN50I_H618
CONFIG_SOC_BCM2712
CONFIG_SOC_BCM58402_A72
CONFIG_SOC_BCM2711
CONFIG_SOC_SERIES_AM62LX_A53
CONFIG_SOC_SERIES_AM62X_A53
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_MIMX9111
CONFIG_SOC_MIMX9131
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_MIMX94398_A55
CONFIG_SOC_MIMX9596_A55
CONFIG_SOC_MIMX9529_A55
CONFIG_SOC_BCM2710
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_SERIES_RZA3M
CONFIG_SOC_SERIES_RZA3UL
CONFIG_SOC_SERIES_AGILEX
CONFIG_SOC_SERIES_AGILEX5
CONFIG_SOC_RK3399
CONFIG_SOC_RK3568
CONFIG_SOC_RK3588
CONFIG_SOC_RK3588S
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_SOC_LS1046A
CONFIG_SOC_V8A
CONFIG_SOC_V9A
CONFIG_SOC_A320
CONFIG_SOC_FVP_AEMV8R_AARCH64
CONFIG_SOC_QEMU_CORTEX_A53
CONFIG_SOC_QEMU_VIRT_ARM64
CONFIG_SOC_XENVM
CONFIG_SOC_QNXHV_VM
CONFIG_SOC_MT8188_A55
```

**定义位置（Location）**：[`arch/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_FWARGS_HANDLER_HOOK)、[`CONFIG_ARCH_SUPPORTS_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP)、[`CONFIG_HAS_ARM_SMCCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_ARM_SMCCC)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_BARRIER_OPERATIONS_ARCH`](P001_kernel_配置项参考_1.md#CONFIG_BARRIER_OPERATIONS_ARCH)、[`CONFIG_ARCH_HAS_BIT_REV`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_BIT_REV)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_ARCH_HAS_DEMAND_PAGING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DEMAND_PAGING)、[`CONFIG_ARCH_HAS_DEMAND_MAPPING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DEMAND_MAPPING)、[`CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING)、[`CONFIG_EVICTION_TRACKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EVICTION_TRACKING)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_MEM_DOMAIN_HAS_THREAD_LIST`](P001_kernel_配置项参考_1.md#CONFIG_MEM_DOMAIN_HAS_THREAD_LIST)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)、[`CONFIG_ARCH_HAS_SEMIHOST`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_SEMIHOST)、[`CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_ISR_TABLES_LOCAL_DECLARATION)、[`CONFIG_ARCH_SUPPORTS_ROM_OFFSET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_OFFSET)、[`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS)、[`CONFIG_ARCH_HAS_IRQ_PENDING_OPS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_PENDING_OPS)、[`CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)、[`CONFIG_SOC_R8A77951_A57`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_A57)、[`CONFIG_SOC_R8A77961`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77961)、[`CONFIG_SOC_R8A779F0_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_A55)、[`CONFIG_SOC_R8A779G0_A76`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_A76)、[`CONFIG_SOC_R8A78000_A720`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_A720)、[`CONFIG_SOC_SUN50I_H618`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN50I_H618)、[`CONFIG_SOC_BCM2712`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2712)、[`CONFIG_SOC_BCM58402_A72`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_A72)、[`CONFIG_SOC_BCM2711`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2711)、[`CONFIG_SOC_SERIES_AM62LX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62LX_A53)、[`CONFIG_SOC_SERIES_AM62X_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_A53)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_MIMX9111`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9111)、[`CONFIG_SOC_MIMX9131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9131)、[`CONFIG_SOC_MIMX9352_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_MIMX94398_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_A55)、[`CONFIG_SOC_MIMX9596_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_A55)、[`CONFIG_SOC_MIMX9529_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_A55)、[`CONFIG_SOC_BCM2710`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2710)、[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_SERIES_RZA3M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_SERIES_AGILEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AGILEX)、[`CONFIG_SOC_SERIES_AGILEX5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AGILEX5)、[`CONFIG_SOC_RK3399`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3399)、[`CONFIG_SOC_RK3568`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3568)、[`CONFIG_SOC_RK3588`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588)、[`CONFIG_SOC_RK3588S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588S)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_SOC_LS1046A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LS1046A)、[`CONFIG_SOC_V8A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A)、[`CONFIG_SOC_V9A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V9A)、[`CONFIG_SOC_A320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_A320)、[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)、[`CONFIG_SOC_QEMU_CORTEX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_CORTEX_A53)、[`CONFIG_SOC_QEMU_VIRT_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_ARM64)、[`CONFIG_SOC_XENVM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XENVM)、[`CONFIG_SOC_QNXHV_VM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QNXHV_VM)、[`CONFIG_SOC_MT8188_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_A55)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_COREDUMP`、`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_SOC_R8A779G0_A76`、`CONFIG_SOC_SUN50I_H618`、`CONFIG_SOC_BCM2712`、`CONFIG_SOC_BCM2711`、`CONFIG_SOC_BCM2710`、`CONFIG_SOC_RK3399`、`CONFIG_SOC_RK3568`、`CONFIG_SOC_RK3588`、`CONFIG_SOC_RK3588S`、`CONFIG_SOC_V8A`、`CONFIG_SOC_V9A`、`CONFIG_SOC_A320`、`CONFIG_SOC_FVP_AEMV8R_AARCH64`、`CONFIG_SOC_QEMU_CORTEX_A53`、`CONFIG_SOC_QEMU_VIRT_ARM64`、`CONFIG_SOC_XENVM`、`CONFIG_SOC_QNXHV_VM`。

<a id="CONFIG_BIG_ENDIAN"></a>

## 26.43 `CONFIG_BIG_ENDIAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项告知构建系统，目标采用大端字节序（Big-endian）。默认采用小端架构（Little-endian），应保持不选中此项。由 `arch/$ARCH/Kconfig`、`soc/**/Kconfig` 或 `boards/**/Kconfig` 选择，用户通常应避免修改。此选项用于选择链接脚本的 `OUTPUT_FORMAT`、工具链标志 `TOOLCHAIN_C_FLAGS` 和 `TOOLCHAIN_LD_FLAGS`，以及 `gen_isr_tables.py` 的命令行选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_OPENRISC
CONFIG_SPARC
```

**定义位置（Location）**：[`arch/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)、[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)。

<a id="CONFIG_CACHE_CAN_SAY_MEM_COHERENCE"></a>

## 26.44 `CONFIG_CACHE_CAN_SAY_MEM_COHERENCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后会定义 `sys_cache_is_mem_coherent()`。该函数可判断指针是否位于一致性区域（Coherence Region）内，因而能够在多处理器代码中安全使用，而不需要显式刷新（Flush）或失效（Invalidate）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
```

**定义位置（Location）**：[`arch/Kconfig:1496`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1496)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_CACHE_DOUBLEMAP"></a>

## 26.45 `CONFIG_CACHE_DOUBLEMAP`

**提示（Prompt）**：缓存双重映射支持（Cache Double-mapping Support）［已弃用］

**说明（Help）**

双重映射（Double-mapping）使指针能够以较低成本转换为指向同一内存的不同地址，分别采用缓存／非缓存（Cached/Uncached）访问。这适用于原文所称的 CPU 内多处理不一致性（Intra-CPU Multiprocessing Incoherence），仅在 `MP_MAX_NUM_CPUS > 1` 时有意义。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`arch/Kconfig:1390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1390)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS"></a>

## 26.46 `CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS`

**提示（Prompt）**：支持缓存与非缓存访问的镜像内存区域（Mirrored Memory Regions）

**说明（Help）**

如果硬件在不同地址提供镜像内存区域（Mirrored Memory Region），访问其中一处经过缓存，访问另一处则直达内存，请启用此项。指针可低成本地转换为缓存或非缓存（Cached/Uncached）访问。这适用于原文所称的 CPU 内多处理不一致性（Intra-CPU Multiprocessing Incoherence），仅在 `MP_MAX_NUM_CPUS > 1` 时有意义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CACHE_INCOHERENT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE15
CONFIG_SOC_SERIES_INTEL_ADSP_ACE20
CONFIG_SOC_SERIES_INTEL_ADSP_ACE30
CONFIG_SOC_SERIES_INTEL_ADSP_ACE40
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_CACHE_DOUBLEMAP
```

**定义位置（Location）**：[`arch/Kconfig:1378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1378)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CACHE_INCOHERENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_CACHE_INCOHERENT)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE15)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE20)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE30)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE40)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_CACHE_DOUBLEMAP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_DOUBLEMAP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_INTEL_ADSP_ACE15`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE20`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE30`、`CONFIG_SOC_SERIES_INTEL_ADSP_ACE40`。

<a id="CONFIG_CACHE_MANAGEMENT"></a>

## 26.47 `CONFIG_CACHE_MANAGEMENT`

**提示（Prompt）**：缓存管理功能（Cache Management Features）

**说明（Help）**

此选项启用由架构或驱动代码实现的缓存管理函数（Cache Management Functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DCACHE || CONFIG_ICACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_MIMXRT1189_CM33
CONFIG_SOC_MIMXRT1186_CM33
CONFIG_SOC_MIMXRT1185_CM33
CONFIG_SOC_MIMXRT118C_CM33
CONFIG_SOC_MIMXRT1187_CM33
CONFIG_SOC_MIMXRT1182
CONFIG_SOC_MIMXRT1181
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_SERIES_PSE84_M55
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
CONFIG_SOC_RTS5817
CONFIG_CRYPTO_MCUX_DCP
CONFIG_STM32_LTDC
CONFIG_DMA_XILINX_ADMA
CONFIG_ETH_XLNX_GEM
CONFIG_ETH_DWC_ETHER_QOS_CORE
CONFIG_ETH_DWC_ETHER_1000_CORE
CONFIG_I2C_STM32_V2_DMA
CONFIG_I2S_SILABS_SIWX91X
CONFIG_I2S_STM32
CONFIG_I2S_STM32_SAI
CONFIG_INTEL_VTD_ICTL
CONFIG_RCAR_MMC_DMA_SUPPORT
CONFIG_SAM_SDMMC
CONFIG_SDHC_STM32_DMA_MODE
CONFIG_SDHC_TI_AM654_ENABLE_ADMA
CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT
CONFIG_SPI_MAX32_DMA
CONFIG_SPI_STM32_DMA
CONFIG_LLEXT
```

**定义位置（Location）**：[`arch/Kconfig:1401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1401)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_MIMXRT1189_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1189_CM33)、[`CONFIG_SOC_MIMXRT1186_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1186_CM33)、[`CONFIG_SOC_MIMXRT1185_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1185_CM33)、[`CONFIG_SOC_MIMXRT118C_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT118C_CM33)、[`CONFIG_SOC_MIMXRT1187_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1187_CM33)、[`CONFIG_SOC_MIMXRT1182`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1182)、[`CONFIG_SOC_MIMXRT1181`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1181)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_SERIES_PSE84_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M55)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_CRYPTO_MCUX_DCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRYPTO_MCUX_DCP)、[`CONFIG_STM32_LTDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_LTDC)、[`CONFIG_DMA_XILINX_ADMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_XILINX_ADMA)、[`CONFIG_ETH_XLNX_GEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_XLNX_GEM)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_I2C_STM32_V2_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_STM32_V2_DMA)、[`CONFIG_I2S_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_SILABS_SIWX91X)、[`CONFIG_I2S_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_STM32)、[`CONFIG_I2S_STM32_SAI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_STM32_SAI)、[`CONFIG_INTEL_VTD_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTEL_VTD_ICTL)、[`CONFIG_RCAR_MMC_DMA_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RCAR_MMC_DMA_SUPPORT)、[`CONFIG_SAM_SDMMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SAM_SDMMC)、[`CONFIG_SDHC_STM32_DMA_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_STM32_DMA_MODE)、[`CONFIG_SDHC_TI_AM654_ENABLE_ADMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_TI_AM654_ENABLE_ADMA)、[`CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT)、[`CONFIG_SPI_MAX32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MAX32_DMA)、[`CONFIG_SPI_STM32_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_STM32_DMA)、[`CONFIG_LLEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_MIMXRT1189_CM33`、`CONFIG_SOC_MIMXRT1186_CM33`、`CONFIG_SOC_MIMXRT1185_CM33`、`CONFIG_SOC_MIMXRT118C_CM33`、`CONFIG_SOC_MIMXRT1187_CM33`、`CONFIG_SOC_MIMXRT1182`、`CONFIG_SOC_MIMXRT1181`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_SERIES_PSE84_M55`、`CONFIG_SOC_RTS5817`。

<a id="CONFIG_CACHE_TYPE"></a>

## 26.48 `CONFIG_CACHE_TYPE`

**提示（Prompt）**：缓存类型（Cache Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT
```

**默认值（Defaults）**

```text
CONFIG_ARCH_CACHE
```

**可选项（Choices）**

```text
CONFIG_ARCH_CACHE
CONFIG_SOC_CACHE
CONFIG_EXTERNAL_CACHE
```

**定义位置（Location）**：[`arch/Kconfig:1472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1472)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_ARCH_CACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_CACHE)、[`CONFIG_SOC_CACHE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SOC_CACHE)、[`CONFIG_EXTERNAL_CACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_EXTERNAL_CACHE)。

<a id="CONFIG_CODE_DATA_RELOCATION"></a>

## 26.49 `CONFIG_CODE_DATA_RELOCATION`

**提示（Prompt）**：支持代码／数据段重定位（Code/Data Section Relocation）

**说明（Help）**

启用将指定文件的 `.text`、`data` 和 `.bss` 段重定位（Relocate）并放入所选内存区域的支持。要重定位的文件和目标区域应在 `CMakeLists.txt` 中通过 `zephyr_code_relocate()` 指定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_CODE_DATA_RELOCATION
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXE31X
CONFIG_CODE_DATA_RELOCATION_SRAM
CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_FLASH_BFLB
CONFIG_SOC_FLASH_MCUX_C40
```

**定义位置（Location）**：[`arch/Kconfig:1298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1298)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CODE_DATA_RELOCATION)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_CODE_DATA_RELOCATION_SRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CODE_DATA_RELOCATION_SRAM)、[`CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_FLASH_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_BFLB)、[`CONFIG_SOC_FLASH_MCUX_C40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_MCUX_C40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`。

<a id="CONFIG_CPU_CACHE_INCOHERENT"></a>

## 26.50 `CONFIG_CPU_CACHE_INCOHERENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有非一致性缓存（Incoherent Cache）时应选择此隐藏配置。这适用于原文所称的 CPU 内多处理不一致性（Intra-CPU Multiprocessing Incoherence），仅在 `MP_MAX_NUM_CPUS > 1` 时有意义。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`arch/Kconfig:1173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1173)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_CPU_HAS_DCACHE"></a>

## 26.51 `CONFIG_CPU_HAS_DCACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有数据缓存（Data Cache，D-cache）时，应选择此隐藏配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32P4
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_MIMXRT1011
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_MIMXRT1175_CM4
CONFIG_SOC_MIMXRT1176_CM4
CONFIG_SOC_MIMXRT1166_CM4
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_LITEX_VEXRISCV
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_ACP_7_X
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_FAMILY_INTEL_ADSP
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_XTENSA_DC233C
CONFIG_SOC_ACP_7_0
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_RTS5817
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_ACP_6_0
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_SOC_MT8186_ADSP
CONFIG_SOC_MT8188_ADSP
CONFIG_SOC_MT8195_ADSP
CONFIG_SOC_MT8196_ADSP
CONFIG_SOC_MT8365_ADSP
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_CPU_EM6
CONFIG_CPU_HS3X
CONFIG_CPU_HS4X
CONFIG_CPU_HS5X
CONFIG_CPU_HS6X
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
CONFIG_CPU_CORTEX_A5
CONFIG_CPU_CORTEX_A7
CONFIG_CPU_CORTEX_A9
CONFIG_CPU_CORTEX_A32
CONFIG_CPU_CORTEX_R5
CONFIG_CPU_CORTEX_R52
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_CPU_XUANTIE_E907
CONFIG_CPU_ATOM
CONFIG_CPU_APOLLO_LAKE
CONFIG_CPU_LAKEMONT_VALUE
CONFIG_CPU_LAKEMONT_PERF
```

**定义位置（Location）**：[`arch/Kconfig:1168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1168)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_MIMXRT1175_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1175_CM4)、[`CONFIG_SOC_MIMXRT1176_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1176_CM4)、[`CONFIG_SOC_MIMXRT1166_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1166_CM4)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_LITEX_VEXRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXRISCV)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_ACP_7_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_X)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)、[`CONFIG_SOC_ACP_7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_7_0)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_ACP_6_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_6_0)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_MT8186_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8186_ADSP)、[`CONFIG_SOC_MT8188_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_ADSP)、[`CONFIG_SOC_MT8195_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8195_ADSP)、[`CONFIG_SOC_MT8196_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8196_ADSP)、[`CONFIG_SOC_MT8365_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8365_ADSP)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_CPU_EM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_EM6)、[`CONFIG_CPU_HS3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS6X)、[`CONFIG_CPU_CORTEX_M52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M85)、[`CONFIG_CPU_CORTEX_A5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A5)、[`CONFIG_CPU_CORTEX_A7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A7)、[`CONFIG_CPU_CORTEX_A9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A9)、[`CONFIG_CPU_CORTEX_A32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A32)、[`CONFIG_CPU_CORTEX_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R5)、[`CONFIG_CPU_CORTEX_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R52)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)、[`CONFIG_CPU_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_ATOM)、[`CONFIG_CPU_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_APOLLO_LAKE)、[`CONFIG_CPU_LAKEMONT_VALUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LAKEMONT_VALUE)、[`CONFIG_CPU_LAKEMONT_PERF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LAKEMONT_PERF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_MIMXRT1175_CM4`、`CONFIG_SOC_MIMXRT1176_CM4`、`CONFIG_SOC_MIMXRT1166_CM4`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_LITEX_VEXRISCV`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_ACP_7_X`、`CONFIG_SOC_FAMILY_INTEL_ADSP`、`CONFIG_SOC_XTENSA_DC233C`、`CONFIG_SOC_ACP_7_0`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_ACP_6_0`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_CPU_HAS_DCLS"></a>

## 26.52 `CONFIG_CPU_HAS_DCLS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器硬件支持双冗余内核锁步（Dual-redundant Core Lock-step，DCLS）拓扑时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_R8A77951_R7
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`arch/Kconfig:1105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1105)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_R8A77951_R7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_R7)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_CPU_HAS_DSP"></a>

## 26.53 `CONFIG_CPU_HAS_DSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有硬件数字信号处理（DSP）单元时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_ARC_HSDK4XD
```

**定义位置（Location）**：[`arch/Kconfig:1117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1117)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_HSDK4XD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_HSDK4XD)。

<a id="CONFIG_CPU_HAS_FPU"></a>

## 26.54 `CONFIG_CPU_HAS_FPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有硬件浮点单元（Floating Point Unit）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_ARC_HSDK
CONFIG_SOC_AM13E23019
CONFIG_SOC_FT9001
CONFIG_SOC_ARC_IOT
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_LPC54628
CONFIG_SOC_LPC55S06
CONFIG_SOC_LPC55S16
CONFIG_SOC_LPC55S26
CONFIG_SOC_LPC55S28
CONFIG_SOC_LPC55S36
CONFIG_SOC_LPC55S69_CPU0
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_EOS_S3
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_RP2350A_M33_0
CONFIG_SOC_RP2350B_M33_0
CONFIG_SOC_EMSDP_EM5D
CONFIG_SOC_EMSDP_EM7D
CONFIG_SOC_EMSDP_EM7D_ESP
CONFIG_SOC_EMSDP_EM9D
CONFIG_SOC_EMSDP_EM11D
CONFIG_SOC_KB1200
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
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
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_SERIES_MCXA1X6
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_MCXW2XX
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
CONFIG_SOC_FAMILY_SILABS_S2_XG21
CONFIG_SOC_FAMILY_SILABS_S2_XG22
CONFIG_SOC_FAMILY_SILABS_S2_XG23
CONFIG_SOC_FAMILY_SILABS_S2_XG24
CONFIG_SOC_FAMILY_SILABS_S2_XG26
CONFIG_SOC_FAMILY_SILABS_S2_XG27
CONFIG_SOC_FAMILY_SILABS_S2_XG28
CONFIG_SOC_FAMILY_SILABS_S2_XG29
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_MIMXRT1011
CONFIG_SOC_MIMXRT1015
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
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
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_MK22F51212
CONFIG_SOC_MK22F12
CONFIG_SOC_MK64F12
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_EMSK_EM9D
CONFIG_SOC_EMSK_EM11D
CONFIG_SOC_NRF52832
CONFIG_SOC_NRF52833
CONFIG_SOC_NRF52840
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
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX8MQ6_M4
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_ARC_HSDK4XD
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_SERIES_TC4X
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_SERIES_B1
CONFIG_SOC_GR716A
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_XMC4XXX
CONFIG_SOC_POSIX
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_SERIES_M48X
CONFIG_SOC_SERIES_NSIM_HS
CONFIG_SOC_SERIES_NSIM_SEM
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_AN521_CPU1
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
CONFIG_SOC_MUSCA_S1
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_S32K142
CONFIG_SOC_S32K142W
CONFIG_SOC_S32K144
CONFIG_SOC_S32K144W
CONFIG_SOC_S32K146
CONFIG_SOC_S32K148
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_CPU_HAS_VFP
CONFIG_CPU_HAS_NEON
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_RISCV_ISA_EXT_F
CONFIG_CPU_ATOM
CONFIG_CPU_APOLLO_LAKE
CONFIG_CPU_LAKEMONT_VALUE
CONFIG_CPU_LAKEMONT_PERF
CONFIG_CPU_RXV2
CONFIG_CPU_RXV3
CONFIG_CPU_RXV3E
CONFIG_CPU_TC162
CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION
```

**定义位置（Location）**：[`arch/Kconfig:1111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1111)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_ARC_HSDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_HSDK)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_ARC_IOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_IOT)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_LPC54628`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54628)、[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_SOC_LPC55S16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S16)、[`CONFIG_SOC_LPC55S26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S26)、[`CONFIG_SOC_LPC55S28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S28)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_LPC55S69_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S69_CPU0)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_RP2350A_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33_0)、[`CONFIG_SOC_RP2350B_M33_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33_0)、[`CONFIG_SOC_EMSDP_EM5D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM5D)、[`CONFIG_SOC_EMSDP_EM7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM7D)、[`CONFIG_SOC_EMSDP_EM7D_ESP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM7D_ESP)、[`CONFIG_SOC_EMSDP_EM9D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM9D)、[`CONFIG_SOC_EMSDP_EM11D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM11D)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_MCXA1X6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X6)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_MCXW2XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXW2XX)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_EFM32WG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32WG)、[`CONFIG_SOC_SERIES_EFM32GG11B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_MIMXRT1015`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1015)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU1)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU1)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_MK22F51212`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F51212)、[`CONFIG_SOC_MK22F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F12)、[`CONFIG_SOC_MK64F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK64F12)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_EMSK_EM9D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM9D)、[`CONFIG_SOC_EMSK_EM11D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM11D)、[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52833)、[`CONFIG_SOC_NRF52840`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52840)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L05_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX8MQ6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6_M4)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_ARC_HSDK4XD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_HSDK4XD)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_GR716A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GR716A)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)、[`CONFIG_SOC_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POSIX)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_SERIES_M48X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M48X)、[`CONFIG_SOC_SERIES_NSIM_HS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_HS)、[`CONFIG_SOC_SERIES_NSIM_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_SEM)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_AN521_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521_CPU1)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)、[`CONFIG_SOC_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MUSCA_S1)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_S32K142`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142)、[`CONFIG_SOC_S32K142W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K142W)、[`CONFIG_SOC_S32K144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144)、[`CONFIG_SOC_S32K144W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K144W)、[`CONFIG_SOC_S32K146`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K146)、[`CONFIG_SOC_S32K148`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K148)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_CPU_HAS_VFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_VFP)、[`CONFIG_CPU_HAS_NEON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_NEON)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_RISCV_ISA_EXT_F`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_CPU_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_ATOM)、[`CONFIG_CPU_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_APOLLO_LAKE)、[`CONFIG_CPU_LAKEMONT_VALUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LAKEMONT_VALUE)、[`CONFIG_CPU_LAKEMONT_PERF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LAKEMONT_PERF)、[`CONFIG_CPU_RXV2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_RXV2)、[`CONFIG_CPU_RXV3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_RXV3)、[`CONFIG_CPU_RXV3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_RXV3E)、[`CONFIG_CPU_TC162`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_TC162)、[`CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_ARC_HSDK`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_LPC54628`、`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_LPC55S16`、`CONFIG_SOC_LPC55S26`、`CONFIG_SOC_LPC55S28`、`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_LPC55S69_CPU0`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_MCXA1X6`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_MCXW2XX`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_MIMXRT1015`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU1`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU1`、`CONFIG_SOC_MK22F51212`、`CONFIG_SOC_MK22F12`、`CONFIG_SOC_MK64F12`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF52832`、`CONFIG_SOC_NRF52833`、`CONFIG_SOC_NRF52840`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY_M4`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_SERIES_TC4X`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_GR716A`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_NSIM_HS`、`CONFIG_SOC_SERIES_NSIM_SEM`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_S32K142`、`CONFIG_SOC_S32K142W`、`CONFIG_SOC_S32K144`、`CONFIG_SOC_S32K144W`、`CONFIG_SOC_S32K146`、`CONFIG_SOC_S32K148`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_CPU_TC162`。

<a id="CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION"></a>

## 26.55 `CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，表示 CPU 具有双精度浮点单元（Double-precision Floating Point Unit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT1015
CONFIG_SOC_MIMXRT1021
CONFIG_SOC_MIMXRT1024
CONFIG_SOC_MIMXRT1041
CONFIG_SOC_MIMXRT1042
CONFIG_SOC_MIMXRT1051
CONFIG_SOC_MIMXRT1052
CONFIG_SOC_MIMXRT1062
CONFIG_SOC_MIMXRT1064
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_TC4X
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_VFP_FEATURE_DOUBLE_PRECISION
CONFIG_RISCV_ISA_EXT_D
CONFIG_CPU_RXV3E
```

**定义位置（Location）**：[`arch/Kconfig:1122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1122)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_MIMXRT1015`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1015)、[`CONFIG_SOC_MIMXRT1021`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1021)、[`CONFIG_SOC_MIMXRT1024`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1024)、[`CONFIG_SOC_MIMXRT1041`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1041)、[`CONFIG_SOC_MIMXRT1042`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1042)、[`CONFIG_SOC_MIMXRT1051`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1051)、[`CONFIG_SOC_MIMXRT1052`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1052)、[`CONFIG_SOC_MIMXRT1062`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1062)、[`CONFIG_SOC_MIMXRT1064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1064)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_VFP_FEATURE_DOUBLE_PRECISION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VFP_FEATURE_DOUBLE_PRECISION)、[`CONFIG_RISCV_ISA_EXT_D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_CPU_RXV3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_RXV3E)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT1015`、`CONFIG_SOC_MIMXRT1021`、`CONFIG_SOC_MIMXRT1024`、`CONFIG_SOC_MIMXRT1041`、`CONFIG_SOC_MIMXRT1042`、`CONFIG_SOC_MIMXRT1051`、`CONFIG_SOC_MIMXRT1052`、`CONFIG_SOC_MIMXRT1062`、`CONFIG_SOC_MIMXRT1064`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_SERIES_TC4X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_CPU_HAS_ICACHE"></a>

## 26.56 `CONFIG_CPU_HAS_ICACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有指令缓存（Instruction Cache，I-cache）时，应选择此隐藏配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_LPC55S36
CONFIG_SOC_SR100
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_MCXW716C
CONFIG_SOC_MCXW727C
CONFIG_SOC_MCXW70AC
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_MIMXRT1011
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_MIMXRT1175_CM4
CONFIG_SOC_MIMXRT1176_CM4
CONFIG_SOC_MIMXRT1166_CM4
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_NRF54L_CPUAPP_COMMON
CONFIG_SOC_NRF7120_ENGA_CPUAPP
CONFIG_SOC_NRF7120E_ENGA_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_SERIES_AMEBAD
CONFIG_SOC_SERIES_AMEBADPLUS
CONFIG_SOC_SERIES_AMEBAG2
CONFIG_SOC_LITEX_VEXRISCV
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_FAMILY_INTEL_ADSP
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_XTENSA_DC233C
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_FAMILY_MAX32_M33
CONFIG_SOC_FAMILY_MAX32_M4
CONFIG_SOC_RTS5817
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_CPU_EM6
CONFIG_CPU_HS3X
CONFIG_CPU_HS4X
CONFIG_CPU_HS5X
CONFIG_CPU_HS6X
CONFIG_CPU_CORTEX_M52
CONFIG_CPU_CORTEX_M55
CONFIG_CPU_CORTEX_M85
CONFIG_CPU_CORTEX_A5
CONFIG_CPU_CORTEX_A7
CONFIG_CPU_CORTEX_A9
CONFIG_CPU_CORTEX_A32
CONFIG_CPU_CORTEX_R5
CONFIG_CPU_CORTEX_R52
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`arch/Kconfig:1180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1180)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_LPC55S36`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S36)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)、[`CONFIG_SOC_MCXW727C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW727C)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_MIMXRT1175_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1175_CM4)、[`CONFIG_SOC_MIMXRT1176_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1176_CM4)、[`CONFIG_SOC_MIMXRT1166_CM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1166_CM4)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_NRF54L_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L_CPUAPP_COMMON)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_SERIES_AMEBAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAD)、[`CONFIG_SOC_SERIES_AMEBADPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBADPLUS)、[`CONFIG_SOC_SERIES_AMEBAG2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AMEBAG2)、[`CONFIG_SOC_LITEX_VEXRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXRISCV)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_FAMILY_MAX32_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M33)、[`CONFIG_SOC_FAMILY_MAX32_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_M4)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_CPU_EM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_EM6)、[`CONFIG_CPU_HS3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS6X)、[`CONFIG_CPU_CORTEX_M52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M52)、[`CONFIG_CPU_CORTEX_M55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M55)、[`CONFIG_CPU_CORTEX_M85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M85)、[`CONFIG_CPU_CORTEX_A5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A5)、[`CONFIG_CPU_CORTEX_A7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A7)、[`CONFIG_CPU_CORTEX_A9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A9)、[`CONFIG_CPU_CORTEX_A32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A32)、[`CONFIG_CPU_CORTEX_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R5)、[`CONFIG_CPU_CORTEX_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R52)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LPC55S36`、`CONFIG_SOC_SR100`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_MCXW716C`、`CONFIG_SOC_MCXW727C`、`CONFIG_SOC_MCXW70AC`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_MIMXRT1175_CM4`、`CONFIG_SOC_MIMXRT1176_CM4`、`CONFIG_SOC_MIMXRT1166_CM4`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF54L_CPUAPP_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_SERIES_AMEBAD`、`CONFIG_SOC_SERIES_AMEBADPLUS`、`CONFIG_SOC_SERIES_AMEBAG2`、`CONFIG_SOC_LITEX_VEXRISCV`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`、`CONFIG_SOC_FAMILY_INTEL_ADSP`、`CONFIG_SOC_XTENSA_DC233C`、`CONFIG_SOC_FAMILY_MAX32_M33`、`CONFIG_SOC_FAMILY_MAX32_M4`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_CPU_HAS_MMU"></a>

## 26.57 `CONFIG_CPU_HAS_MMU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有内存管理单元（Memory Management Unit，MMU）时，选择此隐藏选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_XTENSA_DC233C
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CPU_ARM926EJ_S
CONFIG_ARMV8_A
CONFIG_ARMV9_A
CONFIG_X86
```

**定义位置（Location）**：[`arch/Kconfig:1134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1134)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_ARM926EJ_S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_ARM926EJ_S)、[`CONFIG_ARMV8_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV8_A)、[`CONFIG_ARMV9_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV9_A)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_XTENSA_DC233C`。

<a id="CONFIG_CPU_HAS_MPU"></a>

## 26.58 `CONFIG_CPU_HAS_MPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 具有内存保护单元（Memory Protection Unit，MPU）时，启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_ARC_IOT
CONFIG_SOC_EMSDP_EM4
CONFIG_SOC_EMSDP_EM5D
CONFIG_SOC_EMSDP_EM6
CONFIG_SOC_EMSDP_EM7D
CONFIG_SOC_EMSDP_EM7D_ESP
CONFIG_SOC_EMSDP_EM9D
CONFIG_SOC_EMSDP_EM11D
CONFIG_SOC_EMSK_EM7D
CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32
CONFIG_SOC_SERIES_NSIM_EM
CONFIG_SOC_SERIES_NSIM_HS
CONFIG_SOC_SERIES_NSIM_SEM
CONFIG_SOC_SERIES_NSIM_VPX5
CONFIG_SOC_FVP_AEMV8R_AARCH64
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_QEMU_ARC
CONFIG_CPU_HAS_ARM_MPU
CONFIG_CPU_HAS_NXP_SYSMPU
CONFIG_RISCV_PMP
```

**定义位置（Location）**：[`arch/Kconfig:1129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1129)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_IOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_IOT)、[`CONFIG_SOC_EMSDP_EM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM4)、[`CONFIG_SOC_EMSDP_EM5D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM5D)、[`CONFIG_SOC_EMSDP_EM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM6)、[`CONFIG_SOC_EMSDP_EM7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM7D)、[`CONFIG_SOC_EMSDP_EM7D_ESP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM7D_ESP)、[`CONFIG_SOC_EMSDP_EM9D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM9D)、[`CONFIG_SOC_EMSDP_EM11D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSDP_EM11D)、[`CONFIG_SOC_EMSK_EM7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM7D)、[`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32)、[`CONFIG_SOC_SERIES_NSIM_EM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_EM)、[`CONFIG_SOC_SERIES_NSIM_HS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_HS)、[`CONFIG_SOC_SERIES_NSIM_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_SEM)、[`CONFIG_SOC_SERIES_NSIM_VPX5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_VPX5)、[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_QEMU_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_ARC)、[`CONFIG_CPU_HAS_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_CPU_HAS_NXP_SYSMPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_NXP_SYSMPU)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_XTENSA_SAMPLE_CONTROLLER32`、`CONFIG_SOC_SERIES_NSIM_EM`、`CONFIG_SOC_SERIES_NSIM_HS`、`CONFIG_SOC_SERIES_NSIM_SEM`、`CONFIG_SOC_SERIES_NSIM_VPX5`、`CONFIG_SOC_FVP_AEMV8R_AARCH64`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_QEMU_ARC`。

<a id="CONFIG_CPU_HAS_TEE"></a>

## 26.59 `CONFIG_CPU_HAS_TEE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CPU 支持可信执行环境（Trusted Execution Environment）时，例如具有安全属性单元（Security Attribution Unit），启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_HAS_RENESAS_RA_IDAU
CONFIG_ARC_HAS_SECURE
CONFIG_CPU_HAS_ARM_SAU
CONFIG_CPU_HAS_NRF_IDAU
```

**定义位置（Location）**：[`arch/Kconfig:1098`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1098)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_RENESAS_RA_IDAU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_RENESAS_RA_IDAU)、[`CONFIG_ARC_HAS_SECURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_HAS_SECURE)、[`CONFIG_CPU_HAS_ARM_SAU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_ARM_SAU)、[`CONFIG_CPU_HAS_NRF_IDAU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_NRF_IDAU)。

<a id="CONFIG_DCACHE"></a>

## 26.60 `CONFIG_DCACHE`

**提示（Prompt）**：数据缓存（Data Cache，D-cache）支持

**说明（Help）**

此选项启用数据缓存（Data Cache，D-cache）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DCACHE
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_INTEL_EMMC_HOST_DMA
CONFIG_RCAR_MMC_DMA_SUPPORT
```

**定义位置（Location）**：[`arch/Kconfig:1364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1364)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_INTEL_EMMC_HOST_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_EMMC_HOST_DMA)、[`CONFIG_RCAR_MMC_DMA_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RCAR_MMC_DMA_SUPPORT)。

<a id="CONFIG_DCACHE_LINE_SIZE"></a>

## 26.61 `CONFIG_DCACHE_LINE_SIZE`

**提示（Prompt）**：数据缓存行大小（D-cache Line Size）

**说明（Help）**

CPU 数据缓存行（D-cache Line）的大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DCACHE
```

**默认值（Defaults）**

```text
0 if n
64 if CONFIG_64BIT
32
```

**取值范围（Ranges）**

```text
[2, 4294967295]
```

**定义位置（Location）**：[`arch/Kconfig:1427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1427)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_DCACHE_LINE_SIZE_DETECT"></a>

## 26.62 `CONFIG_DCACHE_LINE_SIZE_DETECT`

**提示（Prompt）**：在运行时检测数据缓存行大小（D-cache Line Size）

**说明（Help）**

启用通过查询某个 SoC 寄存器来确定数据缓存行大小（D-cache Line Size）的功能，代价是增加内存和代码占用，并略微延长启动时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT && CONFIG_DCACHE
```

**定义位置（Location）**：[`arch/Kconfig:1419`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1419)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT"></a>

## 26.63 `CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平台实现了通过查询某个 SoC 寄存器来确定数据缓存行大小（D-cache Line Size）的功能。只有实现缓存 API（Cache API）的软件组件，即架构／SoC 层或驱动，才应选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_EM6
CONFIG_CPU_HS3X
CONFIG_CPU_HS4X
CONFIG_CPU_HS5X
CONFIG_CPU_HS6X
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CACHE_ANDES
CONFIG_CACHE_ASPEED
```

**定义位置（Location）**：[`arch/Kconfig:1408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1408)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_EM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_EM6)、[`CONFIG_CPU_HS3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS6X)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CACHE_ANDES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_ANDES)、[`CONFIG_CACHE_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_ASPEED)。

<a id="CONFIG_DCLS"></a>

## 26.64 `CONFIG_DCLS`

**提示（Prompt）**：处理器配置为双冗余内核锁步（DCLS）模式

**说明（Help）**

处理器硬件配置为双冗余内核锁步（Dual-redundant Core Lock-step，DCLS）拓扑时，启用此选项。如果处理器支持 DCLS，但默认配置为或在烧写时改为分离锁步模式（Split-lock Mode），则应禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DCLS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:1205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1205)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DCLS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCLS)。

<a id="CONFIG_DSP_SHARING"></a>

## 26.65 `CONFIG_DSP_SHARING`

原库同名定义共 2 条；本项为数据库第 5217 条记录，各定义分别保留。

**提示（Prompt）**：DSP 寄存器共享（Register Sharing）

**说明（Help）**

此选项启用在上下文切换（Context Switch）期间保存硬件 DSP 寄存器，以允许多个线程并发执行 DSP 运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_DSP
```

**定义位置（Location）**：[`arch/Kconfig:1309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1309)。

**菜单路径（Menu Path）**：顶层（Top） → DSP 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_DSP`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DSP)。

<a id="CONFIG_DYNAMIC_INTERRUPTS"></a>

## 26.66 `CONFIG_DYNAMIC_INTERRUPTS`

**提示（Prompt）**：运行时安装 IRQ（Installation of IRQs at Runtime）

**说明（Help）**

启用运行时安装中断，将部分中断相关数据结构从 ROM 移至 RAM，并可能在某些架构上增加代码体积。此功能需要可写的软件 ISR 表（Software ISR Table），因此无法与 `CONFIG_GEN_SW_ISR_TABLE_SWITCH` 配合使用，因为后者生成的是 `switch` 语句而非数组。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_GEN_SW_ISR_TABLE_SWITCH
```

**主动选择（Selects）**

```text
CONFIG_SRAM_SW_ISR_TABLE
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32C2
CONFIG_SOC_SERIES_ESP32C3
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C6
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32H2
CONFIG_SOC_SERIES_ESP32P4
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_CC32XX
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
CONFIG_BT_BFLB_BL60X
CONFIG_BT_BFLB_BL70X
CONFIG_BT_BFLB_BL70XL
CONFIG_BT_BFLB_BL808
CONFIG_COUNTER_XLNX_TTC
CONFIG_IEEE802154_BFLB
CONFIG_GIC_V3_ITS
CONFIG_MBOX_ANDES_PLIC_SW
CONFIG_UART_NS16550
CONFIG_SMBUS_INTEL_PCH
CONFIG_LEON_GPTIMER
CONFIG_UDC_KINETIS
CONFIG_UDC_NXP_EHCI
CONFIG_UHC_NXP_EHCI
CONFIG_UHC_NXP_KHCI
CONFIG_UHC_RENESAS_RA
```

**定义位置（Location）**：[`arch/Kconfig:614`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L614)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE_SWITCH`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE_SWITCH)、[`CONFIG_SRAM_SW_ISR_TABLE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_SW_ISR_TABLE)、[`CONFIG_NRF_802154_RADIO_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)、[`CONFIG_BT_BFLB_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL60X)、[`CONFIG_BT_BFLB_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_BFLB_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_BFLB_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL808)、[`CONFIG_COUNTER_XLNX_TTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_XLNX_TTC)、[`CONFIG_IEEE802154_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IEEE802154_BFLB)、[`CONFIG_GIC_V3_ITS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3_ITS)、[`CONFIG_MBOX_ANDES_PLIC_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX_ANDES_PLIC_SW)、[`CONFIG_UART_NS16550`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NS16550)、[`CONFIG_SMBUS_INTEL_PCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMBUS_INTEL_PCH)、[`CONFIG_LEON_GPTIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_LEON_GPTIMER)、[`CONFIG_UDC_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_KINETIS)、[`CONFIG_UDC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_NXP_EHCI)、[`CONFIG_UHC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_EHCI)、[`CONFIG_UHC_NXP_KHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_KHCI)、[`CONFIG_UHC_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_SR100`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_DYNAMIC_OBJECTS"></a>

## 26.67 `CONFIG_DYNAMIC_OBJECTS`

**提示（Prompt）**：允许在运行时分配内核对象（Kernel Objects）

**说明（Help）**

启用后，允许从调用线程的资源池（Resource Pool）请求内核对象（Kernel Object）。由于需要额外的运行时表来验证这些对象，会有少量性能成本。通过这种方式分配的对象，可由仅限监管者模式（Supervisor-only）的 API 调用释放，也可在对象引用数降为零时释放。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_DYNAMIC_THREAD
```

**被弱选择（Implied by）**

```text
CONFIG_TEST_ENABLE_USERSPACE
```

**定义位置（Location）**：[`arch/Kconfig:528`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L528)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_TEST_ENABLE_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_ENABLE_USERSPACE)。

<a id="CONFIG_DYNAMIC_OBJECTS_FORCE_STACK_CACHED"></a>

## 26.68 `CONFIG_DYNAMIC_OBJECTS_FORCE_STACK_CACHED`

**提示（Prompt）**：强制将分配的线程栈对象（Thread Stack Objects）放在缓存区域

**说明（Help）**

启用内核一致性（Kernel Coherence）后，栈可能分配在非缓存区域（Uncached Area），从而影响性能。启用此选项后，会强制将栈指针转换为指向缓存区域（Cached Area）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_KERNEL_COHERENCE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:541`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L541)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_KERNEL_COHERENCE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_COHERENCE)。

<a id="CONFIG_EMPTY_IRQ_SPURIOUS"></a>

## 26.69 `CONFIG_EMPTY_IRQ_SPURIOUS`

**提示（Prompt）**：创建空的伪中断处理程序（Spurious Interrupt Handler）

**说明（Help）**

此选项改变伪中断处理程序（Spurious Interrupt Handler）的函数体。启用后，处理程序仅包含无限 `while` 循环；禁用后，包含完整的 Zephyr 故障处理流程（Fault Handling Procedure）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS
```

**定义位置（Location）**：[`arch/Kconfig:821`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L821)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_EMPTY_IRQ_SPURIOUS`。

<a id="CONFIG_EXCEPTION_DEBUG"></a>

## 26.70 `CONFIG_EXCEPTION_DEBUG`

**提示（Prompt）**：未处理异常调试（Unhandled Exception Debugging）

**说明（Help）**

为各种 CPU 异常／陷阱向量（Exception/Trap Vector）安装处理程序，使调试更容易，代价是少量代码体积增加。会打印具体异常向量及相关错误码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PRINTK || CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:791`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L791)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

<a id="CONFIG_EXTERNAL_CACHE"></a>

## 26.71 `CONFIG_EXTERNAL_CACHE`

**提示（Prompt）**：外部缓存控制器（External Cache Controller）

**说明（Help）**

外部缓存控制器（External Cache Controller）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:1489`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1489)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options） → 缓存类型（Cache Type）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_TYPE)。

<a id="CONFIG_EXTRA_EXCEPTION_INFO"></a>

## 26.72 `CONFIG_EXTRA_EXCEPTION_INFO`

**提示（Prompt）**：收集额外异常信息（Extra Exception Info）

**说明（Help）**

此选项启用在发生故障（Fault）时收集寄存器状态等额外信息，有助于事后分析（Post-mortem Analysis）和问题调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO
```

**被选择（Selected by）**

```text
CONFIG_CPU_AARCH32_CORTEX_A
```

**定义位置（Location）**：[`arch/Kconfig:801`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L801)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_EXTRA_EXCEPTION_INFO`。

<a id="CONFIG_FLASH_BASE_ADDRESS"></a>

## 26.73 `CONFIG_FLASH_BASE_ADDRESS`

**提示（Prompt）**：Flash 基地址（Base Address）

**说明（Help）**

此选项指定开发板上 Flash 的基地址（Base Address），通常由开发板的 defconfig 文件设置，用户一般应避免通过菜单配置修改。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC || CONFIG_ARM || CONFIG_ARM64 || CONFIG_X86 || CONFIG_RISCV || CONFIG_RX || CONFIG_OPENRISC || CONFIG_ARCH_POSIX || CONFIG_HEXAGON || CONFIG_TRICORE
```

**默认值（Defaults）**

```text
0x0 if (CONFIG_XIP && (CONFIG_ARM || CONFIG_ARM64)) || !CONFIG_ARM
0 if !CONFIG_XIP
```

**定义位置（Location）**：[`arch/Kconfig:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_HEXAGON`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HEXAGON)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

<a id="CONFIG_FLASH_SIZE"></a>

## 26.74 `CONFIG_FLASH_SIZE`

**提示（Prompt）**：Flash 大小（Size，kB）

**说明（Help）**

此选项指定 Flash 大小，以 kB 为单位，通常由开发板的 defconfig 文件设置，用户一般应避免通过菜单配置修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC || CONFIG_ARM || CONFIG_ARM64 || CONFIG_X86 || CONFIG_RISCV || CONFIG_RX || CONFIG_OPENRISC || CONFIG_ARCH_POSIX || CONFIG_HEXAGON || CONFIG_TRICORE
```

**默认值（Defaults）**

```text
0 if (CONFIG_XIP && (CONFIG_ARM || CONFIG_ARM64)) || !CONFIG_ARM
0 if !CONFIG_XIP
```

**定义位置（Location）**：[`arch/Kconfig:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L350)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_OPENRISC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_OPENRISC)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_HEXAGON`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HEXAGON)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

<a id="CONFIG_FPU"></a>

## 26.75 `CONFIG_FPU`

**提示（Prompt）**：浮点单元（Floating Point Unit，FPU）

**说明（Help）**

此选项启用硬件浮点单元（Floating Point Unit，FPU），以支持使用浮点寄存器和指令。启用后，默认各线程只能独占使用浮点寄存器，通常意味着只有一个线程可以执行浮点运算。如果多个线程需要并发执行浮点运算，必须启用“FPU 寄存器共享（FPU Register Sharing）”，在上下文切换时保存浮点寄存器。如果平台启用了允许编译器将浮点指令用于通用整数操作的架构专用选项，则会自动启用此共享功能。

注意，不包含硬件浮点单元的平台不能选择此选项；这些平台的浮点支持取决于工具链是否提供软件浮点库（Software Floating Point Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
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
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
CONFIG_NXP_PMC_TMPSNS
CONFIG_NXP_TMPSNS
CONFIG_2SMPB_02E
CONFIG_D6F
CONFIG_ICP201XX
CONFIG_NXP_WIFI_CSI_AMI
CONFIG_NXP_WIFI_WLS
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_SERIES_TC4X
CONFIG_CPU_HAS_VFP
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_CPU_TC162
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:1320`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1320)。

**菜单路径（Menu Path）**：顶层（Top） → 浮点选项（Floating Point Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)、[`CONFIG_NXP_PMC_TMPSNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_PMC_TMPSNS)、[`CONFIG_NXP_TMPSNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_TMPSNS)、[`CONFIG_2SMPB_02E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_2SMPB_02E)、[`CONFIG_D6F`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_D6F)、[`CONFIG_ICP201XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP201XX)、[`CONFIG_NXP_WIFI_CSI_AMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_CSI_AMI)、[`CONFIG_NXP_WIFI_WLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_WLS)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)、[`CONFIG_CPU_HAS_VFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_VFP)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_CPU_TC162`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_TC162)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_SERIES_TC4X`、`CONFIG_CPU_TC162`。

<a id="CONFIG_FPU_SHARING"></a>

## 26.76 `CONFIG_FPU_SHARING`

**提示（Prompt）**：FPU 寄存器共享（Register Sharing）

**说明（Help）**

此选项启用在上下文切换（Context Switch）期间保存硬件浮点寄存器，以允许多个线程并发执行浮点运算。注意，某些编译器配置可能为任意线程生成浮点指令，从而激活浮点上下文（Floating Point Context）；这些线程换入和换出时必须保存该上下文。如果能够保证镜像代码不会在唯一获准使用浮点的线程上下文之外生成浮点指令，开发者仍可在应用项目中禁用浮点共享模式，切换为非共享浮点寄存器模式（Unshared FP Registers Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU
```

**被选择（Selected by）**

```text
CONFIG_FP_HARDABI
CONFIG_FP_SOFTABI
CONFIG_BT_BFLB_BL60X
CONFIG_BT_BFLB_BL70X
CONFIG_BT_BFLB_BL70XL
CONFIG_BT_BFLB_BL61X
CONFIG_BT_BFLB_BL616CL
CONFIG_BT_BFLB_BL808
```

**被弱选择（Implied by）**

```text
CONFIG_ARMV7_M_ARMV8_M_FP
CONFIG_CPU_HAS_VFP
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
```

**定义位置（Location）**：[`arch/Kconfig:1343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1343)。

**菜单路径（Menu Path）**：顶层（Top） → 浮点选项（Floating Point Options） → 浮点单元（Floating Point Unit，FPU）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_FP_HARDABI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FP_HARDABI)、[`CONFIG_FP_SOFTABI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FP_SOFTABI)、[`CONFIG_BT_BFLB_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL60X)、[`CONFIG_BT_BFLB_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL70X)、[`CONFIG_BT_BFLB_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL70XL)、[`CONFIG_BT_BFLB_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL61X)、[`CONFIG_BT_BFLB_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL616CL)、[`CONFIG_BT_BFLB_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BFLB_BL808)、[`CONFIG_ARMV7_M_ARMV8_M_FP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_M_ARMV8_M_FP)、[`CONFIG_CPU_HAS_VFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HAS_VFP)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)。

<a id="CONFIG_FRAME_POINTER"></a>

## 26.77 `CONFIG_FRAME_POINTER`

**提示（Prompt）**：使用帧指针编译内核（Compile with Frame Pointers）

**说明（Help）**

选择 `Y` 可获得精确的栈跟踪（Stack Trace），代价是体积略增、速度略降。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT
```

**定义位置（Location）**：[`arch/Kconfig:561`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L561)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT)。

<a id="CONFIG_GEN_IRQ_START_VECTOR"></a>

## 26.78 `CONFIG_GEN_IRQ_START_VECTOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在某些架构上，部分向量表（Vector Table）为系统异常保留，且独立于 `gen_isr_tables.py` 创建的表声明。创建这些表时，会从 `CONFIG_NUM_IRQS` 减去此值，以获得正确大小。这是隐藏选项，应由各架构设置，用户应保持不变。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_ISR_TABLES
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/Kconfig:746`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L746)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GEN_ISR_TABLES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_ISR_TABLES)。

<a id="CONFIG_GEN_IRQ_VECTOR_TABLE"></a>

## 26.79 `CONFIG_GEN_IRQ_VECTOR_TABLE`

**提示（Prompt）**：生成中断向量表（Interrupt Vector Table）

**说明（Help）**

此选项控制使用 `gen_isr_tables` 的平台是否需要生成中断向量表（Interrupt Vector Table）。仅当平台完全不使用向量表，或要求向量表采用按 IRQ 线索引的函数指针数组之外的格式时，才应禁用。后一种情况下，向量表必须由应用程序或架构代码提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_ISR_TABLES
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_OPENTITAN
CONFIG_CPU_XUANTIE_E907
CONFIG_NRFX_CLIC
```

**定义位置（Location）**：[`arch/Kconfig:651`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L651)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 使用生成的 IRQ 表（Generated IRQ Tables）

**配置项引用（Symbol References）**：[`CONFIG_GEN_ISR_TABLES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_ISR_TABLES)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)、[`CONFIG_NRFX_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NRFX_CLIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_OPENTITAN`、`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_GEN_ISR_TABLES"></a>

## 26.80 `CONFIG_GEN_ISR_TABLES`

**提示（Prompt）**：使用生成的 IRQ 表（Generated IRQ Tables）

**说明（Help）**

此选项控制平台是否使用 `gen_isr_tables` 脚本生成中断表（Interrupt Table）。该机制会创建合适的硬件向量表（Hardware Vector Table）和／或软件 IRQ 表。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT798S_HIFI1
CONFIG_SOC_MIMXRT758S_HIFI1
CONFIG_SOC_MIMXRT735S_HIFI1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_QEMU_HEXAGON_VIRT
```

**定义位置（Location）**：[`arch/Kconfig:644`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L644)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_QEMU_HEXAGON_VIRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_HEXAGON_VIRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_HEXAGON_VIRT`。

<a id="CONFIG_GEN_PRIV_STACKS"></a>

## 26.81 `CONFIG_GEN_PRIV_STACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构要求将提权栈（Privilege Elevation Stack）分配在单独的内存区域，则选择此项。这通常见于 MPU 要求区域按 2 的幂对齐、大小也为 2 的幂的架构。

待修复（FIXME）：应移除此选项，改为检查 `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`，但这需要同时修改 ARM 和 ARC。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARC_MPU
CONFIG_PMP_POWER_OF_TWO_ALIGNMENT
CONFIG_ARM
```

**定义位置（Location）**：[`arch/Kconfig:486`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L486)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_PMP_POWER_OF_TWO_ALIGNMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMP_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)。

<a id="CONFIG_GEN_SW_ISR_TABLE"></a>

## 26.82 `CONFIG_GEN_SW_ISR_TABLE`

**提示（Prompt）**：生成软件 ISR 表（Software ISR Table）

**说明（Help）**

此选项控制使用 `gen_isr_tables` 的平台是否需要生成软件 ISR 表（Software ISR Table）。可生成数组或 `switch-case`，参见 `CONFIG_GEN_SW_ISR_TABLE_TYPE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_ISR_TABLES
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GEN_ISR_TABLES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_ISR_TABLES)。

<a id="CONFIG_GEN_SW_ISR_TABLE_ARRAY"></a>

## 26.83 `CONFIG_GEN_SW_ISR_TABLE_ARRAY`

**提示（Prompt）**：生成 ISR 条目数组（Array of ISR Entries）

**说明（Help）**

这是由 `struct _isr_table_entry` 组成的数组，包含中断服务例程（ISR）及其参数。每个中断都有自己的条目。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_SW_ISR_TABLE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:718`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L718)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 生成软件 ISR 表（Software ISR Table） → 允许选择 ISR 表（ISR Table）的实现方式

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE_TYPE)。

<a id="CONFIG_GEN_SW_ISR_TABLE_SWITCH"></a>

## 26.84 `CONFIG_GEN_SW_ISR_TABLE_SWITCH`

**提示（Prompt）**：生成包含 `switch-case` 的函数

**说明（Help）**

使用 `switch-case` 而非数组。当大多数 IRQ 未使用时，有助于限制二进制大小（Binary Size）：公共的重复条目被合并到单个 `default` 块中，少数已使用中断则各自具有 `case` 块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GEN_SW_ISR_TABLE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:725`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L725)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 生成软件 ISR 表（Software ISR Table） → 允许选择 ISR 表（ISR Table）的实现方式

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE_TYPE)。

<a id="CONFIG_GEN_SW_ISR_TABLE_TYPE"></a>

## 26.85 `CONFIG_GEN_SW_ISR_TABLE_TYPE`

**提示（Prompt）**：允许选择 ISR 表（ISR Table）的实现方式

**说明（Help）**

`CONFIG_GEN_SW_ISR_TABLE_ARRAY` 是默认选项，不确定时应使用它。`GEN_SW_ISR_TABLE_SWITCH` 可在某些场景中优化二进制大小（Binary Size），但如果系统分配了大量 ISR，也可能增加编号较大 ISR 开始执行前的延迟（Latency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_SW_ISR_TABLE
```

**默认值（Defaults）**

```text
CONFIG_GEN_SW_ISR_TABLE_ARRAY
```

**可选项（Choices）**

```text
CONFIG_GEN_SW_ISR_TABLE_ARRAY
CONFIG_GEN_SW_ISR_TABLE_SWITCH
```

**定义位置（Location）**：[`arch/Kconfig:708`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L708)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → 生成软件 ISR 表（Software ISR Table）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE)、[`CONFIG_GEN_SW_ISR_TABLE_ARRAY`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE_ARRAY)、[`CONFIG_GEN_SW_ISR_TABLE_SWITCH`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE_SWITCH)。

<a id="CONFIG_HEXAGON"></a>

## 26.86 `CONFIG_HEXAGON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Qualcomm Hexagon DSP 架构（Architecture）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ARCH_IS_SET
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_HEXAGON_VIRT
```

**定义位置（Location）**：[`arch/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_IS_SET`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IS_SET)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT)、[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_SOC_QEMU_HEXAGON_VIRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_HEXAGON_VIRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`、`CONFIG_SOC_QEMU_HEXAGON_VIRT`。

<a id="CONFIG_HW_STACK_PROTECTION"></a>

## 26.87 `CONFIG_HW_STACK_PROTECTION`

**提示（Prompt）**：硬件栈保护（Hardware Stack Protection）

**说明（Help）**

选择此选项，以启用基于硬件的平台功能，在系统以特权模式（Privileged Mode）运行时捕获栈溢出（Stack Overflow）。未启用 `CONFIG_USERSPACE` 时，系统始终以特权模式运行。注意，此功能不一定能够阻止数据损坏，触发故障时也不能对整个系统状态作出保证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_STACK_PROTECTION
```

**被选择（Selected by）**

```text
CONFIG_TEST_HW_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/Kconfig:399`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L399)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_TEST_HW_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_HW_STACK_PROTECTION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`。

<a id="CONFIG_ICACHE"></a>

## 26.88 `CONFIG_ICACHE`

**提示（Prompt）**：指令缓存（Instruction Cache，I-cache）支持

**说明（Help）**

此选项启用指令缓存（Instruction Cache，I-cache）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ICACHE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/Kconfig:1371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1371)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)。

<a id="CONFIG_ICACHE_LINE_SIZE"></a>

## 26.89 `CONFIG_ICACHE_LINE_SIZE`

**提示（Prompt）**：指令缓存行大小（I-cache Line Size）

**说明（Help）**

CPU 指令缓存行（I-cache Line）的大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICACHE
```

**默认值（Defaults）**

```text
0 if n
64 if CONFIG_64BIT
32
```

**取值范围（Ranges）**

```text
[2, 4294967295]
```

**定义位置（Location）**：[`arch/Kconfig:1458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1458)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_ICACHE_LINE_SIZE_DETECT"></a>

## 26.90 `CONFIG_ICACHE_LINE_SIZE_DETECT`

**提示（Prompt）**：在运行时检测指令缓存行大小（I-cache Line Size）

**说明（Help）**

启用通过查询某个 SoC 寄存器来确定指令缓存行大小（I-cache Line Size）的功能，代价是增加内存和代码占用，并略微延长启动时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT && CONFIG_ICACHE
```

**定义位置（Location）**：[`arch/Kconfig:1450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1450)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE)。

<a id="CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT"></a>

## 26.91 `CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平台实现了通过查询某个 SoC 寄存器来确定指令缓存行大小（I-cache Line Size）的功能。只有实现缓存 API（Cache API）的软件组件，即架构／SoC 层或驱动，才应选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_EM6
CONFIG_CPU_HS3X
CONFIG_CPU_HS4X
CONFIG_CPU_HS5X
CONFIG_CPU_HS6X
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CACHE_ANDES
CONFIG_CACHE_ASPEED
```

**定义位置（Location）**：[`arch/Kconfig:1439`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L1439)。

**菜单路径（Menu Path）**：顶层（Top） → 缓存选项（Cache Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_EM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_EM6)、[`CONFIG_CPU_HS3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS3X)、[`CONFIG_CPU_HS4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS4X)、[`CONFIG_CPU_HS5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS5X)、[`CONFIG_CPU_HS6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_HS6X)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CACHE_ANDES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_ANDES)、[`CONFIG_CACHE_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_ASPEED)。

<a id="CONFIG_INIT_ARCH_HW_AT_BOOT"></a>

## 26.92 `CONFIG_INIT_ARCH_HW_AT_BOOT`

**提示（Prompt）**：启动时初始化内部架构状态（Internal Architecture State）

**说明（Help）**

此选项要求 Zephyr 在启动时，强制将内部架构状态（Architectural State），例如架构级硬件寄存器和系统控制块，初始化为相应架构手册规定的复位值（Reset Value）。当 Zephyr 固件镜像由调试器或引导加载程序链式加载（Chain-load），且需要保证架构内核模块的内部状态恢复到架构规定的复位值时，此选项很有用。

注意：此功能与架构相关，具体实现请参阅支持该功能的各架构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X_CM85
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_SERIES_M031X
CONFIG_SOC_SERIES_M335X
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32WB0X
```

**被弱选择（Implied by）**

```text
CONFIG_BUILD_WITH_TFM
CONFIG_BOOTLOADER_MCUBOOT
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`arch/Kconfig:831`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L831)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X_CM85)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_SERIES_M031X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M031X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_ARCH_HW_INIT`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X_CM85`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32WB0X`。

<a id="CONFIG_IRQ_OFFLOAD"></a>

## 26.93 `CONFIG_IRQ_OFFLOAD`

**提示（Prompt）**：IRQ 卸载（IRQ Offload）

**说明（Help）**

启用 `irq_offload()` API，允许在中断上下文（Interrupt Context）中同步运行函数。仅对需要验证内核对象在 IRQ 上下文中正确性的测试用例有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST
```

**定义位置（Location）**：[`arch/Kconfig:758`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L758)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)。

<a id="CONFIG_IRQ_OFFLOAD_NESTED"></a>

## 26.94 `CONFIG_IRQ_OFFLOAD_NESTED`

**提示（Prompt）**：`irq_offload()` 支持嵌套 IRQ（Nested IRQs）

**说明（Help）**

由平台层设置时，表示允许在中断上下文（Interrupt Context）中合法调用 `irq_offload()`，以在当前 CPU 上产生同步嵌套中断（Synchronous Nested Interrupt）。并非所有硬件都支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IRQ_OFFLOAD
```

**默认值（Defaults）**

```text
y if CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED
```

**定义位置（Location）**：[`arch/Kconfig:781`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L781)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_IRQ_OFFLOAD`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_OFFLOAD)、[`CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_IRQ_OFFLOAD_NESTED)。

<a id="CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS"></a>

## 26.95 `CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS`

**提示（Prompt）**：按地址跳转（Jump by Address）

**说明（Help）**

IRQ 向量表（Vector Table）包含中断处理程序的地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IRQ_VECTOR_TABLE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L685)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → IRQ 向量表类型（Vector Table Type）

**配置项引用（Symbol References）**：[`CONFIG_IRQ_VECTOR_TABLE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_VECTOR_TABLE_TYPE)。

<a id="CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE"></a>

## 26.96 `CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE`

**提示（Prompt）**：按指令跳转（Jump by Code）

**说明（Help）**

IRQ 向量表（Vector Table）包含跳转到中断处理程序地址的跳转指令操作码（Opcode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IRQ_VECTOR_TABLE_TYPE>
```

**定义位置（Location）**：[`arch/Kconfig:690`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L690)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration） → IRQ 向量表类型（Vector Table Type）

**配置项引用（Symbol References）**：[`CONFIG_IRQ_VECTOR_TABLE_TYPE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_VECTOR_TABLE_TYPE)。

<a id="CONFIG_IRQ_VECTOR_TABLE_TYPE"></a>

## 26.97 `CONFIG_IRQ_VECTOR_TABLE_TYPE`

**提示（Prompt）**：IRQ 向量表类型（Vector Table Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_IRQ_VECTOR_TABLE
```

**默认值（Defaults）**

```text
CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE if CONFIG_RISCV && !CONFIG_RISCV_HAS_CLIC
CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS
```

**可选项（Choices）**

```text
CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS
CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE
```

**定义位置（Location）**：[`arch/Kconfig:679`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L679)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_GEN_IRQ_VECTOR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_IRQ_VECTOR_TABLE)、[`CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_HAS_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_HAS_CLIC)、[`CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS)。

<a id="CONFIG_ISR_TABLES_LOCAL_DECLARATION"></a>

## 26.98 `CONFIG_ISR_TABLES_LOCAL_DECLARATION`

**提示（Prompt）**：本地创建 ISR 表并由链接器放置（Placed by Linker）

**说明（Help）**

启用新的中断表生成方案（Interrupt Table Generation）。这是完全不同的生成器，会在调用 `IRQ_CONNECT` 宏的位置本地创建表项，再通过链接脚本将其放在内存中的正确位置。主要优势是生成的中断表兼容链接时优化（Link Time Optimization，LTO）；缺点是需要架构移植层提供支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED && CONFIG_GEN_IRQ_VECTOR_TABLE
```

**定义位置（Location）**：[`arch/Kconfig:601`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L601)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 中断配置（Interrupt Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED)、[`CONFIG_GEN_IRQ_VECTOR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_IRQ_VECTOR_TABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED`。

<a id="CONFIG_KOBJECT_DATA_AREA_RESERVE_EXTRA_PERCENT"></a>

## 26.99 `CONFIG_KOBJECT_DATA_AREA_RESERVE_EXTRA_PERCENT`

**提示（Prompt）**：预留额外内核对象数据区（Kobject Data Area，百分比）

**说明（Help）**

用于计算内核对象（Kobject）元数据哈希表（Metadata Hash Table）占位预留空间大小的乘数。该哈希表由 gperf 生成，强烈依赖内核对象的绝对地址，而这些地址可能在不同预构建（Prebuilt）阶段之间变化。为在最终链接各阶段预留足够哈希表空间，并保持内核对象位置不变，预留大小按第一次预构建的大小，加上按此百分比计算的额外空间确定；百分比的基数是第一次预构建中的内核对象数据区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`arch/Kconfig:464`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L464)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_KOBJECT_RODATA_AREA_EXTRA_BYTES"></a>

## 26.100 `CONFIG_KOBJECT_RODATA_AREA_EXTRA_BYTES`

**提示（Prompt）**：为内核对象只读数据区（Kobject Rodata Area）预留额外字节

**说明（Help）**

为内核对象元数据（Kobject Metadata）的只读数据（RODATA）区域多预留一些字节，以应对 gperf 生成表大小的不确定性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`arch/Kconfig:478`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig#L478)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<!-- kconfig-navigation -->

[上一章](P025_module_xenlib_Kconfig_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P027_arch_Kconfig_配置项参考_2.md)
