---
id: learning.zephyr-docs.kconfig-reference.page-35
title: "`arch/riscv`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第35章\_`arch/riscv`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `arch/riscv` 的 37 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RISCV_ISA_RV32I"></a>

## 35.1 `CONFIG_RISCV_ISA_RV32I`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RV32I 基础整数指令集（Base Integer Instruction Set），32 位

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
CONFIG_SOC_FAMILY_MAX32_RV32
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L8)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_RISCV_ISA_RV64I"></a>

## 35.2 `CONFIG_RISCV_ISA_RV64I`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RV64I 基础整数指令集（Base Integer Instruction Set），64 位

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
CONFIG_64BIT
```

**被选择（Selected by）**

```text
CONFIG_SOC_GANGA
```

**定义位置（Location）**：[`arch/riscv/Kconfig.isa:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig.isa#L20)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_GANGA`。

<a id="CONFIG_RISCV_MCAUSE_EXCEPTION_MASK"></a>

## 35.3 `CONFIG_RISCV_MCAUSE_EXCEPTION_MASK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定 `mcause` 寄存器中用作异常代码（Exception Code）的位。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
0x7FFFFFFFFFFFFFFF if CONFIG_64BIT
0x7FFFFFFF
```

**定义位置（Location）**：[`arch/riscv/Kconfig:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L370)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_RISCV_M_MODE"></a>

## 35.4 `CONFIG_RISCV_M_MODE`

**提示（Prompt）**：机器模式（Machine Mode，M-mode）

**说明（Help）**

在机器模式（Machine Mode，M-mode）运行内核。这是 RISC-V 的默认特权级别（Privilege Level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`arch/riscv/Kconfig:811`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L811)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 特权级别（Privilege Level）

<a id="CONFIG_RISCV_M_MODE_STACK_SIZE"></a>

## 35.5 `CONFIG_RISCV_M_MODE_STACK_SIZE`

**提示（Prompt）**：M-mode SBI 处理程序栈大小，单位为字节（Handler Stack Size）

**说明（Help）**

源码树内机器模式（M-mode）监管级二进制接口（SBI）运行时处理程序使用的专用栈大小，单位为字节。如果扩展处理程序的功能需要更多栈空间，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_S_MODE_INTERNAL_SBI && CONFIG_RISCV
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/riscv/Kconfig:854`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L854)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE_INTERNAL_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_INTERNAL_SBI)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP"></a>

## 35.6 `CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

发生浮点非法指令异常（Floating-Point Illegal Instruction Exception）时，此实现不会在 `mtval` 控制与状态寄存器，即机器陷阱值寄存器（Machine Trap Value Register）中提供有用信息。

RISC-V 规范允许实现根据具体情况决定 `mtval` 何时包含有意义的值。规范规定，发生陷阱（Trap）时，`mtval` 要么置零，要么写入与异常相关的信息。不过，这种与异常相关的信息不一定是导致故障的指令值，实现可以灵活决定提供什么内容。

启用此选项后，不能依赖 `mtval` 保存导致故障的浮点（FP）指令，必须使用其他方法处理浮点异常。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_QEMU_TARGET
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
```

**定义位置（Location）**：[`arch/riscv/Kconfig:772`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L772)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_QEMU_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_TARGET)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)。

<a id="CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP_UNALIGNED"></a>

## 35.7 `CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP_UNALIGNED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 `mepc` 未按 4 字节对齐时，逐半字（Halfword）获取导致故障的浮点（FP）指令。这样可避免不使用 MTVAL 的浮点陷阱处理程序发生未对齐加载异常（Unaligned-Load Exception）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
```

**定义位置（Location）**：[`arch/riscv/Kconfig:794`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L794)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_NO_MTVAL_ON_FP_TRAP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)。

<a id="CONFIG_RISCV_PMP"></a>

## 35.8 `CONFIG_RISCV_PMP`

**提示（Prompt）**：RISC-V 物理内存保护支持（PMP Support）

**说明（Help）**

微控制器（MCU）实现了物理内存保护（Physical Memory Protection，PMP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_RISCV_S_MODE && CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_CPU_HAS_MPU
CONFIG_ARCH_HAS_USERSPACE
CONFIG_ARCH_HAS_STACK_PROTECTION
CONFIG_MPU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE
CONFIG_ARCH_MEM_DOMAIN_DATA if CONFIG_USERSPACE
CONFIG_THREAD_LOCAL_STORAGE if CONFIG_USERSPACE
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS
CONFIG_MEM_DOMAIN_ISOLATED_STACKS if CONFIG_USERSPACE
CONFIG_PMP_KERNEL_MODE_DYNAMIC if CONFIG_MEM_ATTR
CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C6
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32H2
CONFIG_SOC_SERIES_ESP32P4
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_FE310_G002
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
```

