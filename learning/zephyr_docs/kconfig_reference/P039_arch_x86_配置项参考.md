---
id: learning.zephyr-docs.kconfig-reference.page-39
title: "`arch/x86`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第39章\_`arch/x86`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/x86` 的 74 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARCH_HAS_STACKWALK"></a>

## 39.1 `CONFIG_ARCH_HAS_STACKWALK`

原库同名定义共 5 条；本项为数据库第 502 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，表示已实现 `arch_stack_walk()` API，且可以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_OMIT_FRAME_POINTER && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_X86_DEBUG_INFO
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L152)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_OMIT_FRAME_POINTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OMIT_FRAME_POINTER)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_DEBUG_INFO`](P039_arch_x86_配置项参考.md#CONFIG_X86_DEBUG_INFO)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_ARCH_HAS_STACKWALK--record-503"></a>

## 39.2 `CONFIG_ARCH_HAS_STACKWALK`

原库同名定义共 5 条；本项为数据库第 503 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，表示已实现 `arch_stack_walk()` API，且可以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_OMIT_FRAME_POINTER && CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_X86_DEBUG_INFO
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L32)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_OMIT_FRAME_POINTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OMIT_FRAME_POINTER)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_DEBUG_INFO`](P039_arch_x86_配置项参考.md#CONFIG_X86_DEBUG_INFO)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_CPU_APOLLO_LAKE"></a>

## 39.3 `CONFIG_CPU_APOLLO_LAKE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Apollo Lake 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_X86_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_X86_MMU
CONFIG_X86_MMU
CONFIG_X86_CPU_HAS_MMX
CONFIG_X86_CPU_HAS_SSE
CONFIG_X86_CPU_HAS_SSE2
CONFIG_X86_CPU_HAS_SSE3
CONFIG_X86_CPU_HAS_SSSE3
CONFIG_X86_CPU_HAS_SSE41
CONFIG_X86_CPU_HAS_SSE42
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_APOLLO_LAKE
```

**定义位置（Location）**：[`arch/x86/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_X86_CPU_HAS_MMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_MMX)、[`CONFIG_X86_CPU_HAS_SSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE)、[`CONFIG_X86_CPU_HAS_SSE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE2)、[`CONFIG_X86_CPU_HAS_SSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE3)、[`CONFIG_X86_CPU_HAS_SSSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSSE3)、[`CONFIG_X86_CPU_HAS_SSE41`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE41)、[`CONFIG_X86_CPU_HAS_SSE42`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE42)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_X86_CPU_HAS_MMX`、`CONFIG_X86_CPU_HAS_SSE`、`CONFIG_X86_CPU_HAS_SSE2`、`CONFIG_X86_CPU_HAS_SSE3`、`CONFIG_X86_CPU_HAS_SSSE3`、`CONFIG_X86_CPU_HAS_SSE41`、`CONFIG_X86_CPU_HAS_SSE42`、`CONFIG_SOC_APOLLO_LAKE`。

<a id="CONFIG_CPU_ATOM"></a>

## 39.4 `CONFIG_CPU_ATOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Atom 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_X86_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_X86_MMU
CONFIG_X86_CPU_HAS_MMX
CONFIG_X86_CPU_HAS_SSE
CONFIG_X86_CPU_HAS_SSE2
CONFIG_X86_CPU_HAS_SSE3
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_ATOM
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_PANTHER_LAKE
```

**定义位置（Location）**：[`arch/x86/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_X86_CPU_HAS_MMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_MMX)、[`CONFIG_X86_CPU_HAS_SSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE)、[`CONFIG_X86_CPU_HAS_SSE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE2)、[`CONFIG_X86_CPU_HAS_SSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE3)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATOM)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_X86_CPU_HAS_MMX`、`CONFIG_X86_CPU_HAS_SSE`、`CONFIG_X86_CPU_HAS_SSE2`、`CONFIG_X86_CPU_HAS_SSE3`、`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_ATOM`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_CPU_LAKEMONT_PERF"></a>

## 39.5 `CONFIG_CPU_LAKEMONT_PERF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Lakemont Performance 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_X86_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_X86_MMU
CONFIG_X86_CPU_HAS_MMX
CONFIG_X86_CPU_HAS_SSE
CONFIG_X86_CPU_HAS_SSE2
CONFIG_X86_CPU_HAS_SSE3
CONFIG_X86_CPU_HAS_SSSE3
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_LAKEMONT
```

**定义位置（Location）**：[`arch/x86/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_X86_CPU_HAS_MMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_MMX)、[`CONFIG_X86_CPU_HAS_SSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE)、[`CONFIG_X86_CPU_HAS_SSE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE2)、[`CONFIG_X86_CPU_HAS_SSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE3)、[`CONFIG_X86_CPU_HAS_SSSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSSE3)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_X86_CPU_HAS_MMX`、`CONFIG_X86_CPU_HAS_SSE`、`CONFIG_X86_CPU_HAS_SSE2`、`CONFIG_X86_CPU_HAS_SSE3`、`CONFIG_X86_CPU_HAS_SSSE3`、`CONFIG_SOC_LAKEMONT`。

<a id="CONFIG_CPU_LAKEMONT_VALUE"></a>

## 39.6 `CONFIG_CPU_LAKEMONT_VALUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Lakemont Value 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_CPU_HAS_FPU
CONFIG_ARCH_HAS_STACK_PROTECTION if CONFIG_X86_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_X86_MMU
CONFIG_CPU_HAS_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
```

**定义位置（Location）**：[`arch/x86/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`、`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_SOC_FAMILY_INTEL_ISH`。

<a id="CONFIG_EAGER_FPU_SHARING"></a>

## 39.7 `CONFIG_EAGER_FPU_SHARING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项在每次上下文切换（Context Switch）时无条件保存／恢复浮点单元（FPU）与单指令多数据（SIMD）寄存器状态。它缓解 CVE-2018-3665 漏洞，但会降低性能。对于存在该漏洞、且在 FPU 寄存器组中处理敏感信息的系统，无论 FPU 由一个还是多个线程使用，只要启用 `CONFIG_FPU`，就应使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU && CONFIG_USERSPACE && CONFIG_CPU_HAS_FPU && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_X86_NO_LAZY_FP
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L101)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities） → 架构浮点选项（Architecture Floating Point Options）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_LAZY_FP`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_LAZY_FP)。

<a id="CONFIG_GDT_DYNAMIC"></a>

## 39.8 `CONFIG_GDT_DYNAMIC`

**提示（Prompt）**：将 GDT 存储在 RAM 中以便修改（Global Descriptor Table）

**说明（Help）**

将全局描述符表（Global Descriptor Table，GDT）存储在 RAM 而非 ROM 中，以便在运行时修改，代价是额外占用一些内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SET_GDT && !CONFIG_X86_64 && CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_USERSPACE
CONFIG_X86_USE_THREAD_LOCAL_STORAGE
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L35)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 内存布局选项（Memory Layout Options） → 在启动过程中设置全局描述符表（GDT）

**配置项引用（Symbol References）**：[`CONFIG_SET_GDT`](P039_arch_x86_配置项参考.md#CONFIG_SET_GDT)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_STACK_PROTECTION`](P039_arch_x86_配置项参考.md#CONFIG_X86_STACK_PROTECTION)、[`CONFIG_X86_USERSPACE`](P039_arch_x86_配置项参考.md#CONFIG_X86_USERSPACE)、[`CONFIG_X86_USE_THREAD_LOCAL_STORAGE`](P039_arch_x86_配置项参考.md#CONFIG_X86_USE_THREAD_LOCAL_STORAGE)。

<a id="CONFIG_GDT_RESERVED_NUM_ENTRIES"></a>

## 39.9 `CONFIG_GDT_RESERVED_NUM_ENTRIES`

**提示（Prompt）**：预留的 GDT 条目占位数量（Reserved GDT Entry Place Holders）

**说明（Help）**

定义预留的全局描述符表（GDT）条目占位数量，这些条目可以在运行时填充。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GDT_DYNAMIC && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L42)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 内存布局选项（Memory Layout Options） → 在启动过程中设置全局描述符表（GDT） → 将 GDT 存储在 RAM 中以便修改（Global Descriptor Table）

