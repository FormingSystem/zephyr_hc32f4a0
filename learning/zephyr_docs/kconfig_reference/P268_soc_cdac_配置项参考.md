---
id: learning.zephyr-docs.kconfig-reference.page-268
title: "`soc/cdac`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第268章\_`soc/cdac`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/cdac` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_THEJAS32"></a>

## 268.1 `CONFIG_SOC_THEJAS32`

原库同名定义共 2 条；本项为数据库第 18117 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

C-DAC THEJAS32 片上系统（SoC），基于 VEGA ET1031 32 位 RISC-V 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_CDAC
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARIES_V3
```

**定义位置（Location）**：[`soc/cdac/thejas32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/cdac/thejas32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_CDAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CDAC)、[`CONFIG_BOARD_ARIES_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARIES_V3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CDAC`、`CONFIG_BOARD_ARIES_V3`。

<a id="CONFIG_SOC_THEJAS32--record-18118"></a>

## 268.2 `CONFIG_SOC_THEJAS32`

原库同名定义共 2 条；本项为数据库第 18118 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 C-DAC THEJAS32 片上系统（SoC）支持。THEJAS32 围绕 VEGA ET1031 构建；它是由 C-DAC 在印度“数字印度 RISC-V”（Digital India RISC-V，DIR-V）计划中设计的 32 位（RV32IM）、单核、顺序执行（in-order）、三级流水线（3-stage pipeline）RISC-V 处理器。镜像加载到内部 SRAM 并从中执行，因此不使用原地执行（XIP）。该 SoC 的陷阱处理（trap handling）遵循 RISC-V 特权规范（privileged specification），但使用自定义的非 PLIC 中断控制器，因此提供自己的中断管理，而不选择 `RISCV_PRIVILEGED`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_RISCV
CONFIG_INCLUDE_RESET_VECTOR
CONFIG_RISCV_SOC_INTERRUPT_INIT
CONFIG_ATOMIC_OPERATIONS_C
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARIES_V3
```

**定义位置（Location）**：[`soc/cdac/thejas32/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/cdac/thejas32/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_INCLUDE_RESET_VECTOR`](P034_arch_riscv_配置项参考_1.md#CONFIG_INCLUDE_RESET_VECTOR)、[`CONFIG_RISCV_SOC_INTERRUPT_INIT`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_SOC_INTERRUPT_INIT)、[`CONFIG_ATOMIC_OPERATIONS_C`](P197_lib_配置项参考_1.md#CONFIG_ATOMIC_OPERATIONS_C)、[`CONFIG_BOARD_ARIES_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARIES_V3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ARIES_V3`。

<a id="SB_CONFIG_SOC_THEJAS32"></a>

## 268.3 `SB_CONFIG_SOC_THEJAS32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

C-DAC THEJAS32 片上系统（SoC），基于 VEGA ET1031 32 位 RISC-V 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_CDAC
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ARIES_V3
```

**定义位置（Location）**：[`soc/cdac/thejas32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/cdac/thejas32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_CDAC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_CDAC)、[`SB_CONFIG_BOARD_ARIES_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARIES_V3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_CDAC`、`SB_CONFIG_BOARD_ARIES_V3`。

<!-- kconfig-navigation -->

[上一章](P267_soc_brcm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P269_soc_cdns_配置项参考.md)
