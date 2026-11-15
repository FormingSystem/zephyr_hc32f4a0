---
id: learning.zephyr-docs.kconfig-reference.page-203
title: "`modules/Kconfig.intel`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第203章\_`modules/Kconfig.intel`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/Kconfig.intel` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_INTEL_HAL"></a>

## 203.1 `CONFIG_INTEL_HAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在构建过程中构建 Intel 硬件抽象层（HAL）模块。此项由架构（ARCH）Kconfig 自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
```

**定义位置（Location）**：[`modules/Kconfig.intel:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/Kconfig.intel#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ISH`。

<!-- kconfig-navigation -->

[上一章](P202_modules_Kconfig.infineon_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P204_modules_Kconfig.libmetal_配置项参考.md)
