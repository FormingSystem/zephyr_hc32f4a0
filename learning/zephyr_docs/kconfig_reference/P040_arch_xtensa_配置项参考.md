---
id: learning.zephyr-docs.kconfig-reference.page-40
title: "`arch/xtensa`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第40章\_`arch/xtensa`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/xtensa` 的 33 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SIMULATOR_XTENSA"></a>

## 40.1 `CONFIG_SIMULATOR_XTENSA`

**提示（Prompt）**：模拟器目标（Simulator Target）

**说明（Help）**

构建用于在模拟器（Simulator）上运行的镜像时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**被选择（Selected by）**

```text
CONFIG_INTEL_ADSP_SIM
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_INTEL_ADSP_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INTEL_ADSP_SIM)。

<a id="CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS"></a>

## 40.2 `CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS`

**提示（Prompt）**：遇到不可恢复异常时使用 BREAK 指令（Unrecoverable Exception）

**说明（Help）**

遇到不可恢复异常（Unrecoverable Exception）时使用 `BREAK` 指令。这要求连接调试器（Debugger）来捕获 `BREAK`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_CCOUNT_HZ"></a>

## 40.3 `CONFIG_XTENSA_CCOUNT_HZ`

**提示（Prompt）**：CCOUNT 周期频率（Cycle Rate）

**说明（Help）**

根据 `CCOUNT` 寄存器值测量的 Xtensa 内核频率，单位为 Hz。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**默认值（Defaults）**

```text
1000000
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_EAGER_HIFI_SHARING"></a>

## 40.4 `CONFIG_XTENSA_EAGER_HIFI_SHARING`

**提示（Prompt）**：立即式 HiFi 共享（Eager HiFi Sharing）

**说明（Help）**

启用跨上下文切换（Context Switch）的立即式 HiFi 寄存器共享（Eager Sharing）。这意味着每次上下文切换都无条件保存和恢复 HiFi 寄存器，使多个线程可以并发使用 HiFi 指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XTENSA_HIFI_SHARING_MODEL>
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options） → HiFi 寄存器共享（HiFi Register Sharing） → Xtensa HiFi 共享模型（Sharing Model）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_HIFI_SHARING_MODEL`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_HIFI_SHARING_MODEL)。

<a id="CONFIG_XTENSA_EMULATE_UNSUPPORTED_UNSIGNED_LOAD_STORE"></a>

## 40.5 `CONFIG_XTENSA_EMULATE_UNSUPPORTED_UNSIGNED_LOAD_STORE`

**提示（Prompt）**：模拟不受支持的无符号加载／存储（Unsigned Loads / Stores）

**说明（Help）**

当无符号加载／存储指令（Unsigned Load / Store Instruction）触发不支持加载／存储的异常时，异常处理程序会使用受支持的、按字大小且对齐的加载／存储操作，自行完成该操作。目前不支持超长指令字（VLIW）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPILER_CODEGEN_VLIW_DISABLED && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L314)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_CODEGEN_VLIW_DISABLED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW_DISABLED)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_ENABLE_BACKTRACE"></a>

## 40.6 `CONFIG_XTENSA_ENABLE_BACKTRACE`

**提示（Prompt）**：发生恐慌异常时输出回溯（Backtrace on Panic Exception）

**说明（Help）**

启用此配置，在发生恐慌异常（Panic Exception）时打印回溯（Backtrace）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_ESP32S2
CONFIG_SOC_SERIES_ESP32S3
CONFIG_SOC_MIMXRT595S_F1
CONFIG_SOC_FAMILY_INTEL_ADSP
CONFIG_SOC_XTENSA_DC233C
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_MIMXRT595S_F1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_F1)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SOC_XTENSA_DC233C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XTENSA_DC233C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`、`CONFIG_SOC_XTENSA_DC233C`。

<a id="CONFIG_XTENSA_EXCEPTION_ENTER_GDB"></a>

## 40.7 `CONFIG_XTENSA_EXCEPTION_ENTER_GDB`

**提示（Prompt）**：遇到异常时启动 GDB 调试桩（GDB Stub）

**说明（Help）**

遇到非法地址访问或除零等异常时，进入 GDB 调试桩（GDB Stub）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GDBSTUB && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GDBSTUB)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_FATAL_BREADCRUMB"></a>

## 40.8 `CONFIG_XTENSA_FATAL_BREADCRUMB`

**提示（Prompt）**：记录致命异常线索（Fatal Exception Breadcrumbs）

