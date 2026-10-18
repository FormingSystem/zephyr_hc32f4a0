---
id: learning.zephyr-docs.kconfig-reference.page-366
title: "`subsys/logging`配置项参考（15/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第366章\_`subsys/logging`配置项参考（15/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_DBG"></a>

## 366.1 `CONFIG_IMG_MANAGER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT"></a>

## 366.2 `CONFIG_IMG_MANAGER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_ERR"></a>

## 366.3 `CONFIG_IMG_MANAGER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_INF"></a>

## 366.4 `CONFIG_IMG_MANAGER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_OFF"></a>

## 366.5 `CONFIG_IMG_MANAGER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IMG_MANAGER_LOG_LEVEL_WRN"></a>

## 366.6 `CONFIG_IMG_MANAGER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（image manager）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE`](P365_subsys_logging_配置项参考_14.md#CONFIG_IMG_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_CHOICE"></a>

## 366.7 `CONFIG_INPUT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_INPUT
```

**默认值（Defaults）**

```text
CONFIG_INPUT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_INPUT_LOG_LEVEL_OFF
CONFIG_INPUT_LOG_LEVEL_ERR
CONFIG_INPUT_LOG_LEVEL_WRN
CONFIG_INPUT_LOG_LEVEL_INF
CONFIG_INPUT_LOG_LEVEL_DBG
CONFIG_INPUT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_INPUT`](P346_subsys_input_配置项参考.md#CONFIG_INPUT)、[`CONFIG_INPUT_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_DEFAULT)、[`CONFIG_INPUT_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_OFF)、[`CONFIG_INPUT_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_ERR)、[`CONFIG_INPUT_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_WRN)、[`CONFIG_INPUT_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_INF)、[`CONFIG_INPUT_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_DBG)。

<a id="CONFIG_INPUT_LOG_LEVEL_DBG"></a>

## 366.8 `CONFIG_INPUT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_DEFAULT"></a>

## 366.9 `CONFIG_INPUT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_ERR"></a>

## 366.10 `CONFIG_INPUT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_INF"></a>

## 366.11 `CONFIG_INPUT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_OFF"></a>

## 366.12 `CONFIG_INPUT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INPUT_LOG_LEVEL_WRN"></a>

## 366.13 `CONFIG_INPUT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → `input`（输入）。 → 输入（input）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INPUT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE"></a>

## 366.14 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_INTC_AMD_ACP
```

**默认值（Defaults）**

```text
CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_INTC_AMD_ACP_LOG_LEVEL_OFF
CONFIG_INTC_AMD_ACP_LOG_LEVEL_ERR
CONFIG_INTC_AMD_ACP_LOG_LEVEL_WRN
CONFIG_INTC_AMD_ACP_LOG_LEVEL_INF
CONFIG_INTC_AMD_ACP_LOG_LEVEL_DBG
CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_INTC_AMD_ACP`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTC_AMD_ACP)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_OFF)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_ERR)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_WRN)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_INF)、[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_DBG)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_DBG"></a>

## 366.15 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT"></a>

## 366.16 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_ERR"></a>

## 366.17 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_INF"></a>

## 366.18 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_OFF"></a>

## 366.19 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_AMD_ACP_LOG_LEVEL_WRN"></a>

## 366.20 `CONFIG_INTC_AMD_ACP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动 → AMD ACP 中断控制器（intc_amd_acp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_AMD_ACP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_CHOICE"></a>

## 366.21 `CONFIG_INTC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_INTC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_INTC_LOG_LEVEL_OFF
CONFIG_INTC_LOG_LEVEL_ERR
CONFIG_INTC_LOG_LEVEL_WRN
CONFIG_INTC_LOG_LEVEL_INF
CONFIG_INTC_LOG_LEVEL_DBG
CONFIG_INTC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_INTC_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_DEFAULT)、[`CONFIG_INTC_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_OFF)、[`CONFIG_INTC_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_ERR)、[`CONFIG_INTC_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_WRN)、[`CONFIG_INTC_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_INF)、[`CONFIG_INTC_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_DBG)。

<a id="CONFIG_INTC_LOG_LEVEL_DBG"></a>

## 366.22 `CONFIG_INTC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_DEFAULT"></a>

## 366.23 `CONFIG_INTC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_ERR"></a>

## 366.24 `CONFIG_INTC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_INF"></a>

## 366.25 `CONFIG_INTC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_OFF"></a>

## 366.26 `CONFIG_INTC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_INTC_LOG_LEVEL_WRN"></a>

## 366.27 `CONFIG_INTC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 中断控制器（intc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_INTC_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_INTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE"></a>

## 366.28 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IPC_SERVICE_BACKEND_ICBMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_OFF
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_ERR
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_WRN
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_INF
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DBG
CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_OFF)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_ERR)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_WRN)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_INF)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DBG)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DBG"></a>

