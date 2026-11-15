---
id: learning.zephyr-docs.kconfig-reference.page-361
title: "`subsys/logging`配置项参考（10/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第361章\_`subsys/logging`配置项参考（10/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_OFF"></a>

## 361.1 `CONFIG_BT_VOCS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_VOCS_LOG_LEVEL_WRN"></a>

## 361.2 `CONFIG_BT_VOCS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_VOCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 音量偏移控制服务（Volume Offset Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_VOCS_LOG_LEVEL_CHOICE`](P360_subsys_logging_配置项参考_9.md#CONFIG_BT_VOCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_CHOICE"></a>

## 361.3 `CONFIG_BUZZER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BUZZER
```

**默认值（Defaults）**

```text
CONFIG_BUZZER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BUZZER_LOG_LEVEL_OFF
CONFIG_BUZZER_LOG_LEVEL_ERR
CONFIG_BUZZER_LOG_LEVEL_WRN
CONFIG_BUZZER_LOG_LEVEL_INF
CONFIG_BUZZER_LOG_LEVEL_DBG
CONFIG_BUZZER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BUZZER`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER)、[`CONFIG_BUZZER_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_DEFAULT)、[`CONFIG_BUZZER_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_OFF)、[`CONFIG_BUZZER_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_ERR)、[`CONFIG_BUZZER_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_WRN)、[`CONFIG_BUZZER_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_INF)、[`CONFIG_BUZZER_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_DBG)。

<a id="CONFIG_BUZZER_LOG_LEVEL_DBG"></a>

## 361.4 `CONFIG_BUZZER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_DEFAULT"></a>

## 361.5 `CONFIG_BUZZER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_ERR"></a>

## 361.6 `CONFIG_BUZZER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_INF"></a>

## 361.7 `CONFIG_BUZZER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_OFF"></a>

## 361.8 `CONFIG_BUZZER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BUZZER_LOG_LEVEL_WRN"></a>

## 361.9 `CONFIG_BUZZER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BUZZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蜂鸣器驱动（Buzzer Drivers）［实验性，EXPERIMENTAL］ → 蜂鸣器（buzzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_BUZZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_CHOICE"></a>

## 361.10 `CONFIG_CACHE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CACHE
```

**默认值（Defaults）**

```text
CONFIG_CACHE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CACHE_LOG_LEVEL_OFF
CONFIG_CACHE_LOG_LEVEL_ERR
CONFIG_CACHE_LOG_LEVEL_WRN
CONFIG_CACHE_LOG_LEVEL_INF
CONFIG_CACHE_LOG_LEVEL_DBG
CONFIG_CACHE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_DEFAULT)、[`CONFIG_CACHE_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_OFF)、[`CONFIG_CACHE_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_ERR)、[`CONFIG_CACHE_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_WRN)、[`CONFIG_CACHE_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_INF)、[`CONFIG_CACHE_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_DBG)。

<a id="CONFIG_CACHE_LOG_LEVEL_DBG"></a>

## 361.11 `CONFIG_CACHE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_DEFAULT"></a>

## 361.12 `CONFIG_CACHE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_ERR"></a>

## 361.13 `CONFIG_CACHE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_INF"></a>

## 361.14 `CONFIG_CACHE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_OFF"></a>

## 361.15 `CONFIG_CACHE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CACHE_LOG_LEVEL_WRN"></a>

## 361.16 `CONFIG_CACHE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → 缓存（cache）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_CHOICE"></a>

## 361.17 `CONFIG_CAN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CAN
```

**默认值（Defaults）**

```text
CONFIG_CAN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CAN_LOG_LEVEL_OFF
CONFIG_CAN_LOG_LEVEL_ERR
CONFIG_CAN_LOG_LEVEL_WRN
CONFIG_CAN_LOG_LEVEL_INF
CONFIG_CAN_LOG_LEVEL_DBG
CONFIG_CAN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_DEFAULT)、[`CONFIG_CAN_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_OFF)、[`CONFIG_CAN_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_ERR)、[`CONFIG_CAN_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_WRN)、[`CONFIG_CAN_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_INF)、[`CONFIG_CAN_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_DBG)。

<a id="CONFIG_CAN_LOG_LEVEL_DBG"></a>

## 361.18 `CONFIG_CAN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_DEFAULT"></a>

## 361.19 `CONFIG_CAN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_ERR"></a>

## 361.20 `CONFIG_CAN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_INF"></a>

## 361.21 `CONFIG_CAN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_OFF"></a>

## 361.22 `CONFIG_CAN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CAN_LOG_LEVEL_WRN"></a>

## 361.23 `CONFIG_CAN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 控制器局域网（CAN）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE"></a>

## 361.24 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_OFF
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_ERR
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_WRN
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_INF
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DBG
CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_OFF)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_ERR)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_WRN)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_INF)、[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DBG)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DBG"></a>

