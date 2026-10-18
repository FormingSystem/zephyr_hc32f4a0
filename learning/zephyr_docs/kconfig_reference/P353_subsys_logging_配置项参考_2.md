---
id: learning.zephyr-docs.kconfig-reference.page-353
title: "`subsys/logging`配置项参考（2/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第353章\_`subsys/logging`配置项参考（2/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DBG"></a>

## 353.1 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 353.2 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_ERR"></a>

## 353.3 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INF"></a>

## 353.4 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 353.5 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_AICS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_OFF"></a>

## 353.6 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_WRN"></a>

## 353.7 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_CHOICE"></a>

## 353.8 `CONFIG_BT_AICS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AICS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AICS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AICS_LOG_LEVEL_INHERIT
CONFIG_BT_AICS_LOG_LEVEL_OFF
CONFIG_BT_AICS_LOG_LEVEL_ERR
CONFIG_BT_AICS_LOG_LEVEL_WRN
CONFIG_BT_AICS_LOG_LEVEL_INF
CONFIG_BT_AICS_LOG_LEVEL_DBG
CONFIG_BT_AICS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AICS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AICS_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AICS_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_OFF)、[`CONFIG_BT_AICS_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_ERR)、[`CONFIG_BT_AICS_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_WRN)、[`CONFIG_BT_AICS_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_INF)、[`CONFIG_BT_AICS_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_AICS_LOG_LEVEL_DBG"></a>

## 353.9 `CONFIG_BT_AICS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_DEFAULT"></a>

## 353.10 `CONFIG_BT_AICS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_ERR"></a>

## 353.11 `CONFIG_BT_AICS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_INF"></a>

## 353.12 `CONFIG_BT_AICS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_INHERIT"></a>

## 353.13 `CONFIG_BT_AICS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_AICS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_OFF"></a>

## 353.14 `CONFIG_BT_AICS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_LOG_LEVEL_WRN"></a>

## 353.15 `CONFIG_BT_AICS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频输入控制服务（Audio Input Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AICS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_CHOICE"></a>

## 353.16 `CONFIG_BT_ANS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_ANS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ANS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_ANS_LOG_LEVEL_OFF
CONFIG_BT_ANS_LOG_LEVEL_ERR
CONFIG_BT_ANS_LOG_LEVEL_WRN
CONFIG_BT_ANS_LOG_LEVEL_INF
CONFIG_BT_ANS_LOG_LEVEL_DBG
CONFIG_BT_ANS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_ANS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ANS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ANS_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_ANS_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_OFF)、[`CONFIG_BT_ANS_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_ERR)、[`CONFIG_BT_ANS_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_WRN)、[`CONFIG_BT_ANS_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_INF)、[`CONFIG_BT_ANS_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ANS_LOG_LEVEL_DBG"></a>

## 353.17 `CONFIG_BT_ANS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_DEFAULT"></a>

## 353.18 `CONFIG_BT_ANS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_ERR"></a>

## 353.19 `CONFIG_BT_ANS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_INF"></a>

## 353.20 `CONFIG_BT_ANS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_OFF"></a>

## 353.21 `CONFIG_BT_ANS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ANS_LOG_LEVEL_WRN"></a>

## 353.22 `CONFIG_BT_ANS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 警报通知服务（GATT Alert Notification Service）[实验性，EXPERIMENTAL] → 告警通知服务（Alert Notification Service (ANS)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ANS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_CHOICE"></a>

## 353.23 `CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_ASCS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_ASCS_LOG_LEVEL_INHERIT
CONFIG_BT_ASCS_LOG_LEVEL_OFF
CONFIG_BT_ASCS_LOG_LEVEL_ERR
CONFIG_BT_ASCS_LOG_LEVEL_WRN
CONFIG_BT_ASCS_LOG_LEVEL_INF
CONFIG_BT_ASCS_LOG_LEVEL_DBG
CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_ASCS`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_ASCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_ASCS_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_ASCS_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_OFF)、[`CONFIG_BT_ASCS_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_ERR)、[`CONFIG_BT_ASCS_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_WRN)、[`CONFIG_BT_ASCS_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_INF)、[`CONFIG_BT_ASCS_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_DBG"></a>

## 353.24 `CONFIG_BT_ASCS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT"></a>

## 353.25 `CONFIG_BT_ASCS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_ERR"></a>

## 353.26 `CONFIG_BT_ASCS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_INF"></a>

## 353.27 `CONFIG_BT_ASCS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_INHERIT"></a>

## 353.28 `CONFIG_BT_ASCS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_ASCS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_OFF"></a>

## 353.29 `CONFIG_BT_ASCS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ASCS_LOG_LEVEL_WRN"></a>

## 353.30 `CONFIG_BT_ASCS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ASCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音频流控制服务（Audio Stream Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ASCS_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ASCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_CHOICE"></a>

## 353.31 `CONFIG_BT_ATT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ATT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_ATT_LOG_LEVEL_INHERIT
CONFIG_BT_ATT_LOG_LEVEL_OFF
CONFIG_BT_ATT_LOG_LEVEL_ERR
CONFIG_BT_ATT_LOG_LEVEL_WRN
CONFIG_BT_ATT_LOG_LEVEL_INF
CONFIG_BT_ATT_LOG_LEVEL_DBG
CONFIG_BT_ATT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ATT_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_ATT_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_ATT_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_OFF)、[`CONFIG_BT_ATT_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_ERR)、[`CONFIG_BT_ATT_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_WRN)、[`CONFIG_BT_ATT_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_INF)、[`CONFIG_BT_ATT_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_ATT_LOG_LEVEL_DBG"></a>

## 353.32 `CONFIG_BT_ATT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_DEFAULT"></a>

## 353.33 `CONFIG_BT_ATT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_ERR"></a>

## 353.34 `CONFIG_BT_ATT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_INF"></a>

## 353.35 `CONFIG_BT_ATT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_INHERIT"></a>

## 353.36 `CONFIG_BT_ATT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_ATT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_OFF"></a>

## 353.37 `CONFIG_BT_ATT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ATT_LOG_LEVEL_WRN"></a>

## 353.38 `CONFIG_BT_ATT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙属性协议（Bluetooth Attribute Protocol (ATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ATT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_ATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE"></a>

## 353.39 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_STREAM && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INHERIT
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_OFF
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_ERR
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_WRN
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INF
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DBG
CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_STREAM)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_OFF)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_ERR)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_WRN)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INF)、[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_STREAM`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DBG"></a>

## 353.40 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT"></a>

## 353.41 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_ERR"></a>

## 353.42 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INF"></a>

## 353.43 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INHERIT"></a>

## 353.44 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_OFF"></a>

## 353.45 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_WRN"></a>

## 353.46 `CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙音频编解码器（Bluetooth Audio Codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE"></a>

## 353.47 `CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AUDIO_LOG_LEVEL_OFF
CONFIG_BT_AUDIO_LOG_LEVEL_ERR
CONFIG_BT_AUDIO_LOG_LEVEL_WRN
CONFIG_BT_AUDIO_LOG_LEVEL_INF
CONFIG_BT_AUDIO_LOG_LEVEL_DBG
CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AUDIO_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_OFF)、[`CONFIG_BT_AUDIO_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_ERR)、[`CONFIG_BT_AUDIO_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_WRN)、[`CONFIG_BT_AUDIO_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_INF)、[`CONFIG_BT_AUDIO_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_DBG"></a>

## 353.48 `CONFIG_BT_AUDIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT"></a>

## 353.49 `CONFIG_BT_AUDIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_ERR"></a>

## 353.50 `CONFIG_BT_AUDIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_INF"></a>

## 353.51 `CONFIG_BT_AUDIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_OFF"></a>

## 353.52 `CONFIG_BT_AUDIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AUDIO_LOG_LEVEL_WRN"></a>

## 353.53 `CONFIG_BT_AUDIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙音频（Bluetooth Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE"></a>

## 353.54 `CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AVCTP_LOG_LEVEL_INHERIT
CONFIG_BT_AVCTP_LOG_LEVEL_OFF
CONFIG_BT_AVCTP_LOG_LEVEL_ERR
CONFIG_BT_AVCTP_LOG_LEVEL_WRN
CONFIG_BT_AVCTP_LOG_LEVEL_INF
CONFIG_BT_AVCTP_LOG_LEVEL_DBG
CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AVCTP_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AVCTP_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_OFF)、[`CONFIG_BT_AVCTP_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_ERR)、[`CONFIG_BT_AVCTP_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_WRN)、[`CONFIG_BT_AVCTP_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_INF)、[`CONFIG_BT_AVCTP_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_DBG"></a>

## 353.55 `CONFIG_BT_AVCTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT"></a>

## 353.56 `CONFIG_BT_AVCTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_ERR"></a>

## 353.57 `CONFIG_BT_AVCTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_INF"></a>

## 353.58 `CONFIG_BT_AVCTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_INHERIT"></a>

## 353.59 `CONFIG_BT_AVCTP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_AVCTP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_OFF"></a>

## 353.60 `CONFIG_BT_AVCTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVCTP_LOG_LEVEL_WRN"></a>

## 353.61 `CONFIG_BT_AVCTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频控制传输协议（Bluetooth AVCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE"></a>

## 353.62 `CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AVDTP_LOG_LEVEL_INHERIT
CONFIG_BT_AVDTP_LOG_LEVEL_OFF
CONFIG_BT_AVDTP_LOG_LEVEL_ERR
CONFIG_BT_AVDTP_LOG_LEVEL_WRN
CONFIG_BT_AVDTP_LOG_LEVEL_INF
CONFIG_BT_AVDTP_LOG_LEVEL_DBG
CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AVDTP_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AVDTP_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_OFF)、[`CONFIG_BT_AVDTP_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_ERR)、[`CONFIG_BT_AVDTP_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_WRN)、[`CONFIG_BT_AVDTP_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_INF)、[`CONFIG_BT_AVDTP_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_DBG"></a>

## 353.63 `CONFIG_BT_AVDTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT"></a>

## 353.64 `CONFIG_BT_AVDTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_ERR"></a>

## 353.65 `CONFIG_BT_AVDTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_INF"></a>

## 353.66 `CONFIG_BT_AVDTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_INHERIT"></a>

## 353.67 `CONFIG_BT_AVDTP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_AVDTP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_OFF"></a>

## 353.68 `CONFIG_BT_AVDTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVDTP_LOG_LEVEL_WRN"></a>

## 353.69 `CONFIG_BT_AVDTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频分发传输协议调试（Bluetooth AVDTP debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVDTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE"></a>

## 353.70 `CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AVRCP_LOG_LEVEL_INHERIT
CONFIG_BT_AVRCP_LOG_LEVEL_OFF
CONFIG_BT_AVRCP_LOG_LEVEL_ERR
CONFIG_BT_AVRCP_LOG_LEVEL_WRN
CONFIG_BT_AVRCP_LOG_LEVEL_INF
CONFIG_BT_AVRCP_LOG_LEVEL_DBG
CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AVRCP_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AVRCP_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_OFF)、[`CONFIG_BT_AVRCP_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_ERR)、[`CONFIG_BT_AVRCP_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_WRN)、[`CONFIG_BT_AVRCP_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_INF)、[`CONFIG_BT_AVRCP_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_DBG"></a>

## 353.71 `CONFIG_BT_AVRCP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT"></a>

## 353.72 `CONFIG_BT_AVRCP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_ERR"></a>

## 353.73 `CONFIG_BT_AVRCP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_INF"></a>

## 353.74 `CONFIG_BT_AVRCP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_INHERIT"></a>

## 353.75 `CONFIG_BT_AVRCP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_AVRCP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_OFF"></a>

## 353.76 `CONFIG_BT_AVRCP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AVRCP_LOG_LEVEL_WRN"></a>

## 353.77 `CONFIG_BT_AVRCP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙音视频远程控制配置文件（Bluetooth AVRCP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AVRCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE"></a>

## 353.78 `CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_BASE && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_BASE_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_BASE_LOG_LEVEL_OFF
CONFIG_BT_BAP_BASE_LOG_LEVEL_ERR
CONFIG_BT_BAP_BASE_LOG_LEVEL_WRN
CONFIG_BT_BAP_BASE_LOG_LEVEL_INF
CONFIG_BT_BAP_BASE_LOG_LEVEL_DBG
CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_BASE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BASE)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_BASE_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_BAP_BASE`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_DBG"></a>

## 353.79 `CONFIG_BT_BAP_BASE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT"></a>

