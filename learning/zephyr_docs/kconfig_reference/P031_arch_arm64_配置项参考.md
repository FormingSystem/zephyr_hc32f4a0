---
id: learning.zephyr-docs.kconfig-reference.page-31
title: "`arch/arm64`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第31章\_`arch/arm64`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/arm64` 的 62 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AARCH64_IMAGE_HEADER"></a>

## 31.1 `CONFIG_AARCH64_IMAGE_HEADER`

**提示（Prompt）**：添加镜像头部（Image Header）

**说明（Help）**

此选项启用 Linux 使用、并可被 U-Boot 或 Xen `xl` 工具等加载器识别的标准 ARM64 启动镜像头部（Boot Image Header）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**默认值（Defaults）**

```text
y if CONFIG_ARM_MMU || CONFIG_ARM_MPU
```

**被选择（Selected by）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

<a id="CONFIG_ARCH_HAS_STACKWALK"></a>

## 31.2 `CONFIG_ARCH_HAS_STACKWALK`

原库同名定义共 5 条；本项为数据库第 500 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，表示已实现 `arch_stack_walk()` API，且可以启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FRAME_POINTER && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L224)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_FRAME_POINTER`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FRAME_POINTER)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_ARM64_BOOT_DISABLE_DCACHE"></a>

## 31.3 `CONFIG_ARM64_BOOT_DISABLE_DCACHE`

**提示（Prompt）**：从 EL2 启动时，在启用 MMU 之前禁用数据缓存（Data Cache）

**说明（Help）**

为保证安全，如果 Zephyr 从 EL2 启动时数据缓存（Data Cache）已启用，可启用此选项：它先清理并失效全部数据缓存，再禁用数据缓存，待内存管理单元（MMU）配置并启用后重新启用缓存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_DCACHE_ALL_OPS && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L460)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 提供操作全部数据缓存的 API（Data Cache APIs）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_DCACHE_ALL_OPS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_DCACHE_ALL_OPS)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_DCACHE_ALL_OPS"></a>

## 31.4 `CONFIG_ARM64_DCACHE_ALL_OPS`

**提示（Prompt）**：提供操作全部数据缓存的 API（Data Cache APIs）

**说明（Help）**

启用此选项，以提供刷新（Flush）或失效（Invalidate）全部数据缓存的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L453)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_FALLBACK_ON_RESERVED_CORES"></a>

## 31.5 `CONFIG_ARM64_FALLBACK_ON_RESERVED_CORES`

**提示（Prompt）**：启用向保留内核回退（Fallback on Reserved Cores）

**说明（Help）**

允许在设备树（Devicetree）中定义比 `CONFIG_MP_MAX_NUM_CPUS` 要求更多的内核，额外内核成为保留内核（Reserved Core）。如果启动时某个内核上电失败，则跳过它，使用设备树中的下一个内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_MMU_REPORT_XLAT_TABLES_USAGE"></a>

## 31.6 `CONFIG_ARM64_MMU_REPORT_XLAT_TABLES_USAGE`

**提示（Prompt）**：跟踪转换表分配（Translation Table Allocations）

**说明（Help）**

每当已分配转换表（Translation Table）数量达到新的高水位（High-water Mark）时记录消息，便于调整 `CONFIG_MAX_XLAT_TABLES`。在具有代表性的运行过程中，最后看到的 `peak N of M allocated` 日志行给出 MAX 的下限，低于该值会在此工作负载下出现“过小（too small）”的致命错误。另有独立保护机制：当池中空闲比例第一次低于 12.5% 时，始终发出一次 `LOG_WRN`，无需 Kconfig 配置，以便在耗尽前预警。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ARM_MMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L437)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_PAGE_SIZE"></a>

## 31.7 `CONFIG_ARM64_PAGE_SIZE`

**提示（Prompt）**：页面大小（Page Size）

**说明（Help）**

允许从三种页面大小（Page Size）中选择。转换表（Translation Table）的级数由页面大小与虚拟地址空间大小共同决定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
CONFIG_ARM64_PAGE_SIZE_4KB
```

**可选项（Choices）**

```text
CONFIG_ARM64_PAGE_SIZE_4KB
CONFIG_ARM64_PAGE_SIZE_16KB
CONFIG_ARM64_PAGE_SIZE_64KB
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L332)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM64_PAGE_SIZE_4KB`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE_4KB)、[`CONFIG_ARM64_PAGE_SIZE_16KB`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE_16KB)、[`CONFIG_ARM64_PAGE_SIZE_64KB`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE_64KB)。

<a id="CONFIG_ARM64_PAGE_SIZE_16KB"></a>

## 31.8 `CONFIG_ARM64_PAGE_SIZE_16KB`

