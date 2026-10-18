---
id: learning.zephyr-docs.kconfig-reference.page-317
title: "`subsys/Kconfig`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第317章\_`subsys/Kconfig`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/Kconfig` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODULES"></a>

## 317.1 `CONFIG_MODULES`

**提示（Prompt）**：允许使用三态 Kconfig 选项及 `m` 选择（tristate Kconfig options）

**说明（Help）**

Zephyr 支持动态可加载代码（dynamically loadable code），例如通过 `llext` 实现。既可构建为系统映像一部分、又可作为可加载扩展（loadable extension）的代码，可以使用三态 Kconfig 选项（tristate Kconfig options）。为使其生效，项目必须启用 `CONFIG_MODULES`。仅启用此选项本身不会改变构建结果；它只是允许为三态 Kconfig 选项选择 `m`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<!-- kconfig-navigation -->

[上一章](P316_soc_xlnx_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P318_subsys_authentication_配置项参考.md)