**说明（Help）**

发生致命异常（Fatal Exception）时，记录出错的程序计数器（PC）、异常原因（Exception Cause）和出错的虚拟地址（Virtual Address），使崩溃信息即使在没有控制台或 `mtrace` 输出时仍可查看。实际存储和报告机制由片上系统（SoC）提供；启用此选项仅表示致命异常会调用该机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_HIFI3"></a>

## 40.9 `CONFIG_XTENSA_HIFI3`

**提示（Prompt）**：HiFi3 AudioEngine 指令（Instructions）

**说明（Help）**

启用 HiFi 3 指令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_CPU_HAS_HIFI3 && CONFIG_XTENSA_CPU_HAS_HIFI && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_XTENSA_HIFI
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_CPU_HAS_HIFI3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI3)、[`CONFIG_XTENSA_CPU_HAS_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_XTENSA_CPU_HAS_HIFI3`、`CONFIG_XTENSA_CPU_HAS_HIFI`、`CONFIG_XTENSA_HIFI`。

<a id="CONFIG_XTENSA_HIFI4"></a>

## 40.10 `CONFIG_XTENSA_HIFI4`

**提示（Prompt）**：HiFi4 AudioEngine 指令（Instructions）

**说明（Help）**

启用 HiFi 4 指令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_CPU_HAS_HIFI4 && CONFIG_XTENSA_CPU_HAS_HIFI && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_XTENSA_HIFI
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_CPU_HAS_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI4)、[`CONFIG_XTENSA_CPU_HAS_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_XTENSA_CPU_HAS_HIFI4`、`CONFIG_XTENSA_CPU_HAS_HIFI`、`CONFIG_XTENSA_HIFI`。

<a id="CONFIG_XTENSA_HIFI5"></a>

## 40.11 `CONFIG_XTENSA_HIFI5`

**提示（Prompt）**：HiFi5 AudioEngine 指令（Instructions）

**说明（Help）**

启用 HiFi 5 指令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_CPU_HAS_HIFI5 && CONFIG_XTENSA_CPU_HAS_HIFI && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_XTENSA_HIFI
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_CPU_HAS_HIFI5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI5)、[`CONFIG_XTENSA_CPU_HAS_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_XTENSA_CPU_HAS_HIFI5`、`CONFIG_XTENSA_CPU_HAS_HIFI`、`CONFIG_XTENSA_HIFI`。

<a id="CONFIG_XTENSA_HIFI_SHARING"></a>

## 40.12 `CONFIG_XTENSA_HIFI_SHARING`

**提示（Prompt）**：HiFi 寄存器共享（HiFi Register Sharing）

**说明（Help）**

启用跨上下文切换（Context Switch）的硬件 HiFi 寄存器状态保留，使多个线程可以并发执行 HiFi 操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_HIFI && CONFIG_XTENSA_CPU_HAS_HIFI && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI)、[`CONFIG_XTENSA_CPU_HAS_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_XTENSA_HIFI`、`CONFIG_XTENSA_CPU_HAS_HIFI`。

<a id="CONFIG_XTENSA_HIFI_SHARING_MODEL"></a>

## 40.13 `CONFIG_XTENSA_HIFI_SHARING_MODEL`

**提示（Prompt）**：Xtensa HiFi 共享模型（Sharing Model）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_HIFI_SHARING && CONFIG_XTENSA_HIFI_SHARING && CONFIG_XTENSA_CPU_HAS_HIFI && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
CONFIG_XTENSA_EAGER_HIFI_SHARING
```

**可选项（Choices）**

```text
CONFIG_XTENSA_EAGER_HIFI_SHARING
CONFIG_XTENSA_LAZY_HIFI_SHARING
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options） → HiFi 寄存器共享（HiFi Register Sharing）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_HIFI_SHARING`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_HIFI_SHARING)、[`CONFIG_XTENSA_CPU_HAS_HIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_CPU_HAS_HIFI)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_EAGER_HIFI_SHARING`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_EAGER_HIFI_SHARING)、[`CONFIG_XTENSA_LAZY_HIFI_SHARING`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_LAZY_HIFI_SHARING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_XTENSA_CPU_HAS_HIFI`。

<a id="CONFIG_XTENSA_INTERRUPT_NONPREEMPTABLE"></a>

## 40.14 `CONFIG_XTENSA_INTERRUPT_NONPREEMPTABLE`

**提示（Prompt）**：Xtensa 异常与中断不可被抢占（Non-Preemptible Exceptions and Interrupts）