**提示（Prompt）**：16 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PAGE_SIZE>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L343)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 页面大小（Page Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PAGE_SIZE`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE)。

<a id="CONFIG_ARM64_PAGE_SIZE_4KB"></a>

## 31.9 `CONFIG_ARM64_PAGE_SIZE_4KB`

**提示（Prompt）**：4 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PAGE_SIZE>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:340`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L340)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 页面大小（Page Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PAGE_SIZE`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE)。

<a id="CONFIG_ARM64_PAGE_SIZE_64KB"></a>

## 31.10 `CONFIG_ARM64_PAGE_SIZE_64KB`

**提示（Prompt）**：64 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PAGE_SIZE>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L346)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 页面大小（Page Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PAGE_SIZE`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PAGE_SIZE)。

<a id="CONFIG_ARM64_PA_BITS"></a>

## 31.11 `CONFIG_ARM64_PA_BITS`

**提示（Prompt）**：物理地址空间大小（Physical Address Space Size）

**说明（Help）**

选择内核支持的最大物理地址范围（Physical Address Range）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
CONFIG_ARM64_PA_BITS_32
```

**可选项（Choices）**

```text
CONFIG_ARM64_PA_BITS_32
CONFIG_ARM64_PA_BITS_36
CONFIG_ARM64_PA_BITS_40
CONFIG_ARM64_PA_BITS_42
CONFIG_ARM64_PA_BITS_48
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L387)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM64_PA_BITS_32`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS_32)、[`CONFIG_ARM64_PA_BITS_36`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS_36)、[`CONFIG_ARM64_PA_BITS_40`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS_40)、[`CONFIG_ARM64_PA_BITS_42`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS_42)、[`CONFIG_ARM64_PA_BITS_48`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS_48)。

<a id="CONFIG_ARM64_PA_BITS_32"></a>

## 31.12 `CONFIG_ARM64_PA_BITS_32`

**提示（Prompt）**：32 位（32-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:394`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L394)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 物理地址空间大小（Physical Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS)。

<a id="CONFIG_ARM64_PA_BITS_36"></a>

## 31.13 `CONFIG_ARM64_PA_BITS_36`

**提示（Prompt）**：36 位（36-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 物理地址空间大小（Physical Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS)。

<a id="CONFIG_ARM64_PA_BITS_40"></a>

## 31.14 `CONFIG_ARM64_PA_BITS_40`

**提示（Prompt）**：40 位（40-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:400`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L400)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 物理地址空间大小（Physical Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS)。

<a id="CONFIG_ARM64_PA_BITS_42"></a>

## 31.15 `CONFIG_ARM64_PA_BITS_42`

**提示（Prompt）**：42 位（42-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:403`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L403)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 物理地址空间大小（Physical Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS)。

<a id="CONFIG_ARM64_PA_BITS_48"></a>

## 31.16 `CONFIG_ARM64_PA_BITS_48`

**提示（Prompt）**：48 位（48-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L406)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 物理地址空间大小（Physical Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PA_BITS)。

<a id="CONFIG_ARM64_PMUV3"></a>

## 31.17 `CONFIG_ARM64_PMUV3`

**提示（Prompt）**：ARMv8-A PMUv3 支持

**说明（Help）**

启用 ARM 性能监测单元（Performance Monitoring Unit，PMU）支持。PMU 提供硬件性能计数器（Hardware Performance Counter），监测缓存未命中（Cache Miss）、分支预测错误（Branch Misprediction）、内存访问及周期计数等 CPU 行为。此驱动支持 ARMv8-A PMUv3，原文称兼容所有 Cortex-A 处理器，包括 A53、A55、A57、A72、A73、A75、A76、A77、A78、A510、A710、X1、X2 等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64 && CONFIG_ARCH_HAS_PMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig.pmu:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig.pmu#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARCH_HAS_PMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_PMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)。

<a id="CONFIG_ARM64_PMUV3_USER_ACCESS"></a>

## 31.18 `CONFIG_ARM64_PMUV3_USER_ACCESS`

**提示（Prompt）**：用户模式访问 PMU 计数器（User-mode Access to PMU Counters）

**说明（Help）**

允许非特权，即用户模式（User Mode）应用访问 PMU 计数器（Counter），便于基准测试，但可能带来安全影响。警告：启用后，任意用户空间代码都可读取性能计数器，可能泄露敏感的时序信息（Timing Information）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_PMUV3 && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig.pmu:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig.pmu#L21)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PMUV3)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_RNG"></a>

## 31.19 `CONFIG_ARM64_RNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示处理器具有 `FEAT_RNG` 或 `FEAT_RNG_TRAP` 扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:492`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L492)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_SAFE_EXCEPTION_STACK"></a>

## 31.20 `CONFIG_ARM64_SAFE_EXCEPTION_STACK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

安全异常栈（Safe Exception Stack）用于在异常从 EL1 发生时检查内核栈是否溢出。它不用于检查用户栈溢出，因为该检查可以由内核栈承载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**被选择（Selected by）**

```text
CONFIG_ARM64_STACK_PROTECTION
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM64_STACK_PROTECTION`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_STACK_PROTECTION)。

<a id="CONFIG_ARM64_SAFE_EXCEPTION_STACK_SIZE"></a>

## 31.21 `CONFIG_ARM64_SAFE_EXCEPTION_STACK_SIZE`

