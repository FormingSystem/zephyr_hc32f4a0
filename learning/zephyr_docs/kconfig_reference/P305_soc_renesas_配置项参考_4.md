---
id: learning.zephyr-docs.kconfig-reference.page-305
title: "`soc/renesas`配置项参考（4/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第305章\_`soc/renesas`配置项参考（4/4）

本章翻译官方 Kconfig 数据库中 `soc/renesas` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="SB_CONFIG_SOC_SERIES_RZA3UL"></a>

## 305.1 `SB_CONFIG_SOC_SERIES_RZA3UL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A3UL 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G063U02GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza3ul/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3ul/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G063U02GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G063U02GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZG2L"></a>

## 305.2 `SB_CONFIG_SOC_SERIES_RZG2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G044L23GBG
SB_CONFIG_SOC_R9A07G044C22GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G044L23GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G044L23GBG)、[`SB_CONFIG_SOC_R9A07G044C22GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G044C22GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZG2UL"></a>

## 305.3 `SB_CONFIG_SOC_SERIES_RZG2UL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G2UL 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G043U11GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2ul/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2ul/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G043U11GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G043U11GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZG3E"></a>

## 305.4 `SB_CONFIG_SOC_SERIES_RZG3E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G3E 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G047E57GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3e/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3e/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A09G047E57GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G047E57GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZG3S"></a>

## 305.5 `SB_CONFIG_SOC_SERIES_RZG3S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G3S 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A08G045S33GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3s/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3s/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A08G045S33GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A08G045S33GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZN2H"></a>

## 305.6 `SB_CONFIG_SOC_SERIES_RZN2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/N2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G087M44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A09G087M44GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G087M44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZN2L"></a>

## 305.7 `SB_CONFIG_SOC_SERIES_RZN2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/N2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G084M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G084M04GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G084M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZT2H"></a>

## 305.8 `SB_CONFIG_SOC_SERIES_RZT2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G077M44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A09G077M44GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G077M44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZT2L"></a>

## 305.9 `SB_CONFIG_SOC_SERIES_RZT2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G074M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G074M04GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G074M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZT2M"></a>

## 305.10 `SB_CONFIG_SOC_SERIES_RZT2M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G075M24GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2m/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2m/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G075M24GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G075M24GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZV2H"></a>

## 305.11 `SB_CONFIG_SOC_SERIES_RZV2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G057H44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A09G057H44GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G057H44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZV2L"></a>

## 305.12 `SB_CONFIG_SOC_SERIES_RZV2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G054L23GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G054L23GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G054L23GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZV2N"></a>

## 305.13 `SB_CONFIG_SOC_SERIES_RZV2N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G056N48GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A09G056N48GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G056N48GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<!-- kconfig-navigation -->

[上一章](P304_soc_renesas_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P306_soc_renode_配置项参考.md)
