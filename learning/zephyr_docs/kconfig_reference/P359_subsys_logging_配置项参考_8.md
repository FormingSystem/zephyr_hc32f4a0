---
id: learning.zephyr-docs.kconfig-reference.page-359
title: "`subsys/logging`配置项参考（8/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第359章\_`subsys/logging`配置项参考（8/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_ERR"></a>

## 359.1 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_INF"></a>

## 359.2 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_INHERIT"></a>

## 359.3 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_PROXY_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_OFF"></a>

## 359.4 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_WRN"></a>

## 359.5 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE"></a>

## 359.6 `CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_RPL_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_RPL_LOG_LEVEL_OFF
CONFIG_BT_MESH_RPL_LOG_LEVEL_ERR
CONFIG_BT_MESH_RPL_LOG_LEVEL_WRN
CONFIG_BT_MESH_RPL_LOG_LEVEL_INF
CONFIG_BT_MESH_RPL_LOG_LEVEL_DBG
CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_RPL_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_DBG"></a>

## 359.7 `CONFIG_BT_MESH_RPL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT"></a>

## 359.8 `CONFIG_BT_MESH_RPL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_ERR"></a>

## 359.9 `CONFIG_BT_MESH_RPL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_INF"></a>

## 359.10 `CONFIG_BT_MESH_RPL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_INHERIT"></a>

## 359.11 `CONFIG_BT_MESH_RPL_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_RPL_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_OFF"></a>

## 359.12 `CONFIG_BT_MESH_RPL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_RPL_LOG_LEVEL_WRN"></a>

## 359.13 `CONFIG_BT_MESH_RPL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 重放保护列表（Replay protection list）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_RPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE"></a>

## 359.14 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_OFF
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_ERR
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_WRN
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INF
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DBG
CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DBG"></a>

## 359.15 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT"></a>

## 359.16 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_ERR"></a>

## 359.17 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INF"></a>

## 359.18 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INHERIT"></a>

## 359.19 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_OFF"></a>

## 359.20 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_WRN"></a>

## 359.21 `CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 持久化设置（Persistent settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE"></a>

## 359.22 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_TRANS_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_TRANS_LOG_LEVEL_OFF
CONFIG_BT_MESH_TRANS_LOG_LEVEL_ERR
CONFIG_BT_MESH_TRANS_LOG_LEVEL_WRN
CONFIG_BT_MESH_TRANS_LOG_LEVEL_INF
CONFIG_BT_MESH_TRANS_LOG_LEVEL_DBG
CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_DBG"></a>

## 359.23 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT"></a>

## 359.24 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_ERR"></a>

## 359.25 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_INF"></a>

## 359.26 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_INHERIT"></a>

## 359.27 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_TRANS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_OFF"></a>

## 359.28 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_TRANS_LOG_LEVEL_WRN"></a>

## 359.29 `CONFIG_BT_MESH_TRANS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 传输层（Transport layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_TRANS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE"></a>

## 359.30 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MICP_MIC_CTLR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INHERIT
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_OFF
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_ERR
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_WRN
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INF
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DBG
CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MICP_MIC_CTLR`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_CTLR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_OFF)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_ERR)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_WRN)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INF)、[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DBG"></a>

## 359.31 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT"></a>

## 359.32 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_ERR"></a>

## 359.33 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INF"></a>

## 359.34 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INHERIT"></a>

## 359.35 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_OFF"></a>

## 359.36 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_WRN"></a>

## 359.37 `CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风控制器（Microphone Control Profile Microphone Controller）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_CTLR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE"></a>

## 359.38 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`

**提示（Prompt）**：麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MICP_MIC_DEV && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INHERIT
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_OFF
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_ERR
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_WRN
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INF
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DBG
CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MICP_MIC_DEV`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MICP_MIC_DEV)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_OFF)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_ERR)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_WRN)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INF)、[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DBG"></a>

## 359.39 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT"></a>

## 359.40 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_ERR"></a>

## 359.41 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INF"></a>

## 359.42 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INHERIT"></a>

## 359.43 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_OFF"></a>

## 359.44 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_WRN"></a>

## 359.45 `CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 麦克风控制配置文件的麦克风设备（Microphone Control Profile Microphone Device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MICP_MIC_DEV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_CHOICE"></a>

