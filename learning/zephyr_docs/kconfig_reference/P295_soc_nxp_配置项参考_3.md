---
id: learning.zephyr-docs.kconfig-reference.page-295
title: "`soc/nxp`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第295章\_`soc/nxp`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `soc/nxp` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="SB_CONFIG_SOC_MIMX9529_M7"></a>

## 295.1 `SB_CONFIG_SOC_MIMX9529_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX952 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9529
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX952_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx952/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx952/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9529`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9529)、[`SB_CONFIG_BOARD_IMX952_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX952_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9529`、`SB_CONFIG_BOARD_IMX952_EVK`。

<a id="SB_CONFIG_SOC_MIMX9596_A55"></a>

## 295.2 `SB_CONFIG_SOC_MIMX9596_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX95 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9596
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX95_EVK_15X15
SB_CONFIG_BOARD_IMX95_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx95/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx95/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9596`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9596)、[`SB_CONFIG_BOARD_IMX95_EVK_15X15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX95_EVK_15X15)、[`SB_CONFIG_BOARD_IMX95_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX95_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9596`、`SB_CONFIG_BOARD_IMX95_EVK_15X15`、`SB_CONFIG_BOARD_IMX95_EVK`。

<a id="SB_CONFIG_SOC_MIMX9596_M7"></a>

## 295.3 `SB_CONFIG_SOC_MIMX9596_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX95 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9596
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MR_NAVQ95B
SB_CONFIG_BOARD_IMX95_EVK_15X15
SB_CONFIG_BOARD_IMX95_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx95/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx95/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9596`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9596)、[`SB_CONFIG_BOARD_MR_NAVQ95B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MR_NAVQ95B)、[`SB_CONFIG_BOARD_IMX95_EVK_15X15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX95_EVK_15X15)、[`SB_CONFIG_BOARD_IMX95_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX95_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9596`、`SB_CONFIG_BOARD_MR_NAVQ95B`、`SB_CONFIG_BOARD_IMX95_EVK_15X15`、`SB_CONFIG_BOARD_IMX95_EVK`。

<a id="SB_CONFIG_SOC_MIMXRT595S_CM33"></a>

## 295.4 `SB_CONFIG_SOC_MIMXRT595S_CM33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP RT5xx CM33 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT595S
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MIMXRT595_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT595S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT595S)、[`SB_CONFIG_BOARD_MIMXRT595_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MIMXRT595_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT595S`、`SB_CONFIG_BOARD_MIMXRT595_EVK`。

<a id="SB_CONFIG_SOC_MIMXRT595S_F1"></a>

## 295.5 `SB_CONFIG_SOC_MIMXRT595S_F1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP RT5xx 音频 DSP 系列（ADSP Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT595S
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MIMXRT595_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT595S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT595S)、[`SB_CONFIG_BOARD_MIMXRT595_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MIMXRT595_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT595S`、`SB_CONFIG_BOARD_MIMXRT595_EVK`。

<a id="SB_CONFIG_SOC_MIMXRT735S_HIFI1"></a>

## 295.6 `SB_CONFIG_SOC_MIMXRT735S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT735S
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L70)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT735S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT735S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT735S`。

<a id="SB_CONFIG_SOC_MIMXRT758S_HIFI1"></a>

## 295.7 `SB_CONFIG_SOC_MIMXRT758S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT758S
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L56)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT758S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT758S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT758S`。

<a id="SB_CONFIG_SOC_MIMXRT798S_HIFI1"></a>

## 295.8 `SB_CONFIG_SOC_MIMXRT798S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT798S
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MIMXRT700_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L42)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT798S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT798S)、[`SB_CONFIG_BOARD_MIMXRT700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MIMXRT700_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT798S`、`SB_CONFIG_BOARD_MIMXRT700_EVK`。

<a id="SB_CONFIG_SOC_MIMXRT798S_HIFI4"></a>

## 295.9 `SB_CONFIG_SOC_MIMXRT798S_HIFI4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi4 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMXRT798S
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MIMXRT700_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT798S`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT798S)、[`SB_CONFIG_BOARD_MIMXRT700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MIMXRT700_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT798S`、`SB_CONFIG_BOARD_MIMXRT700_EVK`。

<a id="SB_CONFIG_SOC_SERIES_IMX7D"></a>

## 295.10 `SB_CONFIG_SOC_SERIES_IMX7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 iMX7D 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NXP_IMX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MCIMX7D
```

**定义位置（Location）**：[`soc/nxp/imx/imx7d/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx7d/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NXP_IMX)、[`SB_CONFIG_SOC_MCIMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MCIMX7D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NXP_IMX`、`SB_CONFIG_SOC_MCIMX7D`。

<!-- kconfig-navigation -->

[上一章](P294_soc_nxp_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P296_soc_oct_配置项参考.md)
