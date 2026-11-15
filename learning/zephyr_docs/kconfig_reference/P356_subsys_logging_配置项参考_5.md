---
id: learning.zephyr-docs.kconfig-reference.page-356
title: "`subsys/logging`配置项参考（5/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第356章\_`subsys/logging`配置项参考（5/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_ETS_LOG_LEVEL_ERR"></a>

## 356.1 `CONFIG_BT_ETS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ETS_LOG_LEVEL_INF"></a>

## 356.2 `CONFIG_BT_ETS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ETS_LOG_LEVEL_OFF"></a>

## 356.3 `CONFIG_BT_ETS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ETS_LOG_LEVEL_WRN"></a>

## 356.4 `CONFIG_BT_ETS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_CHOICE"></a>

## 356.5 `CONFIG_BT_GATT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_GATT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_GATT_LOG_LEVEL_INHERIT
CONFIG_BT_GATT_LOG_LEVEL_OFF
CONFIG_BT_GATT_LOG_LEVEL_ERR
CONFIG_BT_GATT_LOG_LEVEL_WRN
CONFIG_BT_GATT_LOG_LEVEL_INF
CONFIG_BT_GATT_LOG_LEVEL_DBG
CONFIG_BT_GATT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GATT_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_GATT_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_GATT_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_OFF)、[`CONFIG_BT_GATT_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_ERR)、[`CONFIG_BT_GATT_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_WRN)、[`CONFIG_BT_GATT_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_INF)、[`CONFIG_BT_GATT_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_GATT_LOG_LEVEL_DBG"></a>

## 356.6 `CONFIG_BT_GATT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_DEFAULT"></a>

## 356.7 `CONFIG_BT_GATT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_ERR"></a>

## 356.8 `CONFIG_BT_GATT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_INF"></a>

## 356.9 `CONFIG_BT_GATT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_INHERIT"></a>

## 356.10 `CONFIG_BT_GATT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_GATT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_OFF"></a>

## 356.11 `CONFIG_BT_GATT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GATT_LOG_LEVEL_WRN"></a>

## 356.12 `CONFIG_BT_GATT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GATT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙通用属性配置文件（Bluetooth Generic Attribute Profile (GATT)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GATT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_CHOICE"></a>

## 356.13 `CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_GMAP_LOG_LEVEL_INHERIT
CONFIG_BT_GMAP_LOG_LEVEL_OFF
CONFIG_BT_GMAP_LOG_LEVEL_ERR
CONFIG_BT_GMAP_LOG_LEVEL_WRN
CONFIG_BT_GMAP_LOG_LEVEL_INF
CONFIG_BT_GMAP_LOG_LEVEL_DBG
CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_GMAP_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_GMAP_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_OFF)、[`CONFIG_BT_GMAP_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_ERR)、[`CONFIG_BT_GMAP_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_WRN)、[`CONFIG_BT_GMAP_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_INF)、[`CONFIG_BT_GMAP_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_DBG"></a>

## 356.14 `CONFIG_BT_GMAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT"></a>

## 356.15 `CONFIG_BT_GMAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_ERR"></a>

## 356.16 `CONFIG_BT_GMAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_INF"></a>

## 356.17 `CONFIG_BT_GMAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_INHERIT"></a>

## 356.18 `CONFIG_BT_GMAP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 选择项（Choice）：`BT_GMAP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_OFF"></a>

## 356.19 `CONFIG_BT_GMAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GMAP_LOG_LEVEL_WRN"></a>

## 356.20 `CONFIG_BT_GMAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GMAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GMAP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GMAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_CHOICE"></a>

## 356.21 `CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_GOEP_LOG_LEVEL_INHERIT
CONFIG_BT_GOEP_LOG_LEVEL_OFF
CONFIG_BT_GOEP_LOG_LEVEL_ERR
CONFIG_BT_GOEP_LOG_LEVEL_WRN
CONFIG_BT_GOEP_LOG_LEVEL_INF
CONFIG_BT_GOEP_LOG_LEVEL_DBG
CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_GOEP_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_GOEP_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_OFF)、[`CONFIG_BT_GOEP_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_ERR)、[`CONFIG_BT_GOEP_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_WRN)、[`CONFIG_BT_GOEP_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_INF)、[`CONFIG_BT_GOEP_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_DBG"></a>

## 356.22 `CONFIG_BT_GOEP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT"></a>

## 356.23 `CONFIG_BT_GOEP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_ERR"></a>

## 356.24 `CONFIG_BT_GOEP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_INF"></a>

## 356.25 `CONFIG_BT_GOEP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_INHERIT"></a>

## 356.26 `CONFIG_BT_GOEP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_GOEP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_OFF"></a>

## 356.27 `CONFIG_BT_GOEP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_GOEP_LOG_LEVEL_WRN"></a>

## 356.28 `CONFIG_BT_GOEP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_GOEP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙通用对象交换配置文件（Bluetooth Generic Object Exchange Profile (GOEP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_GOEP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 356.29 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HAS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HAS_CLIENT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DBG"></a>

## 356.30 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 356.31 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_ERR"></a>

## 356.32 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INF"></a>

## 356.33 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 356.34 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_HAS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_OFF"></a>

## 356.35 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_CLIENT_LOG_LEVEL_WRN"></a>

## 356.36 `CONFIG_BT_HAS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务客户端（Hearing Access Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_CHOICE"></a>

## 356.37 `CONFIG_BT_HAS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HAS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HAS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HAS_LOG_LEVEL_INHERIT
CONFIG_BT_HAS_LOG_LEVEL_OFF
CONFIG_BT_HAS_LOG_LEVEL_ERR
CONFIG_BT_HAS_LOG_LEVEL_WRN
CONFIG_BT_HAS_LOG_LEVEL_INF
CONFIG_BT_HAS_LOG_LEVEL_DBG
CONFIG_BT_HAS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HAS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HAS_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HAS_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HAS_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_OFF)、[`CONFIG_BT_HAS_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_ERR)、[`CONFIG_BT_HAS_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_WRN)、[`CONFIG_BT_HAS_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_INF)、[`CONFIG_BT_HAS_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HAS_LOG_LEVEL_DBG"></a>

## 356.38 `CONFIG_BT_HAS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_DEFAULT"></a>

## 356.39 `CONFIG_BT_HAS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_ERR"></a>

## 356.40 `CONFIG_BT_HAS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_INF"></a>

## 356.41 `CONFIG_BT_HAS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_INHERIT"></a>

## 356.42 `CONFIG_BT_HAS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_HAS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_OFF"></a>

## 356.43 `CONFIG_BT_HAS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HAS_LOG_LEVEL_WRN"></a>

## 356.44 `CONFIG_BT_HAS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 助听接入服务（Hearing Access Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE"></a>

## 356.45 `CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HCI_CORE_LOG_LEVEL_INHERIT
CONFIG_BT_HCI_CORE_LOG_LEVEL_OFF
CONFIG_BT_HCI_CORE_LOG_LEVEL_ERR
CONFIG_BT_HCI_CORE_LOG_LEVEL_WRN
CONFIG_BT_HCI_CORE_LOG_LEVEL_INF
CONFIG_BT_HCI_CORE_LOG_LEVEL_DBG
CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_OFF)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_ERR)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_WRN)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_INF)、[`CONFIG_BT_HCI_CORE_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_DBG"></a>

## 356.46 `CONFIG_BT_HCI_CORE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT"></a>

## 356.47 `CONFIG_BT_HCI_CORE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_ERR"></a>

## 356.48 `CONFIG_BT_HCI_CORE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_INF"></a>

## 356.49 `CONFIG_BT_HCI_CORE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_INHERIT"></a>

## 356.50 `CONFIG_BT_HCI_CORE_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_HCI_CORE_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_OFF"></a>

## 356.51 `CONFIG_BT_HCI_CORE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_CORE_LOG_LEVEL_WRN"></a>

## 356.52 `CONFIG_BT_HCI_CORE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙主机控制器接口核心（Bluetooth HCI core）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE"></a>

## 356.53 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INHERIT
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_OFF
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_ERR
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_WRN
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INF
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DBG
CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INF)、[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DBG"></a>

## 356.54 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 356.55 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_ERR"></a>

## 356.56 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INF"></a>

## 356.57 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INHERIT"></a>

## 356.58 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 选择项（Choice）：`BT_HCI_DRIVER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_OFF"></a>

## 356.59 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HCI_DRIVER_LOG_LEVEL_WRN"></a>

## 356.60 `CONFIG_BT_HCI_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 公共部分（Common） → 蓝牙主机控制器接口驱动（Bluetooth HCI driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HCI_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE"></a>

## 356.61 `CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HFP_AG_LOG_LEVEL_INHERIT
CONFIG_BT_HFP_AG_LOG_LEVEL_OFF
CONFIG_BT_HFP_AG_LOG_LEVEL_ERR
CONFIG_BT_HFP_AG_LOG_LEVEL_WRN
CONFIG_BT_HFP_AG_LOG_LEVEL_INF
CONFIG_BT_HFP_AG_LOG_LEVEL_DBG
CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_OFF)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_ERR)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_WRN)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_INF)、[`CONFIG_BT_HFP_AG_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_DBG"></a>

## 356.62 `CONFIG_BT_HFP_AG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT"></a>

## 356.63 `CONFIG_BT_HFP_AG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_ERR"></a>

## 356.64 `CONFIG_BT_HFP_AG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_INF"></a>

## 356.65 `CONFIG_BT_HFP_AG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_INHERIT"></a>

## 356.66 `CONFIG_BT_HFP_AG_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_HFP_AG_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_OFF"></a>

## 356.67 `CONFIG_BT_HFP_AG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_AG_LOG_LEVEL_WRN"></a>

## 356.68 `CONFIG_BT_HFP_AG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提音频网关配置文件（Bluetooth Hands Free Audio Gateway Profile (HFP AG)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_AG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE"></a>

## 356.69 `CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HFP_HF_LOG_LEVEL_INHERIT
CONFIG_BT_HFP_HF_LOG_LEVEL_OFF
CONFIG_BT_HFP_HF_LOG_LEVEL_ERR
CONFIG_BT_HFP_HF_LOG_LEVEL_WRN
CONFIG_BT_HFP_HF_LOG_LEVEL_INF
CONFIG_BT_HFP_HF_LOG_LEVEL_DBG
CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_OFF)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_ERR)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_WRN)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_INF)、[`CONFIG_BT_HFP_HF_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_DBG"></a>

## 356.70 `CONFIG_BT_HFP_HF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT"></a>

## 356.71 `CONFIG_BT_HFP_HF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_ERR"></a>

## 356.72 `CONFIG_BT_HFP_HF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_INF"></a>

## 356.73 `CONFIG_BT_HFP_HF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_INHERIT"></a>

## 356.74 `CONFIG_BT_HFP_HF_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_HFP_HF_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_OFF"></a>

## 356.75 `CONFIG_BT_HFP_HF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HFP_HF_LOG_LEVEL_WRN"></a>

## 356.76 `CONFIG_BT_HFP_HF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙免提配置文件（Bluetooth Hands Free Profile (HFP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HFP_HF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE"></a>

## 356.77 `CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HID_HOST_LOG_LEVEL_INHERIT
CONFIG_BT_HID_HOST_LOG_LEVEL_OFF
CONFIG_BT_HID_HOST_LOG_LEVEL_ERR
CONFIG_BT_HID_HOST_LOG_LEVEL_WRN
CONFIG_BT_HID_HOST_LOG_LEVEL_INF
CONFIG_BT_HID_HOST_LOG_LEVEL_DBG
CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_INHERIT)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_OFF)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_ERR)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_WRN)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_INF)、[`CONFIG_BT_HID_HOST_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_DBG"></a>

## 356.78 `CONFIG_BT_HID_HOST_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT"></a>

## 356.79 `CONFIG_BT_HID_HOST_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_ERR"></a>

## 356.80 `CONFIG_BT_HID_HOST_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_INF"></a>

## 356.81 `CONFIG_BT_HID_HOST_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_INHERIT"></a>

## 356.82 `CONFIG_BT_HID_HOST_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_HID_HOST_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_OFF"></a>

## 356.83 `CONFIG_BT_HID_HOST_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HID_HOST_LOG_LEVEL_WRN"></a>

## 356.84 `CONFIG_BT_HID_HOST_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙人机接口设备主机（Bluetooth Human Interface Device Host (HID Host)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HID_HOST_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_CHOICE"></a>

## 356.85 `CONFIG_BT_HRS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HRS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_HRS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_HRS_LOG_LEVEL_OFF
CONFIG_BT_HRS_LOG_LEVEL_ERR
CONFIG_BT_HRS_LOG_LEVEL_WRN
CONFIG_BT_HRS_LOG_LEVEL_INF
CONFIG_BT_HRS_LOG_LEVEL_DBG
CONFIG_BT_HRS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HRS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HRS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HRS_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_HRS_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_OFF)、[`CONFIG_BT_HRS_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_ERR)、[`CONFIG_BT_HRS_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_WRN)、[`CONFIG_BT_HRS_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_INF)、[`CONFIG_BT_HRS_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_HRS_LOG_LEVEL_DBG"></a>

## 356.86 `CONFIG_BT_HRS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_DEFAULT"></a>

## 356.87 `CONFIG_BT_HRS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_ERR"></a>

## 356.88 `CONFIG_BT_HRS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_INF"></a>

## 356.89 `CONFIG_BT_HRS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_OFF"></a>

## 356.90 `CONFIG_BT_HRS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_HRS_LOG_LEVEL_WRN"></a>

## 356.91 `CONFIG_BT_HRS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_HRS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 心率服务（HRS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_HRS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_HRS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 356.92 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_IAS_CLIENT && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_IAS_CLIENT`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS_CLIENT)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INHERIT`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DBG`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DBG"></a>

## 356.93 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 356.94 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_ERR"></a>

## 356.95 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INF"></a>

## 356.96 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INHERIT"></a>

## 356.97 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 选择项（Choice）：`BT_IAS_CLIENT_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_OFF"></a>

## 356.98 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_CLIENT_LOG_LEVEL_WRN"></a>

## 356.99 `CONFIG_BT_IAS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务客户端（Immediate Alert Service Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_CHOICE"></a>

## 356.100 `CONFIG_BT_IAS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_IAS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_IAS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_IAS_LOG_LEVEL_OFF
CONFIG_BT_IAS_LOG_LEVEL_ERR
CONFIG_BT_IAS_LOG_LEVEL_WRN
CONFIG_BT_IAS_LOG_LEVEL_INF
CONFIG_BT_IAS_LOG_LEVEL_DBG
CONFIG_BT_IAS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_IAS`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_IAS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_IAS_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_IAS_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_OFF)、[`CONFIG_BT_IAS_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_ERR)、[`CONFIG_BT_IAS_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_WRN)、[`CONFIG_BT_IAS_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_INF)、[`CONFIG_BT_IAS_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_IAS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<!-- kconfig-navigation -->

[上一章](P355_subsys_logging_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P357_subsys_logging_配置项参考_6.md)
