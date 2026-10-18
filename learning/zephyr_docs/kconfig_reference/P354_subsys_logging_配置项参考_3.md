---
id: learning.zephyr-docs.kconfig-reference.page-354
title: "`subsys/logging`配置项参考（3/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第354章\_`subsys/logging`配置项参考（3/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_WRN"></a>

## 354.1 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE"></a>

## 354.2 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_BROADCAST_SOURCE && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_OFF
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_ERR
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_WRN
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INF
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DBG
CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_BROADCAST_SOURCE`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SOURCE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DBG"></a>

## 354.3 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT"></a>

## 354.4 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_ERR"></a>

## 354.5 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INF"></a>

## 354.6 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INHERIT"></a>

## 354.7 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_OFF"></a>

## 354.8 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_WRN"></a>

## 354.9 `CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频源（Bluetooth Audio Broadcast Source）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SOURCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE"></a>

## 354.10 `CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_ISO_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_ISO_LOG_LEVEL_OFF
CONFIG_BT_BAP_ISO_LOG_LEVEL_ERR
CONFIG_BT_BAP_ISO_LOG_LEVEL_WRN
CONFIG_BT_BAP_ISO_LOG_LEVEL_INF
CONFIG_BT_BAP_ISO_LOG_LEVEL_DBG
CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_ISO_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_DBG"></a>

## 354.11 `CONFIG_BT_BAP_ISO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT"></a>

## 354.12 `CONFIG_BT_BAP_ISO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_ERR"></a>

## 354.13 `CONFIG_BT_BAP_ISO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_INF"></a>

## 354.14 `CONFIG_BT_BAP_ISO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_INHERIT"></a>

## 354.15 `CONFIG_BT_BAP_ISO_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_ISO_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_OFF"></a>

## 354.16 `CONFIG_BT_BAP_ISO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_ISO_LOG_LEVEL_WRN"></a>

## 354.17 `CONFIG_BT_BAP_ISO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频等时传输（Bluetooth Audio ISO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE"></a>

## 354.18 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_SCAN_DELEGATOR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_OFF
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_ERR
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_WRN
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INF
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG
CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_SCAN_DELEGATOR`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_SCAN_DELEGATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG"></a>

## 354.19 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT"></a>

## 354.20 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_ERR"></a>

## 354.21 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INF"></a>

## 354.22 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INHERIT"></a>

## 354.23 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_OFF"></a>

## 354.24 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_WRN"></a>

## 354.25 `CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务（Broadcast Audio Scan Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE"></a>

## 354.26 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_STREAM_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_STREAM_LOG_LEVEL_OFF
CONFIG_BT_BAP_STREAM_LOG_LEVEL_ERR
CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN
CONFIG_BT_BAP_STREAM_LOG_LEVEL_INF
CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG
CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG"></a>

## 354.27 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT"></a>

## 354.28 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_ERR"></a>

## 354.29 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_INF"></a>

## 354.30 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_INHERIT"></a>

## 354.31 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_STREAM_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_OFF"></a>

## 354.32 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN"></a>

## 354.33 `CONFIG_BT_BAP_STREAM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频流（Bluetooth Audio Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE"></a>

## 354.34 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_UNICAST_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INF
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_UNICAST_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DBG"></a>

## 354.35 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 354.36 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_ERR"></a>

## 354.37 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INF"></a>

## 354.38 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INHERIT"></a>

## 354.39 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_OFF"></a>

## 354.40 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_WRN"></a>

## 354.41 `CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 基本音频配置文件（Basic Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE"></a>

## 354.42 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_UNICAST_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_OFF
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_ERR
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_WRN
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INF
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DBG
CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DBG"></a>

## 354.43 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT"></a>

## 354.44 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_ERR"></a>

## 354.45 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INF"></a>

## 354.46 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INHERIT"></a>

## 354.47 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_OFF"></a>

## 354.48 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_WRN"></a>

## 354.49 `CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频单播服务器（Bluetooth Audio Unicast Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_UNICAST_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_CHOICE"></a>

