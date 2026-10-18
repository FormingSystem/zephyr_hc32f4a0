---
id: learning.zephyr-docs.kconfig-reference.page-34
title: "`arch/riscv`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第34章\_`arch/riscv`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `arch/riscv` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARCH_HAS_STACKWALK"></a>

## 34.1 `CONFIG_ARCH_HAS_STACKWALK`

原库同名定义共 5 条；本项为数据库第 501 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，表示已实现 `arch_stack_walk()` API，且可以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/riscv/Kconfig:764`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L764)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_CLIC_SUPPORT_INTERRUPT_LEVEL"></a>

## 34.2 `CONFIG_CLIC_SUPPORT_INTERRUPT_LEVEL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

适用于具有扩展中断级别（Extended Interrupt Level）的内核本地中断控制器（CLIC）实现：编号较高的中断级别可以抢占编号较低的中断级别。此选项在中断服务例程（ISR）中处理中断级别，以确保嵌套 ISR 正确退出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_HAS_CLIC && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_HAS_CLIC
```

**定义位置（Location）**：[`arch/riscv/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_HAS_CLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CLIC)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_CPU_HAS_ANDES_EXECIT"></a>

## 34.3 `CONFIG_CPU_HAS_ANDES_EXECIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持 `EXEC.IT` 指令（Instruction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_CPU_HAS_ANDES_HSP"></a>

## 34.4 `CONFIG_CPU_HAS_ANDES_HSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持 StackSafe 扩展（Extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_CPU_HAS_ANDES_HWDSP"></a>

## 34.5 `CONFIG_CPU_HAS_ANDES_HWDSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持硬件数字信号处理（DSP）扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_CPU_HAS_ANDES_NMI"></a>

## 34.6 `CONFIG_CPU_HAS_ANDES_NMI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持 Andes 不可屏蔽中断（NMI）扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_CPU_HAS_ANDES_PFT"></a>

## 34.7 `CONFIG_CPU_HAS_ANDES_PFT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持 PowerBrake 扩展（Extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_CPU_HAS_ANDES_PMA"></a>

## 34.8 `CONFIG_CPU_HAS_ANDES_PMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AndesCore 支持可编程物理内存属性（Programmable PMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)。

<a id="CONFIG_CUSTOM_STACK_GUARD"></a>

## 34.9 `CONFIG_CUSTOM_STACK_GUARD`

**提示（Prompt）**：基于自定义栈保护机制的线程栈保护（Thread Stack Guards）

**说明（Help）**

通过自定义栈保护机制（Custom Stack Guard）启用线程／中断栈保护（Thread / Interrupt Stack Guards）。此功能必须得到硬件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**被弱选择（Implied by）**

```text
CONFIG_RISCV_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/riscv/Kconfig:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L685)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_RISCV_STACK_PROTECTION`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_STACK_PROTECTION)。

<a id="CONFIG_CUSTOM_STACK_GUARD_RESERVED_SIZE"></a>

## 34.10 `CONFIG_CUSTOM_STACK_GUARD_RESERVED_SIZE`

**提示（Prompt）**：自定义栈保护保留区大小（Custom Stack Guard Reserved Area Size）

**说明（Help）**

自定义栈保护保留区（Custom Stack Guard Reserved Area）的大小。该区域应足够大，以捕获栈指针（Stack Pointer）减小时的任何突然跨越，并留出一定余量，以容纳最终发生溢出异常（Overflow Exception）时的栈用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CUSTOM_STACK_GUARD && CONFIG_RISCV
```

**默认值（Defaults）**

```text
1024 if CONFIG_64BIT
768
```

**定义位置（Location）**：[`arch/riscv/Kconfig:693`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L693)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → 基于自定义栈保护机制的线程栈保护（Thread Stack Guards）

**配置项引用（Symbol References）**：[`CONFIG_CUSTOM_STACK_GUARD`](P034_arch_riscv_配置项参考_1.md#CONFIG_CUSTOM_STACK_GUARD)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_FLOAT_HARD"></a>

## 34.11 `CONFIG_FLOAT_HARD`

**提示（Prompt）**：硬浮点调用约定（Hard-Float Calling Convention）

**说明（Help）**

启用硬浮点调用约定（Hard-Float Calling Convention），增加 8 个浮点参数寄存器（Floating-Point Argument Register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU && !CONFIG_RISCV_ISA_RV32E && CONFIG_RISCV_ISA_EXT_F && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/riscv/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_RISCV_ISA_RV32E`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_RV32E)、[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_INCLUDE_RESET_VECTOR"></a>

## 34.12 `CONFIG_INCLUDE_RESET_VECTOR`

**提示（Prompt）**：直接跳转到 __initialize（Jump Directly）

**说明（Help）**

选择 `y` 使用 Zephyr 提供的默认实现，直接跳转到 `__initialize`。否则，片上系统（SoC）需要提供自定义的 `__reset` 例程（Routine）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV
CONFIG_SOC_RP2350A_HAZARD3_0
CONFIG_SOC_RP2350B_HAZARD3_0
CONFIG_SOC_FAMILY_CDNS_SWERV
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENTITAN
CONFIG_SOC_LITEX_VEXIIRISCV
CONFIG_SOC_LITEX_VEXRISCV
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_HYDROGEN
CONFIG_SOC_SERIES_NITROGEN
CONFIG_SOC_SERIES_NIOSV
CONFIG_SOC_PIC64GX1000
CONFIG_SOC_THEJAS32
CONFIG_SOC_GANGA
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_SOC_SERIES_RHX
CONFIG_SOC_SERIES_RMX
CONFIG_SOC_JH7100
CONFIG_SOC_JH7110
CONFIG_SOC_MIV
CONFIG_SOC_EFINIX_SAPPHIRE
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`arch/riscv/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV)、[`CONFIG_SOC_RP2350A_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_HAZARD3_0)、[`CONFIG_SOC_RP2350B_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_HAZARD3_0)、[`CONFIG_SOC_FAMILY_CDNS_SWERV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CDNS_SWERV)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_LITEX_VEXIIRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXIIRISCV)、[`CONFIG_SOC_LITEX_VEXRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXRISCV)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_HYDROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_HYDROGEN)、[`CONFIG_SOC_SERIES_NITROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NITROGEN)、[`CONFIG_SOC_SERIES_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)、[`CONFIG_SOC_THEJAS32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_THEJAS32)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_SOC_SERIES_RHX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RHX)、[`CONFIG_SOC_SERIES_RMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RMX)、[`CONFIG_SOC_JH7100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_JH7100)、[`CONFIG_SOC_JH7110`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_JH7110)、[`CONFIG_SOC_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIV)、[`CONFIG_SOC_EFINIX_SAPPHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFINIX_SAPPHIRE)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`、`CONFIG_SOC_FAMILY_CDNS_SWERV`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_LITEX_VEXIIRISCV`、`CONFIG_SOC_LITEX_VEXRISCV`、`CONFIG_SOC_SERIES_HYDROGEN`、`CONFIG_SOC_SERIES_NITROGEN`、`CONFIG_SOC_PIC64GX1000`、`CONFIG_SOC_GANGA`、`CONFIG_SOC_FAMILY_MAX32_RV32`、`CONFIG_SOC_SERIES_RHX`、`CONFIG_SOC_SERIES_RMX`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`、`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_NULL_POINTER_EXCEPTION_DETECTION_PMP"></a>

