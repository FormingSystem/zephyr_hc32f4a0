---
id: learning.zephyr-docs.kconfig-reference.page-362
title: "`subsys/logging`配置项参考（11/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第362章\_`subsys/logging`配置项参考（11/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE"></a>

## 362.1 `CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CPU_LOAD
```

**默认值（Defaults）**

```text
CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CPU_LOAD_LOG_LEVEL_OFF
CONFIG_CPU_LOAD_LOG_LEVEL_ERR
CONFIG_CPU_LOAD_LOG_LEVEL_WRN
CONFIG_CPU_LOAD_LOG_LEVEL_INF
CONFIG_CPU_LOAD_LOG_LEVEL_DBG
CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CPU_LOAD`](P197_lib_配置项参考_1.md#CONFIG_CPU_LOAD)、[`CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT)、[`CONFIG_CPU_LOAD_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_OFF)、[`CONFIG_CPU_LOAD_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_ERR)、[`CONFIG_CPU_LOAD_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_WRN)、[`CONFIG_CPU_LOAD_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_INF)、[`CONFIG_CPU_LOAD_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_DBG)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_DBG"></a>

## 362.2 `CONFIG_CPU_LOAD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT"></a>

## 362.3 `CONFIG_CPU_LOAD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_ERR"></a>

## 362.4 `CONFIG_CPU_LOAD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_INF"></a>

## 362.5 `CONFIG_CPU_LOAD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_OFF"></a>

## 362.6 `CONFIG_CPU_LOAD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_LOAD_LOG_LEVEL_WRN"></a>

## 362.7 `CONFIG_CPU_LOAD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → CPU 负载测量（CPU load measurement） → CPU 负载（cpu_load）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CPU_LOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE"></a>

## 362.8 `CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CRC_DRIVER_LOG_LEVEL_OFF
CONFIG_CRC_DRIVER_LOG_LEVEL_ERR
CONFIG_CRC_DRIVER_LOG_LEVEL_WRN
CONFIG_CRC_DRIVER_LOG_LEVEL_INF
CONFIG_CRC_DRIVER_LOG_LEVEL_DBG
CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_INF)、[`CONFIG_CRC_DRIVER_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_DBG"></a>

## 362.9 `CONFIG_CRC_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 362.10 `CONFIG_CRC_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_ERR"></a>

## 362.11 `CONFIG_CRC_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_INF"></a>

## 362.12 `CONFIG_CRC_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_OFF"></a>

## 362.13 `CONFIG_CRC_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_DRIVER_LOG_LEVEL_WRN"></a>

## 362.14 `CONFIG_CRC_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → 循环冗余校验驱动（CRC_DRIVER）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_CHOICE"></a>

## 362.15 `CONFIG_CRC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CRC
```

**默认值（Defaults）**

```text
CONFIG_CRC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CRC_LOG_LEVEL_OFF
CONFIG_CRC_LOG_LEVEL_ERR
CONFIG_CRC_LOG_LEVEL_WRN
CONFIG_CRC_LOG_LEVEL_INF
CONFIG_CRC_LOG_LEVEL_DBG
CONFIG_CRC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_CRC_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_DEFAULT)、[`CONFIG_CRC_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_OFF)、[`CONFIG_CRC_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_ERR)、[`CONFIG_CRC_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_WRN)、[`CONFIG_CRC_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_INF)、[`CONFIG_CRC_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_DBG)。

<a id="CONFIG_CRC_LOG_LEVEL_DBG"></a>

## 362.16 `CONFIG_CRC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_DEFAULT"></a>

## 362.17 `CONFIG_CRC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_ERR"></a>

## 362.18 `CONFIG_CRC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_INF"></a>

## 362.19 `CONFIG_CRC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_OFF"></a>

## 362.20 `CONFIG_CRC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRC_LOG_LEVEL_WRN"></a>

## 362.21 `CONFIG_CRC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support） → 循环冗余校验（CRC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_CHOICE"></a>

## 362.22 `CONFIG_CRYPTO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CRYPTO
```

**默认值（Defaults）**

```text
CONFIG_CRYPTO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CRYPTO_LOG_LEVEL_OFF
CONFIG_CRYPTO_LOG_LEVEL_ERR
CONFIG_CRYPTO_LOG_LEVEL_WRN
CONFIG_CRYPTO_LOG_LEVEL_INF
CONFIG_CRYPTO_LOG_LEVEL_DBG
CONFIG_CRYPTO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_CRYPTO_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_DEFAULT)、[`CONFIG_CRYPTO_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_OFF)、[`CONFIG_CRYPTO_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_ERR)、[`CONFIG_CRYPTO_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_WRN)、[`CONFIG_CRYPTO_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_INF)、[`CONFIG_CRYPTO_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_DBG)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_DBG"></a>

## 362.23 `CONFIG_CRYPTO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_DEFAULT"></a>

## 362.24 `CONFIG_CRYPTO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_ERR"></a>

## 362.25 `CONFIG_CRYPTO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_INF"></a>

## 362.26 `CONFIG_CRYPTO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_OFF"></a>

## 362.27 `CONFIG_CRYPTO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CRYPTO_LOG_LEVEL_WRN"></a>

## 362.28 `CONFIG_CRYPTO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 密码学驱动（Crypto Drivers） → 密码处理（CRYPTO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CRYPTO_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_CHOICE"></a>

## 362.29 `CONFIG_DAC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DAC
```

**默认值（Defaults）**

```text
CONFIG_DAC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DAC_LOG_LEVEL_OFF
CONFIG_DAC_LOG_LEVEL_ERR
CONFIG_DAC_LOG_LEVEL_WRN
CONFIG_DAC_LOG_LEVEL_INF
CONFIG_DAC_LOG_LEVEL_DBG
CONFIG_DAC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_DAC_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_DEFAULT)、[`CONFIG_DAC_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_OFF)、[`CONFIG_DAC_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_ERR)、[`CONFIG_DAC_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_WRN)、[`CONFIG_DAC_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_INF)、[`CONFIG_DAC_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_DBG)。

<a id="CONFIG_DAC_LOG_LEVEL_DBG"></a>

## 362.30 `CONFIG_DAC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_DEFAULT"></a>

## 362.31 `CONFIG_DAC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_ERR"></a>

## 362.32 `CONFIG_DAC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_INF"></a>

## 362.33 `CONFIG_DAC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_OFF"></a>

## 362.34 `CONFIG_DAC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAC_LOG_LEVEL_WRN"></a>

## 362.35 `CONFIG_DAC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数模转换器（Digital-to-Analog Converter，DAC）驱动 → 数模转换器（DAC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAC_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_CHOICE"></a>

## 362.36 `CONFIG_DAI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DAI
```

**默认值（Defaults）**

```text
CONFIG_DAI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DAI_LOG_LEVEL_OFF
CONFIG_DAI_LOG_LEVEL_ERR
CONFIG_DAI_LOG_LEVEL_WRN
CONFIG_DAI_LOG_LEVEL_INF
CONFIG_DAI_LOG_LEVEL_DBG
CONFIG_DAI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DAI`](P073_drivers_dai_配置项参考.md#CONFIG_DAI)、[`CONFIG_DAI_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_DEFAULT)、[`CONFIG_DAI_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_OFF)、[`CONFIG_DAI_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_ERR)、[`CONFIG_DAI_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_WRN)、[`CONFIG_DAI_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_INF)、[`CONFIG_DAI_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_DBG)。

<a id="CONFIG_DAI_LOG_LEVEL_DBG"></a>

## 362.37 `CONFIG_DAI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_DEFAULT"></a>

## 362.38 `CONFIG_DAI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_ERR"></a>

## 362.39 `CONFIG_DAI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_INF"></a>

## 362.40 `CONFIG_DAI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_OFF"></a>

## 362.41 `CONFIG_DAI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAI_LOG_LEVEL_WRN"></a>

## 362.42 `CONFIG_DAI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字音频接口（Digital Audio Interface，DAI）驱动 → 数字音频接口（dai）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAI_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE"></a>

## 362.43 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DALI
```

**默认值（Defaults）**

```text
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_OFF
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_ERR
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_WRN
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_INF
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DBG
CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DALI`](P074_drivers_dali_配置项参考.md#CONFIG_DALI)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_OFF)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_ERR)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_WRN)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_INF)、[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DBG)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DBG"></a>

## 362.44 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT"></a>

## 362.45 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_ERR"></a>

## 362.46 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_INF"></a>

## 362.47 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_OFF"></a>

## 362.48 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_WRN"></a>

## 362.49 `CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）驱动【实验性】 → 数字可寻址照明接口底层（dali_low_level）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DALI_LOW_LEVEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_CHOICE"></a>

## 362.50 `CONFIG_DAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DAP
```

**默认值（Defaults）**

```text
CONFIG_DAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DAP_LOG_LEVEL_OFF
CONFIG_DAP_LOG_LEVEL_ERR
CONFIG_DAP_LOG_LEVEL_WRN
CONFIG_DAP_LOG_LEVEL_INF
CONFIG_DAP_LOG_LEVEL_DBG
CONFIG_DAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)、[`CONFIG_DAP_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_DEFAULT)、[`CONFIG_DAP_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_OFF)、[`CONFIG_DAP_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_ERR)、[`CONFIG_DAP_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_WRN)、[`CONFIG_DAP_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_INF)、[`CONFIG_DAP_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_DBG)。