**配置项引用（Symbol References）**：[`CONFIG_GDT_DYNAMIC`](P039_arch_x86_配置项参考.md#CONFIG_GDT_DYNAMIC)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_IDT_NUM_VECTORS"></a>

## 39.10 `CONFIG_IDT_NUM_VECTORS`

**提示（Prompt）**：IDT 向量数量（Number of IDT Vectors）

**说明（Help）**

指定中断描述符表（Interrupt Descriptor Table，IDT）中的中断向量条目数量。默认支持全部 256 个向量，此时 IDT 需要 2048 字节内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 256]
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 内存布局选项（Memory Layout Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_IRQ_OFFLOAD_VECTOR"></a>

## 39.11 `CONFIG_IRQ_OFFLOAD_VECTOR`

**提示（Prompt）**：用于中断卸载的 IDT 向量（IRQ Offload）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IRQ_OFFLOAD && CONFIG_X86
```

**默认值（Defaults）**

```text
33
```

**取值范围（Ranges）**

```text
[32, 255]
```

**定义位置（Location）**：[`arch/x86/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_IRQ_OFFLOAD`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_IRQ_OFFLOAD)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ISR_DEPTH"></a>

## 39.12 `CONFIG_ISR_DEPTH`

**提示（Prompt）**：最大中断嵌套深度（Maximum IRQ Nesting Depth）

**说明（Help）**

允许的嵌套层数越多，中断请求（IRQ）栈所需空间就越大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L59)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_ISR_SUBSTACK_SIZE"></a>

## 39.13 `CONFIG_ISR_SUBSTACK_SIZE`

**提示（Prompt）**：ISR 子栈大小（ISR Substack Size）

**说明（Help）**

从中断服务例程（ISR）栈中为每一层嵌套中断请求（IRQ）预留的字节数。必须是 16 的整数倍，以保持栈对齐（Stack Alignment）。注意，`CONFIG_ISR_SUBSTACK_SIZE * CONFIG_ISR_DEPTH` 必须等于 `CONFIG_ISR_STACK_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L65)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_LAZY_FPU_SHARING"></a>

## 39.14 `CONFIG_LAZY_FPU_SHARING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项允许多个线程使用浮点寄存器（Floating-Point Register），在上下文切换（Context Switch）时使用延迟保存／恢复（Lazy Save / Restore）寄存器状态的逻辑。对于 Intel Core 处理器，这可能受到允许恶意软件读取全部浮点寄存器内容的漏洞利用影响，参见 CVE-2018-3665。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FPU && !CONFIG_EAGER_FPU_SHARING && CONFIG_FPU_SHARING && CONFIG_CPU_HAS_FPU && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_X86_NO_LAZY_FP || !CONFIG_USERSPACE
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L116)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities） → 架构浮点选项（Architecture Floating Point Options）

**配置项引用（Symbol References）**：[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_EAGER_FPU_SHARING`](P039_arch_x86_配置项参考.md#CONFIG_EAGER_FPU_SHARING)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_LAZY_FP`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_LAZY_FP)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

<a id="CONFIG_MAX_IRQ_LINES"></a>

## 39.15 `CONFIG_MAX_IRQ_LINES`

**提示（Prompt）**：中断请求线数量（Number of IRQ Lines）

**说明（Help）**

指定系统中的中断请求线（IRQ Line）数量。它决定 `_irq_to_interrupt_vector_table` 的大小，该表用于跟踪中断向量与 IRQ 编号之间的对应关系。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 224]
```

**定义位置（Location）**：[`arch/x86/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_MULTIBOOT"></a>

## 39.16 `CONFIG_MULTIBOOT`

**提示（Prompt）**：生成 Multiboot 头（Multiboot Header）

**说明（Help）**

在输出的可执行文件中嵌入 Multiboot 头（Multiboot Header）。GRUB 等部分引导加载程序（Bootloader）在加载 Zephyr 时会使用它。如不确定，可以放心保持启用。它只会将代码段（Text Segment）增大 12–16 字节，不需要时通常会被忽略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_PC_COMPATIBLE && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/Kconfig:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L287)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_PC_COMPATIBLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_PC_COMPATIBLE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_MULTIBOOT_INFO"></a>

