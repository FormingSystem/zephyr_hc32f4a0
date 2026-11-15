---
id: learning.zephyr-docs.kconfig-reference.page-376
title: "`subsys/logging`配置项参考（25/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第376章\_`subsys/logging`配置项参考（25/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SENSOR_LOG_LEVEL_OFF"></a>

## 376.1 `CONFIG_SENSOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSOR_LOG_LEVEL_WRN"></a>

## 376.2 `CONFIG_SENSOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_CHOICE"></a>

## 376.3 `CONFIG_SENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SENT
```

**默认值（Defaults）**

```text
CONFIG_SENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SENT_LOG_LEVEL_OFF
CONFIG_SENT_LOG_LEVEL_ERR
CONFIG_SENT_LOG_LEVEL_WRN
CONFIG_SENT_LOG_LEVEL_INF
CONFIG_SENT_LOG_LEVEL_DBG
CONFIG_SENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SENT`](P164_drivers_sent_配置项参考.md#CONFIG_SENT)、[`CONFIG_SENT_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_DEFAULT)、[`CONFIG_SENT_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_OFF)、[`CONFIG_SENT_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_ERR)、[`CONFIG_SENT_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_WRN)、[`CONFIG_SENT_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_INF)、[`CONFIG_SENT_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_DBG)。

<a id="CONFIG_SENT_LOG_LEVEL_DBG"></a>

## 376.4 `CONFIG_SENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_DEFAULT"></a>

## 376.5 `CONFIG_SENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_ERR"></a>

## 376.6 `CONFIG_SENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_INF"></a>

## 376.7 `CONFIG_SENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_OFF"></a>

## 376.8 `CONFIG_SENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENT_LOG_LEVEL_WRN"></a>

## 376.9 `CONFIG_SENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单边沿半字节传输（Single Edge Nibble Transmission，SENT）驱动 → 单边沿半字节传输（sent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_CHOICE"></a>

## 376.10 `CONFIG_SETTINGS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
CONFIG_SETTINGS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SETTINGS_LOG_LEVEL_OFF
CONFIG_SETTINGS_LOG_LEVEL_ERR
CONFIG_SETTINGS_LOG_LEVEL_WRN
CONFIG_SETTINGS_LOG_LEVEL_INF
CONFIG_SETTINGS_LOG_LEVEL_DBG
CONFIG_SETTINGS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_DEFAULT)、[`CONFIG_SETTINGS_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_OFF)、[`CONFIG_SETTINGS_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_ERR)、[`CONFIG_SETTINGS_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_WRN)、[`CONFIG_SETTINGS_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_INF)、[`CONFIG_SETTINGS_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_DBG)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_DBG"></a>

## 376.11 `CONFIG_SETTINGS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_DEFAULT"></a>

## 376.12 `CONFIG_SETTINGS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_ERR"></a>

## 376.13 `CONFIG_SETTINGS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_INF"></a>

## 376.14 `CONFIG_SETTINGS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_OFF"></a>

## 376.15 `CONFIG_SETTINGS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SETTINGS_LOG_LEVEL_WRN"></a>

## 376.16 `CONFIG_SETTINGS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 设置子系统（settings）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SETTINGS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_CHOICE"></a>

## 376.17 `CONFIG_SHELL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_LOG_LEVEL_OFF
CONFIG_SHELL_LOG_LEVEL_ERR
CONFIG_SHELL_LOG_LEVEL_WRN
CONFIG_SHELL_LOG_LEVEL_INF
CONFIG_SHELL_LOG_LEVEL_DBG
CONFIG_SHELL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_OFF)、[`CONFIG_SHELL_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_ERR)、[`CONFIG_SHELL_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_WRN)、[`CONFIG_SHELL_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_INF)、[`CONFIG_SHELL_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_LOG_LEVEL_DBG"></a>

## 376.18 `CONFIG_SHELL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_DEFAULT"></a>

## 376.19 `CONFIG_SHELL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_ERR"></a>

## 376.20 `CONFIG_SHELL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_INF"></a>

## 376.21 `CONFIG_SHELL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_OFF"></a>

## 376.22 `CONFIG_SHELL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_LOG_LEVEL_WRN"></a>

## 376.23 `CONFIG_SHELL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行（Shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE"></a>

## 376.24 `CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_MQTT_LOG_LEVEL_OFF
CONFIG_SHELL_MQTT_LOG_LEVEL_ERR
CONFIG_SHELL_MQTT_LOG_LEVEL_WRN
CONFIG_SHELL_MQTT_LOG_LEVEL_INF
CONFIG_SHELL_MQTT_LOG_LEVEL_DBG
CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_OFF)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_ERR)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_WRN)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_INF)、[`CONFIG_SHELL_MQTT_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_DBG"></a>

## 376.25 `CONFIG_SHELL_MQTT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT"></a>

## 376.26 `CONFIG_SHELL_MQTT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_ERR"></a>

## 376.27 `CONFIG_SHELL_MQTT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_INF"></a>

## 376.28 `CONFIG_SHELL_MQTT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_OFF"></a>

## 376.29 `CONFIG_SHELL_MQTT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_MQTT_LOG_LEVEL_WRN"></a>

## 376.30 `CONFIG_SHELL_MQTT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → MQTT 命令行后端（MQTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE"></a>

## 376.31 `CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_RPMSG_LOG_LEVEL_OFF
CONFIG_SHELL_RPMSG_LOG_LEVEL_ERR
CONFIG_SHELL_RPMSG_LOG_LEVEL_WRN
CONFIG_SHELL_RPMSG_LOG_LEVEL_INF
CONFIG_SHELL_RPMSG_LOG_LEVEL_DBG
CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_RPMSG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_OFF)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_ERR)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_WRN)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_INF)、[`CONFIG_SHELL_RPMSG_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_DBG"></a>

## 376.32 `CONFIG_SHELL_RPMSG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT"></a>

## 376.33 `CONFIG_SHELL_RPMSG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_ERR"></a>

## 376.34 `CONFIG_SHELL_RPMSG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_INF"></a>

## 376.35 `CONFIG_SHELL_RPMSG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_OFF"></a>

## 376.36 `CONFIG_SHELL_RPMSG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RPMSG_LOG_LEVEL_WRN"></a>

## 376.37 `CONFIG_SHELL_RPMSG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → RPMsg 命令行后端（RPMsg shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RPMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE"></a>

## 376.38 `CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_RTT_LOG_LEVEL_OFF
CONFIG_SHELL_RTT_LOG_LEVEL_ERR
CONFIG_SHELL_RTT_LOG_LEVEL_WRN
CONFIG_SHELL_RTT_LOG_LEVEL_INF
CONFIG_SHELL_RTT_LOG_LEVEL_DBG
CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_RTT_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_OFF)、[`CONFIG_SHELL_RTT_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_ERR)、[`CONFIG_SHELL_RTT_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_WRN)、[`CONFIG_SHELL_RTT_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_INF)、[`CONFIG_SHELL_RTT_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_DBG"></a>

## 376.39 `CONFIG_SHELL_RTT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT"></a>

## 376.40 `CONFIG_SHELL_RTT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_ERR"></a>

## 376.41 `CONFIG_SHELL_RTT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_INF"></a>

## 376.42 `CONFIG_SHELL_RTT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_OFF"></a>

## 376.43 `CONFIG_SHELL_RTT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_RTT_LOG_LEVEL_WRN"></a>

## 376.44 `CONFIG_SHELL_RTT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → RTT 命令行后端（RTT shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_RTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE"></a>

## 376.45 `CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_SSH && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_SSH_LOG_LEVEL_OFF
CONFIG_SHELL_SSH_LOG_LEVEL_ERR
CONFIG_SHELL_SSH_LOG_LEVEL_WRN
CONFIG_SHELL_SSH_LOG_LEVEL_INF
CONFIG_SHELL_SSH_LOG_LEVEL_DBG
CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SSH)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_SSH_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_OFF)、[`CONFIG_SHELL_SSH_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_ERR)、[`CONFIG_SHELL_SSH_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_WRN)、[`CONFIG_SHELL_SSH_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_INF)、[`CONFIG_SHELL_SSH_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_DBG"></a>

## 376.46 `CONFIG_SHELL_SSH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT"></a>

## 376.47 `CONFIG_SHELL_SSH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_ERR"></a>

## 376.48 `CONFIG_SHELL_SSH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_INF"></a>

## 376.49 `CONFIG_SHELL_SSH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_OFF"></a>

## 376.50 `CONFIG_SHELL_SSH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_SSH_LOG_LEVEL_WRN"></a>

## 376.51 `CONFIG_SHELL_SSH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。 → SSH 命令行后端（SSH shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE"></a>

## 376.52 `CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_TELNET_LOG_LEVEL_OFF
CONFIG_SHELL_TELNET_LOG_LEVEL_ERR
CONFIG_SHELL_TELNET_LOG_LEVEL_WRN
CONFIG_SHELL_TELNET_LOG_LEVEL_INF
CONFIG_SHELL_TELNET_LOG_LEVEL_DBG
CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_TELNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_OFF)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_ERR)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_WRN)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_INF)、[`CONFIG_SHELL_TELNET_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_DBG"></a>

## 376.53 `CONFIG_SHELL_TELNET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT"></a>

## 376.54 `CONFIG_SHELL_TELNET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_ERR"></a>

## 376.55 `CONFIG_SHELL_TELNET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_INF"></a>

## 376.56 `CONFIG_SHELL_TELNET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_OFF"></a>

## 376.57 `CONFIG_SHELL_TELNET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_TELNET_LOG_LEVEL_WRN"></a>

## 376.58 `CONFIG_SHELL_TELNET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → TELNET 命令行后端（TELNET shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_TELNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE"></a>

## 376.59 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_OFF
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_ERR
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_WRN
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_INF
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DBG
CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_OFF)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_ERR)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_WRN)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_INF)、[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DBG)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DBG"></a>

