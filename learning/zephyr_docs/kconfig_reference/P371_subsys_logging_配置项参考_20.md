---
id: learning.zephyr-docs.kconfig-reference.page-371
title: "`subsys/logging`配置项参考（20/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第371章\_`subsys/logging`配置项参考（20/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_ERR"></a>

## 371.1 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_INF"></a>

## 371.2 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_OFF"></a>

## 371.3 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_WRN"></a>

## 371.4 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE"></a>

## 371.5 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_ZBASIC && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_ZBASIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_ZBASIC)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DBG"></a>

## 371.6 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT"></a>

## 371.7 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_ERR"></a>

## 371.8 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_INF"></a>

## 371.9 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_OFF"></a>

## 371.10 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_WRN"></a>

## 371.11 `CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands） → MCUmgr Zephyr 基础管理组（mcumgr_grp_zbasic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_ZBASIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_CHOICE"></a>

## 371.12 `CONFIG_MCUMGR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_LOG_LEVEL_OFF
CONFIG_MCUMGR_LOG_LEVEL_ERR
CONFIG_MCUMGR_LOG_LEVEL_WRN
CONFIG_MCUMGR_LOG_LEVEL_INF
CONFIG_MCUMGR_LOG_LEVEL_DBG
CONFIG_MCUMGR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_DBG"></a>

## 371.13 `CONFIG_MCUMGR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_DEFAULT"></a>

## 371.14 `CONFIG_MCUMGR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_ERR"></a>

## 371.15 `CONFIG_MCUMGR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_INF"></a>

## 371.16 `CONFIG_MCUMGR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_OFF"></a>

## 371.17 `CONFIG_MCUMGR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_LOG_LEVEL_WRN"></a>

## 371.18 `CONFIG_MCUMGR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 微控制器管理（mcumgr）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE"></a>

## 371.19 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && (CONFIG_SMP_CLIENT || CONFIG_ZTEST) && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_OFF
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_ERR
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_WRN
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_INF
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DBG
CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SMP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMP_CLIENT)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DBG"></a>

## 371.20 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 371.21 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_ERR"></a>

## 371.22 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_INF"></a>

## 371.23 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_OFF"></a>

## 371.24 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_WRN"></a>

## 371.25 `CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client） → MCUmgr 简单管理协议客户端（mcumgr_smp_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_SMP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE"></a>

## 371.26 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_OFF
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_ERR
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_WRN
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_INF
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DBG
CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DBG"></a>

## 371.27 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT"></a>

## 371.28 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_ERR"></a>

## 371.29 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_INF"></a>

## 371.30 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_OFF"></a>

## 371.31 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_WRN"></a>

## 371.32 `CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → MCUmgr 传输（mcumgr_transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE"></a>

## 371.33 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_TRANSPORT_LORAWAN && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_OFF
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_ERR
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_WRN
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_INF
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DBG
CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_LORAWAN)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DBG"></a>

## 371.34 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT"></a>

## 371.35 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_ERR"></a>

## 371.36 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_INF"></a>

## 371.37 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_OFF"></a>

## 371.38 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_WRN"></a>

## 371.39 `CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → LoRaWAN MCUmgr 简单管理协议传输（SMP transport） → LoRaWAN MCUmgr 简单管理协议传输（LoRaWAN MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE"></a>

## 371.40 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_TRANSPORT_SPI && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_OFF
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_ERR
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_WRN
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_INF
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DBG
CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_TRANSPORT_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SPI)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DBG"></a>

## 371.41 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT"></a>

## 371.42 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_ERR"></a>

## 371.43 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_INF"></a>

## 371.44 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_OFF"></a>

## 371.45 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_WRN"></a>

## 371.46 `CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 传输及传输相关配置选项（Transports and Transport Related Configuration Options） → SPI MCUmgr 简单管理协议传输（SMP transport） → SPI MCUmgr 简单管理协议传输（SPI MCUmgr SMP transport）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_TRANSPORT_SPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE"></a>

