---
id: learning.zephyr-docs.kconfig-reference.page-360
title: "`subsys/logging`配置项参考（9/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第360章\_`subsys/logging`配置项参考（9/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_RPA_LOG_LEVEL_DBG"></a>

## 360.1 `CONFIG_BT_RPA_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_DEFAULT"></a>

## 360.2 `CONFIG_BT_RPA_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_ERR"></a>

## 360.3 `CONFIG_BT_RPA_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_INF"></a>

## 360.4 `CONFIG_BT_RPA_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_INHERIT"></a>

## 360.5 `CONFIG_BT_RPA_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 选择项（Choice）：`BT_RPA_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_OFF"></a>

## 360.6 `CONFIG_BT_RPA_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_WRN"></a>

## 360.7 `CONFIG_BT_RPA_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RPA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RPA_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RPA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_CHOICE"></a>

## 360.8 `CONFIG_BT_SDP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_SDP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_SDP_LOG_LEVEL_INHERIT
CONFIG_BT_SDP_LOG_LEVEL_OFF
CONFIG_BT_SDP_LOG_LEVEL_ERR
CONFIG_BT_SDP_LOG_LEVEL_WRN
CONFIG_BT_SDP_LOG_LEVEL_INF
CONFIG_BT_SDP_LOG_LEVEL_DBG
CONFIG_BT_SDP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SDP_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_SDP_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_SDP_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_OFF)、[`CONFIG_BT_SDP_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_ERR)、[`CONFIG_BT_SDP_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_WRN)、[`CONFIG_BT_SDP_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_INF)、[`CONFIG_BT_SDP_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_SDP_LOG_LEVEL_DBG"></a>

## 360.9 `CONFIG_BT_SDP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_DEFAULT"></a>

## 360.10 `CONFIG_BT_SDP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_ERR"></a>

## 360.11 `CONFIG_BT_SDP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_INF"></a>

## 360.12 `CONFIG_BT_SDP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_INHERIT"></a>

## 360.13 `CONFIG_BT_SDP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_SDP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_OFF"></a>

## 360.14 `CONFIG_BT_SDP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SDP_LOG_LEVEL_WRN"></a>

## 360.15 `CONFIG_BT_SDP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙服务发现协议（Bluetooth Service Discovery Protocol (SDP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SDP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE"></a>

## 360.16 `CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_SERVICE_LOG_LEVEL_INHERIT
CONFIG_BT_SERVICE_LOG_LEVEL_OFF
CONFIG_BT_SERVICE_LOG_LEVEL_ERR
CONFIG_BT_SERVICE_LOG_LEVEL_WRN
CONFIG_BT_SERVICE_LOG_LEVEL_INF
CONFIG_BT_SERVICE_LOG_LEVEL_DBG
CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_SERVICE_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_INHERIT)、[`CONFIG_BT_SERVICE_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_OFF)、[`CONFIG_BT_SERVICE_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_ERR)、[`CONFIG_BT_SERVICE_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_WRN)、[`CONFIG_BT_SERVICE_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_INF)、[`CONFIG_BT_SERVICE_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_DBG"></a>

## 360.17 `CONFIG_BT_SERVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT"></a>

## 360.18 `CONFIG_BT_SERVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_ERR"></a>

## 360.19 `CONFIG_BT_SERVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_INF"></a>

## 360.20 `CONFIG_BT_SERVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_INHERIT"></a>

## 360.21 `CONFIG_BT_SERVICE_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_SERVICE_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_OFF"></a>

## 360.22 `CONFIG_BT_SERVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SERVICE_LOG_LEVEL_WRN"></a>

## 360.23 `CONFIG_BT_SERVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙服务（Bluetooth Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE"></a>

## 360.24 `CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_SETTINGS_LOG_LEVEL_INHERIT
CONFIG_BT_SETTINGS_LOG_LEVEL_OFF
CONFIG_BT_SETTINGS_LOG_LEVEL_ERR
CONFIG_BT_SETTINGS_LOG_LEVEL_WRN
CONFIG_BT_SETTINGS_LOG_LEVEL_INF
CONFIG_BT_SETTINGS_LOG_LEVEL_DBG
CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_OFF)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_ERR)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_WRN)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_INF)、[`CONFIG_BT_SETTINGS_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_DBG"></a>

## 360.25 `CONFIG_BT_SETTINGS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT"></a>

## 360.26 `CONFIG_BT_SETTINGS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_ERR"></a>

## 360.27 `CONFIG_BT_SETTINGS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_INF"></a>

## 360.28 `CONFIG_BT_SETTINGS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_INHERIT"></a>

## 360.29 `CONFIG_BT_SETTINGS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_SETTINGS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_OFF"></a>

## 360.30 `CONFIG_BT_SETTINGS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SETTINGS_LOG_LEVEL_WRN"></a>

## 360.31 `CONFIG_BT_SETTINGS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙存储（Bluetooth storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_CHOICE"></a>

## 360.32 `CONFIG_BT_SMP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_SMP && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_SMP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_SMP_LOG_LEVEL_INHERIT
CONFIG_BT_SMP_LOG_LEVEL_OFF
CONFIG_BT_SMP_LOG_LEVEL_ERR
CONFIG_BT_SMP_LOG_LEVEL_WRN
CONFIG_BT_SMP_LOG_LEVEL_INF
CONFIG_BT_SMP_LOG_LEVEL_DBG
CONFIG_BT_SMP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_SMP`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SMP)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SMP_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_SMP_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_SMP_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_OFF)、[`CONFIG_BT_SMP_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_ERR)、[`CONFIG_BT_SMP_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_WRN)、[`CONFIG_BT_SMP_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_INF)、[`CONFIG_BT_SMP_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_SMP_LOG_LEVEL_DBG"></a>

## 360.33 `CONFIG_BT_SMP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_DEFAULT"></a>

## 360.34 `CONFIG_BT_SMP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_ERR"></a>

## 360.35 `CONFIG_BT_SMP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_INF"></a>

## 360.36 `CONFIG_BT_SMP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_INHERIT"></a>

## 360.37 `CONFIG_BT_SMP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_SMP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_OFF"></a>

## 360.38 `CONFIG_BT_SMP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_SMP_LOG_LEVEL_WRN"></a>

## 360.39 `CONFIG_BT_SMP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_SMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全管理协议（Bluetooth Security Manager Protocol）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_SMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 360.40 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_TBS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_TBS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_TBS_CLIENT`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG"></a>

## 360.41 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 360.42 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_ERR"></a>

## 360.43 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INF"></a>

## 360.44 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 360.45 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_TBS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_OFF"></a>

## 360.46 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_CLIENT_LOG_LEVEL_WRN"></a>

## 360.47 `CONFIG_BT_TBS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务客户端（Telephone Bearer Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_CHOICE"></a>

## 360.48 `CONFIG_BT_TBS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_TBS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TBS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_TBS_LOG_LEVEL_INHERIT
CONFIG_BT_TBS_LOG_LEVEL_OFF
CONFIG_BT_TBS_LOG_LEVEL_ERR
CONFIG_BT_TBS_LOG_LEVEL_WRN
CONFIG_BT_TBS_LOG_LEVEL_INF
CONFIG_BT_TBS_LOG_LEVEL_DBG
CONFIG_BT_TBS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_TBS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TBS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TBS_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_TBS_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_TBS_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_OFF)、[`CONFIG_BT_TBS_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_ERR)、[`CONFIG_BT_TBS_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_WRN)、[`CONFIG_BT_TBS_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_INF)、[`CONFIG_BT_TBS_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_TBS_LOG_LEVEL_DBG"></a>

## 360.49 `CONFIG_BT_TBS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_DEFAULT"></a>

## 360.50 `CONFIG_BT_TBS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_ERR"></a>

## 360.51 `CONFIG_BT_TBS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_INF"></a>

## 360.52 `CONFIG_BT_TBS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_INHERIT"></a>

## 360.53 `CONFIG_BT_TBS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_TBS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_OFF"></a>

## 360.54 `CONFIG_BT_TBS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TBS_LOG_LEVEL_WRN"></a>

## 360.55 `CONFIG_BT_TBS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TBS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 电话承载服务（Telephone Bearer Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TBS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TBS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_CHOICE"></a>

## 360.56 `CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_TMAP_LOG_LEVEL_INHERIT
CONFIG_BT_TMAP_LOG_LEVEL_OFF
CONFIG_BT_TMAP_LOG_LEVEL_ERR
CONFIG_BT_TMAP_LOG_LEVEL_WRN
CONFIG_BT_TMAP_LOG_LEVEL_INF
CONFIG_BT_TMAP_LOG_LEVEL_DBG
CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_TMAP_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_TMAP_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_OFF)、[`CONFIG_BT_TMAP_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_ERR)、[`CONFIG_BT_TMAP_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_WRN)、[`CONFIG_BT_TMAP_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_INF)、[`CONFIG_BT_TMAP_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_DBG"></a>

## 360.57 `CONFIG_BT_TMAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT"></a>

## 360.58 `CONFIG_BT_TMAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_ERR"></a>

## 360.59 `CONFIG_BT_TMAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_INF"></a>

## 360.60 `CONFIG_BT_TMAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_INHERIT"></a>

## 360.61 `CONFIG_BT_TMAP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 选择项（Choice）：`BT_TMAP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_OFF"></a>

## 360.62 `CONFIG_BT_TMAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TMAP_LOG_LEVEL_WRN"></a>

## 360.63 `CONFIG_BT_TMAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 电话与媒体音频配置文件（Telephony and Media Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TMAP_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_CHOICE"></a>

## 360.64 `CONFIG_BT_TPS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_TPS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_TPS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_TPS_LOG_LEVEL_OFF
CONFIG_BT_TPS_LOG_LEVEL_ERR
CONFIG_BT_TPS_LOG_LEVEL_WRN
CONFIG_BT_TPS_LOG_LEVEL_INF
CONFIG_BT_TPS_LOG_LEVEL_DBG
CONFIG_BT_TPS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_TPS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_TPS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_TPS_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_TPS_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_OFF)、[`CONFIG_BT_TPS_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_ERR)、[`CONFIG_BT_TPS_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_WRN)、[`CONFIG_BT_TPS_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_INF)、[`CONFIG_BT_TPS_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_TPS_LOG_LEVEL_DBG"></a>

## 360.65 `CONFIG_BT_TPS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_DEFAULT"></a>

## 360.66 `CONFIG_BT_TPS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_ERR"></a>

## 360.67 `CONFIG_BT_TPS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_INF"></a>

## 360.68 `CONFIG_BT_TPS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_OFF"></a>

## 360.69 `CONFIG_BT_TPS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_TPS_LOG_LEVEL_WRN"></a>

## 360.70 `CONFIG_BT_TPS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_TPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 发射功率服务（TPS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_TPS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_TPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE"></a>

## 360.71 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_VCP_VOL_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INHERIT
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_OFF
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_ERR
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_WRN
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INF
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DBG
CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_VCP_VOL_CTLR`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_OFF)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_ERR)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_WRN)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INF)、[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DBG"></a>

## 360.72 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT"></a>

## 360.73 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_ERR"></a>

## 360.74 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INF"></a>

## 360.75 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INHERIT"></a>

## 360.76 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_OFF"></a>

## 360.77 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_WRN"></a>

## 360.78 `CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量控制器（Volume Control Profile Volume Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE"></a>

## 360.79 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_VCP_VOL_REND && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INHERIT
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_OFF
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_ERR
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_WRN
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INF
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DBG
CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_VCP_VOL_REND`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VCP_VOL_REND)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INHERIT)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_OFF)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_ERR)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_WRN)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INF)、[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DBG"></a>

## 360.80 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT"></a>

## 360.81 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_ERR"></a>

## 360.82 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INF"></a>

## 360.83 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INHERIT"></a>

## 360.84 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_OFF"></a>

## 360.85 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_WRN"></a>

## 360.86 `CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量控制配置文件的音量渲染器（Volume Control Profile Volume Renderer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VCP_VOL_REND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 360.87 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_VOCS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_VOCS_CLIENT`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VOCS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DBG"></a>

## 360.88 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 360.89 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_ERR"></a>

## 360.90 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INF"></a>

## 360.91 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 360.92 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_OFF"></a>

## 360.93 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_WRN"></a>

## 360.94 `CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务客户端（Volume Offset Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_CHOICE"></a>

## 360.95 `CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_VOCS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_VOCS_LOG_LEVEL_INHERIT
CONFIG_BT_VOCS_LOG_LEVEL_OFF
CONFIG_BT_VOCS_LOG_LEVEL_ERR
CONFIG_BT_VOCS_LOG_LEVEL_WRN
CONFIG_BT_VOCS_LOG_LEVEL_INF
CONFIG_BT_VOCS_LOG_LEVEL_DBG
CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_VOCS`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_VOCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_VOCS_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_VOCS_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_BT_VOCS_LOG_LEVEL_OFF)、[`CONFIG_BT_VOCS_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_ERR)、[`CONFIG_BT_VOCS_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_BT_VOCS_LOG_LEVEL_WRN)、[`CONFIG_BT_VOCS_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_INF)、[`CONFIG_BT_VOCS_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_DBG"></a>

## 360.96 `CONFIG_BT_VOCS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT"></a>

## 360.97 `CONFIG_BT_VOCS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_ERR"></a>

## 360.98 `CONFIG_BT_VOCS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_INF"></a>

## 360.99 `CONFIG_BT_VOCS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_INHERIT"></a>

## 360.100 `CONFIG_BT_VOCS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_VOCS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P359_subsys_logging_配置项参考_8.md) · [返回大纲](大纲.md) · [下一章](P361_subsys_logging_配置项参考_10.md)
