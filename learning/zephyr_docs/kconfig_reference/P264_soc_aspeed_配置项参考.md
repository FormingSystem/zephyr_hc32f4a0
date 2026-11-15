---
id: learning.zephyr-docs.kconfig-reference.page-264
title: "`soc/aspeed`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第264章\_`soc/aspeed`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/aspeed` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AST1030"></a>

## 264.1 `CONFIG_SOC_AST1030`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AST1030 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_AST10X0
```

**被选择（Selected by）**

```text
CONFIG_BOARD_AST1030_EVB
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AST10X0`](P264_soc_aspeed_配置项参考.md#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_BOARD_AST1030_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_AST1030_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_AST1030_EVB`。

<a id="CONFIG_SOC_SERIES_AST10X0"></a>

## 264.2 `CONFIG_SOC_SERIES_AST10X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ASPEED AST10X0 系列支持（series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ASPEED
```

**被选择（Selected by）**

```text
CONFIG_SOC_AST1030
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ASPEED)、[`CONFIG_SOC_AST1030`](P264_soc_aspeed_配置项参考.md#CONFIG_SOC_AST1030)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ASPEED`。

<a id="CONFIG_SRAM_NC_BASE_ADDRESS"></a>

## 264.3 `CONFIG_SRAM_NC_BASE_ADDRESS`

**提示（Prompt）**：非缓存 SRAM 基地址（noncached SRAM Base Address）

**说明（Help）**

非缓存 SRAM（non-cached SRAM）的基地址。默认值来自设备树 `/chosen/zephyr,sram` 的 `reg[1]`。用户通常应避免通过 menuconfig 或配置文件修改它。译注：`/chosen/zephyr,sram` 是设备树节点路径，不是主机文件系统地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_AST10X0 && CONFIG_SOC_FAMILY_ASPEED
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AST10X0`](P264_soc_aspeed_配置项参考.md#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_FAMILY_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ASPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ASPEED`。

<a id="CONFIG_SRAM_NC_SIZE"></a>

## 264.4 `CONFIG_SRAM_NC_SIZE`

**提示（Prompt）**：非缓存 SRAM 大小，单位为 kB（noncached SRAM Size）

**说明（Help）**

非缓存 SRAM（non-cached SRAM）的大小，单位为 kB。默认值来自设备树 `/chosen/zephyr,sram` 的 `reg[1]`。用户通常应避免通过 menuconfig 或配置文件修改它。译注：此处为设备树节点路径，不是主机文件系统地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_AST10X0 && CONFIG_SOC_FAMILY_ASPEED
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AST10X0`](P264_soc_aspeed_配置项参考.md#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_FAMILY_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ASPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ASPEED`。

<a id="SB_CONFIG_SOC_AST1030"></a>

## 264.5 `SB_CONFIG_SOC_AST1030`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AST1030 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_AST10X0
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_AST1030_EVB
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_AST10X0`](P264_soc_aspeed_配置项参考.md#SB_CONFIG_SOC_SERIES_AST10X0)、[`SB_CONFIG_BOARD_AST1030_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_AST1030_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_AST1030_EVB`。

<a id="SB_CONFIG_SOC_SERIES_AST10X0"></a>

## 264.6 `SB_CONFIG_SOC_SERIES_AST10X0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ASPEED AST10X0 系列支持（series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ASPEED
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AST1030
```

**定义位置（Location）**：[`soc/aspeed/ast10x0/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/aspeed/ast10x0/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ASPEED)、[`SB_CONFIG_SOC_AST1030`](P264_soc_aspeed_配置项参考.md#SB_CONFIG_SOC_AST1030)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ASPEED`。

<!-- kconfig-navigation -->

[上一章](P263_soc_arm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P265_soc_atmel_配置项参考.md)
