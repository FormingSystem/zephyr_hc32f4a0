---
id: learning.zephyr-docs.kconfig-reference.page-259
title: "`soc/alif`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第259章\_`soc/alif`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/alif` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AB1C1F4M51820PH0"></a>

## 259.1 `CONFIG_SOC_AB1C1F4M51820PH0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Balletto B1（AB1C1F4M51820PH0）。高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）中具有单个 Cortex-M55 内核，针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_B1
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BALLETTO_B1_SK
CONFIG_BOARD_BALLETTO_B1_DK
```

**定义位置（Location）**：[`soc/alif/balletto/b1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/balletto/b1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_BOARD_BALLETTO_B1_SK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BALLETTO_B1_SK)、[`CONFIG_BOARD_BALLETTO_B1_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BALLETTO_B1_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_B1`、`CONFIG_BOARD_BALLETTO_B1_SK`、`CONFIG_BOARD_BALLETTO_B1_DK`。

<a id="CONFIG_SOC_AE1C1F4051920PH0"></a>

## 259.2 `CONFIG_SOC_AE1C1F4051920PH0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E1C 片上系统（AE1C1F4051920PH0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_E1C
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE
```

**定义位置（Location）**：[`soc/alif/ensemble/e1c/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e1c/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_E1C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_E1C)、[`CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_E1C`。

<a id="CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE"></a>

## 259.3 `CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE1C1F4051920PH0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE1C1F4051920PH0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E1C_SK
CONFIG_BOARD_ENSEMBLE_E1C_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e1c/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e1c/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE1C1F4051920PH0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE1C1F4051920PH0)、[`CONFIG_BOARD_ENSEMBLE_E1C_SK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E1C_SK)、[`CONFIG_BOARD_ENSEMBLE_E1C_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E1C_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E1C_SK`、`CONFIG_BOARD_ENSEMBLE_E1C_DK`。

<a id="CONFIG_SOC_AE402FA0E5597LE0"></a>

## 259.4 `CONFIG_SOC_AE402FA0E5597LE0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E4 片上系统（AE402FA0E5597LE0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_E4
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE
CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_E4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_E4)、[`CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE)、[`CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_E4`。

<a id="CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE"></a>

## 259.5 `CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE402FA0E5597LE0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE402FA0E5597LE0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE402FA0E5597LE0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE402FA0E5597LE0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP"></a>

## 259.6 `CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE402FA0E5597LE0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE402FA0E5597LE0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE402FA0E5597LE0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE402FA0E5597LE0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE612FA0E5597LS0"></a>

## 259.7 `CONFIG_SOC_AE612FA0E5597LS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E6 片上系统（AE612FA0E5597LS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_E6
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE
CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_E6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_E6)、[`CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE)、[`CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_E6`。

<a id="CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE"></a>

## 259.8 `CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE612FA0E5597LS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE612FA0E5597LS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE612FA0E5597LS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE612FA0E5597LS0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP"></a>

## 259.9 `CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE612FA0E5597LS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE612FA0E5597LS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE612FA0E5597LS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE612FA0E5597LS0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE822FA0E5597BS0"></a>

## 259.10 `CONFIG_SOC_AE822FA0E5597BS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E8 片上系统（AE822FA0E5597BS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_E8
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE822FA0E5597BS0_APSS
CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE
CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_E8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_E8)、[`CONFIG_SOC_AE822FA0E5597BS0_APSS`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0_APSS)、[`CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE)、[`CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_E8`。

<a id="CONFIG_SOC_AE822FA0E5597BS0_APSS"></a>

## 259.11 `CONFIG_SOC_AE822FA0E5597BS0_APSS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 应用处理器子系统（Application Processor Subsystem，APSS）。Cortex-A32 内核的最高频率为 800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0)、[`CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE"></a>

## 259.12 `CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0)、[`CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP"></a>

## 259.13 `CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597BS0)、[`CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="CONFIG_SOC_AE822FA0E5597LS0"></a>

## 259.14 `CONFIG_SOC_AE822FA0E5597LS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E8 片上系统（AE822FA0E5597LS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_E8
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE822FA0E5597LS0_APSS
CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE
CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_E8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_E8)、[`CONFIG_SOC_AE822FA0E5597LS0_APSS`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0_APSS)、[`CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE)、[`CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_E8`。

<a id="CONFIG_SOC_AE822FA0E5597LS0_APSS"></a>

## 259.15 `CONFIG_SOC_AE822FA0E5597LS0_APSS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 应用处理器子系统（Application Processor Subsystem，APSS）。Cortex-A32 内核的最高频率为 800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE"></a>

## 259.16 `CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP"></a>

## 259.17 `CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#CONFIG_SOC_AE822FA0E5597LS0)、[`CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AB1C1F4M51820PH0"></a>

## 259.18 `SB_CONFIG_SOC_AB1C1F4M51820PH0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Balletto B1（AB1C1F4M51820PH0）。高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）中具有单个 Cortex-M55 内核，针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_B1
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BALLETTO_B1_SK
SB_CONFIG_BOARD_BALLETTO_B1_DK
```

**定义位置（Location）**：[`soc/alif/balletto/b1/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/balletto/b1/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_B1)、[`SB_CONFIG_BOARD_BALLETTO_B1_SK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BALLETTO_B1_SK)、[`SB_CONFIG_BOARD_BALLETTO_B1_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BALLETTO_B1_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_B1`、`SB_CONFIG_BOARD_BALLETTO_B1_SK`、`SB_CONFIG_BOARD_BALLETTO_B1_DK`。

<a id="SB_CONFIG_SOC_AE1C1F4051920PH0"></a>

## 259.19 `SB_CONFIG_SOC_AE1C1F4051920PH0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E1C 片上系统（AE1C1F4051920PH0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_E1C
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE
```

**定义位置（Location）**：[`soc/alif/ensemble/e1c/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e1c/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_E1C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_E1C)、[`SB_CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_E1C`。

<a id="SB_CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE"></a>

## 259.20 `SB_CONFIG_SOC_AE1C1F4051920PH0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE1C1F4051920PH0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE1C1F4051920PH0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E1C_SK
SB_CONFIG_BOARD_ENSEMBLE_E1C_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e1c/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e1c/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE1C1F4051920PH0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE1C1F4051920PH0)、[`SB_CONFIG_BOARD_ENSEMBLE_E1C_SK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E1C_SK)、[`SB_CONFIG_BOARD_ENSEMBLE_E1C_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E1C_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E1C_SK`、`SB_CONFIG_BOARD_ENSEMBLE_E1C_DK`。

<a id="SB_CONFIG_SOC_AE402FA0E5597LE0"></a>

## 259.21 `SB_CONFIG_SOC_AE402FA0E5597LE0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E4 片上系统（AE402FA0E5597LE0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_E4
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE
SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_E4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_E4)、[`SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE)、[`SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_E4`。

<a id="SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE"></a>

## 259.22 `SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE402FA0E5597LE0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE402FA0E5597LE0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE402FA0E5597LE0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE402FA0E5597LE0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP"></a>

## 259.23 `SB_CONFIG_SOC_AE402FA0E5597LE0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE402FA0E5597LE0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE402FA0E5597LE0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e4/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e4/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE402FA0E5597LE0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE402FA0E5597LE0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE612FA0E5597LS0"></a>

## 259.24 `SB_CONFIG_SOC_AE612FA0E5597LS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E6 片上系统（AE612FA0E5597LS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_E6
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE
SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_E6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_E6)、[`SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE)、[`SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_E6`。

<a id="SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE"></a>

## 259.25 `SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE612FA0E5597LS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE612FA0E5597LS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE612FA0E5597LS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE612FA0E5597LS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP"></a>

## 259.26 `SB_CONFIG_SOC_AE612FA0E5597LS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE612FA0E5597LS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE612FA0E5597LS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e6/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e6/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE612FA0E5597LS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE612FA0E5597LS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597BS0"></a>

## 259.27 `SB_CONFIG_SOC_AE822FA0E5597BS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E8 片上系统（AE822FA0E5597BS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_E8
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE822FA0E5597BS0_APSS
SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE
SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L38)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_E8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_E8)、[`SB_CONFIG_SOC_AE822FA0E5597BS0_APSS`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0_APSS)、[`SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE)、[`SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_E8`。

<a id="SB_CONFIG_SOC_AE822FA0E5597BS0_APSS"></a>

## 259.28 `SB_CONFIG_SOC_AE822FA0E5597BS0_APSS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 应用处理器子系统（Application Processor Subsystem，APSS）。Cortex-A32 内核的最高频率为 800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L44)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE"></a>

