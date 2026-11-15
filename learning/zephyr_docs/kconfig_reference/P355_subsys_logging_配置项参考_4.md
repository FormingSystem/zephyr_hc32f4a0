---
id: learning.zephyr-docs.kconfig-reference.page-355
title: "`subsys/logging`配置项参考（4/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第355章\_`subsys/logging`配置项参考（4/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INF"></a>

## 355.1 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INHERIT"></a>

## 355.2 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_OFF"></a>

## 355.3 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_WRN"></a>

## 355.4 `CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件发起方（Common Audio Profile Initiator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE`](P354_subsys_logging_配置项参考_3.md#CONFIG_BT_CAP_INITIATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE"></a>

## 355.5 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CAP && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CAP_STREAM_LOG_LEVEL_INHERIT
CONFIG_BT_CAP_STREAM_LOG_LEVEL_OFF
CONFIG_BT_CAP_STREAM_LOG_LEVEL_ERR
CONFIG_BT_CAP_STREAM_LOG_LEVEL_WRN
CONFIG_BT_CAP_STREAM_LOG_LEVEL_INF
CONFIG_BT_CAP_STREAM_LOG_LEVEL_DBG
CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_OFF)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_ERR)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_WRN)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_INF)、[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CAP`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_DBG"></a>

## 355.6 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT"></a>

## 355.7 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_ERR"></a>

## 355.8 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_INF"></a>

## 355.9 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_INHERIT"></a>

## 355.10 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CAP_STREAM_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_OFF"></a>

## 355.11 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CAP_STREAM_LOG_LEVEL_WRN"></a>

## 355.12 `CONFIG_BT_CAP_STREAM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 通用音频配置文件音频流（Common Audio Profile Stream）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CAP_STREAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE"></a>

## 355.13 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CCP_CALL_CONTROL_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_INF
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DBG"></a>

## 355.14 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 355.15 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_ERR"></a>

## 355.16 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_INF"></a>

## 355.17 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_OFF"></a>

## 355.18 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_WRN"></a>

## 355.19 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件客户端支持（Call Control Profile Client Support） → 呼叫控制配置文件客户端（Call Control Profile Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE"></a>

## 355.20 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CCP_CALL_CONTROL_SERVER && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_OFF
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_ERR
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_WRN
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_INF
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DBG
CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_OFF)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_ERR)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_WRN)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_INF)、[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DBG"></a>

## 355.21 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT"></a>

## 355.22 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_ERR"></a>

## 355.23 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_INF"></a>

## 355.24 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_OFF"></a>

## 355.25 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_WRN"></a>

## 355.26 `CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 呼叫控制配置文件呼叫控制服务器支持（Call Control Profile Call Control Server Support） → 呼叫控制配置文件的呼叫控制服务器（Call Control Profile Call Control Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CCP_CALL_CONTROL_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_CHOICE"></a>

## 355.27 `CONFIG_BT_CONN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CONN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CONN_LOG_LEVEL_INHERIT
CONFIG_BT_CONN_LOG_LEVEL_OFF
CONFIG_BT_CONN_LOG_LEVEL_ERR
CONFIG_BT_CONN_LOG_LEVEL_WRN
CONFIG_BT_CONN_LOG_LEVEL_INF
CONFIG_BT_CONN_LOG_LEVEL_DBG
CONFIG_BT_CONN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CONN_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CONN_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_OFF)、[`CONFIG_BT_CONN_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_ERR)、[`CONFIG_BT_CONN_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_WRN)、[`CONFIG_BT_CONN_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_INF)、[`CONFIG_BT_CONN_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CONN_LOG_LEVEL_DBG"></a>

## 355.28 `CONFIG_BT_CONN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_DEFAULT"></a>

## 355.29 `CONFIG_BT_CONN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_ERR"></a>

## 355.30 `CONFIG_BT_CONN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_INF"></a>

## 355.31 `CONFIG_BT_CONN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_INHERIT"></a>

## 355.32 `CONFIG_BT_CONN_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_CONN_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_OFF"></a>

## 355.33 `CONFIG_BT_CONN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CONN_LOG_LEVEL_WRN"></a>

## 355.34 `CONFIG_BT_CONN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙连接（Bluetooth connection）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE"></a>

## 355.35 `CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CRYPTO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CRYPTO_LOG_LEVEL_INHERIT
CONFIG_BT_CRYPTO_LOG_LEVEL_OFF
CONFIG_BT_CRYPTO_LOG_LEVEL_ERR
CONFIG_BT_CRYPTO_LOG_LEVEL_WRN
CONFIG_BT_CRYPTO_LOG_LEVEL_INF
CONFIG_BT_CRYPTO_LOG_LEVEL_DBG
CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CRYPTO`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CRYPTO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_OFF)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_ERR)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_WRN)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_INF)、[`CONFIG_BT_CRYPTO_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_DBG"></a>

## 355.36 `CONFIG_BT_CRYPTO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT"></a>

## 355.37 `CONFIG_BT_CRYPTO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_ERR"></a>

## 355.38 `CONFIG_BT_CRYPTO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_INF"></a>

## 355.39 `CONFIG_BT_CRYPTO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_INHERIT"></a>

## 355.40 `CONFIG_BT_CRYPTO_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 选择项（Choice）：`BT_CRYPTO_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_OFF"></a>

## 355.41 `CONFIG_BT_CRYPTO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CRYPTO_LOG_LEVEL_WRN"></a>

## 355.42 `CONFIG_BT_CRYPTO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙密码工具箱（Bluetooth Cryptographic Toolbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE"></a>

## 355.43 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`

**提示（Prompt）**：协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CSIP_SET_COORDINATOR && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INHERIT
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_OFF
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_ERR
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_WRN
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INF
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG
CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CSIP_SET_COORDINATOR`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_COORDINATOR)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_OFF)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_ERR)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_WRN)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INF)、[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG"></a>

## 355.44 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT"></a>

## 355.45 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_ERR"></a>

## 355.46 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INF"></a>

## 355.47 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INHERIT"></a>

## 355.48 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_OFF"></a>

## 355.49 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_WRN"></a>

## 355.50 `CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的集合协调器（Coordinated Set Identification Profile Set Coordinator）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE"></a>

## 355.51 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AUDIO && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INHERIT
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_OFF
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_ERR
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_WRN
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INF
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DBG
CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_OFF)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_ERR)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_WRN)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INF)、[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DBG"></a>

## 355.52 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT"></a>

## 355.53 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_ERR"></a>

## 355.54 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INF"></a>

## 355.55 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INHERIT"></a>

## 355.56 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_OFF"></a>

## 355.57 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_WRN"></a>

## 355.58 `CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识配置文件的密码函数（Coordinated Set Identification Profile crypto functions）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE"></a>

## 355.59 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CSIP_SET_MEMBER && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INHERIT
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_OFF
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_ERR
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_WRN
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INF
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DBG
CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CSIP_SET_MEMBER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CSIP_SET_MEMBER)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_OFF)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_ERR)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_WRN)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INF)、[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DBG"></a>

## 355.60 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT"></a>

## 355.61 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_ERR"></a>

## 355.62 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INF"></a>

## 355.63 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INHERIT"></a>

## 355.64 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_OFF"></a>

## 355.65 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_WRN"></a>

## 355.66 `CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 协调集标识服务（Coordinated Set Identification Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CSIP_SET_MEMBER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE"></a>

## 355.67 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INHERIT
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_OFF
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_ERR
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_WRN
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INF
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DBG
CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INHERIT)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_OFF)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_ERR)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_WRN)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INF)、[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DBG"></a>

## 355.68 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT"></a>

## 355.69 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_ERR"></a>

## 355.70 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INF"></a>

## 355.71 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INHERIT"></a>

## 355.72 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 选择项（Choice）：`BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_OFF"></a>

## 355.73 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_WRN"></a>

## 355.74 `CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙控制器等时适配层（Bluetooth Controller ISO-AL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTLR_ISOAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_CHOICE"></a>

## 355.75 `CONFIG_BT_CTS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CTS && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_CTS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_CTS_LOG_LEVEL_OFF
CONFIG_BT_CTS_LOG_LEVEL_ERR
CONFIG_BT_CTS_LOG_LEVEL_WRN
CONFIG_BT_CTS_LOG_LEVEL_INF
CONFIG_BT_CTS_LOG_LEVEL_DBG
CONFIG_BT_CTS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CTS`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTS)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CTS_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_CTS_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_OFF)、[`CONFIG_BT_CTS_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_ERR)、[`CONFIG_BT_CTS_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_WRN)、[`CONFIG_BT_CTS_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_INF)、[`CONFIG_BT_CTS_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_CTS_LOG_LEVEL_DBG"></a>

## 355.76 `CONFIG_BT_CTS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_DEFAULT"></a>

## 355.77 `CONFIG_BT_CTS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_ERR"></a>

## 355.78 `CONFIG_BT_CTS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_INF"></a>

## 355.79 `CONFIG_BT_CTS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_OFF"></a>

## 355.80 `CONFIG_BT_CTS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_CTS_LOG_LEVEL_WRN"></a>

## 355.81 `CONFIG_BT_CTS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_CTS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 当前时间服务（CTS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_CTS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_CHOICE"></a>

## 355.82 `CONFIG_BT_DF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_DF && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_DF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_DF_LOG_LEVEL_INHERIT
CONFIG_BT_DF_LOG_LEVEL_OFF
CONFIG_BT_DF_LOG_LEVEL_ERR
CONFIG_BT_DF_LOG_LEVEL_WRN
CONFIG_BT_DF_LOG_LEVEL_INF
CONFIG_BT_DF_LOG_LEVEL_DBG
CONFIG_BT_DF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_DF`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DF)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_DF_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_DF_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_INHERIT)、[`CONFIG_BT_DF_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_OFF)、[`CONFIG_BT_DF_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_ERR)、[`CONFIG_BT_DF_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_WRN)、[`CONFIG_BT_DF_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_INF)、[`CONFIG_BT_DF_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_DF_LOG_LEVEL_DBG"></a>

## 355.83 `CONFIG_BT_DF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_DEFAULT"></a>

## 355.84 `CONFIG_BT_DF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_ERR"></a>

## 355.85 `CONFIG_BT_DF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_INF"></a>

## 355.86 `CONFIG_BT_DF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_INHERIT"></a>

## 355.87 `CONFIG_BT_DF_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_DF_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_OFF"></a>

## 355.88 `CONFIG_BT_DF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_DF_LOG_LEVEL_WRN"></a>

## 355.89 `CONFIG_BT_DF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_DF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙测向（Bluetooth Direction Finding）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_DF_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_DF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_CHOICE"></a>

## 355.90 `CONFIG_BT_EAD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_EAD && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_EAD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_EAD_LOG_LEVEL_INHERIT
CONFIG_BT_EAD_LOG_LEVEL_OFF
CONFIG_BT_EAD_LOG_LEVEL_ERR
CONFIG_BT_EAD_LOG_LEVEL_WRN
CONFIG_BT_EAD_LOG_LEVEL_INF
CONFIG_BT_EAD_LOG_LEVEL_DBG
CONFIG_BT_EAD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_EAD`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_EAD)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EAD_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_EAD_LOG_LEVEL_INHERIT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_INHERIT)、[`CONFIG_BT_EAD_LOG_LEVEL_OFF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_OFF)、[`CONFIG_BT_EAD_LOG_LEVEL_ERR`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_ERR)、[`CONFIG_BT_EAD_LOG_LEVEL_WRN`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_WRN)、[`CONFIG_BT_EAD_LOG_LEVEL_INF`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_INF)、[`CONFIG_BT_EAD_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_EAD_LOG_LEVEL_DBG"></a>

## 355.91 `CONFIG_BT_EAD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_DEFAULT"></a>

## 355.92 `CONFIG_BT_EAD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_ERR"></a>

## 355.93 `CONFIG_BT_EAD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_INF"></a>

## 355.94 `CONFIG_BT_EAD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_INHERIT"></a>

## 355.95 `CONFIG_BT_EAD_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 选择项（Choice）：`BT_EAD_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_OFF"></a>

## 355.96 `CONFIG_BT_EAD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_EAD_LOG_LEVEL_WRN"></a>

## 355.97 `CONFIG_BT_EAD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_EAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 库（Libraries） → 蓝牙加密广播数据（Bluetooth Encrypted Advertising Data）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_EAD_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_EAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ETS_LOG_LEVEL_CHOICE"></a>

## 355.98 `CONFIG_BT_ETS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_ETS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ETS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_ETS_LOG_LEVEL_OFF
CONFIG_BT_ETS_LOG_LEVEL_ERR
CONFIG_BT_ETS_LOG_LEVEL_WRN
CONFIG_BT_ETS_LOG_LEVEL_INF
CONFIG_BT_ETS_LOG_LEVEL_DBG
CONFIG_BT_ETS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_ETS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_ETS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ETS_LOG_LEVEL_DEFAULT`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_ETS_LOG_LEVEL_OFF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_ETS_LOG_LEVEL_OFF)、[`CONFIG_BT_ETS_LOG_LEVEL_ERR`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_ETS_LOG_LEVEL_ERR)、[`CONFIG_BT_ETS_LOG_LEVEL_WRN`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_ETS_LOG_LEVEL_WRN)、[`CONFIG_BT_ETS_LOG_LEVEL_INF`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_ETS_LOG_LEVEL_INF)、[`CONFIG_BT_ETS_LOG_LEVEL_DBG`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_ETS_LOG_LEVEL_DBG"></a>

## 355.99 `CONFIG_BT_ETS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ETS_LOG_LEVEL_DEFAULT"></a>

## 355.100 `CONFIG_BT_ETS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → GATT 经过时间服务（GATT Elapsed Time service）[实验性，EXPERIMENTAL] → 经过时间服务（ets）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ETS_LOG_LEVEL_CHOICE`](P355_subsys_logging_配置项参考_4.md#CONFIG_BT_ETS_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P354_subsys_logging_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P356_subsys_logging_配置项参考_5.md)
