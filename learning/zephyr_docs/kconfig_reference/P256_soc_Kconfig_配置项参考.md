---
id: learning.zephyr-docs.kconfig-reference.page-256
title: "`soc/Kconfig`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第256章\_`soc/Kconfig`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/Kconfig` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_DEPRECATED_RELEASE"></a>

## 256.1 `CONFIG_SOC_DEPRECATED_RELEASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项在 SoC 配置中设置，表示将在哪个 Zephyr 发行版中删除该 SoC 配置。设置后，为该 SoC 进行的任何构建都会生成醒目的弃用警告（deprecation warning）。为 SoC 添加此项时，请记得遵循 [API 生命周期的弃用说明](https://docs.zephyrproject.org/latest/develop/api/api_lifecycle.html#deprecated)。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`soc/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_SOC_HAS_CACHE_FUNCTIONS"></a>

## 256.2 `CONFIG_SOC_HAS_CACHE_FUNCTIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 为缓存相关操作（cache related operations）提供自定义方法，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`soc/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SOC_HAS_RUNTIME_NUM_CPUS"></a>

## 256.3 `CONFIG_SOC_HAS_RUNTIME_NUM_CPUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 自行负责在运行时确定 CPU 数量（number of CPUs at runtime），应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`soc/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_SOC_HAS_TIMING_FUNCTIONS"></a>

## 256.4 `CONFIG_SOC_HAS_TIMING_FUNCTIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 为获取时间戳（timestamp）和周期计数（cycle count）提供自定义方法，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32C5
CONFIG_SOC_SERIES_ESP32P4
```

**定义位置（Location）**：[`soc/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32P4`。

<!-- kconfig-navigation -->

[上一章](P255_share_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P257_soc_Kconfig.v2_配置项参考.md)
