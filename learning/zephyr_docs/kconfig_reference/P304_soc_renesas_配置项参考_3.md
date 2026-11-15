---
id: learning.zephyr-docs.kconfig-reference.page-304
title: "`soc/renesas`配置项参考（3/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第304章\_`soc/renesas`配置项参考（3/4）

本章翻译官方 Kconfig 数据库中 `soc/renesas` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="SB_CONFIG_SOC_R5F51406BDFN"></a>

## 304.1 `SB_CONFIG_SOC_R5F51406BDFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51406BDFN`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX140
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RSK_RX140
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX140`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX140)、[`SB_CONFIG_BOARD_RSK_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RSK_RX140)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RSK_RX140`。

<a id="SB_CONFIG_SOC_R5F51406BGFN"></a>

## 304.2 `SB_CONFIG_SOC_R5F51406BGFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F51406BGFN`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX140
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RX140
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX140`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX140)、[`SB_CONFIG_BOARD_FPB_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RX140)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RX140`。

<a id="SB_CONFIG_SOC_R5F514T5AMFM"></a>

## 304.3 `SB_CONFIG_SOC_R5F514T5AMFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`SOC_R5F514T5AMFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX14T
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MCB_RX14T
SB_CONFIG_BOARD_FPB_RX14T
```

**定义位置（Location）**：[`soc/renesas/rx/rx14t/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx14t/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX14T`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX14T)、[`SB_CONFIG_BOARD_MCB_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MCB_RX14T)、[`SB_CONFIG_BOARD_FPB_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RX14T)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MCB_RX14T`、`SB_CONFIG_BOARD_FPB_RX14T`。

<a id="SB_CONFIG_SOC_R5F52618BGFP"></a>

## 304.4 `SB_CONFIG_SOC_R5F52618BGFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R5F52618BGFP 微控制器片上系统（microcontroller SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX261
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RX261
SB_CONFIG_BOARD_EK_RX261
```

**定义位置（Location）**：[`soc/renesas/rx/rx261/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx261/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX261`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX261)、[`SB_CONFIG_BOARD_FPB_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RX261)、[`SB_CONFIG_BOARD_EK_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RX261)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RX261`、`SB_CONFIG_BOARD_EK_RX261`。

<a id="SB_CONFIG_SOC_R5F526TFDDFP"></a>

## 304.5 `SB_CONFIG_SOC_R5F526TFDDFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`SOC_R5F526TFDDFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX26T
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MCB_RX26T
```

**定义位置（Location）**：[`soc/renesas/rx/rx26t/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx26t/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX26T`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX26T)、[`SB_CONFIG_BOARD_MCB_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MCB_RX26T)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MCB_RX26T`。

<a id="SB_CONFIG_SOC_R5F562N8"></a>

## 304.6 `SB_CONFIG_SOC_R5F562N8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5F562N8`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX62N
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_QEMU_RX
```