**提示（Prompt）**：安全异常栈大小（Safe Exception Stack Size）

**说明（Help）**

安全异常栈（Safe Exception Stack）的栈大小，必须足够执行栈溢出检查（Stack Overflow Check）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_SAFE_EXCEPTION_STACK && CONFIG_ARM64
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_SAFE_EXCEPTION_STACK`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_SAFE_EXCEPTION_STACK)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_SET_VMPIDR_EL2"></a>

## 31.22 `CONFIG_ARM64_SET_VMPIDR_EL2`

**提示（Prompt）**：在 EL2 阶段设置 `VMPIDR_EL2`

**说明（Help）**

`VMPIDR_EL2` 保存虚拟化多处理器 ID（Virtualization Multiprocessor ID），这是 EL1 读取 `MPIDR_EL1` 时返回的值。引导加载程序可能已在 EL2 阶段设置此寄存器；若未设置，应由 Zephyr 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L322)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_STACK_PROTECTION"></a>

## 31.23 `CONFIG_ARM64_STACK_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项利用内存管理单元（MMU）或内存保护单元（MPU），在当前进程栈超出边界时触发系统致命错误（System Fatal Error）。实现方式是在所有栈区域之前设置固定的保护区域（Guard Region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_ARM64
```

**默认值（Defaults）**

```text
y if CONFIG_HW_STACK_PROTECTION
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_ARM64_SAFE_EXCEPTION_STACK
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_HW_STACK_PROTECTION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_HW_STACK_PROTECTION)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_ARM64_SAFE_EXCEPTION_STACK`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_SAFE_EXCEPTION_STACK)。

<a id="CONFIG_ARM64_SVE"></a>

## 31.24 `CONFIG_ARM64_SVE`

**提示（Prompt）**：可伸缩向量扩展（Scalable Vector Extension，SVE）支持

**说明（Help）**

启用 ARM64 可伸缩向量扩展（Scalable Vector Extension，SVE）支持，允许线程使用 SVE/SVE2 指令。如果同时设置 `CONFIG_FPU_SHARING`，还会自动处理 SVE 寄存器 `Z0-Z31`、`P0-P15`、`FFR` 的上下文切换。要求 ARMv9-A 架构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV9_A && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**被弱选择（Implied by）**

```text
CONFIG_ARMV9_A
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:469`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L469)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_SVE_VL_MAX"></a>

## 31.25 `CONFIG_ARM64_SVE_VL_MAX`

**提示（Prompt）**：最大 SVE 向量长度（Maximum Vector Length，字节）

**说明（Help）**

支持的最大 SVE 向量长度（Vector Length），以字节为单位，决定每个线程结构中 SVE 上下文（Context）的大小。有效值为 16 到 256 之间的任意 2 的幂，包含端点，即 128～2048 位。可设为小于硬件支持的向量长度，以节省各线程内存，此时硬件将限制为指定长度。设为大于硬件支持的值只会浪费内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_SVE && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:478`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L478)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 可伸缩向量扩展（Scalable Vector Extension，SVE）支持

**配置项引用（Symbol References）**：[`CONFIG_ARM64_SVE`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_SVE)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM64_VA_BITS"></a>

## 31.26 `CONFIG_ARM64_VA_BITS`

**提示（Prompt）**：虚拟地址空间大小（Virtual Address Space Size）

**说明（Help）**

允许从多种虚拟地址空间大小（Virtual Address Space Size）中选择。转换表（Translation Table）的级数由页面大小与虚拟地址空间大小共同决定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
CONFIG_ARM64_VA_BITS_32
```

**可选项（Choices）**

```text
CONFIG_ARM64_VA_BITS_32
CONFIG_ARM64_VA_BITS_36
CONFIG_ARM64_VA_BITS_40
CONFIG_ARM64_VA_BITS_42
CONFIG_ARM64_VA_BITS_48
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM64_VA_BITS_32`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS_32)、[`CONFIG_ARM64_VA_BITS_36`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS_36)、[`CONFIG_ARM64_VA_BITS_40`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS_40)、[`CONFIG_ARM64_VA_BITS_42`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS_42)、[`CONFIG_ARM64_VA_BITS_48`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS_48)。

<a id="CONFIG_ARM64_VA_BITS_32"></a>

## 31.27 `CONFIG_ARM64_VA_BITS_32`

**提示（Prompt）**：32 位（32-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_VA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:363`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L363)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 虚拟地址空间大小（Virtual Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_ARM64_VA_BITS_36"></a>

## 31.28 `CONFIG_ARM64_VA_BITS_36`

**提示（Prompt）**：36 位（36-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_VA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L366)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 虚拟地址空间大小（Virtual Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_ARM64_VA_BITS_40"></a>

## 31.29 `CONFIG_ARM64_VA_BITS_40`

**提示（Prompt）**：40 位（40-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_VA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L369)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 虚拟地址空间大小（Virtual Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_ARM64_VA_BITS_42"></a>

## 31.30 `CONFIG_ARM64_VA_BITS_42`

