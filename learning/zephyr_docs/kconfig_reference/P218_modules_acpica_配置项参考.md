---
id: learning.zephyr-docs.kconfig-reference.page-218
title: "`modules/acpica`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第218章\_`modules/acpica`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/acpica` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ACPI_DSDT_SUPPORT"></a>

## 218.1 `CONFIG_ACPI_DSDT_SUPPORT`

**提示（Prompt）**：构建 DSDT 的 ACPICA 支持源码（source code）

**说明（Help）**

构建差异化系统描述表（DSDT）支持源码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ACPI
```

**默认值（Defaults）**

```text
y if CONFIG_PCIE
```

**定义位置（Location）**：[`modules/acpica/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/acpica/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → acpica（模块路径 `modules/lib/acpica`，相对于 west 工作区顶层目录） → 高级配置与电源接口（ACPI）驱动支持

**配置项引用（Symbol References）**：[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<!-- kconfig-navigation -->

[上一章](P217_modules_Kconfig.xtensa_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P219_modules_cmsis-dsp_配置项参考.md)
