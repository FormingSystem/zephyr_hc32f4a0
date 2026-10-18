---
id: learning.zephyr-docs.kconfig-reference.page-297
title: "`soc/openhwgroup`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第297章\_`soc/openhwgroup`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/openhwgroup` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_CV32A6"></a>

## 297.1 `CONFIG_SOC_CV32A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

采用 32 位配置的最小 CVA6 内核：具有 ima 扩展，不含内存管理单元（MMU）或物理内存保护（PMP）；SoC 包含内核本地中断器（CLINT）、平台级中断控制器（PLIC）、UART、SPI 和以太网（Xilinx 或 lowRISC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CV32A6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CV32A6_GENESYS_2
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv32a6/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv32a6/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CV32A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_SERIES_CV32A6)、[`CONFIG_BOARD_CV32A6_GENESYS_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CV32A6_GENESYS_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CV32A6_GENESYS_2`。

<a id="CONFIG_SOC_CV64A6"></a>

## 297.2 `CONFIG_SOC_CV64A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

采用 64 位配置的标准 CVA6 内核：具有 SV39 内存管理单元（MMU）；SoC 包含内核本地中断器（CLINT）、平台级中断控制器（PLIC）、UART、SPI 和以太网（Xilinx 或 lowRISC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_CV64A6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CV64A6_GENESYS_2
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv64a6/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv64a6/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CV64A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_SERIES_CV64A6)、[`CONFIG_BOARD_CV64A6_GENESYS_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CV64A6_GENESYS_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_CV64A6_GENESYS_2`。

<a id="CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6"></a>

## 297.3 `CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。包含具有 imafdc 扩展和 sv39 内存管理单元（MMU）的 64 位版本，以及多种 32 位配置；32 位配置最多可选配 imafdc 扩展和 sv32 MMU。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_CV32A6
CONFIG_SOC_SERIES_CV64A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_CV32A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_SERIES_CV32A6)、[`CONFIG_SOC_SERIES_CV64A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_SERIES_CV64A6)。

<a id="CONFIG_SOC_SERIES_CV32A6"></a>

## 297.4 `CONFIG_SOC_SERIES_CV32A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 32 位 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。此配置适用于 [CVA6 上游项目](https://github.com/openhwgroup/cva6)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6
```

**被选择（Selected by）**

```text
CONFIG_SOC_CV32A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv32a6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv32a6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6)、[`CONFIG_SOC_CV32A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_CV32A6)。

<a id="CONFIG_SOC_SERIES_CV64A6"></a>

## 297.5 `CONFIG_SOC_SERIES_CV64A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 64 位 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。此配置适用于 [CVA6 上游项目](https://github.com/openhwgroup/cva6)，也适用于支持 Xilinx AXI 以太网子系统（Ethernet Subsystem）的[派生项目](https://github.com/cispa/CVA6-Vivado-Project-with-Xilinx-AXI-Ethernet)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6
```

**被选择（Selected by）**

```text
CONFIG_SOC_CV64A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv64a6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv64a6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6)、[`CONFIG_SOC_CV64A6`](P297_soc_openhwgroup_配置项参考.md#CONFIG_SOC_CV64A6)。

<a id="SB_CONFIG_SOC_CV32A6"></a>

## 297.6 `SB_CONFIG_SOC_CV32A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

采用 32 位配置的最小 CVA6 内核：具有 ima 扩展，不含内存管理单元（MMU）或物理内存保护（PMP）；SoC 包含内核本地中断器（CLINT）、平台级中断控制器（PLIC）、UART、SPI 和以太网（Xilinx 或 lowRISC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CV32A6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CV32A6_GENESYS_2
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv32a6/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv32a6/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CV32A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_SERIES_CV32A6)、[`SB_CONFIG_BOARD_CV32A6_GENESYS_2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CV32A6_GENESYS_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CV32A6_GENESYS_2`。

<a id="SB_CONFIG_SOC_CV64A6"></a>

## 297.7 `SB_CONFIG_SOC_CV64A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

采用 64 位配置的标准 CVA6 内核：具有 SV39 内存管理单元（MMU）；SoC 包含内核本地中断器（CLINT）、平台级中断控制器（PLIC）、UART、SPI 和以太网（Xilinx 或 lowRISC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_CV64A6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CV64A6_GENESYS_2
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv64a6/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv64a6/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CV64A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_SERIES_CV64A6)、[`SB_CONFIG_BOARD_CV64A6_GENESYS_2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CV64A6_GENESYS_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_CV64A6_GENESYS_2`。

<a id="SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6"></a>

## 297.8 `SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。包含具有 imafdc 扩展和 sv39 内存管理单元（MMU）的 64 位版本，以及多种 32 位配置；32 位配置最多可选配 imafdc 扩展和 sv32 MMU。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_CV32A6
SB_CONFIG_SOC_SERIES_CV64A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_CV32A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_SERIES_CV32A6)、[`SB_CONFIG_SOC_SERIES_CV64A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_SERIES_CV64A6)。

<a id="SB_CONFIG_SOC_SERIES_CV32A6"></a>

## 297.9 `SB_CONFIG_SOC_SERIES_CV32A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 32 位 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。此配置适用于 [CVA6 上游项目](https://github.com/openhwgroup/cva6)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CV32A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv32a6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv32a6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6)、[`SB_CONFIG_SOC_CV32A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_CV32A6)。

<a id="SB_CONFIG_SOC_SERIES_CV64A6"></a>

## 297.10 `SB_CONFIG_SOC_SERIES_CV64A6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CVA6 64 位 RISC-V CPU，通常用作 FPGA 上的软核（soft core）。此配置适用于 [CVA6 上游项目](https://github.com/openhwgroup/cva6)，也适用于支持 Xilinx AXI 以太网子系统（Ethernet Subsystem）的[派生项目](https://github.com/cispa/CVA6-Vivado-Project-with-Xilinx-AXI-Ethernet)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_CV64A6
```

**定义位置（Location）**：[`soc/openhwgroup/cva6/cv64a6/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openhwgroup/cva6/cv64a6/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_FAMILY_OPENHWGROUP_CVA6)、[`SB_CONFIG_SOC_CV64A6`](P297_soc_openhwgroup_配置项参考.md#SB_CONFIG_SOC_CV64A6)。

<!-- kconfig-navigation -->

[上一章](P296_soc_oct_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P298_soc_openisa_配置项参考.md)