**定义位置（Location）**：[`arch/riscv/Kconfig:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L447)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_MEM_DOMAIN_DATA`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_DATA)、[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_ISOLATED_STACKS)、[`CONFIG_MEM_DOMAIN_ISOLATED_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_MEM_DOMAIN_ISOLATED_STACKS)、[`CONFIG_PMP_KERNEL_MODE_DYNAMIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_PMP_KERNEL_MODE_DYNAMIC)、[`CONFIG_MEM_ATTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEM_ATTR)、[`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_FE310_G002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FE310_G002)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_EXECUTABLE_PAGE_BIT`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FE310_G002`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_RISCV_PRIVILEGED"></a>

## 35.9 `CONFIG_RISCV_PRIVILEGED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由实现 RISC-V 特权指令集架构（Privileged ISA）的片上系统（SoC）选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_RAMFUNC_SUPPORT if CONFIG_XIP
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_NEORV32
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENTITAN
CONFIG_SOC_LITEX_VEXIIRISCV
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_HYDROGEN
CONFIG_SOC_SERIES_NITROGEN
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_NIOSV
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_SERIES_SY1XX
CONFIG_SOC_GANGA
CONFIG_SOC_SERIES_RHX
CONFIG_SOC_SERIES_RMX
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
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`arch/riscv/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_RAMFUNC_SUPPORT)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_LITEX_VEXIIRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXIIRISCV)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_HYDROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_HYDROGEN)、[`CONFIG_SOC_SERIES_NITROGEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NITROGEN)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_SERIES_SY1XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SY1XX)、[`CONFIG_SOC_GANGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GANGA)、[`CONFIG_SOC_SERIES_RHX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RHX)、[`CONFIG_SOC_SERIES_RMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RMX)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STARFIVE_JH71XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STARFIVE_JH71XX)、[`CONFIG_SOC_SERIES_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MIV)、[`CONFIG_SOC_SERIES_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_EFINIX_SAPPHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFINIX_SAPPHIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_RAMFUNC_SUPPORT`、`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_LITEX_VEXIIRISCV`、`CONFIG_SOC_SERIES_HYDROGEN`、`CONFIG_SOC_SERIES_NITROGEN`、`CONFIG_SOC_SERIES_SY1XX`、`CONFIG_SOC_GANGA`、`CONFIG_SOC_SERIES_RHX`、`CONFIG_SOC_SERIES_RMX`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`、`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_RISCV_PRIVILEGE_MODE"></a>

## 35.10 `CONFIG_RISCV_PRIVILEGE_MODE`

**提示（Prompt）**：RISC-V 特权级别（Privilege Level）

**说明（Help）**

选择内核运行的特权级别（Privilege Level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
CONFIG_RISCV_M_MODE
```

**可选项（Choices）**

```text
CONFIG_RISCV_M_MODE
CONFIG_RISCV_S_MODE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:805`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L805)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_M_MODE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_M_MODE)、[`CONFIG_RISCV_S_MODE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE)。

<a id="CONFIG_RISCV_RESERVED_IRQ_ISR_TABLES_OFFSET"></a>

## 35.11 `CONFIG_RISCV_RESERVED_IRQ_ISR_TABLES_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在某些 RISC-V 平台上，最前面的中断向量主要用于硬件线程间中断通知（Inter-Hart Interrupt Signaling），因此为此用途保留，不可另作使用。设置此选项后，所有中断请求（IRQ）向量安装到软件中断服务例程表（Software ISR Table）和 IRQ 向量表时，都会加上此偏移值。`CONFIG_NUM_IRQS` 必须适当设置，以计入该偏移。此选项是隐藏选项，应由各架构设置，之后保持不动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_ISR_TABLES && CONFIG_RISCV
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/riscv/Kconfig:405`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L405)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_GEN_ISR_TABLES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_ISR_TABLES)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_SMP_IPI_CLINT"></a>

## 35.12 `CONFIG_RISCV_SMP_IPI_CLINT`

**提示（Prompt）**：基于 CLINT 的处理器间中断（IPI）

**说明（Help）**

使用基于内核本地中断器（CLINT）的处理器间中断（IPI）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_CLINT0_ENABLED && <choice CONFIG_RISCV_SMP_IPI_IMPL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 对称多处理 IPI 实现（SMP IPI Implementation）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_SMP_IPI_IMPL`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_IMPL)。