## 366.29 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT"></a>

## 366.30 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_ERR"></a>

## 366.31 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_INF"></a>

## 366.32 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_OFF"></a>

## 366.33 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_WRN"></a>

## 366.34 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend） → 使用独立缓冲区的 ICMSG 后端（ICMSG backend with separate buffers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE"></a>

## 366.35 `CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IPC_SERVICE_LOG_LEVEL_OFF
CONFIG_IPC_SERVICE_LOG_LEVEL_ERR
CONFIG_IPC_SERVICE_LOG_LEVEL_WRN
CONFIG_IPC_SERVICE_LOG_LEVEL_INF
CONFIG_IPC_SERVICE_LOG_LEVEL_DBG
CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_OFF)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_ERR)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_WRN)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_INF)、[`CONFIG_IPC_SERVICE_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_DBG"></a>

## 366.36 `CONFIG_IPC_SERVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT"></a>

## 366.37 `CONFIG_IPC_SERVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_ERR"></a>

## 366.38 `CONFIG_IPC_SERVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_INF"></a>

## 366.39 `CONFIG_IPC_SERVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_OFF"></a>

## 366.40 `CONFIG_IPC_SERVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPC_SERVICE_LOG_LEVEL_WRN"></a>

## 366.41 `CONFIG_IPC_SERVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 处理器间通信服务及后端（IPC service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPC_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_CHOICE"></a>

## 366.42 `CONFIG_IPM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IPM
```

**默认值（Defaults）**

```text
CONFIG_IPM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IPM_LOG_LEVEL_OFF
CONFIG_IPM_LOG_LEVEL_ERR
CONFIG_IPM_LOG_LEVEL_WRN
CONFIG_IPM_LOG_LEVEL_INF
CONFIG_IPM_LOG_LEVEL_DBG
CONFIG_IPM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_DEFAULT)、[`CONFIG_IPM_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_OFF)、[`CONFIG_IPM_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_ERR)、[`CONFIG_IPM_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_WRN)、[`CONFIG_IPM_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_INF)、[`CONFIG_IPM_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_DBG)。

<a id="CONFIG_IPM_LOG_LEVEL_DBG"></a>

## 366.43 `CONFIG_IPM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_DEFAULT"></a>

## 366.44 `CONFIG_IPM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_ERR"></a>

## 366.45 `CONFIG_IPM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_INF"></a>

## 366.46 `CONFIG_IPM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_OFF"></a>

## 366.47 `CONFIG_IPM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IPM_LOG_LEVEL_WRN"></a>

## 366.48 `CONFIG_IPM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → 处理器间邮箱（ipm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IPM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IPM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_CHOICE"></a>

## 366.49 `CONFIG_ISOTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ISOTP
```

**默认值（Defaults）**

```text
CONFIG_ISOTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ISOTP_LOG_LEVEL_OFF
CONFIG_ISOTP_LOG_LEVEL_ERR
CONFIG_ISOTP_LOG_LEVEL_WRN
CONFIG_ISOTP_LOG_LEVEL_INF
CONFIG_ISOTP_LOG_LEVEL_DBG
CONFIG_ISOTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)、[`CONFIG_ISOTP_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_DEFAULT)、[`CONFIG_ISOTP_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_OFF)、[`CONFIG_ISOTP_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_ERR)、[`CONFIG_ISOTP_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_WRN)、[`CONFIG_ISOTP_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_INF)、[`CONFIG_ISOTP_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_DBG)。

<a id="CONFIG_ISOTP_LOG_LEVEL_DBG"></a>

## 366.50 `CONFIG_ISOTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_DEFAULT"></a>

## 366.51 `CONFIG_ISOTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_ERR"></a>

## 366.52 `CONFIG_ISOTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_INF"></a>

## 366.53 `CONFIG_ISOTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_OFF"></a>

## 366.54 `CONFIG_ISOTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ISOTP_LOG_LEVEL_WRN"></a>

