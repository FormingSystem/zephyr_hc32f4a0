---
id: learning.zephyr-docs.kconfig-reference.page-214
title: "`modules/Kconfig.syst`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第214章\_`modules/Kconfig.syst`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.syst` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MIPI_SYST_LIB"></a>

## 214.1 `CONFIG_MIPI_SYST_LIB`

**提示（Prompt）**：MIPI SyS-T 库支持（Library Support）

**说明（Help）**

启用 MIPI SyS-T 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE
```

**定义位置（Location）**：[`modules/Kconfig.syst:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.syst#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MIPI_SYST_ENABLE)。

<a id="CONFIG_MIPI_SYST_NO_WHCAR"></a>

## 214.2 `CONFIG_MIPI_SYST_NO_WHCAR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

要求 MIPI SyS-T 库构建时不包含宽字符（wchar）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_SYST_LIB
```

**默认值（Defaults）**

```text
y if CONFIG_MINIMAL_LIBC
```

**定义位置（Location）**：[`modules/Kconfig.syst:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.syst#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MIPI SyS-T 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_SYST_LIB`](P214_modules_Kconfig.syst_配置项参考.md#CONFIG_MIPI_SYST_LIB)、[`CONFIG_MINIMAL_LIBC`](P197_lib_配置项参考_1.md#CONFIG_MINIMAL_LIBC)。

<a id="CONFIG_MIPI_SYST_RAW_DATA"></a>

## 214.3 `CONFIG_MIPI_SYST_RAW_DATA`

**提示（Prompt）**：输出 MIPI SyS-T 原始数据包（raw data packet）

**说明（Help）**

输出 MIPI SyS-T 原始数据包（raw data packet）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_SYST_LIB
```

**定义位置（Location）**：[`modules/Kconfig.syst:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.syst#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MIPI SyS-T 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_SYST_LIB`](P214_modules_Kconfig.syst_配置项参考.md#CONFIG_MIPI_SYST_LIB)。

<a id="CONFIG_MIPI_SYST_STP"></a>

## 214.4 `CONFIG_MIPI_SYST_STP`

**提示（Prompt）**：MIPI SyS-T 的 STP 传输层（Transport Layer）

**说明（Help）**

启用 MIPI SyS-T 的 STP 传输层（Transport Layer）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_SYST_LIB
```

**定义位置（Location）**：[`modules/Kconfig.syst:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.syst#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MIPI SyS-T 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_SYST_LIB`](P214_modules_Kconfig.syst_配置项参考.md#CONFIG_MIPI_SYST_LIB)。

<!-- kconfig-navigation -->

[上一章](P213_modules_Kconfig.stm32_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P215_modules_Kconfig.telink_配置项参考.md)