**提示（Prompt）**：42 位（42-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_VA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L372)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 虚拟地址空间大小（Virtual Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_ARM64_VA_BITS_48"></a>

## 31.31 `CONFIG_ARM64_VA_BITS_48`

**提示（Prompt）**：48 位（48-bit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_VA_BITS>
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:375`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L375)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → 虚拟地址空间大小（Virtual Address Space Size）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_ARMV8_A"></a>

## 31.32 `CONFIG_ARMV8_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv8-A 处理器实现。根据 [Arm A-profile 架构说明](https://developer.arm.com/products/architecture/cpu-architecture/a-profile)，Armv8-A 引入 64 位和 32 位执行状态（Execution State），分别称为 AArch64 和 AArch32。AArch64 支持 A64 指令集，用 64 位寄存器保存地址，并允许基本指令集的指令使用 64 位寄存器处理数据。AArch32 是保留与 Armv7-A 向后兼容性的 32 位执行状态，并扩展该体系以支持部分 AArch64 功能，支持 T32 和 A32 指令集。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_CPU_HAS_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARM_MMU
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT if CONFIG_ARM_MMU
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_VIRT_ARM64
CONFIG_CPU_CORTEX_A53
CONFIG_CPU_CORTEX_A55
CONFIG_CPU_CORTEX_A57
CONFIG_CPU_CORTEX_A72
CONFIG_CPU_CORTEX_A76
CONFIG_CPU_CORTEX_A76_A55
CONFIG_CPU_CORTEX_A78
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_SOC_QEMU_VIRT_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_ARM64)、[`CONFIG_CPU_CORTEX_A53`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A53)、[`CONFIG_CPU_CORTEX_A55`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A55)、[`CONFIG_CPU_CORTEX_A57`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A57)、[`CONFIG_CPU_CORTEX_A72`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A72)、[`CONFIG_CPU_CORTEX_A76`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A76)、[`CONFIG_CPU_CORTEX_A76_A55`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A76_A55)、[`CONFIG_CPU_CORTEX_A78`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A78)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`、`CONFIG_SOC_QEMU_VIRT_ARM64`。

<a id="CONFIG_ARMV8_A_NS"></a>

## 31.33 `CONFIG_ARMV8_A_NS`

**提示（Prompt）**：ARMv8-A 普通世界（Normal World，即 TrustZone 非安全世界）

**说明（Help）**

此选项表示进入 Zephyr 时处于 TrustZone 非安全状态（Non-Secure State）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**被选择（Selected by）**

```text
CONFIG_GIC_V3_ITS
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_GIC_V3_ITS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3_ITS)。

<a id="CONFIG_ARMV8_R"></a>

## 31.34 `CONFIG_ARMV8_R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv8-R 处理器实现。根据 [Arm R-profile 架构说明](https://developer.arm.com/products/architecture/cpu-architecture/r-profile)，Armv8-R 面向实时处理器体系（Real-time Profile），在最高安全级别引入虚拟化（Virtualization），同时保留基于内存保护单元（MPU）的受保护内存系统架构（Protected Memory System Architecture，PMSA），支持 A32 和 T32 指令集。

译注：此 ARM 外部引用未取得可核验的正文，访问结果为受限响应、空的应用外壳或其他支持入口。保留官方 Kconfig 原始地址，不将外部正文记为已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_AARCH64_CORTEX_R && CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARM_MPU
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R82
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_CPU_CORTEX_R82`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_R82)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`。

<a id="CONFIG_ARMV9_A"></a>

## 31.35 `CONFIG_ARMV9_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 ARMv9-A 处理器实现。ARMv9-A 建立在 ARMv8-A 基础上，增加安全、性能和机器学习（Machine Learning）能力，同时保持与 ARMv8-A 软件向后兼容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_ATOMIC_OPERATIONS_BUILTIN
CONFIG_CPU_HAS_MMU
CONFIG_ARCH_HAS_USERSPACE if CONFIG_ARM_MMU
CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT if CONFIG_ARM_MMU
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_A510
CONFIG_CPU_CORTEX_A320
CONFIG_CPU_CORTEX_A720
```

**弱选择（Implies）**

```text
CONFIG_ARM64_SVE if CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ATOMIC_OPERATIONS_BUILTIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ATOMIC_OPERATIONS_BUILTIN)、[`CONFIG_CPU_HAS_MMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MMU)、[`CONFIG_ARCH_HAS_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_USERSPACE)、[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_CPU_CORTEX_A510`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A510)、[`CONFIG_CPU_CORTEX_A320`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A320)、[`CONFIG_CPU_CORTEX_A720`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A720)、[`CONFIG_ARM64_SVE`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_SVE)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_USERSPACE`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER"></a>

## 31.36 `CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`

原库同名定义共 2 条；本项为数据库第 658 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示 ARM CPU 连接到自定义中断控制器（Custom Interrupt Controller），即不是 GIC。部分 Cortex-A 和 Cortex-R 内核，例如 Cortex-A5、Cortex-R4/5 等，允许连接自定义外部中断控制器；若连接的不是 ARM 通用中断控制器（Generic Interrupt Controller，GIC），就必须选择此项。选择后，架构中断控制函数映射到由 SoC 层实现的中断控制接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
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

**定义位置（Location）**：[`arch/arm64/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_BCM2710`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2710)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BCM2710`。

<a id="CONFIG_ARM_MMU"></a>

## 31.37 `CONFIG_ARM_MMU`

**提示（Prompt）**：ARM 内存管理单元（MMU）支持

**说明（Help）**

内存管理单元（Memory Management Unit）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
n if CONFIG_CPU_AARCH64_CORTEX_R
y
```

**主动选择（Selects）**

```text
CONFIG_MMU
CONFIG_SRAM_REGION_PERMISSIONS
CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API if CONFIG_USERSPACE
CONFIG_ARCH_MEM_DOMAIN_DATA if CONFIG_USERSPACE
CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT if CONFIG_USERSPACE
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_SRAM_REGION_PERMISSIONS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_REGION_PERMISSIONS)、[`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_ARCH_MEM_DOMAIN_DATA`](P001_kernel_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_DATA)、[`CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_MEM_DOMAIN_SUPPORTS_DEINIT)。