## 34.13 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_PMP`

**提示（Prompt）**：使用 PMP 检测空指针异常（Null Pointer Exception Detection）

**说明（Help）**

利用物理内存保护（PMP）功能实现空指针解引用检测（Null Pointer Dereference Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:622`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L622)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_NULL_POINTER_EXCEPTION_REGION_SIZE"></a>

## 34.14 `CONFIG_NULL_POINTER_EXCEPTION_REGION_SIZE`

**提示（Prompt）**：用于实现空指针检测的不可访问区域（Inaccessible Region）

**说明（Help）**

使用一个物理内存保护槽位（PMP Slot），使从地址 `0x0` 开始的区域不可访问，以检测空指针解引用（Null Pointer Dereferencing），并触发 CPU 访问故障（Access Fault）。最小为 4 字节，大小向上取整到 `PMP_GRANULARITY` 的整数倍。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NULL_POINTER_EXCEPTION_DETECTION_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
0x10
```

**定义位置（Location）**：[`arch/riscv/Kconfig:631`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L631)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → 使用 PMP 检测空指针异常（Null Pointer Exception Detection）

**配置项引用（Symbol References）**：[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_PMP`](P034_arch_riscv_配置项参考_1.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_DATA_EXECUTION_PREVENTION"></a>

## 34.15 `CONFIG_PMP_DATA_EXECUTION_PREVENTION`

**提示（Prompt）**：阻止数据执行（Prevent Data Execution）

**说明（Help）**

配置物理内存保护（PMP），防止执行数据节（Data Section）中的内容。这要求使用锁定条目（Locked Entry），目前无法与重定位（Relocation）配合使用，因为复制代码后需要将目标内存标记为可执行。对于用户线程，需要启用一个专用 PMP 寄存器，这要求使用动态内核模式（Dynamic Kernel Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PMP_SLOTS >= 8 && !CONFIG_PMP_NO_NAPOT && !CONFIG_PMP_NO_LOCK_GLOBAL && !CONFIG_CODE_DATA_RELOCATION && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PMP_KERNEL_MODE_DYNAMIC if CONFIG_USERSPACE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:594`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L594)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_PMP_SLOTS`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_SLOTS)、[`CONFIG_PMP_NO_NAPOT`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_NAPOT)、[`CONFIG_PMP_NO_LOCK_GLOBAL`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_LOCK_GLOBAL)、[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_PMP_KERNEL_MODE_DYNAMIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_KERNEL_MODE_DYNAMIC)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_PMP_GRANULARITY"></a>

## 34.16 `CONFIG_PMP_GRANULARITY`

**提示（Prompt）**：PMP 地址匹配粒度（Address Matching Granularity）

**说明（Help）**

粒度必须是大于或等于 4 的 2 的幂，即 4、8、16 等；但如果不支持范围上界（TOR）模式和自然对齐 4 字节（NA4）模式，则最小粒度为 8。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
8 if CONFIG_PMP_NO_TOR && CONFIG_PMP_NO_NA4
4
```

**定义位置（Location）**：[`arch/riscv/Kconfig:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L545)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_PMP_NO_TOR`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_TOR)、[`CONFIG_PMP_NO_NA4`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_NA4)。

<a id="CONFIG_PMP_KERNEL_MODE_DYNAMIC"></a>

## 34.17 `CONFIG_PMP_KERNEL_MODE_DYNAMIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在内核（中断服务例程 ISR、系统调用 Syscall）与线程之间切换时，动态重新配置并激活机器模式（Machine Mode）的物理内存保护（PMP）条目。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_PMP_KERNEL_MODE_DYNAMIC_CATCHALL if !CONFIG_PMP_DATA_EXECUTION_PREVENTION
```

**被选择（Selected by）**

```text
CONFIG_RISCV_PMP
CONFIG_PMP_NO_LOCK_GLOBAL
CONFIG_PMP_STACK_GUARD
CONFIG_PMP_DATA_EXECUTION_PREVENTION
```

**定义位置（Location）**：[`arch/riscv/Kconfig:606`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L606)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_PMP_KERNEL_MODE_DYNAMIC_CATCHALL`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_KERNEL_MODE_DYNAMIC_CATCHALL)、[`CONFIG_PMP_DATA_EXECUTION_PREVENTION`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_DATA_EXECUTION_PREVENTION)、[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_PMP_NO_LOCK_GLOBAL`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_LOCK_GLOBAL)、[`CONFIG_PMP_STACK_GUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMP_STACK_GUARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PMP_STACK_GUARD`。

<a id="CONFIG_PMP_KERNEL_MODE_DYNAMIC_CATCHALL"></a>

## 34.18 `CONFIG_PMP_KERNEL_MODE_DYNAMIC_CATCHALL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

要求为内核线程（Kernel Thread）配置一个覆盖其余全部地址的条目（Catch-All Entry）。`PMP_DATA_EXECUTION_PREVENTION` 始终会创建这样的条目，因此不需要此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_PMP_KERNEL_MODE_DYNAMIC
```

**定义位置（Location）**：[`arch/riscv/Kconfig:613`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L613)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_PMP_KERNEL_MODE_DYNAMIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_KERNEL_MODE_DYNAMIC)。

<a id="CONFIG_PMP_NAPOT_USE_MULTI_SLOTS"></a>

## 34.19 `CONFIG_PMP_NAPOT_USE_MULTI_SLOTS`

**提示（Prompt）**：使用多个 NAPOT 条目覆盖未对齐内存区域（Non-Aligned Memory Regions）

**说明（Help）**

允许将非自然对齐的内存区域拆分为多个自然对齐 2 的幂（Naturally Aligned Power Of Two，NAPOT）条目。这样，即使内存区域的起始地址和大小不同时满足 2 的幂对齐要求，也可以使用物理内存保护（PMP）进行保护。启用后，像 `[0x1800, 0x3800)` 这样的区域会拆分成多个自然对齐的块，例如 `0x800+0x1000+0x800` 字节，每个块由单独的 NAPOT 条目保护。

当不支持范围上界（TOR）模式且内存区域不是自然对齐时，此选项很有用。它消耗更多 PMP 槽位（Slot），但能灵活地覆盖需要保护的内存。

注意：禁用 `PMP_POWER_OF_TWO_ALIGNMENT` 影响的不只是代码与只读数据（Code + rodata）区域。此时，内核模式栈保护区 `Z_RISCV_STACK_GUARD_SIZE` 向上取整到 `Z_RISCV_STACK_PMP_ALIGN` 的整数倍，而不是 2 的幂；`ARCH_KERNEL_STACK_OBJ_ALIGN` 也会降为 PMP 粒度。因此，每个内核模式栈保护区，以及启用 `CONFIG_USERSPACE` 时的每个用户模式栈区域，也都会拆分成多个 NAPOT 条目。在典型的 `PMP_SLOTS=8` 或 `16` 配置中，槽位预算实际上主要消耗在这里。

将 `PMP_GRANULARITY` 设为 64 可减少代码与只读数据区域拆分出的条目数量，但也会使栈保护区大小成为 64 的整数倍，通常不是 2 的幂，因此保护区本身仍需拆分。选择粒度时需要权衡这两方面的影响。

此选项依赖 `!USERSPACE`：启用 `CONFIG_USERSPACE` 时，`arch_mem_domain_max_partitions_get()` 假设每个分区需要 1 或 2 个 PMP 槽位；当某个分区所需的槽位多于剩余槽位时，`resync_pmp_domain()` 只能记录错误，因为 `__ASSERT` 会被编译移除。这样，内存域（Memory Domain）会在部分分区未映射的情况下运行，造成无明显报错的保护丢失。在槽位估算和失败处理路径能够处理需要任意数量槽位的分区之前，此选项仅限于机器模式（M-mode）的代码与只读数据区域场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PMP_NO_TOR && !CONFIG_PMP_POWER_OF_TWO_ALIGNMENT && !CONFIG_PMP_NO_NAPOT && !CONFIG_USERSPACE && CONFIG_RISCV_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/riscv/Kconfig:502`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L502)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_PMP_NO_TOR`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_TOR)、[`CONFIG_PMP_POWER_OF_TWO_ALIGNMENT`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_PMP_NO_NAPOT`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_NAPOT)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_NO_LOCK_GLOBAL"></a>

