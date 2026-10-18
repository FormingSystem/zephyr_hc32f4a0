---
id: learning.zephyr-docs.kconfig-reference.page-221
title: "`modules/cmsis_6`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第221章\_`modules/cmsis_6`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/cmsis_6` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_CORE_HAS_SYSTEM_CORE_CLOCK"></a>

## 221.1 `CONFIG_CMSIS_CORE_HAS_SYSTEM_CORE_CLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

存在 CMSIS `SystemCoreClock` 符号（symbol）时启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_CMSIS_CORE
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`modules/cmsis_6/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis_6/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis_6（模块路径 `modules/hal/cmsis_6`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_CMSIS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CMSIS_CORE`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_CMSIS_M_CHECK_DEVICE_DEFINES"></a>

## 221.2 `CONFIG_CMSIS_M_CHECK_DEVICE_DEFINES`

**提示（Prompt）**：检查设备定义（device defines）

**说明（Help）**

启用 CMSIS 配置标志（configuration flags）的验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_CMSIS_CORE_M && CONFIG_HAS_CMSIS_CORE
```

**定义位置（Location）**：[`modules/cmsis_6/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis_6/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis_6（模块路径 `modules/hal/cmsis_6`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_CMSIS_CORE_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE_M)、[`CONFIG_HAS_CMSIS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_CMSIS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_CMSIS_CORE_M`、`CONFIG_HAS_CMSIS_CORE`。

<!-- kconfig-navigation -->

[上一章](P220_modules_cmsis-nn_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P222_modules_hal_ambiq_配置项参考.md)