## 39.17 `CONFIG_MULTIBOOT_INFO`

**提示（Prompt）**：保留 Multiboot 信息结构（Information Structure）

**说明（Help）**

Multiboot 向内核入口点（Kernel Entry Point）传递一个指向信息结构的指针。某些驱动，例如 Multiboot 帧缓冲显示驱动（Framebuffer Display Driver），需要访问此结构中的信息，因此会设置此选项，将数据保存在永久有效的位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTIBOOT && CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_MULTIBOOT_MEMMAP
```

**定义位置（Location）**：[`arch/x86/Kconfig:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L299)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 生成 Multiboot 头（Multiboot Header）

**配置项引用（Symbol References）**：[`CONFIG_MULTIBOOT`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_MULTIBOOT_MEMMAP`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT_MEMMAP)。

<a id="CONFIG_MULTIBOOT_MEMMAP"></a>

## 39.18 `CONFIG_MULTIBOOT_MEMMAP`

**提示（Prompt）**：若提供则使用 Multiboot 内存映射（Memory Map）

**说明（Help）**

如果加载程序（Loader）提供 Multiboot 内存映射（Memory Map），则使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTIBOOT && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_MULTIBOOT_INFO
CONFIG_X86_MEMMAP
```

**定义位置（Location）**：[`arch/x86/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 生成 Multiboot 头（Multiboot Header）

**配置项引用（Symbol References）**：[`CONFIG_MULTIBOOT`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_MULTIBOOT_INFO`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT_INFO)、[`CONFIG_X86_MEMMAP`](P039_arch_x86_配置项参考.md#CONFIG_X86_MEMMAP)。

<a id="CONFIG_NESTED_INTERRUPTS"></a>

## 39.19 `CONFIG_NESTED_INTERRUPTS`

**提示（Prompt）**：嵌套中断（Nested Interrupts）

**说明（Help）**

启用嵌套中断（Nested Interrupts）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L8)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_PCIE_MMIO_CFG"></a>

## 39.20 `CONFIG_PCIE_MMIO_CFG`

**提示（Prompt）**：通过 MMIO 访问 PCI 配置空间（PCI Configuration Space Access）

**说明（Help）**

选择使用内存映射（Memory-Mapped）的 PCI Express 扩展配置空间（Extended Configuration Space），替代传统的 `0xCF8` / `0xCFC` I/O 端口寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_ACPI
```

**定义位置（Location）**：[`arch/x86/Kconfig:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L248)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)。

<a id="CONFIG_PIC_DISABLE"></a>

## 39.21 `CONFIG_PIC_DISABLE`

**提示（Prompt）**：禁用可编程中断控制器（PIC）

**说明（Help）**

启动时禁用传统 i8259 可编程中断控制器（PIC）上的所有中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_REBOOT_RST_CNT"></a>

## 39.22 `CONFIG_REBOOT_RST_CNT`

**提示（Prompt）**：通过 RST_CNT 寄存器重启（Reboot）

**说明（Help）**

通过 `RST_CNT` 寄存器重启，返回基本输入输出系统（BIOS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`arch/x86/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 重启实现（Reboot Implementation）

<a id="CONFIG_SCHED_IPI_VECTOR"></a>

## 39.23 `CONFIG_SCHED_IPI_VECTOR`

**提示（Prompt）**：用于调度器处理器间中断的 IDT 向量（Scheduler IPI）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
34
```

**取值范围（Ranges）**

```text
[33, 255]
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L42)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_SET_GDT"></a>

## 39.24 `CONFIG_SET_GDT`

**提示（Prompt）**：在启动过程中设置全局描述符表（GDT）

**说明（Help）**

在启动过程中设置全局描述符表（GDT）。不过，某些安全场景中，更早的引导加载程序（Bootloader）阶段已经正确设置 GDT，此选项可能与其冲突；此时应禁用。禁用后，全局 `_gdt` 指针将不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_USERSPACE
CONFIG_X86_USE_THREAD_LOCAL_STORAGE
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L25)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 内存布局选项（Memory Layout Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_STACK_PROTECTION`](P039_arch_x86_配置项参考.md#CONFIG_X86_STACK_PROTECTION)、[`CONFIG_X86_USERSPACE`](P039_arch_x86_配置项参考.md#CONFIG_X86_USERSPACE)、[`CONFIG_X86_USE_THREAD_LOCAL_STORAGE`](P039_arch_x86_配置项参考.md#CONFIG_X86_USE_THREAD_LOCAL_STORAGE)。

<a id="CONFIG_SRAM_OFFSET"></a>

## 39.25 `CONFIG_SRAM_OFFSET`

原库同名定义共 2 条；本项为数据库第 18406 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

许多类似 PC 的 x86 平台在物理内存的第一个兆字节中有多个保留区域。此值指定相对于 RAM 起始地址的偏移，以将内核加载到物理内存并避开这些区域。注意，这不包括 `locore`，后者包含位于物理内存前 64K 中的实模式启动代码（Real Mode Bootstrap Code）。此值通常需要按页对齐（Page-Aligned）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**默认值（Defaults）**

```text
0x100000 if CONFIG_X86_PC_COMPATIBLE
```

**定义位置（Location）**：[`arch/x86/Kconfig:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L201)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_PC_COMPATIBLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_PC_COMPATIBLE)。

<a id="CONFIG_TLB_IPI_VECTOR"></a>

## 39.26 `CONFIG_TLB_IPI_VECTOR`

**提示（Prompt）**：用于 TLB 远程失效处理器间中断的 IDT 向量（TLB Shootdown IPI）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
35
```

**取值范围（Ranges）**

```text
[33, 255]
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L48)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_64"></a>

## 39.27 `CONFIG_X86_64`

**提示（Prompt）**：以 64 位模式运行（64-bit Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_64BIT
CONFIG_USE_SWITCH
CONFIG_USE_SWITCH_SUPPORTED
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_X86_MMU
CONFIG_X86_CPU_HAS_MMX
CONFIG_X86_CPU_HAS_SSE
CONFIG_X86_CPU_HAS_SSE2
CONFIG_X86_MMX
CONFIG_X86_SSE
CONFIG_X86_SSE2
CONFIG_ARCH_HAS_DIRECTED_IPIS if !CONFIG_X2APIC
```

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
```

**定义位置（Location）**：[`arch/x86/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_X86_CPU_HAS_MMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_MMX)、[`CONFIG_X86_CPU_HAS_SSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE)、[`CONFIG_X86_CPU_HAS_SSE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE2)、[`CONFIG_X86_MMX`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMX)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)、[`CONFIG_X86_SSE2`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE2)、[`CONFIG_ARCH_HAS_DIRECTED_IPIS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_DIRECTED_IPIS)、[`CONFIG_X2APIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_X2APIC)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_MMX`、`CONFIG_X86_CPU_HAS_SSE`、`CONFIG_X86_CPU_HAS_SSE2`、`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_X86_BOUNDS_CHECK_BYPASS_MITIGATION"></a>

