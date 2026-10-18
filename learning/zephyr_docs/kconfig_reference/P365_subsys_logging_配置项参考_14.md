---
id: learning.zephyr-docs.kconfig-reference.page-365
title: "`subsys/logging`配置项参考（14/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第365章\_`subsys/logging`配置项参考（14/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_WRN"></a>

## 365.1 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE"></a>

## 365.2 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HL78XX_AT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_OFF
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_ERR
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_WRN
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_INF
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DBG
CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HL78XX_AT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_AT_MONITOR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_OFF)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_ERR)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_WRN)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_INF)、[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DBG)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DBG"></a>

## 365.3 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT"></a>

## 365.4 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_ERR"></a>

## 365.5 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_INF"></a>

## 365.6 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_OFF"></a>

## 365.7 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_WRN"></a>

## 365.8 `CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX 已解析 AT 监视器（Parsed AT Monitor） → 已解析 AT 命令监控库（Parsed AT monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_AT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE"></a>

## 365.9 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HL78XX_EVT_MONITOR && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_OFF
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_ERR
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_WRN
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_INF
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DBG
CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HL78XX_EVT_MONITOR`](P125_drivers_modem_配置项参考_1.md#CONFIG_HL78XX_EVT_MONITOR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_OFF)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_ERR)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_WRN)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_INF)、[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DBG)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DBG"></a>

## 365.10 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT"></a>

## 365.11 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_ERR"></a>

## 365.12 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_INF"></a>

## 365.13 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_OFF"></a>

## 365.14 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_WRN"></a>

## 365.15 `CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → HL78XX AT 通知监视器（AT Notification Monitor） → 事件通知监控库（Event notification monitor library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HL78XX_EVT_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_CHOICE"></a>

## 365.16 `CONFIG_HWINFO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HWINFO
```

**默认值（Defaults）**

```text
CONFIG_HWINFO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HWINFO_LOG_LEVEL_OFF
CONFIG_HWINFO_LOG_LEVEL_ERR
CONFIG_HWINFO_LOG_LEVEL_WRN
CONFIG_HWINFO_LOG_LEVEL_INF
CONFIG_HWINFO_LOG_LEVEL_DBG
CONFIG_HWINFO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HWINFO_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_DEFAULT)、[`CONFIG_HWINFO_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_OFF)、[`CONFIG_HWINFO_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_ERR)、[`CONFIG_HWINFO_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_WRN)、[`CONFIG_HWINFO_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_INF)、[`CONFIG_HWINFO_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_DBG)。

<a id="CONFIG_HWINFO_LOG_LEVEL_DBG"></a>

## 365.17 `CONFIG_HWINFO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_DEFAULT"></a>

## 365.18 `CONFIG_HWINFO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_ERR"></a>

## 365.19 `CONFIG_HWINFO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_INF"></a>

## 365.20 `CONFIG_HWINFO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_OFF"></a>

## 365.21 `CONFIG_HWINFO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWINFO_LOG_LEVEL_WRN"></a>

## 365.22 `CONFIG_HWINFO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWINFO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件信息驱动（Hardware Information Drivers） → 硬件信息（HWINFO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWINFO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE"></a>

## 365.23 `CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HWSPINLOCK
```

**默认值（Defaults）**

```text
CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HWSPINLOCK_LOG_LEVEL_OFF
CONFIG_HWSPINLOCK_LOG_LEVEL_ERR
CONFIG_HWSPINLOCK_LOG_LEVEL_WRN
CONFIG_HWSPINLOCK_LOG_LEVEL_INF
CONFIG_HWSPINLOCK_LOG_LEVEL_DBG
CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HWSPINLOCK`](P104_drivers_hwspinlock_配置项参考.md#CONFIG_HWSPINLOCK)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_OFF)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_ERR)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_WRN)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_INF)、[`CONFIG_HWSPINLOCK_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_DBG)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_DBG"></a>

## 365.24 `CONFIG_HWSPINLOCK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT"></a>

## 365.25 `CONFIG_HWSPINLOCK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_ERR"></a>

## 365.26 `CONFIG_HWSPINLOCK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_INF"></a>

## 365.27 `CONFIG_HWSPINLOCK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_OFF"></a>

