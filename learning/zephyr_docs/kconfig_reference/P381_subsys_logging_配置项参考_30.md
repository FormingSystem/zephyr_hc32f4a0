---
id: learning.zephyr-docs.kconfig-reference.page-381
title: "`subsys/logging`配置项参考（30/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第381章\_`subsys/logging`配置项参考（30/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DBG"></a>

## 381.1 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT"></a>

## 381.2 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_ERR"></a>

## 381.3 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_INF"></a>

## 381.4 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_OFF"></a>

## 381.5 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_WRN"></a>

## 381.6 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces） → XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_CHOICE"></a>

## 381.7 `CONFIG_ZBUS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
CONFIG_ZBUS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ZBUS_LOG_LEVEL_OFF
CONFIG_ZBUS_LOG_LEVEL_ERR
CONFIG_ZBUS_LOG_LEVEL_WRN
CONFIG_ZBUS_LOG_LEVEL_INF
CONFIG_ZBUS_LOG_LEVEL_DBG
CONFIG_ZBUS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ZBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS)、[`CONFIG_ZBUS_LOG_LEVEL_DEFAULT`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_DEFAULT)、[`CONFIG_ZBUS_LOG_LEVEL_OFF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_OFF)、[`CONFIG_ZBUS_LOG_LEVEL_ERR`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_ERR)、[`CONFIG_ZBUS_LOG_LEVEL_WRN`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_WRN)、[`CONFIG_ZBUS_LOG_LEVEL_INF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_INF)、[`CONFIG_ZBUS_LOG_LEVEL_DBG`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_DBG)。

<a id="CONFIG_ZBUS_LOG_LEVEL_DBG"></a>

## 381.8 `CONFIG_ZBUS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_DEFAULT"></a>

## 381.9 `CONFIG_ZBUS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_ERR"></a>

## 381.10 `CONFIG_ZBUS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_INF"></a>

## 381.11 `CONFIG_ZBUS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_OFF"></a>

## 381.12 `CONFIG_ZBUS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_LOG_LEVEL_WRN"></a>

## 381.13 `CONFIG_ZBUS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 消息总线（zbus）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE"></a>

## 381.14 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ZBUS_PROXY_AGENT_IPC && CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_OFF
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_ERR
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_WRN
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_INF
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DBG
CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ZBUS_PROXY_AGENT_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT_IPC)、[`CONFIG_ZBUS_PROXY_AGENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_OFF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_OFF)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_ERR`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_ERR)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_WRN`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_WRN)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_INF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_INF)、[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DBG`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DBG)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DBG"></a>

## 381.15 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT"></a>

## 381.16 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_ERR"></a>

## 381.17 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_INF"></a>

## 381.18 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_OFF"></a>

## 381.19 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_WRN"></a>

## 381.20 `CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend） → ZBus 代理的处理器间通信后端（zbus_proxy_agent_ipc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_IPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE"></a>

## 381.21 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_OFF
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_ERR
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_WRN
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_INF
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DBG
CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ZBUS_PROXY_AGENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_OFF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_OFF)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_ERR`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_ERR)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_WRN`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_WRN)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_INF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_INF)、[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DBG`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DBG)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DBG"></a>

## 381.22 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT"></a>

## 381.23 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_ERR"></a>

## 381.24 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_INF"></a>

## 381.25 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_OFF"></a>

## 381.26 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_WRN"></a>

## 381.27 `CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理（zbus_proxy_agent）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZBUS_PROXY_AGENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_CHOICE"></a>

## 381.28 `CONFIG_ZMS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ZMS
```

**默认值（Defaults）**

```text
CONFIG_ZMS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ZMS_LOG_LEVEL_OFF
CONFIG_ZMS_LOG_LEVEL_ERR
CONFIG_ZMS_LOG_LEVEL_WRN
CONFIG_ZMS_LOG_LEVEL_INF
CONFIG_ZMS_LOG_LEVEL_DBG
CONFIG_ZMS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)、[`CONFIG_ZMS_LOG_LEVEL_DEFAULT`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_DEFAULT)、[`CONFIG_ZMS_LOG_LEVEL_OFF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_OFF)、[`CONFIG_ZMS_LOG_LEVEL_ERR`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_ERR)、[`CONFIG_ZMS_LOG_LEVEL_WRN`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_WRN)、[`CONFIG_ZMS_LOG_LEVEL_INF`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_INF)、[`CONFIG_ZMS_LOG_LEVEL_DBG`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_DBG)。

<a id="CONFIG_ZMS_LOG_LEVEL_DBG"></a>

## 381.29 `CONFIG_ZMS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_DEFAULT"></a>

## 381.30 `CONFIG_ZMS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_ERR"></a>

## 381.31 `CONFIG_ZMS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_INF"></a>

## 381.32 `CONFIG_ZMS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_OFF"></a>

## 381.33 `CONFIG_ZMS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ZMS_LOG_LEVEL_WRN"></a>

## 381.34 `CONFIG_ZMS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZMS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → Zephyr 内存存储（zms）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOG_LEVEL_CHOICE`](P381_subsys_logging_配置项参考_30.md#CONFIG_ZMS_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P380_subsys_logging_配置项参考_29.md) · [返回大纲](大纲.md) · [下一章](P382_subsys_lorawan_配置项参考.md)