<a id="CONFIG_RISCV_SMP_IPI_CUSTOM"></a>

## 35.13 `CONFIG_RISCV_SMP_IPI_CUSTOM`

**提示（Prompt）**：自定义处理器间中断实现（Custom IPI Implementation）

**说明（Help）**

允许自定义处理器间中断（IPI）实现。选择后，必须提供以下函数：

- `arch_sched_directed_ipi()`。
- 启用 `CONFIG_FPU_SHARING` 时的 `arch_flush_fpu_ipi()`。
- 启用 `CONFIG_FPU_SHARING` 时的 `arch_spin_relax()`。
- `arch_smp_init()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_SMP_IPI_IMPL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 对称多处理 IPI 实现（SMP IPI Implementation）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_SMP_IPI_IMPL`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_IMPL)。

<a id="CONFIG_RISCV_SMP_IPI_IMPL"></a>

## 35.14 `CONFIG_RISCV_SMP_IPI_IMPL`

**提示（Prompt）**：RISC-V 对称多处理 IPI 实现（SMP IPI Implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_RISCV
```

**默认值（Defaults）**

```text
CONFIG_RISCV_SMP_IPI_CLINT if DT_HAS_SIFIVE_CLINT0_ENABLED
CONFIG_RISCV_SMP_IPI_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_RISCV_SMP_IPI_CLINT
CONFIG_RISCV_SMP_IPI_SBI
CONFIG_RISCV_SMP_IPI_CUSTOM
```

**定义位置（Location）**：[`arch/riscv/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_SMP_IPI_CLINT`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_CLINT)、[`CONFIG_RISCV_SMP_IPI_CUSTOM`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_CUSTOM)、[`CONFIG_RISCV_SMP_IPI_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_SBI)。

<a id="CONFIG_RISCV_SMP_IPI_SBI"></a>

## 35.15 `CONFIG_RISCV_SMP_IPI_SBI`

**提示（Prompt）**：基于 SBI 的处理器间中断（IPI）

**说明（Help）**

使用监管级二进制接口（SBI）的 IPI 扩展 `sbi_send_ipi`，在目标硬件线程（Hart）上触发监管级软件中断（Supervisor Software Interrupt）。当 Zephyr 在监管模式（S-mode）运行，作为 OpenSBI 等外部 SBI 的载荷（Payload），且该外部 SBI 管理内核本地中断器（CLINT）时，应使用此实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_S_MODE_EXTERNAL_SBI && <choice CONFIG_RISCV_SMP_IPI_IMPL>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 对称多处理 IPI 实现（SMP IPI Implementation）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE_EXTERNAL_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_EXTERNAL_SBI)、[`CONFIG_RISCV_SMP_IPI_IMPL`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SMP_IPI_IMPL)。

<a id="CONFIG_RISCV_SMRNMI_ENABLE_NMI_DELIVERY"></a>

## 35.16 `CONFIG_RISCV_SMRNMI_ENABLE_NMI_DELIVERY`

**提示（Prompt）**：SMRNMI 硬件上的 NMI 递送（MNSTATUS.NMIE=1）

**说明（Help）**