## 365.28 `CONFIG_HWSPINLOCK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HWSPINLOCK_LOG_LEVEL_WRN"></a>

## 365.29 `CONFIG_HWSPINLOCK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 硬件自旋锁驱动（Hardware Spinlock Drivers） → 硬件自旋锁（hwspinlock）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_HWSPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_CHOICE"></a>

## 365.30 `CONFIG_I2C_LOG_LEVEL_CHOICE`

**提示（Prompt）**：I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I2C
```

**默认值（Defaults）**

```text
CONFIG_I2C_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I2C_LOG_LEVEL_OFF
CONFIG_I2C_LOG_LEVEL_ERR
CONFIG_I2C_LOG_LEVEL_WRN
CONFIG_I2C_LOG_LEVEL_INF
CONFIG_I2C_LOG_LEVEL_DBG
CONFIG_I2C_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_DEFAULT)、[`CONFIG_I2C_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_OFF)、[`CONFIG_I2C_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_ERR)、[`CONFIG_I2C_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_WRN)、[`CONFIG_I2C_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_INF)、[`CONFIG_I2C_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_DBG)。

<a id="CONFIG_I2C_LOG_LEVEL_DBG"></a>

## 365.31 `CONFIG_I2C_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_DEFAULT"></a>

## 365.32 `CONFIG_I2C_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_ERR"></a>

## 365.33 `CONFIG_I2C_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_INF"></a>

## 365.34 `CONFIG_I2C_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_OFF"></a>

## 365.35 `CONFIG_I2C_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2C_LOG_LEVEL_WRN"></a>

## 365.36 `CONFIG_I2C_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I2C 总线（i2c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_CHOICE"></a>

## 365.37 `CONFIG_I2S_LOG_LEVEL_CHOICE`

**提示（Prompt）**：I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I2S
```

**默认值（Defaults）**

```text
CONFIG_I2S_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I2S_LOG_LEVEL_OFF
CONFIG_I2S_LOG_LEVEL_ERR
CONFIG_I2S_LOG_LEVEL_WRN
CONFIG_I2S_LOG_LEVEL_INF
CONFIG_I2S_LOG_LEVEL_DBG
CONFIG_I2S_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)、[`CONFIG_I2S_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_DEFAULT)、[`CONFIG_I2S_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_OFF)、[`CONFIG_I2S_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_ERR)、[`CONFIG_I2S_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_WRN)、[`CONFIG_I2S_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_INF)、[`CONFIG_I2S_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_DBG)。

<a id="CONFIG_I2S_LOG_LEVEL_DBG"></a>

## 365.38 `CONFIG_I2S_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_DEFAULT"></a>

## 365.39 `CONFIG_I2S_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_ERR"></a>

## 365.40 `CONFIG_I2S_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_INF"></a>

## 365.41 `CONFIG_I2S_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_OFF"></a>

## 365.42 `CONFIG_I2S_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I2S_LOG_LEVEL_WRN"></a>

## 365.43 `CONFIG_I2S_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I2S_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路间音频（Inter-IC Sound，I²S）总线驱动 → I2S 数字音频总线（i2s）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I2S_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I2S_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE"></a>