**说明（Help）**

允许使用中、高优先级中断，但不抢占低优先级中断和异常（Exception）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_LAZY_HIFI_SHARING"></a>

## 40.15 `CONFIG_XTENSA_LAZY_HIFI_SHARING`

**提示（Prompt）**：延迟式 HiFi 共享（Lazy HiFi Sharing）

**说明（Help）**

启用跨上下文切换（Context Switch）的延迟式 HiFi 寄存器共享（Lazy Sharing）。这意味着只有在线程实际使用 HiFi 指令时才保存和恢复 HiFi 寄存器，从而在不使用 HiFi 指令时更有效地利用资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
((CONFIG_SCHED_IPI_SUPPORTED && CONFIG_ARCH_HAS_DIRECTED_IPIS) || CONFIG_MP_MAX_NUM_CPUS = 1) && <choice CONFIG_XTENSA_HIFI_SHARING_MODEL>
```

**主动选择（Selects）**

```text
CONFIG_ARCH_IPI_LAZY_COPROCESSORS_SAVE
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa HiFi 选项（HiFi Options） → HiFi 寄存器共享（HiFi Register Sharing） → Xtensa HiFi 共享模型（Sharing Model）

**配置项引用（Symbol References）**：[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_XTENSA_HIFI_SHARING_MODEL`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_HIFI_SHARING_MODEL)、[`CONFIG_ARCH_IPI_LAZY_COPROCESSORS_SAVE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_IPI_LAZY_COPROCESSORS_SAVE)。

<a id="CONFIG_XTENSA_MMU"></a>

## 40.16 `CONFIG_XTENSA_MMU`

**提示（Prompt）**：Xtensa 内存管理单元支持（MMU Support）

**说明（Help）**

启用 Xtensa 内存管理单元（Memory Management Unit，MMU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**主动选择（Selects）**

```text
CONFIG_MMU
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT if CONFIG_USERSPACE
CONFIG_CURRENT_THREAD_USE_NO_TLS if CONFIG_USERSPACE
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT)、[`CONFIG_CURRENT_THREAD_USE_NO_TLS`](P001_kernel_配置项参考_1.md#CONFIG_CURRENT_THREAD_USE_NO_TLS)。

<a id="CONFIG_XTENSA_MMU_FLUSH_AUTOREFILL_DTLBS_ON_SWAP"></a>

## 40.17 `CONFIG_XTENSA_MMU_FLUSH_AUTOREFILL_DTLBS_ON_SWAP`

**提示（Prompt）**：切换页表时刷新所有自动重填数据 TLB（Auto-Refill Data TLBs）

**说明（Help）**

切换页表（Page Table）时，刷新，即使其失效，所有自动重填的数据地址转换后备缓冲（Auto-Refill Data TLB）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L261)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_MMU_NUM_L1_TABLES"></a>

## 40.18 `CONFIG_XTENSA_MMU_NUM_L1_TABLES`

**提示（Prompt）**：一级页表数量（Number of L1 Page Tables）

**说明（Help）**

指定地址转换表（Translation Table）的最大数量。该数量直接对应目标中的内存域（Memory Domain）数量，并且需要计入内核自身所需的一张表。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
1 if !CONFIG_USERSPACE
4
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L241)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_XTENSA_MMU_NUM_L2_TABLES"></a>

## 40.19 `CONFIG_XTENSA_MMU_NUM_L2_TABLES`

**提示（Prompt）**：二级页表数量（Number of L2 Page Tables）

**说明（Help）**

每张表最多可以覆盖 4MB 内存地址范围。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
20 if CONFIG_USERSPACE
10
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_XTENSA_MMU_PAGE_TABLE_STATS"></a>

## 40.20 `CONFIG_XTENSA_MMU_PAGE_TABLE_STATS`

**提示（Prompt）**：页表统计（Page Table Statistics）

**说明（Help）**

启用页表统计（Page Table Statistics），包括当前用量和历史使用的最大页表数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L268)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_MMU_PTEVADDR"></a>

## 40.21 `CONFIG_XTENSA_MMU_PTEVADDR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xtensa 页表的虚拟地址（Page Table Virtual Address，`PTEVADDR`）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
0x20000000 if CONFIG_XTENSA_MMU_PTEVADDR_20000000
0x60000000 if CONFIG_XTENSA_MMU_PTEVADDR_60000000
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_MMU_PTEVADDR_20000000`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU_PTEVADDR_20000000)、[`CONFIG_XTENSA_MMU_PTEVADDR_60000000`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU_PTEVADDR_60000000)。

<a id="CONFIG_XTENSA_MMU_PTEVADDR_20000000"></a>

## 40.22 `CONFIG_XTENSA_MMU_PTEVADDR_20000000`

**提示（Prompt）**：0x20000000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support） → 页表虚拟地址（Page Table Virtual Address）

<a id="CONFIG_XTENSA_MMU_PTEVADDR_60000000"></a>

## 40.23 `CONFIG_XTENSA_MMU_PTEVADDR_60000000`

**提示（Prompt）**：0x60000000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support） → 页表虚拟地址（Page Table Virtual Address）

<a id="CONFIG_XTENSA_MMU_PTEVADDR_SHIFT"></a>

## 40.24 `CONFIG_XTENSA_MMU_PTEVADDR_SHIFT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xtensa 页表虚拟地址（Page Table Virtual Address，`PTEVADDR`）的位移位数（Bit Shift Number）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
29 if CONFIG_XTENSA_MMU_PTEVADDR_20000000
29 if CONFIG_XTENSA_MMU_PTEVADDR_60000000
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_XTENSA_MMU_PTEVADDR_20000000`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU_PTEVADDR_20000000)、[`CONFIG_XTENSA_MMU_PTEVADDR_60000000`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU_PTEVADDR_60000000)。

<a id="CONFIG_XTENSA_MMU_USE_DEFAULT_MAPPINGS"></a>

## 40.25 `CONFIG_XTENSA_MMU_USE_DEFAULT_MAPPINGS`

**提示（Prompt）**：使用架构默认 MMU 映射（Default MMU Mappings）

**说明（Help）**

启用后，内存管理单元（MMU）会初始化少量默认映射，覆盖代码（Text）、数据（Data）、未初始化数据（BSS）、只读数据（rodata）等区域，以提供合理的默认配置。详情参阅 `mmu_zephyr_ranges[]`。

禁用后，片上系统（SoC）必须通过 `xtensa_soc_mmu_ranges[]` 提供所有必要的映射，使 SoC 能更细致地控制映射。如不确定，选择 `Y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MMU && CONFIG_CPU_HAS_MMU && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → Xtensa 内存管理单元支持（MMU Support）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS"></a>

