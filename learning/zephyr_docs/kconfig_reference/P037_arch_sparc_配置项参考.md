---
id: learning.zephyr-docs.kconfig-reference.page-37
title: "`arch/sparc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第37章\_`arch/sparc`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/sparc` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SPARC_CASA"></a>

## 37.1 `CONFIG_SPARC_CASA`

**提示（Prompt）**：CASA 指令（Instructions）

**说明（Help）**

使用 CASA 原子指令（Atomic Instruction）。这些指令由 SPARC V9 定义，部分 LEON 处理器提供支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPARC
```

**定义位置（Location）**：[`arch/sparc/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/sparc/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → SPARC 选项（SPARC Options）

**配置项引用（Symbol References）**：[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)。

<a id="CONFIG_SPARC_NWIN"></a>

## 37.2 `CONFIG_SPARC_NWIN`

**提示（Prompt）**：寄存器窗口数量（Number of Register Windows）

**说明（Help）**

硬件实现的寄存器窗口（Register Window）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPARC
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`arch/sparc/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/sparc/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → SPARC 选项（SPARC Options）

**配置项引用（Symbol References）**：[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)。

<a id="CONFIG_SPARC_SVT"></a>

## 37.3 `CONFIG_SPARC_SVT`

**提示（Prompt）**：单向量陷阱处理（Single-Vector Trapping）

**说明（Help）**

使用单向量陷阱处理（Single-Vector Trapping，SVT）。该机制由《SPARC-V8 嵌入式架构规范》（SPARC-V8 Embedded，V8E）定义，部分 LEON 处理器提供支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPARC
```

**定义位置（Location）**：[`arch/sparc/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/sparc/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → SPARC 选项（SPARC Options）

**配置项引用（Symbol References）**：[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)。

<!-- kconfig-navigation -->

[上一章](P036_arch_rx_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P038_arch_tricore_配置项参考.md)