## 39.28 `CONFIG_X86_BOUNDS_CHECK_BYPASS_MITIGATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏配置，用于选择架构无关选项：如果尚不知道 CPU 是否不受 Spectre V1 影响，则默认启用其缓解措施（Mitigation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_X86_NO_SPECTRE_V1
```

**主动选择（Selects）**

```text
CONFIG_BOUNDS_CHECK_BYPASS_MITIGATION
```

**定义位置（Location）**：[`arch/x86/Kconfig:456`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L456)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECTRE_V1`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V1)、[`CONFIG_BOUNDS_CHECK_BYPASS_MITIGATION`](P001_kernel_配置项参考_1.md#CONFIG_BOUNDS_CHECK_BYPASS_MITIGATION)。

<a id="CONFIG_X86_CET"></a>

## 39.29 `CONFIG_X86_CET`

**提示（Prompt）**：控制流强制技术（Control-flow Enforcement Technology，CET）

**说明（Help）**

启用控制流强制技术（Control-flow Enforcement Technology，CET）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_CET && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:505`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L505)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_CET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_CET)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_CET`。

<a id="CONFIG_X86_CET_IBT"></a>

## 39.30 `CONFIG_X86_CET_IBT`

**提示（Prompt）**：间接分支跟踪（Indirect Branch Tracking，IBT）

**说明（Help）**

启用间接分支跟踪（Indirect Branch Tracking，IBT）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CET && CONFIG_PICOLIBC_USE_MODULE && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L511)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 控制流强制技术（Control-flow Enforcement Technology，CET）

**配置项引用（Symbol References）**：[`CONFIG_X86_CET`](P039_arch_x86_配置项参考.md#CONFIG_X86_CET)、[`CONFIG_PICOLIBC_USE_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_USE_MODULE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_CET_SHADOW_STACK_ALIGNMENT"></a>

## 39.31 `CONFIG_X86_CET_SHADOW_STACK_ALIGNMENT`

**提示（Prompt）**：影子栈对齐（Shadow Stack Alignment）

**说明（Help）**

设置影子栈（Shadow Stack）的对齐要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK && CONFIG_X86
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/x86/Kconfig:517`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L517)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_CET_SOC_PREPARE_SHADOW_STACK_SWITCH"></a>

## 39.32 `CONFIG_X86_CET_SOC_PREPARE_SHADOW_STACK_SWITCH`

**提示（Prompt）**：由 SoC 准备影子栈切换（Shadow Stack Switch）

**说明（Help）**

启用后，在切换影子栈（Shadow Stack）之前立即调用片上系统（SoC）代码。应通过 `soc_prepare_shadow_stack_switch` 汇编宏提供该代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:532`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L532)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_CET_VERIFY_KERNEL_SHADOW_STACK"></a>

## 39.33 `CONFIG_X86_CET_VERIFY_KERNEL_SHADOW_STACK`

**提示（Prompt）**：验证内核影子栈（Kernel Shadow Stack）

**说明（Help）**

启用后，在线程换出（Swap Out）时，如果影子栈（Shadow Stack）已启用，内核会检查其影子栈指针不是空指针；出现异常情况意味着可能存在篡改影子栈的尝试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HW_SHADOW_STACK && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:524`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L524)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_COMMON_PAGE_TABLE"></a>

## 39.34 `CONFIG_X86_COMMON_PAGE_TABLE`

**提示（Prompt）**：所有线程共用一张页表（Single Page Table）

**说明（Help）**

启用后，用户空间内存域（Userspace Memory Domain）不再各自拥有页表（Page Table）；上下文切换（Context Switch）操作改为直接修改现有页表。这会慢得多，但显著减少页表占用的 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && !CONFIG_SMP && !CONFIG_X86_KPTI && CONFIG_X86
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/x86/Kconfig:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L338)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_X86_KPTI`](P039_arch_x86_配置项参考.md#CONFIG_X86_KPTI)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_DEBUG_INFO"></a>

## 39.35 `CONFIG_X86_DEBUG_INFO`

**提示（Prompt）**：系统调试信息（System Debugging Information）

**说明（Help）**

添加可供调试器（Debugger）调试系统使用的各种信息，或启用在运行时报告额外调试信息的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_ARCH_HAS_STACKWALK
CONFIG_ARCH_HAS_STACKWALK
```

**定义位置（Location）**：[`arch/x86/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_ARCH_HAS_STACKWALK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARCH_HAS_STACKWALK)。

<a id="CONFIG_X86_DISABLE_SSBD"></a>

## 39.36 `CONFIG_X86_DISABLE_SSBD`

**提示（Prompt）**：禁用推测性存储绕过（Speculative Store Bypass）

**说明（Help）**

禁用推测性存储绕过（Speculative Store Bypass），以缓解某些类型的侧信道攻击（Side Channel Attack）。原文引用《推测执行侧信道》（Speculative Execution Side Channels）2.0 版的说明：设置 SSBD 后，加载操作在所有更早的存储操作地址都已确定之前，不会推测执行；这确保同一个逻辑处理器上的加载操作不会因绕过更早的存储操作，而推测性地使用过时的数据值。