## 34.20 `CONFIG_PMP_NO_LOCK_GLOBAL`

**提示（Prompt）**：不锁定全局 PMP 条目（Global PMP Entries）

**说明（Help）**

将物理内存保护（PMP）条目配置为未锁定状态，即 `L=0`，以实现 PMP 相关功能。这样应用可以动态重新配置 PMP 条目，无需硬复位（Hard Reset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_PMP_KERNEL_MODE_DYNAMIC
```

**定义位置（Location）**：[`arch/riscv/Kconfig:554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L554)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_PMP_KERNEL_MODE_DYNAMIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_KERNEL_MODE_DYNAMIC)。

<a id="CONFIG_PMP_NO_NA4"></a>

## 34.21 `CONFIG_PMP_NO_NA4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果不支持自然对齐 4 字节（Naturally Aligned 4-byte，NA4）模式，则设置此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:480`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L480)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_NO_NAPOT"></a>

## 34.22 `CONFIG_PMP_NO_NAPOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果不支持自然对齐 2 的幂（Naturally Aligned Power Of Two，NAPOT）模式，则设置此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_NO_TOR"></a>

## 34.23 `CONFIG_PMP_NO_TOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果不支持范围上界（Top Of Range，TOR）模式，则设置此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:475`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L475)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_POWER_OF_TWO_ALIGNMENT"></a>

## 34.24 `CONFIG_PMP_POWER_OF_TWO_ALIGNMENT`

**提示（Prompt）**：强制 PMP 内存区域按 2 的幂对齐（Power-of-Two Alignment）

**说明（Help）**

此选项减少物理内存保护槽位（PMP Slot）用量，但会增加内存消耗。当启用用户空间（Userspace）模式，且内存域（Memory Domain）较多和／或可用 PMP 槽位较少时很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_TEST_USERSPACE
y if CONFIG_PMP_SLOTS = 8
y if CONFIG_PMP_NO_TOR
```

**主动选择（Selects）**

```text
CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT
CONFIG_GEN_PRIV_STACKS
```

**定义位置（Location）**：[`arch/riscv/Kconfig:490`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L490)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_TEST_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_USERSPACE)、[`CONFIG_PMP_SLOTS`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_SLOTS)、[`CONFIG_PMP_NO_TOR`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_NO_TOR)、[`CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT)、[`CONFIG_GEN_PRIV_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_PRIV_STACKS)。

<a id="CONFIG_PMP_SLOTS"></a>

## 34.25 `CONFIG_PMP_SLOTS`

**提示（Prompt）**：PMP 槽位数量（Number of PMP Slots）

**说明（Help）**

硬件实现的物理内存保护（PMP）条目数量，典型值为 8 或 16。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`arch/riscv/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_PMP_STACK_GUARD_MIN_SIZE"></a>

## 34.26 `CONFIG_PMP_STACK_GUARD_MIN_SIZE`

**提示（Prompt）**：栈保护区大小（Stack Guard Area Size）

**说明（Help）**

硬件栈保护（Hardware Stack Protection）使用物理内存保护（PMP），在栈底设置一个不可访问的保护区，以捕获栈溢出（Stack Overflow）。此值指定保护区大小。该区域应足够大，以捕获栈指针（Stack Pointer）减小时的任何突然跨越，并留出一定余量，以容纳最终发生溢出异常（Overflow Exception）时的栈用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PMP_STACK_GUARD && CONFIG_RISCV
```

**默认值（Defaults）**

```text
1024 if CONFIG_64BIT
512
```

**定义位置（Location）**：[`arch/riscv/Kconfig:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L579)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_PMP_STACK_GUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMP_STACK_GUARD)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PMP_STACK_GUARD`。

<a id="CONFIG_PMP_UNLOCK_ROM_FOR_DEBUG"></a>

## 34.27 `CONFIG_PMP_UNLOCK_ROM_FOR_DEBUG`

**提示（Prompt）**：解锁 ROM 区域以供调试器访问（Debugger Access）

**说明（Help）**

启用后，ROM 区域的物理内存保护（PMP）条目不设置锁定位，即 `L=0`，使运行于机器模式（Machine Mode）的调试器可以设置断点（Breakpoint）并读取指令。空指针保护区（NULL Pointer Guard）和栈保护区（Stack Guard）仍保持锁定，以在开发期间捕获严重错误。仅在调试构建（Debug Build）中启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/riscv/Kconfig:562`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L562)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options） → RISC-V 物理内存保护支持（PMP Support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL"></a>

## 34.28 `CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL`

**提示（Prompt）**：不在陷阱处理上下文之外使用 mret（Trap Handler Context）

**说明（Help）**

仅在陷阱处理程序（Trap Handler）中使用 `mret` 指令。这适用于要求每个 `mret` 都与一个 `ecall` 配对的 RISC-V 实现。RISC-V 规范并不要求这样做；大多数情况下应选择 `n`，以尽量降低上下文切换（Context Switch）开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_HAS_CLIC
```

**定义位置（Location）**：[`arch/riscv/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_HAS_CLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CLIC)。

<a id="CONFIG_RISCV_CMODEL"></a>

## 34.29 `CONFIG_RISCV_CMODEL`

**提示（Prompt）**：RISC-V 代码模型（Code Model）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
CONFIG_RISCV_CMODEL_LARGE if (CONFIG_SRAM_DEPRECATED_KCONFIG_SET && CONFIG_SRAM_BASE_ADDRESS > 0xffffffff) || (!CONFIG_SRAM_DEPRECATED_KCONFIG_SET && 0 > 0xffffffff) || CONFIG_KERNEL_VM_BASE > 0xffffffff
CONFIG_RISCV_CMODEL_MEDANY if CONFIG_64BIT
CONFIG_RISCV_CMODEL_MEDLOW
```

**可选项（Choices）**

```text
CONFIG_RISCV_CMODEL_MEDLOW
CONFIG_RISCV_CMODEL_MEDANY
CONFIG_RISCV_CMODEL_LARGE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_CMODEL_LARGE`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL_LARGE)、[`CONFIG_SRAM_DEPRECATED_KCONFIG_SET`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_DEPRECATED_KCONFIG_SET)、[`CONFIG_SRAM_BASE_ADDRESS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_BASE_ADDRESS)、[`CONFIG_KERNEL_VM_BASE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_BASE)、[`CONFIG_RISCV_CMODEL_MEDANY`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL_MEDANY)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_RISCV_CMODEL_MEDLOW`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL_MEDLOW)。