## 371.47 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUX_FLEXIO
```

**默认值（Defaults）**

```text
CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUX_FLEXIO_LOG_LEVEL_OFF
CONFIG_MCUX_FLEXIO_LOG_LEVEL_ERR
CONFIG_MCUX_FLEXIO_LOG_LEVEL_WRN
CONFIG_MCUX_FLEXIO_LOG_LEVEL_INF
CONFIG_MCUX_FLEXIO_LOG_LEVEL_DBG
CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_OFF)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_ERR)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_WRN)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_INF)、[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_DBG"></a>

## 371.48 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT"></a>

## 371.49 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_ERR"></a>

## 371.50 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_INF"></a>

## 371.51 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_OFF"></a>

## 371.52 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUX_FLEXIO_LOG_LEVEL_WRN"></a>

## 371.53 `CONFIG_MCUX_FLEXIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → MCUX FlexIO 灵活输入输出（mcux_flexio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUX_FLEXIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_CHOICE"></a>

## 371.54 `CONFIG_MDIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MDIO
```

**默认值（Defaults）**

```text
CONFIG_MDIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MDIO_LOG_LEVEL_OFF
CONFIG_MDIO_LOG_LEVEL_ERR
CONFIG_MDIO_LOG_LEVEL_WRN
CONFIG_MDIO_LOG_LEVEL_INF
CONFIG_MDIO_LOG_LEVEL_DBG
CONFIG_MDIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)、[`CONFIG_MDIO_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_DEFAULT)、[`CONFIG_MDIO_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_OFF)、[`CONFIG_MDIO_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_ERR)、[`CONFIG_MDIO_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_WRN)、[`CONFIG_MDIO_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_INF)、[`CONFIG_MDIO_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_DBG)。

<a id="CONFIG_MDIO_LOG_LEVEL_DBG"></a>

## 371.55 `CONFIG_MDIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_DEFAULT"></a>

## 371.56 `CONFIG_MDIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_ERR"></a>

## 371.57 `CONFIG_MDIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_INF"></a>

## 371.58 `CONFIG_MDIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_OFF"></a>

## 371.59 `CONFIG_MDIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDIO_LOG_LEVEL_WRN"></a>

## 371.60 `CONFIG_MDIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 管理数据输入/输出（Management Data Input/Output，MDIO）驱动 → 管理数据输入输出（mdio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MDIO_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE"></a>

