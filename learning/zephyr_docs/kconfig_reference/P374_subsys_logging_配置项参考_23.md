---
id: learning.zephyr-docs.kconfig-reference.page-374
title: "`subsys/logging`配置项参考（23/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第374章\_`subsys/logging`配置项参考（23/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_DBG"></a>

## 374.1 `CONFIG_PM_CPU_OPS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT"></a>

## 374.2 `CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_ERR"></a>

## 374.3 `CONFIG_PM_CPU_OPS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_INF"></a>

## 374.4 `CONFIG_PM_CPU_OPS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_OFF"></a>

## 374.5 `CONFIG_PM_CPU_OPS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_WRN"></a>

## 374.6 `CONFIG_PM_CPU_OPS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动 → 电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE"></a>

## 374.7 `CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PM_DEVICE
```

**默认值（Defaults）**

```text
CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PM_DEVICE_LOG_LEVEL_OFF
CONFIG_PM_DEVICE_LOG_LEVEL_ERR
CONFIG_PM_DEVICE_LOG_LEVEL_WRN
CONFIG_PM_DEVICE_LOG_LEVEL_INF
CONFIG_PM_DEVICE_LOG_LEVEL_DBG
CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_PM_DEVICE_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_OFF)、[`CONFIG_PM_DEVICE_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_ERR)、[`CONFIG_PM_DEVICE_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_WRN)、[`CONFIG_PM_DEVICE_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_INF)、[`CONFIG_PM_DEVICE_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_DBG"></a>

## 374.8 `CONFIG_PM_DEVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT"></a>

## 374.9 `CONFIG_PM_DEVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_ERR"></a>

## 374.10 `CONFIG_PM_DEVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_INF"></a>

## 374.11 `CONFIG_PM_DEVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_OFF"></a>

## 374.12 `CONFIG_PM_DEVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_DEVICE_LOG_LEVEL_WRN"></a>

## 374.13 `CONFIG_PM_DEVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 设备电源管理（Device Power Management） → 设备电源管理（Device Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_CHOICE"></a>

## 374.14 `CONFIG_PM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PM
```

**默认值（Defaults）**

```text
CONFIG_PM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PM_LOG_LEVEL_OFF
CONFIG_PM_LOG_LEVEL_ERR
CONFIG_PM_LOG_LEVEL_WRN
CONFIG_PM_LOG_LEVEL_INF
CONFIG_PM_LOG_LEVEL_DBG
CONFIG_PM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_PM_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_DEFAULT)、[`CONFIG_PM_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_OFF)、[`CONFIG_PM_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_ERR)、[`CONFIG_PM_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_WRN)、[`CONFIG_PM_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_INF)、[`CONFIG_PM_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_DBG)。

<a id="CONFIG_PM_LOG_LEVEL_DBG"></a>

## 374.15 `CONFIG_PM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_DEFAULT"></a>

## 374.16 `CONFIG_PM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_ERR"></a>

## 374.17 `CONFIG_PM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_INF"></a>

## 374.18 `CONFIG_PM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_OFF"></a>

## 374.19 `CONFIG_PM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_LOG_LEVEL_WRN"></a>

## 374.20 `CONFIG_PM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 电源管理（Power Management） → 系统电源管理（System Power Management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PM_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE"></a>

## 374.21 `CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && (CONFIG_POSIX_SINGLE_PROCESS || CONFIG_XSI_SINGLE_PROCESS) && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_POSIX_ENV_LOG_LEVEL_OFF
CONFIG_POSIX_ENV_LOG_LEVEL_ERR
CONFIG_POSIX_ENV_LOG_LEVEL_WRN
CONFIG_POSIX_ENV_LOG_LEVEL_INF
CONFIG_POSIX_ENV_LOG_LEVEL_DBG
CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_XSI_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_SINGLE_PROCESS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT)、[`CONFIG_POSIX_ENV_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_OFF)、[`CONFIG_POSIX_ENV_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_ERR)、[`CONFIG_POSIX_ENV_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_WRN)、[`CONFIG_POSIX_ENV_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_INF)、[`CONFIG_POSIX_ENV_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_DBG)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_DBG"></a>

## 374.22 `CONFIG_POSIX_ENV_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT"></a>

## 374.23 `CONFIG_POSIX_ENV_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_ERR"></a>

## 374.24 `CONFIG_POSIX_ENV_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_INF"></a>

## 374.25 `CONFIG_POSIX_ENV_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_OFF"></a>

## 374.26 `CONFIG_POSIX_ENV_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POSIX_ENV_LOG_LEVEL_WRN"></a>

## 374.27 `CONFIG_POSIX_ENV_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 环境变量日志（POSIX env logging）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POSIX_ENV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE"></a>

## 374.28 `CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POWER_DOMAIN
```

**默认值（Defaults）**

```text
CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_POWER_DOMAIN_LOG_LEVEL_OFF
CONFIG_POWER_DOMAIN_LOG_LEVEL_ERR
CONFIG_POWER_DOMAIN_LOG_LEVEL_WRN
CONFIG_POWER_DOMAIN_LOG_LEVEL_INF
CONFIG_POWER_DOMAIN_LOG_LEVEL_DBG
CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POWER_DOMAIN`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_OFF)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_ERR)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_WRN)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_INF)、[`CONFIG_POWER_DOMAIN_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_DBG)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_DBG"></a>