<a id="CONFIG_DAP_LOG_LEVEL_DBG"></a>

## 362.51 `CONFIG_DAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_DEFAULT"></a>

## 362.52 `CONFIG_DAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_ERR"></a>

## 362.53 `CONFIG_DAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_INF"></a>

## 362.54 `CONFIG_DAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_OFF"></a>

## 362.55 `CONFIG_DAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DAP_LOG_LEVEL_WRN"></a>

## 362.56 `CONFIG_DAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL] → 调试访问端口（dap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DAP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE"></a>

## 362.57 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DEBUG_COREDUMP
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_OFF
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_ERR
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_WRN
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_INF
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DBG
CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DEBUG_COREDUMP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_OFF)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_ERR)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_WRN)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_INF)、[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DBG)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DBG"></a>

## 362.58 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT"></a>

## 362.59 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_ERR"></a>

## 362.60 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_INF"></a>

## 362.61 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_OFF"></a>

## 362.62 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_COREDUMP_LOG_LEVEL_WRN"></a>

## 362.63 `CONFIG_DEBUG_COREDUMP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试选项（Debugging Options） → 核心转储（Core Dump） → 核心转储（coredump）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_COREDUMP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE"></a>

## 362.64 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DEBUG_CORESIGHT_NRF && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_OFF
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_ERR
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_WRN
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_INF
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DBG
CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_OFF)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_ERR)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_WRN)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_INF)、[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DBG)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DBG"></a>