启用后，此设置应用于系统中的所有线程。对于不需要此特性的 CPU，即使启用也不会产生影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_X86_NO_SPECTRE_V4
```

**定义位置（Location）**：[`arch/x86/Kconfig:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L427)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECTRE_V4`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V4)。

<a id="CONFIG_X86_DYNAMIC_IRQ_STUBS"></a>

## 39.37 `CONFIG_X86_DYNAMIC_IRQ_STUBS`

**提示（Prompt）**：动态中断桩数量（Number of Dynamic Interrupt Stubs）

**说明（Help）**

使用 `irq_connect_dynamic()` 安装中断处理程序，需要在构建时生成一些桩代码（Stub Code）；每个动态中断对应一个桩。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_INTERRUPTS && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L141)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_EFI"></a>

## 39.38 `CONFIG_X86_EFI`

**提示（Prompt）**：可扩展固件接口（EFI）

**说明（Help）**

启用可扩展固件接口（EFI）支持，即构建带有 `zefi` 支持的镜像。更多信息参阅 `arch/x86/zefi/README.txt`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_EFI && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/Kconfig:477`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L477)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_EFI`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_EFI)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_EFI_CONSOLE"></a>

## 39.39 `CONFIG_X86_EFI_CONSOLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将统一可扩展固件接口（UEFI）的控制台设备用作 Zephyr 的 `printk` 处理程序。要求 Zephyr 代码不得干扰固件控制台使用的硬件，例如 UART 或帧缓冲（Framebuffer）；还要求固件环境及其页表（Page Table）使用的所有内存均独立且被保留。通常可以认为这些条件成立，但运行时没有自动检查来验证。还必须禁用其他所有控制台／`printk` 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_EFI && CONFIG_X86_64 && !CONFIG_X86_VERY_EARLY_CONSOLE && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_UART_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_EFI_CONSOLE
```

**定义位置（Location）**：[`arch/x86/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 可扩展固件接口（EFI）

**配置项引用（Symbol References）**：[`CONFIG_X86_EFI`](P039_arch_x86_配置项参考.md#CONFIG_X86_EFI)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86_VERY_EARLY_CONSOLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_VERY_EARLY_CONSOLE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_UART_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CONSOLE)、[`CONFIG_EFI_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EFI_CONSOLE)。

<a id="CONFIG_X86_ENABLE_EXTENDED_IBRS"></a>

## 39.40 `CONFIG_X86_ENABLE_EXTENDED_IBRS`

**提示（Prompt）**：扩展间接分支限制推测（Extended IBRS）

**说明（Help）**

启用扩展间接分支限制推测（Extended Indirect Branch Restricted Speculation）的始终开启（Always On）特性，以缓解间接分支控制（Indirect Branch Control）漏洞，即 Spectre V2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_X86_NO_SPECTRE_V2
```

**定义位置（Location）**：[`arch/x86/Kconfig:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L447)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECTRE_V2`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V2)。

<a id="CONFIG_X86_ENABLE_TSS"></a>

## 39.41 `CONFIG_X86_ENABLE_TSS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项为内核执行定义任务状态段（Task State Segment，TSS），用于处理双重故障（Double Fault）或进行权限提升（Privilege Elevation）。它还定义专用 TSS 和处理程序，以正确处理双重故障异常，避免系统直接进入三重故障（Triple Fault）并复位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_USERSPACE
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L54)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_STACK_PROTECTION`](P039_arch_x86_配置项参考.md#CONFIG_X86_STACK_PROTECTION)、[`CONFIG_X86_USERSPACE`](P039_arch_x86_配置项参考.md#CONFIG_X86_USERSPACE)。

<a id="CONFIG_X86_EXCEPTION_STACK_SIZE"></a>

## 39.42 `CONFIG_X86_EXCEPTION_STACK_SIZE`

**提示（Prompt）**：异常栈大小（Exception Stack Size）

**说明（Help）**

每个 CPU 都有一个异常栈（Exception Stack），同时用于异常处理和早期内核／CPU 初始化。它们只需支持有限的调用树深度（Call-Tree Depth），并且必须能放入低地址核心区（Low Core），因此通常小于中断服务例程（ISR）栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L23)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_EXTRA_PAGE_TABLE_PAGES"></a>

## 39.43 `CONFIG_X86_EXTRA_PAGE_TABLE_PAGES`

**提示（Prompt）**：在页表中预留额外页（Extra Pages）

**说明（Help）**

整个页表（Page Table）在构建时预分配，其大小取决于地址空间范围。此选项允许为页表预留额外的页，每页大小为 `CONFIG_MMU_PAGE_SIZE`，供 `gen_mmu.py` 使用。除非完全确定需要，否则设为 0。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_MMU && CONFIG_X86
```

**默认值（Defaults）**

```text
1 if CONFIG_X86_PAE && ((CONFIG_SRAM_DEPRECATED_KCONFIG_SET && CONFIG_KERNEL_VM_BASE != CONFIG_SRAM_BASE_ADDRESS) || (!CONFIG_SRAM_DEPRECATED_KCONFIG_SET && CONFIG_KERNEL_VM_BASE != 0))
0
```

**定义位置（Location）**：[`arch/x86/Kconfig:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L364)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_PAE`](P039_arch_x86_配置项参考.md#CONFIG_X86_PAE)、[`CONFIG_SRAM_DEPRECATED_KCONFIG_SET`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_DEPRECATED_KCONFIG_SET)、[`CONFIG_KERNEL_VM_BASE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_VM_BASE)、[`CONFIG_SRAM_BASE_ADDRESS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_BASE_ADDRESS)。

<a id="CONFIG_X86_FP_USE_SOFT_FLOAT"></a>

## 39.44 `CONFIG_X86_FP_USE_SOFT_FLOAT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用软件浮点运算（Software Floating Point Operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if !CONFIG_FPU
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L133)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities） → 架构浮点选项（Architecture Floating Point Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)。

<a id="CONFIG_X86_KPTI"></a>

## 39.45 `CONFIG_X86_KPTI`

**提示（Prompt）**：内核页表隔离（Kernel Page Table Isolation）