## 374.29 `CONFIG_POWER_DOMAIN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT"></a>

## 374.30 `CONFIG_POWER_DOMAIN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_ERR"></a>

## 374.31 `CONFIG_POWER_DOMAIN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_INF"></a>

## 374.32 `CONFIG_POWER_DOMAIN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_OFF"></a>

## 374.33 `CONFIG_POWER_DOMAIN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_POWER_DOMAIN_LOG_LEVEL_WRN"></a>

## 374.34 `CONFIG_POWER_DOMAIN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电源域驱动（Power Domain Drivers） → 电源域（power_domain）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_POWER_DOMAIN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_CHOICE"></a>

## 374.35 `CONFIG_PS2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PS2
```

**默认值（Defaults）**

```text
CONFIG_PS2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PS2_LOG_LEVEL_OFF
CONFIG_PS2_LOG_LEVEL_ERR
CONFIG_PS2_LOG_LEVEL_WRN
CONFIG_PS2_LOG_LEVEL_INF
CONFIG_PS2_LOG_LEVEL_DBG
CONFIG_PS2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)、[`CONFIG_PS2_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_DEFAULT)、[`CONFIG_PS2_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_OFF)、[`CONFIG_PS2_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_ERR)、[`CONFIG_PS2_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_WRN)、[`CONFIG_PS2_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_INF)、[`CONFIG_PS2_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_DBG)。

<a id="CONFIG_PS2_LOG_LEVEL_DBG"></a>

## 374.36 `CONFIG_PS2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_DEFAULT"></a>

## 374.37 `CONFIG_PS2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_ERR"></a>

## 374.38 `CONFIG_PS2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_INF"></a>

## 374.39 `CONFIG_PS2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_OFF"></a>

## 374.40 `CONFIG_PS2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PS2_LOG_LEVEL_WRN"></a>

## 374.41 `CONFIG_PS2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PS2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → PS/2 接口（ps2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PS2_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PS2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_CHOICE"></a>

## 374.42 `CONFIG_PSI5_LOG_LEVEL_CHOICE`