## 362.65 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT"></a>

## 362.66 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_ERR"></a>

## 362.67 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_INF"></a>

## 362.68 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_OFF"></a>

## 362.69 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_WRN"></a>

## 362.70 `CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → CoreSight 跟踪（Trace）支持 → CoreSight 跟踪（CoreSight Trace）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_CORESIGHT_NRF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE"></a>

## 362.71 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DEBUG_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DEBUG_DRIVER_LOG_LEVEL_OFF
CONFIG_DEBUG_DRIVER_LOG_LEVEL_ERR
CONFIG_DEBUG_DRIVER_LOG_LEVEL_WRN
CONFIG_DEBUG_DRIVER_LOG_LEVEL_INF
CONFIG_DEBUG_DRIVER_LOG_LEVEL_DBG
CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DEBUG_DRIVER`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_DRIVER)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_INF)、[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_DBG"></a>

## 362.72 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 362.73 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_ERR"></a>

## 362.74 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_INF"></a>

## 362.75 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_OFF"></a>

## 362.76 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DEBUG_DRIVER_LOG_LEVEL_WRN"></a>

## 362.77 `CONFIG_DEBUG_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试驱动（Debug Drivers） → 调试驱动（debug_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DEBUG_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_CHOICE"></a>

## 362.78 `CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_FTL && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DISK_FTL_LOG_LEVEL_OFF
CONFIG_DISK_FTL_LOG_LEVEL_ERR
CONFIG_DISK_FTL_LOG_LEVEL_WRN
CONFIG_DISK_FTL_LOG_LEVEL_INF
CONFIG_DISK_FTL_LOG_LEVEL_DBG
CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT)、[`CONFIG_DISK_FTL_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_OFF)、[`CONFIG_DISK_FTL_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_ERR)、[`CONFIG_DISK_FTL_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_WRN)、[`CONFIG_DISK_FTL_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_INF)、[`CONFIG_DISK_FTL_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_DBG)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_DBG"></a>

## 362.79 `CONFIG_DISK_FTL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT"></a>

## 362.80 `CONFIG_DISK_FTL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_ERR"></a>

## 362.81 `CONFIG_DISK_FTL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_INF"></a>

## 362.82 `CONFIG_DISK_FTL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_OFF"></a>

## 362.83 `CONFIG_DISK_FTL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_FTL_LOG_LEVEL_WRN"></a>

## 362.84 `CONFIG_DISK_FTL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_FTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL） → 磁盘闪存转换层（disk_ftl）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_FTL_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_FTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_CHOICE"></a>

## 362.85 `CONFIG_DISK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_ACCESS
```

**默认值（Defaults）**

```text
CONFIG_DISK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DISK_LOG_LEVEL_OFF
CONFIG_DISK_LOG_LEVEL_ERR
CONFIG_DISK_LOG_LEVEL_WRN
CONFIG_DISK_LOG_LEVEL_INF
CONFIG_DISK_LOG_LEVEL_DBG
CONFIG_DISK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_ACCESS`](P340_subsys_disk_配置项参考.md#CONFIG_DISK_ACCESS)、[`CONFIG_DISK_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_DEFAULT)、[`CONFIG_DISK_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_OFF)、[`CONFIG_DISK_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_ERR)、[`CONFIG_DISK_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_WRN)、[`CONFIG_DISK_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_INF)、[`CONFIG_DISK_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_DBG)。

<a id="CONFIG_DISK_LOG_LEVEL_DBG"></a>

## 362.86 `CONFIG_DISK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_DEFAULT"></a>

## 362.87 `CONFIG_DISK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_ERR"></a>

## 362.88 `CONFIG_DISK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_INF"></a>

## 362.89 `CONFIG_DISK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_OFF"></a>

## 362.90 `CONFIG_DISK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_LOG_LEVEL_WRN"></a>

## 362.91 `CONFIG_DISK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 磁盘接口（Disk Interface） → 磁盘（disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE"></a>

## 362.92 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_VIRTIO_BLK && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_OFF
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_ERR
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_WRN
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_INF
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DBG
CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_VIRTIO_BLK)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_OFF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_OFF)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_ERR`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_ERR)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_WRN`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_WRN)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_INF`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_INF)、[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DBG)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DBG"></a>

## 362.93 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT"></a>

## 362.94 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_ERR"></a>

## 362.95 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_INF"></a>

## 362.96 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_OFF"></a>

## 362.97 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_WRN"></a>

## 362.98 `CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动 → VirtIO 块设备磁盘（disk_virtio_blk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISK_VIRTIO_BLK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_CHOICE"></a>

## 362.99 `CONFIG_DISPLAY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DISPLAY_LOG_LEVEL_OFF
CONFIG_DISPLAY_LOG_LEVEL_ERR
CONFIG_DISPLAY_LOG_LEVEL_WRN
CONFIG_DISPLAY_LOG_LEVEL_INF
CONFIG_DISPLAY_LOG_LEVEL_DBG
CONFIG_DISPLAY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_DISPLAY_LOG_LEVEL_DEFAULT)、[`CONFIG_DISPLAY_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DISPLAY_LOG_LEVEL_OFF)、[`CONFIG_DISPLAY_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_DISPLAY_LOG_LEVEL_ERR)、[`CONFIG_DISPLAY_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_DISPLAY_LOG_LEVEL_WRN)、[`CONFIG_DISPLAY_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DISPLAY_LOG_LEVEL_INF)、[`CONFIG_DISPLAY_LOG_LEVEL_DBG`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_DBG)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_DBG"></a>

## 362.100 `CONFIG_DISPLAY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P361_subsys_logging_配置项参考_10.md) · [返回大纲](大纲.md) · [下一章](P363_subsys_logging_配置项参考_12.md)
