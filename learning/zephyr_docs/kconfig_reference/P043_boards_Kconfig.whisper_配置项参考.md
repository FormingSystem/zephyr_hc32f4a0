---
id: learning.zephyr-docs.kconfig-reference.page-43
title: "`boards/Kconfig.whisper`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第43章\_`boards/Kconfig.whisper`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/Kconfig.whisper` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WHISPER_CLINT_BASE_ADDRESS"></a>

## 43.1 `CONFIG_WHISPER_CLINT_BASE_ADDRESS`

**提示（Prompt）**：--clint 命令行参数的地址（Command Line Argument Address）

**说明（Help）**

指定 `--clint` 命令行参数使用的基地址（Base Address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_WHISPER_USE_CLINT && CONFIG_WHISPER_TARGET
```

**定义位置（Location）**：[`boards/Kconfig.whisper:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.whisper#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → Whisper 模拟器（Whisper Simulator） → 传递 --clint 命令行参数（Command Line Argument）

**配置项引用（Symbol References）**：[`CONFIG_WHISPER_USE_CLINT`](P043_boards_Kconfig.whisper_配置项参考.md#CONFIG_WHISPER_USE_CLINT)、[`CONFIG_WHISPER_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_WHISPER_TARGET)。

<a id="CONFIG_WHISPER_SWINT_BASE_ADDRESS"></a>

## 43.2 `CONFIG_WHISPER_SWINT_BASE_ADDRESS`

**提示（Prompt）**：--softinterrupt 命令行参数的地址（Command Line Argument Address）

**说明（Help）**

指定 `--softinterrupt` 命令行参数使用的基地址（Base Address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_WHISPER_USE_SWINT && CONFIG_WHISPER_TARGET
```

**定义位置（Location）**：[`boards/Kconfig.whisper:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.whisper#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → Whisper 模拟器（Whisper Simulator） → 传递 --softinterrupt 命令行参数（Command Line Argument）

**配置项引用（Symbol References）**：[`CONFIG_WHISPER_USE_SWINT`](P043_boards_Kconfig.whisper_配置项参考.md#CONFIG_WHISPER_USE_SWINT)、[`CONFIG_WHISPER_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_WHISPER_TARGET)。

<a id="CONFIG_WHISPER_USE_CLINT"></a>

## 43.3 `CONFIG_WHISPER_USE_CLINT`

**提示（Prompt）**：传递 --clint 命令行参数（Command Line Argument）

**说明（Help）**

启用向 Whisper 传递 `--clint` 命令行参数（Command Line Argument）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WHISPER_TARGET
```

**定义位置（Location）**：[`boards/Kconfig.whisper:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.whisper#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → Whisper 模拟器（Whisper Simulator）

**配置项引用（Symbol References）**：[`CONFIG_WHISPER_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_WHISPER_TARGET)。

<a id="CONFIG_WHISPER_USE_SWINT"></a>

## 43.4 `CONFIG_WHISPER_USE_SWINT`

**提示（Prompt）**：传递 --softinterrupt 命令行参数（Command Line Argument）

**说明（Help）**

启用向 Whisper 传递 `--softinterrupt` 命令行参数（Command Line Argument）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_WHISPER_USE_CLINT && CONFIG_WHISPER_TARGET
```

**定义位置（Location）**：[`boards/Kconfig.whisper:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.whisper#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → Whisper 模拟器（Whisper Simulator）

**配置项引用（Symbol References）**：[`CONFIG_WHISPER_USE_CLINT`](P043_boards_Kconfig.whisper_配置项参考.md#CONFIG_WHISPER_USE_CLINT)、[`CONFIG_WHISPER_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_WHISPER_TARGET)。

<!-- kconfig-navigation -->

[上一章](P042_boards_Kconfig.v2_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P044_boards_espressif_配置项参考.md)
