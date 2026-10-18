---
id: learning.zephyr-docs.kconfig-reference.page-373
title: "`subsys/logging`配置项参考（22/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第373章\_`subsys/logging`配置项参考（22/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_BUF_LOG_LEVEL_WRN"></a>

## 373.1 `CONFIG_NET_BUF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE"></a>

## 373.2 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NORDIC_VPR_LAUNCHER
```

**默认值（Defaults）**

```text
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_OFF
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_ERR
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_WRN
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_INF
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DBG
CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NORDIC_VPR_LAUNCHER`](P123_drivers_misc_配置项参考.md#CONFIG_NORDIC_VPR_LAUNCHER)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_OFF)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_ERR)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_WRN)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_INF)、[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DBG)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DBG"></a>

## 373.3 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT"></a>

## 373.4 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_ERR"></a>

## 373.5 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_INF"></a>

## 373.6 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_OFF"></a>

## 373.7 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_WRN"></a>

## 373.8 `CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher） → Nordic VPR 启动器（Nordic VPR Launcher）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NORDIC_VPR_LAUNCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE"></a>

## 373.9 `CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`

**提示（Prompt）**：NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF
CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR
CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN
CONFIG_NRFS_BACKEND_LOG_LEVEL_INF
CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG
CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT
CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF
CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR
CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN
CONFIG_NRFS_BACKEND_LOG_LEVEL_INF
CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG
CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_INF)、[`CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG"></a>

## 373.10 `CONFIG_NRFS_BACKEND_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT"></a>

## 373.11 `CONFIG_NRFS_BACKEND_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR"></a>

## 373.12 `CONFIG_NRFS_BACKEND_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_INF"></a>

## 373.13 `CONFIG_NRFS_BACKEND_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF"></a>

## 373.14 `CONFIG_NRFS_BACKEND_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN"></a>

## 373.15 `CONFIG_NRFS_BACKEND_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings） → NRFS 后端（NRFS backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_BACKEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_CHOICE"></a>

## 373.16 `CONFIG_NRFS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
CONFIG_NRFS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NRFS_LOG_LEVEL_OFF
CONFIG_NRFS_LOG_LEVEL_ERR
CONFIG_NRFS_LOG_LEVEL_WRN
CONFIG_NRFS_LOG_LEVEL_INF
CONFIG_NRFS_LOG_LEVEL_DBG
CONFIG_NRFS_LOG_LEVEL_DEFAULT
CONFIG_NRFS_LOG_LEVEL_OFF
CONFIG_NRFS_LOG_LEVEL_ERR
CONFIG_NRFS_LOG_LEVEL_WRN
CONFIG_NRFS_LOG_LEVEL_INF
CONFIG_NRFS_LOG_LEVEL_DBG
CONFIG_NRFS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_NRFS_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_DEFAULT)、[`CONFIG_NRFS_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_OFF)、[`CONFIG_NRFS_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_ERR)、[`CONFIG_NRFS_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_WRN)、[`CONFIG_NRFS_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_INF)、[`CONFIG_NRFS_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOG_LEVEL_DBG"></a>

## 373.17 `CONFIG_NRFS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_DEFAULT"></a>

## 373.18 `CONFIG_NRFS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_ERR"></a>

## 373.19 `CONFIG_NRFS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_INF"></a>

## 373.20 `CONFIG_NRFS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_OFF"></a>

## 373.21 `CONFIG_NRFS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRFS_LOG_LEVEL_WRN"></a>

## 373.22 `CONFIG_NRFS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services） → nRF 服务（nRF-Services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE"></a>

## 373.23 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRF_USBD_COMMON
```

**默认值（Defaults）**

```text
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_OFF
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_ERR
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_WRN
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_INF
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DBG
CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRF_USBD_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBD_COMMON)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_OFF)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_ERR)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_WRN)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_INF)、[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DBG)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DBG"></a>

## 373.24 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT"></a>

## 373.25 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_ERR"></a>

## 373.26 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_INF"></a>

## 373.27 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_OFF"></a>

## 373.28 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NRF_USBD_COMMON_LOG_LEVEL_WRN"></a>

## 373.29 `CONFIG_NRF_USBD_COMMON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动 → nRF USB 设备公共部分（nRF USBD common）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NRF_USBD_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_CHOICE"></a>

