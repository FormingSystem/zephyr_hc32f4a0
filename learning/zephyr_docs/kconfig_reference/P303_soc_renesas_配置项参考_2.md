---
id: learning.zephyr-docs.kconfig-reference.page-303
title: "`soc/renesas`配置项参考（2/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第303章\_`soc/renesas`配置项参考（2/4）

本章翻译官方 Kconfig 数据库中 `soc/renesas` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_R9A07G044C22GBG"></a>

## 303.1 `CONFIG_SOC_R9A07G044C22GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G044C22GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZG2L
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZG2LC_SMARC
CONFIG_SOC_R9A07G044C22GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG2L`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_BOARD_RZG2LC_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZG2LC_SMARC)、[`CONFIG_SOC_R9A07G044C22GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A07G044C22GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZG2LC_SMARC`、`CONFIG_SOC_R9A07G044C22GBG_CM33`。

<a id="CONFIG_SOC_R9A07G044L23GBG"></a>

## 303.2 `CONFIG_SOC_R9A07G044L23GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G044L23GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZG2L
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZG2L_SMARC
CONFIG_SOC_R9A07G044L23GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG2L`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_BOARD_RZG2L_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZG2L_SMARC)、[`CONFIG_SOC_R9A07G044L23GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A07G044L23GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZG2L_SMARC`、`CONFIG_SOC_R9A07G044L23GBG_CM33`。

<a id="CONFIG_SOC_R9A07G054L23GBG"></a>

## 303.3 `CONFIG_SOC_R9A07G054L23GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G054L23GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZV2L
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZV2L_SMARC
CONFIG_SOC_R9A07G054L23GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZV2L`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_BOARD_RZV2L_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZV2L_SMARC)、[`CONFIG_SOC_R9A07G054L23GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A07G054L23GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZV2L_SMARC`、`CONFIG_SOC_R9A07G054L23GBG_CM33`。

<a id="CONFIG_SOC_R9A07G063U02GBG"></a>

## 303.4 `CONFIG_SOC_R9A07G063U02GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G063U02GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZA3UL
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZA3UL_SMARC
```

**定义位置（Location）**：[`soc/renesas/rz/rza3ul/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3ul/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZA3UL`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_BOARD_RZA3UL_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZA3UL_SMARC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZA3UL_SMARC`。

<a id="CONFIG_SOC_R9A07G066M04GBG"></a>

## 303.5 `CONFIG_SOC_R9A07G066M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G066M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZA3M
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZA3M_EK
```

**定义位置（Location）**：[`soc/renesas/rz/rza3m/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3m/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZA3M`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_BOARD_RZA3M_EK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZA3M_EK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZA3M_EK`。

<a id="CONFIG_SOC_R9A07G074M04GBG"></a>

## 303.6 `CONFIG_SOC_R9A07G074M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G074M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZT2L
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZT2L_RSK
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZT2L`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_BOARD_RZT2L_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZT2L_RSK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZT2L_RSK`。

<a id="CONFIG_SOC_R9A07G075M24GBG"></a>

## 303.7 `CONFIG_SOC_R9A07G075M24GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G075M24GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZT2M
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZT2M_RSK
CONFIG_SOC_R9A07G075M24GBG_CR520
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2m/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2m/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZT2M`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_BOARD_RZT2M_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZT2M_RSK)、[`CONFIG_SOC_R9A07G075M24GBG_CR520`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A07G075M24GBG_CR520)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZT2M_RSK`、`CONFIG_SOC_R9A07G075M24GBG_CR520`。

<a id="CONFIG_SOC_R9A07G084M04GBG"></a>

## 303.8 `CONFIG_SOC_R9A07G084M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G084M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZN2L
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZN2L_RSK
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZN2L`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_BOARD_RZN2L_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZN2L_RSK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZN2L_RSK`。

<a id="CONFIG_SOC_R9A08G045S33GBG"></a>