## 371.61 `CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NXP_MEDIAMIX_BLK_CTRL
```

**默认值（Defaults）**

```text
CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MEDIAMIX_LOG_LEVEL_OFF
CONFIG_MEDIAMIX_LOG_LEVEL_ERR
CONFIG_MEDIAMIX_LOG_LEVEL_WRN
CONFIG_MEDIAMIX_LOG_LEVEL_INF
CONFIG_MEDIAMIX_LOG_LEVEL_DBG
CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NXP_MEDIAMIX_BLK_CTRL`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_MEDIAMIX_BLK_CTRL)、[`CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT)、[`CONFIG_MEDIAMIX_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_OFF)、[`CONFIG_MEDIAMIX_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_ERR)、[`CONFIG_MEDIAMIX_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_WRN)、[`CONFIG_MEDIAMIX_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_INF)、[`CONFIG_MEDIAMIX_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_DBG)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_DBG"></a>

## 371.62 `CONFIG_MEDIAMIX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT"></a>

## 371.63 `CONFIG_MEDIAMIX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_ERR"></a>

## 371.64 `CONFIG_MEDIAMIX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_INF"></a>

## 371.65 `CONFIG_MEDIAMIX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_OFF"></a>

## 371.66 `CONFIG_MEDIAMIX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEDIAMIX_LOG_LEVEL_WRN"></a>

## 371.67 `CONFIG_MEDIAMIX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动 → 媒体混合模块（mediamix）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEDIAMIX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_CHOICE"></a>

## 371.68 `CONFIG_MEMC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MEMC
```

**默认值（Defaults）**

```text
CONFIG_MEMC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MEMC_LOG_LEVEL_OFF
CONFIG_MEMC_LOG_LEVEL_ERR
CONFIG_MEMC_LOG_LEVEL_WRN
CONFIG_MEMC_LOG_LEVEL_INF
CONFIG_MEMC_LOG_LEVEL_DBG
CONFIG_MEMC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_DEFAULT)、[`CONFIG_MEMC_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_OFF)、[`CONFIG_MEMC_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_ERR)、[`CONFIG_MEMC_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_WRN)、[`CONFIG_MEMC_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_INF)、[`CONFIG_MEMC_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_DBG)。

<a id="CONFIG_MEMC_LOG_LEVEL_DBG"></a>

## 371.69 `CONFIG_MEMC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_DEFAULT"></a>

## 371.70 `CONFIG_MEMC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_ERR"></a>

## 371.71 `CONFIG_MEMC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_INF"></a>

## 371.72 `CONFIG_MEMC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_OFF"></a>

## 371.73 `CONFIG_MEMC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_LOG_LEVEL_WRN"></a>

## 371.74 `CONFIG_MEMC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 存储器控制器（memc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE"></a>

## 371.75 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_MEMC_RAM && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MEMC_RAMDISK_LOG_LEVEL_OFF
CONFIG_MEMC_RAMDISK_LOG_LEVEL_ERR
CONFIG_MEMC_RAMDISK_LOG_LEVEL_WRN
CONFIG_MEMC_RAMDISK_LOG_LEVEL_INF
CONFIG_MEMC_RAMDISK_LOG_LEVEL_DBG
CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_MEMC_RAM`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MEMC_RAM)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_OFF)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_ERR)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_WRN)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_INF)、[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_DBG)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_DBG"></a>

## 371.76 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT"></a>

## 371.77 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_ERR"></a>

## 371.78 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_INF"></a>

## 371.79 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_OFF"></a>

## 371.80 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MEMC_RAMDISK_LOG_LEVEL_WRN"></a>

## 371.81 `CONFIG_MEMC_RAMDISK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk） → 存储器控制器 RAM 磁盘（memc_ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MEMC_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_CHOICE"></a>

## 371.82 `CONFIG_MFD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MFD
```

**默认值（Defaults）**

```text
CONFIG_MFD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MFD_LOG_LEVEL_OFF
CONFIG_MFD_LOG_LEVEL_ERR
CONFIG_MFD_LOG_LEVEL_WRN
CONFIG_MFD_LOG_LEVEL_INF
CONFIG_MFD_LOG_LEVEL_DBG
CONFIG_MFD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_MFD_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_DEFAULT)、[`CONFIG_MFD_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_OFF)、[`CONFIG_MFD_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_ERR)、[`CONFIG_MFD_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_WRN)、[`CONFIG_MFD_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_INF)、[`CONFIG_MFD_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_DBG)。

<a id="CONFIG_MFD_LOG_LEVEL_DBG"></a>

## 371.83 `CONFIG_MFD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_DEFAULT"></a>

## 371.84 `CONFIG_MFD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_ERR"></a>

## 371.85 `CONFIG_MFD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_INF"></a>

## 371.86 `CONFIG_MFD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_OFF"></a>

## 371.87 `CONFIG_MFD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MFD_LOG_LEVEL_WRN"></a>

## 371.88 `CONFIG_MFD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MFD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多功能设备（Multi-function Device，MFD）驱动 → 多功能设备（mfd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MFD_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MFD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE"></a>

## 371.89 `CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MIPI_DBI_LOG_LEVEL_OFF
CONFIG_MIPI_DBI_LOG_LEVEL_ERR
CONFIG_MIPI_DBI_LOG_LEVEL_WRN
CONFIG_MIPI_DBI_LOG_LEVEL_INF
CONFIG_MIPI_DBI_LOG_LEVEL_DBG
CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT)、[`CONFIG_MIPI_DBI_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_OFF)、[`CONFIG_MIPI_DBI_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_ERR)、[`CONFIG_MIPI_DBI_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_WRN)、[`CONFIG_MIPI_DBI_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_INF)、[`CONFIG_MIPI_DBI_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_DBG)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_DBG"></a>

## 371.90 `CONFIG_MIPI_DBI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT"></a>

## 371.91 `CONFIG_MIPI_DBI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_ERR"></a>

## 371.92 `CONFIG_MIPI_DBI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_INF"></a>

## 371.93 `CONFIG_MIPI_DBI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_OFF"></a>

## 371.94 `CONFIG_MIPI_DBI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DBI_LOG_LEVEL_WRN"></a>

## 371.95 `CONFIG_MIPI_DBI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI 显示总线接口（mipi_dbi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DBI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE"></a>

## 371.96 `CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MIPI_DSI_LOG_LEVEL_OFF
CONFIG_MIPI_DSI_LOG_LEVEL_ERR
CONFIG_MIPI_DSI_LOG_LEVEL_WRN
CONFIG_MIPI_DSI_LOG_LEVEL_INF
CONFIG_MIPI_DSI_LOG_LEVEL_DBG
CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)、[`CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT)、[`CONFIG_MIPI_DSI_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MIPI_DSI_LOG_LEVEL_OFF)、[`CONFIG_MIPI_DSI_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_ERR)、[`CONFIG_MIPI_DSI_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MIPI_DSI_LOG_LEVEL_WRN)、[`CONFIG_MIPI_DSI_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_INF)、[`CONFIG_MIPI_DSI_LOG_LEVEL_DBG`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_DBG)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_DBG"></a>

## 371.97 `CONFIG_MIPI_DSI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT"></a>

## 371.98 `CONFIG_MIPI_DSI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_ERR"></a>

## 371.99 `CONFIG_MIPI_DSI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_INF"></a>

## 371.100 `CONFIG_MIPI_DSI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P370_subsys_logging_配置项参考_19.md) · [返回大纲](大纲.md) · [下一章](P372_subsys_logging_配置项参考_21.md)