启动期间将 `MNSTATUS.NMIE` 位置 1，在实现 SMRNMI 扩展的 RISC-V 硬件上启用不可屏蔽中断（NMI）递送。此选项仅启用 NMI 递送，不提供可恢复不可屏蔽中断（RNMI）处理程序，也不提供 `mnret` 指令支持。必须在片上系统（SoC）专用代码中实现适当的 RNMI 处理程序，以处理 NMI 事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_RISCV_ISA_EXT_ZICSR
```

**定义位置（Location）**：[`arch/riscv/Kconfig:669`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L669)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_ZICSR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICSR)。

<a id="CONFIG_RISCV_SOC_CONTEXT_SAVE"></a>

## 35.17 `CONFIG_RISCV_SOC_CONTEXT_SAVE`

**提示（Prompt）**：IRQ 处理程序中的 SoC 上下文保存（SoC-Based Context Saving）

**说明（Help）**

启用片上系统（SoC）专用的底层上下文管理（Context Management），适用于具有额外状态、需要在进入中断／异常时保存并在退出时恢复这些状态的 SoC。如不确定，保留默认值。

启用此选项要求 SoC 提供 `soc_context.h` 头文件，其中定义以下宏：

- `SOC_ESF_MEMBERS`：需要为其分配空间的结构体成员声明。为保证可移植性，最后一个声明不应以分号结束。通用 RISC-V 架构代码会在 `struct soc_esf` 类型中为这些成员分配空间；该类型还通过 `typedef` 命名为 `soc_esf_t`，包含 `arch.h` 后即可使用。
- `SOC_ESF_INIT`：`struct soc_esf` 状态的结构体内容初始化器（Initializer）。最后一个被初始化成员不应以逗号结束。

通用架构的 IRQ 包装程序（IRQ Wrapper）还会在进入和退出中断服务例程（ISR）时，分别调用 `__soc_save_context` 与 `__soc_restore_context`。这些例程通常应使用汇编实现。如果它们是 C 函数，其签名如下：

```c
void __soc_save_context(soc_esf_t *state);
void __soc_restore_context(soc_esf_t *state);
```

调用遵守标准调用约定（Calling Convention），即状态指针地址位于 `a0`，返回地址位于 `ra`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**主动选择（Selects）**

```text
CONFIG_RISCV_SOC_OFFSETS
```

**被选择（Selected by）**

```text
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_EGIS_ET171
```

**定义位置（Location）**：[`arch/riscv/Kconfig:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L286)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_SOC_OFFSETS`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_OFFSETS)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING"></a>

## 35.18 `CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

允许片上系统（SoC）覆盖中断请求（IRQ）的处理方式。启用后，必须实现 `__soc_handle_all_irqs` 函数；该函数应处理并清除所有待处理中断（Pending Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_HAZARD3_INTC
CONFIG_CLIC
```

**定义位置（Location）**：[`arch/riscv/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_HAZARD3_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_HAZARD3_INTC)、[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)。

<a id="CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_LOCK_OPS"></a>

## 35.19 `CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_LOCK_OPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，允许片上系统（SoC）使用平台专用版本覆盖 `arch_irq_lock()`、`arch_irq_unlock()` 和 `arch_irq_unlocked()`，对应名称为 `z_soc_irq_lock()`、`z_soc_irq_unlock()` 和 `z_soc_irq_unlocked()`。

当 RISC-V SoC 锁定和解锁中断请求（IRQ）时，除了读写 `mstatus` 寄存器之外还需要执行不同或额外的操作，应启用此隐藏选项，并定制对应的 `z_soc_*` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_SOC_HAS_CUSTOM_SYS_IO"></a>

## 35.20 `CONFIG_RISCV_SOC_HAS_CUSTOM_SYS_IO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，允许片上系统（SoC）使用平台专用版本覆盖 `sys_read*()` 和 `sys_write*()`，对应名称为 `z_soc_sys_read*()` 和 `z_soc_sys_write*()`。当 RISC-V SoC 除了读写寄存器之外还需要执行不同或额外的操作，应启用此隐藏选项，并定制对应的 `z_soc_*` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L205)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING"></a>

