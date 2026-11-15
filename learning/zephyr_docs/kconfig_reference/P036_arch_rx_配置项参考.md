---
id: learning.zephyr-docs.kconfig-reference.page-36
title: "`arch/rx`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第36章\_`arch/rx`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/rx` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_RXV1"></a>

## 36.1 `CONFIG_CPU_RXV1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器支持瑞萨（Renesas）RXv1 指令集（Instruction Set）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX62N
```

**定义位置（Location）**：[`arch/rx/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX62N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX62N)。

<a id="CONFIG_CPU_RXV2"></a>

## 36.2 `CONFIG_CPU_RXV2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器支持瑞萨（Renesas）RXv2 指令集（Instruction Set）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**主动选择（Selects）**

```text
CONFIG_HAS_EXCEPT_VECTOR_TABLE
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
```

**定义位置（Location）**：[`arch/rx/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_HAS_EXCEPT_VECTOR_TABLE`](P036_arch_rx_配置项参考.md#CONFIG_HAS_EXCEPT_VECTOR_TABLE)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)。

<a id="CONFIG_CPU_RXV3"></a>

## 36.3 `CONFIG_CPU_RXV3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器支持瑞萨（Renesas）RXv3 指令集（Instruction Set）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**主动选择（Selects）**

```text
CONFIG_HAS_EXCEPT_VECTOR_TABLE
CONFIG_CPU_HAS_FPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
```

**定义位置（Location）**：[`arch/rx/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_HAS_EXCEPT_VECTOR_TABLE`](P036_arch_rx_配置项参考.md#CONFIG_HAS_EXCEPT_VECTOR_TABLE)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)。

<a id="CONFIG_CPU_RXV3E"></a>

## 36.4 `CONFIG_CPU_RXV3E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器支持瑞萨（Renesas）RXv3e 指令集（Instruction Set）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**主动选择（Selects）**

```text
CONFIG_HAS_EXCEPT_VECTOR_TABLE
CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
```

**定义位置（Location）**：[`arch/rx/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_HAS_EXCEPT_VECTOR_TABLE`](P036_arch_rx_配置项参考.md#CONFIG_HAS_EXCEPT_VECTOR_TABLE)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU_DOUBLE_PRECISION)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)。

<a id="CONFIG_HAS_EXCEPT_VECTOR_TABLE"></a>

## 36.5 `CONFIG_HAS_EXCEPT_VECTOR_TABLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理器具有异常向量表（Exception Vector Table）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**被选择（Selected by）**

```text
CONFIG_CPU_RXV2
CONFIG_CPU_RXV3
CONFIG_CPU_RXV3E
```

**定义位置（Location）**：[`arch/rx/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_CPU_RXV2`](P036_arch_rx_配置项参考.md#CONFIG_CPU_RXV2)、[`CONFIG_CPU_RXV3`](P036_arch_rx_配置项参考.md#CONFIG_CPU_RXV3)、[`CONFIG_CPU_RXV3E`](P036_arch_rx_配置项参考.md#CONFIG_CPU_RXV3E)。

<a id="CONFIG_HAS_MAPPED_INTERRUPTS"></a>

## 36.6 `CONFIG_HAS_MAPPED_INTERRUPTS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

映射中断支持（Mapped Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX26T
```

**定义位置（Location）**：[`arch/rx/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)。

<a id="CONFIG_INITIALIZATION_STACK_SIZE"></a>

## 36.7 `CONFIG_INITIALIZATION_STACK_SIZE`

**提示（Prompt）**：初始化栈大小，单位为字节（Initialization Stack Size）

**说明（Help）**

内核初始化过程（Kernel Initialization Process）的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`arch/rx/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)。

<a id="CONFIG_NUM_IRQ_PRIO_LEVELS"></a>

## 36.8 `CONFIG_NUM_IRQ_PRIO_LEVELS`

原库同名定义共 2 条；本项为数据库第 14036 条记录，各定义分别保留。

**提示（Prompt）**：支持的中断优先级数量（Number of Interrupt Priority Levels）

**说明（Help）**

可用中断优先级（Interrupt Priority）为 `0` 到 `NUM_IRQ_PRIO_LEVELS-1`，最小值为 `1`。板级支持包（BSP）必须提供有效默认值，以保证正常运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RX
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`arch/rx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/rx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 瑞萨 RX 选项（Renesas RX Options）

**配置项引用（Symbol References）**：[`CONFIG_RX`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RX)。

<!-- kconfig-navigation -->

[上一章](P035_arch_riscv_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P037_arch_sparc_配置项参考.md)