<a id="CONFIG_RISCV_CMODEL_LARGE"></a>

## 34.30 `CONFIG_RISCV_CMODEL_LARGE`

**提示（Prompt）**：大代码模型（Large Code Model）

**说明（Help）**

在大代码模型（Large Code Model，`large`）中，程序及其静态定义的符号在大小和放置位置方面不受限制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_CMODEL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 代码模型（Code Model）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CMODEL`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL)。

<a id="CONFIG_RISCV_CMODEL_MEDANY"></a>

## 34.31 `CONFIG_RISCV_CMODEL_MEDANY`

**提示（Prompt）**：中等任意地址代码模型（Medium-Any Code Model）

**说明（Help）**

在中等任意地址代码模型（Medium-Any Code Model，`medany`）中，程序及其静态定义的符号必须位于任意一个连续的 2 GiB 地址范围内。此模型生成的代码与位置无关（Position-Independent）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_CMODEL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 代码模型（Code Model）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CMODEL`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL)。

<a id="CONFIG_RISCV_CMODEL_MEDLOW"></a>

## 34.32 `CONFIG_RISCV_CMODEL_MEDLOW`

**提示（Prompt）**：中等低地址代码模型（Medium-Low Code Model）

**说明（Help）**

在中等低地址代码模型（Medium-Low Code Model，`medlow`）中，程序及其静态定义的符号必须位于同一个 2 GiB 地址范围内，且位于绝对地址 `-2 GiB` 到 `+2 GiB` 之间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_CMODEL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 代码模型（Code Model）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CMODEL`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CMODEL)。

<a id="CONFIG_RISCV_CURRENT_VIA_GP"></a>

## 34.33 `CONFIG_RISCV_CURRENT_VIA_GP`

**提示（Prompt）**：将当前线程保存到全局指针寄存器（Global Pointer，GP）

**说明（Help）**

将当前线程的指针保存在全局指针寄存器（Global Pointer，GP）中。启用后，对 `_current` 和 `k_sched_current_thread_query()` 的调用可简化为一次寄存器读取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MP_MAX_NUM_CPUS > 1 && <choice CONFIG_RISCV_GP_PURPOSE>
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL
```

**定义位置（Location）**：[`arch/riscv/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → 全局指针寄存器的用途（Global Pointer，GP）

**配置项引用（Symbol References）**：[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_RISCV_GP_PURPOSE`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_GP_PURPOSE)、[`CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_EXECIT"></a>

## 34.34 `CONFIG_RISCV_CUSTOM_CSR_ANDES_EXECIT`

**提示（Prompt）**：Andes V5 EXEC.IT 扩展（Extension）

**说明（Help）**

`EXEC.IT` 扩展，即指令表执行（Execution on Instruction Table），生成一张查找表（Look-Up Table），并将适合的 32 位指令替换为 16 位的 `exec.it <INDEX>`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_EXECIT && CONFIG_RISCV_ISA_EXT_C && !CONFIG_RISCV_GENERIC_TOOLCHAIN && !CONFIG_LINKER_USE_NO_RELAX && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_EXECIT`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_EXECIT)、[`CONFIG_RISCV_ISA_EXT_C`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_C)、[`CONFIG_RISCV_GENERIC_TOOLCHAIN`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_GENERIC_TOOLCHAIN)、[`CONFIG_LINKER_USE_NO_RELAX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_USE_NO_RELAX)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_HSP"></a>

## 34.35 `CONFIG_RISCV_CUSTOM_CSR_ANDES_HSP`

**提示（Prompt）**：Andes V5 StackSafe 扩展（Extension）

**说明（Help）**

启用 Andes V5 StackSafe 硬件栈保护（Hardware Stack Protection），以支持自定义栈保护机制（Custom Stack Guard）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_HSP && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_STACK_PROTECTION
CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_HSP`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_HSP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_HWDSP"></a>

## 34.36 `CONFIG_RISCV_CUSTOM_CSR_ANDES_HWDSP`

**提示（Prompt）**：AndeStar V5 DSP 指令集架构（ISA）

**说明（Help）**

启用 AndeStar V5 硬件数字信号处理（DSP）功能，以支持使用 DSP 指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_HWDSP && !CONFIG_RISCV_GENERIC_TOOLCHAIN && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_HWDSP`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_HWDSP)、[`CONFIG_RISCV_GENERIC_TOOLCHAIN`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_GENERIC_TOOLCHAIN)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_NEXECIT"></a>

## 34.37 `CONFIG_RISCV_CUSTOM_CSR_ANDES_NEXECIT`

**提示（Prompt）**：Andes V5 新 EXEC.IT 操作码编码（New EXEC.IT Opcode Encoding）

**说明（Help）**

新的 `EXEC.IT` 指令是 `EXEC.IT` 的别名（Alias），使用不同的操作码编码（Opcode Encoding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_CUSTOM_CSR_ANDES_EXECIT && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → Andes V5 EXEC.IT 扩展（Extension）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CUSTOM_CSR_ANDES_EXECIT`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CUSTOM_CSR_ANDES_EXECIT)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_NMI"></a>

## 34.38 `CONFIG_RISCV_CUSTOM_CSR_ANDES_NMI`

**提示（Prompt）**：Andes V5 不可屏蔽中断扩展（NMI Extension）

**说明（Help）**

在 N25/N25F 等 AndeStar V5 内核上，不可屏蔽中断（NMI）向量基地址寄存器 `mnvec` 只读，读回的是 `reset_vector` 输入信号，因此 NMI 从 `__reset` 进入；启动路径会破坏触发 NMI 时原本要让软件检查的状态。

启用此选项可区分复位与 NMI：复位时 `mcause` 和 `mepc` 都为 0；NMI 时 `mcause` 为 1，`mepc` 保存被中断的程序计数器（PC）。检测到 NMI 后跳转到 `_andes_nmi_entry`。

启用 NMI 的片上系统（SoC）应提供自己的 `_andes_nmi_entry`，覆盖弱符号（Weak Symbol）版本；并在启用任何 NMI 源之前设置处理程序所需的状态，例如在 `mscratch` 中设置 NMI 栈。默认的弱符号实现只会使内核停驻（Park）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_NMI && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_NMI`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_NMI)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_PFT"></a>

## 34.39 `CONFIG_RISCV_CUSTOM_CSR_ANDES_PFT`

**提示（Prompt）**：Andes V5 PowerBrake 扩展（Extension）

**说明（Help）**

PowerBrake 扩展通过降低指令执行速率（Instruction Executing Rate）来限制性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_PFT && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_PFT`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_PFT)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA"></a>

## 34.40 `CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA`

**提示（Prompt）**：Andes V5 物理内存属性（Physical Memory Attribute，PMA）

**说明（Help）**

启用 Andes V5 物理内存属性（PMA）功能，使软件能够通过 PMA 控制与状态寄存器（CSR）配置物理内存属性。Andes V5 PMA 的地址匹配方式类似于 RISC-V 物理内存保护（PMP）的自然对齐 2 的幂（NAPOT）模式，即按 2 的幂对齐。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_ANDES_PMA && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_ANDES_PMA`](P034_arch_riscv_配置项参考_1.md#CONFIG_CPU_HAS_ANDES_PMA)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA_NAPOT_GRANULARITY"></a>

## 34.41 `CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA_NAPOT_GRANULARITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

