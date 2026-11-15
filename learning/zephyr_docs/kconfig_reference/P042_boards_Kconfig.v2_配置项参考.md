---
id: learning.zephyr-docs.kconfig-reference.page-42
title: "`boards/Kconfig.v2`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第42章\_`boards/Kconfig.v2`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/Kconfig.v2` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BOARD_BOARDS"></a>

## 42.1 `CONFIG_BOARD_BOARDS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于标识开发板（Board）的 Kconfig 符号（Symbol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`boards/Kconfig.v2:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L8)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_BOARDS_"></a>

## 42.2 `CONFIG_BOARD_BOARDS_`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于标识开发板目标（Board Target）的 Kconfig 符号（Symbol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`boards/Kconfig.v2:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L13)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_QUALIFIERS"></a>

## 42.3 `CONFIG_BOARD_QUALIFIERS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

包含所用开发板的限定部分（Qualifiers），不含开发板名称。例如，为 `nrf5340dk/nrf5340/cpuapp` 构建时，此值为 `nrf5340/cpuapp`。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`boards/Kconfig.v2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L18)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOARD_BOARDS"></a>

## 42.4 `SB_CONFIG_BOARD_BOARDS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于标识开发板（Board）的 Kconfig 符号（Symbol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`boards/Kconfig.v2:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L8)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOARD_BOARDS_"></a>

## 42.5 `SB_CONFIG_BOARD_BOARDS_`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于标识开发板目标（Board Target）的 Kconfig 符号（Symbol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`boards/Kconfig.v2:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L13)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOARD_QUALIFIERS"></a>

## 42.6 `SB_CONFIG_BOARD_QUALIFIERS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

包含所用开发板的限定部分（Qualifiers），不含开发板名称。例如，为 `nrf5340dk/nrf5340/cpuapp` 构建时，此值为 `nrf5340/cpuapp`。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`boards/Kconfig.v2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig.v2#L18)。

**菜单路径（Menu Path）**：顶层（Top）

<!-- kconfig-navigation -->

[上一章](P041_boards_Kconfig_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P043_boards_Kconfig.whisper_配置项参考.md)