## 365.44 `CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_CADENCE_LOG_LEVEL_OFF
CONFIG_I3C_CADENCE_LOG_LEVEL_ERR
CONFIG_I3C_CADENCE_LOG_LEVEL_WRN
CONFIG_I3C_CADENCE_LOG_LEVEL_INF
CONFIG_I3C_CADENCE_LOG_LEVEL_DBG
CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_OFF)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_ERR)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_WRN)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_INF)、[`CONFIG_I3C_CADENCE_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_DBG"></a>

## 365.45 `CONFIG_I3C_CADENCE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT"></a>

## 365.46 `CONFIG_I3C_CADENCE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_ERR"></a>

## 365.47 `CONFIG_I3C_CADENCE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_INF"></a>

## 365.48 `CONFIG_I3C_CADENCE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_OFF"></a>

## 365.49 `CONFIG_I3C_CADENCE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_CADENCE_LOG_LEVEL_WRN"></a>

## 365.50 `CONFIG_I3C_CADENCE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I3C（i3c-cadence）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_CADENCE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_CHOICE"></a>

## 365.51 `CONFIG_I3C_DW_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_DW_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_DW_LOG_LEVEL_OFF
CONFIG_I3C_DW_LOG_LEVEL_ERR
CONFIG_I3C_DW_LOG_LEVEL_WRN
CONFIG_I3C_DW_LOG_LEVEL_INF
CONFIG_I3C_DW_LOG_LEVEL_DBG
CONFIG_I3C_DW_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_DW_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_DW_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_OFF)、[`CONFIG_I3C_DW_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_ERR)、[`CONFIG_I3C_DW_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_WRN)、[`CONFIG_I3C_DW_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_INF)、[`CONFIG_I3C_DW_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_DBG"></a>

## 365.52 `CONFIG_I3C_DW_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_DEFAULT"></a>

## 365.53 `CONFIG_I3C_DW_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_ERR"></a>

## 365.54 `CONFIG_I3C_DW_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_INF"></a>

## 365.55 `CONFIG_I3C_DW_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_OFF"></a>

## 365.56 `CONFIG_I3C_DW_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_DW_LOG_LEVEL_WRN"></a>

## 365.57 `CONFIG_I3C_DW_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_DW_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DesignWare I3C（i3c-dw）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_DW_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE"></a>

## 365.58 `CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_IT51XXX_LOG_LEVEL_OFF
CONFIG_I3C_IT51XXX_LOG_LEVEL_ERR
CONFIG_I3C_IT51XXX_LOG_LEVEL_WRN
CONFIG_I3C_IT51XXX_LOG_LEVEL_INF
CONFIG_I3C_IT51XXX_LOG_LEVEL_DBG
CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_OFF)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_ERR)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_WRN)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_INF)、[`CONFIG_I3C_IT51XXX_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_DBG"></a>

## 365.59 `CONFIG_I3C_IT51XXX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT"></a>

## 365.60 `CONFIG_I3C_IT51XXX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_ERR"></a>

## 365.61 `CONFIG_I3C_IT51XXX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_INF"></a>

## 365.62 `CONFIG_I3C_IT51XXX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_OFF"></a>

## 365.63 `CONFIG_I3C_IT51XXX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_IT51XXX_LOG_LEVEL_WRN"></a>

## 365.64 `CONFIG_I3C_IT51XXX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → IT51xxx I3C（i3c-it51xxx）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_IT51XXX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_CHOICE"></a>

## 365.65 `CONFIG_I3C_LOG_LEVEL_CHOICE`

**提示（Prompt）**：I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_LOG_LEVEL_OFF
CONFIG_I3C_LOG_LEVEL_ERR
CONFIG_I3C_LOG_LEVEL_WRN
CONFIG_I3C_LOG_LEVEL_INF
CONFIG_I3C_LOG_LEVEL_DBG
CONFIG_I3C_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_OFF)、[`CONFIG_I3C_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_ERR)、[`CONFIG_I3C_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_WRN)、[`CONFIG_I3C_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_INF)、[`CONFIG_I3C_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_LOG_LEVEL_DBG"></a>

## 365.66 `CONFIG_I3C_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_DEFAULT"></a>

## 365.67 `CONFIG_I3C_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_ERR"></a>

## 365.68 `CONFIG_I3C_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_INF"></a>

## 365.69 `CONFIG_I3C_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_OFF"></a>

## 365.70 `CONFIG_I3C_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_LOG_LEVEL_WRN"></a>

## 365.71 `CONFIG_I3C_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I3C 总线（i3c）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE"></a>

## 365.72 `CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_MAX32_LOG_LEVEL_OFF
CONFIG_I3C_MAX32_LOG_LEVEL_ERR
CONFIG_I3C_MAX32_LOG_LEVEL_WRN
CONFIG_I3C_MAX32_LOG_LEVEL_INF
CONFIG_I3C_MAX32_LOG_LEVEL_DBG
CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_MAX32_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_OFF)、[`CONFIG_I3C_MAX32_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_ERR)、[`CONFIG_I3C_MAX32_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_WRN)、[`CONFIG_I3C_MAX32_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_INF)、[`CONFIG_I3C_MAX32_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_DBG"></a>

## 365.73 `CONFIG_I3C_MAX32_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT"></a>

## 365.74 `CONFIG_I3C_MAX32_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_ERR"></a>

## 365.75 `CONFIG_I3C_MAX32_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_INF"></a>

## 365.76 `CONFIG_I3C_MAX32_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_OFF"></a>

## 365.77 `CONFIG_I3C_MAX32_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MAX32_LOG_LEVEL_WRN"></a>

## 365.78 `CONFIG_I3C_MAX32_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MAX32 I3C（i3c-max32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MAX32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE"></a>

## 365.79 `CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_MCUX_LOG_LEVEL_OFF
CONFIG_I3C_MCUX_LOG_LEVEL_ERR
CONFIG_I3C_MCUX_LOG_LEVEL_WRN
CONFIG_I3C_MCUX_LOG_LEVEL_INF
CONFIG_I3C_MCUX_LOG_LEVEL_DBG
CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_MCUX_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_OFF)、[`CONFIG_I3C_MCUX_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_ERR)、[`CONFIG_I3C_MCUX_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_WRN)、[`CONFIG_I3C_MCUX_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_INF)、[`CONFIG_I3C_MCUX_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_DBG"></a>

## 365.80 `CONFIG_I3C_MCUX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT"></a>

## 365.81 `CONFIG_I3C_MCUX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_ERR"></a>

## 365.82 `CONFIG_I3C_MCUX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_INF"></a>

## 365.83 `CONFIG_I3C_MCUX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_OFF"></a>

## 365.84 `CONFIG_I3C_MCUX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_MCUX_LOG_LEVEL_WRN"></a>

## 365.85 `CONFIG_I3C_MCUX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I3C（i3c-mcux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_MCUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_CHOICE"></a>

## 365.86 `CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`

**提示（Prompt）**：STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_I3C_STM32_LOG_LEVEL_OFF
CONFIG_I3C_STM32_LOG_LEVEL_ERR
CONFIG_I3C_STM32_LOG_LEVEL_WRN
CONFIG_I3C_STM32_LOG_LEVEL_INF
CONFIG_I3C_STM32_LOG_LEVEL_DBG
CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT)、[`CONFIG_I3C_STM32_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_OFF)、[`CONFIG_I3C_STM32_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_ERR)、[`CONFIG_I3C_STM32_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_WRN)、[`CONFIG_I3C_STM32_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_INF)、[`CONFIG_I3C_STM32_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_DBG)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_DBG"></a>

## 365.87 `CONFIG_I3C_STM32_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT"></a>

## 365.88 `CONFIG_I3C_STM32_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_ERR"></a>

## 365.89 `CONFIG_I3C_STM32_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_INF"></a>

## 365.90 `CONFIG_I3C_STM32_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_OFF"></a>

## 365.91 `CONFIG_I3C_STM32_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_I3C_STM32_LOG_LEVEL_WRN"></a>

## 365.92 `CONFIG_I3C_STM32_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_STM32_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I3C（i3c_stm32）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_I3C_STM32_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE"></a>

## 365.93 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_OFF
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_ERR
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_WRN
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_INF
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DBG
CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_OFF`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_ERR`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_INF`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_INF)、[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DBG`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DBG"></a>

## 365.94 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 365.95 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_ERR"></a>

## 365.96 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_INF"></a>

## 365.97 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_OFF"></a>

## 365.98 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IEEE802154_DRIVER_LOG_LEVEL_WRN"></a>

## 365.99 `CONFIG_IEEE802154_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → IEEE 802.15.4 驱动（IEEE 802.15.4 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IEEE802154_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE"></a>

## 365.100 `CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IMG_MANAGER_LOG_LEVEL_OFF
CONFIG_IMG_MANAGER_LOG_LEVEL_ERR
CONFIG_IMG_MANAGER_LOG_LEVEL_WRN
CONFIG_IMG_MANAGER_LOG_LEVEL_INF
CONFIG_IMG_MANAGER_LOG_LEVEL_DBG
CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_OFF)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_ERR)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_WRN)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_INF)、[`CONFIG_IMG_MANAGER_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_IMG_MANAGER_LOG_LEVEL_DBG)。

<!-- kconfig-navigation -->

[上一章](P364_subsys_logging_配置项参考_13.md) · [返回大纲](大纲.md) · [下一章](P366_subsys_logging_配置项参考_15.md)