**说明（Help）**

实现内核页表隔离（Kernel Page Table Isolation），以缓解利用 Meltdown 读取内核 RAM 的攻击。它会给用户线程的中断和系统调用带来显著性能开销，额外页表（Page Table）和跳板栈（Trampoline Stack）也会明显增加内存占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USERSPACE && !CONFIG_X86_NO_MELTDOWN && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/Kconfig:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L466)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86_NO_MELTDOWN`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_MELTDOWN)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_MAX_ADDITIONAL_MEM_DOMAINS"></a>

## 39.46 `CONFIG_X86_MAX_ADDITIONAL_MEM_DOMAINS`

**提示（Prompt）**：最大内存域数量（Maximum Number of Memory Domains）

**说明（Help）**

启动时的初始页表（Page Table）会预分配，并用于默认内存域（Memory Domain）。在使用共用页表（Common Page Tables）时，实例化额外内存域需要一个空闲的固定驻留内存页（Pinned Memory Page）池，以构建页表。Zephyr 测试用例假设可以额外实例化 3 个内存域。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_MMU && CONFIG_USERSPACE && !CONFIG_X86_COMMON_PAGE_TABLE && CONFIG_X86
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`arch/x86/Kconfig:350`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L350)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_X86_COMMON_PAGE_TABLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_COMMON_PAGE_TABLE)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_MEMMAP"></a>

## 39.47 `CONFIG_X86_MEMMAP`

**提示（Prompt）**：使用内存映射（Memory Map）

**说明（Help）**

启用内存映射（Memory Map）以识别内存区域。内存映射可通过 Multiboot 填充，即设置 `CONFIG_MULTIBOOT=y` 和 `CONFIG_MULTIBOOT_MEMMAP=y`；也可以通过 `x86_memmap[]` 手动定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES
```

**被选择（Selected by）**

```text
CONFIG_MULTIBOOT_MEMMAP
```

**定义位置（Location）**：[`arch/x86/Kconfig:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L268)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES)、[`CONFIG_MULTIBOOT_MEMMAP`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT_MEMMAP)。

<a id="CONFIG_X86_MEMMAP_ENTRIES"></a>

## 39.48 `CONFIG_X86_MEMMAP_ENTRIES`

**提示（Prompt）**：内存映射条目数量（Number of Memory Map Entries）

**说明（Help）**

内存映射（Memory Map）能够容纳的最大内存区域数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_MEMMAP && CONFIG_X86
```

**默认值（Defaults）**

```text
1 if !CONFIG_MULTIBOOT_MEMMAP
64 if CONFIG_MULTIBOOT_MEMMAP
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`arch/x86/Kconfig:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L278)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 使用内存映射（Memory Map）

**配置项引用（Symbol References）**：[`CONFIG_X86_MEMMAP`](P039_arch_x86_配置项参考.md#CONFIG_X86_MEMMAP)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_MULTIBOOT_MEMMAP`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT_MEMMAP)。

<a id="CONFIG_X86_MFENCE_INSTRUCTION_SUPPORTED"></a>

## 39.49 `CONFIG_X86_MFENCE_INSTRUCTION_SUPPORTED`

**提示（Prompt）**：支持 x86 MFENCE 指令（MFENCE Instruction）

**说明（Help）**

对于具有 `CLFLUSH` 指令但没有 `MFENCE` 的 x86 CPU，设置为 `n`，禁用 `arch_dcache_flush()` 对 `MFENCE` 指令的使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L170)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_MMU"></a>

## 39.50 `CONFIG_X86_MMU`

**提示（Prompt）**：内存管理单元（Memory Management Unit，MMU）

**说明（Help）**

启用 x86 的内存管理单元（MMU），并在启动时创建一组运行时可修改的页表（Page Table）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_MMU
```

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_LAKEMONT
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
CONFIG_CPU_APOLLO_LAKE
CONFIG_X86_64
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_ATOM
```