## 376.60 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT"></a>

## 376.61 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_ERR"></a>

## 376.62 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_INF"></a>

## 376.63 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_OFF"></a>

## 376.64 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_WRN"></a>

## 376.65 `CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → WebSocket 命令行后端（Websocket shell backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SHELL_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_CHOICE"></a>

## 376.66 `CONFIG_SMBUS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
CONFIG_SMBUS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SMBUS_LOG_LEVEL_OFF
CONFIG_SMBUS_LOG_LEVEL_ERR
CONFIG_SMBUS_LOG_LEVEL_WRN
CONFIG_SMBUS_LOG_LEVEL_INF
CONFIG_SMBUS_LOG_LEVEL_DBG
CONFIG_SMBUS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_SMBUS_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_DEFAULT)、[`CONFIG_SMBUS_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_OFF)、[`CONFIG_SMBUS_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_ERR)、[`CONFIG_SMBUS_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_WRN)、[`CONFIG_SMBUS_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_INF)、[`CONFIG_SMBUS_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_DBG)。

<a id="CONFIG_SMBUS_LOG_LEVEL_DBG"></a>

## 376.67 `CONFIG_SMBUS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_DEFAULT"></a>

## 376.68 `CONFIG_SMBUS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_ERR"></a>

## 376.69 `CONFIG_SMBUS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_INF"></a>

## 376.70 `CONFIG_SMBUS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_OFF"></a>

## 376.71 `CONFIG_SMBUS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SMBUS_LOG_LEVEL_WRN"></a>

## 376.72 `CONFIG_SMBUS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → 系统管理总线（smbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SMBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_CHOICE"></a>

## 376.73 `CONFIG_SOC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_SOC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SOC_LOG_LEVEL_OFF
CONFIG_SOC_LOG_LEVEL_ERR
CONFIG_SOC_LOG_LEVEL_WRN
CONFIG_SOC_LOG_LEVEL_INF
CONFIG_SOC_LOG_LEVEL_DBG
CONFIG_SOC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SOC_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_DEFAULT)、[`CONFIG_SOC_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_OFF)、[`CONFIG_SOC_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_ERR)、[`CONFIG_SOC_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_WRN)、[`CONFIG_SOC_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_INF)、[`CONFIG_SOC_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_DBG)。

<a id="CONFIG_SOC_LOG_LEVEL_DBG"></a>

## 376.74 `CONFIG_SOC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_DEFAULT"></a>

## 376.75 `CONFIG_SOC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_ERR"></a>

## 376.76 `CONFIG_SOC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_INF"></a>

## 376.77 `CONFIG_SOC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_OFF"></a>

## 376.78 `CONFIG_SOC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOC_LOG_LEVEL_WRN"></a>

## 376.79 `CONFIG_SOC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统（SOC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SOC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_CHOICE"></a>

## 376.80 `CONFIG_SPI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SPI
```

**默认值（Defaults）**

```text
CONFIG_SPI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SPI_LOG_LEVEL_OFF
CONFIG_SPI_LOG_LEVEL_ERR
CONFIG_SPI_LOG_LEVEL_WRN
CONFIG_SPI_LOG_LEVEL_INF
CONFIG_SPI_LOG_LEVEL_DBG
CONFIG_SPI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_DEFAULT)、[`CONFIG_SPI_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_OFF)、[`CONFIG_SPI_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_ERR)、[`CONFIG_SPI_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_WRN)、[`CONFIG_SPI_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_INF)、[`CONFIG_SPI_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_DBG)。

<a id="CONFIG_SPI_LOG_LEVEL_DBG"></a>

## 376.81 `CONFIG_SPI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_DEFAULT"></a>

## 376.82 `CONFIG_SPI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_ERR"></a>

## 376.83 `CONFIG_SPI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_INF"></a>

## 376.84 `CONFIG_SPI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_OFF"></a>

## 376.85 `CONFIG_SPI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SPI_LOG_LEVEL_WRN"></a>

## 376.86 `CONFIG_SPI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 串行外设接口（spi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SPI_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_CHOICE"></a>

## 376.87 `CONFIG_STEPPER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
CONFIG_STEPPER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_STEPPER_LOG_LEVEL_OFF
CONFIG_STEPPER_LOG_LEVEL_ERR
CONFIG_STEPPER_LOG_LEVEL_WRN
CONFIG_STEPPER_LOG_LEVEL_INF
CONFIG_STEPPER_LOG_LEVEL_DBG
CONFIG_STEPPER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_DEFAULT)、[`CONFIG_STEPPER_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_OFF)、[`CONFIG_STEPPER_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_ERR)、[`CONFIG_STEPPER_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_WRN)、[`CONFIG_STEPPER_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_INF)、[`CONFIG_STEPPER_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_DBG)。

<a id="CONFIG_STEPPER_LOG_LEVEL_DBG"></a>

## 376.88 `CONFIG_STEPPER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_DEFAULT"></a>

## 376.89 `CONFIG_STEPPER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_ERR"></a>

## 376.90 `CONFIG_STEPPER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_INF"></a>

## 376.91 `CONFIG_STEPPER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_OFF"></a>

## 376.92 `CONFIG_STEPPER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STEPPER_LOG_LEVEL_WRN"></a>

## 376.93 `CONFIG_STEPPER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STEPPER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 步进电机（stepper）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STEPPER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE"></a>

## 376.94 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`

**提示（Prompt）**：STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_STM32_NEOCHROM_GPU2D && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_OFF
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_ERR
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_WRN
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_INF
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DBG
CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_STM32_NEOCHROM_GPU2D`](P311_soc_st_配置项参考.md#CONFIG_STM32_NEOCHROM_GPU2D)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_OFF)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_ERR`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_ERR)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_WRN)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_INF`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_INF)、[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DBG`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DBG"></a>

## 376.95 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT"></a>

## 376.96 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_ERR"></a>

## 376.97 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_INF"></a>

## 376.98 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_OFF"></a>

## 376.99 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_WRN"></a>

## 376.100 `CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support） → STM32 NeoChrom 二维图形加速器（stm32_neochrom_gpu2d）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE`](P376_subsys_logging_配置项参考_25.md#CONFIG_STM32_NEOCHROM_GPU2D_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P375_subsys_logging_配置项参考_24.md) · [返回大纲](大纲.md) · [下一章](P377_subsys_logging_配置项参考_26.md)