## 359.46 `CONFIG_BT_MPL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MPL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MPL_LOG_LEVEL_INHERIT
CONFIG_BT_MPL_LOG_LEVEL_OFF
CONFIG_BT_MPL_LOG_LEVEL_ERR
CONFIG_BT_MPL_LOG_LEVEL_WRN
CONFIG_BT_MPL_LOG_LEVEL_INF
CONFIG_BT_MPL_LOG_LEVEL_DBG
CONFIG_BT_MPL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MPL_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MPL_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MPL_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_OFF)、[`CONFIG_BT_MPL_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_ERR)、[`CONFIG_BT_MPL_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_WRN)、[`CONFIG_BT_MPL_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_INF)、[`CONFIG_BT_MPL_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MPL_LOG_LEVEL_DBG"></a>

## 359.47 `CONFIG_BT_MPL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_DEFAULT"></a>

## 359.48 `CONFIG_BT_MPL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_ERR"></a>

## 359.49 `CONFIG_BT_MPL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_INF"></a>

## 359.50 `CONFIG_BT_MPL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_INHERIT"></a>

## 359.51 `CONFIG_BT_MPL_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_MPL_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_OFF"></a>

## 359.52 `CONFIG_BT_MPL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MPL_LOG_LEVEL_WRN"></a>

## 359.53 `CONFIG_BT_MPL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MPL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体播放器（Media player）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MPL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 359.54 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_OTS_CLIENT && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_OTS_CLIENT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DBG"></a>

## 359.55 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 359.56 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_ERR"></a>

## 359.57 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INF"></a>

## 359.58 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 359.59 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 选择项（Choice）：`BT_OTS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_OFF"></a>

## 359.60 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_CLIENT_LOG_LEVEL_WRN"></a>

## 359.61 `CONFIG_BT_OTS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 对象传输服务客户端（Object Transfer Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_CHOICE"></a>

## 359.62 `CONFIG_BT_OTS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_OTS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_OTS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_OTS_LOG_LEVEL_OFF
CONFIG_BT_OTS_LOG_LEVEL_ERR
CONFIG_BT_OTS_LOG_LEVEL_WRN
CONFIG_BT_OTS_LOG_LEVEL_INF
CONFIG_BT_OTS_LOG_LEVEL_DBG
CONFIG_BT_OTS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OTS_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_OTS_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_OFF)、[`CONFIG_BT_OTS_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_ERR)、[`CONFIG_BT_OTS_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_WRN)、[`CONFIG_BT_OTS_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_INF)、[`CONFIG_BT_OTS_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_OTS_LOG_LEVEL_DBG"></a>

## 359.63 `CONFIG_BT_OTS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_DEFAULT"></a>

## 359.64 `CONFIG_BT_OTS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_ERR"></a>

## 359.65 `CONFIG_BT_OTS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_INF"></a>

## 359.66 `CONFIG_BT_OTS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_OFF"></a>

## 359.67 `CONFIG_BT_OTS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_OTS_LOG_LEVEL_WRN"></a>

## 359.68 `CONFIG_BT_OTS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_OTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 蓝牙对象传输服务（BT_OTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_OTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_CHOICE"></a>

## 359.69 `CONFIG_BT_PACS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_PACS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_PACS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_PACS_LOG_LEVEL_INHERIT
CONFIG_BT_PACS_LOG_LEVEL_OFF
CONFIG_BT_PACS_LOG_LEVEL_ERR
CONFIG_BT_PACS_LOG_LEVEL_WRN
CONFIG_BT_PACS_LOG_LEVEL_INF
CONFIG_BT_PACS_LOG_LEVEL_DBG
CONFIG_BT_PACS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_PACS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PACS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PACS_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_PACS_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_PACS_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_OFF)、[`CONFIG_BT_PACS_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_ERR)、[`CONFIG_BT_PACS_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_WRN)、[`CONFIG_BT_PACS_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_INF)、[`CONFIG_BT_PACS_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_PACS`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_PACS_LOG_LEVEL_DBG"></a>

## 359.70 `CONFIG_BT_PACS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_DEFAULT"></a>

## 359.71 `CONFIG_BT_PACS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_ERR"></a>

## 359.72 `CONFIG_BT_PACS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_INF"></a>

## 359.73 `CONFIG_BT_PACS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_INHERIT"></a>

## 359.74 `CONFIG_BT_PACS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_PACS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_OFF"></a>

## 359.75 `CONFIG_BT_PACS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PACS_LOG_LEVEL_WRN"></a>

## 359.76 `CONFIG_BT_PACS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PACS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 已发布音频能力服务（Published Audio Capabilities Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PACS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_CHOICE"></a>

## 359.77 `CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_PBAP_LOG_LEVEL_INHERIT
CONFIG_BT_PBAP_LOG_LEVEL_OFF
CONFIG_BT_PBAP_LOG_LEVEL_ERR
CONFIG_BT_PBAP_LOG_LEVEL_WRN
CONFIG_BT_PBAP_LOG_LEVEL_INF
CONFIG_BT_PBAP_LOG_LEVEL_DBG
CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_PBAP_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_PBAP_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_OFF)、[`CONFIG_BT_PBAP_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_ERR)、[`CONFIG_BT_PBAP_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_WRN)、[`CONFIG_BT_PBAP_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_INF)、[`CONFIG_BT_PBAP_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_DBG"></a>

## 359.78 `CONFIG_BT_PBAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT"></a>

## 359.79 `CONFIG_BT_PBAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_ERR"></a>

## 359.80 `CONFIG_BT_PBAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_INF"></a>

## 359.81 `CONFIG_BT_PBAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_INHERIT"></a>

## 359.82 `CONFIG_BT_PBAP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_PBAP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_OFF"></a>

## 359.83 `CONFIG_BT_PBAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBAP_LOG_LEVEL_WRN"></a>

## 359.84 `CONFIG_BT_PBAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙电话簿访问配置文件（Bluetooth Phone Book Access Profile (PBAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_CHOICE"></a>

## 359.85 `CONFIG_BT_PBP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_PBP && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_PBP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_PBP_LOG_LEVEL_OFF
CONFIG_BT_PBP_LOG_LEVEL_ERR
CONFIG_BT_PBP_LOG_LEVEL_WRN
CONFIG_BT_PBP_LOG_LEVEL_INF
CONFIG_BT_PBP_LOG_LEVEL_DBG
CONFIG_BT_PBP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_PBP`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PBP_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_PBP_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_OFF)、[`CONFIG_BT_PBP_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_ERR)、[`CONFIG_BT_PBP_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_WRN)、[`CONFIG_BT_PBP_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_INF)、[`CONFIG_BT_PBP_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_PBP_LOG_LEVEL_DBG"></a>

## 359.86 `CONFIG_BT_PBP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_DEFAULT"></a>

## 359.87 `CONFIG_BT_PBP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_ERR"></a>

## 359.88 `CONFIG_BT_PBP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_INF"></a>

## 359.89 `CONFIG_BT_PBP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_OFF"></a>

## 359.90 `CONFIG_BT_PBP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_PBP_LOG_LEVEL_WRN"></a>

## 359.91 `CONFIG_BT_PBP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_PBP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 公共广播配置文件（Public Broadcast Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_PBP_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_PBP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE"></a>

## 359.92 `CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_RFCOMM_LOG_LEVEL_INHERIT
CONFIG_BT_RFCOMM_LOG_LEVEL_OFF
CONFIG_BT_RFCOMM_LOG_LEVEL_ERR
CONFIG_BT_RFCOMM_LOG_LEVEL_WRN
CONFIG_BT_RFCOMM_LOG_LEVEL_INF
CONFIG_BT_RFCOMM_LOG_LEVEL_DBG
CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_INHERIT)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_OFF)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_ERR)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_WRN)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_INF)、[`CONFIG_BT_RFCOMM_LOG_LEVEL_DBG`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_DBG"></a>

## 359.93 `CONFIG_BT_RFCOMM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT"></a>

## 359.94 `CONFIG_BT_RFCOMM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_ERR"></a>

## 359.95 `CONFIG_BT_RFCOMM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_INF"></a>

## 359.96 `CONFIG_BT_RFCOMM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_INHERIT"></a>

## 359.97 `CONFIG_BT_RFCOMM_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_RFCOMM_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_OFF"></a>

## 359.98 `CONFIG_BT_RFCOMM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RFCOMM_LOG_LEVEL_WRN"></a>

## 359.99 `CONFIG_BT_RFCOMM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙 RFCOMM 串口仿真协议（Bluetooth RFCOMM）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_RFCOMM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_RPA_LOG_LEVEL_CHOICE"></a>

## 359.100 `CONFIG_BT_RPA_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙可解析私有地址（Bluetooth Resolvable Private Address (RPA)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_RPA_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_RPA_LOG_LEVEL_INHERIT
CONFIG_BT_RPA_LOG_LEVEL_OFF
CONFIG_BT_RPA_LOG_LEVEL_ERR
CONFIG_BT_RPA_LOG_LEVEL_WRN
CONFIG_BT_RPA_LOG_LEVEL_INF
CONFIG_BT_RPA_LOG_LEVEL_DBG
CONFIG_BT_RPA_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_RPA_LOG_LEVEL_DEFAULT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_RPA_LOG_LEVEL_INHERIT`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_INHERIT)、[`CONFIG_BT_RPA_LOG_LEVEL_OFF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_OFF)、[`CONFIG_BT_RPA_LOG_LEVEL_ERR`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_ERR)、[`CONFIG_BT_RPA_LOG_LEVEL_WRN`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_WRN)、[`CONFIG_BT_RPA_LOG_LEVEL_INF`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_INF)、[`CONFIG_BT_RPA_LOG_LEVEL_DBG`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_RPA_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<!-- kconfig-navigation -->

[上一章](P358_subsys_logging_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P360_subsys_logging_配置项参考_9.md)
