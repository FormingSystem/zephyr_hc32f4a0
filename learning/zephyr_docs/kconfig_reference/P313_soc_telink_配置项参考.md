---
id: learning.zephyr-docs.kconfig-reference.page-313
title: "`soc/telink`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第313章\_`soc/telink`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/telink` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_SERIES_TLSR951X"></a>

## 313.1 `CONFIG_SOC_SERIES_TLSR951X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Telink TLSR951X 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_TELINK_TLSR
```

**被选择（Selected by）**

```text
CONFIG_SOC_TLSR9518
```

**定义位置（Location）**：[`soc/telink/tlsr/tlsr951x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/telink/tlsr/tlsr951x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_TELINK_TLSR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_TELINK_TLSR)、[`CONFIG_SOC_TLSR9518`](P313_soc_telink_配置项参考.md#CONFIG_SOC_TLSR9518)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_TELINK_TLSR`。

<a id="CONFIG_SOC_TLSR9518"></a>

## 313.2 `CONFIG_SOC_TLSR9518`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Telink TLSR9518 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_TLSR951X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_TLSR9518ADK80D
```

**定义位置（Location）**：[`soc/telink/tlsr/tlsr951x/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/telink/tlsr/tlsr951x/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_TLSR951X`](P313_soc_telink_配置项参考.md#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_BOARD_TLSR9518ADK80D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TLSR9518ADK80D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_TLSR9518ADK80D`。

<a id="SB_CONFIG_SOC_SERIES_TLSR951X"></a>

## 313.3 `SB_CONFIG_SOC_SERIES_TLSR951X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Telink TLSR951X 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_TELINK_TLSR
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_TLSR9518
```

**定义位置（Location）**：[`soc/telink/tlsr/tlsr951x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/telink/tlsr/tlsr951x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_TELINK_TLSR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_TELINK_TLSR)、[`SB_CONFIG_SOC_TLSR9518`](P313_soc_telink_配置项参考.md#SB_CONFIG_SOC_TLSR9518)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_TELINK_TLSR`。

<a id="SB_CONFIG_SOC_TLSR9518"></a>

## 313.4 `SB_CONFIG_SOC_TLSR9518`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Telink TLSR9518 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_TLSR951X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_TLSR9518ADK80D
```

**定义位置（Location）**：[`soc/telink/tlsr/tlsr951x/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/telink/tlsr/tlsr951x/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_TLSR951X`](P313_soc_telink_配置项参考.md#SB_CONFIG_SOC_SERIES_TLSR951X)、[`SB_CONFIG_BOARD_TLSR9518ADK80D`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TLSR9518ADK80D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_TLSR9518ADK80D`。

<!-- kconfig-navigation -->

[上一章](P312_soc_starfive_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P314_soc_ti_配置项参考.md)