**定义位置（Location）**：[`soc/renesas/rx/rx62n/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx62n/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX62N`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX62N)、[`SB_CONFIG_BOARD_QEMU_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_QEMU_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_QEMU_RX`。

<a id="SB_CONFIG_SOC_R5K574MCB4AE"></a>

## 304.7 `SB_CONFIG_SOC_R5K574MCB4AE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5K574MCB4AE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX74M
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RX74M
```

**定义位置（Location）**：[`soc/renesas/rx/rx74m/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74m/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX74M`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX74M)、[`SB_CONFIG_BOARD_EK_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RX74M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RX74M`。

<a id="SB_CONFIG_SOC_R5K574NCB4AE"></a>

## 304.8 `SB_CONFIG_SOC_R5K574NCB4AE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R5K574NCB4AE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RX74N
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RX74N
```

**定义位置（Location）**：[`soc/renesas/rx/rx74n/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74n/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RX74N`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RX74N)、[`SB_CONFIG_BOARD_EK_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RX74N)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RX74N`。

<a id="SB_CONFIG_SOC_R7FA2A1AB3CFM"></a>

## 304.9 `SB_CONFIG_SOC_R7FA2A1AB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA2A1AB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA2A1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA2A1
```

**定义位置（Location）**：[`soc/renesas/ra/ra2a1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2a1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA2A1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA2A1)、[`SB_CONFIG_BOARD_EK_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA2A1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA2A1`。

<a id="SB_CONFIG_SOC_R7FA4C1BD3CFP"></a>

## 304.10 `SB_CONFIG_SOC_R7FA4C1BD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4C1BD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4C1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4C1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4c1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4c1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4C1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4C1)、[`SB_CONFIG_BOARD_EK_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4C1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4C1`。

<a id="SB_CONFIG_SOC_R7FA4E10D2CFM"></a>

## 304.11 `SB_CONFIG_SOC_R7FA4E10D2CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E10D2CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4E1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RA4E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4E1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4E1)、[`SB_CONFIG_BOARD_FPB_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RA4E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RA4E1`。

<a id="SB_CONFIG_SOC_R7FA4E10D2CNE"></a>

## 304.12 `SB_CONFIG_SOC_R7FA4E10D2CNE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E10D2CNE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4E1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VOICE_RA4E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4E1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4E1)、[`SB_CONFIG_BOARD_VOICE_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VOICE_RA4E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_VOICE_RA4E1`。

<a id="SB_CONFIG_SOC_R7FA4E2B93CFM"></a>

## 304.13 `SB_CONFIG_SOC_R7FA4E2B93CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4E2B93CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4E2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4E2
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4E2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4E2)、[`SB_CONFIG_BOARD_EK_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4E2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4E2`。

<a id="SB_CONFIG_SOC_R7FA4L1BD4CFP"></a>

## 304.14 `SB_CONFIG_SOC_R7FA4L1BD4CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4L1BD4CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4L1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4L1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4l1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4l1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4L1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4L1)、[`SB_CONFIG_BOARD_EK_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4L1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4L1`。

<a id="SB_CONFIG_SOC_R7FA4M1AB3CFM"></a>

## 304.15 `SB_CONFIG_SOC_R7FA4M1AB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ARDUINO_UNO_R4
SB_CONFIG_BOARD_ARDUINO_NANO_R4
SB_CONFIG_BOARD_MIKROE_CLICKER_RA4M1
SB_CONFIG_BOARD_WEACT_RA4M1_CORE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4M1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4M1)、[`SB_CONFIG_BOARD_ARDUINO_UNO_R4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARDUINO_UNO_R4)、[`SB_CONFIG_BOARD_ARDUINO_NANO_R4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARDUINO_NANO_R4)、[`SB_CONFIG_BOARD_MIKROE_CLICKER_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MIKROE_CLICKER_RA4M1)、[`SB_CONFIG_BOARD_WEACT_RA4M1_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_RA4M1_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ARDUINO_UNO_R4`、`SB_CONFIG_BOARD_ARDUINO_NANO_R4`、`SB_CONFIG_BOARD_MIKROE_CLICKER_RA4M1`、`SB_CONFIG_BOARD_WEACT_RA4M1_CORE`。

<a id="SB_CONFIG_SOC_R7FA4M1AB3CFP"></a>

## 304.16 `SB_CONFIG_SOC_R7FA4M1AB3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4M1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4M1)、[`SB_CONFIG_BOARD_EK_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4M1`。

<a id="SB_CONFIG_SOC_R7FA4M1AB3CNE"></a>

## 304.17 `SB_CONFIG_SOC_R7FA4M1AB3CNE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M1AB3CNE`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_XIAO_RA4M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4M1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4M1)、[`SB_CONFIG_BOARD_XIAO_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_RA4M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_XIAO_RA4M1`。

<a id="SB_CONFIG_SOC_R7FA4M2AD3CFP"></a>

## 304.18 `SB_CONFIG_SOC_R7FA4M2AD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M2AD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4M2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4M2
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4M2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4M2)、[`SB_CONFIG_BOARD_EK_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4M2`。

<a id="SB_CONFIG_SOC_R7FA4M3AF3CFB"></a>

## 304.19 `SB_CONFIG_SOC_R7FA4M3AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4M3AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4M3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4M3`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4M3)、[`SB_CONFIG_BOARD_EK_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4M3`。

<a id="SB_CONFIG_SOC_R7FA4W1AD2CNG"></a>

## 304.20 `SB_CONFIG_SOC_R7FA4W1AD2CNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA4W1AD2CNG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA4W1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA4W1
```

**定义位置（Location）**：[`soc/renesas/ra/ra4w1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4w1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA4W1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA4W1)、[`SB_CONFIG_BOARD_EK_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA4W1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA4W1`。

<a id="SB_CONFIG_SOC_R7FA6E10F2CFP"></a>

## 304.21 `SB_CONFIG_SOC_R7FA6E10F2CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6E10F2CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6E1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RA6E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6E1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6E1)、[`SB_CONFIG_BOARD_FPB_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RA6E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RA6E1`。

<a id="SB_CONFIG_SOC_R7FA6E2BB3CFM"></a>

## 304.22 `SB_CONFIG_SOC_R7FA6E2BB3CFM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6E2BB3CFM`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6E2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RA6E2
SB_CONFIG_BOARD_EK_RA6E2
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6E2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6E2)、[`SB_CONFIG_BOARD_FPB_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RA6E2)、[`SB_CONFIG_BOARD_EK_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6E2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RA6E2`、`SB_CONFIG_BOARD_EK_RA6E2`。

<a id="SB_CONFIG_SOC_R7FA6M1AD3CFP"></a>

## 304.23 `SB_CONFIG_SOC_R7FA6M1AD3CFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M1AD3CFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA6M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M1)、[`SB_CONFIG_BOARD_EK_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA6M1`。

<a id="SB_CONFIG_SOC_R7FA6M2AF3CFB"></a>

## 304.24 `SB_CONFIG_SOC_R7FA6M2AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M2AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA6M2
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M2)、[`SB_CONFIG_BOARD_EK_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6M2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA6M2`。

<a id="SB_CONFIG_SOC_R7FA6M3AF2CBG"></a>

## 304.25 `SB_CONFIG_SOC_R7FA6M3AF2CBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M3AF2CBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M3`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M3)。

<a id="SB_CONFIG_SOC_R7FA6M3AH3CFC"></a>

## 304.26 `SB_CONFIG_SOC_R7FA6M3AH3CFC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M3AH3CFC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA6M3
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M3`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M3)、[`SB_CONFIG_BOARD_EK_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA6M3`。

<a id="SB_CONFIG_SOC_R7FA6M4AF3CFB"></a>

## 304.27 `SB_CONFIG_SOC_R7FA6M4AF3CFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M4AF3CFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA6M4
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m4/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m4/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M4`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M4)、[`SB_CONFIG_BOARD_EK_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6M4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA6M4`。

<a id="SB_CONFIG_SOC_R7FA6M5BH3CFC"></a>

## 304.28 `SB_CONFIG_SOC_R7FA6M5BH3CFC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA6M5BH3CFC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA6M5
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ARDUINO_PORTENTA_C33
SB_CONFIG_BOARD_EK_RA6M5
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA6M5`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA6M5)、[`SB_CONFIG_BOARD_ARDUINO_PORTENTA_C33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARDUINO_PORTENTA_C33)、[`SB_CONFIG_BOARD_EK_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA6M5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ARDUINO_PORTENTA_C33`、`SB_CONFIG_BOARD_EK_RA6M5`。

<a id="SB_CONFIG_SOC_R7FA8D1BHECBD"></a>

## 304.29 `SB_CONFIG_SOC_R7FA8D1BHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8D1BHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8D1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RA8D1_VISION_BOARD
SB_CONFIG_BOARD_EK_RA8D1
SB_CONFIG_BOARD_CPKCOR_RA8D1B
SB_CONFIG_BOARD_AIK_RA8D1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8D1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8D1)、[`SB_CONFIG_BOARD_RA8D1_VISION_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RA8D1_VISION_BOARD)、[`SB_CONFIG_BOARD_EK_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA8D1)、[`SB_CONFIG_BOARD_CPKCOR_RA8D1B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CPKCOR_RA8D1B)、[`SB_CONFIG_BOARD_AIK_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_AIK_RA8D1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RA8D1_VISION_BOARD`、`SB_CONFIG_BOARD_EK_RA8D1`、`SB_CONFIG_BOARD_CPKCOR_RA8D1B`、`SB_CONFIG_BOARD_AIK_RA8D1`。

<a id="SB_CONFIG_SOC_R7FA8E1AFDCFB"></a>

## 304.30 `SB_CONFIG_SOC_R7FA8E1AFDCFB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8E1AFDCFB`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8E1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FPB_RA8E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8E1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8E1)、[`SB_CONFIG_BOARD_FPB_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FPB_RA8E1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_FPB_RA8E1`。

<a id="SB_CONFIG_SOC_R7FA8E1AFDCFP"></a>

## 304.31 `SB_CONFIG_SOC_R7FA8E1AFDCFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8E1AFDCFP`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8E1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8E1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8E1)。

<a id="SB_CONFIG_SOC_R7FA8M1AHECBD"></a>

## 304.32 `SB_CONFIG_SOC_R7FA8M1AHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8M1AHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8M1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EK_RA8M1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8M1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8M1)、[`SB_CONFIG_BOARD_EK_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EK_RA8M1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EK_RA8M1`。

<a id="SB_CONFIG_SOC_R7FA8T1AHECBD"></a>

## 304.33 `SB_CONFIG_SOC_R7FA8T1AHECBD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7FA8T1AHECBD`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8T1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MCK_RA8T1
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t1/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t1/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8T1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8T1)、[`SB_CONFIG_BOARD_MCK_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MCK_RA8T1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MCK_RA8T1`。

<a id="SB_CONFIG_SOC_R7KA8D2KFLCAC"></a>

## 304.34 `SB_CONFIG_SOC_R7KA8D2KFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8D2KFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8D2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8D2KFLCAC_CM85
SB_CONFIG_SOC_R7KA8D2KFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8D2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8D2)、[`SB_CONFIG_SOC_R7KA8D2KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8D2KFLCAC_CM85)、[`SB_CONFIG_SOC_R7KA8D2KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8D2KFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R7KA8D2KFLCAC_CM85`、`SB_CONFIG_SOC_R7KA8D2KFLCAC_CM33`。

<a id="SB_CONFIG_SOC_R7KA8M2JFLCAC"></a>

## 304.35 `SB_CONFIG_SOC_R7KA8M2JFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8M2JFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8M2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8M2JFLCAC_CM85
SB_CONFIG_SOC_R7KA8M2JFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8M2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8M2)、[`SB_CONFIG_SOC_R7KA8M2JFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8M2JFLCAC_CM85)、[`SB_CONFIG_SOC_R7KA8M2JFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8M2JFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R7KA8M2JFLCAC_CM85`、`SB_CONFIG_SOC_R7KA8M2JFLCAC_CM33`。

<a id="SB_CONFIG_SOC_R7KA8P1KFLCAC"></a>

## 304.36 `SB_CONFIG_SOC_R7KA8P1KFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8P1KFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8P1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8P1KFLCAC_CM85
SB_CONFIG_SOC_R7KA8P1KFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8P1`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8P1)、[`SB_CONFIG_SOC_R7KA8P1KFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8P1KFLCAC_CM85)、[`SB_CONFIG_SOC_R7KA8P1KFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8P1KFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R7KA8P1KFLCAC_CM85`、`SB_CONFIG_SOC_R7KA8P1KFLCAC_CM33`。

<a id="SB_CONFIG_SOC_R7KA8T2LFLCAC"></a>

## 304.37 `SB_CONFIG_SOC_R7KA8T2LFLCAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7KA8T2LFLCAC`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RA8T2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8T2LFLCAC_CM85
SB_CONFIG_SOC_R7KA8T2LFLCAC_CM33
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RA8T2`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RA8T2)、[`SB_CONFIG_SOC_R7KA8T2LFLCAC_CM85`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8T2LFLCAC_CM85)、[`SB_CONFIG_SOC_R7KA8T2LFLCAC_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7KA8T2LFLCAC_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R7KA8T2LFLCAC_CM85`、`SB_CONFIG_SOC_R7KA8T2LFLCAC_CM33`。

<a id="SB_CONFIG_SOC_R7S921053VCBG"></a>

## 304.38 `SB_CONFIG_SOC_R7S921053VCBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R7S921053VCBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZA2M
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZA2M_EVK
SB_CONFIG_SOC_R7S921053VCBG_CA9
```

**定义位置（Location）**：[`soc/renesas/rz/rza2m/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza2m/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZA2M`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RZA2M)、[`SB_CONFIG_BOARD_RZA2M_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZA2M_EVK)、[`SB_CONFIG_SOC_R7S921053VCBG_CA9`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7S921053VCBG_CA9)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZA2M_EVK`、`SB_CONFIG_SOC_R7S921053VCBG_CA9`。

<a id="SB_CONFIG_SOC_R8A77951_A57"></a>

## 304.39 `SB_CONFIG_SOC_R8A77951_A57`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R8A77951 A57 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_H3ULCB
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_RCAR_GEN3)、[`SB_CONFIG_BOARD_RCAR_H3ULCB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_H3ULCB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_RCAR_GEN3`、`SB_CONFIG_BOARD_RCAR_H3ULCB`。

<a id="SB_CONFIG_SOC_R8A77951_R7"></a>

## 304.40 `SB_CONFIG_SOC_R8A77951_R7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R8A77951 R7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_SALVATOR_X
SB_CONFIG_BOARD_RCAR_H3ULCB
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_RCAR_GEN3)、[`SB_CONFIG_BOARD_RCAR_SALVATOR_X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_SALVATOR_X)、[`SB_CONFIG_BOARD_RCAR_H3ULCB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_H3ULCB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_RCAR_GEN3`、`SB_CONFIG_BOARD_RCAR_SALVATOR_X`、`SB_CONFIG_BOARD_RCAR_H3ULCB`。

<a id="SB_CONFIG_SOC_R8A77961"></a>

## 304.41 `SB_CONFIG_SOC_R8A77961`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R8A77961`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_SALVATOR_XS
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen3/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen3/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_RCAR_GEN3)、[`SB_CONFIG_BOARD_RCAR_SALVATOR_XS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_SALVATOR_XS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_RCAR_GEN3`、`SB_CONFIG_BOARD_RCAR_SALVATOR_XS`。

<a id="SB_CONFIG_SOC_R8A779F0_A55"></a>

## 304.42 `SB_CONFIG_SOC_R8A779F0_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

r8a779f0 a55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_SPIDER_S4
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen4/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen4/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_RCAR_GEN4)、[`SB_CONFIG_BOARD_RCAR_SPIDER_S4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_SPIDER_S4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_RCAR_GEN4`、`SB_CONFIG_BOARD_RCAR_SPIDER_S4`。

<a id="SB_CONFIG_SOC_R8A779F0_R52"></a>

## 304.43 `SB_CONFIG_SOC_R8A779F0_R52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

r8a779f0 r52 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_SPIDER_S4
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen4/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen4/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_RCAR_GEN4)、[`SB_CONFIG_BOARD_RCAR_SPIDER_S4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_SPIDER_S4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_RCAR_GEN4`、`SB_CONFIG_BOARD_RCAR_SPIDER_S4`。

<a id="SB_CONFIG_SOC_R8A78000_A720"></a>

## 304.44 `SB_CONFIG_SOC_R8A78000_A720`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持 R8A78000 A720 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN5
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN5`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RCAR_GEN5)、[`SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H`。

<a id="SB_CONFIG_SOC_R8A78000_R52"></a>

## 304.45 `SB_CONFIG_SOC_R8A78000_R52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持 R8A78000 R52 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RCAR_GEN5
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RCAR_GEN5`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RCAR_GEN5)、[`SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RCAR_IRONHIDE_X5H`。

<a id="SB_CONFIG_SOC_R9A07G043U11GBG"></a>

## 304.46 `SB_CONFIG_SOC_R9A07G043U11GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G043U11GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZG2UL
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZG2UL_SMARC
SB_CONFIG_SOC_R9A07G043U11GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2ul/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2ul/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZG2UL`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZG2UL)、[`SB_CONFIG_BOARD_RZG2UL_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZG2UL_SMARC)、[`SB_CONFIG_SOC_R9A07G043U11GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A07G043U11GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZG2UL_SMARC`、`SB_CONFIG_SOC_R9A07G043U11GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A07G044C22GBG"></a>

## 304.47 `SB_CONFIG_SOC_R9A07G044C22GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G044C22GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZG2L
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZG2LC_SMARC
SB_CONFIG_SOC_R9A07G044C22GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZG2L`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZG2L)、[`SB_CONFIG_BOARD_RZG2LC_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZG2LC_SMARC)、[`SB_CONFIG_SOC_R9A07G044C22GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A07G044C22GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZG2LC_SMARC`、`SB_CONFIG_SOC_R9A07G044C22GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A07G044L23GBG"></a>

## 304.48 `SB_CONFIG_SOC_R9A07G044L23GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G044L23GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZG2L
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZG2L_SMARC
SB_CONFIG_SOC_R9A07G044L23GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZG2L`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZG2L)、[`SB_CONFIG_BOARD_RZG2L_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZG2L_SMARC)、[`SB_CONFIG_SOC_R9A07G044L23GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A07G044L23GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZG2L_SMARC`、`SB_CONFIG_SOC_R9A07G044L23GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A07G054L23GBG"></a>

## 304.49 `SB_CONFIG_SOC_R9A07G054L23GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G054L23GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZV2L
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZV2L_SMARC
SB_CONFIG_SOC_R9A07G054L23GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZV2L`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZV2L)、[`SB_CONFIG_BOARD_RZV2L_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZV2L_SMARC)、[`SB_CONFIG_SOC_R9A07G054L23GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A07G054L23GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZV2L_SMARC`、`SB_CONFIG_SOC_R9A07G054L23GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A07G063U02GBG"></a>

## 304.50 `SB_CONFIG_SOC_R9A07G063U02GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G063U02GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZA3UL
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZA3UL_SMARC
```

**定义位置（Location）**：[`soc/renesas/rz/rza3ul/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3ul/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZA3UL`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZA3UL)、[`SB_CONFIG_BOARD_RZA3UL_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZA3UL_SMARC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZA3UL_SMARC`。

<a id="SB_CONFIG_SOC_R9A07G066M04GBG"></a>

## 304.51 `SB_CONFIG_SOC_R9A07G066M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G066M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZA3M
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZA3M_EK
```

**定义位置（Location）**：[`soc/renesas/rz/rza3m/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3m/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZA3M`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_SERIES_RZA3M)、[`SB_CONFIG_BOARD_RZA3M_EK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZA3M_EK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZA3M_EK`。

<a id="SB_CONFIG_SOC_R9A07G074M04GBG"></a>

## 304.52 `SB_CONFIG_SOC_R9A07G074M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G074M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZT2L
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZT2L_RSK
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZT2L`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZT2L)、[`SB_CONFIG_BOARD_RZT2L_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZT2L_RSK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZT2L_RSK`。

<a id="SB_CONFIG_SOC_R9A07G075M24GBG"></a>

## 304.53 `SB_CONFIG_SOC_R9A07G075M24GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G075M24GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZT2M
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZT2M_RSK
SB_CONFIG_SOC_R9A07G075M24GBG_CR520
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2m/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2m/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZT2M`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZT2M)、[`SB_CONFIG_BOARD_RZT2M_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZT2M_RSK)、[`SB_CONFIG_SOC_R9A07G075M24GBG_CR520`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A07G075M24GBG_CR520)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZT2M_RSK`、`SB_CONFIG_SOC_R9A07G075M24GBG_CR520`。

<a id="SB_CONFIG_SOC_R9A07G084M04GBG"></a>

## 304.54 `SB_CONFIG_SOC_R9A07G084M04GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A07G084M04GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZN2L
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZN2L_RSK
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2l/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2l/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZN2L`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZN2L)、[`SB_CONFIG_BOARD_RZN2L_RSK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZN2L_RSK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZN2L_RSK`。

<a id="SB_CONFIG_SOC_R9A08G045S33GBG"></a>

## 304.55 `SB_CONFIG_SOC_R9A08G045S33GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A08G045S33GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZG3S
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZG3S_SMARC
SB_CONFIG_SOC_R9A08G045S33GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3s/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3s/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZG3S`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZG3S)、[`SB_CONFIG_BOARD_RZG3S_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZG3S_SMARC)、[`SB_CONFIG_SOC_R9A08G045S33GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A08G045S33GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZG3S_SMARC`、`SB_CONFIG_SOC_R9A08G045S33GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A09G047E57GBG"></a>

## 304.56 `SB_CONFIG_SOC_R9A09G047E57GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G047E57GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZG3E
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZG3E_SMARC
SB_CONFIG_SOC_R9A09G047E57GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzg3e/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzg3e/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZG3E`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZG3E)、[`SB_CONFIG_BOARD_RZG3E_SMARC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZG3E_SMARC)、[`SB_CONFIG_SOC_R9A09G047E57GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A09G047E57GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZG3E_SMARC`、`SB_CONFIG_SOC_R9A09G047E57GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A09G056N48GBG"></a>

## 304.57 `SB_CONFIG_SOC_R9A09G056N48GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G056N48GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZV2N
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G056N48GBG_CM33
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2n/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2n/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZV2N`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZV2N)、[`SB_CONFIG_SOC_R9A09G056N48GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A09G056N48GBG_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R9A09G056N48GBG_CM33`。

<a id="SB_CONFIG_SOC_R9A09G057H44GBG"></a>

## 304.58 `SB_CONFIG_SOC_R9A09G057H44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G057H44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZV2H
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G057H44GBG_CM33
SB_CONFIG_SOC_R9A09G057H44GBG_CR8
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZV2H`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZV2H)、[`SB_CONFIG_SOC_R9A09G057H44GBG_CM33`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G057H44GBG_CM33)、[`SB_CONFIG_SOC_R9A09G057H44GBG_CR8`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G057H44GBG_CR8)。

<a id="SB_CONFIG_SOC_R9A09G057H44GBG_CM33"></a>

## 304.59 `SB_CONFIG_SOC_R9A09G057H44GBG_CM33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RZ/V2H CM33 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_R9A09G057H44GBG
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZV2H_EVK
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_R9A09G057H44GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G057H44GBG)、[`SB_CONFIG_BOARD_RZV2H_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZV2H_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZV2H_EVK`。

<a id="SB_CONFIG_SOC_R9A09G057H44GBG_CR8"></a>

## 304.60 `SB_CONFIG_SOC_R9A09G057H44GBG_CR8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RZ/V2H CR8 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_R9A09G057H44GBG
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZV2H_EVK
```

**定义位置（Location）**：[`soc/renesas/rz/rzv2h/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzv2h/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_R9A09G057H44GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A09G057H44GBG)、[`SB_CONFIG_BOARD_RZV2H_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZV2H_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZV2H_EVK`。

<a id="SB_CONFIG_SOC_R9A09G077M44GBG"></a>

## 304.61 `SB_CONFIG_SOC_R9A09G077M44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G077M44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZT2H
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_RZT2H_EVB
```

**定义位置（Location）**：[`soc/renesas/rz/rzt2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzt2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZT2H`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZT2H)、[`SB_CONFIG_BOARD_RZT2H_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RZT2H_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_RZT2H_EVB`。

<a id="SB_CONFIG_SOC_R9A09G087M44GBG"></a>

## 304.62 `SB_CONFIG_SOC_R9A09G087M44GBG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统型号（SoC part number）：`R9A09G087M44GBG`

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RZN2H
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A09G087M44GBG_CR52_0
```

**定义位置（Location）**：[`soc/renesas/rz/rzn2h/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rzn2h/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RZN2H`](P305_soc_renesas_配置项参考_4.md#SB_CONFIG_SOC_SERIES_RZN2H)、[`SB_CONFIG_SOC_R9A09G087M44GBG_CR52_0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R9A09G087M44GBG_CR52_0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_R9A09G087M44GBG_CR52_0`。

<a id="SB_CONFIG_SOC_SERIES_DA1469X"></a>

## 304.63 `SB_CONFIG_SOC_SERIES_DA1469X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨 SmartBond™ DA1469x 系列微控制器（Renesas series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_SMARTBOND
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_DA14695
SB_CONFIG_SOC_DA14697
SB_CONFIG_SOC_DA14699
```

**定义位置（Location）**：[`soc/renesas/smartbond/da1469x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/smartbond/da1469x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_SMARTBOND)、[`SB_CONFIG_SOC_DA14695`](P303_soc_renesas_配置项参考_2.md#SB_CONFIG_SOC_DA14695)、[`SB_CONFIG_SOC_DA14697`](P303_soc_renesas_配置项参考_2.md#SB_CONFIG_SOC_DA14697)、[`SB_CONFIG_SOC_DA14699`](P303_soc_renesas_配置项参考_2.md#SB_CONFIG_SOC_DA14699)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`。

<a id="SB_CONFIG_SOC_SERIES_RA0E1"></a>

## 304.64 `SB_CONFIG_SOC_SERIES_RA0E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA0E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA0E1073CFJ
SB_CONFIG_SOC_R7FA0E1073CNH
SB_CONFIG_SOC_R7FA0E1073CNK
SB_CONFIG_SOC_R7FA0E1073CSC
SB_CONFIG_SOC_R7FA0E1073CSD
SB_CONFIG_SOC_R7FA0E1073CNL
SB_CONFIG_SOC_R7FA0E1053CFJ
SB_CONFIG_SOC_R7FA0E1053CNH
SB_CONFIG_SOC_R7FA0E1053CNK
SB_CONFIG_SOC_R7FA0E1053CSC
SB_CONFIG_SOC_R7FA0E1053CNL
```

**定义位置（Location）**：[`soc/renesas/ra/ra0e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra0e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA0E1073CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CFJ)、[`SB_CONFIG_SOC_R7FA0E1073CNH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CNH)、[`SB_CONFIG_SOC_R7FA0E1073CNK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CNK)、[`SB_CONFIG_SOC_R7FA0E1073CSC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CSC)、[`SB_CONFIG_SOC_R7FA0E1073CSD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CSD)、[`SB_CONFIG_SOC_R7FA0E1073CNL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1073CNL)、[`SB_CONFIG_SOC_R7FA0E1053CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1053CFJ)、[`SB_CONFIG_SOC_R7FA0E1053CNH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1053CNH)、[`SB_CONFIG_SOC_R7FA0E1053CNK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1053CNK)、[`SB_CONFIG_SOC_R7FA0E1053CSC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1053CSC)、[`SB_CONFIG_SOC_R7FA0E1053CNL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA0E1053CNL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`、`SB_CONFIG_SOC_R7FA0E1073CFJ`、`SB_CONFIG_SOC_R7FA0E1073CNH`、`SB_CONFIG_SOC_R7FA0E1073CNK`、`SB_CONFIG_SOC_R7FA0E1073CSC`、`SB_CONFIG_SOC_R7FA0E1073CSD`、`SB_CONFIG_SOC_R7FA0E1073CNL`、`SB_CONFIG_SOC_R7FA0E1053CFJ`、`SB_CONFIG_SOC_R7FA0E1053CNH`、`SB_CONFIG_SOC_R7FA0E1053CNK`、`SB_CONFIG_SOC_R7FA0E1053CSC`、`SB_CONFIG_SOC_R7FA0E1053CNL`。

<a id="SB_CONFIG_SOC_SERIES_RA2A1"></a>

## 304.65 `SB_CONFIG_SOC_SERIES_RA2A1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA2A1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA2A1AB3CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra2a1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra2a1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA2A1AB3CFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA2A1AB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4C1"></a>

## 304.66 `SB_CONFIG_SOC_SERIES_RA4C1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4C1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4C1BD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4c1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4c1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4C1BD3CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4C1BD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4E1"></a>

## 304.67 `SB_CONFIG_SOC_SERIES_RA4E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4E10D2CFM
SB_CONFIG_SOC_R7FA4E10D2CNE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4E10D2CFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4E10D2CFM)、[`SB_CONFIG_SOC_R7FA4E10D2CNE`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4E10D2CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4E2"></a>

## 304.68 `SB_CONFIG_SOC_SERIES_RA4E2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4E2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4E2B93CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra4e2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4e2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4E2B93CFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4E2B93CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4L1"></a>

## 304.69 `SB_CONFIG_SOC_SERIES_RA4L1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4L1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4L1BD4CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4l1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4l1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4L1BD4CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4L1BD4CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4M1"></a>

## 304.70 `SB_CONFIG_SOC_SERIES_RA4M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4M1AB3CFM
SB_CONFIG_SOC_R7FA4M1AB3CFP
SB_CONFIG_SOC_R7FA4M1AB3CNE
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4M1AB3CFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4M1AB3CFM)、[`SB_CONFIG_SOC_R7FA4M1AB3CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4M1AB3CFP)、[`SB_CONFIG_SOC_R7FA4M1AB3CNE`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4M1AB3CNE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4M2"></a>

## 304.71 `SB_CONFIG_SOC_SERIES_RA4M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4M2AD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4M2AD3CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4M2AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4M3"></a>

## 304.72 `SB_CONFIG_SOC_SERIES_RA4M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4M3 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4M3AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra4m3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4m3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4M3AF3CFB`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4M3AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA4T1"></a>

## 304.73 `SB_CONFIG_SOC_SERIES_RA4T1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4T1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4T1BB3CFM
SB_CONFIG_SOC_R7FA4T1BB3CFL
SB_CONFIG_SOC_R7FA4T1BB3CFJ
SB_CONFIG_SOC_R7FA4T1BB3CNE
SB_CONFIG_SOC_R7FA4T1BB3CNH
SB_CONFIG_SOC_R7FA4T1B93CFM
SB_CONFIG_SOC_R7FA4T1B93CFL
SB_CONFIG_SOC_R7FA4T1B93CFJ
SB_CONFIG_SOC_R7FA4T1B93CNE
SB_CONFIG_SOC_R7FA4T1B93CNH
```

**定义位置（Location）**：[`soc/renesas/ra/ra4t1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4t1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4T1BB3CFM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1BB3CFM)、[`SB_CONFIG_SOC_R7FA4T1BB3CFL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1BB3CFL)、[`SB_CONFIG_SOC_R7FA4T1BB3CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1BB3CFJ)、[`SB_CONFIG_SOC_R7FA4T1BB3CNE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1BB3CNE)、[`SB_CONFIG_SOC_R7FA4T1BB3CNH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1BB3CNH)、[`SB_CONFIG_SOC_R7FA4T1B93CFM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1B93CFM)、[`SB_CONFIG_SOC_R7FA4T1B93CFL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1B93CFL)、[`SB_CONFIG_SOC_R7FA4T1B93CFJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1B93CFJ)、[`SB_CONFIG_SOC_R7FA4T1B93CNE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1B93CNE)、[`SB_CONFIG_SOC_R7FA4T1B93CNH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_R7FA4T1B93CNH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`、`SB_CONFIG_SOC_R7FA4T1BB3CFM`、`SB_CONFIG_SOC_R7FA4T1BB3CFL`、`SB_CONFIG_SOC_R7FA4T1BB3CFJ`、`SB_CONFIG_SOC_R7FA4T1BB3CNE`、`SB_CONFIG_SOC_R7FA4T1BB3CNH`、`SB_CONFIG_SOC_R7FA4T1B93CFM`、`SB_CONFIG_SOC_R7FA4T1B93CFL`、`SB_CONFIG_SOC_R7FA4T1B93CFJ`、`SB_CONFIG_SOC_R7FA4T1B93CNE`、`SB_CONFIG_SOC_R7FA4T1B93CNH`。

<a id="SB_CONFIG_SOC_SERIES_RA4W1"></a>

## 304.74 `SB_CONFIG_SOC_SERIES_RA4W1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA4W1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA4W1AD2CNG
```

**定义位置（Location）**：[`soc/renesas/ra/ra4w1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra4w1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA4W1AD2CNG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA4W1AD2CNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6E1"></a>

## 304.75 `SB_CONFIG_SOC_SERIES_RA6E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6E10F2CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6E10F2CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6E10F2CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6E2"></a>

## 304.76 `SB_CONFIG_SOC_SERIES_RA6E2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6E2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6E2BB3CFM
```

**定义位置（Location）**：[`soc/renesas/ra/ra6e2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6e2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6E2BB3CFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6E2BB3CFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6M1"></a>

## 304.77 `SB_CONFIG_SOC_SERIES_RA6M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6M1AD3CFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6M1AD3CFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M1AD3CFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6M2"></a>

## 304.78 `SB_CONFIG_SOC_SERIES_RA6M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6M2AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6M2AF3CFB`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M2AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6M3"></a>

## 304.79 `SB_CONFIG_SOC_SERIES_RA6M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M3 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6M3AH3CFC
SB_CONFIG_SOC_R7FA6M3AF2CBG
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6M3AH3CFC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M3AH3CFC)、[`SB_CONFIG_SOC_R7FA6M3AF2CBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M3AF2CBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6M4"></a>

## 304.80 `SB_CONFIG_SOC_SERIES_RA6M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M4 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6M4AF3CFB
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m4/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m4/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6M4AF3CFB`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M4AF3CFB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA6M5"></a>

## 304.81 `SB_CONFIG_SOC_SERIES_RA6M5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA6M5 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA6M5BH3CFC
```

**定义位置（Location）**：[`soc/renesas/ra/ra6m5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra6m5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA6M5BH3CFC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA6M5BH3CFC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8D1"></a>

## 304.82 `SB_CONFIG_SOC_SERIES_RA8D1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8D1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA8D1BHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA8D1BHECBD`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA8D1BHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8D2"></a>

## 304.83 `SB_CONFIG_SOC_SERIES_RA8D2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8D2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8D2KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8d2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8d2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7KA8D2KFLCAC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7KA8D2KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8E1"></a>

## 304.84 `SB_CONFIG_SOC_SERIES_RA8E1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8E1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA8E1AFDCFB
SB_CONFIG_SOC_R7FA8E1AFDCFP
```

**定义位置（Location）**：[`soc/renesas/ra/ra8e1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8e1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA8E1AFDCFB`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA8E1AFDCFB)、[`SB_CONFIG_SOC_R7FA8E1AFDCFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA8E1AFDCFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8M1"></a>

## 304.85 `SB_CONFIG_SOC_SERIES_RA8M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8M1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA8M1AHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA8M1AHECBD`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA8M1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8M2"></a>

## 304.86 `SB_CONFIG_SOC_SERIES_RA8M2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8M2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8M2JFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8m2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8m2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7KA8M2JFLCAC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7KA8M2JFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8P1"></a>

## 304.87 `SB_CONFIG_SOC_SERIES_RA8P1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8P1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8P1KFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8p1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8p1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7KA8P1KFLCAC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7KA8P1KFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8T1"></a>

## 304.88 `SB_CONFIG_SOC_SERIES_RA8T1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8T1 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7FA8T1AHECBD
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t1/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t1/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7FA8T1AHECBD`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7FA8T1AHECBD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RA8T2"></a>

## 304.89 `SB_CONFIG_SOC_SERIES_RA8T2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RA8T2 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7KA8T2LFLCAC
```

**定义位置（Location）**：[`soc/renesas/ra/ra8t2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/ra/ra8t2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RA)、[`SB_CONFIG_SOC_R7KA8T2LFLCAC`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7KA8T2LFLCAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="SB_CONFIG_SOC_SERIES_RCAR_GEN5"></a>

## 304.90 `SB_CONFIG_SOC_SERIES_RCAR_GEN5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

R-Car 第五代片上系统系列支持（R-Car Gen5 SoC series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RCAR
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R8A78000_R52
SB_CONFIG_SOC_R8A78000_A720
```

**定义位置（Location）**：[`soc/renesas/rcar/rcar_gen5/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rcar/rcar_gen5/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RCAR)、[`SB_CONFIG_SOC_R8A78000_R52`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R8A78000_R52)、[`SB_CONFIG_SOC_R8A78000_A720`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R8A78000_A720)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RCAR`。

<a id="SB_CONFIG_SOC_SERIES_RX130"></a>

## 304.91 `SB_CONFIG_SOC_SERIES_RX130`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX130 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F51308AXFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx130/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx130/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F51308AXFP`](P303_soc_renesas_配置项参考_2.md#SB_CONFIG_SOC_R5F51308AXFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX140"></a>

## 304.92 `SB_CONFIG_SOC_SERIES_RX140`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX140 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F51406BDFN
SB_CONFIG_SOC_R5F51406BGFN
```

**定义位置（Location）**：[`soc/renesas/rx/rx140/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx140/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F51406BDFN`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F51406BDFN)、[`SB_CONFIG_SOC_R5F51406BGFN`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F51406BGFN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX14T"></a>

## 304.93 `SB_CONFIG_SOC_SERIES_RX14T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX14T 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F514T5AMFM
```

**定义位置（Location）**：[`soc/renesas/rx/rx14t/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx14t/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F514T5AMFM`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F514T5AMFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX261"></a>

## 304.94 `SB_CONFIG_SOC_SERIES_RX261`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX261 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F52618BGFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx261/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx261/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F52618BGFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F52618BGFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX26T"></a>

## 304.95 `SB_CONFIG_SOC_SERIES_RX26T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX26T 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F526TFDDFP
```

**定义位置（Location）**：[`soc/renesas/rx/rx26t/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx26t/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F526TFDDFP`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F526TFDDFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX62N"></a>

## 304.96 `SB_CONFIG_SOC_SERIES_RX62N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX62N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5F562N8
```

**定义位置（Location）**：[`soc/renesas/rx/rx62n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx62n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5F562N8`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5F562N8)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX74M"></a>

## 304.97 `SB_CONFIG_SOC_SERIES_RX74M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX74M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5K574MCB4AE
```

**定义位置（Location）**：[`soc/renesas/rx/rx74m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5K574MCB4AE`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5K574MCB4AE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RX74N"></a>

## 304.98 `SB_CONFIG_SOC_SERIES_RX74N`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RX74N 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R5K574NCB4AE
```

**定义位置（Location）**：[`soc/renesas/rx/rx74n/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rx/rx74n/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RX)、[`SB_CONFIG_SOC_R5K574NCB4AE`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R5K574NCB4AE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="SB_CONFIG_SOC_SERIES_RZA2M"></a>

## 304.99 `SB_CONFIG_SOC_SERIES_RZA2M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A2M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R7S921053VCBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza2m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza2m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R7S921053VCBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R7S921053VCBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<a id="SB_CONFIG_SOC_SERIES_RZA3M"></a>

## 304.100 `SB_CONFIG_SOC_SERIES_RZA3M`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

瑞萨（Renesas）RZ/A3M 系列（series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_RENESAS_RZ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_R9A07G066M04GBG
```

**定义位置（Location）**：[`soc/renesas/rz/rza3m/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/renesas/rz/rza3m/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_RENESAS_RZ)、[`SB_CONFIG_SOC_R9A07G066M04GBG`](P304_soc_renesas_配置项参考_3.md#SB_CONFIG_SOC_R9A07G066M04GBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_RENESAS_RZ`。

<!-- kconfig-navigation -->

[上一章](P303_soc_renesas_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P305_soc_renesas_配置项参考_4.md)
