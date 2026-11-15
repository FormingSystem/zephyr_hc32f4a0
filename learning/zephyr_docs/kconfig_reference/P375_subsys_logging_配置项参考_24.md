---
id: learning.zephyr-docs.kconfig-reference.page-375
title: "`subsys/logging`配置项参考（24/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第375章\_`subsys/logging`配置项参考（24/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_ERR"></a>

## 375.1 `CONFIG_PULSE_IO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_INF"></a>

## 375.2 `CONFIG_PULSE_IO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_OFF"></a>

## 375.3 `CONFIG_PULSE_IO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PULSE_IO_LOG_LEVEL_WRN"></a>

## 375.4 `CONFIG_PULSE_IO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PULSE_IO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → 脉冲输入输出（pulse_io）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_LOG_LEVEL_CHOICE`](P374_subsys_logging_配置项参考_23.md#CONFIG_PULSE_IO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_CHOICE"></a>

## 375.5 `CONFIG_PWM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_PWM
```

**默认值（Defaults）**

```text
CONFIG_PWM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PWM_LOG_LEVEL_OFF
CONFIG_PWM_LOG_LEVEL_ERR
CONFIG_PWM_LOG_LEVEL_WRN
CONFIG_PWM_LOG_LEVEL_INF
CONFIG_PWM_LOG_LEVEL_DBG
CONFIG_PWM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PWM_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_DEFAULT)、[`CONFIG_PWM_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_OFF)、[`CONFIG_PWM_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_ERR)、[`CONFIG_PWM_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_WRN)、[`CONFIG_PWM_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_INF)、[`CONFIG_PWM_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_DBG)。

<a id="CONFIG_PWM_LOG_LEVEL_DBG"></a>

## 375.6 `CONFIG_PWM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_DEFAULT"></a>

## 375.7 `CONFIG_PWM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_ERR"></a>

## 375.8 `CONFIG_PWM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_INF"></a>

## 375.9 `CONFIG_PWM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_OFF"></a>

## 375.10 `CONFIG_PWM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PWM_LOG_LEVEL_WRN"></a>

## 375.11 `CONFIG_PWM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PWM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 脉宽调制（pwm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_PWM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_PWM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_CHOICE"></a>

## 375.12 `CONFIG_RAMDISK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_RAM && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_RAMDISK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RAMDISK_LOG_LEVEL_OFF
CONFIG_RAMDISK_LOG_LEVEL_ERR
CONFIG_RAMDISK_LOG_LEVEL_WRN
CONFIG_RAMDISK_LOG_LEVEL_INF
CONFIG_RAMDISK_LOG_LEVEL_DBG
CONFIG_RAMDISK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_RAM`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_RAM)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_RAMDISK_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_DEFAULT)、[`CONFIG_RAMDISK_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_OFF)、[`CONFIG_RAMDISK_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_ERR)、[`CONFIG_RAMDISK_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_WRN)、[`CONFIG_RAMDISK_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_INF)、[`CONFIG_RAMDISK_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_DBG)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_DBG"></a>

## 375.13 `CONFIG_RAMDISK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_DEFAULT"></a>

## 375.14 `CONFIG_RAMDISK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_ERR"></a>

## 375.15 `CONFIG_RAMDISK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_INF"></a>

## 375.16 `CONFIG_RAMDISK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_OFF"></a>

## 375.17 `CONFIG_RAMDISK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RAMDISK_LOG_LEVEL_WRN"></a>

## 375.18 `CONFIG_RAMDISK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RAMDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk） → RAM 磁盘（ramdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RAMDISK_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RAMDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_CHOICE"></a>