**定义位置（Location）**：[`arch/x86/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)、[`CONFIG_CPU_APOLLO_LAKE`](P039_arch_x86_配置项参考.md#CONFIG_CPU_APOLLO_LAKE)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_SOC_ATOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_LAKEMONT`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`、`CONFIG_SOC_ATOM`。

<a id="CONFIG_X86_MMX"></a>

## 39.51 `CONFIG_X86_MMX`

**提示（Prompt）**：MMX 支持（MMX Support）

**说明（Help）**

启用 MMX 支持，并允许线程使用 MMX 寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_MMX && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_64
```

**定义位置（Location）**：[`arch/x86/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_MMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_MMX)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_MMX`。

<a id="CONFIG_X86_NO_LAZY_FP"></a>

## 39.52 `CONFIG_X86_NO_LAZY_FP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不受 CVE-2018-3665 所述 Lazy FP CPU 漏洞影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES
```

**定义位置（Location）**：[`arch/x86/Kconfig:407`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L407)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES)。

<a id="CONFIG_X86_NO_MELTDOWN"></a>

## 39.53 `CONFIG_X86_NO_MELTDOWN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不受 CVE-2017-5754 所述 Meltdown CPU 漏洞影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES
```

**定义位置（Location）**：[`arch/x86/Kconfig:378`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L378)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES)。

<a id="CONFIG_X86_NO_SPECTRE_V1"></a>

## 39.54 `CONFIG_X86_NO_SPECTRE_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不受 CVE-2017-5753、CVE-2018-3693 和 CVE-2019-1125 所述 Spectre V1、V1.1、V1.2 及 `swapgs` CPU 漏洞影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES
```

**定义位置（Location）**：[`arch/x86/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES)。

<a id="CONFIG_X86_NO_SPECTRE_V2"></a>

## 39.55 `CONFIG_X86_NO_SPECTRE_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不受 CVE-2017-5715 所述 Spectre V2 CPU 漏洞影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES
```

**定义位置（Location）**：[`arch/x86/Kconfig:393`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L393)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES)。

<a id="CONFIG_X86_NO_SPECTRE_V4"></a>

## 39.56 `CONFIG_X86_NO_SPECTRE_V4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不受 CVE-2018-3639 所述 Spectre V4 CPU 漏洞影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES
```

**定义位置（Location）**：[`arch/x86/Kconfig:400`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L400)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES)。

<a id="CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES"></a>

## 39.57 `CONFIG_X86_NO_SPECULATIVE_VULNERABILITIES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项应按片上系统（SoC）分别设置，表示该 SoC 不执行任何形式的推测执行（Speculative Execution），或属于对利用推测执行侧信道攻击（Side Channel Attack）这一类漏洞免疫的较新芯片。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_NO_MELTDOWN
CONFIG_X86_NO_SPECTRE_V1
CONFIG_X86_NO_SPECTRE_V2
CONFIG_X86_NO_SPECTRE_V4
CONFIG_X86_NO_LAZY_FP
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
```

**定义位置（Location）**：[`arch/x86/Kconfig:414`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L414)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_NO_MELTDOWN`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_MELTDOWN)、[`CONFIG_X86_NO_SPECTRE_V1`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V1)、[`CONFIG_X86_NO_SPECTRE_V2`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V2)、[`CONFIG_X86_NO_SPECTRE_V4`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_SPECTRE_V4)、[`CONFIG_X86_NO_LAZY_FP`](P039_arch_x86_配置项参考.md#CONFIG_X86_NO_LAZY_FP)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ISH`。

<a id="CONFIG_X86_PAE"></a>

## 39.58 `CONFIG_X86_PAE`

**提示（Prompt）**：使用 PAE 页表（PAE Page Tables）

**说明（Help）**

启用后，使用物理地址扩展（PAE）样式的页表，而不是 32 位页表。优点是支持执行禁用位（Execute Disable Bit），代价是分页结构（Paging Structure）需要更多内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_MMU && !CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L88)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_X86_MMU`](P039_arch_x86_配置项参考.md#CONFIG_X86_MMU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_PC_COMPATIBLE"></a>

## 39.59 `CONFIG_X86_PC_COMPATIBLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示为具有基本输入输出系统（BIOS）、高级配置与电源接口（ACPI）等功能的 PC 兼容平台构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES
CONFIG_HAS_SRAM_OFFSET
```

**定义位置（Location）**：[`arch/x86/Kconfig:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L259)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_RESERVED_PAGE_FRAMES)、[`CONFIG_HAS_SRAM_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_SRAM_OFFSET)。

<a id="CONFIG_X86_RUNTIME_IRQ_STATS"></a>

## 39.60 `CONFIG_X86_RUNTIME_IRQ_STATS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

添加中断请求（IRQ）运行时统计，以便使用主机工具（Host Tools）在运行时分析 IRQ 性能数据。启用此选项，并实现平台相关的 `runtime_irq_stats()` API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L178)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_SSE"></a>

## 39.61 `CONFIG_X86_SSE`

**提示（Prompt）**：SSE 支持（SSE Support）

**说明（Help）**

启用流式 SIMD 扩展（SSE）支持，并允许线程使用 SSE 寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_SOC_LAKEMONT
CONFIG_X86_64
CONFIG_X86_SSE2
CONFIG_X86_SSE3
CONFIG_X86_SSSE3
CONFIG_X86_SSE41
CONFIG_X86_SSE42
CONFIG_X86_SSE4A
```

**定义位置（Location）**：[`arch/x86/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)、[`CONFIG_X86_SSE2`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE2)、[`CONFIG_X86_SSE3`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE3)、[`CONFIG_X86_SSSE3`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSSE3)、[`CONFIG_X86_SSE41`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE41)、[`CONFIG_X86_SSE42`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE42)、[`CONFIG_X86_SSE4A`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE4A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE`、`CONFIG_SOC_LAKEMONT`。

<a id="CONFIG_X86_SSE2"></a>

## 39.62 `CONFIG_X86_SSE2`

**提示（Prompt）**：SSE2 支持（SSE2 Support）

**说明（Help）**

启用 SSE2 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE2 && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**被选择（Selected by）**

```text
CONFIG_SOC_LAKEMONT
CONFIG_X86_64
```

**定义位置（Location）**：[`arch/x86/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE2)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE2`、`CONFIG_SOC_LAKEMONT`。

<a id="CONFIG_X86_SSE3"></a>

## 39.63 `CONFIG_X86_SSE3`

**提示（Prompt）**：SSE3 支持（SSE3 Support）

**说明（Help）**

启用 SSE3 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE3 && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**被选择（Selected by）**

```text
CONFIG_SOC_LAKEMONT
```

**定义位置（Location）**：[`arch/x86/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE3)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE3`、`CONFIG_SOC_LAKEMONT`。

<a id="CONFIG_X86_SSE41"></a>

## 39.64 `CONFIG_X86_SSE41`

**提示（Prompt）**：SSE4.1 支持（SSE4.1 Support）

**说明（Help）**

启用 SSE4.1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE41 && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**定义位置（Location）**：[`arch/x86/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE41`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE41)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE41`。

<a id="CONFIG_X86_SSE42"></a>

## 39.65 `CONFIG_X86_SSE42`

**提示（Prompt）**：SSE4.2 支持（SSE4.2 Support）

**说明（Help）**

启用 SSE4.2 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE42 && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**定义位置（Location）**：[`arch/x86/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE42`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE42)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE42`。

<a id="CONFIG_X86_SSE4A"></a>

## 39.66 `CONFIG_X86_SSE4A`

**提示（Prompt）**：SSE4A 支持（SSE4A Support）

**说明（Help）**

启用 SSE4A 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSE4A && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**定义位置（Location）**：[`arch/x86/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSE4A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSE4A)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSE4A`。

<a id="CONFIG_X86_SSE_FP_MATH"></a>

## 39.67 `CONFIG_X86_SSE_FP_MATH`

**提示（Prompt）**：编译器生成用于浮点运算的 SSEx 指令（Floating Point Math）

**说明（Help）**

允许编译器生成 SSEx 指令执行浮点运算（Floating Point Math）。当需要对多个数据对象执行完全相同的操作时，这可以显著提高性能；但发生抢占式任务切换（Preemptive Task Switch）时，由于必须保存和恢复更大的寄存器组，也可能显著降低性能。禁用后，编译器只使用 x87 指令集执行浮点运算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_SSE && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**定义位置（Location）**：[`arch/x86/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_X86_SSSE3"></a>

