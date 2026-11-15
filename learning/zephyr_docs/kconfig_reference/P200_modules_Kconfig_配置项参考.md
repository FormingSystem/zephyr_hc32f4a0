---
id: learning.zephyr-docs.kconfig-reference.page-200
title: "`modules/Kconfig`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第200章\_`modules/Kconfig`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_ONLY_NO_BLOBS"></a>

## 200.1 `CONFIG_BUILD_ONLY_NO_BLOBS`

**提示（Prompt）**：仅构建模式（Build only mode），不链接二进制固件（firmware blob）

**说明（Help）**

从构建中排除二进制固件（firmware blobs）。生成的应用无法正常工作，但可以为测试目的构建需要这些固件的驱动。主要用于此类驱动的持续集成验证（CI validation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

<a id="CONFIG_TAINT_BLOBS"></a>

## 200.2 `CONFIG_TAINT_BLOBS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建时本地存在二进制文件块（binary blobs）时选择此项，以反映这些文件可能使构建带有污染标记（tainted）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_TAINT
```

**定义位置（Location）**：[`modules/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_TAINT`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_TAINT)。

<!-- kconfig-navigation -->

[上一章](P199_lib_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P201_modules_Kconfig.esp32_配置项参考.md)