## 361.25 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT"></a>

## 361.26 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_ERR"></a>

## 361.27 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_INF"></a>

## 361.28 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_OFF"></a>

## 361.29 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_WRN"></a>

## 361.30 `CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 操作系统支持库（OS Support Library） → cbprintf 数据打包（cbprintf_package）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CBPRINTF_PACKAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_CHOICE"></a>

## 361.31 `CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CLOCK_CONTROL_TI_CDCE9XX && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CDCE9XX_LOG_LEVEL_OFF
CONFIG_CDCE9XX_LOG_LEVEL_ERR
CONFIG_CDCE9XX_LOG_LEVEL_WRN
CONFIG_CDCE9XX_LOG_LEVEL_INF
CONFIG_CDCE9XX_LOG_LEVEL_DBG
CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CLOCK_CONTROL_TI_CDCE9XX`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_TI_CDCE9XX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT)、[`CONFIG_CDCE9XX_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_OFF)、[`CONFIG_CDCE9XX_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_ERR)、[`CONFIG_CDCE9XX_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_WRN)、[`CONFIG_CDCE9XX_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_INF)、[`CONFIG_CDCE9XX_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_DBG)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_DBG"></a>

## 361.32 `CONFIG_CDCE9XX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT"></a>

## 361.33 `CONFIG_CDCE9XX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_ERR"></a>

## 361.34 `CONFIG_CDCE9XX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_INF"></a>

## 361.35 `CONFIG_CDCE9XX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_OFF"></a>

## 361.36 `CONFIG_CDCE9XX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CDCE9XX_LOG_LEVEL_WRN"></a>

## 361.37 `CONFIG_CDCE9XX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CDCE9XX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator） → CDCE9XX 时钟控制（CDCE9XX clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CDCE9XX_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CDCE9XX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_CHOICE"></a>

## 361.38 `CONFIG_CFB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CHARACTER_FRAMEBUFFER
```

**默认值（Defaults）**

```text
CONFIG_CFB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CFB_LOG_LEVEL_OFF
CONFIG_CFB_LOG_LEVEL_ERR
CONFIG_CFB_LOG_LEVEL_WRN
CONFIG_CFB_LOG_LEVEL_INF
CONFIG_CFB_LOG_LEVEL_DBG
CONFIG_CFB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CHARACTER_FRAMEBUFFER`](P343_subsys_fb_配置项参考.md#CONFIG_CHARACTER_FRAMEBUFFER)、[`CONFIG_CFB_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_DEFAULT)、[`CONFIG_CFB_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_OFF)、[`CONFIG_CFB_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_ERR)、[`CONFIG_CFB_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_WRN)、[`CONFIG_CFB_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_INF)、[`CONFIG_CFB_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_DBG)。

<a id="CONFIG_CFB_LOG_LEVEL_DBG"></a>

## 361.39 `CONFIG_CFB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_DEFAULT"></a>

## 361.40 `CONFIG_CFB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_ERR"></a>

## 361.41 `CONFIG_CFB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_INF"></a>

## 361.42 `CONFIG_CFB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_OFF"></a>

## 361.43 `CONFIG_CFB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CFB_LOG_LEVEL_WRN"></a>

## 361.44 `CONFIG_CFB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CFB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays） → 字符帧缓冲区（cfb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CFB_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CFB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_CHOICE"></a>

## 361.45 `CONFIG_CHARGER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
CONFIG_CHARGER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CHARGER_LOG_LEVEL_OFF
CONFIG_CHARGER_LOG_LEVEL_ERR
CONFIG_CHARGER_LOG_LEVEL_WRN
CONFIG_CHARGER_LOG_LEVEL_INF
CONFIG_CHARGER_LOG_LEVEL_DBG
CONFIG_CHARGER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_CHARGER_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_DEFAULT)、[`CONFIG_CHARGER_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_OFF)、[`CONFIG_CHARGER_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_ERR)、[`CONFIG_CHARGER_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_WRN)、[`CONFIG_CHARGER_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_INF)、[`CONFIG_CHARGER_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_DBG)。

<a id="CONFIG_CHARGER_LOG_LEVEL_DBG"></a>

## 361.46 `CONFIG_CHARGER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_DEFAULT"></a>

## 361.47 `CONFIG_CHARGER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_ERR"></a>

## 361.48 `CONFIG_CHARGER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_INF"></a>

## 361.49 `CONFIG_CHARGER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_OFF"></a>

## 361.50 `CONFIG_CHARGER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CHARGER_LOG_LEVEL_WRN"></a>

## 361.51 `CONFIG_CHARGER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CHARGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 充电器（charger）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CHARGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE"></a>

## 361.52 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CLOCK_CONTROL_LOG_LEVEL_OFF
CONFIG_CLOCK_CONTROL_LOG_LEVEL_ERR
CONFIG_CLOCK_CONTROL_LOG_LEVEL_WRN
CONFIG_CLOCK_CONTROL_LOG_LEVEL_INF
CONFIG_CLOCK_CONTROL_LOG_LEVEL_DBG
CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_OFF)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_ERR)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_WRN)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_INF)、[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_DBG)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_DBG"></a>