## 366.55 `CONFIG_ISOTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISOTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → ISO-TP 传输协议（ISOTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_ISOTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_CHOICE"></a>

## 366.56 `CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_IVSHMEM && CONFIG_VIRTUALIZATION
```

**默认值（Defaults）**

```text
CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_IVSHMEM_LOG_LEVEL_OFF
CONFIG_IVSHMEM_LOG_LEVEL_ERR
CONFIG_IVSHMEM_LOG_LEVEL_WRN
CONFIG_IVSHMEM_LOG_LEVEL_INF
CONFIG_IVSHMEM_LOG_LEVEL_DBG
CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_IVSHMEM`](P184_drivers_virtualization_配置项参考.md#CONFIG_IVSHMEM)、[`CONFIG_VIRTUALIZATION`](P184_drivers_virtualization_配置项参考.md#CONFIG_VIRTUALIZATION)、[`CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT)、[`CONFIG_IVSHMEM_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_OFF)、[`CONFIG_IVSHMEM_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_ERR)、[`CONFIG_IVSHMEM_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_WRN)、[`CONFIG_IVSHMEM_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_INF)、[`CONFIG_IVSHMEM_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_DBG)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_DBG"></a>

## 366.57 `CONFIG_IVSHMEM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT"></a>

## 366.58 `CONFIG_IVSHMEM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_ERR"></a>

## 366.59 `CONFIG_IVSHMEM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_INF"></a>

## 366.60 `CONFIG_IVSHMEM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_OFF"></a>

## 366.61 `CONFIG_IVSHMEM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_IVSHMEM_LOG_LEVEL_WRN"></a>

## 366.62 `CONFIG_IVSHMEM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IVSHMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 虚拟化客户机驱动（Virtualization Guest Drivers） → 虚拟机间共享内存设备（Inter-VM Shared Memory，ivshmem） → 虚拟机间共享内存（ivshmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_IVSHMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_CHOICE"></a>

## 366.63 `CONFIG_KERNEL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_KERNEL_LOG_LEVEL_OFF
CONFIG_KERNEL_LOG_LEVEL_ERR
CONFIG_KERNEL_LOG_LEVEL_WRN
CONFIG_KERNEL_LOG_LEVEL_INF
CONFIG_KERNEL_LOG_LEVEL_DBG
CONFIG_KERNEL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_KERNEL_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_DEFAULT)、[`CONFIG_KERNEL_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_OFF)、[`CONFIG_KERNEL_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_ERR)、[`CONFIG_KERNEL_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_WRN)、[`CONFIG_KERNEL_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_INF)、[`CONFIG_KERNEL_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_DBG)。

<a id="CONFIG_KERNEL_LOG_LEVEL_DBG"></a>

## 366.64 `CONFIG_KERNEL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_DEFAULT"></a>

## 366.65 `CONFIG_KERNEL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_ERR"></a>

## 366.66 `CONFIG_KERNEL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_INF"></a>

## 366.67 `CONFIG_KERNEL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_OFF"></a>

## 366.68 `CONFIG_KERNEL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_KERNEL_LOG_LEVEL_WRN"></a>

## 366.69 `CONFIG_KERNEL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_KERNEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核（kernel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_KERNEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_CHOICE"></a>

## 366.70 `CONFIG_LED_LOG_LEVEL_CHOICE`

**提示（Prompt）**：发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LED
```

**默认值（Defaults）**

```text
CONFIG_LED_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LED_LOG_LEVEL_OFF
CONFIG_LED_LOG_LEVEL_ERR
CONFIG_LED_LOG_LEVEL_WRN
CONFIG_LED_LOG_LEVEL_INF
CONFIG_LED_LOG_LEVEL_DBG
CONFIG_LED_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_LED_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_DEFAULT)、[`CONFIG_LED_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_OFF)、[`CONFIG_LED_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_ERR)、[`CONFIG_LED_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_WRN)、[`CONFIG_LED_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_INF)、[`CONFIG_LED_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_DBG)。

<a id="CONFIG_LED_LOG_LEVEL_DBG"></a>

## 366.71 `CONFIG_LED_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_DEFAULT"></a>

## 366.72 `CONFIG_LED_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_ERR"></a>

## 366.73 `CONFIG_LED_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_INF"></a>

## 366.74 `CONFIG_LED_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_OFF"></a>

## 366.75 `CONFIG_LED_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_LOG_LEVEL_WRN"></a>

## 366.76 `CONFIG_LED_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → 发光二极管（led）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_CHOICE"></a>

## 366.77 `CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LED_STRIP_LOG_LEVEL_OFF
CONFIG_LED_STRIP_LOG_LEVEL_ERR
CONFIG_LED_STRIP_LOG_LEVEL_WRN
CONFIG_LED_STRIP_LOG_LEVEL_INF
CONFIG_LED_STRIP_LOG_LEVEL_DBG
CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT)、[`CONFIG_LED_STRIP_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_OFF)、[`CONFIG_LED_STRIP_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_ERR)、[`CONFIG_LED_STRIP_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_WRN)、[`CONFIG_LED_STRIP_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_INF)、[`CONFIG_LED_STRIP_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_DBG)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_DBG"></a>

## 366.78 `CONFIG_LED_STRIP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT"></a>

## 366.79 `CONFIG_LED_STRIP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_ERR"></a>

## 366.80 `CONFIG_LED_STRIP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_INF"></a>

## 366.81 `CONFIG_LED_STRIP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_OFF"></a>

## 366.82 `CONFIG_LED_STRIP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LED_STRIP_LOG_LEVEL_WRN"></a>

## 366.83 `CONFIG_LED_STRIP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LED_STRIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带（LED strip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LED_STRIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_CHOICE"></a>

## 366.84 `CONFIG_LIN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LIN
```

**默认值（Defaults）**

```text
CONFIG_LIN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LIN_LOG_LEVEL_OFF
CONFIG_LIN_LOG_LEVEL_ERR
CONFIG_LIN_LOG_LEVEL_WRN
CONFIG_LIN_LOG_LEVEL_INF
CONFIG_LIN_LOG_LEVEL_DBG
CONFIG_LIN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)、[`CONFIG_LIN_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_DEFAULT)、[`CONFIG_LIN_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_OFF)、[`CONFIG_LIN_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_ERR)、[`CONFIG_LIN_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_WRN)、[`CONFIG_LIN_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_INF)、[`CONFIG_LIN_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_DBG)。

