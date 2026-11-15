---
id: learning.zephyr-docs.kconfig-reference.page-279
title: "`soc/gd`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第279章\_`soc/gd`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/gd` 的 19 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_FAMILY_GD_GD32_HAS_BACKUP_DOMAIN_PROTECTION"></a>

## 279.1 `CONFIG_SOC_FAMILY_GD_GD32_HAS_BACKUP_DOMAIN_PROTECTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

对于需要显式启用后备域资源访问（backup domain resources access）的 SoC，选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_GD32F4XX
```

**定义位置（Location）**：[`soc/gd/gd32/common/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/common/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_SERIES_GD32F4XX`](P279_soc_gd_配置项参考.md#CONFIG_SOC_SERIES_GD32F4XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`。

<a id="CONFIG_SOC_SERIES_GD32A50X"></a>

## 279.2 `CONFIG_SOC_SERIES_GD32A50X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32A50X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32A503
```

**定义位置（Location）**：[`soc/gd/gd32/gd32a50x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32a50x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32A503`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32A503)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32A503`。

<a id="CONFIG_SOC_SERIES_GD32C2X1"></a>

## 279.3 `CONFIG_SOC_SERIES_GD32C2X1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32C2X1 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32C231
```

**定义位置（Location）**：[`soc/gd/gd32/gd32c2x1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32c2x1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32C231`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32C231)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32C231`。

<a id="CONFIG_SOC_SERIES_GD32E10X"></a>

## 279.4 `CONFIG_SOC_SERIES_GD32E10X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32E10X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32E103
```

**定义位置（Location）**：[`soc/gd/gd32/gd32e10x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32e10x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32E103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32E103)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32E103`。

<a id="CONFIG_SOC_SERIES_GD32E50X"></a>

## 279.5 `CONFIG_SOC_SERIES_GD32E50X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32E50X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32E507
```

**定义位置（Location）**：[`soc/gd/gd32/gd32e50x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32e50x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32E507`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32E507)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32E507`。

<a id="CONFIG_SOC_SERIES_GD32F3X0"></a>

## 279.6 `CONFIG_SOC_SERIES_GD32F3X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F3X0 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32F350
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f3x0/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f3x0/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32F350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32F350`。

<a id="CONFIG_SOC_SERIES_GD32F403"></a>

## 279.7 `CONFIG_SOC_SERIES_GD32F403`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F403 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32F403
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f403/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f403/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F403)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32F403`。

<a id="CONFIG_SOC_SERIES_GD32F4XX"></a>

## 279.8 `CONFIG_SOC_SERIES_GD32F4XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F4XX 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32F405
CONFIG_SOC_GD32F407
CONFIG_SOC_GD32F450
CONFIG_SOC_GD32F470
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f4xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f4xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32F405`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F405)、[`CONFIG_SOC_GD32F407`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F407)、[`CONFIG_SOC_GD32F450`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F450)、[`CONFIG_SOC_GD32F470`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32F470)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32F405`、`CONFIG_SOC_GD32F407`、`CONFIG_SOC_GD32F450`、`CONFIG_SOC_GD32F470`。

<a id="CONFIG_SOC_SERIES_GD32L23X"></a>

## 279.9 `CONFIG_SOC_SERIES_GD32L23X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32L23X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32L233
```

**定义位置（Location）**：[`soc/gd/gd32/gd32l23x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32l23x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32L233`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32L233)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32L233`。

<a id="CONFIG_SOC_SERIES_GD32VF103"></a>

## 279.10 `CONFIG_SOC_SERIES_GD32VF103`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32VF103 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
CONFIG_SOC_GD32VF103
```

**定义位置（Location）**：[`soc/gd/gd32/gd32vf103/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32vf103/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GD32VF103)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_GD32VF103`。

<a id="SB_CONFIG_SOC_SERIES_GD32A50X"></a>

## 279.11 `SB_CONFIG_SOC_SERIES_GD32A50X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32A50X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32A503
```

**定义位置（Location）**：[`soc/gd/gd32/gd32a50x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32a50x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32A503`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32A503)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32A503`。

<a id="SB_CONFIG_SOC_SERIES_GD32C2X1"></a>

## 279.12 `SB_CONFIG_SOC_SERIES_GD32C2X1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32C2X1 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32C231
```

**定义位置（Location）**：[`soc/gd/gd32/gd32c2x1/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32c2x1/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32C231`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32C231)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32C231`。

<a id="SB_CONFIG_SOC_SERIES_GD32E10X"></a>

## 279.13 `SB_CONFIG_SOC_SERIES_GD32E10X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32E10X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32E103
```

**定义位置（Location）**：[`soc/gd/gd32/gd32e10x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32e10x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32E103`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32E103)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32E103`。

<a id="SB_CONFIG_SOC_SERIES_GD32E50X"></a>

## 279.14 `SB_CONFIG_SOC_SERIES_GD32E50X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32E50X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32E507
```

**定义位置（Location）**：[`soc/gd/gd32/gd32e50x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32e50x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32E507`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32E507)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32E507`。

<a id="SB_CONFIG_SOC_SERIES_GD32F3X0"></a>

## 279.15 `SB_CONFIG_SOC_SERIES_GD32F3X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F3X0 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32F350
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f3x0/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f3x0/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32F350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32F350`。

<a id="SB_CONFIG_SOC_SERIES_GD32F403"></a>

## 279.16 `SB_CONFIG_SOC_SERIES_GD32F403`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F403 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32F403
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f403/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f403/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F403)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32F403`。

<a id="SB_CONFIG_SOC_SERIES_GD32F4XX"></a>

## 279.17 `SB_CONFIG_SOC_SERIES_GD32F4XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32F4XX 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32F405
SB_CONFIG_SOC_GD32F407
SB_CONFIG_SOC_GD32F450
SB_CONFIG_SOC_GD32F470
```

**定义位置（Location）**：[`soc/gd/gd32/gd32f4xx/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32f4xx/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32F405`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F405)、[`SB_CONFIG_SOC_GD32F407`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F407)、[`SB_CONFIG_SOC_GD32F450`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F450)、[`SB_CONFIG_SOC_GD32F470`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32F470)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32F405`、`SB_CONFIG_SOC_GD32F407`、`SB_CONFIG_SOC_GD32F450`、`SB_CONFIG_SOC_GD32F470`。

<a id="SB_CONFIG_SOC_SERIES_GD32L23X"></a>

## 279.18 `SB_CONFIG_SOC_SERIES_GD32L23X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32L23X 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32L233
```

**定义位置（Location）**：[`soc/gd/gd32/gd32l23x/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32l23x/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32L233`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32L233)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32L233`。

<a id="SB_CONFIG_SOC_SERIES_GD32VF103"></a>

## 279.19 `SB_CONFIG_SOC_SERIES_GD32VF103`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用兆易创新 GD32VF103 微控制器系列支持（GigaDevice MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_GD_GD32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_GD32VF103
```

**定义位置（Location）**：[`soc/gd/gd32/gd32vf103/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/gd/gd32/gd32vf103/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_GD_GD32)、[`SB_CONFIG_SOC_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_GD32VF103)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_GD_GD32`、`SB_CONFIG_SOC_GD32VF103`。

<!-- kconfig-navigation -->

[上一章](P278_soc_focaltech_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P280_soc_infineon_配置项参考.md)