物理内存属性（PMA）区域的最小大小及对齐要求。使用此符号保证 PMA 区域满足最小大小和对齐要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA && DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/riscv/custom/andes/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/andes/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → Andes V5 物理内存属性（Physical Memory Attribute，PMA）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CUSTOM_CSR_ANDES_PMA)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_CUSTOM_CSR_THEAD_CMO"></a>

## 34.42 `CONFIG_RISCV_CUSTOM_CSR_THEAD_CMO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用玄铁（XuanTie）CPU 系列的缓存操作（Cache Operation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_XTHEAD_CMO && DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_CACHE_MANAGEMENT
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_XTHEAD_CMO`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_XTHEAD_CMO)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)。

<a id="CONFIG_RISCV_CUSTOM_CSR_THEAD_CMO_E907"></a>

## 34.43 `CONFIG_RISCV_CUSTOM_CSR_THEAD_CMO_E907`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用玄铁（XuanTie）E907 内核的附加缓存操作（Cache Operation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_XTHEAD_CMO && DT_HAS_XUANTIE_E907_ENABLED && DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_CACHE_MANAGEMENT
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_XTHEAD_CMO`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_XTHEAD_CMO)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)。

<a id="CONFIG_RISCV_CUSTOM_CSR_VEXRISCV_CACHE"></a>

## 34.44 `CONFIG_RISCV_CUSTOM_CSR_VEXRISCV_CACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 VexRiscv CPU 系列的缓存支持（Cache Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_CACHE && DT_HAS_SPINALHDL_VEXRISCV_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/riscv/custom/vexriscv/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/vexriscv/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_CACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_CACHE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_FPU_INSN_VALIDATE"></a>

## 34.45 `CONFIG_RISCV_FPU_INSN_VALIDATE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

仅供调试的派生符号（Derived Debug-Only Symbol）。启用后，浮点单元（FPU）陷阱处理程序会显式解码触发陷阱的指令，确保它是有效的浮点指令。这可以捕获一些边界情况，例如向量指令（Vector Instruction）等非 FPU 指令意外触发浮点（FP）陷阱。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU_SHARING && CONFIG_ASSERT && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/riscv/Kconfig:863`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L863)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_GENERIC_TOOLCHAIN"></a>

## 34.46 `CONFIG_RISCV_GENERIC_TOOLCHAIN`

**提示（Prompt）**：使用通用 riscv32 工具链编译（Generic Toolchain）

**说明（Help）**

使用通用 `riscv32` 工具链（Toolchain）编译，使具有自定义 RISC-V 指令集架构（ISA）扩展的片上系统（SoC）也能使用该通用工具链编译。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/riscv/Kconfig:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L377)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_GP"></a>

## 34.47 `CONFIG_RISCV_GP`

**提示（Prompt）**：RISC-V 全局指针相对寻址（Global Pointer Relative Addressing）

**说明（Help）**

对可执行文件中任意位置声明的小型全局变量使用全局指针相对寻址（Global Pointer Relative Addressing）。这可以提高性能并减小代码体积。

注意：要支持此特性，RISC-V 片上系统（SoC）需要在程序开始时，或在任何使用 GP 相对寻址的指令之前，初始化全局指针（Global Pointer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING && <choice CONFIG_RISCV_GP_PURPOSE>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → 全局指针寄存器的用途（Global Pointer，GP）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING)、[`CONFIG_RISCV_GP_PURPOSE`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_GP_PURPOSE)。

<a id="CONFIG_RISCV_GP_PURPOSE"></a>

## 34.48 `CONFIG_RISCV_GP_PURPOSE`

**提示（Prompt）**：全局指针寄存器的用途（Global Pointer，GP）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
CONFIG_RISCV_GP if CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING
```

**可选项（Choices）**

```text
CONFIG_RISCV_GP
CONFIG_RISCV_CURRENT_VIA_GP
```

**定义位置（Location）**：[`arch/riscv/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_GP`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_GP)、[`CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING)、[`CONFIG_RISCV_CURRENT_VIA_GP`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CURRENT_VIA_GP)。

<a id="CONFIG_RISCV_HART_MASK"></a>

## 34.49 `CONFIG_RISCV_HART_MASK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

配置硬件线程标识（HART ID）的掩码（Mask）。对于 HART ID 从非零值开始的 RISC-V 系统，例如 `128, 129, ..(0x80, 8x81, ..)`，可以将此项设为 `63 (0x7f)`，以提取从 0 开始的那些位。

译注：上述数值写法保留自上游原文；其中 `8x81` 疑为 `0x81`，十进制 `63` 与十六进制 `0x7f` 也不等值。实际配置应根据硬件的 HART ID 编码选择掩码，不能直接将这组不一致的示例当作数值依据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`arch/riscv/Kconfig:429`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L429)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_HAS_AIA"></a>

## 34.50 `CONFIG_RISCV_HAS_AIA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统（SoC）是否支持高级中断架构（Advanced Interrupt Architecture，AIA）。该架构包括高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）和传入消息信号中断控制器（Incoming Message-Signaled Interrupt Controller，IMSIC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PRIVILEGED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_VIRT_RISCV32
```

**定义位置（Location）**：[`arch/riscv/Kconfig:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L347)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PRIVILEGED`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PRIVILEGED)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_QEMU_VIRT_RISCV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_RISCV32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_VIRT_RISCV32`。

<a id="CONFIG_RISCV_HAS_CLIC"></a>

## 34.51 `CONFIG_RISCV_HAS_CLIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统（SoC）是否支持内核本地中断控制器（Core-Local Interrupt Controller，CLIC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PRIVILEGED && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL if CONFIG_MULTITHREADING
CONFIG_CLIC_SUPPORT_INTERRUPT_LEVEL if !CONFIG_NRFX_CLIC
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`arch/riscv/Kconfig:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L339)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PRIVILEGED`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PRIVILEGED)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_CLIC_SUPPORT_INTERRUPT_LEVEL`](P034_arch_riscv_配置项参考_1.md#CONFIG_CLIC_SUPPORT_INTERRUPT_LEVEL)、[`CONFIG_NRFX_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NRFX_CLIC)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD"></a>

## 34.52 `CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

硬件提供自定义栈保护机制（Custom Stack Guard）时选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_CUSTOM_CSR_ANDES_HSP
```

**定义位置（Location）**：[`arch/riscv/Kconfig:680`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L680)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_CUSTOM_CSR_ANDES_HSP`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_CUSTOM_CSR_ANDES_HSP)。

<a id="CONFIG_RISCV_HAS_PLIC"></a>