<a id="CONFIG_LIN_LOG_LEVEL_DBG"></a>

## 366.85 `CONFIG_LIN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_DEFAULT"></a>

## 366.86 `CONFIG_LIN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_ERR"></a>

## 366.87 `CONFIG_LIN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_INF"></a>

## 366.88 `CONFIG_LIN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_OFF"></a>

## 366.89 `CONFIG_LIN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LIN_LOG_LEVEL_WRN"></a>

## 366.90 `CONFIG_LIN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → 本地互连网络（LIN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LIN_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_CHOICE"></a>

## 366.91 `CONFIG_LLEXT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
CONFIG_LLEXT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LLEXT_LOG_LEVEL_OFF
CONFIG_LLEXT_LOG_LEVEL_ERR
CONFIG_LLEXT_LOG_LEVEL_WRN
CONFIG_LLEXT_LOG_LEVEL_INF
CONFIG_LLEXT_LOG_LEVEL_DBG
CONFIG_LLEXT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_DEFAULT)、[`CONFIG_LLEXT_LOG_LEVEL_OFF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_OFF)、[`CONFIG_LLEXT_LOG_LEVEL_ERR`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_ERR)、[`CONFIG_LLEXT_LOG_LEVEL_WRN`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_WRN)、[`CONFIG_LLEXT_LOG_LEVEL_INF`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_INF)、[`CONFIG_LLEXT_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_DBG)。

<a id="CONFIG_LLEXT_LOG_LEVEL_DBG"></a>

## 366.92 `CONFIG_LLEXT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_DEFAULT"></a>

## 366.93 `CONFIG_LLEXT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_ERR"></a>

## 366.94 `CONFIG_LLEXT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_INF"></a>

## 366.95 `CONFIG_LLEXT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_OFF"></a>

## 366.96 `CONFIG_LLEXT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLEXT_LOG_LEVEL_WRN"></a>

## 366.97 `CONFIG_LLEXT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 可链接可加载扩展（llext）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LLEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE"></a>

## 366.98 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG
CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF)、[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG"></a>

## 366.99 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT"></a>

## 366.100 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P365_subsys_logging_配置项参考_14.md) · [返回大纲](大纲.md) · [下一章](P367_subsys_logging_配置项参考_16.md)
