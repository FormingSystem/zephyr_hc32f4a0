---
id: learning.zephyr-docs.kconfig-reference.page-267
title: "`soc/brcm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第267章\_`soc/brcm`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/brcm` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_BCM58400"></a>

## 267.1 `CONFIG_SOC_BCM58400`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58400 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_VALKYRIE
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BCM958401M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/valkyrie/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/valkyrie/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_VALKYRIE`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_SERIES_VALKYRIE)、[`CONFIG_BOARD_BCM958401M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BCM958401M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_BCM958401M2`。

<a id="CONFIG_SOC_BCM58402_A72"></a>

## 267.2 `CONFIG_SOC_BCM58402_A72`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58402 A72 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_VIPER
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BCM958402M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_VIPER`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_SERIES_VIPER)、[`CONFIG_BOARD_BCM958402M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BCM958402M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_BCM958402M2`。

<a id="CONFIG_SOC_BCM58402_M7"></a>

## 267.3 `CONFIG_SOC_BCM58402_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58402 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_VIPER
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BCM958402M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_VIPER`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_SERIES_VIPER)、[`CONFIG_BOARD_BCM958402M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BCM958402M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_BCM958402M2`。

<a id="CONFIG_SOC_SERIES_VALKYRIE"></a>

## 267.4 `CONFIG_SOC_SERIES_VALKYRIE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Broadcom Valkyrie 系列支持（Series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BCMVK
```

**被选择（Selected by）**

```text
CONFIG_SOC_BCM58400
```

**定义位置（Location）**：[`soc/brcm/bcmvk/valkyrie/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/valkyrie/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BCMVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BCMVK)、[`CONFIG_SOC_BCM58400`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_BCM58400)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BCMVK`。

<a id="CONFIG_SOC_SERIES_VIPER"></a>

## 267.5 `CONFIG_SOC_SERIES_VIPER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Broadcom Viper 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_BCMVK
```

**被选择（Selected by）**

```text
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_BCM58402_A72
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_BCMVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_BCMVK)、[`CONFIG_SOC_BCM58402_M7`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_BCM58402_A72`](P267_soc_brcm_配置项参考.md#CONFIG_SOC_BCM58402_A72)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_BCMVK`。

<a id="SB_CONFIG_SOC_BCM58400"></a>

## 267.6 `SB_CONFIG_SOC_BCM58400`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58400 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_VALKYRIE
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BCM958401M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/valkyrie/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/valkyrie/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_VALKYRIE`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_SERIES_VALKYRIE)、[`SB_CONFIG_BOARD_BCM958401M2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BCM958401M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_BCM958401M2`。

<a id="SB_CONFIG_SOC_BCM58402_A72"></a>

## 267.7 `SB_CONFIG_SOC_BCM58402_A72`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58402 A72 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_VIPER
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BCM958402M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_VIPER`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_SERIES_VIPER)、[`SB_CONFIG_BOARD_BCM958402M2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BCM958402M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_BCM958402M2`。

<a id="SB_CONFIG_SOC_BCM58402_M7"></a>

## 267.8 `SB_CONFIG_SOC_BCM58402_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Broadcom BCM58402 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_VIPER
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BCM958402M2
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_VIPER`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_SERIES_VIPER)、[`SB_CONFIG_BOARD_BCM958402M2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BCM958402M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_BCM958402M2`。

<a id="SB_CONFIG_SOC_SERIES_VALKYRIE"></a>

## 267.9 `SB_CONFIG_SOC_SERIES_VALKYRIE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Broadcom Valkyrie 系列支持（Series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BCMVK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BCM58400
```

**定义位置（Location）**：[`soc/brcm/bcmvk/valkyrie/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/valkyrie/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BCMVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BCMVK)、[`SB_CONFIG_SOC_BCM58400`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_BCM58400)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BCMVK`。

<a id="SB_CONFIG_SOC_SERIES_VIPER"></a>

## 267.10 `SB_CONFIG_SOC_SERIES_VIPER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Broadcom Viper 系列支持（Series support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_BCMVK
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BCM58402_M7
SB_CONFIG_SOC_BCM58402_A72
```

**定义位置（Location）**：[`soc/brcm/bcmvk/viper/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/brcm/bcmvk/viper/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_BCMVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_BCMVK)、[`SB_CONFIG_SOC_BCM58402_M7`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_BCM58402_M7)、[`SB_CONFIG_SOC_BCM58402_A72`](P267_soc_brcm_配置项参考.md#SB_CONFIG_SOC_BCM58402_A72)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_BCMVK`。

<!-- kconfig-navigation -->

[上一章](P266_soc_bflb_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P268_soc_cdac_配置项参考.md)
