---
id: learning.zephyr-docs.kconfig-reference.page-204
title: "`modules/Kconfig.libmetal`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第204章\_`modules/Kconfig.libmetal`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.libmetal` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LIBMETAL"></a>

## 204.1 `CONFIG_LIBMETAL`

**提示（Prompt）**：libmetal 支持（Support）

**说明（Help）**

启用 libmetal 硬件抽象层（HAL abstraction layer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_LIBMETAL_MODULE
```

**被选择（Selected by）**

```text
CONFIG_OPENAMP
```

**定义位置（Location）**：[`modules/Kconfig.libmetal:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.libmetal#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_LIBMETAL_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_LIBMETAL_MODULE)、[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_LIBMETAL_MODULE`。

<a id="CONFIG_LIBMETAL_SRC_PATH"></a>

## 204.2 `CONFIG_LIBMETAL_SRC_PATH`

**提示（Prompt）**：libmetal 库源码路径（source path）

**说明（Help）**

指定 libmetal 库的源码路径（source path）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LIBMETAL
```

**默认值（Defaults）**

```text
"libmetal"
```

**定义位置（Location）**：[`modules/Kconfig.libmetal:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.libmetal#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → libmetal 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_LIBMETAL`](P204_modules_Kconfig.libmetal_配置项参考.md#CONFIG_LIBMETAL)。

<!-- kconfig-navigation -->

[上一章](P203_modules_Kconfig.intel_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P205_modules_Kconfig.mcuboot_配置项参考.md)