## 34.53 `CONFIG_RISCV_HAS_PLIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统（SoC）是否支持平台级中断控制器（Platform Level Interrupt Controller，PLIC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_PRIVILEGED && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_QEMU_VIRT_RISCV32E
CONFIG_SOC_QEMU_VIRT_RISCV64
CONFIG_SOC_OPENTITAN
CONFIG_SOC_LITEX_VEXIIRISCV
CONFIG_SOC_SERIES_HYDROGEN
CONFIG_SOC_SERIES_NITROGEN
CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_GANGA
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STARFIVE_JH71XX
CONFIG_SOC_SERIES_MIV
CONFIG_SOC_SERIES_POLARFIRE
CONFIG_SOC_EFINIX_SAPPHIRE
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
```

**定义位置（Location）**：[`arch/riscv/Kconfig:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L333)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_PRIVILEGED`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PRIVILEGED)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_QEMU_VIRT_RISCV32E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_RISCV32E)、[`CONFIG_SOC_QEMU_VIRT_RISCV64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_RISCV64)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_LITEX_VEXIIRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXIIRISCV)、[`CONFIG_SOC_SERIES_HYDROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_HYDROGEN)、[`CONFIG_SOC_SERIES_NITROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NITROGEN)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STARFIVE_JH71XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STARFIVE_JH71XX)、[`CONFIG_SOC_SERIES_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MIV)、[`CONFIG_SOC_SERIES_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_EFINIX_SAPPHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFINIX_SAPPHIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_VIRT_RISCV32E`、`CONFIG_SOC_QEMU_VIRT_RISCV64`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_LITEX_VEXIIRISCV`、`CONFIG_SOC_SERIES_HYDROGEN`、`CONFIG_SOC_SERIES_NITROGEN`、`CONFIG_SOC_GANGA`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_RISCV_IMPRECISE_FPU_STATE_TRACKING"></a>

## 34.54 `CONFIG_RISCV_IMPRECISE_FPU_STATE_TRACKING`

**提示（Prompt）**：非精确的 FPU 状态跟踪实现（Imprecise FPU State Tracking）

**说明（Help）**

根据《RISC-V 指令集手册》（RISC-V Instruction Set Manual）第 II 卷、20240411 版本的 3.1.6.6 节，某些实现可以选择非精确地跟踪浮点寄存器状态是否为脏（Dirty）：即使状态尚未修改，也报告为脏。此选项反映这种实现方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:660`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L660)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_BASE_FENCE"></a>

## 34.55 `CONFIG_RISCV_ISA_BASE_FENCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

标准基础整数指令集（Base Integer Instruction Set）包含 `fence` 指令，但某些实现可能缺少该指令。屏障检查（Barrier Check）依赖此符号，以确保硬件线程（Hart）确实支持 `fence`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if !n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L33)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_A"></a>

## 34.56 `CONFIG_RISCV_ISA_EXT_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`A`：原子指令标准扩展（Standard Extension for Atomic Instructions）。标准原子指令扩展的指令子集名为 `A`，包含以原子方式对内存执行读—改—写（Read-Modify-Write）的指令，用于在同一内存空间运行的多个 RISC-V 线程之间实现同步（Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
CONFIG_RISCV_ISA_EXT_G
```

**弱选择（Implies）**

```text
CONFIG_RISCV_ISA_EXT_ZAAMO
CONFIG_RISCV_ISA_EXT_ZALRSC
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L51)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)、[`CONFIG_RISCV_ISA_EXT_ZAAMO`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZAAMO)、[`CONFIG_RISCV_ISA_EXT_ZALRSC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZALRSC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`。

<a id="CONFIG_RISCV_ISA_EXT_C"></a>

## 34.57 `CONFIG_RISCV_ISA_EXT_C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`C`：压缩指令标准扩展（Standard Extension for Compressed Instructions）。RISC-V 标准压缩指令集扩展名为 `C`，通过为常用操作添加短的 16 位指令编码，减少静态与动态代码大小（Static and Dynamic Code Size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ISA_EXT_ZCA
CONFIG_RISCV_ISA_EXT_ZCD if CONFIG_RISCV_ISA_EXT_D
CONFIG_RISCV_ISA_EXT_ZCF if CONFIG_RISCV_ISA_EXT_F && (CONFIG_RISCV_ISA_RV32I || CONFIG_RISCV_ISA_RV32E)
```

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L113)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV_ISA_EXT_ZCD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCD)、[`CONFIG_RISCV_ISA_EXT_D`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_RISCV_ISA_EXT_ZCF`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCF)、[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV_ISA_RV32I`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_ISA_RV32I)、[`CONFIG_RISCV_ISA_RV32E`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_RV32E)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`。

<a id="CONFIG_RISCV_ISA_EXT_D"></a>

## 34.58 `CONFIG_RISCV_ISA_EXT_D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`D`：双精度浮点标准扩展（Standard Extension for Double-Precision Floating-Point）。标准双精度浮点指令集扩展名为 `D`，增加符合 IEEE 754-2008 算术标准的双精度浮点计算指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_F && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION
```

**被选择（Selected by）**

```text
CONFIG_RISCV_ISA_EXT_G
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L76)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)。

<a id="CONFIG_RISCV_ISA_EXT_F"></a>

## 34.59 `CONFIG_RISCV_ISA_EXT_F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`F`：单精度浮点标准扩展（Standard Extension for Single-Precision Floating-Point）。标准单精度浮点指令集扩展名为 `F`，增加符合 IEEE 754-2008 算术标准的单精度浮点计算指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_IT8XXX2
CONFIG_RISCV_ISA_EXT_G
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L64)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)。

<a id="CONFIG_RISCV_ISA_EXT_G"></a>

## 34.60 `CONFIG_RISCV_ISA_EXT_G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

IMAFDZicsr_Zifencei 扩展（Extensions）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ISA_EXT_M
CONFIG_RISCV_ISA_EXT_A
CONFIG_RISCV_ISA_EXT_F
CONFIG_RISCV_ISA_EXT_D
CONFIG_RISCV_ISA_EXT_ZICSR
CONFIG_RISCV_ISA_EXT_ZIFENCEI
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L89)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_M`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_M)、[`CONFIG_RISCV_ISA_EXT_A`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_A)、[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV_ISA_EXT_D`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)、[`CONFIG_RISCV_ISA_EXT_ZIFENCEI`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZIFENCEI)。

<a id="CONFIG_RISCV_ISA_EXT_M"></a>

## 34.61 `CONFIG_RISCV_ISA_EXT_M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`M`：整数乘除法标准扩展（Standard Extension for Integer Multiplication and Division）。标准整数乘除法指令扩展名为 `M`，包含对两个整数寄存器中的值进行乘法或除法运算的指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT8XXX2
CONFIG_SOC_GANGA
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_RISCV_ISA_EXT_G
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L41)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT8XXX2`、`CONFIG_SOC_GANGA`、`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_RISCV_ISA_EXT_Q"></a>

## 34.62 `CONFIG_RISCV_ISA_EXT_Q`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Q`：四精度浮点标准扩展（Standard Extension for Quad-Precision Floating-Point）。此标准扩展提供符合 IEEE 754-2008 算术标准的 128 位二进制浮点指令。128 位、即四精度二进制浮点指令子集名为 `Q`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_RV64I && CONFIG_RISCV_ISA_EXT_F && CONFIG_RISCV_ISA_EXT_D && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L100)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_RV64I`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_ISA_RV64I)、[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV_ISA_EXT_D`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_SMAIA"></a>

