---
id: learning.zephyr-docs.kconfig-reference.page-272
title: "`soc/egis`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第272章\_`soc/egis`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/egis` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_EGIS_ET171"></a>

## 272.1 `CONFIG_SOC_EGIS_ET171`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Egis ET171 片上系统实现（SoC implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_EGIS_ET171
```

**定义位置（Location）**：[`soc/egis/et171/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/egis/et171/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EGIS_ET171)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EGIS_ET171`。

<a id="CONFIG_SOC_EGIS_ET171_FIRMWARE_VERSION"></a>

## 272.2 `CONFIG_SOC_EGIS_ET171_FIRMWARE_VERSION`

**提示（Prompt）**：固件版本（Firmware Version）

**说明（Help）**

二进制头部中的固件版本信息（Firmware version info）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EGIS_ET171
```

**默认值（Defaults）**

```text
0xAAAAAAAA
```

**定义位置（Location）**：[`soc/egis/et171/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/egis/et171/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EGIS_ET171`](P272_soc_egis_配置项参考.md#CONFIG_SOC_EGIS_ET171)。

<a id="CONFIG_SOC_EGIS_ET171_VENDOR_FIRMWARE_SIZE"></a>

## 272.3 `CONFIG_SOC_EGIS_ET171_VENDOR_FIRMWARE_SIZE`

**提示（Prompt）**：二进制头部中的固件大小（firmware size）

**说明（Help）**

自定义二进制头部中的固件大小信息（firmware size info）。为零时不使用。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_EGIS_ET171
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/egis/et171/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/egis/et171/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EGIS_ET171`](P272_soc_egis_配置项参考.md#CONFIG_SOC_EGIS_ET171)。

<a id="SB_CONFIG_SOC_EGIS_ET171"></a>

## 272.4 `SB_CONFIG_SOC_EGIS_ET171`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Egis ET171 片上系统实现（SoC implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EGIS_ET171
```

**定义位置（Location）**：[`soc/egis/et171/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/egis/et171/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EGIS_ET171)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EGIS_ET171`。

<!-- kconfig-navigation -->

[上一章](P271_soc_efinix_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P273_soc_elan_配置项参考.md)