<a id="CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE"></a>

## 31.38 `CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE`

原库同名定义共 2 条；本项为数据库第 670 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM MPU 区域的最小大小及对齐（Minimum Size and Alignment）。使用此符号保证 MPU 区域满足最小大小和对齐要求。没有内存保护支持的 ARM 构建也强制采用至少 4 字节对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_MPU && CONFIG_CPU_AARCH64_CORTEX_R && CONFIG_ARM64
```

**默认值（Defaults）**

```text
64 if CONFIG_ARM_MPU
4
```

**定义位置（Location）**：[`arch/arm64/core/cortex_r/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/cortex_r/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_CPU_AARCH64_CORTEX_R"></a>

## 31.39 `CONFIG_CPU_AARCH64_CORTEX_R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R 64 位系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_ARCH_HAS_STACK_PROTECTION
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_R82
```

**弱选择（Implies）**

```text
CONFIG_FPU
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_ARCH_HAS_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_PROTECTION)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_CORTEX_R82`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_R82)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_PROTECTION`。

<a id="CONFIG_CPU_CORTEX"></a>

## 31.40 `CONFIG_CPU_CORTEX`

原库同名定义共 2 条；本项为数据库第 4310 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
```

**定义位置（Location）**：[`arch/arm64/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_CPU_AARCH32_CORTEX_R`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)。

<a id="CONFIG_CPU_CORTEX_A"></a>

## 31.41 `CONFIG_CPU_CORTEX_A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A 系列 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX
CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL if CONFIG_SMP && !CONFIG_PM
CONFIG_HAS_FLASH_LOAD_OFFSET
CONFIG_KERNEL_DIRECT_MAP if CONFIG_MMU
CONFIG_SCHED_IPI_SUPPORTED if CONFIG_SMP
CONFIG_CPU_HAS_FPU
CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT if !CONFIG_SMP
CONFIG_CPU_HAS_DCACHE
CONFIG_CPU_HAS_ICACHE
CONFIG_ARCH_HAS_PMU
CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS
CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR if !CONFIG_SMP
CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE if CONFIG_SMP
```

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_VIRT_ARM64
CONFIG_CPU_CORTEX_A53
CONFIG_CPU_CORTEX_A55
CONFIG_CPU_CORTEX_A57
CONFIG_CPU_CORTEX_A72
CONFIG_CPU_CORTEX_A76
CONFIG_CPU_CORTEX_A76_A55
CONFIG_CPU_CORTEX_A78
CONFIG_CPU_CORTEX_A510
CONFIG_CPU_CORTEX_A320
CONFIG_CPU_CORTEX_A720
```

**弱选择（Implies）**

```text
CONFIG_FPU
CONFIG_FPU_SHARING
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX)、[`CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_KERNEL_DIRECT_MAP`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_DIRECT_MAP)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_CPU_HAS_ICACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_ICACHE)、[`CONFIG_ARCH_HAS_PMU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_PMU)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR)、[`CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_COREDUMP_SMP_FREEZE)、[`CONFIG_SOC_QEMU_VIRT_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_VIRT_ARM64)、[`CONFIG_CPU_CORTEX_A53`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A53)、[`CONFIG_CPU_CORTEX_A55`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A55)、[`CONFIG_CPU_CORTEX_A57`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A57)、[`CONFIG_CPU_CORTEX_A72`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A72)、[`CONFIG_CPU_CORTEX_A76`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A76)、[`CONFIG_CPU_CORTEX_A76_A55`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A76_A55)、[`CONFIG_CPU_CORTEX_A78`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A78)、[`CONFIG_CPU_CORTEX_A510`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A510)、[`CONFIG_CPU_CORTEX_A320`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A320)、[`CONFIG_CPU_CORTEX_A720`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A720)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_SINGLE_THREAD_SUPPORT`、`CONFIG_ARCH_SUPPORTS_COREDUMP_THREADS`、`CONFIG_ARCH_SUPPORTS_COREDUMP_STACK_PTR`、`CONFIG_SOC_QEMU_VIRT_ARM64`。

<a id="CONFIG_CPU_CORTEX_A320"></a>

## 31.42 `CONFIG_CPU_CORTEX_A320`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用实现 ARMv9.2-A 架构的 Cortex-A320 CPU，提供增强 SVE2、改进的安全扩展及专门的性能优化等高级功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV9_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_A320
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_SOC_A320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_A320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_A320`。

