---
id: learning.zephyr-docs.kconfig-reference.page-45
title: "`boards/lilygo`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第45章\_`boards/lilygo`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/lilygo` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BOARD_T_DECK"></a>

## 45.1 `CONFIG_BOARD_T_DECK`

**提示（Prompt）**：LilyGO T-Deck 开发板（Board）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ESP32S3
CONFIG_SOC_ESP32S3_PROCPU if BOARD_T_DECK_ESP32S3_PROCPU
CONFIG_SOC_ESP32S3_APPCPU if BOARD_T_DECK_ESP32S3_APPCPU
```

**定义位置（Location）**：[`boards/lilygo/t_deck/Kconfig.t_deck:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/lilygo/t_deck/Kconfig.t_deck#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32S3)、[`CONFIG_SOC_ESP32S3_PROCPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32S3_PROCPU)、[`CONFIG_SOC_ESP32S3_APPCPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32S3_APPCPU)。

<a id="SB_CONFIG_BOARD_T_DECK"></a>

## 45.2 `SB_CONFIG_BOARD_T_DECK`

**提示（Prompt）**：LilyGO T-Deck 开发板（Board）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ESP32S3
SB_CONFIG_SOC_ESP32S3_PROCPU if BOARD_T_DECK_ESP32S3_PROCPU
SB_CONFIG_SOC_ESP32S3_APPCPU if BOARD_T_DECK_ESP32S3_APPCPU
```

**定义位置（Location）**：[`boards/lilygo/t_deck/Kconfig.t_deck:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/lilygo/t_deck/Kconfig.t_deck#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ESP32S3)、[`SB_CONFIG_SOC_ESP32S3_PROCPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ESP32S3_PROCPU)、[`SB_CONFIG_SOC_ESP32S3_APPCPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ESP32S3_APPCPU)。

<!-- kconfig-navigation -->

[上一章](P044_boards_espressif_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P046_boards_shields_配置项参考.md)