## 40.26 `CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS`

**提示（Prompt）**：使用包含更多 NOP 的 Xtensa 专用 arch_spin_relax()（No-Operation Instructions）

**说明（Help）**

某些 Xtensa 片上系统（SoC），尤其在对称多处理（SMP）模式下，获取自旋锁（Spinlock）失败后可能需要额外的空操作指令（NOP）。这给总线留出更多时间，在 CPU 之间同步 RCW 事务（Transaction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_MPU"></a>

## 40.27 `CONFIG_XTENSA_MPU`

**提示（Prompt）**：Xtensa 内存保护单元支持（MPU Support）［实验性，EXPERIMENTAL］

**说明（Help）**

启用 Xtensa 内存保护单元（Memory Protection Unit，MPU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CACHE && !CONFIG_SMP && CONFIG_CPU_HAS_MPU && CONFIG_XTENSA
```

**主动选择（Selects）**

```text
CONFIG_MPU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_XTENSA_SMALL_VECTOR_TABLE_ENTRY
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE
CONFIG_CURRENT_THREAD_USE_NO_TLS if CONFIG_USERSPACE
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_XTENSA_SMALL_VECTOR_TABLE_ENTRY`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_SMALL_VECTOR_TABLE_ENTRY)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_CURRENT_THREAD_USE_NO_TLS`](P001_kernel_配置项参考_1.md#CONFIG_CURRENT_THREAD_USE_NO_TLS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_XTENSA_NUM_SPIN_RELAX_NOPS"></a>

## 40.28 `CONFIG_XTENSA_NUM_SPIN_RELAX_NOPS`

**提示（Prompt）**：arch_spin_relax() 使用的 NOP 数量（Number of NOPs）

**说明（Help）**

指定 Xtensa 专用 `arch_spin_relax()` 中的空操作指令（NOP）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → 使用包含更多 NOP 的 Xtensa 专用 arch_spin_relax()（No-Operation Instructions）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MORE_SPIN_RELAX_NOPS)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_RESET_VECTOR"></a>

## 40.29 `CONFIG_XTENSA_RESET_VECTOR`