<a id="CONFIG_CPU_CORTEX_A510"></a>

## 31.43 `CONFIG_CPU_CORTEX_A510`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A510 CPU，它是实现 ARMv9-A 架构的 Arm 能效内核（Efficiency Core），针对嵌入式应用提供具有 ARMv9-A 功能的节能处理能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV9_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_V9A
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_SOC_V9A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V9A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_V9A`。

<a id="CONFIG_CPU_CORTEX_A53"></a>

## 31.44 `CONFIG_CPU_CORTEX_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A53 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_SUN50I_H618
CONFIG_SOC_SERIES_AM62LX_A53
CONFIG_SOC_SERIES_AM62X_A53
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_BCM2710
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_SERIES_AGILEX
CONFIG_SOC_RK3399
CONFIG_SOC_V8A
CONFIG_SOC_QEMU_CORTEX_A53
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_SUN50I_H618`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN50I_H618)、[`CONFIG_SOC_SERIES_AM62LX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62LX_A53)、[`CONFIG_SOC_SERIES_AM62X_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_A53)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_BCM2710`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2710)、[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_SERIES_AGILEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AGILEX)、[`CONFIG_SOC_RK3399`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3399)、[`CONFIG_SOC_V8A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A)、[`CONFIG_SOC_QEMU_CORTEX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_CORTEX_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SUN50I_H618`、`CONFIG_SOC_BCM2710`、`CONFIG_SOC_RK3399`、`CONFIG_SOC_V8A`、`CONFIG_SOC_QEMU_CORTEX_A53`。

<a id="CONFIG_CPU_CORTEX_A55"></a>

## 31.45 `CONFIG_CPU_CORTEX_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A55 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A779F0_A55
CONFIG_SOC_MIMX9111
CONFIG_SOC_MIMX9131
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_MIMX94398_A55
CONFIG_SOC_MIMX9596_A55
CONFIG_SOC_MIMX9529_A55
CONFIG_SOC_SERIES_RZA3M
CONFIG_SOC_SERIES_RZA3UL
CONFIG_SOC_RK3568
CONFIG_SOC_RK3588S
CONFIG_SOC_MT8188_A55
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_R8A779F0_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_A55)、[`CONFIG_SOC_MIMX9111`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9111)、[`CONFIG_SOC_MIMX9131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9131)、[`CONFIG_SOC_MIMX9352_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_MIMX94398_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_A55)、[`CONFIG_SOC_MIMX9596_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_A55)、[`CONFIG_SOC_MIMX9529_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_A55)、[`CONFIG_SOC_SERIES_RZA3M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_RK3568`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3568)、[`CONFIG_SOC_RK3588S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588S)、[`CONFIG_SOC_MT8188_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_A55)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RK3568`、`CONFIG_SOC_RK3588S`。

<a id="CONFIG_CPU_CORTEX_A57"></a>

## 31.46 `CONFIG_CPU_CORTEX_A57`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A57 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A77951_A57
CONFIG_SOC_R8A77961
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_R8A77951_A57`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_A57)、[`CONFIG_SOC_R8A77961`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77961)。

<a id="CONFIG_CPU_CORTEX_A72"></a>