## 373.30 `CONFIG_NVMEM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NVMEM
```

**默认值（Defaults）**

```text
CONFIG_NVMEM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NVMEM_LOG_LEVEL_OFF
CONFIG_NVMEM_LOG_LEVEL_ERR
CONFIG_NVMEM_LOG_LEVEL_WRN
CONFIG_NVMEM_LOG_LEVEL_INF
CONFIG_NVMEM_LOG_LEVEL_DBG
CONFIG_NVMEM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_NVMEM_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_DEFAULT)、[`CONFIG_NVMEM_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_OFF)、[`CONFIG_NVMEM_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_ERR)、[`CONFIG_NVMEM_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_WRN)、[`CONFIG_NVMEM_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_INF)、[`CONFIG_NVMEM_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_DBG)。

<a id="CONFIG_NVMEM_LOG_LEVEL_DBG"></a>

## 373.31 `CONFIG_NVMEM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_DEFAULT"></a>

## 373.32 `CONFIG_NVMEM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_ERR"></a>

## 373.33 `CONFIG_NVMEM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_INF"></a>

## 373.34 `CONFIG_NVMEM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_OFF"></a>

## 373.35 `CONFIG_NVMEM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVMEM_LOG_LEVEL_WRN"></a>

## 373.36 `CONFIG_NVMEM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVMEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 非易失性存储器（Non Volatile Memory，NVMEM） → 非易失性存储器（nvmem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVMEM_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVMEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_CHOICE"></a>

## 373.37 `CONFIG_NVME_LOG_LEVEL_CHOICE`

**提示（Prompt）**：NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NVME_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NVME_LOG_LEVEL_OFF
CONFIG_NVME_LOG_LEVEL_ERR
CONFIG_NVME_LOG_LEVEL_WRN
CONFIG_NVME_LOG_LEVEL_INF
CONFIG_NVME_LOG_LEVEL_DBG
CONFIG_NVME_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_NVME_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_DEFAULT)、[`CONFIG_NVME_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_OFF)、[`CONFIG_NVME_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_ERR)、[`CONFIG_NVME_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_WRN)、[`CONFIG_NVME_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_INF)、[`CONFIG_NVME_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_DBG)。

<a id="CONFIG_NVME_LOG_LEVEL_DBG"></a>

## 373.38 `CONFIG_NVME_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_DEFAULT"></a>

## 373.39 `CONFIG_NVME_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_ERR"></a>

## 373.40 `CONFIG_NVME_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_INF"></a>

## 373.41 `CONFIG_NVME_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_OFF"></a>

## 373.42 `CONFIG_NVME_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVME_LOG_LEVEL_WRN"></a>

## 373.43 `CONFIG_NVME_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk） → NVMe 存储（nvme）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVME_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_CHOICE"></a>

## 373.44 `CONFIG_NVS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NVS
```

**默认值（Defaults）**

```text
CONFIG_NVS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NVS_LOG_LEVEL_OFF
CONFIG_NVS_LOG_LEVEL_ERR
CONFIG_NVS_LOG_LEVEL_WRN
CONFIG_NVS_LOG_LEVEL_INF
CONFIG_NVS_LOG_LEVEL_DBG
CONFIG_NVS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)、[`CONFIG_NVS_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_DEFAULT)、[`CONFIG_NVS_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_OFF)、[`CONFIG_NVS_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_ERR)、[`CONFIG_NVS_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_WRN)、[`CONFIG_NVS_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_INF)、[`CONFIG_NVS_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_DBG)。

<a id="CONFIG_NVS_LOG_LEVEL_DBG"></a>

## 373.45 `CONFIG_NVS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_DEFAULT"></a>

## 373.46 `CONFIG_NVS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_ERR"></a>

## 373.47 `CONFIG_NVS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_INF"></a>

## 373.48 `CONFIG_NVS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_OFF"></a>

## 373.49 `CONFIG_NVS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NVS_LOG_LEVEL_WRN"></a>

## 373.50 `CONFIG_NVS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NVS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储（nvs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NVS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE"></a>

## 373.51 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NXP_S32_EMIOS
```

**默认值（Defaults）**

```text
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_OFF
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_ERR
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_WRN
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_INF
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DBG
CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NXP_S32_EMIOS`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_S32_EMIOS)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_OFF)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_ERR)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_WRN)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_INF)、[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DBG)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DBG"></a>

## 373.52 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT"></a>

## 373.53 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_ERR"></a>

## 373.54 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_INF"></a>

## 373.55 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_OFF"></a>

## 373.56 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NXP_S32_EMIOS_LOG_LEVEL_WRN"></a>

## 373.57 `CONFIG_NXP_S32_EMIOS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动 → NXP S32 增强型模块化输入输出系统（NXP S32 eMIOS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_NXP_S32_EMIOS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_CHOICE"></a>

