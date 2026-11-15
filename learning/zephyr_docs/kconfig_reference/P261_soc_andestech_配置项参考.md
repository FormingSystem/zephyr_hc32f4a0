---
id: learning.zephyr-docs.kconfig-reference.page-261
title: "`soc/andestech`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第261章\_`soc/andestech`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/andestech` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AE350"></a>

## 261.1 `CONFIG_SOC_AE350`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Andes AE350 片上系统实现（SoC implementation）。译注：原始提示末尾含有多余的双引号。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AE350
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ADP_XC7K
CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AE350`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_SERIES_AE350)、[`CONFIG_BOARD_ADP_XC7K`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADP_XC7K)、[`CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ADP_XC7K`、`CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK`。

<a id="CONFIG_SOC_AE350_INTERRUPT_TYPE"></a>

## 261.2 `CONFIG_SOC_AE350_INTERRUPT_TYPE`

**提示（Prompt）**：基础中断类型（Base interrupt type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_AE350 && CONFIG_SOC_SERIES_AE350 && CONFIG_SOC_FAMILY_ANDES_V5
```

**默认值（Defaults）**

```text
CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC
```

**可选项（Choices）**

```text
CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC
CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE350`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350)、[`CONFIG_SOC_SERIES_AE350`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_FAMILY_ANDES_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ANDES_V5)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ANDES_V5`。

<a id="CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC"></a>

## 261.3 `CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`

**提示（Prompt）**：内核本地中断控制器（Core Local Interrupt Controller，CLIC）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_AE350_INTERRUPT_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_RISCV_HAS_CLIC
CONFIG_CLIC_SMCLICSHV_EXT if CONFIG_RISCV_VECTORED_MODE
CONFIG_CLIC_SMCLICCONFIG_EXT
CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 基础中断类型（Base interrupt type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE350_INTERRUPT_TYPE`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350_INTERRUPT_TYPE)、[`CONFIG_RISCV_HAS_CLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_CLIC)、[`CONFIG_CLIC_SMCLICSHV_EXT`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC_SMCLICSHV_EXT)、[`CONFIG_RISCV_VECTORED_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_VECTORED_MODE)、[`CONFIG_CLIC_SMCLICCONFIG_EXT`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC_SMCLICCONFIG_EXT)、[`CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS)。

<a id="CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC"></a>

## 261.4 `CONFIG_SOC_AE350_INTERRUPT_TYPE_PLIC`

**提示（Prompt）**：平台级中断控制器（Platform-Level Interrupt Controller，PLIC）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_AE350_INTERRUPT_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_RISCV_HAS_PLIC
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 基础中断类型（Base interrupt type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE350_INTERRUPT_TYPE`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350_INTERRUPT_TYPE)、[`CONFIG_RISCV_HAS_PLIC`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_HAS_PLIC)。

<a id="CONFIG_SOC_ANDES_V5_IOCP"></a>

## 261.5 `CONFIG_SOC_ANDES_V5_IOCP`

**提示（Prompt）**：Andes V5 I/O 一致性端口（I/O Coherence Port，IOCP）

**说明（Help）**

支持 Andes V5 I/O 一致性端口（I/O Coherence Port），以处理缓存与外部无缓存主设备（external non-caching master，例如 DMA 控制器）之间的缓存一致性（cache coherency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DCACHE && CONFIG_SOC_SERIES_AE350 && CONFIG_SOC_FAMILY_ANDES_V5
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_SOC_SERIES_AE350`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_FAMILY_ANDES_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ANDES_V5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ANDES_V5`。

<a id="CONFIG_SOC_SERIES_AE350"></a>

## 261.6 `CONFIG_SOC_SERIES_AE350`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Andes V5 AE350 片上系统系列实现（SoC Series Implementation）。译注：原始提示末尾含有多余的双引号。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ANDES_V5
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE350
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ANDES_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ANDES_V5)、[`CONFIG_SOC_AE350`](P261_soc_andestech_配置项参考.md#CONFIG_SOC_AE350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ANDES_V5`。

<a id="SB_CONFIG_SOC_AE350"></a>

## 261.7 `SB_CONFIG_SOC_AE350`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Andes AE350 片上系统实现（SoC implementation）。译注：原始提示末尾含有多余的双引号。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AE350
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ADP_XC7K
SB_CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AE350`](P261_soc_andestech_配置项参考.md#SB_CONFIG_SOC_SERIES_AE350)、[`SB_CONFIG_BOARD_ADP_XC7K`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADP_XC7K)、[`SB_CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ADP_XC7K`、`SB_CONFIG_BOARD_TANG_MEGA_138K_PRO_DOCK`。

<a id="SB_CONFIG_SOC_SERIES_AE350"></a>

## 261.8 `SB_CONFIG_SOC_SERIES_AE350`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Andes V5 AE350 片上系统系列实现（SoC Series Implementation）。译注：原始提示末尾含有多余的双引号。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ANDES_V5
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE350
```

**定义位置（Location）**：[`soc/andestech/ae350/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/andestech/ae350/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ANDES_V5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ANDES_V5)、[`SB_CONFIG_SOC_AE350`](P261_soc_andestech_配置项参考.md#SB_CONFIG_SOC_AE350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ANDES_V5`。

<!-- kconfig-navigation -->

[上一章](P260_soc_ambiq_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P262_soc_antmicro_配置项参考.md)