## 39.68 `CONFIG_X86_SSSE3`

**提示（Prompt）**：补充 SSE3 支持（Supplemental SSE3，SSSE3）

**说明（Help）**

启用补充 SSE3（Supplemental SSE3）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_CPU_HAS_SSSE3 && (CONFIG_FPU || CONFIG_X86_64) && CONFIG_X86
```

**主动选择（Selects）**

```text
CONFIG_X86_SSE
```

**被选择（Selected by）**

```text
CONFIG_SOC_LAKEMONT
```

**定义位置（Location）**：[`arch/x86/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → x86 特性（x86 Features）

**配置项引用（Symbol References）**：[`CONFIG_X86_CPU_HAS_SSSE3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CPU_HAS_SSSE3)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_SSE`](P039_arch_x86_配置项参考.md#CONFIG_X86_SSE)、[`CONFIG_SOC_LAKEMONT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LAKEMONT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_X86_CPU_HAS_SSSE3`、`CONFIG_SOC_LAKEMONT`。

<a id="CONFIG_X86_STACK_PROTECTION"></a>

## 39.69 `CONFIG_X86_STACK_PROTECTION`

原库同名定义共 2 条；本项为数据库第 21523 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

利用内存管理单元（MMU），在当前进程栈超出边界时触发系统致命错误（Fatal Error）。实现方式是在所有栈区域之前放置一个 4K 保护页（Guard Page）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_SET_GDT
CONFIG_GDT_DYNAMIC
CONFIG_X86_ENABLE_TSS
```

**弱选择（Implies）**

```text
CONFIG_THREAD_STACK_MEM_MAPPED if !CONFIG_DEMAND_PAGING
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L63)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_SET_GDT`](P039_arch_x86_配置项参考.md#CONFIG_SET_GDT)、[`CONFIG_GDT_DYNAMIC`](P039_arch_x86_配置项参考.md#CONFIG_GDT_DYNAMIC)、[`CONFIG_X86_ENABLE_TSS`](P039_arch_x86_配置项参考.md#CONFIG_X86_ENABLE_TSS)、[`CONFIG_THREAD_STACK_MEM_MAPPED`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_MEM_MAPPED)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)。

<a id="CONFIG_X86_STACK_PROTECTION--record-21524"></a>

## 39.70 `CONFIG_X86_STACK_PROTECTION`

原库同名定义共 2 条；本项为数据库第 21524 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

利用内存管理单元（MMU），在当前进程栈超出边界时触发系统致命错误（Fatal Error）。实现方式是在所有栈区域之前放置一个 4K 保护页（Guard Page）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**弱选择（Implies）**

```text
CONFIG_THREAD_STACK_MEM_MAPPED
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L74)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_STACK_MEM_MAPPED`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_MEM_MAPPED)。

<a id="CONFIG_X86_USERSPACE"></a>

## 39.71 `CONFIG_X86_USERSPACE`

原库同名定义共 2 条；本项为数据库第 21525 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用将线程权限降至保护环 3（Ring 3）的 API，支持用户级线程（User-Level Thread）；这些线程彼此隔离，并受到限制，不能使内核崩溃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_USERSPACE
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_SET_GDT
CONFIG_GDT_DYNAMIC
CONFIG_X86_ENABLE_TSS
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L76)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options） → 处理器能力（Processor Capabilities）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_SET_GDT`](P039_arch_x86_配置项参考.md#CONFIG_SET_GDT)、[`CONFIG_GDT_DYNAMIC`](P039_arch_x86_配置项参考.md#CONFIG_GDT_DYNAMIC)、[`CONFIG_X86_ENABLE_TSS`](P039_arch_x86_配置项参考.md#CONFIG_X86_ENABLE_TSS)。

<a id="CONFIG_X86_USERSPACE--record-21526"></a>

## 39.72 `CONFIG_X86_USERSPACE`

原库同名定义共 2 条；本项为数据库第 21526 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用将线程权限降至保护环 3（Ring 3）的 API，支持用户级线程（User-Level Thread）；这些线程彼此隔离，并受到限制，不能使内核崩溃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_USERSPACE
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.intel64:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.intel64#L84)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_X86_USE_THREAD_LOCAL_STORAGE"></a>

## 39.73 `CONFIG_X86_USE_THREAD_LOCAL_STORAGE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于启用线程局部存储（Thread Local Storage，TLS）的内部配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X86_64 && CONFIG_X86
```

**默认值（Defaults）**

```text
y if CONFIG_THREAD_LOCAL_STORAGE
```

**主动选择（Selects）**

```text
CONFIG_SET_GDT
CONFIG_GDT_DYNAMIC
```

**定义位置（Location）**：[`arch/x86/core/Kconfig.ia32:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/Kconfig.ia32#L162)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)、[`CONFIG_SET_GDT`](P039_arch_x86_配置项参考.md#CONFIG_SET_GDT)、[`CONFIG_GDT_DYNAMIC`](P039_arch_x86_配置项参考.md#CONFIG_GDT_DYNAMIC)。

<a id="CONFIG_X86_VERY_EARLY_CONSOLE"></a>

## 39.74 `CONFIG_X86_VERY_EARLY_CONSOLE`

**提示（Prompt）**：支持启动极早期的 printk（Very Early Boot printk）

**说明（Help）**

非仿真的 x86 设备通常需要专用硬件才能连接调试器（Debugger），这类硬件可能不容易获得。此选项添加一个极简串口驱动（Serial Driver），在 `z_cstart()` 最开始通过 `arch_kernel_init()` 初始化。该驱动使 `printk` 可以向设备树（Devicetree）中的 16550 UART 端口 0 实例输出消息。此微型驱动假设通过端口（Port）对 UART 执行 I/O。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`arch/x86/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → x86 架构选项（Architecture Options）

<!-- kconfig-navigation -->

[上一章](P038_arch_tricore_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P040_arch_xtensa_配置项参考.md)
