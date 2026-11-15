---
id: learning.zephyr-docs.kconfig-reference.page-428
title: "`subsys/stats`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第428章\_`subsys/stats`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/stats` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_STATS"></a>

## 428.1 `CONFIG_STATS`

**提示（Prompt）**：统计（Statistics）支持

**说明（Help）**

启用每个模块的事件计数器（Event counter），用于故障排查、维护和使用情况监测。可通过 mcumgr 管理子系统获取统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_EEPROM_SIMULATOR
CONFIG_FLASH_SIMULATOR_STATS
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL
```

**定义位置（Location）**：[`subsys/stats/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/stats/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_SIMULATOR`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SIMULATOR)、[`CONFIG_FLASH_SIMULATOR_STATS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_STATS)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL)。

<a id="CONFIG_STATS_NAMES"></a>

## 428.2 `CONFIG_STATS_NAMES`

**提示（Prompt）**：统计项名称（Statistic names）

**说明（Help）**

在构建中包含每个统计项的完整名称字符串。禁用时，统计项使用 `s0`、`s1` 等通用名称。启用可简化调试，但会增大代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS
```

**被选择（Selected by）**

```text
CONFIG_EEPROM_SIMULATOR
CONFIG_FLASH_SIMULATOR_STATS
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL
```

**被弱选择（Implied by）**

```text
CONFIG_STATS_SHELL
```

**定义位置（Location）**：[`subsys/stats/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/stats/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 统计（Statistics）支持

**配置项引用（Symbol References）**：[`CONFIG_STATS`](P428_subsys_stats_配置项参考.md#CONFIG_STATS)、[`CONFIG_EEPROM_SIMULATOR`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM_SIMULATOR)、[`CONFIG_FLASH_SIMULATOR_STATS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_STATS)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL)、[`CONFIG_STATS_SHELL`](P428_subsys_stats_配置项参考.md#CONFIG_STATS_SHELL)。

<a id="CONFIG_STATS_SHELL"></a>

## 428.3 `CONFIG_STATS_SHELL`

**提示（Prompt）**：统计命令行命令（Statistics Shell Command）

**说明（Help）**

在构建中包含每个统计项的完整名称字符串。禁用时，统计项使用 `s0`、`s1` 等通用名称。启用可简化调试，但会增大代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_SHELL
```

**弱选择（Implies）**

```text
CONFIG_STATS_NAMES
```

**定义位置（Location）**：[`subsys/stats/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/stats/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 统计（Statistics）支持

**配置项引用（Symbol References）**：[`CONFIG_STATS`](P428_subsys_stats_配置项参考.md#CONFIG_STATS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_STATS_NAMES`](P428_subsys_stats_配置项参考.md#CONFIG_STATS_NAMES)。

<!-- kconfig-navigation -->

[上一章](P427_subsys_sip_svc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P429_subsys_storage_配置项参考.md)
