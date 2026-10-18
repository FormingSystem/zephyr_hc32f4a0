---
id: learning.zephyr-docs.kconfig-reference.page-219
title: "`modules/cmsis-dsp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第219章\_`modules/cmsis-dsp`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/cmsis-dsp` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_DSP"></a>

## 219.1 `CONFIG_CMSIS_DSP`

原库同名定义共 2 条；本项为数据库第 3947 条记录，各定义分别保留。

**提示（Prompt）**：CMSIS-DSP 库支持（Library Support）

**说明（Help）**

此选项启用 CMSIS-DSP 库（Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
0
```

**被选择（Selected by）**

```text
CONFIG_CMSIS_NN
CONFIG_CMSIS_NN
```

**定义位置（Location）**：[`modules/cmsis-dsp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-dsp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)。

<!-- kconfig-navigation -->

[上一章](P218_modules_acpica_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P220_modules_cmsis-nn_配置项参考.md)