## 353.80 `CONFIG_BT_BAP_BASE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_ERR"></a>

## 353.81 `CONFIG_BT_BAP_BASE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_INF"></a>

## 353.82 `CONFIG_BT_BAP_BASE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_INHERIT"></a>

## 353.83 `CONFIG_BT_BAP_BASE_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_BASE_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_OFF"></a>

## 353.84 `CONFIG_BT_BAP_BASE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BASE_LOG_LEVEL_WRN"></a>

## 353.85 `CONFIG_BT_BAP_BASE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙基本音频配置文件的广播音频源端点（Bluetooth Basic Audio Profile Broadcast Audio Source Endpoint）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BASE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE"></a>

## 353.86 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_BROADCAST_ASSISTANT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_OFF
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_ERR
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_WRN
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INF
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG
CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG"></a>

## 353.87 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT"></a>

## 353.88 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_ERR"></a>

## 353.89 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INF"></a>

## 353.90 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INHERIT"></a>

## 353.91 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_OFF"></a>

## 353.92 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_WRN"></a>

## 353.93 `CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 广播音频扫描服务客户端调试（Broadcast Audio Scan Service client debug）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE"></a>

## 353.94 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_BAP_BROADCAST_SINK && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INHERIT
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_OFF
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_ERR
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_WRN
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INF
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DBG
CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_BAP_BROADCAST_SINK`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_BAP_BROADCAST_SINK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INHERIT)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_OFF)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_ERR)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_WRN`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_WRN)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INF)、[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DBG"></a>

## 353.95 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT"></a>

## 353.96 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_ERR"></a>

## 353.97 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INF"></a>

## 353.98 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INHERIT"></a>

## 353.99 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_OFF"></a>

## 353.100 `CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 蓝牙广播音频接收端（Bluetooth Audio Broadcast Sink）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_BAP_BROADCAST_SINK_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P352_subsys_logging_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P354_subsys_logging_配置项参考_3.md)