## 375.19 `CONFIG_REGULATOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
CONFIG_REGULATOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_REGULATOR_LOG_LEVEL_OFF
CONFIG_REGULATOR_LOG_LEVEL_ERR
CONFIG_REGULATOR_LOG_LEVEL_WRN
CONFIG_REGULATOR_LOG_LEVEL_INF
CONFIG_REGULATOR_LOG_LEVEL_DBG
CONFIG_REGULATOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_REGULATOR_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_DEFAULT)、[`CONFIG_REGULATOR_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_OFF)、[`CONFIG_REGULATOR_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_ERR)、[`CONFIG_REGULATOR_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_WRN)、[`CONFIG_REGULATOR_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_INF)、[`CONFIG_REGULATOR_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_DBG)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_DBG"></a>

## 375.20 `CONFIG_REGULATOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_DEFAULT"></a>

## 375.21 `CONFIG_REGULATOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_ERR"></a>

## 375.22 `CONFIG_REGULATOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_INF"></a>

## 375.23 `CONFIG_REGULATOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_OFF"></a>

## 375.24 `CONFIG_REGULATOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_REGULATOR_LOG_LEVEL_WRN"></a>

## 375.25 `CONFIG_REGULATOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_REGULATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 稳压／稳流器（Regulator）驱动 → 稳压器（regulator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_REGULATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE"></a>

## 375.26 `CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_RETAINED_MEM
```

**默认值（Defaults）**

```text
CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RETAINED_MEM_LOG_LEVEL_OFF
CONFIG_RETAINED_MEM_LOG_LEVEL_ERR
CONFIG_RETAINED_MEM_LOG_LEVEL_WRN
CONFIG_RETAINED_MEM_LOG_LEVEL_INF
CONFIG_RETAINED_MEM_LOG_LEVEL_DBG
CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_OFF)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_ERR)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_WRN)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_INF)、[`CONFIG_RETAINED_MEM_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_DBG)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_DBG"></a>

## 375.27 `CONFIG_RETAINED_MEM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT"></a>

## 375.28 `CONFIG_RETAINED_MEM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_ERR"></a>

## 375.29 `CONFIG_RETAINED_MEM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_INF"></a>

## 375.30 `CONFIG_RETAINED_MEM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_OFF"></a>

## 375.31 `CONFIG_RETAINED_MEM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETAINED_MEM_LOG_LEVEL_WRN"></a>

## 375.32 `CONFIG_RETAINED_MEM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 保留内存（Retained Memory）驱动 → 保留内存（retained_mem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETAINED_MEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_CHOICE"></a>

## 375.33 `CONFIG_RETENTION_LOG_LEVEL_CHOICE`

**提示（Prompt）**：保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_RETENTION
```

**默认值（Defaults）**

```text
CONFIG_RETENTION_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RETENTION_LOG_LEVEL_OFF
CONFIG_RETENTION_LOG_LEVEL_ERR
CONFIG_RETENTION_LOG_LEVEL_WRN
CONFIG_RETENTION_LOG_LEVEL_INF
CONFIG_RETENTION_LOG_LEVEL_DBG
CONFIG_RETENTION_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION)、[`CONFIG_RETENTION_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_DEFAULT)、[`CONFIG_RETENTION_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_OFF)、[`CONFIG_RETENTION_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_ERR)、[`CONFIG_RETENTION_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_WRN)、[`CONFIG_RETENTION_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_INF)、[`CONFIG_RETENTION_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_DBG)。

<a id="CONFIG_RETENTION_LOG_LEVEL_DBG"></a>

## 375.34 `CONFIG_RETENTION_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_DEFAULT"></a>

## 375.35 `CONFIG_RETENTION_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_ERR"></a>

## 375.36 `CONFIG_RETENTION_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_INF"></a>

## 375.37 `CONFIG_RETENTION_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_OFF"></a>

## 375.38 `CONFIG_RETENTION_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RETENTION_LOG_LEVEL_WRN"></a>

## 375.39 `CONFIG_RETENTION_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RETENTION_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 保留存储支持（Retention support） → 保留存储（retention）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RETENTION_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE"></a>

