---
id: learning.zephyr-docs.kconfig-reference.page-257
title: "`soc/Kconfig.v2`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第257章\_`soc/Kconfig.v2`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/Kconfig.v2` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC"></a>

## 257.1 `CONFIG_SOC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统名称（SoC name）。对于硬件模型 v2（hw model v2），所选 SoC 必须定义此设置的值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SOC_FAMILY"></a>

## 257.2 `CONFIG_SOC_FAMILY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统家族（SoC family）。如果 SoC 属于某个 SoC 家族，则所选 SoC 必须定义此设置的值。通常 SoC 家族也表示 SoC 的厂商。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SOC_PART_NUMBER"></a>

## 257.3 `CONFIG_SOC_PART_NUMBER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此字符串保存 SoC 的完整器件型号（full part number）。这是隐藏选项，不应直接设置。器件型号选择项（part number selection choice）定义此字符串的默认值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SOC_SERIES"></a>

## 257.4 `CONFIG_SOC_SERIES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统系列（SoC series）。如果 SoC 属于某个共同系列，则所选 SoC 必须定义此设置的值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="SB_CONFIG_SOC"></a>

## 257.5 `SB_CONFIG_SOC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统名称（SoC name）。对于硬件模型 v2（hw model v2），所选 SoC 必须定义此设置的值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L12)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_SOC_FAMILY"></a>

## 257.6 `SB_CONFIG_SOC_FAMILY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统家族（SoC family）。如果 SoC 属于某个 SoC 家族，则所选 SoC 必须定义此设置的值。通常 SoC 家族也表示 SoC 的厂商。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L24)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_SOC_PART_NUMBER"></a>

## 257.7 `SB_CONFIG_SOC_PART_NUMBER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此字符串保存 SoC 的完整器件型号（full part number）。这是隐藏选项，不应直接设置。器件型号选择项（part number selection choice）定义此字符串的默认值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L31)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_SOC_SERIES"></a>

## 257.8 `SB_CONFIG_SOC_SERIES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

片上系统系列（SoC series）。如果 SoC 属于某个共同系列，则所选 SoC 必须定义此设置的值。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig.v2:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig.v2#L18)。

**菜单路径（Menu Path）**：顶层（Top）

<!-- kconfig-navigation -->

[上一章](P256_soc_Kconfig_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P258_soc_adi_配置项参考.md)