## 303.9 `CONFIG_SOC_R9A08G045S33GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A08G045S33GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZG3S
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZG3S_SMARC
CONFIG_SOC_R9A08G045S33GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3s/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3s/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG3S`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_BOARD_RZG3S_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZG3S_SMARC)、[`CONFIG_SOC_R9A08G045S33GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A08G045S33GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZG3S_SMARC`、`CONFIG_SOC_R9A08G045S33GBG_CM33`。

<a id="CONFIG_SOC_R9A09G047E57GBG"></a>

## 303.10 `CONFIG_SOC_R9A09G047E57GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G047E57GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZG3E
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZG3E_SMARC
CONFIG_SOC_R9A09G047E57GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3e/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3e/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG3E`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_BOARD_RZG3E_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZG3E_SMARC)、[`CONFIG_SOC_R9A09G047E57GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G047E57GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZG3E_SMARC`、`CONFIG_SOC_R9A09G047E57GBG_CM33`。

<a id="CONFIG_SOC_R9A09G056N48GBG"></a>

## 303.11 `CONFIG_SOC_R9A09G056N48GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G056N48GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZV2N
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G056N48GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2n/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2n/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZV2N`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_R9A09G056N48GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G056N48GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R9A09G056N48GBG_CM33`。

<a id="CONFIG_SOC_R9A09G057H44GBG"></a>

