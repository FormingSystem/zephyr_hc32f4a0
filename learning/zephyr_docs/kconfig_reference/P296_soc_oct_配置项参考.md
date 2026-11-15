---
id: learning.zephyr-docs.kconfig-reference.page-296
title: "`soc/oct`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第296章\_`soc/oct`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/oct` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_OSD32MP15X"></a>

## 296.1 `CONFIG_SOC_OSD32MP15X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Octavo Systems OSD32MP15X 系统级封装（SiP）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_OSD32MP1_BRK
```

**定义位置（Location）**：[`soc/oct/osd32mp15x/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/oct/osd32mp15x/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_OSD32MP1_BRK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OSD32MP1_BRK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_OSD32MP1_BRK`。

<a id="SB_CONFIG_SOC_OSD32MP15X"></a>

## 296.2 `SB_CONFIG_SOC_OSD32MP15X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Octavo Systems OSD32MP15X 系统级封装（SiP）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_OSD32MP1_BRK
```

**定义位置（Location）**：[`soc/oct/osd32mp15x/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/oct/osd32mp15x/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_OSD32MP1_BRK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OSD32MP1_BRK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_OSD32MP1_BRK`。

<!-- kconfig-navigation -->

[上一章](P295_soc_nxp_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P297_soc_openhwgroup_配置项参考.md)