## 259.29 `SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP"></a>

## 259.30 `SB_CONFIG_SOC_AE822FA0E5597BS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597BS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597BS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_AK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L58)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597BS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597BS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_AK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_AK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597LS0"></a>

## 259.31 `SB_CONFIG_SOC_AE822FA0E5597LS0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Alif Ensemble E8 片上系统（AE822FA0E5597LS0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_E8
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AE822FA0E5597LS0_APSS
SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE
SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_E8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_E8)、[`SB_CONFIG_SOC_AE822FA0E5597LS0_APSS`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0_APSS)、[`SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE)、[`SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_E8`。

<a id="SB_CONFIG_SOC_AE822FA0E5597LS0_APSS"></a>

## 259.32 `SB_CONFIG_SOC_AE822FA0E5597LS0_APSS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 应用处理器子系统（Application Processor Subsystem，APSS）。Cortex-A32 内核的最高频率为 800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE"></a>

## 259.33 `SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 高能效实时子系统（High Efficiency Real Time Subsystem，RTSS-HE）。Cortex-M55 内核针对能效优化，最高频率为 160 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<a id="SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP"></a>

## 259.34 `SB_CONFIG_SOC_AE822FA0E5597LS0_RTSS_HP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AE822FA0E5597LS0 高性能实时子系统（High Performance Real Time Subsystem，RTSS-HP）。Cortex-M55 内核针对计算性能优化，最高频率为 400 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AE822FA0E5597LS0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ENSEMBLE_E8_DK
```

**定义位置（Location）**：[`soc/alif/ensemble/e8/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/alif/ensemble/e8/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AE822FA0E5597LS0`](P259_soc_alif_配置项参考.md#SB_CONFIG_SOC_AE822FA0E5597LS0)、[`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ENSEMBLE_E8_DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ENSEMBLE_E8_DK`。

<!-- kconfig-navigation -->

[上一章](P258_soc_adi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P260_soc_ambiq_配置项参考.md)