## 373.58 `CONFIG_OPAMP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
CONFIG_OPAMP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_OPAMP_LOG_LEVEL_OFF
CONFIG_OPAMP_LOG_LEVEL_ERR
CONFIG_OPAMP_LOG_LEVEL_WRN
CONFIG_OPAMP_LOG_LEVEL_INF
CONFIG_OPAMP_LOG_LEVEL_DBG
CONFIG_OPAMP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_OPAMP_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_DEFAULT)、[`CONFIG_OPAMP_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_OFF)、[`CONFIG_OPAMP_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_ERR)、[`CONFIG_OPAMP_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_WRN)、[`CONFIG_OPAMP_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_INF)、[`CONFIG_OPAMP_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_DBG)。

<a id="CONFIG_OPAMP_LOG_LEVEL_DBG"></a>

## 373.59 `CONFIG_OPAMP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_DEFAULT"></a>

## 373.60 `CONFIG_OPAMP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_ERR"></a>

## 373.61 `CONFIG_OPAMP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_INF"></a>

## 373.62 `CONFIG_OPAMP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_OFF"></a>

## 373.63 `CONFIG_OPAMP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPAMP_LOG_LEVEL_WRN"></a>

## 373.64 `CONFIG_OPAMP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPAMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → 运算放大器（opamp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OPAMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_CHOICE"></a>

## 373.65 `CONFIG_OTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_OTP
```

**默认值（Defaults）**

```text
CONFIG_OTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_OTP_LOG_LEVEL_OFF
CONFIG_OTP_LOG_LEVEL_ERR
CONFIG_OTP_LOG_LEVEL_WRN
CONFIG_OTP_LOG_LEVEL_INF
CONFIG_OTP_LOG_LEVEL_DBG
CONFIG_OTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_OTP_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_DEFAULT)、[`CONFIG_OTP_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_OFF)、[`CONFIG_OTP_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_ERR)、[`CONFIG_OTP_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_WRN)、[`CONFIG_OTP_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_INF)、[`CONFIG_OTP_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_DBG)。

<a id="CONFIG_OTP_LOG_LEVEL_DBG"></a>

## 373.66 `CONFIG_OTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_DEFAULT"></a>

## 373.67 `CONFIG_OTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_ERR"></a>

## 373.68 `CONFIG_OTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_INF"></a>

## 373.69 `CONFIG_OTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_OFF"></a>

## 373.70 `CONFIG_OTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OTP_LOG_LEVEL_WRN"></a>

## 373.71 `CONFIG_OTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → 一次性可编程存储器（otp）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_OTP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_OTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_CHOICE"></a>

## 373.72 `CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PCIE_ENDPOINT
```

**默认值（Defaults）**

```text
CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PCIE_EP_LOG_LEVEL_OFF
CONFIG_PCIE_EP_LOG_LEVEL_ERR
CONFIG_PCIE_EP_LOG_LEVEL_WRN
CONFIG_PCIE_EP_LOG_LEVEL_INF
CONFIG_PCIE_EP_LOG_LEVEL_DBG
CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PCIE_ENDPOINT`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_ENDPOINT)、[`CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT)、[`CONFIG_PCIE_EP_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_OFF)、[`CONFIG_PCIE_EP_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_ERR)、[`CONFIG_PCIE_EP_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_WRN)、[`CONFIG_PCIE_EP_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_INF)、[`CONFIG_PCIE_EP_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_DBG)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_DBG"></a>

## 373.73 `CONFIG_PCIE_EP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT"></a>

## 373.74 `CONFIG_PCIE_EP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_ERR"></a>

## 373.75 `CONFIG_PCIE_EP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_INF"></a>

## 373.76 `CONFIG_PCIE_EP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_OFF"></a>

## 373.77 `CONFIG_PCIE_EP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_EP_LOG_LEVEL_WRN"></a>

## 373.78 `CONFIG_PCIE_EP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_EP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → PCIe 端点（PCIE_EP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_EP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_CHOICE"></a>

## 373.79 `CONFIG_PCIE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PCIE
```

**默认值（Defaults）**

```text
CONFIG_PCIE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PCIE_LOG_LEVEL_OFF
CONFIG_PCIE_LOG_LEVEL_ERR
CONFIG_PCIE_LOG_LEVEL_WRN
CONFIG_PCIE_LOG_LEVEL_INF
CONFIG_PCIE_LOG_LEVEL_DBG
CONFIG_PCIE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_PCIE_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_DEFAULT)、[`CONFIG_PCIE_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_OFF)、[`CONFIG_PCIE_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_ERR)、[`CONFIG_PCIE_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_WRN)、[`CONFIG_PCIE_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_INF)、[`CONFIG_PCIE_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_DBG)。

<a id="CONFIG_PCIE_LOG_LEVEL_DBG"></a>

## 373.80 `CONFIG_PCIE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_DEFAULT"></a>

## 373.81 `CONFIG_PCIE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_ERR"></a>

## 373.82 `CONFIG_PCIE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_INF"></a>

## 373.83 `CONFIG_PCIE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_OFF"></a>

## 373.84 `CONFIG_PCIE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PCIE_LOG_LEVEL_WRN"></a>

## 373.85 `CONFIG_PCIE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PCIE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI Express 总线（pcie）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PCIE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_CHOICE"></a>

## 373.86 `CONFIG_PECI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PECI
```

**默认值（Defaults）**

```text
CONFIG_PECI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PECI_LOG_LEVEL_OFF
CONFIG_PECI_LOG_LEVEL_ERR
CONFIG_PECI_LOG_LEVEL_WRN
CONFIG_PECI_LOG_LEVEL_INF
CONFIG_PECI_LOG_LEVEL_DBG
CONFIG_PECI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PECI`](P135_drivers_peci_配置项参考.md#CONFIG_PECI)、[`CONFIG_PECI_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_DEFAULT)、[`CONFIG_PECI_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_OFF)、[`CONFIG_PECI_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_ERR)、[`CONFIG_PECI_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_WRN)、[`CONFIG_PECI_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_INF)、[`CONFIG_PECI_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_DBG)。

<a id="CONFIG_PECI_LOG_LEVEL_DBG"></a>

## 373.87 `CONFIG_PECI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_DEFAULT"></a>

## 373.88 `CONFIG_PECI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_ERR"></a>

## 373.89 `CONFIG_PECI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_INF"></a>

## 373.90 `CONFIG_PECI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_OFF"></a>

## 373.91 `CONFIG_PECI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PECI_LOG_LEVEL_WRN"></a>

## 373.92 `CONFIG_PECI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PECI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 平台环境控制接口（Platform Environment Control Interface，PECI）驱动 → 平台环境控制接口（peci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PECI_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PECI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_CHOICE"></a>

## 373.93 `CONFIG_PINCTRL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PINCTRL
```

**默认值（Defaults）**

```text
CONFIG_PINCTRL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PINCTRL_LOG_LEVEL_OFF
CONFIG_PINCTRL_LOG_LEVEL_ERR
CONFIG_PINCTRL_LOG_LEVEL_WRN
CONFIG_PINCTRL_LOG_LEVEL_INF
CONFIG_PINCTRL_LOG_LEVEL_DBG
CONFIG_PINCTRL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_PINCTRL_LOG_LEVEL_DEFAULT`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_DEFAULT)、[`CONFIG_PINCTRL_LOG_LEVEL_OFF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_OFF)、[`CONFIG_PINCTRL_LOG_LEVEL_ERR`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_ERR)、[`CONFIG_PINCTRL_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_WRN)、[`CONFIG_PINCTRL_LOG_LEVEL_INF`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_INF)、[`CONFIG_PINCTRL_LOG_LEVEL_DBG`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_DBG)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_DBG"></a>

## 373.94 `CONFIG_PINCTRL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_DEFAULT"></a>

## 373.95 `CONFIG_PINCTRL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_ERR"></a>

## 373.96 `CONFIG_PINCTRL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_INF"></a>

## 373.97 `CONFIG_PINCTRL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_OFF"></a>

## 373.98 `CONFIG_PINCTRL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PINCTRL_LOG_LEVEL_WRN"></a>

## 373.99 `CONFIG_PINCTRL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PINCTRL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 引脚控制器驱动（Pin Controller Drivers） → 引脚控制（PINCTRL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PINCTRL_LOG_LEVEL_CHOICE`](P373_subsys_logging_配置项参考_22.md#CONFIG_PINCTRL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE"></a>

## 373.100 `CONFIG_PM_CPU_OPS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电源管理 CPU 操作（pm_cpu_ops）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PM_CPU_OPS
```

**默认值（Defaults）**

```text
CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PM_CPU_OPS_LOG_LEVEL_OFF
CONFIG_PM_CPU_OPS_LOG_LEVEL_ERR
CONFIG_PM_CPU_OPS_LOG_LEVEL_WRN
CONFIG_PM_CPU_OPS_LOG_LEVEL_INF
CONFIG_PM_CPU_OPS_LOG_LEVEL_DBG
CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PM_CPU_OPS`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_DEFAULT)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_OFF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_OFF)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_ERR`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_ERR)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_WRN`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_WRN)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_INF`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_INF)、[`CONFIG_PM_CPU_OPS_LOG_LEVEL_DBG`](P374_subsys_logging_配置项参考_23.md#CONFIG_PM_CPU_OPS_LOG_LEVEL_DBG)。

<!-- kconfig-navigation -->

[上一章](P372_subsys_logging_配置项参考_21.md) · [返回大纲](大纲.md) · [下一章](P374_subsys_logging_配置项参考_23.md)