## 35.21 `CONFIG_RISCV_SOC_HAS_GP_RELATIVE_ADDRESSING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当片上系统（SoC）已在程序开始时，或在任何使用全局指针相对寻址（GP Relative Addressing）的指令之前，实现全局指针（Global Pointer，GP）初始化时，选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_NEORV32
CONFIG_SOC_RISCV_VIRTUAL_RENODE
CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV
CONFIG_SOC_SERIES_ESP32C2
CONFIG_SOC_SERIES_ESP32C3
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32C6
CONFIG_SOC_SERIES_ESP32C61
CONFIG_SOC_SERIES_ESP32H2
CONFIG_SOC_SERIES_ESP32P4
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENTITAN
CONFIG_SOC_LITEX_VEXIIRISCV
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_IT8XXX2
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_NIOSV
CONFIG_SOC_SERIES_PIC64GX
CONFIG_SOC_PIC64GX1000
CONFIG_SOC_SERIES_RHX
CONFIG_SOC_SERIES_RMX
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_STARFIVE_JH71XX
CONFIG_SOC_SERIES_MIV
CONFIG_SOC_SERIES_POLARFIRE
CONFIG_SOC_POLARFIRE
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
```

**定义位置（Location）**：[`arch/riscv/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32)、[`CONFIG_SOC_RISCV_VIRTUAL_RENODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RISCV_VIRTUAL_RENODE)、[`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_LITEX_VEXIIRISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LITEX_VEXIIRISCV)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_NIOSV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NIOSV)、[`CONFIG_SOC_SERIES_PIC64GX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PIC64GX)、[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)、[`CONFIG_SOC_SERIES_RHX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RHX)、[`CONFIG_SOC_SERIES_RMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RMX)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_STARFIVE_JH71XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STARFIVE_JH71XX)、[`CONFIG_SOC_SERIES_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MIV)、[`CONFIG_SOC_SERIES_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_QEMU_VIRT_RISCV`、`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_LITEX_VEXIIRISCV`、`CONFIG_SOC_PIC64GX1000`、`CONFIG_SOC_SERIES_RHX`、`CONFIG_SOC_SERIES_RMX`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_RISCV_SOC_HAS_ISR_STACKING"></a>

## 35.22 `CONFIG_RISCV_SOC_HAS_ISR_STACKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用中断服务例程（ISR）期间片上系统（SoC）专用的底层硬件入栈／出栈操作（Hardware Stacking / Unstacking）。支持此特性的 SoC 需要选择这个隐藏选项。

某些 SoC 在处理中断时，会由硬件按照自定义异常栈帧（Exception Stack Frame，ESF）格式，将一部分上下文自动保存到栈中；执行 `mret` 时，再由硬件自动恢复这部分上下文。

启用此选项要求 SoC 提供 `soc_isr_stacking.h` 头文件，并定义以下内容：

- `SOC_ISR_SW_STACKING`：受 `_ASMLANGUAGE` 条件保护的宏。IRQ 包装程序的汇编代码在进入 ISR 时调用它，将硬件尚未压栈的其余上下文保存到 ESF。
- `SOC_ISR_SW_UNSTACKING`：受 `_ASMLANGUAGE` 条件保护的宏。IRQ 包装程序的汇编代码在退出 ISR 时调用它，从 ESF 恢复那些不会由硬件在 `mret` 时恢复的上下文。
- `SOC_ISR_STACKING_ESF_DECLARE`：受 `!_ASMLANGUAGE` 条件保护的 ESF 结构体声明。ESF 定义应按照硬件实际入栈顺序包含硬件保存的寄存器，并包含软件宏保存的寄存器。结构体必须命名为 `struct arch_esf`。
- `SOC_ISR_STACKING_ESR_INIT`：受 `!_ASMLANGUAGE` 条件保护的宏。初始化栈时，应为某些硬件入栈寄存器设置适当初值，以避免入口上下文切换恢复初始栈时发生错误行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_USERSPACE && CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_CORE_NORDIC_VPR
```

**定义位置（Location）**：[`arch/riscv/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)。

<a id="CONFIG_RISCV_SOC_HAS_SYSCALL_INTMASK"></a>

## 35.23 `CONFIG_RISCV_SOC_HAS_SYSCALL_INTMASK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，适用于以下片上系统（SoC）：在用户模式系统调用（User-Mode Syscall）的 `ECALL` 异常尚未处理结束时，若发生中断或其他异步报告事件，例如非精确访问故障（Imprecise Access Fault），则无法安全递送该事件。精确的同步陷阱（Precise Synchronous Trap）仍可正常嵌套，例如用于从系统调用主体切换出去的 `ECALL`。

系统调用路径在运行系统调用主体前会设置 `mstatus.MIE`，因此这类 SoC 必须通过另一种方式屏蔽中断。启用此隐藏选项，并提供 `soc_syscall.h` 头文件，在其中定义受 `_ASMLANGUAGE` 条件保护的 `SOC_SYSCALL_INTMASK` 宏。IRQ 包装程序在系统调用入口调用该宏，此时 SoC 上下文已经保存，调用者保存的临时寄存器（Caller-Saved Temporaries）可供使用，因此宏可以改写它们。通常，该宏会提高硬件中断级别阈值（Interrupt Level Threshold）。

这是 SoC 钩子（Hook），而非通用内核本地中断控制器（CLIC）中断级别支持的一部分，因为需要此功能的 SoC 通过 SoC 代码驱动中断控制器，并不选择 `RISCV_HAS_CLIC`，所以通用代码无法获知它们的阈值。