## 375.40 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_RPMSG_SERVICE
```

**默认值（Defaults）**

```text
CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RPMSG_SERVICE_LOG_LEVEL_OFF
CONFIG_RPMSG_SERVICE_LOG_LEVEL_ERR
CONFIG_RPMSG_SERVICE_LOG_LEVEL_WRN
CONFIG_RPMSG_SERVICE_LOG_LEVEL_INF
CONFIG_RPMSG_SERVICE_LOG_LEVEL_DBG
CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_OFF)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_ERR)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_WRN)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_INF)、[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_DBG"></a>

## 375.41 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT"></a>

## 375.42 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_ERR"></a>

## 375.43 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_INF"></a>

## 375.44 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_OFF"></a>

## 375.45 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RPMSG_SERVICE_LOG_LEVEL_WRN"></a>

## 375.46 `CONFIG_RPMSG_SERVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务及后端（RPMsg service and backend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RPMSG_SERVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_CHOICE"></a>

## 375.47 `CONFIG_RTC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_RTC
```

**默认值（Defaults）**

```text
CONFIG_RTC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RTC_LOG_LEVEL_OFF
CONFIG_RTC_LOG_LEVEL_ERR
CONFIG_RTC_LOG_LEVEL_WRN
CONFIG_RTC_LOG_LEVEL_INF
CONFIG_RTC_LOG_LEVEL_DBG
CONFIG_RTC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_RTC_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_DEFAULT)、[`CONFIG_RTC_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_OFF)、[`CONFIG_RTC_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_ERR)、[`CONFIG_RTC_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_WRN)、[`CONFIG_RTC_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_INF)、[`CONFIG_RTC_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_DBG)。

<a id="CONFIG_RTC_LOG_LEVEL_DBG"></a>

## 375.48 `CONFIG_RTC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_DEFAULT"></a>

## 375.49 `CONFIG_RTC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_ERR"></a>

## 375.50 `CONFIG_RTC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_INF"></a>

## 375.51 `CONFIG_RTC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_OFF"></a>

## 375.52 `CONFIG_RTC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTC_LOG_LEVEL_WRN"></a>

## 375.53 `CONFIG_RTC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 实时时钟（rtc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_CHOICE"></a>

## 375.54 `CONFIG_RTIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_RTIO
```

**默认值（Defaults）**

```text
CONFIG_RTIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RTIO_LOG_LEVEL_OFF
CONFIG_RTIO_LOG_LEVEL_ERR
CONFIG_RTIO_LOG_LEVEL_WRN
CONFIG_RTIO_LOG_LEVEL_INF
CONFIG_RTIO_LOG_LEVEL_DBG
CONFIG_RTIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_DEFAULT)、[`CONFIG_RTIO_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_OFF)、[`CONFIG_RTIO_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_ERR)、[`CONFIG_RTIO_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_WRN)、[`CONFIG_RTIO_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_INF)、[`CONFIG_RTIO_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_DBG)。

<a id="CONFIG_RTIO_LOG_LEVEL_DBG"></a>

## 375.55 `CONFIG_RTIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_DEFAULT"></a>

## 375.56 `CONFIG_RTIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_ERR"></a>

## 375.57 `CONFIG_RTIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_INF"></a>

## 375.58 `CONFIG_RTIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_OFF"></a>

## 375.59 `CONFIG_RTIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTIO_LOG_LEVEL_WRN"></a>

## 375.60 `CONFIG_RTIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 实时输入输出（Real-Time I/O，RTIO）。 → 实时输入输出（RTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_RTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_CHOICE"></a>

## 375.61 `CONFIG_SDHC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SDHC
```

**默认值（Defaults）**

```text
CONFIG_SDHC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SDHC_LOG_LEVEL_OFF
CONFIG_SDHC_LOG_LEVEL_ERR
CONFIG_SDHC_LOG_LEVEL_WRN
CONFIG_SDHC_LOG_LEVEL_INF
CONFIG_SDHC_LOG_LEVEL_DBG
CONFIG_SDHC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_DEFAULT)、[`CONFIG_SDHC_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_OFF)、[`CONFIG_SDHC_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_ERR)、[`CONFIG_SDHC_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_WRN)、[`CONFIG_SDHC_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_INF)、[`CONFIG_SDHC_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_DBG)。

<a id="CONFIG_SDHC_LOG_LEVEL_DBG"></a>

## 375.62 `CONFIG_SDHC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_DEFAULT"></a>

## 375.63 `CONFIG_SDHC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_ERR"></a>

## 375.64 `CONFIG_SDHC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_INF"></a>

## 375.65 `CONFIG_SDHC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_OFF"></a>

## 375.66 `CONFIG_SDHC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDHC_LOG_LEVEL_WRN"></a>

## 375.67 `CONFIG_SDHC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDHC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → SD 主机控制器（sdhc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDHC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_CHOICE"></a>

## 375.68 `CONFIG_SDMMC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_SDMMC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SDMMC_LOG_LEVEL_OFF
CONFIG_SDMMC_LOG_LEVEL_ERR
CONFIG_SDMMC_LOG_LEVEL_WRN
CONFIG_SDMMC_LOG_LEVEL_INF
CONFIG_SDMMC_LOG_LEVEL_DBG
CONFIG_SDMMC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_SDMMC_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_DEFAULT)、[`CONFIG_SDMMC_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_OFF)、[`CONFIG_SDMMC_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_ERR)、[`CONFIG_SDMMC_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_WRN)、[`CONFIG_SDMMC_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_INF)、[`CONFIG_SDMMC_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_DBG)。

<a id="CONFIG_SDMMC_LOG_LEVEL_DBG"></a>

## 375.69 `CONFIG_SDMMC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_DEFAULT"></a>

## 375.70 `CONFIG_SDMMC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_ERR"></a>

## 375.71 `CONFIG_SDMMC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_INF"></a>

## 375.72 `CONFIG_SDMMC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_OFF"></a>

## 375.73 `CONFIG_SDMMC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SDMMC_LOG_LEVEL_WRN"></a>

## 375.74 `CONFIG_SDMMC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SDMMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → SD/MMC 存储卡（sdmmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SDMMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_CHOICE"></a>

## 375.75 `CONFIG_SD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
CONFIG_SD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SD_LOG_LEVEL_OFF
CONFIG_SD_LOG_LEVEL_ERR
CONFIG_SD_LOG_LEVEL_WRN
CONFIG_SD_LOG_LEVEL_INF
CONFIG_SD_LOG_LEVEL_DBG
CONFIG_SD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SD_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SD_STACK)、[`CONFIG_SD_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_DEFAULT)、[`CONFIG_SD_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_OFF)、[`CONFIG_SD_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_ERR)、[`CONFIG_SD_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_WRN)、[`CONFIG_SD_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_INF)、[`CONFIG_SD_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_DBG)。

