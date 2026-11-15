---
id: learning.zephyr-docs.kconfig-reference.page-24
title: "`<module:picolibc>/zephyr`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第24章\_`<module:picolibc>/zephyr`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:picolibc>/zephyr` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PICOLIBC_MODULE"></a>

## 24.1 `CONFIG_PICOLIBC_MODULE`

**提示（Prompt）**：picolibc 模块支持（Module Support）

**说明（Help）**

此选项构建 picolibc 模块（Module），仅在选择 `PICOLIBC_USE_MODULE` 时使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：`<module:picolibc>/zephyr/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `picolibc`（picolibc 模块；工作区相对路径 `modules/lib/picolibc`）

<!-- kconfig-navigation -->

[上一章](P023_module_percepio_zephyr_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P025_module_xenlib_Kconfig_配置项参考.md)