屏蔽状态属于各自的异常帧（Exception Frame）：SoC 上下文保存／恢复钩子 `RISCV_SOC_CONTEXT_SAVE` 在陷阱入口保存状态，并在异常退出路径恢复状态。由于每次上下文切换都会经过该路径，即 `RISCV_ALWAYS_SWITCH_THROUGH_ECALL`，在系统调用主体中阻塞的线程会把 CPU 交给另一个线程，而后者会恢复自己保存的状态；新线程则从 `SOC_ESF_INIT` 开始。因此，屏蔽状态一定会在系统调用返回或线程切出时结束，不会延续到之后。

代价是系统调用主体不可被抢占（Non-Preemptible）：提高屏蔽阈值期间不会递送任何事件，因此包括系统时钟节拍（System Tick）在内的中断会一直保持待处理，直到系统调用返回或阻塞。这段时间内，`arch_irq_unlocked()` 仅在形式上为真；如果内核未使用无节拍（Tickless）模式，系统调用主体用基于节拍的运行时间（Uptime）限制忙等待（Busy Wait）时，将永远无法超时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_RISCV_SOC_CONTEXT_SAVE && CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L215)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_RISCV_SOC_CONTEXT_SAVE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_CONTEXT_SAVE)、[`CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ALWAYS_SWITCH_THROUGH_ECALL)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_SOC_INTERRUPT_INIT"></a>

## 35.24 `CONFIG_RISCV_SOC_INTERRUPT_INIT`

**提示（Prompt）**：基于 SoC 的中断初始化（SoC-Based Interrupt Initialization）

**说明（Help）**

启用基于片上系统（SoC）的中断初始化；启用后，在 `_IntLibInit` 中调用 `soc_interrupt_init`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_SOC_S400
CONFIG_SOC_S420
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_THEJAS32
```

**定义位置（Location）**：[`arch/riscv/Kconfig:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L364)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_SOC_S400`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S400)、[`CONFIG_SOC_S420`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S420)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_THEJAS32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_THEJAS32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_S400`、`CONFIG_SOC_S420`。

<a id="CONFIG_RISCV_SOC_OFFSETS"></a>

## 35.25 `CONFIG_RISCV_SOC_OFFSETS`

**提示（Prompt）**：基于 SoC 的偏移量（SoC-Based Offsets）

**说明（Help）**

启用此选项要求片上系统（SoC）提供 `soc_offsets.h` 头文件，其中定义以下宏：

- `GEN_SOC_OFFSET_SYMS()`：展开为对 `GEN_OFFSET_SYM(soc_esf_t, soc_specific_member)` 的调用，以确保 `offsets.h` 定义了 `SOC_ESF_MEMBERS` 的偏移宏（Offset Macro）。最后一项不应以分号结束。更多信息参阅 `gen_offset.h`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**被选择（Selected by）**

```text
CONFIG_RISCV_SOC_CONTEXT_SAVE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_SOC_CONTEXT_SAVE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_CONTEXT_SAVE)。

<a id="CONFIG_RISCV_SOC_SYSCALL_CLOSE_ECALL"></a>

## 35.26 `CONFIG_RISCV_SOC_SYSCALL_CLOSE_ECALL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，适用于无法在用户模式系统调用（User-Mode Syscall）的 `ECALL` 异常仍在处理期间，递送由系统调用主体自身触发的故障的片上系统（SoC）。特权栈（Privileged Stack）下方的栈保护区（Stack Guard）会捕获调用链过深的系统调用，但在这类 SoC 上，访问故障会在尚未结束的 `ECALL` 中以异步方式报告，导致内核锁死、芯片复位，软件收不到任何事件。屏蔽中断对此无效，因为故障来自系统调用主体，而非中断控制器。

启用此隐藏选项，可在运行系统调用主体之前退出异常。IRQ 包装程序通过仍保持机器模式（Machine Mode）的陷阱返回（Trap Return）回到后续指令，因此主体继续使用相同的特权栈和相同的权限运行，但已经位于异常之外。这样，主体中发生的故障就成为 SoC 能正常递送的普通顶层陷阱（Top-Level Trap）；如果系统调用导致特权栈溢出，系统会报告栈溢出，并仅终止出错线程。

异常退出路径会从已保存的异常帧重新加载异常程序计数器（Exception Program Counter）和状态寄存器，因此在这里临时使用它们不会干扰返回用户模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_STACK_PROTECTION"></a>