**提示（Prompt）**：构建复位向量代码（Reset Vector Code）

**说明（Help）**

控制是否构建初始复位向量代码（Reset Vector Code）。模拟器（Simulator）始终需要这段代码；实际开发板可能已在启动 ROM（Boot ROM）中实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT595S_F1
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_HIFI1
CONFIG_SOC_MIMXRT758S_HIFI1
CONFIG_SOC_MIMXRT735S_HIFI1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
CONFIG_SOC_ACP_6_0
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_SOC_MIMXRT595S_F1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_F1)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)、[`CONFIG_SOC_ACP_6_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ACP_6_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_ACP_6_0`。

<a id="CONFIG_XTENSA_SMALL_VECTOR_TABLE_ENTRY"></a>

## 40.30 `CONFIG_XTENSA_SMALL_VECTOR_TABLE_ENTRY`

**提示（Prompt）**：针对较小向量表条目的变通措施（Small Vector Table Entries）

**说明（Help）**

增加一小段间接跳转，绕过向量表条目（Vector Table Entry）的大小限制；将默认处理程序移到向量表末尾，并重命名为 `_Level\LVL\()VectorHelper`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

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
CONFIG_XTENSA_MPU
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_XTENSA_MPU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MPU)。

<a id="CONFIG_XTENSA_SYSCALL_USE_HELPER"></a>

## 40.31 `CONFIG_XTENSA_SYSCALL_USE_HELPER`

**提示（Prompt）**：使用用户空间系统调用辅助函数（Userspace Syscall Helper）

**说明（Help）**

使用系统调用辅助函数（Syscall Helper）传递超过 3 个参数。这是针对某些工具链无法正确建模寄存器用量问题的变通措施（Workaround）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_XTENSA_MMU || CONFIG_XTENSA_MPU) && CONFIG_USERSPACE && CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y if "zephyr" = "xt-clang"
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L297)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_MMU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MMU)、[`CONFIG_XTENSA_MPU`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_MPU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_SYSCALL_USE_HELPER_ALL"></a>

## 40.32 `CONFIG_XTENSA_SYSCALL_USE_HELPER_ALL`

**提示（Prompt）**：所有参数数量均使用用户空间系统调用辅助函数（Userspace Syscall Helper）

**说明（Help）**

除 `XTENSA_SYSCALL_USE_HELPER` 已处理的 4–6 个参数调用外，也让 0–3 个参数的系统调用通过独立的辅助函数（Out-of-Line Helper Function）执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_SYSCALL_USE_HELPER && CONFIG_XTENSA
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L306)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options） → 使用用户空间系统调用辅助函数（Userspace Syscall Helper）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_SYSCALL_USE_HELPER`](P040_arch_xtensa_配置项参考.md#CONFIG_XTENSA_SYSCALL_USE_HELPER)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)。

<a id="CONFIG_XTENSA_USE_CORE_CRT1"></a>

## 40.33 `CONFIG_XTENSA_USE_CORE_CRT1`

**提示（Prompt）**：使用内核提供的 crt1.S（Core crt1.S）

**说明（Help）**

片上系统（SoC）或开发板可将此设置设为 false，以定义自己的 `__start`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT595S_F1
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_HIFI1
CONFIG_SOC_MIMXRT758S_HIFI1
CONFIG_SOC_MIMXRT735S_HIFI1
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_MIMX8QM6_ADSP
CONFIG_SOC_MIMX8ML8_ADSP
CONFIG_SOC_MIMX8UD7_ADSP
CONFIG_SOC_MIMX8QX6_ADSP
CONFIG_SOC_SERIES_INTEL_ADSP_CAVS
```

**定义位置（Location）**：[`arch/xtensa/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → Xtensa 选项（Xtensa Options）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_SOC_MIMXRT595S_F1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_F1)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI1)、[`CONFIG_SOC_MIMXRT758S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_HIFI1)、[`CONFIG_SOC_MIMXRT735S_HIFI1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_HIFI1)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_MIMX8QM6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6_ADSP)、[`CONFIG_SOC_MIMX8ML8_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_ADSP)、[`CONFIG_SOC_MIMX8UD7_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7_ADSP)、[`CONFIG_SOC_MIMX8QX6_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6_ADSP)、[`CONFIG_SOC_SERIES_INTEL_ADSP_CAVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_CAVS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_HIFI4`。

<!-- kconfig-navigation -->

[上一章](P039_arch_x86_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P041_boards_Kconfig_配置项参考.md)