## 354.50 `CONFIG_BT_BAS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAS_LOG_LEVEL_OFF
CONFIG_BT_BAS_LOG_LEVEL_ERR
CONFIG_BT_BAS_LOG_LEVEL_WRN
CONFIG_BT_BAS_LOG_LEVEL_INF
CONFIG_BT_BAS_LOG_LEVEL_DBG
CONFIG_BT_BAS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAS`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAS_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAS_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_OFF)、[`CONFIG_BT_BAS_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_ERR)、[`CONFIG_BT_BAS_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_WRN)、[`CONFIG_BT_BAS_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_INF)、[`CONFIG_BT_BAS_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAS_LOG_LEVEL_DBG"></a>

## 354.51 `CONFIG_BT_BAS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_DEFAULT"></a>

## 354.52 `CONFIG_BT_BAS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_ERR"></a>

## 354.53 `CONFIG_BT_BAS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_INF"></a>

## 354.54 `CONFIG_BT_BAS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_OFF"></a>

## 354.55 `CONFIG_BT_BAS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAS_LOG_LEVEL_WRN"></a>

## 354.56 `CONFIG_BT_BAS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 电池服务（BAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAS_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_CHOICE"></a>

## 354.57 `CONFIG_BT_BIP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BIP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BIP_LOG_LEVEL_INHERIT
CONFIG_BT_BIP_LOG_LEVEL_OFF
CONFIG_BT_BIP_LOG_LEVEL_ERR
CONFIG_BT_BIP_LOG_LEVEL_WRN
CONFIG_BT_BIP_LOG_LEVEL_INF
CONFIG_BT_BIP_LOG_LEVEL_DBG
CONFIG_BT_BIP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BIP_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BIP_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BIP_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_OFF)、[`CONFIG_BT_BIP_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_ERR)、[`CONFIG_BT_BIP_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_WRN)、[`CONFIG_BT_BIP_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_INF)、[`CONFIG_BT_BIP_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BIP_LOG_LEVEL_DBG"></a>

## 354.58 `CONFIG_BT_BIP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_DEFAULT"></a>

## 354.59 `CONFIG_BT_BIP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_ERR"></a>

## 354.60 `CONFIG_BT_BIP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_INF"></a>

## 354.61 `CONFIG_BT_BIP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_INHERIT"></a>

## 354.62 `CONFIG_BT_BIP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_BIP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_OFF"></a>

## 354.63 `CONFIG_BT_BIP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BIP_LOG_LEVEL_WRN"></a>

## 354.64 `CONFIG_BT_BIP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙基本图像配置文件（Bluetooth Basic Imaging Profile (BIP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BIP_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE"></a>

## 354.65 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CAP_ACCEPTOR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_OFF
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_ERR
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_WRN
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INF
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DBG
CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CAP_ACCEPTOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_ACCEPTOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DBG"></a>

## 354.66 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT"></a>

## 354.67 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_ERR"></a>

## 354.68 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INF"></a>

## 354.69 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INHERIT"></a>

## 354.70 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_OFF"></a>

## 354.71 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_WRN"></a>

## 354.72 `CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件接受方（Common Audio Profile Acceptor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_ACCEPTOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE"></a>

## 354.73 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CAP_COMMANDER && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_OFF
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_ERR
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_WRN
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INF
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DBG
CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CAP_COMMANDER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_COMMANDER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DBG"></a>

## 354.74 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT"></a>

## 354.75 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_ERR"></a>

## 354.76 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INF"></a>

## 354.77 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INHERIT"></a>

## 354.78 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_OFF"></a>

## 354.79 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_WRN"></a>

## 354.80 `CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件命令方（Common Audio Profile Commander）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMANDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE"></a>

## 354.81 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_COMMON_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_COMMON_LOG_LEVEL_OFF
CONFIG_BT_CAP_COMMON_LOG_LEVEL_ERR
CONFIG_BT_CAP_COMMON_LOG_LEVEL_WRN
CONFIG_BT_CAP_COMMON_LOG_LEVEL_INF
CONFIG_BT_CAP_COMMON_LOG_LEVEL_DBG
CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_DBG"></a>

## 354.82 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT"></a>

## 354.83 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_ERR"></a>

## 354.84 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_INF"></a>

## 354.85 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_INHERIT"></a>

## 354.86 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_COMMON_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_OFF"></a>

## 354.87 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_COMMON_LOG_LEVEL_WRN"></a>

## 354.88 `CONFIG_BT_CAP_COMMON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件公共部分（Common Audio Profile Common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE"></a>

## 354.89 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CAP_HANDOVER && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_OFF
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_ERR
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_WRN
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INF
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DBG
CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CAP_HANDOVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_HANDOVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INHERIT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_OFF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INF`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DBG"></a>

## 354.90 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT"></a>

## 354.91 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_ERR"></a>

## 354.92 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INF"></a>

## 354.93 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INHERIT"></a>

## 354.94 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_OFF"></a>

## 354.95 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_WRN"></a>

## 354.96 `CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件移交（Common Audio Profile Handover）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_HANDOVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE"></a>

## 354.97 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CAP_INITIATOR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_OFF
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_ERR
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_WRN
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INF
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DBG
CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CAP_INITIATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CAP_INITIATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_ERR`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DBG`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DBG"></a>

## 354.98 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT"></a>

## 354.99 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_ERR"></a>

## 354.100 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P353_subsys_logging_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P355_subsys_logging_配置项参考_4.md)