## 35.27 `CONFIG_RISCV_STACK_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用以下两种机制之一：自定义栈保护（Custom Stack Guard），或基于物理内存保护（PMP）的栈保护。当当前进程栈超出边界时，触发系统致命错误（Fatal Error）。两种栈保护选项互斥，优先选择自定义栈保护。如果需要，开发者仍可手动选择基于 PMP 的栈保护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_PMP_STACK_GUARD if !CONFIG_CUSTOM_STACK_GUARD && CONFIG_RISCV_PMP
```

**弱选择（Implies）**

```text
CONFIG_CUSTOM_STACK_GUARD if CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD
```

**定义位置（Location）**：[`arch/riscv/Kconfig:704`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L704)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_PMP_STACK_GUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PMP_STACK_GUARD)、[`CONFIG_CUSTOM_STACK_GUARD`](P034_arch_riscv_配置项参考_1.md#CONFIG_CUSTOM_STACK_GUARD)、[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CUSTOM_STACK_GUARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PMP_STACK_GUARD`。

<a id="CONFIG_RISCV_S_MODE"></a>

## 35.28 `CONFIG_RISCV_S_MODE`

**提示（Prompt）**：监管模式（Supervisor Mode，S-mode）

**说明（Help）**

表示内核运行在监管模式（Supervisor Mode，S-mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`arch/riscv/Kconfig:818`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L818)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 特权级别（Privilege Level）

<a id="CONFIG_RISCV_S_MODE_EXTERNAL_SBI"></a>

## 35.29 `CONFIG_RISCV_S_MODE_EXTERNAL_SBI`

**提示（Prompt）**：依赖外部 SBI 直接进入 S-mode，例如 OpenSBI（External SBI）

**说明（Help）**

跳过源码树内的机器模式（M-mode）启动序列，包括 `PMP`、`medeleg`、`mideleg`、`mcounteren`、`mtvec` 的设置，以及通过 `mret` 降至监管模式（S-mode）的步骤。

当 U-Boot 等引导加载程序（Bootloader）已在 OpenSBI 这样的外部机器模式监管级二进制接口（M-mode SBI）实现之下以 S-mode 运行，并将 Zephyr 作为载荷（Payload）启动时，使用此选项。此时，外部 SBI 已完成 M-mode 设置和委托（Delegation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_S_MODE_SBI>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:842`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L842)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 监管级二进制接口实现（SBI Implementation）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_SBI)。

<a id="CONFIG_RISCV_S_MODE_INTERNAL_SBI"></a>

## 35.30 `CONFIG_RISCV_S_MODE_INTERNAL_SBI`

**提示（Prompt）**：使用内置最小 SBI 运行时（Built-In Minimal SBI Runtime）

**说明（Help）**

启用后，由启动代码内部处理从机器模式（Machine Mode，M-mode）到监管模式（Supervisor Mode，S-mode）的转换。最小的监管级二进制接口（SBI）运行时会常驻 M-mode，以处理定时器中断（Timer Interrupt）和 `ecall` 请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RISCV_S_MODE_SBI>
```

**定义位置（Location）**：[`arch/riscv/Kconfig:834`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L834)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 监管级二进制接口实现（SBI Implementation）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_SBI)。

<a id="CONFIG_RISCV_S_MODE_SBI"></a>

## 35.31 `CONFIG_RISCV_S_MODE_SBI`

**提示（Prompt）**：RISC-V 监管级二进制接口实现（SBI Implementation）

**说明（Help）**

选择在监管模式（Supervisor Mode，S-mode）运行时使用的监管级二进制接口（Supervisor Binary Interface，SBI）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_S_MODE && CONFIG_RISCV
```

**默认值（Defaults）**

```text
CONFIG_RISCV_S_MODE_INTERNAL_SBI
```

**可选项（Choices）**

```text
CONFIG_RISCV_S_MODE_INTERNAL_SBI
CONFIG_RISCV_S_MODE_EXTERNAL_SBI
```

**定义位置（Location）**：[`arch/riscv/Kconfig:826`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L826)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_S_MODE_INTERNAL_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_INTERNAL_SBI)、[`CONFIG_RISCV_S_MODE_EXTERNAL_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_EXTERNAL_SBI)。

<a id="CONFIG_RISCV_TRAP_HANDLER_ALIGNMENT"></a>

## 35.32 `CONFIG_RISCV_TRAP_HANDLER_ALIGNMENT`

**提示（Prompt）**：RISC-V 陷阱处理程序对齐大小，单位为字节（Trap Handler Alignment）

**说明（Help）**