## 34.63 `CONFIG_RISCV_ISA_EXT_SMAIA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Smaia`：高级中断架构扩展（AIA Extension）。Smaia 包含 AIA 针对硬件线程（Hart）在所有特权级别（Privilege Level）上规定的全部新增控制与状态寄存器（CSR），以及全部中断响应行为变更。根据 AIA 规范 1.6 节，实际启用的 CSR 集合取决于多种因素；此扩展用于推断某个 CSR 是否启用，例如硬件线程实现 RV32 和 SMAIA 时，会启用 `mieh`、`miph`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L306)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_SMCSRIND"></a>

## 34.64 `CONFIG_RISCV_ISA_EXT_SMCSRIND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Smcsrind`：CSR 间接访问标准扩展（Standard Extension for Indirect CSR Access）。Smcsrind 通过 `MISELECT` 和 `MIREG` 寄存器提供对控制与状态寄存器（CSR）的间接访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZICSR && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L146)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_SSAIA"></a>

## 34.65 `CONFIG_RISCV_ISA_EXT_SSAIA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Ssaia`：高级中断架构扩展（AIA Extension）。Ssaia 包含 AIA 针对硬件线程（Hart）在所有特权级别（Privilege Level）上规定的新增控制与状态寄存器（CSR）及中断响应行为变更，但不包括机器级 CSR，也不包括监管级（Supervisor Level）无法直接观察的行为。根据 AIA 规范 1.6 节，实际启用的 CSR 集合取决于多种因素；此扩展用于推断某个 CSR 是否启用，例如硬件线程实现 RV32 和 SSAIA 时，会启用 `sieh`、`siph`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L319)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_BA"></a>

## 34.66 `CONFIG_RISCV_ISA_EXT_XTHEAD_BA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥地址计算扩展（T-head Address Calculation Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_BB"></a>

## 34.67 `CONFIG_RISCV_ISA_EXT_XTHEAD_BB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥基本位操作扩展（T-head Basic Bit-Manipulation Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_BS"></a>

## 34.68 `CONFIG_RISCV_ISA_EXT_XTHEAD_BS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥单比特指令扩展（T-head Single-Bit Instructions Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_CMO"></a>

## 34.69 `CONFIG_RISCV_ISA_EXT_XTHEAD_CMO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥缓存管理操作扩展（T-head Cache Management Operations Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_CONDMOV"></a>

## 34.70 `CONFIG_RISCV_ISA_EXT_XTHEAD_CONDMOV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥条件移动扩展（T-head Conditional Move Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_FMEMIDX"></a>

## 34.71 `CONFIG_RISCV_ISA_EXT_XTHEAD_FMEMIDX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥浮点寄存器索引访存操作扩展（T-head Indexed Memory Operations for Floating-Point Registers Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_F && DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_FMV"></a>

## 34.72 `CONFIG_RISCV_ISA_EXT_XTHEAD_FMV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥双精度浮点高位数据传输扩展（T-head Double Floating-Point High-Bit Data Transmission Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_D && DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_D`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_INT"></a>

## 34.73 `CONFIG_RISCV_ISA_EXT_XTHEAD_INT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥中断加速扩展（T-head Acceleration Interruption Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_MAC"></a>

## 34.74 `CONFIG_RISCV_ISA_EXT_XTHEAD_MAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥乘加扩展（T-head Multiply-Accumulate Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_MEMIDX"></a>

## 34.75 `CONFIG_RISCV_ISA_EXT_XTHEAD_MEMIDX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥索引访存操作扩展（T-head Indexed Memory Operation Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_MEMPAIR"></a>

## 34.76 `CONFIG_RISCV_ISA_EXT_XTHEAD_MEMPAIR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥双通用寄存器访存操作扩展（T-head Two-GPR Memory Operation Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_SYNC"></a>

## 34.77 `CONFIG_RISCV_ISA_EXT_XTHEAD_SYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥多核同步扩展（T-head Multi-Core Synchronization Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_XTHEAD_VECTOR"></a>

## 34.78 `CONFIG_RISCV_ISA_EXT_XTHEAD_VECTOR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平头哥向量扩展（T-head Vector Extension）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XUANTIE_E907_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/custom/thead/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/custom/thead/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZAAMO"></a>

## 34.79 `CONFIG_RISCV_ISA_EXT_ZAAMO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zaamo`：A 扩展中的原子内存操作子集（Atomic Memory Operation Subset）。Zaamo 启用对 `AMO*.W/D` 类指令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被弱选择（Implied by）**

```text
CONFIG_RISCV_ISA_EXT_A
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L166)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_A`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_A)。

<a id="CONFIG_RISCV_ISA_EXT_ZALRSC"></a>

## 34.80 `CONFIG_RISCV_ISA_EXT_ZALRSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zalrsc`：A 扩展中的保留加载／条件存储子集（Load-Reserved / Store-Conditional Subset）。Zalrsc 启用对 `LR.W/D` 和 `SC.W/D` 类指令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被弱选择（Implied by）**

```text
CONFIG_RISCV_ISA_EXT_A
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L174)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_A`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_A)。

<a id="CONFIG_RISCV_ISA_EXT_ZBA"></a>

## 34.81 `CONFIG_RISCV_ISA_EXT_ZBA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zba`：位操作扩展（BitManip Extension）。Zba 指令可加速生成基本类型数组的索引地址，基本类型包括半字（Halfword）、字（Word）和双字（Doubleword）；索引可以是无符号的字宽索引或 XLEN 宽度索引。其操作是将移位后的索引加到基地址上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L247)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZBB"></a>

## 34.82 `CONFIG_RISCV_ISA_EXT_ZBB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zbb`：基本位操作扩展（Basic Bit-Manipulation Extension）。Zbb 指令可执行基本位操作，例如带取反的逻辑运算、前导／末尾零位计数（Leading / Trailing Zero Count）以及置位数计数（Population Count）等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L258)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZBC"></a>

## 34.83 `CONFIG_RISCV_ISA_EXT_ZBC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zbc`：无进位乘法位操作扩展（Carry-less Multiplication BitManip Extension）。Zbc 指令可执行无进位乘法，即有限域 GF(2) 上多项式环中的乘法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L268)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZBKB"></a>

## 34.84 `CONFIG_RISCV_ISA_EXT_ZBKB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zbkb`：密码学位操作扩展（Bit-Manipulation for Cryptography）。Zbkb 指令可加速密码学工作负载（Cryptography Workload），包括循环移位（Rotation）、反转（Reversion）、打包（Packing）及一些高级位操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_BIT_REV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_ISA_EXT_ZK
CONFIG_RISCV_ISA_EXT_ZKS
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L277)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_ARCH_HAS_BIT_REV`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_BIT_REV)、[`CONFIG_RISCV_ISA_EXT_ZK`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZK)、[`CONFIG_RISCV_ISA_EXT_ZKS`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZKS)。

<a id="CONFIG_RISCV_ISA_EXT_ZBS"></a>

## 34.85 `CONFIG_RISCV_ISA_EXT_ZBS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zbs`：单比特指令位操作扩展（Single-Bit Instructions BitManip Extension）。Zbs 提供单比特指令，用于设置、清除、翻转或提取寄存器中的单个位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L287)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZCA"></a>

## 34.86 `CONFIG_RISCV_ISA_EXT_ZCA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zca`：压缩指令扩展（Compressed Instructions Extension）。Zca 是 C 扩展的子集，不包含浮点加载和存储指令（Floating-Point Load and Store Instructions）。

译注：原文标题在 `Zca` 后写成了“Zba Extension”；正文明确描述 Zca，此处保留两者的对应关系并说明该命名不一致。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_RISCV_ISA_EXT_C
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L182)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_C`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_C)。