## 361.53 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT"></a>

## 361.54 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_ERR"></a>

## 361.55 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_INF"></a>

## 361.56 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_OFF"></a>

## 361.57 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_CONTROL_LOG_LEVEL_WRN"></a>

## 361.58 `CONFIG_CLOCK_CONTROL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 时钟控制（clock control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_CONTROL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE"></a>

## 361.59 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CLOCK_MONITOR_LOG_LEVEL_OFF
CONFIG_CLOCK_MONITOR_LOG_LEVEL_ERR
CONFIG_CLOCK_MONITOR_LOG_LEVEL_WRN
CONFIG_CLOCK_MONITOR_LOG_LEVEL_INF
CONFIG_CLOCK_MONITOR_LOG_LEVEL_DBG
CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_OFF)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_ERR)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_WRN)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_INF)、[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_DBG)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_DBG"></a>

## 361.60 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT"></a>

## 361.61 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_ERR"></a>

## 361.62 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_INF"></a>

## 361.63 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_OFF"></a>

## 361.64 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CLOCK_MONITOR_LOG_LEVEL_WRN"></a>

## 361.65 `CONFIG_CLOCK_MONITOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers） → 时钟监控（clock_monitor）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CLOCK_MONITOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_CHOICE"></a>

## 361.66 `CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_COMPARATOR_LOG_LEVEL_OFF
CONFIG_COMPARATOR_LOG_LEVEL_ERR
CONFIG_COMPARATOR_LOG_LEVEL_WRN
CONFIG_COMPARATOR_LOG_LEVEL_INF
CONFIG_COMPARATOR_LOG_LEVEL_DBG
CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT)、[`CONFIG_COMPARATOR_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_OFF)、[`CONFIG_COMPARATOR_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_ERR)、[`CONFIG_COMPARATOR_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_WRN)、[`CONFIG_COMPARATOR_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_INF)、[`CONFIG_COMPARATOR_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_DBG)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_DBG"></a>

## 361.67 `CONFIG_COMPARATOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT"></a>

## 361.68 `CONFIG_COMPARATOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_ERR"></a>

## 361.69 `CONFIG_COMPARATOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_INF"></a>

## 361.70 `CONFIG_COMPARATOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_OFF"></a>

## 361.71 `CONFIG_COMPARATOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COMPARATOR_LOG_LEVEL_WRN"></a>

## 361.72 `CONFIG_COMPARATOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPARATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器（comparator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COMPARATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE"></a>

## 361.73 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_COREDUMP_DEVICE
```

**默认值（Defaults）**

```text
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_OFF
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_ERR
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_WRN
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_INF
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DBG
CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_COREDUMP_DEVICE`](P067_drivers_coredump_配置项参考.md#CONFIG_COREDUMP_DEVICE)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_OFF)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_ERR)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_WRN)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_INF)、[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DBG"></a>

## 361.74 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT"></a>

## 361.75 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_ERR"></a>

## 361.76 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_INF"></a>

## 361.77 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_OFF"></a>

## 361.78 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COREDUMP_DEVICE_LOG_LEVEL_WRN"></a>

## 361.79 `CONFIG_COREDUMP_DEVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 核心转储伪设备驱动（Coredump Pseudo-Device Drivers） → 核心转储设备（coredump device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COREDUMP_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_CHOICE"></a>

## 361.80 `CONFIG_COUNTER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
CONFIG_COUNTER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_COUNTER_LOG_LEVEL_OFF
CONFIG_COUNTER_LOG_LEVEL_ERR
CONFIG_COUNTER_LOG_LEVEL_WRN
CONFIG_COUNTER_LOG_LEVEL_INF
CONFIG_COUNTER_LOG_LEVEL_DBG
CONFIG_COUNTER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_DEFAULT)、[`CONFIG_COUNTER_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_OFF)、[`CONFIG_COUNTER_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_ERR)、[`CONFIG_COUNTER_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_WRN)、[`CONFIG_COUNTER_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_INF)、[`CONFIG_COUNTER_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_DBG)。

<a id="CONFIG_COUNTER_LOG_LEVEL_DBG"></a>

## 361.81 `CONFIG_COUNTER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_DEFAULT"></a>

## 361.82 `CONFIG_COUNTER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_ERR"></a>

## 361.83 `CONFIG_COUNTER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_INF"></a>

## 361.84 `CONFIG_COUNTER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_OFF"></a>

## 361.85 `CONFIG_COUNTER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_LOG_LEVEL_WRN"></a>

## 361.86 `CONFIG_COUNTER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → 计数器（counter）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE"></a>

## 361.87 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_COUNTER_XLNX_TTC && CONFIG_COUNTER
```

**默认值（Defaults）**

```text
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_OFF
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_ERR
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_WRN
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_INF
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DBG
CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_COUNTER_XLNX_TTC`](P069_drivers_counter_配置项参考_2.md#CONFIG_COUNTER_XLNX_TTC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_OFF)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_ERR)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_WRN)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_INF)、[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DBG)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DBG"></a>

## 361.88 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT"></a>

## 361.89 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_ERR"></a>

## 361.90 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_INF"></a>

## 361.91 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_OFF"></a>

## 361.92 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_WRN"></a>

## 361.93 `CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 计数器驱动（Counter Drivers） → Xilinx 三重定时器计数器驱动（Triple Timer Counter，TTC） → TTC 计数器（ttc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_COUNTER_XLNX_TTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE"></a>

## 361.94 `CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_CPU_FREQ_LOG_LEVEL_OFF
CONFIG_CPU_FREQ_LOG_LEVEL_ERR
CONFIG_CPU_FREQ_LOG_LEVEL_WRN
CONFIG_CPU_FREQ_LOG_LEVEL_INF
CONFIG_CPU_FREQ_LOG_LEVEL_DBG
CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)、[`CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT)、[`CONFIG_CPU_FREQ_LOG_LEVEL_OFF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_OFF)、[`CONFIG_CPU_FREQ_LOG_LEVEL_ERR`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_ERR)、[`CONFIG_CPU_FREQ_LOG_LEVEL_WRN`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_WRN)、[`CONFIG_CPU_FREQ_LOG_LEVEL_INF`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_INF)、[`CONFIG_CPU_FREQ_LOG_LEVEL_DBG`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_DBG)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_DBG"></a>

## 361.95 `CONFIG_CPU_FREQ_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT"></a>

## 361.96 `CONFIG_CPU_FREQ_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_ERR"></a>

## 361.97 `CONFIG_CPU_FREQ_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_INF"></a>

## 361.98 `CONFIG_CPU_FREQ_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_OFF"></a>

## 361.99 `CONFIG_CPU_FREQ_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_CPU_FREQ_LOG_LEVEL_WRN"></a>

## 361.100 `CONFIG_CPU_FREQ_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整（CPU Frequency Scaling）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE`](P361_subsys_logging_配置项参考_10.md#CONFIG_CPU_FREQ_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P360_subsys_logging_配置项参考_9.md) · [返回大纲](大纲.md) · [下一章](P362_subsys_logging_配置项参考_11.md)