## 31.47 `CONFIG_CPU_CORTEX_A72`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A72 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_BCM58402_A72
CONFIG_SOC_BCM2711
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_LS1046A
CONFIG_SOC_XENVM
CONFIG_SOC_QNXHV_VM
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_BCM58402_A72`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_A72)、[`CONFIG_SOC_BCM2711`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2711)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_LS1046A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LS1046A)、[`CONFIG_SOC_XENVM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XENVM)、[`CONFIG_SOC_QNXHV_VM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QNXHV_VM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BCM2711`、`CONFIG_SOC_XENVM`、`CONFIG_SOC_QNXHV_VM`。

<a id="CONFIG_CPU_CORTEX_A720"></a>

## 31.48 `CONFIG_CPU_CORTEX_A720`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A720 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV9_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A78000_A720
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_SOC_R8A78000_A720`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_A720)。

<a id="CONFIG_CPU_CORTEX_A76"></a>

## 31.49 `CONFIG_CPU_CORTEX_A76`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A76 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A779G0_A76
CONFIG_SOC_BCM2712
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_R8A779G0_A76`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_A76)、[`CONFIG_SOC_BCM2712`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2712)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R8A779G0_A76`、`CONFIG_SOC_BCM2712`。

<a id="CONFIG_CPU_CORTEX_A76_A55"></a>

## 31.50 `CONFIG_CPU_CORTEX_A76_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用由 Cortex-A76 和 A55 构成的大小核 CPU 集群（Big.LITTLE CPU Cluster）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AGILEX5
CONFIG_SOC_RK3588
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_SERIES_AGILEX5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AGILEX5)、[`CONFIG_SOC_RK3588`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RK3588`。

<a id="CONFIG_CPU_CORTEX_A78"></a>

## 31.51 `CONFIG_CPU_CORTEX_A78`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-A78 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_A
```

**被选择（Selected by）**

```text
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_AMD_VERSAL2_APU
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)。

<a id="CONFIG_CPU_CORTEX_R82"></a>

## 31.52 `CONFIG_CPU_CORTEX_R82`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示使用 Cortex-R82 CPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_ARMV8_R
```

**被选择（Selected by）**

```text
CONFIG_SOC_FVP_AEMV8R_AARCH64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARMV8_R`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_R)、[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FVP_AEMV8R_AARCH64`。

<a id="CONFIG_HAS_ARM_SMCCC"></a>

## 31.53 `CONFIG_HAS_ARM_SMCCC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 Armv7 及以上架构加入安全监控调用（Secure Monitor Call，SMC）和虚拟机监控器调用（Hypervisor Call，HVC）指令支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**被选择（Selected by）**

```text
CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_MAX_XLAT_TABLES"></a>

## 31.54 `CONFIG_MAX_XLAT_TABLES`

**提示（Prompt）**：转换表最大数量（Maximum Number of Translation Tables）

**说明（Help）**

此选项指定转换表（Translation Table）的最大数量，据此在编译时分配转换表，并在运行时按需使用。如果运行时需求超过预分配数量，会触发断言（Assert）。所需数量取决于平台上离散内存区域的数量，包括普通内存和设备内存，以及为这些区域分配属性时所需的粒度（Granularity）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MMU && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
32 if CONFIG_USERSPACE && CONFIG_TEST && CONFIG_SMP
28 if CONFIG_USERSPACE && CONFIG_TEST
20 if CONFIG_USERSPACE && CONFIG_ARM64_VA_BITS >= 40
16 if CONFIG_USERSPACE
16 if CONFIG_SMP && CONFIG_ARM64_VA_BITS >= 36
12 if CONFIG_ARM64_VA_BITS >= 40
8
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:418`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L418)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MMU`](P031_arch_arm64_配置项参考.md#CONFIG_ARM_MMU)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARM64_VA_BITS`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_VA_BITS)。

<a id="CONFIG_MPU_ALLOW_FLASH_WRITE"></a>

## 31.55 `CONFIG_MPU_ALLOW_FLASH_WRITE`

原库同名定义共 2 条；本项为数据库第 12269 条记录，各定义分别保留。

**提示（Prompt）**：为 Flash 增加 MPU 写访问权限（Write Access）

**说明（Help）**

