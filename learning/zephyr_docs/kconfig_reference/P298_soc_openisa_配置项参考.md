---
id: learning.zephyr-docs.kconfig-reference.page-298
title: "`soc/openisa`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第298章\_`soc/openisa`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/openisa` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_OPENISA_RV32M1"></a>

## 298.1 `CONFIG_SOC_OPENISA_RV32M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 OpenISA RV32M1 RISC-V 处理器支持。选择此项以 RI5CY 或 ZERO-RISCY 内核为目标。不应使用此选项针对其中任何一个 Arm 内核构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_OPENISA_RV32M1_RI5CY
CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1_RI5CY`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1_RI5CY)、[`CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY)。

<a id="CONFIG_SOC_OPENISA_RV32M1_RI5CY"></a>

## 298.2 `CONFIG_SOC_OPENISA_RV32M1_RI5CY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenISA RV32M1 RI5CY 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RV32M1_VEGA
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_BOARD_RV32M1_VEGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RV32M1_VEGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RV32M1_VEGA`。

<a id="CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY"></a>

## 298.3 `CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenISA RV32M1 ZERO-RISCY 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_OPENISA_RV32M1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RV32M1_VEGA
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_BOARD_RV32M1_VEGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RV32M1_VEGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RV32M1_VEGA`。

<a id="SB_CONFIG_SOC_OPENISA_RV32M1"></a>

## 298.4 `SB_CONFIG_SOC_OPENISA_RV32M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 OpenISA RV32M1 RISC-V 处理器支持。选择此项以 RI5CY 或 ZERO-RISCY 内核为目标。不应使用此选项针对其中任何一个 Arm 内核构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_OPENISA_RV32M1_RI5CY
SB_CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_OPENISA_RV32M1_RI5CY`](P298_soc_openisa_配置项参考.md#SB_CONFIG_SOC_OPENISA_RV32M1_RI5CY)、[`SB_CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY`](P298_soc_openisa_配置项参考.md#SB_CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY)。

<a id="SB_CONFIG_SOC_OPENISA_RV32M1_RI5CY"></a>

## 298.5 `SB_CONFIG_SOC_OPENISA_RV32M1_RI5CY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenISA RV32M1 RI5CY 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_OPENISA_RV32M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RV32M1_VEGA
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#SB_CONFIG_SOC_OPENISA_RV32M1)、[`SB_CONFIG_BOARD_RV32M1_VEGA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RV32M1_VEGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RV32M1_VEGA`。

<a id="SB_CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY"></a>

## 298.6 `SB_CONFIG_SOC_OPENISA_RV32M1_ZERO_RISCY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenISA RV32M1 ZERO-RISCY 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_OPENISA_RV32M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RV32M1_VEGA
```

**定义位置（Location）**：[`soc/openisa/rv32m1/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/openisa/rv32m1/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_OPENISA_RV32M1`](P298_soc_openisa_配置项参考.md#SB_CONFIG_SOC_OPENISA_RV32M1)、[`SB_CONFIG_BOARD_RV32M1_VEGA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RV32M1_VEGA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RV32M1_VEGA`。

<!-- kconfig-navigation -->

[上一章](P297_soc_openhwgroup_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P299_soc_quicklogic_配置项参考.md)
