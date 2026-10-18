---
id: learning.zephyr-docs.kconfig-reference.page-284
title: "`soc/mediatek`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第284章\_`soc/mediatek`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/mediatek` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_MT8186_ADSP"></a>

## 284.1 `CONFIG_SOC_MT8186_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8186 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8186
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8186
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8186/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8186/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8186)、[`CONFIG_BOARD_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8186)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8186`、`CONFIG_BOARD_MT8186`。

<a id="CONFIG_SOC_MT8188_A55"></a>

## 284.2 `CONFIG_SOC_MT8188_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8188 Cortex-A55 集群（cluster）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8188
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8390_GENIO_700_EVK
CONFIG_BOARD_MT8370_GENIO_510_EVK
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8188/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8188/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188)、[`CONFIG_BOARD_MT8390_GENIO_700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8390_GENIO_700_EVK)、[`CONFIG_BOARD_MT8370_GENIO_510_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8370_GENIO_510_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8188`、`CONFIG_BOARD_MT8390_GENIO_700_EVK`、`CONFIG_BOARD_MT8370_GENIO_510_EVK`。

<a id="CONFIG_SOC_MT8188_ADSP"></a>

## 284.3 `CONFIG_SOC_MT8188_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8188 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8188
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8188
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8188/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8188/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188)、[`CONFIG_BOARD_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8188)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8188`、`CONFIG_BOARD_MT8188`。

<a id="CONFIG_SOC_MT8195_ADSP"></a>

## 284.4 `CONFIG_SOC_MT8195_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8195 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8195
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8195
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8195/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8195/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8195)、[`CONFIG_BOARD_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8195)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8195`、`CONFIG_BOARD_MT8195`。

<a id="CONFIG_SOC_MT8196_ADSP"></a>

## 284.5 `CONFIG_SOC_MT8196_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8196 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8196
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8196
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8196/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8196/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8196)、[`CONFIG_BOARD_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8196)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8196`、`CONFIG_BOARD_MT8196`。

<a id="CONFIG_SOC_MT8365_ADSP"></a>

## 284.6 `CONFIG_SOC_MT8365_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8365 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MT8365
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MT8365
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8365/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8365/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8365)、[`CONFIG_BOARD_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MT8365)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MT8365`、`CONFIG_BOARD_MT8365`。

<a id="CONFIG_SOC_SERIES_MT818X"></a>

## 284.7 `CONFIG_SOC_SERIES_MT818X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT818x 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MT8186
CONFIG_SOC_MT8188
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MT8XXX)、[`CONFIG_SOC_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8186)、[`CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MT8XXX`、`CONFIG_SOC_MT8186`、`CONFIG_SOC_MT8188`。

<a id="CONFIG_SOC_SERIES_MT8195"></a>

## 284.8 `CONFIG_SOC_SERIES_MT8195`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8195 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MT8195
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MT8XXX)、[`CONFIG_SOC_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8195)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MT8XXX`、`CONFIG_SOC_MT8195`。

<a id="CONFIG_SOC_SERIES_MT8196"></a>

## 284.9 `CONFIG_SOC_SERIES_MT8196`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8196 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MT8196
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MT8XXX)、[`CONFIG_SOC_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8196)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MT8XXX`、`CONFIG_SOC_MT8196`。

<a id="CONFIG_SOC_SERIES_MT8365"></a>

## 284.10 `CONFIG_SOC_SERIES_MT8365`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8365 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MT8365
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MT8XXX)、[`CONFIG_SOC_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8365)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MT8XXX`、`CONFIG_SOC_MT8365`。

<a id="SB_CONFIG_SOC_MT8186_ADSP"></a>

## 284.11 `SB_CONFIG_SOC_MT8186_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8186 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8186
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8186
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8186/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8186/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8186)、[`SB_CONFIG_BOARD_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8186)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8186`、`SB_CONFIG_BOARD_MT8186`。

<a id="SB_CONFIG_SOC_MT8188_A55"></a>

## 284.12 `SB_CONFIG_SOC_MT8188_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8188 Cortex-A55 集群（cluster）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8188
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8390_GENIO_700_EVK
SB_CONFIG_BOARD_MT8370_GENIO_510_EVK
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8188/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8188/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8188)、[`SB_CONFIG_BOARD_MT8390_GENIO_700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8390_GENIO_700_EVK)、[`SB_CONFIG_BOARD_MT8370_GENIO_510_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8370_GENIO_510_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8188`、`SB_CONFIG_BOARD_MT8390_GENIO_700_EVK`、`SB_CONFIG_BOARD_MT8370_GENIO_510_EVK`。

<a id="SB_CONFIG_SOC_MT8188_ADSP"></a>

## 284.13 `SB_CONFIG_SOC_MT8188_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8188 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8188
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8188
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8188/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8188/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8188)、[`SB_CONFIG_BOARD_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8188)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8188`、`SB_CONFIG_BOARD_MT8188`。

<a id="SB_CONFIG_SOC_MT8195_ADSP"></a>

## 284.14 `SB_CONFIG_SOC_MT8195_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8195 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8195
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8195
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8195/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8195/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8195)、[`SB_CONFIG_BOARD_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8195)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8195`、`SB_CONFIG_BOARD_MT8195`。

<a id="SB_CONFIG_SOC_MT8196_ADSP"></a>

## 284.15 `SB_CONFIG_SOC_MT8196_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8196 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8196
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8196
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8196/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8196/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8196)、[`SB_CONFIG_BOARD_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8196)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8196`、`SB_CONFIG_BOARD_MT8196`。

<a id="SB_CONFIG_SOC_MT8365_ADSP"></a>

## 284.16 `SB_CONFIG_SOC_MT8365_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8365 音频数字信号处理器（audio DSP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MT8365
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MT8365
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/mt8365/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/mt8365/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8365)、[`SB_CONFIG_BOARD_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MT8365)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MT8365`、`SB_CONFIG_BOARD_MT8365`。

<a id="SB_CONFIG_SOC_SERIES_MT818X"></a>

## 284.17 `SB_CONFIG_SOC_SERIES_MT818X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT818x 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MT8186
SB_CONFIG_SOC_MT8188
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MT8XXX)、[`SB_CONFIG_SOC_MT8186`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8186)、[`SB_CONFIG_SOC_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8188)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MT8XXX`、`SB_CONFIG_SOC_MT8186`、`SB_CONFIG_SOC_MT8188`。

<a id="SB_CONFIG_SOC_SERIES_MT8195"></a>

## 284.18 `SB_CONFIG_SOC_SERIES_MT8195`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8195 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MT8195
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MT8XXX)、[`SB_CONFIG_SOC_MT8195`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8195)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MT8XXX`、`SB_CONFIG_SOC_MT8195`。

<a id="SB_CONFIG_SOC_SERIES_MT8196"></a>

## 284.19 `SB_CONFIG_SOC_SERIES_MT8196`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8196 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MT8196
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MT8XXX)、[`SB_CONFIG_SOC_MT8196`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8196)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MT8XXX`、`SB_CONFIG_SOC_MT8196`。

<a id="SB_CONFIG_SOC_SERIES_MT8365"></a>

## 284.20 `SB_CONFIG_SOC_SERIES_MT8365`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mediatek MT8365 平台

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MT8XXX
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MT8365
```

**定义位置（Location）**：[`soc/mediatek/mt8xxx/Kconfig.soc:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/mediatek/mt8xxx/Kconfig.soc#L28)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MT8XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MT8XXX)、[`SB_CONFIG_SOC_MT8365`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MT8365)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MT8XXX`、`SB_CONFIG_SOC_MT8365`。

<!-- kconfig-navigation -->

[上一章](P283_soc_litex_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P285_soc_microchip_配置项参考_1.md)