## 303.12 `CONFIG_SOC_R9A09G057H44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G057H44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZV2H
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_R9A09G057H44GBG_CR8
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZV2H`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZV2H)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G057H44GBG_CR8)。

<a id="CONFIG_SOC_R9A09G057H44GBG_CM33"></a>

## 303.13 `CONFIG_SOC_R9A09G057H44GBG_CM33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RZ/V2H CM33 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_R9A09G057H44GBG
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZV2H_EVK
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_R9A09G057H44GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G057H44GBG)、[`CONFIG_BOARD_RZV2H_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZV2H_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZV2H_EVK`。

<a id="CONFIG_SOC_R9A09G057H44GBG_CR8"></a>

## 303.14 `CONFIG_SOC_R9A09G057H44GBG_CR8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RZ/V2H CR8 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_R9A09G057H44GBG
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZV2H_EVK
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_R9A09G057H44GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G057H44GBG)、[`CONFIG_BOARD_RZV2H_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZV2H_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZV2H_EVK`。

<a id="CONFIG_SOC_R9A09G077M44GBG"></a>

## 303.15 `CONFIG_SOC_R9A09G077M44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G077M44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZT2H
```

**被选择（Selected by）**

```text
CONFIG_BOARD_RZT2H_EVB
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZT2H`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_BOARD_RZT2H_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RZT2H_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_RZT2H_EVB`。

<a id="CONFIG_SOC_R9A09G087M44GBG"></a>

## 303.16 `CONFIG_SOC_R9A09G087M44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G087M44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RZN2H
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G087M44GBG_CR52_0
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZN2H`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_R9A09G087M44GBG_CR52_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G087M44GBG_CR52_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R9A09G087M44GBG_CR52_0`。

<a id="CONFIG_SOC_RA_DYNAMIC_INTERRUPT_NUMBER"></a>

## 303.17 `CONFIG_SOC_RA_DYNAMIC_INTERRUPT_NUMBER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 SoC 选择此配置时，中断号（interrupt numbers）不是固定值，可以动态分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA2A1
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_SERIES_RA2A1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8M1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RA8T2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_SERIES_RA2L1`。

<a id="CONFIG_SOC_RA_ENABLE_START_SECOND_CORE"></a>

## 303.18 `CONFIG_SOC_RA_ENABLE_START_SECOND_CORE`

**提示（Prompt）**：允许主内核启动辅助内核（primary core starts secondary core）

**说明（Help）**

启用后，表示第二内核将在 `soc_late_init_hook` 中启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_PN_NUMBER_OF_CORES = 2 && CONFIG_CPU_CORTEX_M85 && CONFIG_SOC_FAMILY_RENESAS_RA
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_PN_NUMBER_OF_CORES`](P302_soc_renesas_配置项参考_1.md#CONFIG_RENESAS_PN_NUMBER_OF_CORES)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_RA_SECOND_CORE_BUILD"></a>

## 303.19 `CONFIG_SOC_RA_SECOND_CORE_BUILD`

**提示（Prompt）**：表示此镜像为辅助内核构建（secondary core image）

**说明（Help）**

启用后，表示此镜像是为辅助内核（secondary core）构建的。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8D2KFLCAC_CM33
CONFIG_SOC_R7KA8M2JFLCAC_CM33
CONFIG_SOC_R7KA8P1KFLCAC_CM33
CONFIG_SOC_R7KA8T2LFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8D2KFLCAC_CM33)、[`CONFIG_SOC_R7KA8M2JFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8M2JFLCAC_CM33)、[`CONFIG_SOC_R7KA8P1KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8P1KFLCAC_CM33)、[`CONFIG_SOC_R7KA8T2LFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7KA8T2LFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7KA8D2KFLCAC_CM33`、`CONFIG_SOC_R7KA8M2JFLCAC_CM33`、`CONFIG_SOC_R7KA8P1KFLCAC_CM33`、`CONFIG_SOC_R7KA8T2LFLCAC_CM33`。

<a id="CONFIG_SOC_SERIES_DA1469X"></a>

## 303.20 `CONFIG_SOC_SERIES_DA1469X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨 SmartBond™ DA1469x 系列微控制器（Renesas series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_SMARTBOND
```

**被选择（Selected by）**

```text
CONFIG_SOC_DA14695
CONFIG_SOC_DA14697
CONFIG_SOC_DA14699
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_SMARTBOND)、[`CONFIG_SOC_DA14695`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_DA14695)、[`CONFIG_SOC_DA14697`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_DA14697)、[`CONFIG_SOC_DA14699`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_DA14699)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`。

<a id="CONFIG_SOC_SERIES_RA0E1"></a>

## 303.21 `CONFIG_SOC_SERIES_RA0E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA0E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA0E1073CFJ
CONFIG_SOC_R7FA0E1073CNH
CONFIG_SOC_R7FA0E1073CNK
CONFIG_SOC_R7FA0E1073CSC
CONFIG_SOC_R7FA0E1073CSD
CONFIG_SOC_R7FA0E1073CNL
CONFIG_SOC_R7FA0E1053CFJ
CONFIG_SOC_R7FA0E1053CNH
CONFIG_SOC_R7FA0E1053CNK
CONFIG_SOC_R7FA0E1053CSC
CONFIG_SOC_R7FA0E1053CNL
```

**定义位置（Location）**：[`soc/renesas/ra/ra0e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra0e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA0E1073CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CFJ)、[`CONFIG_SOC_R7FA0E1073CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNH)、[`CONFIG_SOC_R7FA0E1073CNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNK)、[`CONFIG_SOC_R7FA0E1073CSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CSC)、[`CONFIG_SOC_R7FA0E1073CSD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CSD)、[`CONFIG_SOC_R7FA0E1073CNL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1073CNL)、[`CONFIG_SOC_R7FA0E1053CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CFJ)、[`CONFIG_SOC_R7FA0E1053CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNH)、[`CONFIG_SOC_R7FA0E1053CNK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNK)、[`CONFIG_SOC_R7FA0E1053CSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CSC)、[`CONFIG_SOC_R7FA0E1053CNL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA0E1053CNL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7FA0E1073CFJ`、`CONFIG_SOC_R7FA0E1073CNH`、`CONFIG_SOC_R7FA0E1073CNK`、`CONFIG_SOC_R7FA0E1073CSC`、`CONFIG_SOC_R7FA0E1073CSD`、`CONFIG_SOC_R7FA0E1073CNL`、`CONFIG_SOC_R7FA0E1053CFJ`、`CONFIG_SOC_R7FA0E1053CNH`、`CONFIG_SOC_R7FA0E1053CNK`、`CONFIG_SOC_R7FA0E1053CSC`、`CONFIG_SOC_R7FA0E1053CNL`。

<a id="CONFIG_SOC_SERIES_RA2A1"></a>

## 303.22 `CONFIG_SOC_SERIES_RA2A1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA2A1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA2A1AB3CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra2a1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2a1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA2A1AB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA2A1AB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4C1"></a>

## 303.23 `CONFIG_SOC_SERIES_RA4C1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4C1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4C1BD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4c1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4c1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4C1BD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4C1BD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4E1"></a>

## 303.24 `CONFIG_SOC_SERIES_RA4E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4E10D2CFM
CONFIG_SOC_R7FA4E10D2CNE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4E10D2CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E10D2CFM)、[`CONFIG_SOC_R7FA4E10D2CNE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E10D2CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4E2"></a>

## 303.25 `CONFIG_SOC_SERIES_RA4E2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4E2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4E2B93CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4E2B93CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4E2B93CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4L1"></a>

## 303.26 `CONFIG_SOC_SERIES_RA4L1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4L1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4L1BD4CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4l1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4l1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4L1BD4CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4L1BD4CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4M1"></a>

## 303.27 `CONFIG_SOC_SERIES_RA4M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4M1AB3CFM
CONFIG_SOC_R7FA4M1AB3CFP
CONFIG_SOC_R7FA4M1AB3CNE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M1AB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CFM)、[`CONFIG_SOC_R7FA4M1AB3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CFP)、[`CONFIG_SOC_R7FA4M1AB3CNE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M1AB3CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4M2"></a>

## 303.28 `CONFIG_SOC_SERIES_RA4M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4M2AD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M2AD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M2AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4M3"></a>

## 303.29 `CONFIG_SOC_SERIES_RA4M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M3 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4M3AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4M3AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4M3AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA4T1"></a>

## 303.30 `CONFIG_SOC_SERIES_RA4T1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4T1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4T1BB3CFM
CONFIG_SOC_R7FA4T1BB3CFL
CONFIG_SOC_R7FA4T1BB3CFJ
CONFIG_SOC_R7FA4T1BB3CNE
CONFIG_SOC_R7FA4T1BB3CNH
CONFIG_SOC_R7FA4T1B93CFM
CONFIG_SOC_R7FA4T1B93CFL
CONFIG_SOC_R7FA4T1B93CFJ
CONFIG_SOC_R7FA4T1B93CNE
CONFIG_SOC_R7FA4T1B93CNH
```

**定义位置（Location）**：[`soc/renesas/ra/ra4t1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4t1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4T1BB3CFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFM)、[`CONFIG_SOC_R7FA4T1BB3CFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFL)、[`CONFIG_SOC_R7FA4T1BB3CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CFJ)、[`CONFIG_SOC_R7FA4T1BB3CNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CNE)、[`CONFIG_SOC_R7FA4T1BB3CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1BB3CNH)、[`CONFIG_SOC_R7FA4T1B93CFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFM)、[`CONFIG_SOC_R7FA4T1B93CFL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFL)、[`CONFIG_SOC_R7FA4T1B93CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CFJ)、[`CONFIG_SOC_R7FA4T1B93CNE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CNE)、[`CONFIG_SOC_R7FA4T1B93CNH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R7FA4T1B93CNH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_R7FA4T1BB3CFM`、`CONFIG_SOC_R7FA4T1BB3CFL`、`CONFIG_SOC_R7FA4T1BB3CFJ`、`CONFIG_SOC_R7FA4T1BB3CNE`、`CONFIG_SOC_R7FA4T1BB3CNH`、`CONFIG_SOC_R7FA4T1B93CFM`、`CONFIG_SOC_R7FA4T1B93CFL`、`CONFIG_SOC_R7FA4T1B93CFJ`、`CONFIG_SOC_R7FA4T1B93CNE`、`CONFIG_SOC_R7FA4T1B93CNH`。

<a id="CONFIG_SOC_SERIES_RA4W1"></a>

## 303.31 `CONFIG_SOC_SERIES_RA4W1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4W1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA4W1AD2CNG
```

**定义位置（Location）**：[`soc/renesas/ra/ra4w1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4w1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA4W1AD2CNG`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA4W1AD2CNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6E1"></a>

## 303.32 `CONFIG_SOC_SERIES_RA6E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6E10F2CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6E10F2CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6E10F2CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6E2"></a>

## 303.33 `CONFIG_SOC_SERIES_RA6E2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6E2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6E2BB3CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6E2BB3CFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6E2BB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6M1"></a>

## 303.34 `CONFIG_SOC_SERIES_RA6M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6M1AD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M1AD3CFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M1AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6M2"></a>

## 303.35 `CONFIG_SOC_SERIES_RA6M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6M2AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M2AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M2AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6M3"></a>

## 303.36 `CONFIG_SOC_SERIES_RA6M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M3 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6M3AH3CFC
CONFIG_SOC_R7FA6M3AF2CBG
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M3AH3CFC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M3AH3CFC)、[`CONFIG_SOC_R7FA6M3AF2CBG`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M3AF2CBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6M4"></a>

## 303.37 `CONFIG_SOC_SERIES_RA6M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M4 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6M4AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m4/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m4/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M4AF3CFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M4AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA6M5"></a>

## 303.38 `CONFIG_SOC_SERIES_RA6M5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M5 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA6M5BH3CFC
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA6M5BH3CFC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA6M5BH3CFC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8D1"></a>

## 303.39 `CONFIG_SOC_SERIES_RA8D1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8D1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA8D1BHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8D1BHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8D1BHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8D2"></a>

## 303.40 `CONFIG_SOC_SERIES_RA8D2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8D2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8D2KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8D2KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8E1"></a>

## 303.41 `CONFIG_SOC_SERIES_RA8E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA8E1AFDCFB
CONFIG_SOC_R7FA8E1AFDCFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8E1AFDCFB`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8E1AFDCFB)、[`CONFIG_SOC_R7FA8E1AFDCFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8E1AFDCFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8M1"></a>

## 303.42 `CONFIG_SOC_SERIES_RA8M1`

原库同名定义共 2 条；本项为数据库第 18046 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA8M1AHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8M1AHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8M1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8M1--record-18047"></a>

## 303.43 `CONFIG_SOC_SERIES_RA8M1`

原库同名定义共 2 条；本项为数据库第 18047 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨 RA8M1 微控制器系列支持（Renesas MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**主动选择（Selects）**

```text
CONFIG_ARM
CONFIG_CPU_CORTEX_M85
CONFIG_CPU_HAS_ARM_MPU
CONFIG_CPU_HAS_FPU
CONFIG_CPU_HAS_ARM_SAU
CONFIG_ARMV8_M_DSP
CONFIG_ARMV8_1_M_MVEI
CONFIG_ARMV8_1_M_MVEF
CONFIG_FPU
CONFIG_HAS_SWO
CONFIG_XIP
CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC if CONFIG_CLOCK_CONTROL
CONFIG_HAS_RENESAS_RA_FSP
CONFIG_GPIO_RA_HAS_VBTICTLR
CONFIG_HAS_PM
CONFIG_PM_STATE_SET_IRQ_UNLOCKED
CONFIG_SOC_RA_DYNAMIC_INTERRUPT_NUMBER
CONFIG_ARM_MPU
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA8M1AHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M85`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M85)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_CPU_HAS_ARM_SAU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_SAU)、[`CONFIG_ARMV8_M_DSP`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_M_DSP)、[`CONFIG_ARMV8_1_M_MVEI`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MVEI)、[`CONFIG_ARMV8_1_M_MVEF`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV8_1_M_MVEF)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_HAS_SWO`](P030_arch_arm_配置项参考_2.md#CONFIG_HAS_SWO)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_HAS_RENESAS_RA_FSP`](P209_modules_Kconfig.renesas_配置项参考_1.md#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_GPIO_RA_HAS_VBTICTLR`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_RA_HAS_VBTICTLR)、[`CONFIG_HAS_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_PM)、[`CONFIG_PM_STATE_SET_IRQ_UNLOCKED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_STATE_SET_IRQ_UNLOCKED)、[`CONFIG_SOC_RA_DYNAMIC_INTERRUPT_NUMBER`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_RA_DYNAMIC_INTERRUPT_NUMBER)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_SOC_R7FA8M1AHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8M1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8M2"></a>

## 303.44 `CONFIG_SOC_SERIES_RA8M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8M2JFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8M2JFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8P1"></a>

## 303.45 `CONFIG_SOC_SERIES_RA8P1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8P1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8P1KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8P1KFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8T1"></a>

## 303.46 `CONFIG_SOC_SERIES_RA8T1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8T1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7FA8T1AHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7FA8T1AHECBD`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7FA8T1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RA8T2"></a>

## 303.47 `CONFIG_SOC_SERIES_RA8T2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8T2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7KA8T2LFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_R7KA8T2LFLCAC`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_SOC_SERIES_RCAR_GEN5"></a>

## 303.48 `CONFIG_SOC_SERIES_RCAR_GEN5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R-Car 第五代片上系统系列支持（R-Car Gen5 SoC series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RCAR
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_R8A78000_A720
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RCAR)、[`CONFIG_SOC_R8A78000_R52`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_R8A78000_A720`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R8A78000_A720)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RCAR`。

<a id="CONFIG_SOC_SERIES_RX130"></a>

## 303.49 `CONFIG_SOC_SERIES_RX130`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX130 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F51308AXFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F51308AXFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F51308AXFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX140"></a>

## 303.50 `CONFIG_SOC_SERIES_RX140`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX140 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F51406BDFN
CONFIG_SOC_R5F51406BGFN
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F51406BDFN`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F51406BDFN)、[`CONFIG_SOC_R5F51406BGFN`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F51406BGFN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX14T"></a>

## 303.51 `CONFIG_SOC_SERIES_RX14T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX14T 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F514T5AMFM
```

**定义位置（Location）**：[`soc/renesas/rx/rx14t/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx14t/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F514T5AMFM`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F514T5AMFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX261"></a>

## 303.52 `CONFIG_SOC_SERIES_RX261`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX261 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F52618BGFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx261/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx261/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F52618BGFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F52618BGFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX26T"></a>

## 303.53 `CONFIG_SOC_SERIES_RX26T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX26T 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F526TFDDFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx26t/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx26t/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F526TFDDFP`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F526TFDDFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX62N"></a>

## 303.54 `CONFIG_SOC_SERIES_RX62N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX62N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5F562N8
```

**定义位置（Location）**：[`soc/renesas/rx/rx62n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx62n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5F562N8`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5F562N8)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX74M"></a>

## 303.55 `CONFIG_SOC_SERIES_RX74M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX74M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5K574MCB4AE
```

**定义位置（Location）**：[`soc/renesas/rx/rx74m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5K574MCB4AE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5K574MCB4AE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RX74N"></a>

## 303.56 `CONFIG_SOC_SERIES_RX74N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX74N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R5K574NCB4AE
```

**定义位置（Location）**：[`soc/renesas/rx/rx74n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_SOC_R5K574NCB4AE`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R5K574NCB4AE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_SOC_SERIES_RZA2M"></a>

## 303.57 `CONFIG_SOC_SERIES_RZA2M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A2M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R7S921053VCBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza2m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza2m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R7S921053VCBG`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R7S921053VCBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZA3M"></a>

## 303.58 `CONFIG_SOC_SERIES_RZA3M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A3M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G066M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza3m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G066M04GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G066M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZA3UL"></a>

## 303.59 `CONFIG_SOC_SERIES_RZA3UL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A3UL 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G063U02GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza3ul/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3ul/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G063U02GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G063U02GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZG2L"></a>

## 303.60 `CONFIG_SOC_SERIES_RZG2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G044L23GBG
CONFIG_SOC_R9A07G044C22GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G044L23GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G044L23GBG)、[`CONFIG_SOC_R9A07G044C22GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G044C22GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZG2UL"></a>

## 303.61 `CONFIG_SOC_SERIES_RZG2UL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G2UL 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G043U11GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2ul/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2ul/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G043U11GBG`](P302_soc_renesas_配置项参考_1.md#CONFIG_SOC_R9A07G043U11GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZG3E"></a>

## 303.62 `CONFIG_SOC_SERIES_RZG3E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G3E 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G047E57GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3e/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3e/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A09G047E57GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G047E57GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZG3S"></a>

## 303.63 `CONFIG_SOC_SERIES_RZG3S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/G3S 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A08G045S33GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3s/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3s/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A08G045S33GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A08G045S33GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZN2H"></a>

## 303.64 `CONFIG_SOC_SERIES_RZN2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/N2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G087M44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A09G087M44GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G087M44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZN2L"></a>

## 303.65 `CONFIG_SOC_SERIES_RZN2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/N2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G084M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G084M04GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G084M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZT2H"></a>

## 303.66 `CONFIG_SOC_SERIES_RZT2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G077M44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A09G077M44GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G077M44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZT2L"></a>

## 303.67 `CONFIG_SOC_SERIES_RZT2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G074M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G074M04GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G074M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZT2M"></a>

## 303.68 `CONFIG_SOC_SERIES_RZT2M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/T2M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G075M24GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2m/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2m/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G075M24GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G075M24GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZV2H"></a>

## 303.69 `CONFIG_SOC_SERIES_RZV2H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2H 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G057H44GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A09G057H44GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G057H44GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZV2L"></a>

## 303.70 `CONFIG_SOC_SERIES_RZV2L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2L 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A07G054L23GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A07G054L23GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A07G054L23GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_SOC_SERIES_RZV2N"></a>

## 303.71 `CONFIG_SOC_SERIES_RZV2N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/V2N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
CONFIG_SOC_R9A09G056N48GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_R9A09G056N48GBG`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_R9A09G056N48GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_1"></a>

## 303.72 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_1`

**提示（Prompt）**：不分频（No division）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_128"></a>

## 303.73 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_128`

**提示（Prompt）**：128 分频（Divide-by-128）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_16"></a>

## 303.74 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_16`

**提示（Prompt）**：16 分频（Divide-by-16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_256"></a>

## 303.75 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_256`

**提示（Prompt）**：256 分频（Divide-by-256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_32"></a>

## 303.76 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_32`

**提示（Prompt）**：32 分频（Divide-by-32）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_64"></a>

## 303.77 `CONFIG_WDT_RENESAS_RX_OFS0_CLKDIV_64`

**提示（Prompt）**：64 分频（Divide-by-64）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗时钟分频比选择（IWDT Clock Divide Ratio Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_DIS"></a>

## 303.78 `CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_DIS`

**提示（Prompt）**：转换到睡眠模式（sleep mode）、软件待机模式（software standby mode）或深度睡眠模式（deep sleep mode）时，停止计数。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗睡眠模式计数停止控制（IWDT Sleep Mode Count Stop Control）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_ENA"></a>

## 303.79 `CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_ENA`

**提示（Prompt）**：禁用停止计数功能（Count stop is disabled）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗睡眠模式计数停止控制（IWDT Sleep Mode Count Stop Control）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IRQ_ENA"></a>

## 303.80 `CONFIG_WDT_RENESAS_RX_OFS0_IRQ_ENA`

**提示（Prompt）**：启用不可屏蔽中断请求输出（Non-maskable interrupt request output）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗复位／中断请求选择（IWDT Reset Interrupt Request Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDTSLCSTP"></a>

## 303.81 `CONFIG_WDT_RENESAS_RX_OFS0_IWDTSLCSTP`

**提示（Prompt）**：独立看门狗睡眠模式计数停止控制（IWDT Sleep Mode Count Stop Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDT_RENESAS_RX_IWDT_AUTO_START_MODE && CONFIG_SOC_SERIES_RX130 && CONFIG_SOC_FAMILY_RENESAS_RX
```

**默认值（Defaults）**

```text
0 if CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_DIS
1 if CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_ENA
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_WDT_RENESAS_RX_IWDT_AUTO_START_MODE`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WDT_RENESAS_RX_IWDT_AUTO_START_MODE)、[`CONFIG_SOC_SERIES_RX130`](P303_soc_renesas_配置项参考_2.md#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_DIS`](P303_soc_renesas_配置项参考_2.md#CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_DIS)、[`CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_ENA`](P303_soc_renesas_配置项参考_2.md#CONFIG_WDT_RENESAS_RX_OFS0_COUNT_STOP_ENA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_0"></a>

## 303.82 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_0`

**提示（Prompt）**：0%，不指定窗口结束位置（window end position）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口结束位置选择（IWDT Window End Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_25"></a>

## 303.83 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_25`

**提示（Prompt）**：百分之二十五（25%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口结束位置选择（IWDT Window End Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_50"></a>

## 303.84 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_50`

**提示（Prompt）**：百分之五十（50%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口结束位置选择（IWDT Window End Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_75"></a>

## 303.85 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_END_75`

**提示（Prompt）**：百分之七十五（75%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口结束位置选择（IWDT Window End Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_100"></a>

## 303.86 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_100`

**提示（Prompt）**：100%，不指定窗口开始位置（window start position）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口开始位置选择（IWDT Window Start Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_25"></a>

## 303.87 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_25`

**提示（Prompt）**：百分之二十五（25%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口开始位置选择（IWDT Window Start Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_50"></a>

## 303.88 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_50`

**提示（Prompt）**：百分之五十（50%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口开始位置选择（IWDT Window Start Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_75"></a>

## 303.89 `CONFIG_WDT_RENESAS_RX_OFS0_IWDT_WINDOW_STRT_75`

**提示（Prompt）**：百分之七十五（75%）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗窗口开始位置选择（IWDT Window Start Position Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_RESET_ENA"></a>

## 303.90 `CONFIG_WDT_RENESAS_RX_OFS0_RESET_ENA`

**提示（Prompt）**：启用复位输出（Reset output）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗复位／中断请求选择（IWDT Reset Interrupt Request Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_1024"></a>

## 303.91 `CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_1024`

**提示（Prompt）**：1024 个周期（1024 cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗超时周期选择（IWDT Timeout Period Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_128"></a>

## 303.92 `CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_128`

**提示（Prompt）**：128 个周期（128 cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗超时周期选择（IWDT Timeout Period Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_2048"></a>

## 303.93 `CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_2048`

**提示（Prompt）**：2048 个周期（2048 cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗超时周期选择（IWDT Timeout Period Select）

<a id="CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_512"></a>

## 303.94 `CONFIG_WDT_RENESAS_RX_OFS0_TIMEOUT_PERIOD_512`

**提示（Prompt）**：512 个周期（512 cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗超时周期选择（IWDT Timeout Period Select）

<a id="CONFIG_WDT_RENESAS_RX_STARTMODE_AUTO_ACTIVATE"></a>

## 303.95 `CONFIG_WDT_RENESAS_RX_STARTMODE_AUTO_ACTIVATE`

**提示（Prompt）**：复位后，独立看门狗（IWDT）以自动启动模式（auto-start mode）自动激活。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗 OFS0 启动模式选择（IWDT OFS0 Start Mode Select）

<a id="CONFIG_WDT_RENESAS_RX_STARTMODE_HALT"></a>

## 303.96 `CONFIG_WDT_RENESAS_RX_STARTMODE_HALT`

**提示（Prompt）**：复位后，独立看门狗（IWDT）停止运行。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 独立看门狗 OFS0 启动模式选择（IWDT OFS0 Start Mode Select）

<a id="SB_CONFIG_SOC_DA14695"></a>

## 303.97 `SB_CONFIG_SOC_DA14695`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14695 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_DA1469X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_DA14695_DK_USB
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_DA1469X`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_DA1469X)、[`SB_CONFIG_BOARD_DA14695_DK_USB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DA14695_DK_USB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_DA14695_DK_USB`。

<a id="SB_CONFIG_SOC_DA14697"></a>

## 303.98 `SB_CONFIG_SOC_DA14697`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14697 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_DA1469X
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_DA1469X`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_DA1469X)。

<a id="SB_CONFIG_SOC_DA14699"></a>

## 303.99 `SB_CONFIG_SOC_DA14699`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DA14699 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_DA1469X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_DA1469X_DK_PRO
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_DA1469X`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_DA1469X)、[`SB_CONFIG_BOARD_DA1469X_DK_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DA1469X_DK_PRO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_DA1469X_DK_PRO`。

<a id="SB_CONFIG_SOC_R5F51308AXFP"></a>

## 303.100 `SB_CONFIG_SOC_R5F51308AXFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51308AXFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX130
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RSK_RX130
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX130`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX130)、[`SB_CONFIG_BOARD_RSK_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RSK_RX130)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RSK_RX130`。

<!-- kconfig-navigation -->

[上一章](P302_soc_renesas_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P304_soc_renesas_配置项参考_3.md)