<a id="CONFIG_SD_LOG_LEVEL_DBG"></a>

## 375.76 `CONFIG_SD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_DEFAULT"></a>

## 375.77 `CONFIG_SD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_ERR"></a>

## 375.78 `CONFIG_SD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_INF"></a>

## 375.79 `CONFIG_SD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_OFF"></a>

## 375.80 `CONFIG_SD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SD_LOG_LEVEL_WRN"></a>

## 375.81 `CONFIG_SD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD） → SD 协议栈（SD stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SD_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE"></a>

## 375.82 `CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SECURE_STORAGE
```

**默认值（Defaults）**

```text
CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SECURE_STORAGE_LOG_LEVEL_OFF
CONFIG_SECURE_STORAGE_LOG_LEVEL_ERR
CONFIG_SECURE_STORAGE_LOG_LEVEL_WRN
CONFIG_SECURE_STORAGE_LOG_LEVEL_INF
CONFIG_SECURE_STORAGE_LOG_LEVEL_DBG
CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SECURE_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_OFF)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_ERR)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_WRN)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_INF)、[`CONFIG_SECURE_STORAGE_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_DBG)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_DBG"></a>

## 375.83 `CONFIG_SECURE_STORAGE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT"></a>

## 375.84 `CONFIG_SECURE_STORAGE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_ERR"></a>

## 375.85 `CONFIG_SECURE_STORAGE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_INF"></a>

## 375.86 `CONFIG_SECURE_STORAGE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_OFF"></a>

## 375.87 `CONFIG_SECURE_STORAGE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SECURE_STORAGE_LOG_LEVEL_WRN"></a>

## 375.88 `CONFIG_SECURE_STORAGE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全存储子系统（Secure storage subsystem） → 安全存储（secure_storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SECURE_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_CHOICE"></a>

## 375.89 `CONFIG_SENSING_LOG_LEVEL_CHOICE`

**提示（Prompt）**：感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SENSING
```

**默认值（Defaults）**

```text
CONFIG_SENSING_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SENSING_LOG_LEVEL_OFF
CONFIG_SENSING_LOG_LEVEL_ERR
CONFIG_SENSING_LOG_LEVEL_WRN
CONFIG_SENSING_LOG_LEVEL_INF
CONFIG_SENSING_LOG_LEVEL_DBG
CONFIG_SENSING_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SENSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSING)、[`CONFIG_SENSING_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_DEFAULT)、[`CONFIG_SENSING_LOG_LEVEL_OFF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_OFF)、[`CONFIG_SENSING_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_ERR)、[`CONFIG_SENSING_LOG_LEVEL_WRN`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_WRN)、[`CONFIG_SENSING_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_INF)、[`CONFIG_SENSING_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_DBG)。

<a id="CONFIG_SENSING_LOG_LEVEL_DBG"></a>

## 375.90 `CONFIG_SENSING_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_DEFAULT"></a>

## 375.91 `CONFIG_SENSING_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_ERR"></a>

## 375.92 `CONFIG_SENSING_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_INF"></a>

## 375.93 `CONFIG_SENSING_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_OFF"></a>

## 375.94 `CONFIG_SENSING_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSING_LOG_LEVEL_WRN"></a>

## 375.95 `CONFIG_SENSING_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSING_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem） → 感知（sensing）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSING_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSING_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSOR_LOG_LEVEL_CHOICE"></a>

## 375.96 `CONFIG_SENSOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SENSOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SENSOR_LOG_LEVEL_OFF
CONFIG_SENSOR_LOG_LEVEL_ERR
CONFIG_SENSOR_LOG_LEVEL_WRN
CONFIG_SENSOR_LOG_LEVEL_INF
CONFIG_SENSOR_LOG_LEVEL_DBG
CONFIG_SENSOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SENSOR_LOG_LEVEL_DEFAULT`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_DEFAULT)、[`CONFIG_SENSOR_LOG_LEVEL_OFF`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENSOR_LOG_LEVEL_OFF)、[`CONFIG_SENSOR_LOG_LEVEL_ERR`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_ERR)、[`CONFIG_SENSOR_LOG_LEVEL_WRN`](P376_subsys_logging_配置项参考_25.md#CONFIG_SENSOR_LOG_LEVEL_WRN)、[`CONFIG_SENSOR_LOG_LEVEL_INF`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_INF)、[`CONFIG_SENSOR_LOG_LEVEL_DBG`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_DBG)。

<a id="CONFIG_SENSOR_LOG_LEVEL_DBG"></a>

## 375.97 `CONFIG_SENSOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSOR_LOG_LEVEL_DEFAULT"></a>

## 375.98 `CONFIG_SENSOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSOR_LOG_LEVEL_ERR"></a>

## 375.99 `CONFIG_SENSOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SENSOR_LOG_LEVEL_INF"></a>

## 375.100 `CONFIG_SENSOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SENSOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器（sensor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_LOG_LEVEL_CHOICE`](P375_subsys_logging_配置项参考_24.md#CONFIG_SENSOR_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P374_subsys_logging_配置项参考_23.md) · [返回大纲](大纲.md) · [下一章](P376_subsys_logging_配置项参考_25.md)
