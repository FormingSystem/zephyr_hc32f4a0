---
id: learning.zephyr-docs.kconfig-reference.page-283
title: "`soc/litex`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第283章\_`soc/litex`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/litex` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LITEX_CSR_DATA_WIDTH"></a>

## 283.1 `CONFIG_LITEX_CSR_DATA_WIDTH`

**提示（Prompt）**：选择控制／状态寄存器宽度（Control/Status register width）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_LITEX
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`soc/litex/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/litex/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_LITEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LITEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_LITEX`。

<a id="CONFIG_LITEX_CSR_DATA_WIDTH_DEPRECATED"></a>

## 283.2 `CONFIG_LITEX_CSR_DATA_WIDTH_DEPRECATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当 `LITEX_CSR_DATA_WIDTH` 设为非 32 的值时，此选项用于选择 `DEPRECATED`。它将在未来版本中移除。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LITEX_CSR_DATA_WIDTH != 32 && CONFIG_SOC_FAMILY_LITEX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`soc/litex/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/litex/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LITEX_CSR_DATA_WIDTH`](P283_soc_litex_配置项参考.md#CONFIG_LITEX_CSR_DATA_WIDTH)、[`CONFIG_SOC_FAMILY_LITEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LITEX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_LITEX`。

<a id="CONFIG_LITEX_CSR_ORDERING"></a>

## 283.3 `CONFIG_LITEX_CSR_ORDERING`

**提示（Prompt）**：选择控制／状态寄存器字节序（Control/Status register ordering）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_LITEX
```

**默认值（Defaults）**

```text
CONFIG_LITEX_CSR_ORDERING_BIG
```

**可选项（Choices）**

```text
CONFIG_LITEX_CSR_ORDERING_BIG
CONFIG_LITEX_CSR_ORDERING_LITTLE
```

**定义位置（Location）**：[`soc/litex/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/litex/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_LITEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LITEX)、[`CONFIG_LITEX_CSR_ORDERING_BIG`](P283_soc_litex_配置项参考.md#CONFIG_LITEX_CSR_ORDERING_BIG)、[`CONFIG_LITEX_CSR_ORDERING_LITTLE`](P283_soc_litex_配置项参考.md#CONFIG_LITEX_CSR_ORDERING_LITTLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_LITEX`。

<a id="CONFIG_LITEX_CSR_ORDERING_BIG"></a>

## 283.4 `CONFIG_LITEX_CSR_ORDERING_BIG`

**提示（Prompt）**：大端字节序（Big-endian ordering）

**说明（Help）**

控制／状态寄存器（CSR）访问使用大端字节序（big-endian ordering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LITEX_CSR_ORDERING>
```

**定义位置（Location）**：[`soc/litex/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/litex/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 选择控制／状态寄存器字节序（Control/Status register ordering）

**配置项引用（Symbol References）**：[`CONFIG_LITEX_CSR_ORDERING`](P283_soc_litex_配置项参考.md#CONFIG_LITEX_CSR_ORDERING)。

<a id="CONFIG_LITEX_CSR_ORDERING_LITTLE"></a>

## 283.5 `CONFIG_LITEX_CSR_ORDERING_LITTLE`

**提示（Prompt）**：小端字节序（Little-endian ordering）

**说明（Help）**

控制／状态寄存器（CSR）访问使用小端字节序（little-endian ordering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LITEX_CSR_ORDERING>
```

**定义位置（Location）**：[`soc/litex/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/litex/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 选择控制／状态寄存器字节序（Control/Status register ordering）

**配置项引用（Symbol References）**：[`CONFIG_LITEX_CSR_ORDERING`](P283_soc_litex_配置项参考.md#CONFIG_LITEX_CSR_ORDERING)。

<!-- kconfig-navigation -->

[上一章](P282_soc_ite_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P284_soc_mediatek_配置项参考.md)