<a id="CONFIG_RISCV_ISA_EXT_ZCB"></a>

## 34.87 `CONFIG_RISCV_ISA_EXT_ZCB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zcb`：简单压缩指令扩展（Simple Compressed Instructions Extension）。Zcb 是一组可节省代码体积的简单指令，易于在所有 CPU 上实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZCA && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L191)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZCD"></a>

## 34.88 `CONFIG_RISCV_ISA_EXT_ZCD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zcd`：双精度浮点压缩指令扩展（Double-Precision FP Compressed Instructions Extension）。Zcd 包含压缩的双精度浮点加载和存储指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_D && CONFIG_RISCV_ISA_EXT_ZCA && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_RISCV_ISA_EXT_C
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L201)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_D`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_D)、[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_C`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_C)。

<a id="CONFIG_RISCV_ISA_EXT_ZCF"></a>

## 34.89 `CONFIG_RISCV_ISA_EXT_ZCF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zcf`：单精度浮点压缩指令扩展（Single-Precision FP Compressed Instructions Extension）。Zcf 包含压缩的单精度浮点加载和存储指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_RISCV_ISA_RV32I || CONFIG_RISCV_ISA_RV32E) && CONFIG_RISCV_ISA_EXT_F && CONFIG_RISCV_ISA_EXT_ZCA && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_RISCV_ISA_EXT_C
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L212)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_RV32I`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_ISA_RV32I)、[`CONFIG_RISCV_ISA_RV32E`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_RV32E)、[`CONFIG_RISCV_ISA_EXT_F`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_F)、[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_C`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_C)。

<a id="CONFIG_RISCV_ISA_EXT_ZCMP"></a>

## 34.90 `CONFIG_RISCV_ISA_EXT_ZCMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zcmp`：复杂压缩指令扩展（Complex Compressed Instructions Extension）。Zcmp 包含面向嵌入式 CPU 的复杂操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZCA && !CONFIG_RISCV_ISA_EXT_ZCD && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L224)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV_ISA_EXT_ZCD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCD)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZCMT"></a>

## 34.91 `CONFIG_RISCV_ISA_EXT_ZCMT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zcmt`：压缩表跳转指令扩展（Compressed Table Jump Instructions Extension）。Zcmt 包含面向嵌入式 CPU 的压缩表跳转指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZICSR && CONFIG_RISCV_ISA_EXT_ZCA && !CONFIG_RISCV_ISA_EXT_ZCD && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L235)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)、[`CONFIG_RISCV_ISA_EXT_ZCA`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCA)、[`CONFIG_RISCV_ISA_EXT_ZCD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZCD)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZICNTR"></a>

## 34.92 `CONFIG_RISCV_ISA_EXT_ZICNTR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zicntr`：基础计数器与定时器标准扩展（Standard Extension for Base Counters and Timers）。Zicntr 包含三个具有专用功能的计数器：`CYCLE`、`TIME` 和 `INSTRET`，分别用于周期计数（Cycle Count）、实时时钟（Real-Time Clock）和已退休指令数（Instructions Retired）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZICSR && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L126)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_EXT_ZICSR"></a>

## 34.93 `CONFIG_RISCV_ISA_EXT_ZICSR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zicsr`：控制与状态寄存器指令标准扩展（Standard Extension for Control and Status Register Instructions）。Zicsr 引入对完整 CSR 指令集的支持，这些指令操作控制与状态寄存器（CSR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_RISCV_SMRNMI_ENABLE_NMI_DELIVERY
CONFIG_RISCV_ISA_EXT_G
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L137)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_RISCV_SMRNMI_ENABLE_NMI_DELIVERY`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMRNMI_ENABLE_NMI_DELIVERY)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`、`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_RISCV_ISA_EXT_ZIFENCEI"></a>

## 34.94 `CONFIG_RISCV_ISA_EXT_ZIFENCEI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zifencei`：取指屏障标准扩展（Standard Extension for Instruction-Fetch Fence）。Zifencei 包含 `FENCE.I` 指令，使同一硬件线程（Hart）上的指令存储器写入与指令获取之间能够显式同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_RISCV_ISA_EXT_G
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L156)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_RISCV_ISA_EXT_G`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`、`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_RISCV_ISA_EXT_ZK"></a>

## 34.95 `CONFIG_RISCV_ISA_EXT_ZK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zk`：标量密码学标准扩展（Standard Extension for Scalar Cryptography）。Zk 支持符合 NIST 标准的标量密码学指令，包括以下子扩展：Zbkb（密码学位操作，Bit Manipulation for Cryptography）、Zbkc（无进位乘法，Carry-less Multiplication）、Zbkx（交叉开关置换，Crossbar Permutations）、Zknd / Zkne（NIST AES 解密／加密）、Zknh（SHA-256 和 SHA-512 等 NIST 哈希函数）以及 Zkr（熵源，Entropy Source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ISA_EXT_ZBKB
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L333)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_ZBKB`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZBKB)。

<a id="CONFIG_RISCV_ISA_EXT_ZKR"></a>

## 34.96 `CONFIG_RISCV_ISA_EXT_ZKR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zkr`：熵源标准扩展（Standard Extension for Entropy Source）。Zkr 提供 `seed` 控制与状态寄存器（CSR），这是一个物理熵源，每次访问提供 16 位随机数据。默认仅机器模式（M-mode）可访问该 CSR；只有通过 `mseccfg` CSR 的 `SSEED` 和 `USEED` 位授权后，监管模式（S-mode）或用户模式（U-mode）才能访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZICSR && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
y if CONFIG_RISCV_ISA_EXT_ZK
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L347)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_ZK`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZK)。

<a id="CONFIG_RISCV_ISA_EXT_ZKS"></a>

## 34.97 `CONFIG_RISCV_ISA_EXT_ZKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zks`：商密算法套件标准扩展（Standard Extension for ShangMi Suite）。Zks 支持实现中国国家密码标准的商密算法套件（ShangMi Suite）。它包含与 Zk 共用的 Zbkb、Zbkc、Zbkx 子扩展，以及 Zksed（SM4 分组密码，Block Cipher）和 Zksh（SM3 哈希函数，Hash Function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ISA_EXT_ZBKB
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L360)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_ZBKB`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZBKB)。

<a id="CONFIG_RISCV_ISA_EXT_ZMMUL"></a>

## 34.98 `CONFIG_RISCV_ISA_EXT_ZMMUL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`Zmmul`：整数乘法扩展（Integer Multiplication Extension）。Zmmul 实现 M 扩展中的乘法子集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L297)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_RV128I"></a>

## 34.99 `CONFIG_RISCV_ISA_RV128I`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RV128I 基础整数指令集（Base Integer Instruction Set），128 位

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L27)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_ISA_RV32E"></a>

## 34.100 `CONFIG_RISCV_ISA_RV32E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RV32E 嵌入式基础整数指令集（Embedded Base Integer Instruction Set），32 位

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L14)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<!-- kconfig-navigation -->

[上一章](P033_arch_posix_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P035_arch_riscv_配置项参考_2.md)