**提示（Prompt）**：外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PSI5
```

**默认值（Defaults）**

```text
CONFIG_PSI5_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PSI5_LOG_LEVEL_OFF
CONFIG_PSI5_LOG_LEVEL_ERR
CONFIG_PSI5_LOG_LEVEL_WRN
CONFIG_PSI5_LOG_LEVEL_INF
CONFIG_PSI5_LOG_LEVEL_DBG
CONFIG_PSI5_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PSI5`](P140_drivers_psi5_配置项参考.md#CONFIG_PSI5)、[`CONFIG_PSI5_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_DEFAULT)、[`CONFIG_PSI5_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_OFF)、[`CONFIG_PSI5_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_ERR)、[`CONFIG_PSI5_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_WRN)、[`CONFIG_PSI5_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_INF)、[`CONFIG_PSI5_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_DBG)。

<a id="CONFIG_PSI5_LOG_LEVEL_DBG"></a>

## 374.43 `CONFIG_PSI5_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_DEFAULT"></a>

## 374.44 `CONFIG_PSI5_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_ERR"></a>

## 374.45 `CONFIG_PSI5_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_INF"></a>

## 374.46 `CONFIG_PSI5_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_OFF"></a>

## 374.47 `CONFIG_PSI5_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PSI5_LOG_LEVEL_WRN"></a>

## 374.48 `CONFIG_PSI5_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PSI5_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动 → 外围传感器接口 5（psi5）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PSI5_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PSI5_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE"></a>

## 374.49 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_BARRIERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_OFF
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_ERR
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_WRN
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_INF
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DBG
CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_BARRIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_BARRIERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DBG"></a>

## 374.50 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT"></a>

## 374.51 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_ERR"></a>

## 374.52 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_INF"></a>

## 374.53 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_OFF"></a>

## 374.54 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_BARRIER_LOG_LEVEL_WRN"></a>

## 374.55 `CONFIG_PTHREAD_BARRIER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers） → POSIX 线程屏障（POSIX thread barriers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_BARRIER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE"></a>

## 374.56 `CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_COND_LOG_LEVEL_OFF
CONFIG_PTHREAD_COND_LOG_LEVEL_ERR
CONFIG_PTHREAD_COND_LOG_LEVEL_WRN
CONFIG_PTHREAD_COND_LOG_LEVEL_INF
CONFIG_PTHREAD_COND_LOG_LEVEL_DBG
CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_COND_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_DBG"></a>

## 374.57 `CONFIG_PTHREAD_COND_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT"></a>

## 374.58 `CONFIG_PTHREAD_COND_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_ERR"></a>

## 374.59 `CONFIG_PTHREAD_COND_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_INF"></a>

## 374.60 `CONFIG_PTHREAD_COND_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_OFF"></a>

## 374.61 `CONFIG_PTHREAD_COND_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_COND_LOG_LEVEL_WRN"></a>

## 374.62 `CONFIG_PTHREAD_COND_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 条件变量（POSIX condition variable）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_COND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE"></a>

## 374.63 `CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_KEY_LOG_LEVEL_OFF
CONFIG_PTHREAD_KEY_LOG_LEVEL_ERR
CONFIG_PTHREAD_KEY_LOG_LEVEL_WRN
CONFIG_PTHREAD_KEY_LOG_LEVEL_INF
CONFIG_PTHREAD_KEY_LOG_LEVEL_DBG
CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_KEY_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_DBG"></a>

## 374.64 `CONFIG_PTHREAD_KEY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT"></a>

## 374.65 `CONFIG_PTHREAD_KEY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_ERR"></a>

## 374.66 `CONFIG_PTHREAD_KEY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_INF"></a>

## 374.67 `CONFIG_PTHREAD_KEY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_OFF"></a>

## 374.68 `CONFIG_PTHREAD_KEY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_KEY_LOG_LEVEL_WRN"></a>

## 374.69 `CONFIG_PTHREAD_KEY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程专有数据（POSIX thread-specific data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_KEY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_CHOICE"></a>

## 374.70 `CONFIG_PTHREAD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_LOG_LEVEL_OFF
CONFIG_PTHREAD_LOG_LEVEL_ERR
CONFIG_PTHREAD_LOG_LEVEL_WRN
CONFIG_PTHREAD_LOG_LEVEL_INF
CONFIG_PTHREAD_LOG_LEVEL_DBG
CONFIG_PTHREAD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_DBG"></a>

## 374.71 `CONFIG_PTHREAD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_DEFAULT"></a>

## 374.72 `CONFIG_PTHREAD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_ERR"></a>

## 374.73 `CONFIG_PTHREAD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_INF"></a>

## 374.74 `CONFIG_PTHREAD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_OFF"></a>

## 374.75 `CONFIG_PTHREAD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_LOG_LEVEL_WRN"></a>

## 374.76 `CONFIG_PTHREAD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 线程（POSIX thread）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE"></a>

## 374.77 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_OFF
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_ERR
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_WRN
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_INF
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DBG
CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DBG"></a>

## 374.78 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT"></a>

## 374.79 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_ERR"></a>

## 374.80 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_INF"></a>

## 374.81 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_OFF"></a>

## 374.82 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_MUTEX_LOG_LEVEL_WRN"></a>

## 374.83 `CONFIG_PTHREAD_MUTEX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support） → POSIX 互斥锁（POSIX mutex）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_MUTEX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE"></a>

## 374.84 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_RW_LOCKS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_OFF
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_ERR
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_WRN
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_INF
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DBG
CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_RW_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RW_LOCKS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DBG"></a>

## 374.85 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT"></a>

## 374.86 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_ERR"></a>

## 374.87 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_INF"></a>

## 374.88 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_OFF"></a>

## 374.89 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_WRN"></a>

## 374.90 `CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks） → POSIX 读写锁（POSIX Reader-Writer Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_RWLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE"></a>

## 374.91 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_SPIN_LOCKS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_OFF
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_ERR
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_WRN
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_INF
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DBG
CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_SPIN_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SPIN_LOCKS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_OFF)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_ERR)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_WRN)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_INF)、[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DBG)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DBG"></a>

## 374.92 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT"></a>

## 374.93 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_ERR"></a>

## 374.94 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_INF"></a>

## 374.95 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_OFF"></a>

## 374.96 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_WRN"></a>

## 374.97 `CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks） → POSIX 自旋锁（POSIX Spin Locks）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PTHREAD_SPINLOCK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_CHOICE"></a>

## 374.98 `CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PULSE_IO_LOG_LEVEL_OFF
CONFIG_PULSE_IO_LOG_LEVEL_ERR
CONFIG_PULSE_IO_LOG_LEVEL_WRN
CONFIG_PULSE_IO_LOG_LEVEL_INF
CONFIG_PULSE_IO_LOG_LEVEL_DBG
CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)、[`CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT)、[`CONFIG_PULSE_IO_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_PULSE_IO_LOG_LEVEL_OFF)、[`CONFIG_PULSE_IO_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_PULSE_IO_LOG_LEVEL_ERR)、[`CONFIG_PULSE_IO_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_PULSE_IO_LOG_LEVEL_WRN)、[`CONFIG_PULSE_IO_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_PULSE_IO_LOG_LEVEL_INF)、[`CONFIG_PULSE_IO_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_DBG)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_DBG"></a>

## 374.99 `CONFIG_PULSE_IO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT"></a>

## 374.100 `CONFIG_PULSE_IO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P373_subsys_logging_配置项参考_22.md) · [返回大纲](大纲.md) · [下一章](P375_subsys_logging_配置项参考_24.md)