启用后，允许 MPU 对 Flash 内存进行读／写／执行（RWX）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_MPU && CONFIG_CPU_HAS_MPU && CONFIG_CPU_AARCH64_CORTEX_R && CONFIG_ARM64
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_S32K1
CONFIG_FLASH_SHELL
CONFIG_SOC_FLASH_CC13XX_CC26XX
CONFIG_SOC_FLASH_CC23X0
CONFIG_SOC_FLASH_GD32
CONFIG_SOC_FLASH_GECKO
CONFIG_FLASH_MSPI_INFINEON_S28HX512T
CONFIG_FLASH_MCHP_NVMCTRL_G1
CONFIG_FLASH_MCHP_NVMCTRL_G2
CONFIG_FLASH_MCHP_NVMCTRL_G3
CONFIG_SOC_FLASH_MCUX
CONFIG_SOC_FLASH_NRF
CONFIG_SOC_FLASH_NRF_RRAM
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
CONFIG_SOC_FLASH_SAM
CONFIG_SOC_FLASH_SAM0
CONFIG_SOC_FLASH_SILABS_S2
CONFIG_SOC_FLASH_SMARTBOND
CONFIG_SOC_FLASH_STM32
CONFIG_BT_SETTINGS
CONFIG_MCUMGR_GRP_IMG
CONFIG_HAWKBIT
CONFIG_UPDATEHUB
CONFIG_USB_DFU_CLASS
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
CONFIG_SOC_FLASH_NRF_MRAM
CONFIG_SOC_FLASH_NRF_MRAMC
```

**定义位置（Location）**：[`arch/arm64/core/cortex_r/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/cortex_r/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_MPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_MPU)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_FLASH_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_SHELL)、[`CONFIG_SOC_FLASH_CC13XX_CC26XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_CC13XX_CC26XX)、[`CONFIG_SOC_FLASH_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_CC23X0)、[`CONFIG_SOC_FLASH_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_GD32)、[`CONFIG_SOC_FLASH_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_GECKO)、[`CONFIG_FLASH_MSPI_INFINEON_S28HX512T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MSPI_INFINEON_S28HX512T)、[`CONFIG_FLASH_MCHP_NVMCTRL_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G1)、[`CONFIG_FLASH_MCHP_NVMCTRL_G2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G2)、[`CONFIG_FLASH_MCHP_NVMCTRL_G3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MCHP_NVMCTRL_G3)、[`CONFIG_SOC_FLASH_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_SOC_FLASH_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF)、[`CONFIG_SOC_FLASH_NRF_RRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)、[`CONFIG_SOC_FLASH_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SAM)、[`CONFIG_SOC_FLASH_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SAM0)、[`CONFIG_SOC_FLASH_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SILABS_S2)、[`CONFIG_SOC_FLASH_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_SMARTBOND)、[`CONFIG_SOC_FLASH_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_STM32)、[`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)、[`CONFIG_MCUMGR_GRP_IMG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_HAWKBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)、[`CONFIG_USB_DFU_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_CLASS)、[`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD)、[`CONFIG_SOC_FLASH_NRF_MRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_NRF_MRAMC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`。

<a id="CONFIG_WAIT_AT_RESET_VECTOR"></a>

## 31.56 `CONFIG_WAIT_AT_RESET_VECTOR`

**提示（Prompt）**：在复位向量处等待（Wait at Reset Vector）

**说明（Help）**

在复位向量（Reset Vector）处自旋，等待调试器连接并恢复执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`arch/arm64/core/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_XEN"></a>

## 31.57 `CONFIG_XEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM64 平台对 Xen 虚拟机监控器（Hypervisor）的支持。当开发板设备树包含已启用、且兼容标识（Compatible）为 `xen,xen` 的 `hypervisor` 节点时，此项启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ARMV8_A || CONFIG_ARMV9_A) && DT_HAS_XEN_XEN_ENABLED && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GNU_C_EXTENSIONS
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_ARMV8_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV8_A)、[`CONFIG_ARMV9_A`](P031_arch_arm64_配置项参考.md#CONFIG_ARMV9_A)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_GNU_C_EXTENSIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_GNU_C_EXTENSIONS)。

<a id="CONFIG_XEN_DOM0"></a>

## 31.58 `CONFIG_XEN_DOM0`

**提示（Prompt）**：Zephyr 作为 Xen 特权域（Domain 0）

**说明（Help）**

构建的二进制文件将用作 Xen 特权域（Privileged Domain，即 Domain 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_XEN_DOM0LESS"></a>

## 31.59 `CONFIG_XEN_DOM0LESS`

**提示（Prompt）**：用于 Xen 无 Dom0 配置（Dom0less Setup）的 Zephyr

**说明（Help）**

将 Zephyr 配置为可在无 Dom0 环境（Dom0less Setup）中启动的非特权域（DomU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && !CONFIG_XEN_DOM0 && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_XEN_DOM0`](P031_arch_arm64_配置项参考.md#CONFIG_XEN_DOM0)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_XEN_DOMCTL_INTERFACE_VERSION"></a>

## 31.60 `CONFIG_XEN_DOMCTL_INTERFACE_VERSION`

**提示（Prompt）**：Xen Domctl 接口版本（Interface Version）

**说明（Help）**

要使用的 Xen Domctl 接口版本（Interface Version），Zephyr 通过该版本的 domctl 接口与虚拟机监控器（Hypervisor）通信。默认值为内核支持的最新版本。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**默认值（Defaults）**

```text
0x17
```

**取值范围（Ranges）**

```text
[0x15, 0x18]
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_XEN_INTERFACE_VERSION"></a>

## 31.61 `CONFIG_XEN_INTERFACE_VERSION`

**提示（Prompt）**：Xen 接口版本（Interface Version）

**说明（Help）**

要使用的 Xen 接口版本（Interface Version），Zephyr 通过该版本接口与虚拟机监控器（Hypervisor）通信。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**默认值（Defaults）**

```text
0x00040e00
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_XEN_SYSCTL_INTERFACE_VERSION"></a>

## 31.62 `CONFIG_XEN_SYSCTL_INTERFACE_VERSION`

**提示（Prompt）**：Xen Sysctl 接口版本（Interface Version）

**说明（Help）**

要使用的 Xen Sysctl 接口版本（Interface Version）。原文称这是 Zephyr 与虚拟机监控器（Hypervisor）通信所用的 domctl 接口版本，默认值为内核支持的最新版本。

译注：本项标题为 Sysctl，但帮助正文使用 `domctl`，两者按原文保留并提示此不一致。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN && CONFIG_CPU_CORTEX_A && CONFIG_ARM64
```

**默认值（Defaults）**

```text
0x15
```

**取值范围（Ranges）**

```text
[0x15, 0x16]
```

**定义位置（Location）**：[`arch/arm64/core/xen/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm64/core/xen/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](P031_arch_arm64_配置项参考.md#CONFIG_XEN)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<!-- kconfig-navigation -->

[上一章](P030_arch_arm_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P032_arch_common_配置项参考.md)
