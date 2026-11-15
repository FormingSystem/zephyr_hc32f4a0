---
id: learning.zephyr-docs.kconfig-reference.page-206
title: "`modules/Kconfig.microchip`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第206章\_`modules/Kconfig.microchip`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.microchip` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_MEC5_HAL"></a>

## 206.1 `CONFIG_HAS_MEC5_HAL`

**提示（Prompt）**：Microchip MEC5 硬件抽象层（HAL）驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/Kconfig.microchip:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.microchip#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

<a id="CONFIG_HAS_MEC_HAL"></a>

## 206.2 `CONFIG_HAS_MEC_HAL`

**提示（Prompt）**：Microchip MEC 硬件抽象层（HAL）驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MEC1501_HSZ
```

**定义位置（Location）**：[`modules/Kconfig.microchip:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.microchip#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MEC1501_HSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1501_HSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MEC1501_HSZ`。

<a id="CONFIG_HAS_MPFS_HAL"></a>

## 206.3 `CONFIG_HAS_MPFS_HAL`

**提示（Prompt）**：Microchip MPFS 硬件抽象层（HAL）驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MPFS_HAL
```

**定义位置（Location）**：[`modules/Kconfig.microchip:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.microchip#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_MPFS_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPFS_HAL)。

<!-- kconfig-navigation -->

[上一章](P205_modules_Kconfig.mcuboot_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P207_modules_Kconfig.nuvoton_配置项参考.md)