配置 RISC-V 陷阱处理代码（Trap Handling Code）的对齐要求。具体对齐要求来自 RISC-V 平台专用的 `MTVEC` 寄存器格式。根据规范，最小对齐为 4 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
64 if CONFIG_RISCV_HAS_CLIC
4
```

**定义位置（Location）**：[`arch/riscv/Kconfig:748`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L748)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_RISCV_HAS_CLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CLIC)。

<a id="CONFIG_RISCV_USER_COUNTER_ACCESS"></a>

## 35.33 `CONFIG_RISCV_USER_COUNTER_ACCESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

设置 `mcounteren`，并在实现监管模式（S-mode）的硬件线程（Hart）上设置 `scounteren`，使用户线程可以直接读取 Zicntr 计数器，而不会触发非法指令异常（Illegal Instruction Exception）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZICNTR && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_USERSPACE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L438)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZICNTR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZICNTR)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_RISCV_USER_STRING_NLEN_VALIDATE"></a>

## 35.34 `CONFIG_RISCV_USER_STRING_NLEN_VALIDATE`

**提示（Prompt）**：预先验证 arch_user_string_nlen() 中的指针（Pre-Validate Pointer）

**说明（Help）**

`arch_user_string_nlen()` 会解引用用户指针；发生非法地址访问时，通过故障修复（Fault Fixup）机制恢复，该机制将故障发生时的 `mepc` 与加载指令的地址范围进行匹配。

某些 RISC-V 片上系统（SoC）的加载访问故障（Load Access Fault）是非精确的：报告的 `mepc` 可能落在出错加载指令之后的不固定距离处，有时甚至位于另一个函数中。因此，修复机制无法识别该故障，原本应可恢复的错误会升级为致命复位。

启用此选项后，读取前先使用 `arch_buffer_validate()` 验证字符串：先验证整个范围，如果只有部分范围可访问，再按物理内存保护（PMP）粒度逐块验证，从而绝不发出可能导致故障的加载操作。对于具有精确加载故障的 SoC，应保持禁用；这些 SoC 的故障修复机制无需此辅助即可工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_RISCV_PMP && CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:641`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L641)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RISCV_USE_MSAVE_RESTORE"></a>

## 35.35 `CONFIG_RISCV_USE_MSAVE_RESTORE`

**提示（Prompt）**：使用 -msave-restore 编译以减少部分代码体积（Code Footprint）

**说明（Help）**

`-msave-restore` 选项让编译器调用库例程 `__riscv_save_X` 和 `__riscv_restore_X`，保存及恢复被调用者保存寄存器（Callee-Saved Register），而不是在每个函数中内联相应操作。这可以减小某些大型函数的代码体积，但会引入额外的分支开销，可能影响热点路径（Hot Path）的性能。如果片上系统（SoC）支持，应优先使用 `Zcmp` 指令集架构（ISA）扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**定义位置（Location）**：[`arch/riscv/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_RV_BOOT_HART"></a>

## 35.36 `CONFIG_RV_BOOT_HART`

**提示（Prompt）**：起始硬件线程标识（Starting HART ID）

**说明（Help）**

设置对称多处理（SMP）内核的起始硬件线程标识（HART ID）。对于 MPFS 和 FU540 等 RISC-V 系统，应设为 1，以跳过 E51 的 HART 0，因为它不能用于 SMP 配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/riscv/Kconfig:421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L421)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_USE_ISR_WRAPPER"></a>

## 35.37 `CONFIG_USE_ISR_WRAPPER`

**提示（Prompt）**：使用 isr_wrapper 处理中断和／或异常／故障（Interrupt / Exception / Fault）

**说明（Help）**

辅助配置，用于在未启用 `GEN_SW_ISR_TABLE` 时仍使用 `_isr_wrapper` 的异常处理功能。例如，多线程（MULTITHREADING）需要异常处理以及线程入口／切换函数，但可能只使用中断请求向量表（IRQ Vector Table）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if CONFIG_MULTITHREADING
```

**被选择（Selected by）**

```text
CONFIG_GEN_SW_ISR_TABLE
```

**定义位置（Location）**：[`arch/riscv/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/riscv/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → RISC-V 选项（RISC-V Options） → RISC-V 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_GEN_SW_ISR_TABLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_SW_ISR_TABLE)。

<!-- kconfig-navigation -->

[上一章](P034_arch_riscv_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P036_arch_rx_配置项参考.md)
